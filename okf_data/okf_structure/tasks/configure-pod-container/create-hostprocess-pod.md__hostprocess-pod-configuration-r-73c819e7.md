---
id: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#hostprocess-pod-configuration-requirements
kind: section
title: HostProcess Pod configuration requirements
source: tasks/configure-pod-container/create-hostprocess-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/
heading: HostProcess Pod configuration requirements
parent: okf-structure/tasks/configure-pod-container/create-hostprocess-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#limitations
next_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#volume-mounts
word_count: 200
---

Enabling a Windows HostProcess pod requires setting the right configurations in the pod security
configuration. Of the policies defined in the Pod Security Standards
HostProcess pods are disallowed by the baseline and restricted policies. It is therefore recommended
that HostProcess pods run in alignment with the privileged profile.

When running under the privileged policy, here are
the configurations which need to be set to enable the creation of a HostProcess pod:

  <caption style="display: none">Privileged policy specification</caption>
  
    
      Control
      Policy
    
  
  
    
      <tt>securityContext.windowsOptions.hostProcess</tt>
      
        Windows pods offer the ability to run 
        HostProcess containers which enables privileged access to the Windows node. 
        Allowed Values
        
          <code>true</code>
        
      
    
    
      <tt>hostNetwork</tt>
      
        Pods container HostProcess containers must use the host's network namespace.
        Allowed Values
        
          <code>true</code>
        
      
    
    
      <tt>securityContext.windowsOptions.runAsUserName</tt>
      
        Specification of which user the HostProcess container should run as is required for the pod spec.
        Allowed Values
        
          <code>NT AUTHORITY\SYSTEM</code>
          <code>NT AUTHORITY\Local service</code>
          <code>NT AUTHORITY\NetworkService</code>
          Local usergroup names (see below)
        
      
    
    
      <tt>runAsNonRoot</tt>
      
        Because HostProcess containers have privileged access to the host, the <tt>runAsNonRoot</tt> field cannot be set to true.
        Allowed Values
        
          Undefined/Nil
          <code>false</code>
        
      
    
  

### Example manifest (excerpt) {#manifest-example}

```yaml
spec:
  securityContext:
    windowsOptions:
      hostProcess: true
      runAsUserName: "NT AUTHORITY\\Local service"
  hostNetwork: true
  containers:
  - name: test
    image: image1:latest
    command:
      - ping
      - -t
      - 127.0.0.1
  nodeSelector:
    "kubernetes.io/os": windows
```
