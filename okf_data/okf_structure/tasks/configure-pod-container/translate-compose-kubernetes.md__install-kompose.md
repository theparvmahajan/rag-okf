---
id: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes.md#install-kompose
kind: section
title: Install Kompose
source: tasks/configure-pod-container/translate-compose-kubernetes.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/
heading: Install Kompose
parent: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes.md#use-kompose
word_count: 110
---

We have multiple ways to install Kompose. Our preferred method is downloading the binary from the latest GitHub release.

Kompose is released via GitHub on a three-week cycle, you can see all current releases on the GitHub release page.

```sh
# Linux
curl -L https://github.com/kubernetes/kompose/releases/download/v1.34.0/kompose-linux-amd64 -o kompose

# macOS
curl -L https://github.com/kubernetes/kompose/releases/download/v1.34.0/kompose-darwin-amd64 -o kompose

# Windows
curl -L https://github.com/kubernetes/kompose/releases/download/v1.34.0/kompose-windows-amd64.exe -o kompose.exe

chmod +x kompose
sudo mv ./kompose /usr/local/bin/kompose
```

Alternatively, you can download the tarball.

Installing using `go get` pulls from the master branch with the latest development changes.

```sh
go get -u github.com/kubernetes/kompose
```

On macOS you can install the latest release via Homebrew:

```bash
brew install kompose
```
