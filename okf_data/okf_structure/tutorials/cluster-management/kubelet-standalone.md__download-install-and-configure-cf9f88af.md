---
id: okf-structure/tutorials/cluster-management/kubelet-standalone.md#download-install-and-configure-the-components
kind: section
title: Download, install, and configure the components
source: tutorials/cluster-management/kubelet-standalone.md
url: https://kubernetes.io/docs/tutorials/cluster-management/kubelet-standalone/
heading: Download, install, and configure the components
parent: okf-structure/tutorials/cluster-management/kubelet-standalone
children: []
prev_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#prepare-the-system
next_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#run-a-pod-in-the-kubelet
word_count: 666
---

### Install a container runtime {#container-runtime}

Download the latest available versions of the required packages (recommended).

This tutorial suggests installing the CRI-O container runtime
(external link).

There are several ways to install
the CRI-O container runtime, depending on your particular Linux distribution. Although
CRI-O recommends using either `deb` or `rpm` packages, this tutorial uses the
_static binary bundle_ script of the
CRI-O Packaging project,
both to streamline the overall process, and to remain distribution agnostic.

The script installs and configures additional required software, such as
`cni-plugins`, for container
networking, and `crun` and
`runc`, for running containers.

The script will automatically detect your system's processor architecture
(`amd64` or `arm64`) and select and install the latest versions of the software packages.

### Set up CRI-O {#cri-o-setup}

Visit the releases page (external link).

Download the static binary bundle script:

```shell
curl https://raw.githubusercontent.com/cri-o/packaging/main/get > crio-install
```

Run the installer script:

```shell
sudo bash crio-install
```

Enable and start the `crio` service:

```shell
sudo systemctl daemon-reload
sudo systemctl enable --now crio.service
```

Quick test:

```shell
sudo systemctl is-active crio.service
```

The output is similar to:

```
active
```

Detailed service check:

```shell
sudo journalctl -f -u crio.service
```

### Install network plugins

The `cri-o` installer installs and configures the `cni-plugins` package. You can
verify the installation running the following command:

```shell
/opt/cni/bin/bridge --version
```

The output is similar to:

```
CNI bridge plugin v1.5.1
CNI protocol versions supported: 0.1.0, 0.2.0, 0.3.0, 0.3.1, 0.4.0, 1.0.0
```

To check the default configuration:

```shell
cat /etc/cni/net.d/11-crio-ipv4-bridge.conflist
```

The output is similar to:

```json
{
  "cniVersion": "1.0.0",
  "name": "crio",
  "plugins": [
    {
      "type": "bridge",
      "bridge": "cni0",
      "isGateway": true,
      "ipMasq": true,
      "hairpinMode": true,
      "ipam": {
        "type": "host-local",
        "routes": [
            { "dst": "0.0.0.0/0" }
        ],
        "ranges": [
            [{ "subnet": "10.85.0.0/16" }]
        ]
      }
    }
  ]
}
```

Make sure that the default `subnet` range (`10.85.0.0/16`) does not overlap with
any of your active networks. If there is an overlap, you can edit the file and change it
accordingly. Restart the service after the change.

### Download and set up the kubelet

Download the latest stable release of the kubelet.

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubelet"

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubelet"

Configure:

```shell
sudo mkdir -p /etc/kubernetes/manifests
```

```shell
sudo tee /etc/kubernetes/kubelet.yaml <<EOF
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
authentication:
  webhook:
    enabled: false # Do NOT use in production clusters!
authorization:
  mode: AlwaysAllow # Do NOT use in production clusters!
enableServer: false
logging:
  format: text
address: 127.0.0.1 # Restrict access to localhost
readOnlyPort: 10255 # Do NOT use in production clusters!
staticPodPath: /etc/kubernetes/manifests
containerRuntimeEndpoint: unix:///var/run/crio/crio.sock
EOF
```

Because you are not setting up a production cluster, you are using plain HTTP
(`readOnlyPort: 10255`) for unauthenticated queries to the kubelet's API.

The _authentication webhook_ is disabled and _authorization mode_ is set to `AlwaysAllow`
for the purpose of this tutorial. You can learn more about
authorization modes
and webhook authentication to properly
configure kubelet in standalone mode in your environment.

See Ports and Protocols to
understand which ports Kubernetes components use.

Install:

```shell
chmod +x kubelet
sudo cp kubelet /usr/bin/
```

Create a `systemd` service unit file:

```shell
sudo tee /etc/systemd/system/kubelet.service <<EOF
[Unit]
Description=Kubelet

[Service]
ExecStart=/usr/bin/kubelet \
 --config=/etc/kubernetes/kubelet.yaml
Restart=always

[Install]
WantedBy=multi-user.target
EOF
```

The command line argument `--kubeconfig` has been intentionally omitted in the
service configuration file. This argument sets the path to a
kubeconfig
file that specifies how to connect to the API server, enabling API server mode.
Omitting it, enables standalone mode.

Enable and start the `kubelet` service:

```shell
sudo systemctl daemon-reload
sudo systemctl enable --now kubelet.service
```

Quick test:

```shell
sudo systemctl is-active kubelet.service
```

The output is similar to:

```
active
```

Detailed service check:

```shell
sudo journalctl -u kubelet.service
```

Check the kubelet's API `/healthz` endpoint:

```shell
curl http://localhost:10255/healthz?verbose
```

The output is similar to:

```
[+]ping ok
[+]log ok
[+]syncloop ok
healthz check passed
```

Query the kubelet's API `/pods` endpoint:

```shell
curl http://localhost:10255/pods | jq '.'
```

The output is similar to:

```json
{
  "kind": "PodList",
  "apiVersion": "v1",
  "metadata": {},
  "items": null
}
```
