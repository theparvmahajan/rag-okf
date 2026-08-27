---
id: okf-structure/tutorials/security/seccomp.md#download-example-seccomp-profiles-download-profiles
kind: section
title: Download example seccomp profiles {#download-profiles}
source: tutorials/security/seccomp.md
url: https://kubernetes.io/docs/tutorials/security/seccomp/
heading: Download example seccomp profiles {#download-profiles}
parent: okf-structure/tutorials/security/seccomp
children: []
prev_sibling: okf-structure/tutorials/security/seccomp.md#prerequisites
next_sibling: okf-structure/tutorials/security/seccomp.md#create-a-local-kubernetes-cluster-with-kind
word_count: 74
---

The contents of these profiles will be explored later on, but for now go ahead
and download them into a directory named `profiles/` so that they can be loaded
into the cluster.

Run these commands:

```shell
mkdir ./profiles
curl -L -o profiles/audit.json https://k8s.io/examples/pods/security/seccomp/profiles/audit.json
curl -L -o profiles/violation.json https://k8s.io/examples/pods/security/seccomp/profiles/violation.json
curl -L -o profiles/fine-grained.json https://k8s.io/examples/pods/security/seccomp/profiles/fine-grained.json
ls profiles
```

You should see three profiles listed at the end of the final step:
```
audit.json  fine-grained.json  violation.json
```
