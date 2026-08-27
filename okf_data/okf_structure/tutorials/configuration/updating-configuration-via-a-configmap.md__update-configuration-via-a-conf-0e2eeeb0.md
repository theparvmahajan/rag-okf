---
id: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap.md#update-configuration-via-a-configmap-mounted-as-a-volume-rollout-configmap-volume
kind: section
title: Update configuration via a ConfigMap mounted as a Volume {#rollout-configmap-volume}
source: tutorials/configuration/updating-configuration-via-a-configmap.md
url: https://kubernetes.io/docs/tutorials/configuration/updating-configuration-via-a-configmap/
heading: Update configuration via a ConfigMap mounted as a Volume {#rollout-configmap-volume}
parent: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap
children: []
prev_sibling: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap.md#objectives
next_sibling: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap.md#update-environment-variables-of-a-pod-via-a-configmap-rollout-configmap-env
word_count: 568
---

Use the `kubectl create configmap` command to create a ConfigMap from
literal values:

```shell
kubectl create configmap sport --from-literal=sport=football
```

Below is an example of a Deployment manifest with the ConfigMap `sport` mounted as a
volume into the Pod's only container.

Create the Deployment:

```shell
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-as-volume.yaml
```

Check the pods for this Deployment to ensure they are ready (matching by
selector):

```shell
kubectl get pods --selector=app.kubernetes.io/name=configmap-volume
```

You should see an output similar to:

```
NAME                                READY   STATUS    RESTARTS   AGE
configmap-volume-6b976dfdcf-qxvbm   1/1     Running   0          72s
configmap-volume-6b976dfdcf-skpvm   1/1     Running   0          72s
configmap-volume-6b976dfdcf-tbc6r   1/1     Running   0          72s
```

On each node where one of these Pods is running, the kubelet fetches the data for
that ConfigMap and translates it to files in a local volume.
The kubelet then mounts that volume into the container, as specified in the Pod template.
The code running in that container loads the information from the file
and uses it to print a report to stdout.
You can check this report by viewing the logs for one of the Pods in that Deployment:

```shell
# Pick one Pod that belongs to the Deployment, and view its logs
kubectl logs deployments/configmap-volume
```

You should see an output similar to:

```
Found 3 pods, using pod/configmap-volume-76d9c5678f-x5rgj
Thu Jan  4 14:06:46 UTC 2024 My preferred sport is football
Thu Jan  4 14:06:56 UTC 2024 My preferred sport is football
Thu Jan  4 14:07:06 UTC 2024 My preferred sport is football
Thu Jan  4 14:07:16 UTC 2024 My preferred sport is football
Thu Jan  4 14:07:26 UTC 2024 My preferred sport is football
```

Edit the ConfigMap:

```shell
kubectl edit configmap sport
```

In the editor that appears, change the value of key `sport` from `football` to `cricket`. Save your changes.
The kubectl tool updates the ConfigMap accordingly (if you see an error, try again).

Here's an example of how that manifest could look after you edit it:

```yaml
apiVersion: v1
data:
  sport: cricket
kind: ConfigMap
# You can leave the existing metadata as they are.
# The values you'll see won't exactly match these.
metadata:
  creationTimestamp: "2024-01-04T14:05:06Z"
  name: sport
  namespace: default
  resourceVersion: "1743935"
  uid: 024ee001-fe72-487e-872e-34d6464a8a23
```

You should see the following output:

```
configmap/sport edited
```

Tail (follow the latest entries in) the logs of one of the pods that belongs to this Deployment:

```shell
kubectl logs deployments/configmap-volume --follow
```

After few seconds, you should see the log output change as follows:

```
Thu Jan  4 14:11:36 UTC 2024 My preferred sport is football
Thu Jan  4 14:11:46 UTC 2024 My preferred sport is football
Thu Jan  4 14:11:56 UTC 2024 My preferred sport is football
Thu Jan  4 14:12:06 UTC 2024 My preferred sport is cricket
Thu Jan  4 14:12:16 UTC 2024 My preferred sport is cricket
```

When you have a ConfigMap that is mapped into a running Pod using either a
`configMap` volume or a `projected` volume, and you update that ConfigMap,
the running Pod sees the update almost immediately.  
However, your application only sees the change if it is written to either poll for changes,
or watch for file updates.  
An application that loads its configuration once at startup will not notice a change.

The total delay from the moment when the ConfigMap is updated to the moment when
new keys are projected to the Pod can be as long as kubelet sync period.  
Also check Mounted ConfigMaps are updated automatically.
