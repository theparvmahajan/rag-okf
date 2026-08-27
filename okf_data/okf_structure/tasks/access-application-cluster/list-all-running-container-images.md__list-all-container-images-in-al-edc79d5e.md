---
id: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-all-container-images-in-all-namespaces
kind: section
title: List all Container images in all namespaces
source: tasks/access-application-cluster/list-all-running-container-images.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/list-all-running-container-images/
heading: List all Container images in all namespaces
parent: okf-structure/tasks/access-application-cluster/list-all-running-container-images
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#prerequisites
next_sibling: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-container-images-by-pod
word_count: 167
---

- Fetch all Pods in all namespaces using `kubectl get pods --all-namespaces`
- Format the output to include only the list of Container image names
  using `-o jsonpath={.items[*].spec['initContainers', 'containers'][*].image}`.  This will recursively parse out the
  `image` field from the returned json.
  - See the jsonpath reference
    for further information on how to use jsonpath.
- Format the output using standard tools: `tr`, `sort`, `uniq`
  - Use `tr` to replace spaces with newlines
  - Use `sort` to sort the results
  - Use `uniq` to aggregate image counts

```shell
kubectl get pods --all-namespaces -o jsonpath="{.items[*].spec['initContainers', 'containers'][*].image}" |\
tr -s '[[:space:]]' '\n' |\
sort |\
uniq -c
```
The jsonpath is interpreted as follows:

- `.items[*]`: for each returned value
- `.spec`: get the spec
- `['initContainers', 'containers'][*]`: for each container
- `.image`: get the image

When fetching a single Pod by name, for example `kubectl get pod nginx`,
the `.items[*]` portion of the path should be omitted because a single
Pod is returned instead of a list of items.
