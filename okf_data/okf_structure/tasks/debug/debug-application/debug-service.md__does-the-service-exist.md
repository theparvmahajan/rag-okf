---
id: okf-structure/tasks/debug/debug-application/debug-service.md#does-the-service-exist
kind: section
title: Does the Service exist?
source: tasks/debug/debug-application/debug-service.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/
heading: Does the Service exist?
parent: okf-structure/tasks/debug/debug-application/debug-service
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-service.md#setup
next_sibling: okf-structure/tasks/debug/debug-application/debug-service.md#any-network-policy-ingress-rules-affecting-the-target-pods
word_count: 250
---

The astute reader will have noticed that you did not actually create a Service
yet - that is intentional.  This is a step that sometimes gets forgotten, and
is the first thing to check.

What would happen if you tried to access a non-existent Service?  If
you have another Pod that consumes this Service by name you would get
something like:

```shell
wget -O- hostnames
```
```none
Resolving hostnames (hostnames)... failed: Name or service not known.
wget: unable to resolve host address 'hostnames'
```

The first thing to check is whether that Service actually exists:

```shell
kubectl get svc hostnames
```
```none
No resources found.
Error from server (NotFound): services "hostnames" not found
```

Let's create the Service.  As before, this is for the walk-through - you can
use your own Service's details here.

```shell
kubectl expose deployment hostnames --port=80 --target-port=9376
```
```none
service/hostnames exposed
```

And read it back:

```shell
kubectl get svc hostnames
```
```none
NAME        TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
hostnames   ClusterIP   10.0.1.175   <none>        80/TCP    5s
```

Now you know that the Service exists.

As before, this is the same as if you had started the Service with YAML:

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: hostnames
  name: hostnames
spec:
  selector:
    app: hostnames
  ports:
  - name: default
    protocol: TCP
    port: 80
    targetPort: 9376
```

In order to highlight the full range of configuration, the Service you created
here uses a different port number than the Pods.  For many real-world
Services, these values might be the same.
