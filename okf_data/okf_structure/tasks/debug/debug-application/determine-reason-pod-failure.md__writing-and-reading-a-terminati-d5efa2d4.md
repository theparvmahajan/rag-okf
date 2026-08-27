---
id: okf-structure/tasks/debug/debug-application/determine-reason-pod-failure.md#writing-and-reading-a-termination-message
kind: section
title: Writing and reading a termination message
source: tasks/debug/debug-application/determine-reason-pod-failure.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/
heading: Writing and reading a termination message
parent: okf-structure/tasks/debug/debug-application/determine-reason-pod-failure
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/determine-reason-pod-failure.md#prerequisites
next_sibling: okf-structure/tasks/debug/debug-application/determine-reason-pod-failure.md#customizing-the-termination-message
word_count: 212
---

In this exercise, you create a Pod that runs one container.
The manifest for that Pod specifies a command that runs when the container starts:

1. Create a Pod based on the YAML configuration file:

    ```shell
    kubectl apply -f https://k8s.io/examples/debug/termination.yaml
    ```
    
    In the YAML file, in the `command` and `args` fields, you can see that the
    container sleeps for 10 seconds and then writes "Sleep expired" to
    the `/dev/termination-log` file. After the container writes
    the "Sleep expired" message, it terminates.

1. Display information about the Pod:

    ```shell
    kubectl get pod termination-demo
    ```

    Repeat the preceding command until the Pod is no longer running.

1. Display detailed information about the Pod:

    ```shell
    kubectl get pod termination-demo --output=yaml
    ```

    The output includes the "Sleep expired" message:

    ```yaml
    apiVersion: v1
    kind: Pod
    ...
        lastState:
          terminated:
            containerID: ...
            exitCode: 0
            finishedAt: ...
            message: |
              Sleep expired
            ...
    ```

1. Use a Go template to filter the output so that it includes only the termination message:

    ```shell
    kubectl get pod termination-demo -o go-template="{{range .status.containerStatuses}}{{.lastState.terminated.message}}{{end}}"
    ```

If you are running a multi-container Pod, you can use a Go template to include the container's name.
By doing so, you can discover which of the containers is failing:

```shell
kubectl get pod multi-container-pod -o go-template='{{range .status.containerStatuses}}{{printf "%s:\n%s\n\n" .name .lastState.terminated.message}}{{end}}'
```
