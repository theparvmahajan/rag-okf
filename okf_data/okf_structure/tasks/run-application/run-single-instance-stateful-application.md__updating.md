---
id: okf-structure/tasks/run-application/run-single-instance-stateful-application.md#updating
kind: section
title: Updating
source: tasks/run-application/run-single-instance-stateful-application.md
url: https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/
heading: Updating
parent: okf-structure/tasks/run-application/run-single-instance-stateful-application
children: []
prev_sibling: okf-structure/tasks/run-application/run-single-instance-stateful-application.md#accessing-the-mysql-instance
next_sibling: okf-structure/tasks/run-application/run-single-instance-stateful-application.md#deleting-a-deployment
word_count: 112
---

The image or any other part of the Deployment can be updated as usual
with the `kubectl apply` command. Here are some precautions that are
specific to stateful apps:

- Don't scale the app. This setup is for single-instance apps
  only. The underlying PersistentVolume can only be mounted to one
  Pod. For clustered stateful apps, see the
  StatefulSet documentation.
- Use `strategy:` `type: Recreate` in the Deployment configuration
  YAML file. This instructs Kubernetes to _not_ use rolling
  updates. Rolling updates will not work, as you cannot have more than
  one Pod running at a time. The `Recreate` strategy will stop the
  first pod before creating a new one with the updated configuration.
