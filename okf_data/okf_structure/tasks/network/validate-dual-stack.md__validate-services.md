---
id: okf-structure/tasks/network/validate-dual-stack.md#validate-services
kind: section
title: Validate Services
source: tasks/network/validate-dual-stack.md
url: https://kubernetes.io/docs/tasks/network/validate-dual-stack/
heading: Validate Services
parent: okf-structure/tasks/network/validate-dual-stack
children: []
prev_sibling: okf-structure/tasks/network/validate-dual-stack.md#validate-addressing
next_sibling: null
word_count: 484
---

Create the following Service that does not explicitly define `.spec.ipFamilyPolicy`.
Kubernetes will assign a cluster IP for the Service from the first configured
`service-cluster-ip-range` and set the `.spec.ipFamilyPolicy` to `SingleStack`.

Use `kubectl` to view the YAML for the Service.

```shell
kubectl get svc my-service -o yaml
```

The Service has `.spec.ipFamilyPolicy` set to `SingleStack` and `.spec.clusterIP` set
to an IPv4 address from the first configured range set via `--service-cluster-ip-range`
flag on kube-controller-manager.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
  namespace: default
spec:
  clusterIP: 10.0.217.164
  clusterIPs:
  - 10.0.217.164
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - port: 80
    protocol: TCP
    targetPort: 9376
  selector:
    app.kubernetes.io/name: MyApp
  sessionAffinity: None
  type: ClusterIP
status:
  loadBalancer: {}
```

Create the following Service that explicitly defines `IPv6` as the first array element in
`.spec.ipFamilies`. Kubernetes will assign a cluster IP for the Service from the IPv6 range
configured `service-cluster-ip-range` and set the `.spec.ipFamilyPolicy` to `SingleStack`.

Use `kubectl` to view the YAML for the Service.

```shell
kubectl get svc my-service -o yaml
```

The Service has `.spec.ipFamilyPolicy` set to `SingleStack` and `.spec.clusterIP` set to
an IPv6 address from the IPv6 range set via `--service-cluster-ip-range` flag on kube-controller-manager.

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/name: MyApp
  name: my-service
spec:
  clusterIP: 2001:db8:fd00::5118
  clusterIPs:
  - 2001:db8:fd00::5118
  ipFamilies:
  - IPv6
  ipFamilyPolicy: SingleStack
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app.kubernetes.io/name: MyApp
  sessionAffinity: None
  type: ClusterIP
status:
  loadBalancer: {}
```

Create the following Service that explicitly defines `PreferDualStack` in `.spec.ipFamilyPolicy`.
Kubernetes will assign both IPv4 and IPv6 addresses (as this cluster has dual-stack enabled) and
select the `.spec.ClusterIP` from the list of `.spec.ClusterIPs` based on the address family of
the first element in the `.spec.ipFamilies` array.

The `kubectl get svc` command will only show the primary IP in the `CLUSTER-IP` field.

```shell
kubectl get svc -l app.kubernetes.io/name=MyApp
```

```
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
my-service   ClusterIP   10.0.216.242   <none>        80/TCP    5s
```

Validate that the Service gets cluster IPs from the IPv4 and IPv6 address blocks using
`kubectl describe`. You may then validate access to the service via the IPs and ports.

```shell
kubectl describe svc -l app.kubernetes.io/name=MyApp
```

```
Name:              my-service
Namespace:         default
Labels:            app.kubernetes.io/name=MyApp
Annotations:       <none>
Selector:          app.kubernetes.io/name=MyApp
Type:              ClusterIP
IP Family Policy:  PreferDualStack
IP Families:       IPv4,IPv6
IP:                10.0.216.242
IPs:               10.0.216.242,2001:db8:fd00::af55
Port:              <unset>  80/TCP
TargetPort:        9376/TCP
Endpoints:         <none>
Session Affinity:  None
Events:            <none>
```

### Create a dual-stack load balanced Service

If the cloud provider supports the provisioning of IPv6 enabled external load balancers,
create the following Service with `PreferDualStack` in `.spec.ipFamilyPolicy`, `IPv6` as
the first element of the `.spec.ipFamilies` array and the `type` field set to `LoadBalancer`.

Check the Service:

```shell
kubectl get svc -l app.kubernetes.io/name=MyApp
```

Validate that the Service receives a `CLUSTER-IP` address from the IPv6 address block
along with an `EXTERNAL-IP`. You may then validate access to the service via the IP and port.

```
NAME         TYPE           CLUSTER-IP            EXTERNAL-IP        PORT(S)        AGE
my-service   LoadBalancer   2001:db8:fd00::7ebc   2603:1030:805::5   80:30790/TCP   35s
```
