---
id: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#create-an-index-html-file-on-your-node
kind: section
title: Create an index.html file on your Node
source: tutorials/configuration/configure-persistent-volume-storage.md
url: https://kubernetes.io/docs/tutorials/configuration/configure-persistent-volume-storage/
heading: Create an index.html file on your Node
parent: okf-structure/tutorials/configuration/configure-persistent-volume-storage
children: []
prev_sibling: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#prerequisites
next_sibling: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#create-a-persistentvolume
word_count: 166
---

Open a shell to the single Node in your cluster. How you open a shell depends
on how you set up your cluster. For example, if you are using Minikube, you
can open a shell to your Node by entering `minikube ssh`.

In your shell on that Node, create a `/mnt/data` directory:

```shell
# This assumes that your Node uses "sudo" to run commands
# as the superuser
sudo mkdir /mnt/data
```

In the `/mnt/data` directory, create an `index.html` file:

```shell
# This again assumes that your Node uses "sudo" to run commands
# as the superuser
sudo sh -c "echo 'Hello from Kubernetes storage' > /mnt/data/index.html"
```

If your Node uses a tool for superuser access other than `sudo`, you can
usually make this work if you replace `sudo` with the name of the other tool.

Test that the `index.html` file exists:

```shell
cat /mnt/data/index.html
```

The output should be:

```
Hello from Kubernetes storage
```

You can now close the shell to your Node.
