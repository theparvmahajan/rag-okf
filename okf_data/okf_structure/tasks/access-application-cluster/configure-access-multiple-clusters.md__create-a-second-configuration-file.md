---
id: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#create-a-second-configuration-file
kind: section
title: Create a second configuration file
source: tasks/access-application-cluster/configure-access-multiple-clusters.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
heading: Create a second configuration file
parent: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#define-clusters-users-and-contexts
next_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#set-the-kubeconfig-environment-variable
word_count: 41
---

In your `config-exercise` directory, create a file named `config-demo-2` with this content:

```yaml
apiVersion: v1
kind: Config
preferences: {}

contexts:
- context:
    cluster: development
    namespace: ramp
    user: developer
  name: dev-ramp-up
```

The preceding configuration file defines a new context named `dev-ramp-up`.
