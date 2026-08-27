---
id: okf-structure/tasks/run-application/configure-pdb.md#protecting-an-application-with-a-poddisruptionbudget
kind: section
title: Protecting an Application with a PodDisruptionBudget
source: tasks/run-application/configure-pdb.md
url: https://kubernetes.io/docs/tasks/run-application/configure-pdb/
heading: Protecting an Application with a PodDisruptionBudget
parent: okf-structure/tasks/run-application/configure-pdb
children: []
prev_sibling: okf-structure/tasks/run-application/configure-pdb.md#prerequisites
next_sibling: okf-structure/tasks/run-application/configure-pdb.md#identify-an-application-to-protect
word_count: 39
---

1. Identify what application you want to protect with a PodDisruptionBudget (PDB).
1. Think about how your application reacts to disruptions.
1. Create a PDB definition as a YAML file.
1. Create the PDB object from the YAML file.
