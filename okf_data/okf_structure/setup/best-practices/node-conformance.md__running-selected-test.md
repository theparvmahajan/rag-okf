---
id: okf-structure/setup/best-practices/node-conformance.md#running-selected-test
kind: section
title: Running Selected Test
source: setup/best-practices/node-conformance.md
url: https://kubernetes.io/docs/setup/best-practices/node-conformance/
heading: Running Selected Test
parent: okf-structure/setup/best-practices/node-conformance
children: []
prev_sibling: okf-structure/setup/best-practices/node-conformance.md#running-node-conformance-test-for-other-architectures
next_sibling: okf-structure/setup/best-practices/node-conformance.md#caveats
word_count: 151
---

To run specific tests, overwrite the environment variable `FOCUS` with the
regular expression of tests you want to run.

```shell
sudo docker run -it --rm --privileged --net=host \
  -v /:/rootfs:ro -v $CONFIG_DIR:$CONFIG_DIR -v $LOG_DIR:/var/result \
  -e FOCUS=MirrorPod \ # Only run MirrorPod test
  registry.k8s.io/node-test:0.2
```

To skip specific tests, overwrite the environment variable `SKIP` with the
regular expression of tests you want to skip.

```shell
sudo docker run -it --rm --privileged --net=host \
  -v /:/rootfs:ro -v $CONFIG_DIR:$CONFIG_DIR -v $LOG_DIR:/var/result \
  -e SKIP=MirrorPod \ # Run all conformance tests but skip MirrorPod test
  registry.k8s.io/node-test:0.2
```

Node conformance test is a containerized version of
node e2e test.
By default, it runs all conformance tests.

Theoretically, you can run any node e2e test if you configure the container and
mount required volumes properly. But **it is strongly recommended to only run conformance
test**, because it requires much more complex configuration to run non-conformance test.
