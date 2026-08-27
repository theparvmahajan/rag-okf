---
id: okf-structure/concepts/storage/projected-volumes.md#serviceaccounttoken-projected-volumes-serviceaccounttoken
kind: section
title: serviceAccountToken projected volumes {#serviceaccounttoken}
source: concepts/storage/projected-volumes.md
url: https://kubernetes.io/docs/concepts/storage/projected-volumes/
heading: serviceAccountToken projected volumes {#serviceaccounttoken}
parent: okf-structure/concepts/storage/projected-volumes
children: []
prev_sibling: okf-structure/concepts/storage/projected-volumes.md#introduction-2
next_sibling: okf-structure/concepts/storage/projected-volumes.md#clustertrustbundle-projected-volumes-clustertrustbundle
word_count: 181
---

You can inject the token for the current service account
into a Pod at a specified path. For example:

The example Pod has a projected volume containing the injected service account
token. Containers in this Pod can use that token to access the Kubernetes API
server, authenticating with the identity of the pod's ServiceAccount.
The `audience` field contains the intended audience of the
token. A recipient of the token must identify itself with an identifier specified
in the audience of the token, and otherwise should reject the token. This field
is optional and it defaults to the identifier of the API server.

The `expirationSeconds` is the expected duration of validity of the service account
token. It defaults to 1 hour and must be at least 10 minutes (600 seconds). An administrator
can also limit its maximum value by specifying the `--service-account-max-token-expiration`
option for the API server. The `path` field specifies a relative path to the mount point
of the projected volume.

A container using a projected volume source as a `subPath`
volume mount will not receive updates for those volume sources.
