---
id: okf-structure/concepts/cluster-administration/flow-control.md#enabling-disabling-api-priority-and-fairness
kind: section
title: Enabling/Disabling API Priority and Fairness
source: concepts/cluster-administration/flow-control.md
url: https://kubernetes.io/docs/concepts/cluster-administration/flow-control/
heading: Enabling/Disabling API Priority and Fairness
parent: okf-structure/concepts/cluster-administration/flow-control
children: []
prev_sibling: okf-structure/concepts/cluster-administration/flow-control.md#introduction
next_sibling: okf-structure/concepts/cluster-administration/flow-control.md#recursive-server-scenarios
word_count: 120
---

The API Priority and Fairness feature is controlled by a command-line flag
and is enabled by default. See 
Options
for a general explanation of the available kube-apiserver command-line 
options and how to enable and disable them. The name of the 
command-line option for APF is "--enable-priority-and-fairness". This feature
also involves an API Group 
with: (a) a stable `v1` version, introduced in 1.29, and 
enabled by default (b) a `v1beta3` version, enabled by default, and
deprecated in v1.29. You can
disable the API group beta version `v1beta3` by adding the
following command-line flags to your `kube-apiserver` invocation:

```shell
kube-apiserver \
--runtime-config=flowcontrol.apiserver.k8s.io/v1beta3=false \
 # …and other flags as usual
```

The command-line flag `--enable-priority-and-fairness=false` will disable the
API Priority and Fairness feature.
