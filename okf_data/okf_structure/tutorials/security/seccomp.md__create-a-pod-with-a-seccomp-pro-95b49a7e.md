---
id: okf-structure/tutorials/security/seccomp.md#create-a-pod-with-a-seccomp-profile-that-only-allows-necessary-syscalls
kind: section
title: Create a Pod with a seccomp profile that only allows necessary syscalls
source: tutorials/security/seccomp.md
url: https://kubernetes.io/docs/tutorials/security/seccomp/
heading: Create a Pod with a seccomp profile that only allows necessary syscalls
parent: okf-structure/tutorials/security/seccomp
children: []
prev_sibling: okf-structure/tutorials/security/seccomp.md#create-a-pod-with-a-seccomp-profile-that-causes-violation
next_sibling: okf-structure/tutorials/security/seccomp.md#enable-the-use-of-runtimedefault-as-the-default-seccomp-profile-for-all-workloads
word_count: 337
---

If you take a look at the `fine-grained.json` profile, you will notice some of the syscalls
seen in syslog of the first example where the profile set `"defaultAction":
"SCMP_ACT_LOG"`. Now the profile is setting `"defaultAction": "SCMP_ACT_ERRNO"`,
but explicitly allowing a set of syscalls in the `"action": "SCMP_ACT_ALLOW"`
block. Ideally, the container will run successfully and you will see no messages
sent to `syslog`.

The manifest for this example is:

Create the Pod in your cluster:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/seccomp/ga/fine-pod.yaml
```

```shell
kubectl get pod fine-pod
```

The Pod should be showing as having started successfully:
```
NAME        READY   STATUS    RESTARTS   AGE
fine-pod   1/1     Running   0          30s
```

Open up a new terminal window and use `tail` to monitor for log entries that
mention calls from `http-echo`:

```shell
# The log path on your computer might be different from "/var/log/syslog"
tail -f /var/log/syslog | grep 'http-echo'
```

Next, expose the Pod with a NodePort Service:

```shell
kubectl expose pod fine-pod --type NodePort --port 5678
```

Check what port the Service has been assigned on the node:

```shell
kubectl get service fine-pod
```

The output is similar to:
```
NAME        TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
fine-pod    NodePort   10.111.36.142   <none>        5678:32373/TCP   72s
```

Use `curl` to access that endpoint from inside the kind control plane container:

```shell
# Change 32373 to the port number you saw from "kubectl get service fine-pod"
docker exec -it kind-control-plane curl localhost:32373
```

```
just made some syscalls!
```

You should see no output in the `syslog`. This is because the profile allowed all
necessary syscalls and specified that an error should occur if one outside of
the list is invoked. This is an ideal situation from a security perspective, but
required some effort in analyzing the program. It would be nice if there was a
simple way to get closer to this security without requiring as much effort.

Delete the Service and the Pod before moving to the next section:

```shell
kubectl delete service fine-pod --wait
kubectl delete pod fine-pod --wait --now
```
