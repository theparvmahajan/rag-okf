---
id: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-container-images-using-a-go-template-instead-of-jsonpath
kind: section
title: List Container images using a go-template instead of jsonpath
source: tasks/access-application-cluster/list-all-running-container-images.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/list-all-running-container-images/
heading: List Container images using a go-template instead of jsonpath
parent: okf-structure/tasks/access-application-cluster/list-all-running-container-images
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-container-images-filtering-by-pod-namespace
next_sibling: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#whatsnext
word_count: 25
---

As an alternative to jsonpath, Kubectl supports using go-templates
for formatting the output:

```shell
kubectl get pods --all-namespaces -o go-template --template="{{range .items}}{{range .spec.containers}}{{.image}} {{end}}{{end}}"
```
