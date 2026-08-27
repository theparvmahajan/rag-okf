---
id: okf-structure/tasks/configure-pod-container/configure-gmsa.md#create-gmsa-credential-spec-resources
kind: section
title: Create GMSA credential spec resources
source: tasks/configure-pod-container/configure-gmsa.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/
heading: Create GMSA credential spec resources
parent: okf-structure/tasks/configure-pod-container/configure-gmsa
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#configure-gmsas-and-windows-nodes-in-active-directory
next_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#configure-cluster-role-to-enable-rbac-on-specific-gmsa-credential-specs
word_count: 292
---

With the GMSACredentialSpec CRD installed (as described earlier), custom resources
containing GMSA credential specs can be configured. The GMSA credential spec does
not contain secret or sensitive data. It is information that a container runtime
can use to describe the desired GMSA of a container to Windows. GMSA credential
specs can be generated in YAML format with a utility
PowerShell script.

Following are the steps for generating a GMSA credential spec YAML manually in JSON format and then converting it:

1. Import the CredentialSpec
   module: `ipmo CredentialSpec.psm1`

1. Create a credential spec in JSON format using `New-CredentialSpec`.
   To create a GMSA credential spec named WebApp1, invoke
   `New-CredentialSpec -Name WebApp1 -AccountName WebApp1 -Domain $(Get-ADDomain -Current LocalComputer)`

1. Use `Get-CredentialSpec` to show the path of the JSON file.

1. Convert the credspec file from JSON to YAML format and apply the necessary
   header fields `apiVersion`, `kind`, `metadata` and `credspec` to make it a
   GMSACredentialSpec custom resource that can be configured in Kubernetes.

The following YAML configuration describes a GMSA credential spec named `gmsa-WebApp1`:

```yaml
apiVersion: windows.k8s.io/v1
kind: GMSACredentialSpec
metadata:
  name: gmsa-WebApp1  # This is an arbitrary name but it will be used as a reference
credspec:
  ActiveDirectoryConfig:
    GroupManagedServiceAccounts:
    - Name: WebApp1   # Username of the GMSA account
      Scope: CONTOSO  # NETBIOS Domain Name
    - Name: WebApp1   # Username of the GMSA account
      Scope: contoso.com # DNS Domain Name
  CmsPlugins:
  - ActiveDirectory
  DomainJoinConfig:
    DnsName: contoso.com  # DNS Domain Name
    DnsTreeName: contoso.com # DNS Domain Name Root
    Guid: 244818ae-87ac-4fcd-92ec-e79e5252348a  # GUID of the Domain
    MachineAccountName: WebApp1 # Username of the GMSA account
    NetBiosName: CONTOSO  # NETBIOS Domain Name
    Sid: S-1-5-21-2126449477-2524075714-3094792973 # SID of the Domain
```

The above credential spec resource may be saved as `gmsa-Webapp1-credspec.yaml`
and applied to the cluster using: `kubectl apply -f gmsa-Webapp1-credspec.yml`
