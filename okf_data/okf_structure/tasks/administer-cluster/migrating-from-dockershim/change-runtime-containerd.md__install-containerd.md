---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#install-containerd
kind: section
title: Install Containerd
source: tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/
heading: Install Containerd
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#stop-the-docker-daemon
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#configure-the-kubelet-to-use-containerd-as-its-container-runtime
word_count: 175
---

Follow the guide
for detailed steps to install containerd.

1. Install the `containerd.io` package from the official Docker repositories. 
   Instructions for setting up the Docker repository for your respective Linux distribution and
   installing the `containerd.io` package can be found at 
   Getting started with containerd.

1. Configure containerd:

   ```shell
   sudo mkdir -p /etc/containerd
   containerd config default | sudo tee /etc/containerd/config.toml
   ```
1. Restart containerd:

   ```shell
   sudo systemctl restart containerd
   ```

Start a Powershell session, set `$Version` to the desired version (ex: `$Version="1.4.3"`), and
then run the following commands:

1. Download containerd:

   ```powershell
   curl.exe -L https://github.com/containerd/containerd/releases/download/v$Version/containerd-$Version-windows-amd64.tar.gz -o containerd-windows-amd64.tar.gz
   tar.exe xvf .\containerd-windows-amd64.tar.gz
   ```

2. Extract and configure:

   ```powershell
   Copy-Item -Path ".\bin\" -Destination "$Env:ProgramFiles\containerd" -Recurse -Force
   cd $Env:ProgramFiles\containerd\
   .\containerd.exe config default | Out-File config.toml -Encoding ascii

   # Review the configuration. Depending on setup you may want to adjust:
   # - the sandbox_image (Kubernetes pause image)
   # - cni bin_dir and conf_dir locations
   Get-Content config.toml

   # (Optional - but highly recommended) Exclude containerd from Windows Defender Scans
   Add-MpPreference -ExclusionProcess "$Env:ProgramFiles\containerd\containerd.exe"
   ```

3. Start containerd:

   ```powershell
   .\containerd.exe --register-service
   Start-Service containerd
   ```
