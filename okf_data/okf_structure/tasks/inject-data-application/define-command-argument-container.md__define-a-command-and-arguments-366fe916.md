---
id: okf-structure/tasks/inject-data-application/define-command-argument-container.md#define-a-command-and-arguments-when-you-create-a-pod
kind: section
title: Define a command and arguments when you create a Pod
source: tasks/inject-data-application/define-command-argument-container.md
url: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/
heading: Define a command and arguments when you create a Pod
parent: okf-structure/tasks/inject-data-application/define-command-argument-container
children: []
prev_sibling: okf-structure/tasks/inject-data-application/define-command-argument-container.md#prerequisites
next_sibling: okf-structure/tasks/inject-data-application/define-command-argument-container.md#use-environment-variables-to-define-arguments
word_count: 222
---

When you create a Pod, you can define a command and arguments for the
containers that run in the Pod. To define a command, include the `command`
field in the configuration file. To define arguments for the command, include
the `args` field in the configuration file. The command and arguments that
you define cannot be changed after the Pod is created.

The command and arguments that you define in the configuration file
override the default command and arguments provided by the container image.
If you define args, but do not define a command, the default command is used
with your new arguments.

The `command` field corresponds to `ENTRYPOINT`, and the `args` field corresponds to `CMD` in some container runtimes.

In this exercise, you create a Pod that runs one container. The configuration
file for the Pod defines a command and two arguments:

1. Create a Pod based on the YAML configuration file:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/commands.yaml
   ```

1. List the running Pods:

   ```shell
   kubectl get pods
   ```

   The output shows that the container that ran in the command-demo Pod has
   completed.

1. To see the output of the command that ran in the container, view the logs
from the Pod:

   ```shell
   kubectl logs command-demo
   ```

   The output shows the values of the HOSTNAME and KUBERNETES_PORT environment
   variables:

   ```
   command-demo
   tcp://10.3.240.1:443
   ```
