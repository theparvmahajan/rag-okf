---
id: okf-structure/tasks/debug/debug-cluster/windows.md#node-level-troubleshooting-troubleshooting-node
kind: section
title: Node-level troubleshooting {#troubleshooting-node}
source: tasks/debug/debug-cluster/windows.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/windows/
heading: Node-level troubleshooting {#troubleshooting-node}
parent: okf-structure/tasks/debug/debug-cluster/windows
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/debug/debug-cluster/windows.md#network-troubleshooting-troubleshooting-network
word_count: 101
---

1. My Pods are stuck at "Container Creating" or restarting over and over

   Ensure that your pause image is compatible with your Windows OS version.
   See Pause container
   to see the latest / recommended pause image and/or get more information.

   
   If using containerd as your container runtime the pause image is specified in the
   `plugins.plugins.cri.sandbox_image` field of the of config.toml configuration file.
   

1. My pods show status as `ErrImgPull` or `ImagePullBackOff`

   Ensure that your Pod is getting scheduled to a
   compatible
   Windows Node.

   More information on how to specify a compatible node for your Pod can be found in
   this guide.
