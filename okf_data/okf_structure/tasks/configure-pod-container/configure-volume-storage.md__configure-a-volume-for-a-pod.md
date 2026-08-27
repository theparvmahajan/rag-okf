---
id: okf-structure/tasks/configure-pod-container/configure-volume-storage.md#configure-a-volume-for-a-pod
kind: section
title: Configure a volume for a Pod
source: tasks/configure-pod-container/configure-volume-storage.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-volume-storage/
heading: Configure a volume for a Pod
parent: okf-structure/tasks/configure-pod-container/configure-volume-storage
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-volume-storage.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/configure-volume-storage.md#whatsnext
word_count: 343
---

In this exercise, you create a Pod that runs one Container. This Pod has a
Volume of type
emptyDir
that lasts for the life of the Pod, even if the Container terminates and
restarts. Here is the configuration file for the Pod:

1. Create the Pod:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/storage/redis.yaml
   ```

1. Verify that the Pod's Container is running, and then watch for changes to
   the Pod:

   ```shell
   kubectl get pod redis --watch
   ```

   The output looks like this:

   ```console
   NAME      READY     STATUS    RESTARTS   AGE
   redis     1/1       Running   0          13s
   ```

1. In another terminal, get a shell to the running Container:

   ```shell
   kubectl exec -it redis -- /bin/bash
   ```

1. In your shell, go to `/data/redis`, and then create a file:

   ```shell
   root@redis:/data# cd /data/redis/
   root@redis:/data/redis# echo Hello > test-file
   ```

1. In your shell, list the running processes:

   ```shell
   root@redis:/data/redis# apt-get update
   root@redis:/data/redis# apt-get install procps
   root@redis:/data/redis# ps aux
   ```

   The output is similar to this:

   ```console
   USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
   redis        1  0.1  0.1  33308  3828 ?        Ssl  00:46   0:00 redis-server *:6379
   root        12  0.0  0.0  20228  3020 ?        Ss   00:47   0:00 /bin/bash
   root        15  0.0  0.0  17500  2072 ?        R+   00:48   0:00 ps aux
   ```

1. In your shell, kill the Redis process:

   ```shell
   root@redis:/data/redis# kill <pid>
   ```

   where `<pid>` is the Redis process ID (PID).

1. In your original terminal, watch for changes to the Redis Pod. Eventually,
   you will see something like this:

   ```console
   NAME      READY     STATUS     RESTARTS   AGE
   redis     1/1       Running    0          13s
   redis     0/1       Completed  0         6m
   redis     1/1       Running    1         6m
   ```

At this point, the Container has terminated and restarted. This is because the
Redis Pod has a
restartPolicy
of `Always`.

1. Get a shell into the restarted Container:

   ```shell
   kubectl exec -it redis -- /bin/bash
   ```

1. In your shell, go to `/data/redis`, and verify that `test-file` is still there.

   ```shell
   root@redis:/data/redis# cd /data/redis/
   root@redis:/data/redis# ls
   test-file
   ```

1. Delete the Pod that you created for this exercise:

   ```shell
   kubectl delete pod redis
   ```
