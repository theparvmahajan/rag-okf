---
id: okf-structure/concepts/security/hardening-guide/scheduler.md#introduction
kind: section
title: Hardening Guide - Scheduler Configuration
source: concepts/security/hardening-guide/scheduler.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/scheduler/
heading: null
parent: okf-structure/concepts/security/hardening-guide/scheduler
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/security/hardening-guide/scheduler.md#kube-scheduler-configuration
word_count: 68
---

The Kubernetes scheduler is
one of the critical components of the
control plane.

This document covers how to improve the security posture of the Scheduler.

A misconfigured scheduler can have security implications. 
Such a scheduler can target specific nodes and evict the workloads or applications that are sharing the node and its resources. 
This can aid an attacker with a Yo-Yo attack: an attack on a vulnerable autoscaler.
