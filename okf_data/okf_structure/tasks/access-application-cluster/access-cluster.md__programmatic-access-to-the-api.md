---
id: okf-structure/tasks/access-application-cluster/access-cluster.md#programmatic-access-to-the-api
kind: section
title: Programmatic access to the API
source: tasks/access-application-cluster/access-cluster.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/
heading: Programmatic access to the API
parent: okf-structure/tasks/access-application-cluster/access-cluster
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/access-cluster.md#directly-accessing-the-rest-api
next_sibling: okf-structure/tasks/access-application-cluster/access-cluster.md#accessing-the-api-from-a-pod
word_count: 185
---

Kubernetes officially supports Go and Python
client libraries.

### Go client

* To get the library, run the following command: `go get k8s.io/client-go@kubernetes-<kubernetes-version-number>`,
  see INSTALL.md
  for detailed installation instructions. See
  https://github.com/kubernetes/client-go
  to see which versions are supported.
* Write an application atop of the client-go clients. Note that client-go defines its own API objects,
  so if needed, please import API definitions from client-go rather than from the main repository,
  e.g., `import "k8s.io/client-go/kubernetes"` is correct.

The Go client can use the same kubeconfig file
as the kubectl CLI does to locate and authenticate to the apiserver. See this
example.

If the application is deployed as a Pod in the cluster, please refer to the next section.

### Python client

To use Python client, run the following command:
`pip install kubernetes`. See Python Client Library page
for more installation options.

The Python client can use the same kubeconfig file
as the kubectl CLI does to locate and authenticate to the apiserver. See this
example.

### Other languages

There are client libraries for accessing the API from other languages.
See documentation for other libraries for how they authenticate.
