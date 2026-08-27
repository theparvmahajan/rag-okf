---
id: okf-structure/tasks/run-application/update-deployment-rolling.md#performing-a-rolling-update
kind: section
title: Performing a rolling update
source: tasks/run-application/update-deployment-rolling.md
url: https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/
heading: Performing a rolling update
parent: okf-structure/tasks/run-application/update-deployment-rolling
children: []
prev_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#prerequisites
next_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#monitoring-rollout-progress
word_count: 199
---

Any change to the `.spec.template` field of a Deployment triggers a rolling
update. Kubernetes creates new Pods with the updated configuration and gradually
terminates old Pods.

### Updating with `kubectl apply`

You can trigger a rolling update by editing the Deployment manifest and applying the change. This approach works well when you keep manifests in version control.

Export the current Deployment to a local file:

```shell
kubectl get deployment nginx-deployment -o yaml > /tmp/nginx-deployment.yaml
```

Edit `/tmp/nginx-deployment.yaml` and change `.spec.template.spec.containers[0].image`
from `nginx:1.14.2` to `nginx:1.16.1`.

Before applying, compare your local changes against the cluster state:

```shell
kubectl diff -f /tmp/nginx-deployment.yaml
```

The output is similar to:

```
diff -u -N /tmp/LIVE/apps.v1.Deployment.default.nginx-deployment /tmp/MERGED/apps.v1.Deployment.default.nginx-deployment
--- /tmp/LIVE/apps.v1.Deployment...
+++ /tmp/MERGED/apps.v1.Deployment...
@@ -29,7 +29,7 @@
       containers:
-      - image: nginx:1.14.2
+      - image: nginx:1.16.1
         name: nginx
```

Apply the updated manifest:

```shell
kubectl apply -f /tmp/nginx-deployment.yaml
```

### Updating only the container image

To update the container image without editing a manifest file, use
`kubectl set image`:

```shell
kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
```

The output is similar to:

```
deployment.apps/nginx-deployment image updated
```

Verify the image was updated:

```shell
kubectl get deployment nginx-deployment -o jsonpath='{.spec.template.spec.containers[0].image}'
```

The output is similar to:

```
nginx:1.16.1
```
