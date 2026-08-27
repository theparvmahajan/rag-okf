---
id: okf-structure/concepts/security/pod-security-standards.md#profile-details
kind: section
title: Profile Details
source: concepts/security/pod-security-standards.md
url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
heading: Profile Details
parent: okf-structure/concepts/security/pod-security-standards
children: []
prev_sibling: okf-structure/concepts/security/pod-security-standards.md#introduction
next_sibling: okf-structure/concepts/security/pod-security-standards.md#policy-instantiation
word_count: 952
---

### Privileged

**The _Privileged_ policy is purposely-open, and entirely unrestricted.** This type of policy is
typically aimed at system- and infrastructure-level workloads managed by privileged, trusted users.

The Privileged policy is defined by an absence of restrictions. If you define a Pod where the Privileged
security policy applies, the Pod you define is able to bypass typical container isolation mechanisms.
For example, you can define a Pod that has access to the node's host network.

### Baseline

**The _Baseline_ policy is aimed at ease of adoption for common containerized workloads while
preventing known privilege escalations.** This policy is targeted at application operators and
developers of non-critical applications. The following listed controls should be
enforced/disallowed:

In this table, wildcards (`*`) indicate all elements in a list. For example,
`spec.containers[*].securityContext` refers to the Security Context object for _all defined
containers_. If any of the listed containers fails to meet the requirements, the entire pod will
fail validation.

	<caption style="display:none">Baseline policy specification</caption>
	
		
			Control
			Policy
		
		
			HostProcess
			
				Windows Pods offer the ability to run HostProcess containers which enables privileged access to the Windows host machine. Privileged access to the host is disallowed in the Baseline policy. 
				Restricted Fields
				
					<code>spec.securityContext.windowsOptions.hostProcess</code>
					<code>spec.containers[*].securityContext.windowsOptions.hostProcess</code>
					<code>spec.initContainers[*].securityContext.windowsOptions.hostProcess</code>
					<code>spec.ephemeralContainers[*].securityContext.windowsOptions.hostProcess</code>
				
				Allowed Values
				
					Undefined/nil
					<code>false</code>
				
			
		
		
			Host Namespaces
			
				Sharing the host namespaces must be disallowed.
				Restricted Fields
				
					<code>spec.hostNetwork</code>
					<code>spec.hostPID</code>
					<code>spec.hostIPC</code>
				
				Allowed Values
				
					Undefined/nil
					<code>false</code>
				
			
		
		
			Privileged Containers
			
				Privileged Pods disable most security mechanisms and must be disallowed.
				Restricted Fields
				
					<code>spec.containers[*].securityContext.privileged</code>
					<code>spec.initContainers[*].securityContext.privileged</code>
					<code>spec.ephemeralContainers[*].securityContext.privileged</code>
				
				Allowed Values
				
					Undefined/nil
					<code>false</code>
				
			
		
		
			Capabilities
			
				Adding additional capabilities beyond those listed below must be disallowed.
				Restricted Fields
				
					<code>spec.containers[*].securityContext.capabilities.add</code>
					<code>spec.initContainers[*].securityContext.capabilities.add</code>
					<code>spec.ephemeralContainers[*].securityContext.capabilities.add</code>
				
				Allowed Values
				
					Undefined/nil
					<code>AUDIT_WRITE</code>
					<code>CHOWN</code>
					<code>DAC_OVERRIDE</code>
					<code>FOWNER</code>
					<code>FSETID</code>
					<code>KILL</code>
					<code>MKNOD</code>
					<code>NET_BIND_SERVICE</code>
					<code>SETFCAP</code>
					<code>SETGID</code>
					<code>SETPCAP</code>
					<code>SETUID</code>
					<code>SYS_CHROOT</code>
				
			
		
		
			HostPath Volumes
			
				HostPath volumes must be forbidden.
				Restricted Fields
				
					<code>spec.volumes[*].hostPath</code>
				
				Allowed Values
				
					Undefined/nil
				
			
		
		
			Host Ports
			
				HostPorts should be disallowed entirely (recommended) or restricted to a known list
				Restricted Fields
				
					<code>spec.containers[*].ports[*].hostPort</code>
					<code>spec.initContainers[*].ports[*].hostPort</code>
					<code>spec.ephemeralContainers[*].ports[*].hostPort</code>
				
				Allowed Values
				
					Undefined/nil
					Known list (not supported by the built-in Pod Security Admission controller)
					<code>0</code>
				
			
		
		
			Host Probes / Lifecycle Hooks (v1.34+)
			
				The Host field in probes and lifecycle hooks must be disallowed.
				Restricted Fields
				
					<code>spec.containers[*].livenessProbe.httpGet.host</code>
					<code>spec.containers[*].readinessProbe.httpGet.host</code>
					<code>spec.containers[*].startupProbe.httpGet.host</code>
					<code>spec.containers[*].livenessProbe.tcpSocket.host</code>
					<code>spec.containers[*].readinessProbe.tcpSocket.host</code>
					<code>spec.containers[*].startupProbe.tcpSocket.host</code>
					<code>spec.containers[*].lifecycle.postStart.tcpSocket.host</code>
					<code>spec.containers[*].lifecycle.preStop.tcpSocket.host</code>
					<code>spec.containers[*].lifecycle.postStart.httpGet.host</code>
					<code>spec.containers[*].lifecycle.preStop.httpGet.host</code>
					<code>spec.initContainers[*].livenessProbe.httpGet.host</code>
					<code>spec.initContainers[*].readinessProbe.httpGet.host</code>
					<code>spec.initContainers[*].startupProbe.httpGet.host</code>
					<code>spec.initContainers[*].livenessProbe.tcpSocket.host</code>
					<code>spec.initContainers[*].readinessProbe.tcpSocket.host</code>
					<code>spec.initContainers[*].startupProbe.tcpSocket.host</code>
					<code>spec.initContainers[*].lifecycle.postStart.tcpSocket.host</code>
					<code>spec.initContainers[*].lifecycle.preStop.tcpSocket.host</code>
					<code>spec.initContainers[*].lifecycle.postStart.httpGet.host</code>
					<code>spec.initContainers[*].lifecycle.preStop.httpGet.host</code>
				
				Allowed Values
				
					Undefined/nil
					""
				
			
		
		
			AppArmor
			
				On supported hosts, the <code>RuntimeDefault</code> AppArmor profile is applied by default. The baseline policy should prevent overriding or disabling the default AppArmor profile, or restrict overrides to an allowed set of profiles.
				Restricted Fields
				
					<code>spec.securityContext.appArmorProfile.type</code>
					<code>spec.containers[*].securityContext.appArmorProfile.type</code>
					<code>spec.initContainers[*].securityContext.appArmorProfile.type</code>
					<code>spec.ephemeralContainers[*].securityContext.appArmorProfile.type</code>
				
				Allowed Values
				
					Undefined/nil
					<code>RuntimeDefault</code>
					<code>Localhost</code>
				
				<hr />
				
					<code>metadata.annotations["container.apparmor.security.beta.kubernetes.io/*"]</code>
				
				Allowed Values
				
					Undefined/nil
					<code>runtime/default</code>
					<code>localhost/*</code>
				
			
		
		
			SELinux
			
				Setting the SELinux type is restricted, and setting a custom SELinux user or role option is forbidden.
				Restricted Fields
				
					<code>spec.securityContext.seLinuxOptions.type</code>
					<code>spec.containers[*].securityContext.seLinuxOptions.type</code>
					<code>spec.initContainers[*].securityContext.seLinuxOptions.type</code>
					<code>spec.ephemeralContainers[*].securityContext.seLinuxOptions.type</code>
				
				Allowed Values
				
					Undefined/""
					<code>container_t</code>
					<code>container_init_t</code>
					<code>container_kvm_t</code>
					<code>container_engine_t</code> (since Kubernetes 1.31)
				
				<hr />
				Restricted Fields
				
					<code>spec.securityContext.seLinuxOptions.user</code>
					<code>spec.containers[*].securityContext.seLinuxOptions.user</code>
					<code>spec.initContainers[*].securityContext.seLinuxOptions.user</code>
					<code>spec.ephemeralContainers[*].securityContext.seLinuxOptions.user</code>
					<code>spec.securityContext.seLinuxOptions.role</code>
					<code>spec.containers[*].securityContext.seLinuxOptions.role</code>
					<code>spec.initContainers[*].securityContext.seLinuxOptions.role</code>
					<code>spec.ephemeralContainers[*].securityContext.seLinuxOptions.role</code>
				
				Allowed Values
				
					Undefined/""
				
			
		
		
			<code>/proc</code> Mount Type
			
				The default <code>/proc</code> masks are set up to reduce attack surface, and should be required.
				Restricted Fields
				
					<code>spec.containers[*].securityContext.procMount</code>
					<code>spec.initContainers[*].securityContext.procMount</code>
					<code>spec.ephemeralContainers[*].securityContext.procMount</code>
				
				Allowed Values
				
					Undefined/nil
					<code>Default</code>
				
			
		
		
  			Seccomp
  			
  				Seccomp profile must not be explicitly set to <code>Unconfined</code>.
  				Restricted Fields
				
					<code>spec.securityContext.seccompProfile.type</code>
					<code>spec.containers[*].securityContext.seccompProfile.type</code>
					<code>spec.initContainers[*].securityContext.seccompProfile.type</code>
					<code>spec.ephemeralContainers[*].securityContext.seccompProfile.type</code>
				
				Allowed Values
				
					Undefined/nil
					<code>RuntimeDefault</code>
					<code>Localhost</code>
				
  			
  		
		
			Sysctls
			
				Sysctls can disable security mechanisms or affect all containers on a host, and should be disallowed except for an allowed "safe" subset. A sysctl is considered safe if it is namespaced in the container or the Pod, and it is isolated from other Pods or processes on the same Node.
				Restricted Fields
				
					<code>spec.securityContext.sysctls[*].name</code>
				
				Allowed Values
				
					Undefined/nil
					<code>kernel.shm_rmid_forced</code>
					<code>net.ipv4.ip_local_port_range</code>
					<code>net.ipv4.ip_unprivileged_port_start</code>
					<code>net.ipv4.tcp_syncookies</code>
					<code>net.ipv4.ping_group_range</code>
					<code>net.ipv4.ip_local_reserved_ports</code> (since Kubernetes 1.27)
					<code>net.ipv4.tcp_keepalive_time</code> (since Kubernetes 1.29)
					<code>net.ipv4.tcp_fin_timeout</code> (since Kubernetes 1.29)
					<code>net.ipv4.tcp_keepalive_intvl</code> (since Kubernetes 1.29)
					<code>net.ipv4.tcp_keepalive_probes</code> (since Kubernetes 1.29)
				
			
		
	

### Restricted

**The _Restricted_ policy is aimed at enforcing current Pod hardening best practices, at the
expense of some compatibility.** It is targeted at operators and developers of security-critical
applications, as well as lower-trust users. The following listed controls should be
enforced/disallowed:

In this table, wildcards (`*`) indicate all elements in a list. For example,
`spec.containers[*].securityContext` refers to the Security Context object for _all defined
containers_. If any of the listed containers fails to meet the requirements, the entire pod will
fail validation.

	<caption style="display:none">Restricted policy specification</caption>
	
		
			Control
			Policy
		
		
			Everything from the Baseline policy
		
		
			Volume Types
			
				The Restricted policy only permits the following volume types.
				Restricted Fields
				
					<code>spec.volumes[*]</code>
				
				Allowed Values
				Every item in the <code>spec.volumes[*]</code> list must set one of the following fields to a non-null value:
				
					<code>spec.volumes[*].configMap</code>
					<code>spec.volumes[*].csi</code>
					<code>spec.volumes[*].downwardAPI</code>
					<code>spec.volumes[*].emptyDir</code>
					<code>spec.volumes[*].ephemeral</code>
					<code>spec.volumes[*].persistentVolumeClaim</code>
					<code>spec.volumes[*].projected</code>
					<code>spec.volumes[*].secret</code>
				
			
		
		
			Privilege Escalation (v1.8+)
			
				Privilege escalation (such as via set-user-ID or set-group-ID file mode) should not be allowed. This is Linux only policy in v1.25+ <code>(spec.os.name != windows)</code>
				Restricted Fields
				
					<code>spec.containers[*].securityContext.allowPrivilegeEscalation</code>
					<code>spec.initContainers[*].securityContext.allowPrivilegeEscalation</code>
					<code>spec.ephemeralContainers[*].securityContext.allowPrivilegeEscalation</code>
				
				Allowed Values
				
					<code>false</code>
				
			
		
		
			Running as Non-root
			
				Containers must be required to run as non-root users.
				Restricted Fields
				
					<code>spec.securityContext.runAsNonRoot</code>
					<code>spec.containers[*].securityContext.runAsNonRoot</code>
					<code>spec.initContainers[*].securityContext.runAsNonRoot</code>
					<code>spec.ephemeralContainers[*].securityContext.runAsNonRoot</code>
				
				Allowed Values
				
					<code>true</code>
				
				<small>
					The container fields may be undefined/<code>nil</code> if the pod-level
					<code>spec.securityContext.runAsNonRoot</code> is set to <code>true</code>.
				</small>
			
		
		
			Running as Non-root user (v1.23+)
			
				Containers must not set <tt>runAsUser</tt> to 0
				Restricted Fields
				
					<code>spec.securityContext.runAsUser</code>
				    <code>spec.containers[*].securityContext.runAsUser</code>
					<code>spec.initContainers[*].securityContext.runAsUser</code>
					<code>spec.ephemeralContainers[*].securityContext.runAsUser</code>
				
				Allowed Values
				
					any non-zero value
					<code>undefined/null</code>
				
			
		
		
  			Seccomp (v1.19+)
  			
  				Seccomp profile must be explicitly set to one of the allowed values. Both the <code>Unconfined</code> profile and the absence of a profile are prohibited. This is Linux only policy in v1.25+ <code>(spec.os.name != windows)</code>
  				Restricted Fields
				
					<code>spec.securityContext.seccompProfile.type</code>
					<code>spec.containers[*].securityContext.seccompProfile.type</code>
					<code>spec.initContainers[*].securityContext.seccompProfile.type</code>
					<code>spec.ephemeralContainers[*].securityContext.seccompProfile.type</code>
				
				Allowed Values
				
					<code>RuntimeDefault</code>
					<code>Localhost</code>
				
				<small>
					The container fields may be undefined/<code>nil</code> if the pod-level
					<code>spec.securityContext.seccompProfile.type</code> field is set appropriately.
					Conversely, the pod-level field may be undefined/<code>nil</code> if _all_ container-
					level fields are set.
				</small>
  			
  		
		  
			Capabilities (v1.22+)
			
				
					Containers must drop <code>ALL</code> capabilities, and are only permitted to add back
 					the <code>NET_BIND_SERVICE</code> capability. This is Linux only policy in v1.25+ <code>(.spec.os.name != "windows")</code>
				
				Restricted Fields
				
					<code>spec.containers[*].securityContext.capabilities.drop</code>
					<code>spec.initContainers[*].securityContext.capabilities.drop</code>
					<code>spec.ephemeralContainers[*].securityContext.capabilities.drop</code>
				
				Allowed Values
				
					Any list of capabilities that includes <code>ALL</code>
				
				<hr />
				Restricted Fields
				
					<code>spec.containers[*].securityContext.capabilities.add</code>
					<code>spec.initContainers[*].securityContext.capabilities.add</code>
					<code>spec.ephemeralContainers[*].securityContext.capabilities.add</code>
				
				Allowed Values
				
					Undefined/nil
					<code>NET_BIND_SERVICE</code>
