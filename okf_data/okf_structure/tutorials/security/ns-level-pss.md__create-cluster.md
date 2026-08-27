---
id: okf-structure/tutorials/security/ns-level-pss.md#create-cluster
kind: section
title: Create cluster
source: tutorials/security/ns-level-pss.md
url: https://kubernetes.io/docs/tutorials/security/ns-level-pss/
heading: Create cluster
parent: okf-structure/tutorials/security/ns-level-pss
children: []
prev_sibling: okf-structure/tutorials/security/ns-level-pss.md#prerequisites
next_sibling: okf-structure/tutorials/security/ns-level-pss.md#create-a-namespace
word_count: 124
---

1. Create a `kind` cluster as follows:

   ```shell
   kind create cluster --name psa-ns-level
   ```

   The output is similar to this:

   ```
   Creating cluster "psa-ns-level" ...
    ✓ Ensuring node image (kindest/node:v) 🖼 
    ✓ Preparing nodes 📦  
    ✓ Writing configuration 📜 
    ✓ Starting control-plane 🕹️ 
    ✓ Installing CNI 🔌 
    ✓ Installing StorageClass 💾 
   Set kubectl context to "kind-psa-ns-level"
   You can now use your cluster with:
    
   kubectl cluster-info --context kind-psa-ns-level
    
   Not sure what to do next? 😅  Check out https://kind.sigs.k8s.io/docs/user/quick-start/
   ```

1. Set the kubectl context to the new cluster:

   ```shell
   kubectl cluster-info --context kind-psa-ns-level
   ```
   The output is similar to this:

   ```
   Kubernetes control plane is running at https://127.0.0.1:50996
   CoreDNS is running at https://127.0.0.1:50996/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
    
   To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
   ```
