---
id: okf-structure/tutorials/security/apparmor.md#administration
kind: section
title: Administration
source: tutorials/security/apparmor.md
url: https://kubernetes.io/docs/tutorials/security/apparmor/
heading: Administration
parent: okf-structure/tutorials/security/apparmor
children: []
prev_sibling: okf-structure/tutorials/security/apparmor.md#example
next_sibling: okf-structure/tutorials/security/apparmor.md#authoring-profiles
word_count: 96
---

### Setting up Nodes with profiles

Kubernetes  does not provide any built-in mechanisms for loading AppArmor profiles onto
Nodes. Profiles can be loaded through custom infrastructure or tools like the
Kubernetes Security Profiles Operator.

The scheduler is not aware of which profiles are loaded onto which Node, so the full set of profiles
must be loaded onto every Node.  An alternative approach is to add a Node label for each profile (or
class of profiles) on the Node, and use a
node selector to ensure the Pod is run on a
Node with the required profile.
