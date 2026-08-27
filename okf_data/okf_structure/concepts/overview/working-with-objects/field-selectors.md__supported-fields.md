---
id: okf-structure/concepts/overview/working-with-objects/field-selectors.md#supported-fields
kind: section
title: Supported fields
source: concepts/overview/working-with-objects/field-selectors.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/
heading: Supported fields
parent: okf-structure/concepts/overview/working-with-objects/field-selectors
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/field-selectors.md#introduction
next_sibling: okf-structure/concepts/overview/working-with-objects/field-selectors.md#supported-operators
word_count: 178
---

Supported field selectors vary by Kubernetes resource type. All resource types support the `metadata.name` and `metadata.namespace` fields. Using unsupported field selectors produces an error. For example:

```shell
kubectl get ingress --field-selector foo.bar=baz
```
```
Error from server (BadRequest): Unable to find "ingresses" that match label selector "", field selector "foo.bar=baz": "foo.bar" is not a known field selector: only "metadata.name", "metadata.namespace"
```

### List of supported fields

| Kind                      | Fields                                                                                                                                                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pod                       | `spec.nodeName``spec.restartPolicy``spec.schedulerName``spec.serviceAccountName``spec.hostNetwork``status.phase``status.podIP``status.podIPs``status.nominatedNodeName`                                                                            |
| Event                     | `involvedObject.kind``involvedObject.namespace``involvedObject.name``involvedObject.uid``involvedObject.apiVersion``involvedObject.resourceVersion``involvedObject.fieldPath``reason``reportingComponent``source``type` |
| Secret                    | `type`                                                                                                                                                                                                                                                          |
| Service                   | `spec.clusterIP``spec.type`                                                                                                                                                                                                                                 |
| Namespace                 | `status.phase`                                                                                                                                                                                                                                                  |
| ReplicaSet                | `status.replicas`                                                                                                                                                                                                                                               |
| ReplicationController     | `status.replicas`                                                                                                                                                                                                                                               |
| Job                       | `status.successful`                                                                                                                                                                                                                                             |
| Node                      | `spec.unschedulable`                                                                                                                                                                                                                                            |
| CertificateSigningRequest | `spec.signerName`                                                                                                                                                                                                                                               |

### Custom resources fields

All custom resource types support the `metadata.name` and `metadata.namespace` fields.

Additionally, the `spec.versions[*].selectableFields` field of a CustomResourceDefinition
declares which other fields in a custom resource may be used in field selectors. See selectable fields for custom resources
for more information about how to use field selectors with CustomResourceDefinitions.
