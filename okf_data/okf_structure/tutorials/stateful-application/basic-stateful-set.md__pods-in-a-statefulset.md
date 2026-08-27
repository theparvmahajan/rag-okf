---
id: okf-structure/tutorials/stateful-application/basic-stateful-set.md#pods-in-a-statefulset
kind: section
title: Pods in a StatefulSet
source: tutorials/stateful-application/basic-stateful-set.md
url: https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/
heading: Pods in a StatefulSet
parent: okf-structure/tutorials/stateful-application/basic-stateful-set
children: []
prev_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#creating-a-statefulset
next_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#scaling-a-statefulset
word_count: 1208
---

Pods in a StatefulSet have a unique ordinal index and a stable network identity.

### Examining the Pod's ordinal index

Get the StatefulSet's Pods:

```shell
kubectl get pods -l app=nginx
```
```
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          1m
web-1     1/1       Running   0          1m
```

As mentioned in the StatefulSets
concept, the Pods in a StatefulSet have a sticky, unique identity. This identity
is based on a unique ordinal index that is assigned to each Pod by the
StatefulSet controller.  
The Pods' names take the form `<statefulset name>-<ordinal index>`.
Since the `web` StatefulSet has two replicas, it creates two Pods, `web-0` and `web-1`.

### Using stable network identities

Each Pod has a stable hostname based on its ordinal index. Use
`kubectl exec` to execute the
`hostname` command in each Pod:

```shell
for i in 0 1; do kubectl exec "web-$i" -- sh -c 'hostname'; done
```
```
web-0
web-1
```

Use `kubectl run` to execute
a container that provides the `nslookup` command from the `dnsutils` package.
Using `nslookup` on the Pods' hostnames, you can examine their in-cluster DNS
addresses:

```shell
kubectl run -i --tty --image busybox:1.28 dns-test --restart=Never --rm
```
which starts a new shell. In that new shell, run:
```shell
# Run this in the dns-test container shell
nslookup web-0.nginx
```
The output is similar to:
```
Server:    10.0.0.10
Address 1: 10.0.0.10 kube-dns.kube-system.svc.cluster.local

Name:      web-0.nginx
Address 1: 10.244.1.6

nslookup web-1.nginx
Server:    10.0.0.10
Address 1: 10.0.0.10 kube-dns.kube-system.svc.cluster.local

Name:      web-1.nginx
Address 1: 10.244.2.6
```

(and now exit the container shell: `exit`)

The CNAME of the headless service points to SRV records (one for each Pod that
is Running and Ready). The SRV records point to A record entries that
contain the Pods' IP addresses.

In one terminal, watch the StatefulSet's Pods:

```shell
# Start a new watch
# End this watch when you've seen that the delete is finished
kubectl get pod --watch -l app=nginx
```
In a second terminal, use
`kubectl delete` to delete all
the Pods in the StatefulSet:

```shell
kubectl delete pod -l app=nginx
```
```
pod "web-0" deleted
pod "web-1" deleted
```

Wait for the StatefulSet to restart them, and for both Pods to transition to
Running and Ready:

```shell
# This should already be running
kubectl get pod --watch -l app=nginx
```
```
NAME      READY     STATUS              RESTARTS   AGE
web-0     0/1       ContainerCreating   0          0s
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          2s
web-1     0/1       Pending   0         0s
web-1     0/1       Pending   0         0s
web-1     0/1       ContainerCreating   0         0s
web-1     1/1       Running   0         34s
```

Use `kubectl exec` and `kubectl run` to view the Pods' hostnames and in-cluster
DNS entries. First, view the Pods' hostnames:

```shell
for i in 0 1; do kubectl exec web-$i -- sh -c 'hostname'; done
```
```
web-0
web-1
```
then, run:
```shell
kubectl run -i --tty --image busybox:1.28 dns-test --restart=Never --rm
```
which starts a new shell.  
In that new shell, run:
```shell
# Run this in the dns-test container shell
nslookup web-0.nginx
```
The output is similar to:
```
Server:    10.0.0.10
Address 1: 10.0.0.10 kube-dns.kube-system.svc.cluster.local

Name:      web-0.nginx
Address 1: 10.244.1.7

nslookup web-1.nginx
Server:    10.0.0.10
Address 1: 10.0.0.10 kube-dns.kube-system.svc.cluster.local

Name:      web-1.nginx
Address 1: 10.244.2.8
```

(and now exit the container shell: `exit`)

The Pods' ordinals, hostnames, SRV records, and A record names have not changed,
but the IP addresses associated with the Pods may have changed. In the cluster
used for this tutorial, they have. This is why it is important not to configure
other applications to connect to Pods in a StatefulSet by the IP address
of a particular Pod (it is OK to connect to Pods by resolving their hostname).

#### Discovery for specific Pods in a StatefulSet

If you need to find and connect to the active members of a StatefulSet, you
should query the CNAME of the headless Service
(`nginx.default.svc.cluster.local`). The SRV records associated with the
CNAME will contain only the Pods in the StatefulSet that are Running and
Ready.

If your application already implements connection logic that tests for
liveness and readiness, you can use the SRV records of the Pods (
`web-0.nginx.default.svc.cluster.local`,
`web-1.nginx.default.svc.cluster.local`), as they are stable, and your
application will be able to discover the Pods' addresses when they transition
to Running and Ready.

If your application wants to find any healthy Pod in a StatefulSet,
and therefore does not need to track each specific Pod,
you could also connect to the IP address of a `type: ClusterIP` Service,
backed by the Pods in that StatefulSet. You can use the same Service that
tracks the StatefulSet (specified in the `serviceName` of the StatefulSet)
or a separate Service that selects the right set of Pods.

### Writing to stable storage

Get the PersistentVolumeClaims for `web-0` and `web-1`:

```shell
kubectl get pvc -l app=nginx
```
The output is similar to:
```
NAME        STATUS    VOLUME                                     CAPACITY   ACCESSMODES   AGE
www-web-0   Bound     pvc-15c268c7-b507-11e6-932f-42010a800002   1Gi        RWO           48s
www-web-1   Bound     pvc-15c79307-b507-11e6-932f-42010a800002   1Gi        RWO           48s
```

The StatefulSet controller created two
PersistentVolumeClaims
that are bound to two
PersistentVolumes.

As the cluster used in this tutorial is configured to dynamically provision PersistentVolumes,
the PersistentVolumes were created and bound automatically.

The NGINX webserver, by default, serves an index file from
`/usr/share/nginx/html/index.html`. The `volumeMounts` field in the
StatefulSet's `spec` ensures that the `/usr/share/nginx/html` directory is
backed by a PersistentVolume.

Write the Pods' hostnames to their `index.html` files and verify that the NGINX
webservers serve the hostnames:

```shell
for i in 0 1; do kubectl exec "web-$i" -- sh -c 'echo "$(hostname)" > /usr/share/nginx/html/index.html'; done

for i in 0 1; do kubectl exec -i -t "web-$i" -- curl http://localhost/; done
```
```
web-0
web-1
```

If you instead see **403 Forbidden** responses for the above curl command,
you will need to fix the permissions of the directory mounted by the `volumeMounts`
(due to a bug when using hostPath volumes),
by running:

`for i in 0 1; do kubectl exec web-$i -- chmod 755 /usr/share/nginx/html; done`

before retrying the `curl` command above.

In one terminal, watch the StatefulSet's Pods:

```shell
# End this watch when you've reached the end of the section.
# At the start of "Scaling a StatefulSet" you'll start a new watch.
kubectl get pod --watch -l app=nginx
```

In a second terminal, delete all of the StatefulSet's Pods:

```shell
kubectl delete pod -l app=nginx
```
```
pod "web-0" deleted
pod "web-1" deleted
```
Examine the output of the `kubectl get` command in the first terminal, and wait
for all of the Pods to transition to Running and Ready.

```shell
# This should already be running
kubectl get pod --watch -l app=nginx
```
```
NAME      READY     STATUS              RESTARTS   AGE
web-0     0/1       ContainerCreating   0          0s
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          2s
web-1     0/1       Pending   0         0s
web-1     0/1       Pending   0         0s
web-1     0/1       ContainerCreating   0         0s
web-1     1/1       Running   0         34s
```

Verify the web servers continue to serve their hostnames:

```
for i in 0 1; do kubectl exec -i -t "web-$i" -- curl http://localhost/; done
```
```
web-0
web-1
```

Even though `web-0` and `web-1` were rescheduled, they continue to serve their
hostnames because the PersistentVolumes associated with their
PersistentVolumeClaims are remounted to their `volumeMounts`. No matter what
node `web-0`and `web-1` are scheduled on, their PersistentVolumes will be
mounted to the appropriate mount points.
