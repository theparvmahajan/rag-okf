---
id: okf-structure/tasks/tools/install-kubectl-linux.md#optional-kubectl-configurations-and-plugins
kind: section
title: Optional kubectl configurations and plugins
source: tasks/tools/install-kubectl-linux.md
url: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
heading: Optional kubectl configurations and plugins
parent: okf-structure/tasks/tools/install-kubectl-linux
children: []
prev_sibling: okf-structure/tasks/tools/install-kubectl-linux.md#verify-kubectl-configuration
next_sibling: okf-structure/tasks/tools/install-kubectl-linux.md#whatsnext
word_count: 206
---

### Enable shell autocompletion

kubectl provides autocompletion support for Bash, Zsh, Fish, and PowerShell,
which can save you a lot of typing.

Below are the procedures to set up autocompletion for Bash, Fish, and Zsh.

### Configure kuberc

See kuberc for more information.

### Install `kubectl convert` plugin

1. Download the latest release with the command:

   
   
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl-convert"
   
   
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl-convert"
   
   

1. Validate the binary (optional)

   Download the kubectl-convert checksum file:

   
   
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl-convert.sha256"
   
   
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl-convert.sha256"
   
   

   Validate the kubectl-convert binary against the checksum file:

   ```bash
   echo "$(cat kubectl-convert.sha256) kubectl-convert" | sha256sum --check
   ```

   If valid, the output is:

   ```console
   kubectl-convert: OK
   ```

   If the check fails, `sha256` exits with nonzero status and prints output similar to:

   ```console
   kubectl-convert: FAILED
   sha256sum: WARNING: 1 computed checksum did NOT match
   ```

   
   Download the same version of the binary and checksum.
   

1. Install kubectl-convert

   ```bash
   sudo install -o root -g root -m 0755 kubectl-convert /usr/local/bin/kubectl-convert
   ```

1. Verify plugin is successfully installed

   ```shell
   kubectl convert --help
   ```

   If you do not see an error, it means the plugin is successfully installed.

1. After installing the plugin, clean up the installation files:

   ```bash
   rm kubectl-convert kubectl-convert.sha256
   ```
