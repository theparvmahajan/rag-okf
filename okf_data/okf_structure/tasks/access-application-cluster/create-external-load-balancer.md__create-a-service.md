---
id: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#create-a-service
kind: section
title: Create a Service
source: tasks/access-application-cluster/create-external-load-balancer.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/
heading: Create a Service
parent: okf-structure/tasks/access-application-cluster/create-external-load-balancer
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#prerequisites
next_sibling: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#finding-your-ip-address
word_count: 121
---

### Create a Service from a manifest

To create an external load balancer, add the following line to your
Service manifest:

```yaml
    type: LoadBalancer
```

Your manifest might then look like:

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
  type: LoadBalancer
```

### Create a Service using kubectl

You can alternatively create the service with the `kubectl expose` command and
its `--type=LoadBalancer` flag:

```bash
kubectl expose deployment example --port=8765 --target-port=9376 \
        --name=example-service --type=LoadBalancer
```

This command creates a new Service using the same selectors as the referenced
resource (in the case of the example above, a
Deployment named `example`).

For more information, including optional flags, refer to the
`kubectl expose` reference.
