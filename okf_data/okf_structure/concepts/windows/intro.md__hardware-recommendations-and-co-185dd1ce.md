---
id: okf-structure/concepts/windows/intro.md#hardware-recommendations-and-considerations-windows-hardware-recommendations
kind: section
title: Hardware recommendations and considerations {#windows-hardware-recommendations}
source: concepts/windows/intro.md
url: https://kubernetes.io/docs/concepts/windows/intro/
heading: Hardware recommendations and considerations {#windows-hardware-recommendations}
parent: okf-structure/concepts/windows/intro
children: []
prev_sibling: okf-structure/concepts/windows/intro.md#windows-os-version-compatibility-windows-os-version-support
next_sibling: okf-structure/concepts/windows/intro.md#getting-help-and-troubleshooting-troubleshooting
word_count: 235
---

The following hardware specifications outlined here should be regarded as sensible default values. 
They are not intended to represent minimum requirements or specific recommendations for production environments.
Depending on the requirements for your workload these values may need to be adjusted. 

- 64-bit processor 4 CPU cores or more, capable of supporting virtualization
- 8GB or more of RAM
- 50GB or more of free disk space

Refer to
Hardware requirements for Windows Server Microsoft documentation
for the most up-to-date information on minimum hardware requirements. For guidance on deciding on resources for
production worker nodes refer to Production worker nodes Kubernetes documentation.

To optimize system resources, if a graphical user interface is not required,
it may be preferable to use a Windows Server OS installation that excludes
the Windows Desktop Experience
installation option, as this configuration typically frees up more system 
resources. 

In assessing disk space for Windows worker nodes, take note that Windows container images are typically larger than
Linux container images, with container image sizes ranging
from 300MB to over 10GB
for a single image. Additionally, take note that the `C:` drive in Windows containers represents a virtual free size of
20GB by default, which is not the actual consumed space, but rather the disk size for which a single container can grow
to occupy when using local storage on the host.
See Containers on Windows - Container Storage Documentation
for more detail.
