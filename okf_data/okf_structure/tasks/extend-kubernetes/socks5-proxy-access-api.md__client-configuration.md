---
id: okf-structure/tasks/extend-kubernetes/socks5-proxy-access-api.md#client-configuration
kind: section
title: Client configuration
source: tasks/extend-kubernetes/socks5-proxy-access-api.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/socks5-proxy-access-api/
heading: Client configuration
parent: okf-structure/tasks/extend-kubernetes/socks5-proxy-access-api
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/socks5-proxy-access-api.md#using-ssh-to-create-a-socks5-proxy
next_sibling: okf-structure/tasks/extend-kubernetes/socks5-proxy-access-api.md#clean-up
word_count: 376
---

To access the Kubernetes API server through the proxy you must instruct `kubectl` to send queries through
the `SOCKS` proxy we created earlier. Do this by either setting the appropriate environment variable, 
or via the `proxy-url` attribute in the kubeconfig file. Using an environment variable: 

```shell
export HTTPS_PROXY=socks5://localhost:1080
```

To always use this setting on a specific `kubectl` context, specify the `proxy-url` attribute in the relevant 
`cluster` entry within the `~/.kube/config` file. For example:

```yaml
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LRMEMMW2 # shortened for readability 
    server: https://<API_SERVER_IP_ADDRESS>:6443  # the "Kubernetes API" server, in other words the IP address of kubernetes-remote-server.example
    proxy-url: socks5://localhost:1080   # the "SSH SOCKS5 proxy" in the diagram above
  name: default
contexts:
- context:
    cluster: default
    user: default
  name: default
current-context: default
kind: Config
preferences: {}
users:
- name: default
  user:
    client-certificate-data: LS0tLS1CR== # shortened for readability
    client-key-data: LS0tLS1CRUdJT=      # shortened for readability
```

Once you have created the tunnel via the ssh command mentioned earlier, and defined either the environment variable or 
the `proxy-url` attribute, you can interact with your cluster through that proxy. For example:

```shell
kubectl get pods
```

```console
NAMESPACE     NAME                                     READY   STATUS      RESTARTS   AGE
kube-system   coredns-85cb69466-klwq8                  1/1     Running     0          5m46s
```

- Before `kubectl` 1.24, most `kubectl` commands worked when using a socks proxy, except `kubectl exec`.
- `kubectl` supports both `HTTPS_PROXY` and `https_proxy` environment variables. These are used by other 
  programs that support SOCKS, such as `curl`. Therefore in some cases it 
  will be better to define the environment variable on the command line:
  ```shell
  HTTPS_PROXY=socks5://localhost:1080 kubectl get pods
  ```
- When using `proxy-url`, the proxy is used only for the relevant `kubectl` context, 
  whereas the environment variable will affect all contexts.
- The k8s API server hostname can be further protected from DNS leakage by using the `socks5h` protocol name
  instead of the more commonly known `socks5` protocol shown above. In this case, `kubectl` will ask the proxy server
  (such as an ssh bastion) to resolve the k8s API server domain name, instead of resolving it on the system running
  `kubectl`. Note also that with `socks5h`, a k8s API server URL like `https://localhost:6443/api` does not refer 
  to your local client computer. Instead, it refers to `localhost` as known on the proxy server (eg the ssh bastion).
