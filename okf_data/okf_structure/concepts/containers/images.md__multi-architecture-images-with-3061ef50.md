---
id: okf-structure/concepts/containers/images.md#multi-architecture-images-with-image-indexes
kind: section
title: Multi-architecture images with image indexes
source: concepts/containers/images.md
url: https://kubernetes.io/docs/concepts/containers/images/
heading: Multi-architecture images with image indexes
parent: okf-structure/concepts/containers/images
children: []
prev_sibling: okf-structure/concepts/containers/images.md#serial-and-parallel-image-pulls
next_sibling: okf-structure/concepts/containers/images.md#using-a-private-registry
word_count: 128
---

As well as providing binary images, a container registry can also serve a
container image index.
An image index can point to multiple image manifests
for architecture-specific versions of a container. The idea is that you can have
a name for an image (for example: `pause`, `example/mycontainer`, `kube-apiserver`)
and allow different systems to fetch the right binary image for the machine
architecture they are using.

The Kubernetes project typically creates container images for its releases with
names that include the suffix `-$(ARCH)`. For backward compatibility, generate
older images with suffixes. For instance, an image named as `pause` would be a
multi-architecture image containing manifests for all supported architectures,
while `pause-amd64` would be a backward-compatible version for older configurations,
or for YAML files with hardcoded image names containing suffixes.
