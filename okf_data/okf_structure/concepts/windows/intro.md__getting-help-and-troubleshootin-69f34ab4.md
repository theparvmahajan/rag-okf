---
id: okf-structure/concepts/windows/intro.md#getting-help-and-troubleshooting-troubleshooting
kind: section
title: Getting help and troubleshooting {#troubleshooting}
source: concepts/windows/intro.md
url: https://kubernetes.io/docs/concepts/windows/intro/
heading: Getting help and troubleshooting {#troubleshooting}
parent: okf-structure/concepts/windows/intro
children: []
prev_sibling: okf-structure/concepts/windows/intro.md#hardware-recommendations-and-considerations-windows-hardware-recommendations
next_sibling: okf-structure/concepts/windows/intro.md#deployment-tools
word_count: 229
---

Your main source of help for troubleshooting your Kubernetes cluster should start
with the Troubleshooting
page.

Some additional, Windows-specific troubleshooting help is included
in this section. Logs are an important element of troubleshooting
issues in Kubernetes. Make sure to include them any time you seek
troubleshooting assistance from other contributors. Follow the
instructions in the
SIG Windows contributing guide on gathering logs.

### Reporting issues and feature requests

If you have what looks like a bug, or you would like to
make a feature request, please follow the SIG Windows contributing guide to create a new issue.
You should first search the list of issues in case it was
reported previously and comment with your experience on the issue and add additional
logs. SIG Windows channel on the Kubernetes Slack is also a great avenue to get some initial support and
troubleshooting ideas prior to creating a ticket.

### Validating the Windows cluster operability

The Kubernetes project provides a _Windows Operational Readiness_ specification,
accompanied by a structured test suite. This suite is split into two sets of tests,
core and extended, each containing categories aimed at testing specific areas.
It can be used to validate all the functionalities of a Windows and hybrid system
(mixed with Linux nodes) with full coverage.

To set up the project on a newly created cluster, refer to the instructions in the
project guide.
