---
id: okf-structure/tasks/administer-cluster/decrypt-data.md#decrypt-all-data-decrypting-all-data
kind: section
title: Decrypt all data {#decrypting-all-data}
source: tasks/administer-cluster/decrypt-data.md
url: https://kubernetes.io/docs/tasks/administer-cluster/decrypt-data/
heading: Decrypt all data {#decrypting-all-data}
parent: okf-structure/tasks/administer-cluster/decrypt-data
children: []
prev_sibling: okf-structure/tasks/administer-cluster/decrypt-data.md#determine-whether-encryption-at-rest-is-already-enabled
next_sibling: okf-structure/tasks/administer-cluster/decrypt-data.md#whatsnext
word_count: 364
---

This example shows how to stop encrypting the Secret API at rest. If you are encrypting
other API kinds, adjust the steps to match.

### Locate the encryption configuration file

First, find the API server configuration files. On each control plane node, static Pod manifest
for the kube-apiserver specifies a command line argument, `--encryption-provider-config`.
You are likely to find that this file is mounted into the static Pod using a
`hostPath` volume mount. Once you locate the volume
you can find the file on the node filesystem and inspect it.

### Configure the API server to decrypt objects

To disable encryption at rest, place the `identity` provider as the first
entry in your encryption configuration file.

For example, if your existing EncryptionConfiguration file reads:
```yaml
---
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
    providers:
      - aescbc:
          keys:
            # Do not use this (invalid) example key for encryption
            - name: example
              secret: 2KfZgdiq2K0g2YrYpyDYs9mF2LPZhQ==
```

then change it to:

```yaml
---
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
    providers:
      - identity: {} # add this line
      - aescbc:
          keys:
            - name: example
              secret: 2KfZgdiq2K0g2YrYpyDYs9mF2LPZhQ==
```

and restart the kube-apiserver Pod on this node.

### Reconfigure other control plane hosts {#api-server-config-update-more-1}

If you have multiple API servers in your cluster, you should deploy the changes in turn to each API server.

Make sure that you use the same encryption configuration on each control plane host.

### Force decryption

Then run the following command to force decryption of all Secrets:

```shell
# If you are decrypting a different kind of object, change "secrets" to match.
kubectl get secrets --all-namespaces -o json | kubectl replace -f -
```

Once you have replaced **all** existing encrypted resources with backing data that
don't use encryption, you can remove the encryption settings from the
`kube-apiserver`.

The command line options to remove are:

- `--encryption-provider-config`
- `--encryption-provider-config-automatic-reload`

Restart the kube-apiserver Pod again to apply the new configuration.

### Reconfigure other control plane hosts {#api-server-config-update-more-2}

If you have multiple API servers in your cluster, you should again deploy the changes in turn to each API server.

Make sure that you use the same encryption configuration on each control plane host.
