---
id: okf-structure/setup/best-practices/node-conformance.md#caveats
kind: section
title: Caveats
source: setup/best-practices/node-conformance.md
url: https://kubernetes.io/docs/setup/best-practices/node-conformance/
heading: Caveats
parent: okf-structure/setup/best-practices/node-conformance
children: []
prev_sibling: okf-structure/setup/best-practices/node-conformance.md#running-selected-test
next_sibling: null
word_count: 42
---

* The test leaves some docker images on the node, including the node conformance
  test image and images of containers used in the functionality
  test.
* The test leaves dead containers on the node. These containers are created
  during the functionality test.
