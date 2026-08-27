---
id: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration.md#update-the-preferred-storage-schema-of-a-crd
kind: section
title: Update the preferred storage schema of a CRD
source: tasks/manage-kubernetes-objects/storage-version-migration.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/storage-version-migration/
heading: Update the preferred storage schema of a CRD
parent: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration.md#re-encrypt-kubernetes-secrets-using-storage-version-migration
next_sibling: null
word_count: 710
---

Consider a scenario where a CustomResourceDefinition
(CRD) is created to serve custom resources (CRs) and is set as the preferred storage schema. When it's time
to introduce v2 of the CRD, it can be added for serving only with a conversion
webhook. This enables a smoother transition where users can create CRs using
either the v1 or v2 schema, with the webhook in place to perform the necessary
schema conversion between them. Before setting v2 as the preferred storage schema
version, it's important to ensure that all existing CRs stored as v1 are migrated to v2.
This migration can be achieved through _Storage Version Migration_ to migrate all CRs from v1 to v2.

- Create a manifest for the CRD, named `test-crd.yaml`, as follows:

  ```yaml
  apiVersion: apiextensions.k8s.io/v1
  kind: CustomResourceDefinition
  metadata:
    name: selfierequests.example.com
  spec:
    group: example.com
    names:
      plural: selfierequests
      singular: selfierequest
      kind: SelfieRequest
      listKind: SelfieRequestList
    scope: Namespaced
    versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            hostPort:
              type: string
    conversion:
      strategy: Webhook
      webhook:
        clientConfig:
          url: "https://127.0.0.1:9443/crdconvert"
          caBundle: <CABundle info>
      conversionReviewVersions:
      - v1
      - v2
  ```

  The stored version at this point should be `v1`, confirm this by running:
  ```shell
  kubectl get crd selfierequests.example.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}'
  ```

  Create CRD using kubectl:

  ```shell
  kubectl apply -f test-crd.yaml
  ```

- Create a manifest for an example testcrd. Name the manifest `cr1.yaml` and use these contents:

  ```yaml
  apiVersion: example.com/v1
  kind: SelfieRequest
  metadata:
    name: cr1
    namespace: default
  ```

  Create CR using kubectl:

  ```shell
  kubectl apply -f cr1.yaml
  ```

- Verify that CR is written and stored as v1 by getting the object from etcd.

  ```shell
  ETCDCTL_API=3 etcdctl get /kubernetes.io/example.com/testcrds/default/cr1 [...] | hexdump -C
  ```

  where `[...]` contains the additional arguments for connecting to the etcd server.

- Update the CRD `test-crd.yaml` to include v2 version for serving and storage
  and v1 as serving only, as follows:

  ```yaml
  apiVersion: apiextensions.k8s.io/v1
  kind: CustomResourceDefinition
  metadata:
  name: selfierequests.example.com
  spec:
    group: example.com
    names:
      plural: selfierequests
      singular: selfierequest
      kind: SelfieRequest
      listKind: SelfieRequestList
    scope: Namespaced
    versions:
      - name: v2
        served: true
        storage: true
        schema:
          openAPIV3Schema:
            type: object
            properties:
              host:
                type: string
              port:
                type: string
      - name: v1
        served: true
        storage: false
        schema:
          openAPIV3Schema:
            type: object
            properties:
              hostPort:
                type: string
    conversion:
      strategy: Webhook
      webhook:
        clientConfig:
          url: "https://127.0.0.1:9443/crdconvert"
          caBundle: <CABundle info>
        conversionReviewVersions:
          - v1
          - v2
  ```

  The stored version now should be `v2`, confirm this:
  ```shell
  kubectl get crd selfierequests.example.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}'
  ```

  Update CRD using kubectl:

  ```shell
  kubectl apply -f test-crd.yaml
  ```

- Create CR resource file with name `cr2.yaml` as follows:

  ```yaml
  apiVersion: example.com/v2
  kind: SelfieRequest
  metadata:
    name: cr2
    namespace: default
  ```

- Create CR using kubectl:

  ```shell
  kubectl apply -f cr2.yaml
  ```

- Verify that CR is written and stored as v2 by getting the object from etcd.

  ```shell
  ETCDCTL_API=3 etcdctl get /kubernetes.io/example.com/testcrds/default/cr2 [...] | hexdump -C
  ```

  where `[...]` contains the additional arguments for connecting to the etcd server.

- Create a StorageVersionMigration manifest named `migrate-crd.yaml`, with the contents as follows:

  ```yaml
  kind: StorageVersionMigration
  apiVersion: storagemigration.k8s.io/v1beta1
  metadata:
    name: crdsvm
  spec:
    resource:
      group: example.com
      resource: selfierequests
  ```

  Create the object using _kubectl_ as follows:

  ```shell
  kubectl apply -f migrate-crd.yaml
  ```

- Monitor migration of secrets using status. Successful migration should have
  `Succeeded` condition set to "True" in the status field. Get the migration resource
  as follows:

  ```shell
  kubectl get storageversionmigration.storagemigration.k8s.io/crdsvm -o yaml
  ```

  The output is similar to:

  ```yaml
  kind: StorageVersionMigration
  apiVersion: storagemigration.k8s.io/v1beta1
  metadata:
    name: crdsvm
    uid: 13062fe4-32d7-47cc-9528-5067fa0c6ac8
    resourceVersion: "111"
    creationTimestamp: "2024-03-12T22:40:01Z"
  spec:
    resource:
      group: example.com
      resource: testcrds
  status:
    conditions:
      - type: Running
        status: "False"
        lastUpdateTime: "2024-03-12T22:40:03Z"
        reason: StorageVersionMigrationInProgress
      - type: Succeeded
        status: "True"
        lastUpdateTime: "2024-03-12T22:40:03Z"
        reason: StorageVersionMigrationSucceeded
    resourceVersion: "106"
  ```

- Verify that previously created cr1 is now written and stored as v2 by getting the object from etcd.

  ```shell
  ETCDCTL_API=3 etcdctl get /kubernetes.io/example.com/testcrds/default/cr1 [...] | hexdump -C
  ```

  where `[...]` contains the additional arguments for connecting to the etcd server.

- Also verify that the CRD's stored version status is now only v2:

  ```shell
  kubectl get crd testcrds.example.com -o yaml
  ```

  The output is similar to:

  ```yaml
  kind: CustomResourceDefinition
  apiVersion: apiextensions.k8s.io/v1
  metadata:
    name: testcrds.example.com
  spec:
    group: example.com
    names:
      kind: TestCRD
      plural: testcrds
    scope: Namespaced
    versions:
      - name: v1
        served: true
        storage: false
      - name: v2
        served: true
        storage: true
  status:
    acceptedNames:
      kind: TestCRD
      plural: testcrds
    conditions:
      - type: Established
        status: "True"
    storedVersions:
      - v2
  ```
