---
id: okf-structure/concepts/storage/storage-capacity.md#limitations
kind: section
title: Limitations
source: concepts/storage/storage-capacity.md
url: https://kubernetes.io/docs/concepts/storage/storage-capacity/
heading: Limitations
parent: okf-structure/concepts/storage/storage-capacity
children: []
prev_sibling: okf-structure/concepts/storage/storage-capacity.md#rescheduling
next_sibling: okf-structure/concepts/storage/storage-capacity.md#whatsnext
word_count: 101
---

Storage capacity tracking increases the chance that scheduling works
on the first try, but cannot guarantee this because the scheduler has
to decide based on potentially out-dated information. Usually, the
same retry mechanism as for scheduling without any storage capacity
information handles scheduling failures.

One situation where scheduling can fail permanently is when a Pod uses
multiple volumes: one volume might have been created already in a
topology segment which then does not have enough capacity left for
another volume. Manual intervention is necessary to recover from this,
for example by increasing capacity or deleting the volume that was
already created.
