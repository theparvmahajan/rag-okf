---
id: okf-structure/concepts/configuration/configmap.md#configmaps-and-pods
kind: section
title: ConfigMaps and Pods
source: concepts/configuration/configmap.md
url: https://kubernetes.io/docs/concepts/configuration/configmap/
heading: ConfigMaps and Pods
parent: okf-structure/concepts/configuration/configmap
children: []
prev_sibling: okf-structure/concepts/configuration/configmap.md#configmap-object
next_sibling: okf-structure/concepts/configuration/configmap.md#using-configmaps
word_count: 373
---

You can write a Pod `spec` that refers to a ConfigMap and configures the container(s)
in that Pod based on the data in the ConfigMap. The Pod and the ConfigMap must be in
the same namespace.

The `spec` of a static Pod cannot refer to a ConfigMap
or any other API objects.

Here's an example ConfigMap that has some keys with single values,
and other keys where the value looks like a fragment of a configuration
format.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: game-demo
data:
  # property-like keys; each key maps to a simple value
  player_initial_lives: "3"
  ui_properties_file_name: "user-interface.properties"

  # file-like keys
  game.properties: |
    enemy.types=aliens,monsters
    player.maximum-lives=5
  user-interface.properties: |
    color.good=purple
    color.bad=yellow
    allow.textmode=true
```

There are four different ways that you can use a ConfigMap to configure
a container inside a Pod:

1. Inside a container command and args
1. Environment variables for a container
1. Add a file in read-only volume, for the application to read
1. Write code to run inside the Pod that uses the Kubernetes API to read a ConfigMap

These different methods lend themselves to different ways of modeling
the data being consumed.
For the first three methods, the
kubelet uses the data from
the ConfigMap when it launches container(s) for a Pod.

The fourth method means you have to write code to read the ConfigMap and its data.
However, because you're using the Kubernetes API directly, your application can
subscribe to get updates whenever the ConfigMap changes, and react
when that happens. By accessing the Kubernetes API directly, this
technique also lets you access a ConfigMap in a different namespace.

Here's an example Pod that uses values from `game-demo` to configure a Pod:

A ConfigMap doesn't differentiate between single line property values and
multi-line file-like values.
What matters is how Pods and other objects consume those values.

For this example, defining a volume and mounting it inside the `demo`
container as `/config` creates two files,
`/config/game.properties` and `/config/user-interface.properties`,
even though there are four keys in the ConfigMap. This is because the Pod
definition specifies an `items` array in the `volumes` section.
If you omit the `items` array entirely, every key  in the ConfigMap becomes
a file with the same name as the key, and you get 4 files.
