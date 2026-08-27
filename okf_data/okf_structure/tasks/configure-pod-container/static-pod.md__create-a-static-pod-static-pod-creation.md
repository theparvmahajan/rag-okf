---
id: okf-structure/tasks/configure-pod-container/static-pod.md#create-a-static-pod-static-pod-creation
kind: section
title: Create a static pod {#static-pod-creation}
source: tasks/configure-pod-container/static-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/
heading: Create a static pod {#static-pod-creation}
parent: okf-structure/tasks/configure-pod-container/static-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/static-pod.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/static-pod.md#observe-static-pod-behavior-behavior-of-static-pods
word_count: 538
---

You can configure a static Pod with either a file system hosted configuration file
or a web hosted configuration file.

### Filesystem-hosted static Pod manifest {#configuration-files}

Manifests are standard Pod definitions in JSON or YAML format in a specific directory.
Use the `staticPodPath: <the directory>` field in the
kubelet configuration file,
which periodically scans the directory and creates/deletes static Pods as YAML/JSON files appear/disappear there.
Note that the kubelet will ignore files starting with dots when scanning the specified directory.

The kubelet processes **all files not starting with a dot** in the static Pod directory
— there is no filtering by file extension. For example, if you create a backup of a
manifest by running `cp kube-apiserver.yaml kube-apiserver.yaml.backup`, the kubelet
will read **both** files and attempt to create a static Pod from each. When two files
define a Pod with the same name, the resulting behavior is undefined and can cause the
backup's outdated spec to silently take effect instead of the current manifest. If you
do create a backup, store it **outside** the static Pod directory (for example, in
`/etc/kubernetes/backup/`).

For example, this is how to start a simple web server as a static Pod:

1. Choose a node where you want to run the static Pod. In this example, it's `my-node1`.

   ```shell
   ssh my-node1
   ```

1. Choose a directory, say `/etc/kubernetes/manifests` and place a web server
   Pod definition there, for example `/etc/kubernetes/manifests/static-web.yaml`:
 
   ```shell
   # Run this command on the node where kubelet is running
   mkdir -p /etc/kubernetes/manifests/
   cat <<EOF >/etc/kubernetes/manifests/static-web.yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: static-web
     labels:
       role: myrole
   spec:
     containers:
       - name: web
         image: nginx
         ports:
           - name: web
             containerPort: 80
             protocol: TCP
   EOF
   ```

1. Configure the kubelet on that node to set a `staticPodPath` value in the
   kubelet configuration file.  
   See Set Kubelet Parameters Via A Configuration File
   for more information.

   An alternative and deprecated method is to configure the kubelet on that node
   to look for static Pod manifests locally, using a command line argument.
   To use the deprecated approach, start the kubelet with the 
   `--pod-manifest-path=/etc/kubernetes/manifests/` argument.
   
1. Restart the kubelet. On Fedora, you would run:

   ```shell
   # Run this command on the node where the kubelet is running
   systemctl restart kubelet
   ```

### Web-hosted static pod manifest {#pods-created-via-http}

Kubelet periodically downloads a file specified by `--manifest-url=<URL>` argument
and interprets it as a JSON/YAML file that contains Pod definitions.
Similar to how filesystem-hosted manifests work, the kubelet
refetches the manifest on a schedule. If there are changes to the list of static
Pods, the kubelet applies them.

To use this approach:

1. Create a YAML file and store it on a web server so that you can pass the URL of that file to the kubelet.

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: static-web
     labels:
       role: myrole
   spec:
     containers:
       - name: web
         image: nginx
         ports:
           - name: web
             containerPort: 80
             protocol: TCP
   ```

1. Configure the kubelet on your selected node to use this web manifest by
   updating your kubelet configuration file to include the `staticPodURL` field:

   ```yaml
   apiVersion: kubelet.config.k8s.io/v1beta1
   kind: KubeletConfiguration
   staticPodURL: "<manifest-url>"
   ```

1. Restart the kubelet. On Fedora, you would run:

   ```shell
   # Run this command on the node where the kubelet is running
   systemctl restart kubelet
   ```
