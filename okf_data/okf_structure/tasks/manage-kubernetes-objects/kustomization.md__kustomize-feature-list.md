---
id: okf-structure/tasks/manage-kubernetes-objects/kustomization.md#kustomize-feature-list
kind: section
title: Kustomize Feature List
source: tasks/manage-kubernetes-objects/kustomization.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/
heading: Kustomize Feature List
parent: okf-structure/tasks/manage-kubernetes-objects/kustomization
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/kustomization.md#how-to-apply-view-delete-objects-using-kustomize
next_sibling: okf-structure/tasks/manage-kubernetes-objects/kustomization.md#whatsnext
word_count: 304
---

| Field | Type | Explanation |
|-------|------|-------------|
| bases | []string | Each entry in this list should resolve to a directory containing a kustomization.yaml file |
| commonAnnotations | map[string]string | annotations to add to all resources |
| commonLabels | map[string]string | labels to add to all resources and selectors |
| configMapGenerator | []ConfigMapArgs | Each entry in this list generates a ConfigMap |
| configurations | []string | Each entry in this list should resolve to a file containing Kustomize transformer configurations |
| crds | []string | Each entry in this list should resolve to an OpenAPI definition file for Kubernetes types |
| generatorOptions | GeneratorOptions | Modify behaviors of all ConfigMap and Secret generator |
| images | []Image | Each entry is to modify the name, tags and/or digest for one image without creating patches |
| labels | map[string]string | Add labels without automatically injecting corresponding selectors |
| namePrefix | string | value of this field is prepended to the names of all resources |
| nameSuffix | string | value of this field is appended to the names of all resources |
| patchesJson6902 | []Patch | Each entry in this list should resolve to a Kubernetes object and a Json Patch |
| patchesStrategicMerge | []string | Each entry in this list should resolve a strategic merge patch of a Kubernetes object |
| replacements | []Replacements | copy the value from a resource's field into any number of specified targets. |
| resources | []string | Each entry in this list must resolve to an existing resource configuration file |
| secretGenerator | []SecretArgs | Each entry in this list generates a Secret |
| vars | []Var | Each entry is to capture text from one resource's field |
