---
id: okf-structure/concepts/security/api-server-bypass-risks.md#the-kubelet-api-kubelet-api
kind: section
title: The kubelet API {#kubelet-api}
source: concepts/security/api-server-bypass-risks.md
url: https://kubernetes.io/docs/concepts/security/api-server-bypass-risks/
heading: The kubelet API {#kubelet-api}
parent: okf-structure/concepts/security/api-server-bypass-risks
children: []
prev_sibling: okf-structure/concepts/security/api-server-bypass-risks.md#static-pods-static-pods
next_sibling: okf-structure/concepts/security/api-server-bypass-risks.md#the-etcd-api
word_count: 350
---

The kubelet provides an HTTP API that is typically exposed on TCP port 10250 on cluster
worker nodes. The API might also be exposed on control plane nodes depending on the Kubernetes
distribution in use. Direct access to the API allows for disclosure of information about
the pods running on a node, the logs from those pods, and execution of commands in
every container running on the node.

Some of these endpoints support Websocket protocols via HTTP `GET` requests, which are authorized with the **get** verb.
This means that **get** permission on `nodes/proxy` is not a read-only permission,
and authorizes access to endpoints which can be used to execute commands in any container running on the node.

When Kubernetes cluster users have RBAC access to `Node` object sub-resources, that access
serves as authorization to interact with the kubelet API. The exact access depends on
which sub-resource access has been granted, as detailed in
kubelet authorization.

Direct access to the kubelet API is not subject to admission control and is not logged
by Kubernetes audit logging. An attacker with direct access to this API may be able to
bypass controls that detect or prevent certain actions.

The kubelet API can be configured to authenticate requests in a number of ways.
By default, the kubelet configuration allows anonymous access. Most Kubernetes providers
change the default to use webhook and certificate authentication. This lets the control plane
ensure that the caller is authorized to access the `nodes` API resource or sub-resources.
The default anonymous access doesn't make this assertion with the control plane.

### Mitigations

- Restrict access to sub-resources of the `nodes` API object using mechanisms such as
  RBAC. Only grant this access when required,
  such as by monitoring services.
- Avoid granting the `nodes/proxy` catch-all permission, even with just the **get** verb.
  Instead, grant granular permissions.
- Restrict access to the kubelet port. Only allow specified and trusted IP address
  ranges to access the port.
- Ensure that kubelet authentication.
  is set to webhook or certificate mode.
- Ensure that the unauthenticated "read-only" Kubelet port is not enabled on the cluster.
