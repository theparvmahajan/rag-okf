---
id: okf-structure/tasks/configure-pod-container/share-process-namespace.md#configure-a-pod
kind: section
title: Configure a Pod
source: tasks/configure-pod-container/share-process-namespace.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/
heading: Configure a Pod
parent: okf-structure/tasks/configure-pod-container/share-process-namespace
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/share-process-namespace.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/share-process-namespace.md#understanding-process-namespace-sharing
word_count: 266
---

Process namespace sharing is enabled using the `shareProcessNamespace` field of
`.spec` for a Pod. For example:

1. Create the pod `nginx` on your cluster:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/share-process-namespace.yaml
   ```

1. Attach to the `shell` container and run `ps`:

   ```shell
   kubectl exec -it nginx -c shell -- /bin/sh
   ```

   If you don't see a command prompt, try pressing enter. In the container shell:

   ```shell
   # run this inside the "shell" container
   ps ax
   ```

   The output is similar to this:

   ```none
   PID   USER     TIME  COMMAND
       1 root      0:00 /pause
       8 root      0:00 nginx: master process nginx -g daemon off;
      14 101       0:00 nginx: worker process
      15 root      0:00 sh
      21 root      0:00 ps ax
   ```

You can signal processes in other containers. For example, send `SIGHUP` to
`nginx` to restart the worker process. This requires the `SYS_PTRACE` capability.

```shell
# run this inside the "shell" container
kill -HUP 8   # change "8" to match the PID of the nginx leader process, if necessary
ps ax
```

The output is similar to this:

```none
PID   USER     TIME  COMMAND
    1 root      0:00 /pause
    8 root      0:00 nginx: master process nginx -g daemon off;
   15 root      0:00 sh
   22 101       0:00 nginx: worker process
   23 root      0:00 ps ax
```

It's even possible to access the file system of another container using the
`/proc/$pid/root` link.

```shell
# run this inside the "shell" container
# change "8" to the PID of the Nginx process, if necessary
head /proc/8/root/etc/nginx/nginx.conf
```

The output is similar to this:

```none
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
```
