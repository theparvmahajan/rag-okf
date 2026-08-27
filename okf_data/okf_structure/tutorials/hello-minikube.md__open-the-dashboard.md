---
id: okf-structure/tutorials/hello-minikube.md#open-the-dashboard
kind: section
title: Open the Dashboard
source: tutorials/hello-minikube.md
url: https://kubernetes.io/docs/tutorials/hello-minikube/
heading: Open the Dashboard
parent: okf-structure/tutorials/hello-minikube
children: []
prev_sibling: okf-structure/tutorials/hello-minikube.md#check-the-status-of-the-minikube-cluster
next_sibling: okf-structure/tutorials/hello-minikube.md#create-a-deployment
word_count: 237
---

Open the Kubernetes dashboard. You can do this two different ways:

Open a **new** terminal, and run:
```shell
# Start a new terminal, and leave this running.
minikube dashboard
```

Now, switch back to the terminal where you ran `minikube start`.

The `dashboard` command enables the dashboard add-on and opens the proxy in the default web browser.
You can create Kubernetes resources on the dashboard such as Deployment and Service.

To find out how to avoid directly invoking the browser from the terminal and get a URL for the web dashboard, see the "URL copy and paste" tab.

By default, the dashboard is only accessible from within the internal Kubernetes virtual network.
The `dashboard` command creates a temporary proxy to make the dashboard accessible from outside the Kubernetes virtual network.

To stop the proxy, run `Ctrl+C` to exit the process.
After the command exits, the dashboard remains running in the Kubernetes cluster.
You can run the `dashboard` command again to create another proxy to access the dashboard.

If you don't want minikube to open a web browser for you, run the `dashboard` subcommand with the
`--url` flag. `minikube` outputs a URL that you can open in the browser you prefer.

Open a **new** terminal, and run:
```shell
# Start a new terminal, and leave this running.
minikube dashboard --url
```

Now, you can use this URL and switch back to the terminal where you ran `minikube start`.
