---
id: okf-structure/concepts/workloads/pods/pod-hostname.md#default-pod-hostname
kind: section
title: Default Pod hostname
source: concepts/workloads/pods/pod-hostname.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-hostname/
heading: Default Pod hostname
parent: okf-structure/concepts/workloads/pods/pod-hostname
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-hostname.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/pod-hostname.md#hostname-with-pod-s-hostname-and-subdomain-fields
word_count: 81
---

When a Pod is created, its hostname (as observed from within the Pod) 
is derived from the Pod's metadata.name value. 
Both the hostname and its corresponding fully qualified domain name (FQDN) 
are set to the metadata.name value (from the Pod's perspective)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox-1
spec:
  containers:
  - image: busybox:1.28
    command:
      - sleep
      - "3600"
    name: busybox
```
The Pod created by this manifest will have its hostname and fully qualified domain name (FQDN) set to `busybox-1`.
