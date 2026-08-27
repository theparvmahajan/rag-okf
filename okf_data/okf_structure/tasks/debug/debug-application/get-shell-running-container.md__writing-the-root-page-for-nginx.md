---
id: okf-structure/tasks/debug/debug-application/get-shell-running-container.md#writing-the-root-page-for-nginx
kind: section
title: Writing the root page for nginx
source: tasks/debug/debug-application/get-shell-running-container.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/
heading: Writing the root page for nginx
parent: okf-structure/tasks/debug/debug-application/get-shell-running-container
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/get-shell-running-container.md#getting-a-shell-to-a-container
next_sibling: okf-structure/tasks/debug/debug-application/get-shell-running-container.md#running-individual-commands-in-a-container
word_count: 114
---

Look again at the configuration file for your Pod. The Pod
has an `emptyDir` volume, and the container mounts the volume
at `/usr/share/nginx/html`.

In your shell, create an `index.html` file in the `/usr/share/nginx/html`
directory:

```shell
# Run this inside the container
echo 'Hello shell demo' > /usr/share/nginx/html/index.html
```

In your shell, send a GET request to the nginx server:

```shell
# Run this in the shell inside your container
apt-get update
apt-get install curl
curl http://localhost/
```

The output shows the text that you wrote to the `index.html` file:

```
Hello shell demo
```

When you are finished with your shell, enter `exit`.

```shell
exit # To quit the shell in the container
```
