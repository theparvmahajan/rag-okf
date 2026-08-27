---
id: okf-structure/concepts/containers/images.md#serial-and-parallel-image-pulls
kind: section
title: Serial and parallel image pulls
source: concepts/containers/images.md
url: https://kubernetes.io/docs/concepts/containers/images/
heading: Serial and parallel image pulls
parent: okf-structure/concepts/containers/images
children: []
prev_sibling: okf-structure/concepts/containers/images.md#updating-images
next_sibling: okf-structure/concepts/containers/images.md#multi-architecture-images-with-image-indexes
word_count: 357
---

By default, the kubelet pulls images serially. In other words, the kubelet sends
only one image pull request to the image service at a time. Other image pull
requests have to wait until the one being processed is complete.

Nodes make image pull decisions in isolation. Even when you use serialized image
pulls, two different nodes can pull the same image in parallel.

If you would like to enable parallel image pulls, you can set the field
`serializeImagePulls` to false in the kubelet configuration.
With `serializeImagePulls` set to false, image pull requests will be sent to the image service immediately,
and multiple images will be pulled at the same time.

When enabling parallel image pulls, ensure that the image service of your container
runtime can handle parallel image pulls.

The kubelet never pulls multiple images in parallel on behalf of one Pod. For example,
if you have a Pod that has an init container and an application container, the image
pulls for the two containers will not be parallelized. However, if you have two
Pods that use different images, and the parallel image pull feature is enabled,
the kubelet will pull the images in parallel on behalf of the two different Pods.

### Maximum parallel image pulls

When `serializeImagePulls` is set to false, the kubelet defaults to no limit on
the maximum number of images being pulled at the same time. If you would like to
limit the number of parallel image pulls, you can set the field `maxParallelImagePulls`
in the kubelet configuration. With `maxParallelImagePulls` set to _n_, only _n_
images can be pulled at the same time, and any image pull beyond _n_ will have to
wait until at least one ongoing image pull is complete.

Limiting the number of parallel image pulls prevents image pulling from consuming
too much network bandwidth or disk I/O, when parallel image pulling is enabled.

You can set `maxParallelImagePulls` to a positive number that is greater than or
equal to 1. If you set `maxParallelImagePulls` to be greater than or equal to 2,
you must set `serializeImagePulls` to false. The kubelet will fail to start
with an invalid `maxParallelImagePulls` setting.
