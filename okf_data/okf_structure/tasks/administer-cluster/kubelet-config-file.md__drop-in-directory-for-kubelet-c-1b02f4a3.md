---
id: okf-structure/tasks/administer-cluster/kubelet-config-file.md#drop-in-directory-for-kubelet-configuration-files-kubelet-conf-d
kind: section
title: Drop-in directory for kubelet configuration files {#kubelet-conf-d}
source: tasks/administer-cluster/kubelet-config-file.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/
heading: Drop-in directory for kubelet configuration files {#kubelet-conf-d}
parent: okf-structure/tasks/administer-cluster/kubelet-config-file
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubelet-config-file.md#start-a-kubelet-process-configured-via-the-config-file
next_sibling: okf-structure/tasks/administer-cluster/kubelet-config-file.md#viewing-the-kubelet-configuration
word_count: 303
---

You can specify a drop-in configuration directory for the kubelet. By default, the kubelet does not look
for drop-in configuration files anywhere - you must specify a path.
For example: `--config-dir=/etc/kubernetes/kubelet.conf.d`

For Kubernetes v1.28 to v1.29, you can only specify `--config-dir` if you also set
the environment variable `KUBELET_CONFIG_DROPIN_DIR_ALPHA` for the kubelet process (the value
of that variable does not matter).

The suffix of a valid kubelet drop-in configuration file **must** be `.conf`. For instance: `99-kubelet-address.conf`

The kubelet processes files in its config drop-in directory by sorting the **entire file name** alphanumerically.
For instance, `00-kubelet.conf` is processed first, and then overridden with a file named `01-kubelet.conf`.

These files may contain partial configurations but should not be invalid and must include type metadata, specifically `apiVersion` and `kind`. 
Validation is only performed on the final resulting configuration structure stored internally in the kubelet. 
This offers flexibility in managing and merging kubelet configurations from different sources while preventing undesirable configurations. 
However, it is important to note that behavior varies based on the data type of the configuration fields.

Different data types in the kubelet configuration structure merge differently. See the
reference document
for more information.

### Kubelet configuration merging order

On startup, the kubelet merges configuration from:

* Feature gates specified over the command line (lowest precedence).
* The kubelet configuration.
* Drop-in configuration files, according to sort order.
* Command line arguments excluding feature gates (highest precedence).

The config drop-in dir mechanism for the kubelet is similar but different from how the `kubeadm` tool allows you to patch configuration.
The `kubeadm` tool uses a specific patching strategy
for its configuration, whereas the only patch strategy for kubelet configuration drop-in files is `replace`.
The kubelet determines the order of merges based on sorting the **suffixes** alphanumerically,
and replaces every field present in a higher priority file.
