---
id: okf-structure/tutorials/security/apparmor.md#securing-a-pod
kind: section
title: Securing a Pod
source: tutorials/security/apparmor.md
url: https://kubernetes.io/docs/tutorials/security/apparmor/
heading: Securing a Pod
parent: okf-structure/tutorials/security/apparmor
children: []
prev_sibling: okf-structure/tutorials/security/apparmor.md#prerequisites
next_sibling: okf-structure/tutorials/security/apparmor.md#example
word_count: 138
---

Prior to Kubernetes v1.30, AppArmor was specified through annotations. Use the documentation version
selector to view the documentation with this deprecated API.

AppArmor profiles can be specified at the pod level or container level. The container AppArmor
profile takes precedence over the pod profile.

```yaml
securityContext:
  appArmorProfile:
    type: <profile_type>
```

Where `<profile_type>` is one of:

* `RuntimeDefault` to use the runtime's default profile
* `Localhost` to use a profile loaded on the host (see below)
* `Unconfined` to run without AppArmor

See Specifying AppArmor Confinement for full details on the AppArmor profile API.

To verify that the profile was applied, you can check that the container's root process is
running with the correct profile by examining its proc attr:

```shell
kubectl exec <pod_name> -- cat /proc/1/attr/current
```

The output should look something like this:

```
cri-containerd.apparmor.d (enforce)
```
