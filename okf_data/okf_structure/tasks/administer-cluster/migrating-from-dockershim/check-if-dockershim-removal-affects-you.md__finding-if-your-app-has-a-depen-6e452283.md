---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md#finding-if-your-app-has-a-dependencies-on-docker-find-docker-dependencies
kind: section
title: Finding if your app has a dependencies on Docker {#find-docker-dependencies}
source: tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/
heading: Finding if your app has a dependencies on Docker {#find-docker-dependencies}
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md#dependency-on-docker-explained-role-of-dockershim
word_count: 249
---

If you are using Docker for building your application containers, you can still
run these containers on any container runtime. This use of Docker does not count
as a dependency on Docker as a container runtime.

When alternative container runtime is used, executing Docker commands may either
not work or yield unexpected output. This is how you can find whether you have a
dependency on Docker:

1. Make sure no privileged Pods execute Docker commands (like `docker ps`),
   restart the Docker service (commands such as `systemctl restart docker.service`),
   or modify Docker-specific files such as `/etc/docker/daemon.json`.
1. Check for any private registries or image mirror settings in the Docker
   configuration file (like `/etc/docker/daemon.json`). Those typically need to
   be reconfigured for another container runtime.
1. Check that scripts and apps running on nodes outside of your Kubernetes
   infrastructure do not execute Docker commands. It might be:
   - SSH to nodes to troubleshoot;
   - Node startup scripts;
   - Monitoring and security agents installed on nodes directly.
1. Third-party tools that perform above mentioned privileged operations. See
   Migrating telemetry and security agents from dockershim
   for more information.
1. Make sure there are no indirect dependencies on dockershim behavior.
   This is an edge case and unlikely to affect your application. Some tooling may be configured
   to react to Docker-specific behaviors, for example, raise alert on specific metrics or search for
   a specific log message as part of troubleshooting instructions.
   If you have such tooling configured, test the behavior on a test
   cluster before migration.
