---
id: okf-structure/tasks/administer-cluster/switch-to-evented-pleg.md#switching-to-evented-pleg
kind: section
title: Switching to Evented PLEG
source: tasks/administer-cluster/switch-to-evented-pleg.md
url: https://kubernetes.io/docs/tasks/administer-cluster/switch-to-evented-pleg/
heading: Switching to Evented PLEG
parent: okf-structure/tasks/administer-cluster/switch-to-evented-pleg
children: []
prev_sibling: okf-structure/tasks/administer-cluster/switch-to-evented-pleg.md#why-switch-to-evented-pleg
next_sibling: okf-structure/tasks/administer-cluster/switch-to-evented-pleg.md#whatsnext
word_count: 237
---

1. Start the Kubelet with the feature gate
   `EventedPLEG` enabled. You can manage the kubelet feature gates editing the kubelet
   config file and restarting the kubelet service.
   You need to do this on each node where you are using this feature.

2. Make sure the node is drained before proceeding. 

3. Start the container runtime with the container event generation enabled. 

   
   
   Version 1.7+
   
   
   Version 1.26+

   Check if the CRI-O is already configured to emit CRI events by verifying the configuration,

   ```shell
   crio config | grep enable_pod_events
   ```

   If it is enabled, the output should be similar to the following:

   ```none
   enable_pod_events = true
   ```

   To enable it, start the CRI-O daemon with the flag `--enable-pod-events=true` or
   use a dropin config with the following lines:

   ```toml
   [crio.runtime]
   enable_pod_events: true
   ```
   
   

   

4. Verify that the kubelet is using event-based container stage change monitoring.
   To check, look for the term `EventedPLEG` in the kubelet logs.

   The output should be similar to this:

   ```console
   I0314 11:10:13.909915 1105457 feature_gate.go:249] feature gates: &{map[EventedPLEG:true]}
   ```

   If you have set `--v` to 4 and above, you might see more entries that indicate
   that the kubelet is using event-based container state monitoring.

   ```console
   I0314 11:12:42.009542 1110177 evented.go:238] "Evented PLEG: Generated pod status from the received event" podUID=3b2c6172-b112-447a-ba96-94e7022912dc
   I0314 11:12:44.623326 1110177 evented.go:238] "Evented PLEG: Generated pod status from the received event" podUID=b3fba5ea-a8c5-4b76-8f43-481e17e8ec40
   I0314 11:12:44.714564 1110177 evented.go:238] "Evented PLEG: Generated pod status from the received event" podUID=b3fba5ea-a8c5-4b76-8f43-481e17e8ec40
   ```
