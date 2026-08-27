---
id: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#prerequisites
kind: section
title: Prerequisites
source: tasks/inject-data-application/distribute-credentials-secure.md
url: https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/
heading: Prerequisites
parent: okf-structure/tasks/inject-data-application/distribute-credentials-secure
children: []
prev_sibling: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#introduction
next_sibling: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#create-a-secret
word_count: 100
---

### Convert your secret data to a base-64 representation

Suppose you want to have two pieces of secret data: a username `my-app` and a password
`39528$vdg7Jb`. First, use a base64 encoding tool to convert your username and password to a base64 representation. Here's an example using the commonly available base64 program:

```shell
echo -n 'my-app' | base64
echo -n '39528$vdg7Jb' | base64
```

The output shows that the base-64 representation of your username is `bXktYXBw`,
and the base-64 representation of your password is `Mzk1MjgkdmRnN0pi`.

Use a local tool trusted by your OS to decrease the security risks of external tools.
