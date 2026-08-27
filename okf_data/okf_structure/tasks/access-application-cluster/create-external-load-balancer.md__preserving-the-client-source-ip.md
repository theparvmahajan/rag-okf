---
id: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#preserving-the-client-source-ip
kind: section
title: Preserving the client source IP
source: tasks/access-application-cluster/create-external-load-balancer.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/
heading: Preserving the client source IP
parent: okf-structure/tasks/access-application-cluster/create-external-load-balancer
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#finding-your-ip-address
next_sibling: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#garbage-collecting-load-balancers
word_count: 318
---

By default, the source IP seen in the target container is *not the original
source IP* of the client. To enable preservation of the client IP, the following
fields can be configured in the `.spec` of the Service:

* `.spec.externalTrafficPolicy` - denotes if this Service desires to route
  external traffic to node-local or cluster-wide endpoints. There are two available
  options: `Cluster` (default) and `Local`. `Cluster` obscures the client source
  IP and may cause a second hop to another node, but should have good overall
  load-spreading. `Local` preserves the client source IP and avoids a second hop
  for LoadBalancer and NodePort type Services, but risks potentially imbalanced
  traffic spreading.
* `.spec.healthCheckNodePort` - specifies the health check node port
  (numeric port number) for the service. If you don't specify
  `healthCheckNodePort`, the service controller allocates a port from your
  cluster's NodePort range.  
  You can configure that range by setting an API server command line option,
  `--service-node-port-range`. The Service will use the user-specified
  `healthCheckNodePort` value if you specify it, provided that the
  Service `type` is set to LoadBalancer and `externalTrafficPolicy` is set
  to `Local`.

Setting `externalTrafficPolicy` to Local in the Service manifest
activates this feature. For example:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: example-service
spec:
  selector:
    app: example
  ports:
    - port: 8765
      targetPort: 9376
  externalTrafficPolicy: Local
  type: LoadBalancer
```

### Caveats and limitations when preserving source IPs

Load balancing services from some cloud providers do not let you configure different weights for each target.

With each target weighted equally in terms of sending traffic to Nodes, external
traffic is not equally load balanced across different Pods. The external load balancer
is unaware of the number of Pods on each node that are used as a target.

Where `NumServicePods <<  NumNodes` or `NumServicePods >> NumNodes`, a fairly close-to-equal
distribution will be seen, even without weights.

Internal pod to pod traffic should behave similar to ClusterIP services, with equal probability across all pods.
