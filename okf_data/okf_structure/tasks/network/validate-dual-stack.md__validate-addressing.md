---
id: okf-structure/tasks/network/validate-dual-stack.md#validate-addressing
kind: section
title: Validate addressing
source: tasks/network/validate-dual-stack.md
url: https://kubernetes.io/docs/tasks/network/validate-dual-stack/
heading: Validate addressing
parent: okf-structure/tasks/network/validate-dual-stack
children: []
prev_sibling: okf-structure/tasks/network/validate-dual-stack.md#prerequisites
next_sibling: okf-structure/tasks/network/validate-dual-stack.md#validate-services
word_count: 345
---

### Validate node addressing

Each dual-stack Node should have a single IPv4 block and a single IPv6 block allocated.
Validate that IPv4/IPv6 Pod address ranges are configured by running the following command.
Replace the sample node name with a valid dual-stack Node from your cluster. In this example,
the Node's name is `k8s-linuxpool1-34450317-0`:

```shell
kubectl get nodes k8s-linuxpool1-34450317-0 -o go-template --template='{{range .spec.podCIDRs}}{{printf "%s\n" .}}{{end}}'
```

```
10.244.1.0/24
2001:db8::/64
```

There should be one IPv4 block and one IPv6 block allocated.

Validate that the node has an IPv4 and IPv6 interface detected.
Replace node name with a valid node from the cluster.
In this example the node name is `k8s-linuxpool1-34450317-0`:

```shell
kubectl get nodes k8s-linuxpool1-34450317-0 -o go-template --template='{{range .status.addresses}}{{printf "%s: %s\n" .type .address}}{{end}}'
```

```
Hostname: k8s-linuxpool1-34450317-0
InternalIP: 10.0.0.5
InternalIP: 2001:db8:10::5
```

### Validate Pod addressing

Validate that a Pod has an IPv4 and IPv6 address assigned. Replace the Pod name with
a valid Pod in your cluster. In this example the Pod name is `pod01`:

```shell
kubectl get pods pod01 -o go-template --template='{{range .status.podIPs}}{{printf "%s\n" .ip}}{{end}}'
```

```
10.244.1.4
2001:db8::4
```

You can also validate Pod IPs using the Downward API via the `status.podIPs` fieldPath.
The following snippet demonstrates how you can expose the Pod IPs via an environment variable
called `MY_POD_IPS` within a container.

```yaml
        env:
        - name: MY_POD_IPS
          valueFrom:
            fieldRef:
              fieldPath: status.podIPs
```

The following command prints the value of the `MY_POD_IPS` environment variable from
within a container. The value is a comma separated list that corresponds to the
Pod's IPv4 and IPv6 addresses.

```shell
kubectl exec -it pod01 -- set | grep MY_POD_IPS
```

```
MY_POD_IPS=10.244.1.4,2001:db8::4
```

The Pod's IP addresses will also be written to `/etc/hosts` within a container.
The following command executes a cat on `/etc/hosts` on a dual stack Pod.
From the output you can verify both the IPv4 and IPv6 IP address for the Pod.

```shell
kubectl exec -it pod01 -- cat /etc/hosts
```

```
# Kubernetes-managed hosts file.
127.0.0.1    localhost
::1    localhost ip6-localhost ip6-loopback
fe00::0    ip6-localnet
fe00::0    ip6-mcastprefix
fe00::1    ip6-allnodes
fe00::2    ip6-allrouters
10.244.1.4    pod01
2001:db8::4    pod01
```
