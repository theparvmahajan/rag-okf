---
id: okf-structure/concepts/workloads/pods/user-namespaces.md#set-up-a-node-to-support-user-namespaces
kind: section
title: Set up a node to support user namespaces
source: concepts/workloads/pods/user-namespaces.md
url: https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/
heading: Set up a node to support user namespaces
parent: okf-structure/concepts/workloads/pods/user-namespaces
children: []
prev_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#understanding-user-namespaces-for-pods-pods-and-userns
next_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#id-count-for-each-of-pods
word_count: 433
---

By default, the kubelet assigns pods UIDs/GIDs above the range 0-65535, based on
the assumption that the host's files and processes use UIDs/GIDs within this
range, which is standard for most Linux distributions. This approach prevents
any overlap between the UIDs/GIDs of the host and those of the pods.

Avoiding the overlap is important to mitigate the impact of vulnerabilities such
as [CVE-2021-25741][CVE-2021-25741], where a pod can potentially read arbitrary
files in the host. If the UIDs/GIDs of the pod and the host don't overlap, it is
limited what a pod would be able to do: the pod UID/GID won't match the host's
file owner/group.

The kubelet can use a custom range for user IDs and group IDs for pods. To
configure a custom range, the node needs to have:

 * A user `kubelet` in the system (you cannot use any other username here)
 * The binary `getsubids` installed (part of [shadow-utils][shadow-utils]) and
   in the `PATH` for the kubelet binary.
 * A configuration of subordinate UIDs/GIDs for the `kubelet` user (see
   `man 5 subuid` and
   `man 5 subgid`).

This setting only gathers the UID/GID range configuration and does not change
the user executing the `kubelet`.

You must follow some constraints for the subordinate ID range that you assign
to the `kubelet` user:

* The subordinate user ID, that starts the UID range for Pods, **must** be a
  multiple of 65536 and must also be greater than or equal to 65536. In other
  words, you cannot use any ID from the range 0-65535 for Pods; the kubelet
  imposes this restriction to make it difficult to create an accidentally insecure
  configuration.

* The subordinate ID count must be a multiple of 65536

* The subordinate ID count must be at least `65536 x <maxPods>` where `<maxPods>`
  is the maximum number of pods that can run on the node.

* You must assign the same range for both user IDs and for group IDs, It doesn't
  matter if other users have user ID ranges that don't align with the group ID
  ranges.

* None of the assigned ranges should overlap with any other assignment.

* The subordinate configuration must be only one line. In other words, you can't
  have multiple ranges.

For example, you could define `/etc/subuid` and `/etc/subgid` to both have
these entries for the `kubelet` user:

```
# The format is
#   name:firstID:count of IDs
# where
# - firstID is 65536 (the minimum value possible)
# - count of IDs is 110 * 65536
#   (110 is the default limit for number of pods on the node)

kubelet:65536:7208960
```

[CVE-2021-25741]: https://github.com/kubernetes/kubernetes/issues/104980
[shadow-utils]: https://github.com/shadow-maint/shadow
