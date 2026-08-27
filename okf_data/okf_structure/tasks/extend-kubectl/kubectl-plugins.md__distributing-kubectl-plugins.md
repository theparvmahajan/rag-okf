---
id: okf-structure/tasks/extend-kubectl/kubectl-plugins.md#distributing-kubectl-plugins
kind: section
title: Distributing kubectl plugins
source: tasks/extend-kubectl/kubectl-plugins.md
url: https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/
heading: Distributing kubectl plugins
parent: okf-structure/tasks/extend-kubectl/kubectl-plugins
children: []
prev_sibling: okf-structure/tasks/extend-kubectl/kubectl-plugins.md#writing-kubectl-plugins
next_sibling: okf-structure/tasks/extend-kubectl/kubectl-plugins.md#whatsnext
word_count: 213
---

If you have developed a plugin for others to use, you should consider how you
package it, distribute it and deliver updates to your users.

### Krew {#distributing-krew}

Krew offers a cross-platform way to package and
distribute your plugins. This way, you use a single packaging format for all
target platforms (Linux, Windows, macOS etc) and deliver updates to your users.
Krew also maintains a plugin
index so that other people can
discover your plugin and install it.

### Native / platform specific package management {#distributing-native}

Alternatively, you can use traditional package managers such as, `apt` or `yum`
on Linux, Chocolatey on Windows, and Homebrew on macOS. Any package
manager will be suitable if it can place new executables placed somewhere
in the user's `PATH`.
As a plugin author, if you pick this option then you also have the burden
of updating your kubectl plugin's distribution package across multiple
platforms for each release.

### Source code {#distributing-source-code}

You can publish the source code; for example, as a Git repository. If you
choose this option, someone who wants to use that plugin must fetch the code,
set up a build environment (if it needs compiling), and deploy the plugin.
If you also make compiled packages available, or use Krew, that will make
installs easier.
