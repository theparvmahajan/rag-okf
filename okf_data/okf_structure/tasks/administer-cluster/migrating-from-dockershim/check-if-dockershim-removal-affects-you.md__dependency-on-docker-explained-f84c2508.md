---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md#dependency-on-docker-explained-role-of-dockershim
kind: section
title: Dependency on Docker explained {#role-of-dockershim}
source: tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/
heading: Dependency on Docker explained {#role-of-dockershim}
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md#finding-if-your-app-has-a-dependencies-on-docker-find-docker-dependencies
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md#known-issues
word_count: 316
---

A container runtime is software that can
execute the containers that make up a Kubernetes pod. Kubernetes is responsible for orchestration
and scheduling of Pods; on each node, the kubelet
uses the container runtime interface as an abstraction so that you can use any compatible
container runtime.

In its earliest releases, Kubernetes offered compatibility with one container runtime: Docker.
Later in the Kubernetes project's history, cluster operators wanted to adopt additional container runtimes.
The CRI was designed to allow this kind of flexibility - and the kubelet began supporting CRI. However,
because Docker existed before the CRI specification was invented, the Kubernetes project created an
adapter component, `dockershim`. The dockershim adapter allows the kubelet to interact with Docker as
if Docker were a CRI compatible runtime.

You can read about it in Kubernetes Containerd integration goes GA blog post.

Dockershim vs. CRI with Containerd

Switching to Containerd as a container runtime eliminates the middleman. All the
same containers can be run by container runtimes like Containerd as before. But
now, since containers schedule directly with the container runtime, they are not visible to Docker.
So any Docker tooling or fancy UI you might have used
before to check on these containers is no longer available.

You cannot get container information using `docker ps` or `docker inspect`
commands. As you cannot list containers, you cannot get logs, stop containers,
or execute something inside a container using `docker exec`.

If you're running workloads via Kubernetes, the best way to stop a container is through
the Kubernetes API rather than directly through the container runtime (this advice applies
for all container runtimes, not only Docker).

You can still pull images or build them using `docker build` command. But images
built or pulled by Docker would not be visible to container runtime and
Kubernetes. They needed to be pushed to some registry to allow them to be used
by Kubernetes.
