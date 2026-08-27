---
id: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#operators
kind: section
title: Operators
source: concepts/scheduling-eviction/assign-pod-node.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
heading: Operators
parent: okf-structure/concepts/scheduling-eviction/assign-pod-node
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#pod-topology-labels
next_sibling: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#whatsnext
word_count: 210
---

The following are all the logical operators that you can use in the `operator` field for `nodeAffinity` and `podAffinity` mentioned above.

|    Operator    |    Behavior     |
| :------------: | :-------------: |
| `In` | The label value is present in the supplied set of strings |
|   `NotIn`   | The label value is not contained in the supplied set of strings |
| `Exists` | A label with this key exists on the object |
| `DoesNotExist` | No label with this key exists on the object |

The following operators can only be used with `nodeAffinity`.

|    Operator    |    Behavior    |
| :------------: | :-------------: |
| `Gt` | The field value will be parsed as an integer, and the integer that results from parsing the value of a label named by this selector is greater than this integer |
| `Lt` | The field value will be parsed as an integer, and the integer that results from parsing the value of a label named by this selector is less than this integer |

`Gt` and `Lt` operators will not work with non-integer values. If the given value
doesn't parse as an integer, the Pod will fail to get scheduled. Also, `Gt` and `Lt`
are not available for `podAffinity`.
