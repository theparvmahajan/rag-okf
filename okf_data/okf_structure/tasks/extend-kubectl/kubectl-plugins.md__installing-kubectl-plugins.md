---
id: okf-structure/tasks/extend-kubectl/kubectl-plugins.md#installing-kubectl-plugins
kind: section
title: Installing kubectl plugins
source: tasks/extend-kubectl/kubectl-plugins.md
url: https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/
heading: Installing kubectl plugins
parent: okf-structure/tasks/extend-kubectl/kubectl-plugins
children: []
prev_sibling: okf-structure/tasks/extend-kubectl/kubectl-plugins.md#prerequisites
next_sibling: okf-structure/tasks/extend-kubectl/kubectl-plugins.md#writing-kubectl-plugins
word_count: 314
---

A plugin is a standalone executable file, whose name begins with `kubectl-`. To install a plugin, move its executable file to anywhere on your `PATH`.

You can also discover and install kubectl plugins available in the open source
using Krew. Krew is a plugin manager maintained by
the Kubernetes SIG CLI community.

Kubectl plugins available via the Krew plugin index
are not audited for security. You should install and run third-party plugins at your
own risk, since they are arbitrary programs running on your machine.

### Discovering plugins

`kubectl` provides a command `kubectl plugin list` that searches your `PATH` for valid plugin executables.
Executing this command causes a traversal of all files in your `PATH`. Any files that are executable, and
begin with `kubectl-` will show up *in the order in which they are present in your `PATH`* in this command's output.
A warning will be included for any files beginning with `kubectl-` that are *not* executable.
A warning will also be included for any valid plugin files that overlap each other's name.

You can use Krew to discover and install `kubectl`
plugins from a community-curated
plugin index.

#### Create plugins

`kubectl` allows plugins to add custom create commands of the shape `kubectl create something` by providing a `kubectl-create-something` binary in the `PATH`.

#### Limitations

It is currently not possible to create plugins that overwrite existing `kubectl` commands or extend commands other than `create`.
For example, creating a plugin `kubectl-version` will cause that plugin to never be executed, as the existing `kubectl version`
command will always take precedence over it.
Due to this limitation, it is also *not* possible to use plugins to add new subcommands to existing `kubectl` commands.
For example, adding a subcommand `kubectl attach vm` by naming your plugin `kubectl-attach-vm` will cause that plugin to be ignored.

`kubectl plugin list` shows warnings for any valid plugins that attempt to do this.
