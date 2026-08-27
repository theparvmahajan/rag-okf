---
id: okf-structure/tasks/access-application-cluster/web-ui-dashboard.md#accessing-the-dashboard-ui
kind: section
title: Accessing the Dashboard UI
source: tasks/access-application-cluster/web-ui-dashboard.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/
heading: Accessing the Dashboard UI
parent: okf-structure/tasks/access-application-cluster/web-ui-dashboard
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/web-ui-dashboard.md#deploying-the-dashboard-ui
next_sibling: okf-structure/tasks/access-application-cluster/web-ui-dashboard.md#welcome-view
word_count: 129
---

To protect your cluster data, Dashboard deploys with a minimal RBAC configuration by default.
Currently, Dashboard only supports logging in with a Bearer Token.
To create a token for this demo, you can follow our guide on
creating a sample user.

The sample user created in the tutorial will have administrative privileges and is for educational purposes only.

### Command line proxy

You can enable access to the Dashboard using the `kubectl` command-line tool,
by running the following command:

```
kubectl -n kubernetes-dashboard port-forward svc/kubernetes-dashboard-kong-proxy 8443:443
```

Kubectl will make Dashboard available at https://localhost:8443.

The UI can _only_ be accessed from the machine where the command is executed. See `kubectl port-forward --help` for more options.

The kubeconfig authentication method does **not** support external identity providers
or X.509 certificate-based authentication.
