---
id: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline.md#metrics-api
kind: section
title: Metrics API
source: tasks/debug/debug-cluster/resource-metrics-pipeline.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/
heading: Metrics API
parent: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline.md#introduction
next_sibling: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline.md#measuring-resource-usage
word_count: 255
---

The metrics-server implements the Metrics API. This API allows you to access CPU and memory usage
for the nodes and pods in your cluster. Its primary role is to feed resource usage metrics to K8s
autoscaler components.

Here is an example of the Metrics API request for a `minikube` node piped through `jq` for easier
reading:

```shell
kubectl get --raw "/apis/metrics.k8s.io/v1beta1/nodes/minikube" | jq '.'
```

Here is the same API call using `curl`:

```shell
curl http://localhost:8080/apis/metrics.k8s.io/v1beta1/nodes/minikube
```

Sample response:

```json
{
  "kind": "NodeMetrics",
  "apiVersion": "metrics.k8s.io/v1beta1",
  "metadata": {
    "name": "minikube",
    "selfLink": "/apis/metrics.k8s.io/v1beta1/nodes/minikube",
    "creationTimestamp": "2022-01-27T18:48:43Z"
  },
  "timestamp": "2022-01-27T18:48:33Z",
  "window": "30s",
  "usage": {
    "cpu": "487558164n",
    "memory": "732212Ki"
  }
}
```

Here is an example of the Metrics API request for a `kube-scheduler-minikube` pod contained in the
`kube-system` namespace and piped through `jq` for easier reading:

```shell
kubectl get --raw "/apis/metrics.k8s.io/v1beta1/namespaces/kube-system/pods/kube-scheduler-minikube" | jq '.'
```

Here is the same API call using `curl`:

```shell
curl http://localhost:8080/apis/metrics.k8s.io/v1beta1/namespaces/kube-system/pods/kube-scheduler-minikube
```

Sample response:

```json
{
  "kind": "PodMetrics",
  "apiVersion": "metrics.k8s.io/v1beta1",
  "metadata": {
    "name": "kube-scheduler-minikube",
    "namespace": "kube-system",
    "selfLink": "/apis/metrics.k8s.io/v1beta1/namespaces/kube-system/pods/kube-scheduler-minikube",
    "creationTimestamp": "2022-01-27T19:25:00Z"
  },
  "timestamp": "2022-01-27T19:24:31Z",
  "window": "30s",
  "containers": [
    {
      "name": "kube-scheduler",
      "usage": {
        "cpu": "9559630n",
        "memory": "22244Ki"
      }
    }
  ]
}
```

The Metrics API is defined in the k8s.io/metrics
repository. You must enable the API aggregation layer
and register an APIService
for the `metrics.k8s.io` API.

To learn more about the Metrics API, see resource metrics API design,
the metrics-server repository and the
resource metrics API.

You must deploy the metrics-server or alternative adapter that serves the Metrics API to be able
to access it.
