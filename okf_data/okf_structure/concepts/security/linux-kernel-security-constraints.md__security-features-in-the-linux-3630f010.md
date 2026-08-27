---
id: okf-structure/concepts/security/linux-kernel-security-constraints.md#security-features-in-the-linux-kernel-linux-security-features
kind: section
title: Security features in the Linux kernel {#linux-security-features}
source: concepts/security/linux-kernel-security-constraints.md
url: https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/
heading: Security features in the Linux kernel {#linux-security-features}
parent: okf-structure/concepts/security/linux-kernel-security-constraints
children: []
prev_sibling: okf-structure/concepts/security/linux-kernel-security-constraints.md#run-workloads-without-root-privileges-run-without-root
next_sibling: okf-structure/concepts/security/linux-kernel-security-constraints.md#kernel-level-security-features-and-privileged-containers-kernel-security-features-privileged-containers
word_count: 1179
---

Kubernetes lets you configure and use Linux kernel features to improve isolation
and harden your containerized workloads. Common features include the following:

* **Secure computing mode (seccomp)**: Filter which system calls a process can
  make
* **AppArmor**: Restrict the access privileges of individual programs
* **Security Enhanced Linux (SELinux)**: Assign security labels to objects for
  more manageable security policy enforcement

To configure settings for one of these features, the operating system that you
choose for your nodes must enable the feature in the kernel. For example,
Ubuntu 7.10 and later enable AppArmor by default. To learn whether your OS
enables a specific feature, consult the OS documentation.

You use the `securityContext` field in your Pod specification to define the
constraints that apply to those processes. The `securityContext` field also
supports other security settings, such as specific Linux capabilities or file
access permissions using UIDs and GIDs. To learn more, refer to
Configure a SecurityContext for a Pod or Container.

### seccomp

Some of your workloads might need privileges to perform specific actions as the
root user on your node's host machine. Linux uses *capabilities* to divide the
available privileges into categories, so that processes can get the privileges
required to perform specific actions without being granted all privileges. Each
capability has a set of system calls (syscalls) that a process can make. seccomp
lets you restrict these individual syscalls. 
It can be used to sandbox the privileges of a process, restricting the calls it
is able to make from userspace into the kernel.

In Kubernetes, you use a *container runtime* on each node to run your
containers. Example runtimes include CRI-O, Docker, or containerd. Each runtime
allows only a subset of Linux capabilities by default. You can further limit the
allowed syscalls individually by using a seccomp profile. Container runtimes
usually include a default seccomp profile. 
Kubernetes lets you automatically
apply seccomp profiles loaded onto a node to your Pods and containers.

Kubernetes also has the `allowPrivilegeEscalation` setting for Pods and
containers. When set to `false`, this prevents processes from gaining new
capabilities and restricts unprivileged users from changing the applied seccomp
profile to a more permissive profile.

To learn how to implement seccomp in Kubernetes, refer to
Restrict a Container's Syscalls with seccomp
or the Seccomp node reference

To learn more about seccomp, see
Seccomp BPF
in the Linux kernel documentation.

#### Considerations for seccomp {#seccomp-considerations}

seccomp is a low-level security configuration that you should only configure
yourself if you require fine-grained control over Linux syscalls. Using
seccomp, especially at scale, has the following risks:

* Configurations might break during application updates
* Attackers can still use allowed syscalls to exploit vulnerabilities
* Profile management for individual applications becomes challenging at scale

**Recommendation**: Use the default seccomp profile that's bundled with your
container runtime. If you need a more isolated environment, consider using a
sandbox, such as gVisor. Sandboxes solve the preceding risks with custom
seccomp profiles, but require more compute resources on your nodes and might
have compatibility issues with GPUs and other specialized hardware.

### AppArmor and SELinux: policy-based mandatory access control {#policy-based-mac}

You can use Linux policy-based mandatory access control (MAC) mechanisms, such
as AppArmor and SELinux, to harden your Kubernetes workloads.

#### AppArmor

AppArmor is a Linux kernel security module that
supplements the standard Linux user and group based permissions to confine
programs to a limited set of resources. AppArmor can be configured for any
application to reduce its potential attack surface and provide greater in-depth
defense. It is configured through profiles tuned to allow the access needed by a
specific program or container, such as Linux capabilities, network access, and
file permissions. Each profile can be run in either enforcing mode, which blocks
access to disallowed resources, or complain mode, which only reports violations.

AppArmor can help you to run a more secure deployment by restricting what
containers are allowed to do, and/or provide better auditing through system
logs. The container runtime that you use might ship with a default AppArmor
profile, or you can use a custom profile.

To learn how to use AppArmor in Kubernetes, refer to
Restrict a Container's Access to Resources with AppArmor.

#### SELinux

SELinux is a Linux kernel security module that lets you restrict the access
that a specific *subject*, such as a process, has to the files on your system.
You define security policies that apply to subjects that have specific SELinux
labels. When a process that has an SELinux label attempts to access a file, the
SELinux server checks whether that process' security policy allows the access
and makes an authorization decision.

In Kubernetes, you can set an SELinux label in the `securityContext` field of
your manifest. The specified labels are assigned to those processes. If you
have configured security policies that affect those labels, the host OS kernel
enforces these policies.

To learn how to use SELinux in Kubernetes, refer to
Assign SELinux labels to a container.

#### Differences between AppArmor and SELinux {#apparmor-selinux-diff}

The operating system on your Linux nodes usually includes one of either
AppArmor or SELinux. Both mechanisms provide similar types of protection, but
have differences such as the following:

* **Configuration**: AppArmor uses profiles to define access to resources.
  SELinux uses policies that apply to specific labels.
* **Policy application**: In AppArmor, you define resources using file paths.
  SELinux uses the index node (inode) of a resource to identify the resource.

### Summary of features {#summary}

The following table describes the use cases and scope of each security control.
You can use all of these controls together to build a more hardened system.

  <caption>Summary of Linux kernel security features</caption>
  
    
      Security feature
      Description
      How to use
      Example
    
  
  
    
      seccomp
      Restrict individual kernel calls in the userspace. Reduces the
      likelihood that a vulnerability that uses a restricted syscall would
      compromise the system.
      Specify a loaded seccomp profile in the Pod or container specification
      to apply its constraints to the processes in the Pod.
      Reject the <code>unshare</code> syscall, which was used in
      CVE-2022-0185.
    
    
      AppArmor
      Restrict program access to specific resources. Reduces the attack
      surface of the program. Improves audit logging.
      Specify a loaded AppArmor profile in the container specification.
      Restrict a read-only program from writing to any file path
      in the system.
    
    
      SELinux
      Restrict access to resources such as files, applications, ports, and
      processes using labels and security policies.
      Specify access restrictions for specific labels. Tag processes with
      those labels to enforce the access restrictions related to the label.
      Restrict a container from accessing files outside its own filesystem.
    
  

Mechanisms like AppArmor and SELinux can provide protection that extends beyond
the container. For example, you can use SELinux to help mitigate
CVE-2019-5736.

### Considerations for managing custom configurations {#considerations-custom-configurations}

seccomp, AppArmor, and SELinux usually have a default configuration that offers
basic protections.  You can also create custom profiles and policies that meet
the requirements of your workloads. Managing and distributing these custom
configurations at scale might be challenging, especially if you use all three
features together. To help you to manage these configurations at scale, use a
tool like the
Kubernetes Security Profiles Operator.
