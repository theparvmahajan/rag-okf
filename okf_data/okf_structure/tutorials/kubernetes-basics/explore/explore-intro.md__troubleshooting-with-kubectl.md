---
id: okf-structure/tutorials/kubernetes-basics/explore/explore-intro.md#troubleshooting-with-kubectl
kind: section
title: Troubleshooting with kubectl
source: tutorials/kubernetes-basics/explore/explore-intro.md
url: https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/
heading: Troubleshooting with kubectl
parent: okf-structure/tutorials/kubernetes-basics/explore/explore-intro
children: []
prev_sibling: okf-structure/tutorials/kubernetes-basics/explore/explore-intro.md#nodes
next_sibling: okf-structure/tutorials/kubernetes-basics/explore/explore-intro.md#whatsnext
word_count: 639
---

In Module 2, you used
the kubectl command-line interface. You'll continue to use it in Module 3 to get
information about deployed applications and their environments. The most common
operations can be done with the following kubectl subcommands:

* `kubectl get` - list resources
* `kubectl describe` - show detailed information about a resource
* `kubectl logs`  - print the logs from a container in a pod
* `kubectl exec` - execute a command on a container in a pod

You can use these commands to see when applications were deployed, what their current
statuses are, where they are running and what their configurations are.

Now that we know more about our cluster components and the command line, let's
explore our application.

### Check application configuration

Let's verify that the application we deployed in the previous scenario is running.
We'll use the `kubectl get` command and look for existing Pods:

```shell
kubectl get pods
```

If no pods are running, please wait a couple of seconds and list the Pods again.
You can continue once you see one Pod running.

Next, to view what containers are inside that Pod and what images are used to build
those containers we run the `kubectl describe pods` command:

```shell
kubectl describe pods
```

We see here details about the Pod’s container: IP address, the ports used and a
list of events related to the lifecycle of the Pod.

The output of the `describe` subcommand is extensive and covers some concepts that
we didn’t explain yet, but don’t worry, they will become familiar by the end of this tutorial.

The `describe` subcommand can be used to get detailed information about most of the
Kubernetes primitives, including Nodes, Pods, and Deployments. The describe output is
designed to be human readable, not to be scripted against.

### Show the app in the terminal

Recall that Pods are running in an isolated, private network - so we need to proxy access
to them so we can debug and interact with them. To do this, we'll use the `kubectl proxy`
command to run a proxy in a **second terminal**. Open a new terminal window, and
in that new terminal, run:

```shell
kubectl proxy
```

Now again, we'll get the Pod name and query that pod directly through the proxy.
To get the Pod name and store it in the `POD_NAME` environment variable:

```shell
export POD_NAME="$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')"
echo Name of the Pod: $POD_NAME
```

To see the output of our application, run a `curl` request:

```shell
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME:8080/proxy/
```

The URL is the route to the API of the Pod.

We don't need to specify the container name, because we only have one container inside the pod.

### Executing commands on the container

We can execute commands directly on the container once the Pod is up and running.
For this, we use the `exec` subcommand and use the name of the Pod as a parameter.
Let’s list the environment variables:

```shell
kubectl exec "$POD_NAME" -- env
```

Again, it's worth mentioning that the name of the container itself can be omitted
since we only have a single container in the Pod.

Next let’s start a bash session in the Pod’s container:

```shell
kubectl exec -ti $POD_NAME -- bash
```

We have now an open console on the container where we run our NodeJS application.
The source code of the app is in the `server.js` file:

```shell
cat server.js
```

You can check that the application is up by running a curl command:

```shell
curl http://localhost:8080
```

Here we used `localhost` because we executed the command inside the NodeJS Pod.
If you cannot connect to `localhost:8080`, check to make sure you have run the
`kubectl exec` command and are launching the command from within the Pod.

To close your container connection, type `exit`.
