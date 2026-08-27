---
id: okf-structure/concepts/storage/volume-attributes-classes.md#parameters
kind: section
title: Parameters
source: concepts/storage/volume-attributes-classes.md
url: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/
heading: Parameters
parent: okf-structure/concepts/storage/volume-attributes-classes
children: []
prev_sibling: okf-structure/concepts/storage/volume-attributes-classes.md#the-volumeattributesclass-api
next_sibling: null
word_count: 117
---

VolumeAttributeClasses have parameters that describe volumes belonging to them. Different parameters may be accepted
depending on the provisioner or the resizer. For example, the value `4000`, for the parameter `iops`,
and the parameter `throughput` are specific to GCE PD.
When a parameter is omitted, the default is used at volume provisioning.
If a user applies the PVC with a different VolumeAttributesClass with omitted parameters, the default value of
the parameters may be used depending on the CSI driver implementation.
Please refer to the related CSI driver documentation for more details.

There can be at most 512 parameters defined for a VolumeAttributesClass.
The total length of the parameters object including its keys and values cannot exceed 256 KiB.
