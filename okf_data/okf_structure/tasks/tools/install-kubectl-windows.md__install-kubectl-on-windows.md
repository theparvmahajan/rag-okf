---
id: okf-structure/tasks/tools/install-kubectl-windows.md#install-kubectl-on-windows
kind: section
title: Install kubectl on Windows
source: tasks/tools/install-kubectl-windows.md
url: https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/
heading: Install kubectl on Windows
parent: okf-structure/tasks/tools/install-kubectl-windows
children: []
prev_sibling: okf-structure/tasks/tools/install-kubectl-windows.md#prerequisites
next_sibling: okf-structure/tasks/tools/install-kubectl-windows.md#verify-kubectl-configuration
word_count: 408
---

The following methods exist for installing kubectl on Windows:

- Install kubectl binary on Windows (via direct download or curl)
- Install on Windows using Chocolatey, Scoop, or winget

### Install kubectl binary on Windows (via direct download or curl)

1. You have two options for installing kubectl on your Windows device

   - Direct download:
     
     Download the latest  patch release binary directly for your specific architecture by visiting the Kubernetes release page. Be sure to select the correct binary for your architecture (e.g., amd64, arm64, etc.).
   
   - Using curl:

     If you have `curl` installed, use this command:

     ```powershell
     curl.exe -LO "https://dl.k8s.io/release/v/bin/windows/amd64/kubectl.exe"
     ```

   
   To find out the latest stable version (for example, for scripting), take a look at
   https://dl.k8s.io/release/stable.txt.
   

1. Validate the binary (optional)

   Download the `kubectl` checksum file:

   ```powershell
   curl.exe -LO "https://dl.k8s.io/v/bin/windows/amd64/kubectl.exe.sha256"
   ```

   Validate the `kubectl` binary against the checksum file:

   - Using Command Prompt to manually compare `CertUtil`'s output to the checksum file downloaded:

     ```cmd
     CertUtil -hashfile kubectl.exe SHA256
     type kubectl.exe.sha256
     ```

   - Using PowerShell to automate the verification using the `-eq` operator to
     get a `True` or `False` result:

     ```powershell
      $(Get-FileHash -Algorithm SHA256 .\kubectl.exe).Hash -eq $(Get-Content .\kubectl.exe.sha256)
     ```

1. Append or prepend the `kubectl` binary folder to your `PATH` environment variable.

1. Test to ensure the version of `kubectl` is the same as downloaded:

   ```cmd
   kubectl version --client
   ```
   
   Or use this for detailed view of version:

   ```cmd
   kubectl version --client --output=yaml
   ```

Docker Desktop for Windows
adds its own version of `kubectl` to `PATH`. If you have installed Docker Desktop before,
you may need to place your `PATH` entry before the one added by the Docker Desktop
installer or remove the Docker Desktop's `kubectl`.

### Install on Windows using Chocolatey, Scoop, or winget {#install-nonstandard-package-tools}

1. To install kubectl on Windows you can use either Chocolatey
   package manager, Scoop command-line installer, or
   winget package manager.

   
   
   ```powershell
   choco install kubernetes-cli
   ```
   
   
   ```powershell
   scoop install kubectl
   ```
   
   
   ```powershell
   winget install -e --id Kubernetes.kubectl
   ```
   
   

1. Test to ensure the version you installed is up-to-date:

   ```powershell
   kubectl version --client
   ```

1. Navigate to your home directory:

   ```powershell
   # If you're using cmd.exe, run: cd %USERPROFILE%
   cd ~
   ```

1. Create the `.kube` directory:

   ```powershell
   mkdir .kube
   ```

1. Change to the `.kube` directory you just created:

   ```powershell
   cd .kube
   ```

1. Configure kubectl to use a remote Kubernetes cluster:

   ```powershell
   New-Item config -type file
   ```

Edit the config file with a text editor of your choice, such as Notepad.
