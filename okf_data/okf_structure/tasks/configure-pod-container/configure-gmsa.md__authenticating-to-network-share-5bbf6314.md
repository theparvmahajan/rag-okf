---
id: okf-structure/tasks/configure-pod-container/configure-gmsa.md#authenticating-to-network-shares-using-hostname-or-fqdn
kind: section
title: Authenticating to network shares using hostname or FQDN
source: tasks/configure-pod-container/configure-gmsa.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/
heading: Authenticating to network shares using hostname or FQDN
parent: okf-structure/tasks/configure-pod-container/configure-gmsa
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#configure-gmsa-credential-spec-reference-in-pod-spec
next_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#troubleshooting
word_count: 77
---

If you are experiencing issues connecting to SMB shares from Pods using hostname or FQDN,
but are able to access the shares via their IPv4 address then make sure the following registry key is set on the Windows nodes.

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Services\hns\State" /v EnableCompartmentNamespace /t REG_DWORD /d 1
```

Running Pods will then need to be recreated to pick up the behavior changes.
More information on how this registry key is used can be found
here
