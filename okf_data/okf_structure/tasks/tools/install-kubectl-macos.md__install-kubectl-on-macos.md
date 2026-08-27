---
id: okf-structure/tasks/tools/install-kubectl-macos.md#install-kubectl-on-macos
kind: section
title: Install kubectl on macOS
source: tasks/tools/install-kubectl-macos.md
url: https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/
heading: Install kubectl on macOS
parent: okf-structure/tasks/tools/install-kubectl-macos
children: []
prev_sibling: okf-structure/tasks/tools/install-kubectl-macos.md#prerequisites
next_sibling: okf-structure/tasks/tools/install-kubectl-macos.md#verify-kubectl-configuration
word_count: 398
---

The following methods exist for installing kubectl on macOS:

- Install kubectl on macOS
  - Install kubectl binary with curl on macOS
  - Install with Homebrew on macOS
  - Install with Macports on macOS
- Verify kubectl configuration
- Optional kubectl configurations and plugins
  - Enable shell autocompletion
  - Install `kubectl convert` plugin

### Install kubectl binary with curl on macOS

1. Download the latest release:

   
   
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl"
   
   
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl"
   
   

   
   To download a specific version, replace the `$(curl -L -s https://dl.k8s.io/release/stable.txt)`
   portion of the command with the specific version.

   For example, to download version  on Intel macOS, type:

   ```bash
   curl -LO "https://dl.k8s.io/release/v/bin/darwin/amd64/kubectl"
   ```

   And for macOS on Apple Silicon, type:

   ```bash
   curl -LO "https://dl.k8s.io/release/v/bin/darwin/arm64/kubectl"
   ```

   

1. Validate the binary (optional)

   Download the kubectl checksum file:

   
   
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl.sha256"
   
   
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl.sha256"
   
   
  
   Validate the kubectl binary against the checksum file:

   ```bash
   echo "$(cat kubectl.sha256)  kubectl" | shasum -a 256 --check
   ```

   If valid, the output is:

   ```console
   kubectl: OK
   ```

   If the check fails, `shasum` exits with nonzero status and prints output similar to:

   ```console
   kubectl: FAILED
   shasum: WARNING: 1 computed checksum did NOT match
   ```

   
   Download the same version of the binary and checksum.
   

1. Make the kubectl binary executable.

   ```bash
   chmod +x ./kubectl
   ```

1. Move the kubectl binary to a file location on your system `PATH`.

   ```bash
   sudo mv ./kubectl /usr/local/bin/kubectl
   sudo chown root: /usr/local/bin/kubectl
   ```

   
   Make sure `/usr/local/bin` is in your PATH environment variable.
   

1. Test to ensure the version you installed is up-to-date:

   ```bash
   kubectl version --client
   ```
   
   Or use this for detailed view of version:

   ```cmd
   kubectl version --client --output=yaml
   ```

1. After installing and validating kubectl, delete the checksum file:

   ```bash
   rm kubectl.sha256
   ```

### Install with Homebrew on macOS

If you are on macOS and using Homebrew package manager,
you can install kubectl with Homebrew.

1. Run the installation command:

   ```bash
   brew install kubectl
   ```

   or

   ```bash
   brew install kubernetes-cli
   ```

1. Test to ensure the version you installed is up-to-date:

   ```bash
   kubectl version --client
   ```

### Install with Macports on macOS

If you are on macOS and using Macports package manager,
you can install kubectl with Macports.

1. Run the installation command:

   ```bash
   sudo port selfupdate
   sudo port install kubectl
   ```

1. Test to ensure the version you installed is up-to-date:

   ```bash
   kubectl version --client
   ```
