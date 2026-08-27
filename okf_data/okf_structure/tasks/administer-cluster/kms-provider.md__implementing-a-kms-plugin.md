---
id: okf-structure/tasks/administer-cluster/kms-provider.md#implementing-a-kms-plugin
kind: section
title: Implementing a KMS plugin
source: tasks/administer-cluster/kms-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/
heading: Implementing a KMS plugin
parent: okf-structure/tasks/administer-cluster/kms-provider
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#configuring-the-kms-provider
next_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#encrypting-your-data-with-the-kms-provider
word_count: 1360
---

To implement a KMS plugin, you can develop a new plugin gRPC server or enable a KMS plugin
already provided by your cloud provider.
You then integrate the plugin with the remote KMS and deploy it on the Kubernetes control plane.

### Enabling the KMS supported by your cloud provider

Refer to your cloud provider for instructions on enabling the cloud provider-specific KMS plugin.

### Developing a KMS plugin gRPC server

You can develop a KMS plugin gRPC server using a stub file available for Go. For other languages,
you use a proto file to create a stub file that you can use to develop the gRPC server code.

#### KMS v1 {#developing-a-kms-plugin-gRPC-server-kms-v1}

* Using Go: Use the functions and data structures in the stub file:
  api.pb.go
  to develop the gRPC server code

* Using languages other than Go: Use the protoc compiler with the proto file:
  api.proto
  to generate a stub file for the specific language

#### KMS v2 {#developing-a-kms-plugin-gRPC-server-kms-v2}

* Using Go: A high level
  library
  is provided to make the process easier.  Low level implementations
  can use the functions and data structures in the stub file:
  api.pb.go
  to develop the gRPC server code

* Using languages other than Go: Use the protoc compiler with the proto file:
  api.proto
  to generate a stub file for the specific language

Then use the functions and data structures in the stub file to develop the server code.

#### Notes

##### KMS v1 {#developing-a-kms-plugin-gRPC-server-notes-kms-v1}

* kms plugin version: `v1beta1`

  In response to procedure call Version, a compatible KMS plugin should return `v1beta1` as `VersionResponse.version`.

* message version: `v1beta1`

  All messages from KMS provider have the version field set to `v1beta1`.

* protocol: UNIX domain socket (`unix`)

  The plugin is implemented as a gRPC server that listens at UNIX domain socket. The plugin deployment should create a file on the file system to run the gRPC unix domain socket connection. The API server (gRPC client) is configured with the KMS provider (gRPC server) unix domain socket endpoint in order to communicate with it. An abstract Linux socket may be used by starting the endpoint with `/@`, i.e. `unix:///@foo`. Care must be taken when using this type of socket as they do not have concept of ACL (unlike traditional file based sockets). However, they are subject to Linux networking namespace, so will only be accessible to containers within the same pod unless host networking is used.

##### KMS v2 {#developing-a-kms-plugin-gRPC-server-notes-kms-v2}

* KMS plugin version: `v2`

  In response to the `Status` remote procedure call, a compatible KMS plugin should return its KMS compatibility
  version as `StatusResponse.version`. That status response should also include
  "ok" as `StatusResponse.healthz` and a `key_id` (remote KMS KEK ID) as `StatusResponse.key_id`.
  The Kubernetes project recommends you make your plugin
  compatible with the stable `v2` KMS API. Kubernetes  also supports the
  `v2beta1` API for KMS; future Kubernetes releases are likely to continue supporting that beta version.

  The API server polls the `Status` procedure call approximately every minute when everything is healthy,
  and every 10 seconds when the plugin is not healthy.  Plugins must take care to optimize this call as it will be
  under constant load.

* Encryption

  The `EncryptRequest` procedure call provides the plaintext and a UID for logging purposes.  The response must include
  the ciphertext, the `key_id` for the KEK used, and, optionally, any metadata that the KMS plugin needs to aid in
  future `DecryptRequest` calls (via the `annotations` field).  The plugin must guarantee that any distinct plaintext
  results in a distinct response `(ciphertext, key_id, annotations)`.

  If the plugin returns a non-empty `annotations` map, all map keys must be fully qualified domain names such as
  `example.com`. An example use case of `annotation` is `{"kms.example.io/remote-kms-auditid":"<audit ID used by the remote KMS>"}`

  The API server does not perform the `EncryptRequest` procedure call at a high rate.  Plugin implementations should
  still aim to keep each request's latency at under 100 milliseconds.

* Decryption

  The `DecryptRequest` procedure call provides the `(ciphertext, key_id, annotations)` from `EncryptRequest` and a UID
  for logging purposes.  As expected, it is the inverse of the `EncryptRequest` call.  Plugins must verify that the
  `key_id` is one that they understand - they must not attempt to decrypt data unless they are sure that it was
  encrypted by them at an earlier time.

  The API server may perform thousands of `DecryptRequest` procedure calls on startup to fill its watch cache.  Thus
  plugin implementations must perform these calls as quickly as possible, and should aim to keep each request's latency
  at under 10 milliseconds.

* Understanding `key_id` and Key Rotation

  The `key_id` is the public, non-secret name of the remote KMS KEK that is currently in use.  It may be logged
  during regular operation of the API server, and thus must not contain any private data.  Plugin implementations
  are encouraged to use a hash to avoid leaking any data.  The KMS v2 metrics take care to hash this value before
  exposing it via the `/metrics` endpoint.

  The API server considers the `key_id` returned from the `Status` procedure call to be authoritative.  Thus, a change
  to this value signals to the API server that the remote KEK has changed, and data encrypted with the old KEK should
  be marked stale when a no-op write is performed (as described below).  If an `EncryptRequest` procedure call returns a
  `key_id` that is different from `Status`, the response is thrown away and the plugin is considered unhealthy.  Thus
  implementations must guarantee that the `key_id` returned from `Status` will be the same as the one returned by
  `EncryptRequest`.  Furthermore, plugins must ensure that the `key_id` is stable and does not flip-flop between values
  (i.e. during a remote KEK rotation).

  Plugins must not re-use `key_id`s, even in situations where a previously used remote KEK has been reinstated.  For
  example, if a plugin was using `key_id=A`, switched to `key_id=B`, and then went back to `key_id=A` - instead of
  reporting `key_id=A` the plugin should report some derivative value such as `key_id=A_001` or use a new value such
  as `key_id=C`.

  Since the API server polls `Status` about every minute, `key_id` rotation is not immediate.  Furthermore, the API
  server will coast on the last valid state for about three minutes.  Thus if a user wants to take a passive approach
  to storage migration (i.e. by waiting), they must schedule a migration to occur at `3 + N + M` minutes after the
  remote KEK has been rotated (`N` is how long it takes the plugin to observe the `key_id` change and `M` is the
  desired buffer to allow config changes to be processed - a minimum `M` of five minutes is recommend).  Note that no
  API server restart is required to perform KEK rotation.

  
  Because you don't control the number of writes performed with the DEK,
  the Kubernetes project recommends rotating the KEK at least every 90 days.
  

* protocol: UNIX domain socket (`unix`)

  The plugin is implemented as a gRPC server that listens at UNIX domain socket.
  The plugin deployment should create a file on the file system to run the gRPC unix domain socket connection.
  The API server (gRPC client) is configured with the KMS provider (gRPC server) unix
  domain socket endpoint in order to communicate with it.
  An abstract Linux socket may be used by starting the endpoint with `/@`, i.e. `unix:///@foo`.
  Care must be taken when using this type of socket as they do not have concept of ACL
  (unlike traditional file based sockets).
  However, they are subject to Linux networking namespace, so will only be accessible to
  containers within the same pod unless host networking is used.

### Integrating a KMS plugin with the remote KMS

The KMS plugin can communicate with the remote KMS using any protocol supported by the KMS.
All configuration data, including authentication credentials the KMS plugin uses to communicate with the remote KMS,
are stored and managed by the KMS plugin independently.
The KMS plugin can encode the ciphertext with additional metadata that may be required before sending it to the KMS
for decryption (KMS v2 makes this process easier by providing a dedicated `annotations` field).

### Deploying the KMS plugin

Ensure that the KMS plugin runs on the same host(s) as the Kubernetes API server(s).
