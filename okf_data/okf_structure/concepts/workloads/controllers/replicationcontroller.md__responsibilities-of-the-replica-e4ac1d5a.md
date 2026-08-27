---
id: okf-structure/concepts/workloads/controllers/replicationcontroller.md#responsibilities-of-the-replicationcontroller
kind: section
title: Responsibilities of the ReplicationController
source: concepts/workloads/controllers/replicationcontroller.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/
heading: Responsibilities of the ReplicationController
parent: okf-structure/concepts/workloads/controllers/replicationcontroller
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/replicationcontroller.md#writing-programs-for-replication
next_sibling: okf-structure/concepts/workloads/controllers/replicationcontroller.md#api-object
word_count: 235
---

The ReplicationController ensures that the desired number of pods matches its label selector and are operational. Currently, only terminated pods are excluded from its count. In the future, readiness and other information available from the system may be taken into account, we may add more controls over the replacement policy, and we plan to emit events that could be used by external clients to implement arbitrarily sophisticated replacement and/or scale-down policies.

The ReplicationController is forever constrained to this narrow responsibility. It itself will not perform readiness nor liveness probes. Rather than performing auto-scaling, it is intended to be controlled by an external auto-scaler (as discussed in #492), which would change its `replicas` field. We will not add scheduling policies (for example, spreading) to the ReplicationController. Nor should it verify that the pods controlled match the currently specified template, as that would obstruct auto-sizing and other automated processes. Similarly, completion deadlines, ordering dependencies, configuration expansion, and other features belong elsewhere. We even plan to factor out the mechanism for bulk pod creation (#170).

The ReplicationController is intended to be a composable building-block primitive. We expect higher-level APIs and/or tools to be built on top of it and other complementary primitives for user convenience in the future. The "macro" operations currently supported by kubectl (run, scale) are proof-of-concept examples of this. For instance, we could imagine something like Asgard managing ReplicationControllers, auto-scalers, services, scheduling policies, canaries, etc.
