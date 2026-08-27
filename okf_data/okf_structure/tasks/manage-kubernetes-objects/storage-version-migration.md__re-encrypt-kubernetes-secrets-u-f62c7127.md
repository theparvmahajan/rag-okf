---
id: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration.md#re-encrypt-kubernetes-secrets-using-storage-version-migration
kind: section
title: Re-encrypt Kubernetes secrets using storage version migration
source: tasks/manage-kubernetes-objects/storage-version-migration.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/storage-version-migration/
heading: Re-encrypt Kubernetes secrets using storage version migration
parent: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration.md#prerequisites
next_sibling: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration.md#update-the-preferred-storage-schema-of-a-crd
word_count: 271
---

- To begin with, configure KMS provider
  to encrypt data at rest in etcd using following encryption configuration.

  ```yaml
  kind: EncryptionConfiguration
  apiVersion: apiserver.config.k8s.io/v1
  resources:
  - resources:
    - secrets
    providers:
    - aescbc:
        keys:
        - name: key1
          secret: c2VjcmV0IGlzIHNlY3VyZQ==
  ```

  Make sure to enable automatic reload of encryption
  configuration file by setting `--encryption-provider-config-automatic-reload` to true.

- Create a Secret using kubectl.

  ```shell
  kubectl create secret generic my-secret --from-literal=key1=supersecret
  ```

- Verify
  the serialized data for that Secret object is prefixed with `k8s:enc:aescbc:v1:key1`.

- Update the encryption configuration file as follows to rotate the encryption key.

  ```yaml
  kind: EncryptionConfiguration
  apiVersion: apiserver.config.k8s.io/v1
  resources:
  - resources:
    - secrets
    providers:
    - aescbc:
        keys:
        - name: key2
          secret: c2VjcmV0IGlzIHNlY3VyZSwgaXMgaXQ/
    - aescbc:
        keys:
        - name: key1
          secret: c2VjcmV0IGlzIHNlY3VyZQ==
  ```

- To ensure that previously created secret `my-secret` is re-encrypted
  with new key `key2`, you will use _Storage Version Migration_.

- Create a StorageVersionMigration manifest named `migrate-secret.yaml` as follows:

  ```yaml
  kind: StorageVersionMigration
  apiVersion: storagemigration.k8s.io/v1beta1
  metadata:
    name: secrets-migration
  spec:
    resource:
      group: ""
      resource: secrets
  ```

  Create the object using `kubectl` as follows:

  ```shell
  kubectl apply -f migrate-secret.yaml
  ```

- Monitor migration of Secrets by checking the `.status` of the StorageVersionMigration.
  A successful migration should have its
  `Succeeded` condition set to true. Get the StorageVersionMigration object as follows:

  ```shell
  kubectl wait --for=condition=Succeeded storageversionmigration.storagemigration.k8s.io/secrets-migration
  ```

  The output is similar to:

  ```yaml
  kind: StorageVersionMigration
  apiVersion: storagemigration.k8s.io/v1beta1
  metadata:
    name: secrets-migration
    uid: 628f6922-a9cb-4514-b076-12d3c178967c
    resourceVersion: "90"
    creationTimestamp: "2024-03-12T20:29:45Z"
  spec:
    resource:
      group: ""
      resource: secrets
  status:
    conditions:
    - type: Running
      status: "False"
      lastUpdateTime: "2024-03-12T20:29:46Z"
      reason: StorageVersionMigrationInProgress
    - type: Succeeded
      status: "True"
      lastUpdateTime: "2024-03-12T20:29:46Z"
      reason: StorageVersionMigrationSucceeded
    resourceVersion: "84"
  ```

- Verify
  the stored secret is now prefixed with `k8s:enc:aescbc:v1:key2`.
