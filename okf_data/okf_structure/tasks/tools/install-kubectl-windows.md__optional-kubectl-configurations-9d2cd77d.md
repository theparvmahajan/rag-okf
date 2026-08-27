---
id: okf-structure/tasks/tools/install-kubectl-windows.md#optional-kubectl-configurations-and-plugins
kind: section
title: Optional kubectl configurations and plugins
source: tasks/tools/install-kubectl-windows.md
url: https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/
heading: Optional kubectl configurations and plugins
parent: okf-structure/tasks/tools/install-kubectl-windows
children: []
prev_sibling: okf-structure/tasks/tools/install-kubectl-windows.md#verify-kubectl-configuration
next_sibling: okf-structure/tasks/tools/install-kubectl-windows.md#whatsnext
word_count: 189
---

### Enable shell autocompletion

kubectl provides autocompletion support for Bash, Zsh, Fish, and PowerShell,
which can save you a lot of typing.

Below are the procedures to set up autocompletion for PowerShell.

### Configure kuberc

See kuberc for more information.

### Install `kubectl convert` plugin

1. Download the latest release with the command:

   ```powershell
   curl.exe -LO "https://dl.k8s.io/release/v/bin/windows/amd64/kubectl-convert.exe"
   ```

1. Validate the binary (optional).

   Download the `kubectl-convert` checksum file:

   ```powershell
   curl.exe -LO "https://dl.k8s.io/v/bin/windows/amd64/kubectl-convert.exe.sha256"
   ```

   Validate the `kubectl-convert` binary against the checksum file:

   - Using Command Prompt to manually compare `CertUtil`'s output to the checksum file downloaded:

     ```cmd
     CertUtil -hashfile kubectl-convert.exe SHA256
     type kubectl-convert.exe.sha256
     ```

   - Using PowerShell to automate the verification using the `-eq` operator to get
     a `True` or `False` result:

     ```powershell
     $($(CertUtil -hashfile .\kubectl-convert.exe SHA256)[1] -replace " ", "") -eq $(type .\kubectl-convert.exe.sha256)
     ```

1. Append or prepend the `kubectl-convert` binary folder to your `PATH` environment variable.

1. Verify the plugin is successfully installed.

   ```shell
   kubectl convert --help
   ```

   If you do not see an error, it means the plugin is successfully installed.

1. After installing the plugin, clean up the installation files:

   ```powershell
   del kubectl-convert.exe
   del kubectl-convert.exe.sha256
   ```
