---
id: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#mounting-the-same-persistentvolume-in-two-places
kind: section
title: Mounting the same PersistentVolume in two places
source: tutorials/configuration/configure-persistent-volume-storage.md
url: https://kubernetes.io/docs/tutorials/configuration/configure-persistent-volume-storage/
heading: Mounting the same PersistentVolume in two places
parent: okf-structure/tutorials/configuration/configure-persistent-volume-storage
children: []
prev_sibling: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#clean-up
next_sibling: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#clean-up-2
word_count: 583
---

You have understood how to create a PersistentVolume & PersistentVolumeClaim, and how to mount
the volume to a single location in a container. Let's explore how you can mount the same PersistentVolume
at two different locations in a container. Below is an example:

Here:

- `subPath`: This field allows specific files or directories from the mounted PersistentVolume to be exposed at
  different locations within the container.  In this example:
  - `subPath: html` mounts the html directory.
  - `subPath: nginx.conf` mounts a specific file, nginx.conf.

Since the first subPath is `html`, an `html` directory has to be created within `/mnt/data/`
on the node.

The second subPath `nginx.conf` means that a file within the `/mnt/data/` directory will be used. No other directory
needs to be created.

Two volume mounts will be made on your nginx container:

- `/usr/share/nginx/html` for the static website
- `/etc/nginx/nginx.conf` for the default config

### Move the index.html file on your Node to a new folder

The `index.html` file mentioned here refers to the one created in the "Create an index.html file on your Node" section.

Open a shell to the single Node in your cluster. How you open a shell depends on how you set up your cluster.
For example, if you are using Minikube, you can open a shell to your Node by entering `minikube ssh`.

Create a `/mnt/data/html` directory:

```shell
# This assumes that your Node uses "sudo" to run commands
# as the superuser
sudo mkdir /mnt/data/html
```

Move index.html into the directory:

```shell
# Move index.html from its current location to the html sub-directory
sudo mv /mnt/data/index.html html
```

### Create a new nginx.conf file

This is a modified version of the default `nginx.conf` file. Here, the default `keepalive_timeout` has been
modified to `60`

Create the nginx.conf file:

```shell
cat <<EOF > /mnt/data/nginx.conf
user  nginx;
worker_processes  auto;
error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '\$remote_addr - \$remote_user [\$time_local] "\$request" '
                      '\$status \$body_bytes_sent "\$http_referer" '
                      '"\$http_user_agent" "\$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  60;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
EOF
```

### Create a Pod

Here we will create a pod that uses the existing persistentVolume and persistentVolumeClaim.
However, the pod mounts only a specific file, `nginx.conf`, and directory, `html`, to the container.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/storage/pv-duplicate.yaml
```

Verify that the container in the Pod is running:

```shell
kubectl get pod test
```

Get a shell to the container running in your Pod:

```shell
kubectl exec -it test -- /bin/bash
```

In your shell, verify that nginx is serving the `index.html` file from the
hostPath volume:

```shell
# Be sure to run these 3 commands inside the root shell that comes from
# running "kubectl exec" in the previous step
apt update
apt install curl
curl http://localhost/
```

The output shows the text that you wrote to the `index.html` file on the
hostPath volume:

```
Hello from Kubernetes storage
```

In your shell, also verify that nginx is serving the `nginx.conf` file from the
hostPath volume:

```shell
# Be sure to run these commands inside the root shell that comes from
# running "kubectl exec" in the previous step
cat /etc/nginx/nginx.conf | grep keepalive_timeout
```

The output shows the modified text that you wrote to the `nginx.conf` file on the
hostPath volume:

```
keepalive_timeout  60;
```

If you see these messages, you have successfully configured a Pod to
use a specific file and directory in a storage from a PersistentVolumeClaim.
