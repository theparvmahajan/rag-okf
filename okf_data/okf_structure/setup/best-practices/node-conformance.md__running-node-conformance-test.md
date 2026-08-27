---
id: okf-structure/setup/best-practices/node-conformance.md#running-node-conformance-test
kind: section
title: Running Node Conformance Test
source: setup/best-practices/node-conformance.md
url: https://kubernetes.io/docs/setup/best-practices/node-conformance/
heading: Running Node Conformance Test
parent: okf-structure/setup/best-practices/node-conformance
children: []
prev_sibling: okf-structure/setup/best-practices/node-conformance.md#node-prerequisite
next_sibling: okf-structure/setup/best-practices/node-conformance.md#running-node-conformance-test-for-other-architectures
word_count: 119
---

To run the node conformance test, perform the following steps:

1. Work out the value of the `--kubeconfig` option for the kubelet; for example:
   `--kubeconfig=/var/lib/kubelet/config.yaml`.
    Because the test framework starts a local control plane to test the kubelet,
    use `http://localhost:8080` as the URL of the API server.
    There are some other kubelet command line parameters you may want to use:
  
   * `--cloud-provider`: If you are using `--cloud-provider=gce`, you should
     remove the flag to run the test.

1. Run the node conformance test with command:

   ```shell
   # $CONFIG_DIR is the pod manifest path of your kubelet.
   # $LOG_DIR is the test output path.
   sudo docker run -it --rm --privileged --net=host \
     -v /:/rootfs -v $CONFIG_DIR:$CONFIG_DIR -v $LOG_DIR:/var/result \
     registry.k8s.io/node-test:0.2
   ```
