---
id: okf-structure/concepts/windows/user-guide.md#getting-started-deploying-a-windows-workload
kind: section
title: 'Getting Started: Deploying a Windows workload'
source: concepts/windows/user-guide.md
url: https://kubernetes.io/docs/concepts/windows/user-guide/
heading: 'Getting Started: Deploying a Windows workload'
parent: okf-structure/concepts/windows/user-guide
children: []
prev_sibling: okf-structure/concepts/windows/user-guide.md#prerequisites
next_sibling: okf-structure/concepts/windows/user-guide.md#observability
word_count: 445
---

The example YAML file below deploys a simple webserver application running inside a Windows container.

Create a manifest named `win-webserver.yaml` with the contents below:

```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: win-webserver
  labels:
    app: win-webserver
spec:
  ports:
    # the port that this service should serve on
    - port: 80
      targetPort: 80
  selector:
    app: win-webserver
  type: NodePort
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: win-webserver
  name: win-webserver
spec:
  replicas: 2
  selector:
    matchLabels:
      app: win-webserver
  template:
    metadata:
      labels:
        app: win-webserver
      name: win-webserver
    spec:
     containers:
      - name: windowswebserver
        image: mcr.microsoft.com/windows/servercore:ltsc2019
        command:
        - powershell.exe
        - -command
        - "<#code used from https://gist.github.com/19WAS85/5424431#> ; $$listener = New-Object System.Net.HttpListener ; $$listener.Prefixes.Add('http://*:80/') ; $$listener.Start() ; $$callerCounts = @{} ; Write-Host('Listening at http://*:80/') ; while ($$listener.IsListening) { ;$$context = $$listener.GetContext() ;$$requestUrl = $$context.Request.Url ;$$clientIP = $$context.Request.RemoteEndPoint.Address ;$$response = $$context.Response ;Write-Host '' ;Write-Host('> {0}' -f $$requestUrl) ;  ;$$count = 1 ;$$k=$$callerCounts.Get_Item($$clientIP) ;if ($$k -ne $$null) { $$count += $$k } ;$$callerCounts.Set_Item($$clientIP, $$count) ;$$ip=(Get-NetAdapter | Get-NetIpAddress); $$header='<html><body><H1>Windows Container Web Server</H1>' ;$$callerCountsString='' ;$$callerCounts.Keys | % { $$callerCountsString+='IP {0} callerCount {1} ' -f $$ip[1].IPAddress,$$callerCounts.Item($$_) } ;$$footer='</body></html>' ;$$content='{0}{1}{2}' -f $$header,$$callerCountsString,$$footer ;Write-Output $$content ;$$buffer = [System.Text.Encoding]::UTF8.GetBytes($$content) ;$$response.ContentLength64 = $$buffer.Length ;$$response.OutputStream.Write($$buffer, 0, $$buffer.Length) ;$$response.Close() ;$$responseStatus = $$response.StatusCode ;Write-Host('< {0}' -f $$responseStatus)  } ; "
     nodeSelector:
      kubernetes.io/os: windows
```

Port mapping is also supported, but for simplicity this example exposes
port 80 of the container directly to the Service.

1. Check that all nodes are healthy:

    ```bash
    kubectl get nodes
    ```

1. Deploy the service and watch for pod updates:

    ```bash
    kubectl apply -f win-webserver.yaml
    kubectl get pods -o wide -w
    ```

    When the service is deployed correctly both Pods are marked as Ready. To exit the watch command, press Ctrl+C.

1. Check that the deployment succeeded. To verify:

    * Several pods listed from the Linux control plane node, use `kubectl get pods`
    * Node-to-pod communication across the network, `curl` port 80 of your pod IPs from the Linux control plane node
      to check for a web server response
    * Pod-to-pod communication, ping between pods (and across hosts, if you have more than one Windows node)
      using `kubectl exec`
    * Service-to-pod communication, `curl` the virtual service IP (seen under `kubectl get services`)
      from the Linux control plane node and from individual pods
    * Service discovery, `curl` the service name with the Kubernetes default DNS suffix
    * Inbound connectivity, `curl` the NodePort from the Linux control plane node or machines outside of the cluster
    * Outbound connectivity, `curl` external IPs from inside the pod using `kubectl exec`

Windows container hosts are not able to access the IP of services scheduled on them due to current platform limitations of the Windows networking stack.
Only Windows pods are able to access service IPs.
