---
id: okf-structure/tasks/configure-pod-container/configure-runasusername.md#windows-username-limitations
kind: section
title: Windows Username limitations
source: tasks/configure-pod-container/configure-runasusername.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-runasusername/
heading: Windows Username limitations
parent: okf-structure/tasks/configure-pod-container/configure-runasusername
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-runasusername.md#set-the-username-for-a-container
next_sibling: okf-structure/tasks/configure-pod-container/configure-runasusername.md#whatsnext
word_count: 197
---

In order to use this feature, the value set in the `runAsUserName` field must be a valid username. It must have the following format: `DOMAIN\USER`, where `DOMAIN\` is optional. Windows user names are case insensitive. Additionally, there are some restrictions regarding the `DOMAIN` and `USER`:

- The `runAsUserName` field cannot be empty, and it cannot contain control characters (ASCII values: `0x00-0x1F`, `0x7F`)
- The `DOMAIN` must be either a NetBios name, or a DNS name, each with their own restrictions:
  - NetBios names: maximum 15 characters, cannot start with `.` (dot), and cannot contain the following characters: `\ / : * ? " < > |`
  - DNS names: maximum 255 characters, contains only alphanumeric characters, dots, and dashes, and it cannot start or end with a `.` (dot) or `-` (dash).
- The `USER` must have at most 20 characters, it cannot contain *only* dots or spaces, and it cannot contain the following characters: `" / \ [ ] : ; | = , + * ? < > @`.

Examples of acceptable values for the `runAsUserName` field: `ContainerAdministrator`, `ContainerUser`, `NT AUTHORITY\NETWORK SERVICE`, `NT AUTHORITY\LOCAL SERVICE`.

For more information about these limitations, check here and here.
