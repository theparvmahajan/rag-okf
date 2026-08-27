---
id: okf-structure/tasks/manage-daemon/update-daemon-set.md#performing-a-rolling-update
kind: section
title: Performing a Rolling Update
source: tasks/manage-daemon/update-daemon-set.md
url: https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/
heading: Performing a Rolling Update
parent: okf-structure/tasks/manage-daemon/update-daemon-set
children: []
prev_sibling: okf-structure/tasks/manage-daemon/update-daemon-set.md#daemonset-update-strategy
next_sibling: okf-structure/tasks/manage-daemon/update-daemon-set.md#troubleshooting
word_count: 333
---

To enable the rolling update feature of a DaemonSet, you must set its
`.spec.updateStrategy.type` to `RollingUpdate`.

You may want to set
`.spec.updateStrategy.rollingUpdate.maxUnavailable` 
(default to 1),
`.spec.minReadySeconds`
(default to 0) and
`.spec.updateStrategy.rollingUpdate.maxSurge`
(defaults to 0) as well.

### Creating a DaemonSet with `RollingUpdate` update strategy

This YAML file specifies a DaemonSet with an update strategy as 'RollingUpdate'

After verifying the update strategy of the DaemonSet manifest, create the DaemonSet:

```shell
kubectl create -f https://k8s.io/examples/controllers/fluentd-daemonset.yaml
```

Alternatively, use `kubectl apply` to create the same DaemonSet if you plan to
update the DaemonSet with `kubectl apply`.

```shell
kubectl apply -f https://k8s.io/examples/controllers/fluentd-daemonset.yaml
```

### Checking DaemonSet `RollingUpdate` update strategy

Check the update strategy of your DaemonSet, and make sure it's set to
`RollingUpdate`:

```shell
kubectl get ds/fluentd-elasticsearch -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}' -n kube-system
```

If you haven't created the DaemonSet in the system, check your DaemonSet
manifest with the following command instead:

```shell
kubectl apply -f https://k8s.io/examples/controllers/fluentd-daemonset.yaml --dry-run=client -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
```

The output from both commands should be:

```
RollingUpdate
```

If the output isn't `RollingUpdate`, go back and modify the DaemonSet object or
manifest accordingly.

### Updating a DaemonSet template

Any updates to a `RollingUpdate` DaemonSet `.spec.template` will trigger a rolling
update. Let's update the DaemonSet by applying a new YAML file. This can be done with several different `kubectl` commands.

#### Declarative commands

If you update DaemonSets using
configuration files,
use `kubectl apply`:

```shell
kubectl apply -f https://k8s.io/examples/controllers/fluentd-daemonset-update.yaml
```

#### Imperative commands

If you update DaemonSets using
imperative commands,
use `kubectl edit` :

```shell
kubectl edit ds/fluentd-elasticsearch -n kube-system
```

##### Updating only the container image

If you only need to update the container image in the DaemonSet template, i.e.
`.spec.template.spec.containers[*].image`, use `kubectl set image`:

```shell
kubectl set image ds/fluentd-elasticsearch fluentd-elasticsearch=quay.io/fluentd_elasticsearch/fluentd:v2.6.0 -n kube-system
```

### Watching the rolling update status

Finally, watch the rollout status of the latest DaemonSet rolling update:

```shell
kubectl rollout status ds/fluentd-elasticsearch -n kube-system
```

When the rollout is complete, the output is similar to this:

```shell
daemonset "fluentd-elasticsearch" successfully rolled out
```
