---
id: okf-structure/tasks/configure-pod-container/configure-gmsa.md#configure-gmsa-credential-spec-reference-in-pod-spec
kind: section
title: Configure GMSA credential spec reference in Pod spec
source: tasks/configure-pod-container/configure-gmsa.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/
heading: Configure GMSA credential spec reference in Pod spec
parent: okf-structure/tasks/configure-pod-container/configure-gmsa
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#assign-role-to-service-accounts-to-use-specific-gmsa-credspecs
next_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#authenticating-to-network-shares-using-hostname-or-fqdn
word_count: 254
---

The Pod spec field `securityContext.windowsOptions.gmsaCredentialSpecName` is used to
specify references to desired GMSA credential spec custom resources in Pod specs.
This configures all containers in the Pod spec to use the specified GMSA. A sample
Pod spec with the annotation populated to refer to `gmsa-WebApp1`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    run: with-creds
  name: with-creds
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      run: with-creds
  template:
    metadata:
      labels:
        run: with-creds
    spec:
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: gmsa-webapp1
      containers:
      - image: mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019
        imagePullPolicy: Always
        name: iis
      nodeSelector:
        kubernetes.io/os: windows
```

Individual containers in a Pod spec can also specify the desired GMSA credspec
using a per-container `securityContext.windowsOptions.gmsaCredentialSpecName` field. For example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    run: with-creds
  name: with-creds
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      run: with-creds
  template:
    metadata:
      labels:
        run: with-creds
    spec:
      containers:
      - image: mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019
        imagePullPolicy: Always
        name: iis
        securityContext:
          windowsOptions:
            gmsaCredentialSpecName: gmsa-Webapp1
      nodeSelector:
        kubernetes.io/os: windows
```

As Pod specs with GMSA fields populated (as described above) are applied in a cluster,
the following sequence of events take place:

1. The mutating webhook resolves and expands all references to GMSA credential spec
   resources to the contents of the GMSA credential spec.

1. The validating webhook ensures the service account associated with the Pod is
   authorized for the `use` verb on the specified GMSA credential spec.

1. The container runtime configures each Windows container with the specified GMSA
   credential spec so that the container can assume the identity of the GMSA in
   Active Directory and access services in the domain using that identity.
