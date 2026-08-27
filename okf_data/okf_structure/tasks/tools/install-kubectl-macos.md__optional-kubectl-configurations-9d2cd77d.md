---
id: okf-structure/tasks/tools/install-kubectl-macos.md#optional-kubectl-configurations-and-plugins
kind: section
title: Optional kubectl configurations and plugins
source: tasks/tools/install-kubectl-macos.md
url: https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/
heading: Optional kubectl configurations and plugins
parent: okf-structure/tasks/tools/install-kubectl-macos
children: []
prev_sibling: okf-structure/tasks/tools/install-kubectl-macos.md#verify-kubectl-configuration
next_sibling: okf-structure/tasks/tools/install-kubectl-macos.md#whatsnext
word_count: 318
---

### Enable shell autocompletion

kubectl provides autocompletion support for Bash, Zsh, Fish, and PowerShell
which can save you a lot of typing.

Below are the procedures to set up autocompletion for Bash, Fish, and Zsh.

### Configure kuberc

See kuberc for more information.

### Install `kubectl convert` plugin

1. Download the latest release with the command:

   
   
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl-convert"
   
   
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl-convert"
   
   

1. Validate the binary (optional)

   Download the kubectl-convert checksum file:

   
   
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl-convert.sha256"
   
   
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl-convert.sha256"
   
   

   Validate the kubectl-convert binary against the checksum file:

   ```bash
   echo "$(cat kubectl-convert.sha256)  kubectl-convert" | shasum -a 256 --check
   ```

   If valid, the output is:

   ```console
   kubectl-convert: OK
   ```

   If the check fails, `shasum` exits with nonzero status and prints output similar to:

   ```console
   kubectl-convert: FAILED
   shasum: WARNING: 1 computed checksum did NOT match
   ```

   
   Download the same version of the binary and checksum.
   

1. Make kubectl-convert binary executable

   ```bash
   chmod +x ./kubectl-convert
   ```

1. Move the kubectl-convert binary to a file location on your system `PATH`.

   ```bash
   sudo mv ./kubectl-convert /usr/local/bin/kubectl-convert
   sudo chown root: /usr/local/bin/kubectl-convert
   ```

   
   Make sure `/usr/local/bin` is in your PATH environment variable.
   

1. Verify plugin is successfully installed

   ```shell
   kubectl convert --help
   ```

   If you do not see an error, it means the plugin is successfully installed.

1. After installing the plugin, clean up the installation files:

   ```bash
   rm kubectl-convert kubectl-convert.sha256
   ```

### Uninstall kubectl on macOS

Depending on how you installed `kubectl`, use one of the following methods.

### Uninstall kubectl using the command-line

1.  Locate the `kubectl` binary on your system:

    ```bash
    which kubectl
    ```

1.  Remove the `kubectl` binary:

    ```bash
    sudo rm <path>
    ```
    Replace `<path>` with the path to the `kubectl` binary from the previous step. For example, `sudo rm /usr/local/bin/kubectl`.

### Uninstall kubectl using homebrew

If you installed `kubectl` using Homebrew, run the following command:

```bash
brew remove kubectl
```
