---
id: okf-structure/tasks/administer-cluster/kms-provider.md#encrypting-your-data-with-the-kms-provider
kind: section
title: Encrypting your data with the KMS provider
source: tasks/administer-cluster/kms-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/
heading: Encrypting your data with the KMS provider
parent: okf-structure/tasks/administer-cluster/kms-provider
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#implementing-a-kms-plugin
next_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#verifying-that-the-data-is-encrypted
word_count: 406
---

To encrypt the data:

1. Create a new `EncryptionConfiguration` file using the appropriate properties for the `kms` provider
to encrypt resources like Secrets and ConfigMaps. If you want to encrypt an extension API that is
defined in a CustomResourceDefinition, your cluster must be running Kubernetes v1.26 or newer.

1. Set the `--encryption-provider-config` flag on the kube-apiserver to point to the location of the configuration file.

1. `--encryption-provider-config-automatic-reload` boolean argument 
   determines if the file set by `--encryption-provider-config` should be
   automatically reloaded
   if the disk contents change.

1. Restart your API server.

### KMS v1 {#encrypting-your-data-with-the-kms-provider-kms-v1}

   ```yaml
   apiVersion: apiserver.config.k8s.io/v1
   kind: EncryptionConfiguration
   resources:
     - resources:
         - secrets
         - configmaps
         - pandas.awesome.bears.example
       providers:
         - kms:
             name: myKmsPluginFoo
             endpoint: unix:///tmp/socketfile-foo.sock
             cachesize: 100
             timeout: 3s
         - kms:
             name: myKmsPluginBar
             endpoint: unix:///tmp/socketfile-bar.sock
             cachesize: 100
             timeout: 3s
   ```

### KMS v2 {#encrypting-your-data-with-the-kms-provider-kms-v2}

   ```yaml
   apiVersion: apiserver.config.k8s.io/v1
   kind: EncryptionConfiguration
   resources:
     - resources:
         - secrets
         - configmaps
         - pandas.awesome.bears.example
       providers:
         - kms:
             apiVersion: v2
             name: myKmsPluginFoo
             endpoint: unix:///tmp/socketfile-foo.sock
             timeout: 3s
         - kms:
             apiVersion: v2
             name: myKmsPluginBar
             endpoint: unix:///tmp/socketfile-bar.sock
             timeout: 3s
   ```

Setting `--encryption-provider-config-automatic-reload` to `true` collapses all health checks to a single health check endpoint. Individual health checks are only available when KMS v1 providers are in use and the encryption config is not auto-reloaded.

The following table summarizes the health check endpoints for each KMS version:

| KMS configurations | Without Automatic Reload | With Automatic Reload |
| ------------------ | ------------------------ | --------------------- |
| KMS v1 only        | Individual Healthchecks  | Single Healthcheck    |
| KMS v2 only        | Single Healthcheck       | Single Healthcheck    |
| Both KMS v1 and v2 | Individual Healthchecks  | Single Healthcheck    |
| No KMS             | None                     | Single Healthcheck    |

`Single Healthcheck` means that the only health check endpoint is `/healthz/kms-providers`.

`Individual Healthchecks` means that each KMS plugin has an associated health check endpoint based on its location in the encryption config: `/healthz/kms-provider-0`, `/healthz/kms-provider-1` etc.

These healthcheck endpoint paths are hard coded and generated/controlled by the server. The indices for individual healthchecks corresponds to the order in which the KMS encryption config is processed.

Until the steps defined in Ensuring all secrets are encrypted are performed, the `providers` list should end with the `identity: {}` provider to allow unencrypted data to be read.  Once all resources are encrypted, the `identity` provider should be removed to prevent the API server from honoring unencrypted data.

For details about the `EncryptionConfiguration` format, please check the
API server encryption API reference.
