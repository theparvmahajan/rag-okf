"""
Curated ontology of Kubernetes object kinds and the relationships between
them - this is OKF Version B's actual content (the "new, unpublished thing"
being tested, vs. Version A's pure document structure).

Why this is hand-curated rather than extracted from the corpus:
The SSRN paper's OKF links were document-structural (parent/child/sibling
inside one PDF's outline) and explicitly did NOT test "richer semantic
graphs or entity relations" (Discussion 8.2, and the Limitations section
calls this out directly as future work). To test that gap, Version B needs
edges that describe what the *objects* do to each other (Service selects
Pod, Deployment owns ReplicaSet, ...), not what the *documents* do to each
other. Kubernetes' controller/ownership/selection model is stable, public
API-machinery behavior - not paraphrased from any single source - so it's
written here directly, in plain language, and then each edge is grounded
against this specific corpus by okf/relations_builder.py's keyword search
(see GROUNDING NOTE there) so retrieval still points at real corpus pages,
not at text invented for this ontology.

Each edge:
  subject   - kind name (must be a key in KINDS)
  predicate - short relation verb phrase, subject -> object
  object    - kind name (must be a key in KINDS)
  note      - 1-2 sentences, plain language, explaining the mechanism
  keywords  - extra terms (beyond subject/object names) used to help
              ground this specific edge against corpus text, e.g.
              "owner reference" for ownership edges vs. "label selector"
              for selection edges - two edges can share subject+object
              (Deployment->Pod is implied two ways) but need different
              grounding terms.
"""

KINDS = {
    "Pod": "The smallest deployable unit - one or more containers that share "
           "network and storage, scheduled together onto a single Node.",
    "Container": "A single running process image inside a Pod, defined in "
                 "the Pod's container spec.",
    "ReplicaSet": "Ensures a specified number of identical Pod replicas are "
                  "running at any time, replacing Pods that fail or are deleted.",
    "Deployment": "Declaratively manages ReplicaSets to provide rolling "
                  "updates, rollbacks, and scaling for stateless Pods.",
    "StatefulSet": "Manages Pods that need a stable network identity, stable "
                    "storage, and ordered, sequential deployment/scaling.",
    "DaemonSet": "Ensures a copy of a Pod runs on every (or every matching) "
                 "Node in the cluster, added or removed as Nodes join or leave.",
    "Job": "Runs Pods to completion for a finite task, retrying on failure "
           "up to a configured limit.",
    "CronJob": "Creates Jobs on a repeating schedule, like a cluster-native cron.",
    "Service": "A stable virtual IP and DNS name that load-balances traffic "
               "to a dynamic set of Pods, found via a label selector.",
    "EndpointSlice": "Tracks the actual set of network endpoints (Pod IPs and "
                      "ports) that currently match a Service's selector.",
    "Ingress": "Routes external HTTP/HTTPS traffic to Services inside the "
               "cluster based on host/path rules.",
    "IngressClass": "Identifies which ingress controller implementation "
                     "should handle a given Ingress resource.",
    "NetworkPolicy": "Firewall-like rules that restrict which Pods may "
                      "communicate with which other Pods or endpoints.",
    "ConfigMap": "Holds non-secret configuration data as key/value pairs "
                 "that can be injected into Pods as env vars, files, or CLI args.",
    "Secret": "Like a ConfigMap but for sensitive data (credentials, tokens, "
              "keys), with extra access and storage conventions.",
    "PersistentVolume": "A piece of storage provisioned in the cluster, "
                         "independent of any single Pod's lifecycle.",
    "PersistentVolumeClaim": "A Pod's request for storage, bound to a "
                              "matching PersistentVolume so the Pod can mount it.",
    "StorageClass": "Describes a class of storage and its provisioner, used "
                     "to dynamically create a PersistentVolume for a claim.",
    "ServiceAccount": "An identity that Pods use to authenticate to the "
                       "Kubernetes API server.",
    "Role": "A namespaced set of permissions (verbs on resources) within "
            "the Kubernetes RBAC system.",
    "RoleBinding": "Grants the permissions in a Role to a user, group, or "
                   "ServiceAccount, scoped to one Namespace.",
    "ClusterRole": "Like a Role, but not namespaced - defines permissions "
                   "cluster-wide or for cluster-scoped resources.",
    "ClusterRoleBinding": "Grants the permissions in a ClusterRole "
                          "cluster-wide, to a user, group, or ServiceAccount.",
    "Namespace": "A logical partition inside one cluster; most object kinds "
                 "live inside exactly one Namespace and are isolated from others.",
    "Node": "A worker machine (VM or physical) that the control plane "
            "schedules Pods onto.",
    "HorizontalPodAutoscaler": "Automatically adjusts the replica count of a "
                                "Deployment/ReplicaSet/StatefulSet based on "
                                "observed metrics like CPU or custom metrics.",
    "PodDisruptionBudget": "Limits how many Pods of a set can be voluntarily "
                            "disrupted at once (e.g. during a Node drain), "
                            "protecting availability.",
    "ResourceQuota": "Caps the total compute/storage/object-count resources "
                      "that can be consumed within one Namespace.",
    "LimitRange": "Sets default and min/max resource constraints for "
                  "individual Pods/Containers within a Namespace.",
    "PriorityClass": "A named priority level that can be assigned to Pods, "
                      "used by the scheduler to decide preemption order.",
}

EDGES = [
    dict(subject="Deployment", predicate="owns", object="ReplicaSet",
         note="A Deployment creates and owns ReplicaSets via an owner "
              "reference; the garbage collector uses that reference, not "
              "labels, to cascade-delete ReplicaSets when the Deployment "
              "is deleted.",
         keywords=["owner reference", "garbage collection", "owns"]),
    dict(subject="ReplicaSet", predicate="owns", object="Pod",
         note="A ReplicaSet creates and owns the Pods matching its "
              "selector via an owner reference, and recreates them if "
              "they disappear.",
         keywords=["owner reference", "garbage collection", "replicas"]),
    dict(subject="Deployment", predicate="manages rollout via", object="ReplicaSet",
         note="Updating a Deployment's Pod template creates a new "
              "ReplicaSet and gradually scales it up while scaling the "
              "old ReplicaSet down - a rolling update.",
         keywords=["rolling update", "rollout", "revision", "scale"]),
    dict(subject="StatefulSet", predicate="owns", object="Pod",
         note="A StatefulSet creates Pods directly (no intermediate "
              "ReplicaSet) with a stable name, ordinal index, and "
              "persistent identity across rescheduling.",
         keywords=["ordinal", "stable network identity", "owns"]),
    dict(subject="DaemonSet", predicate="owns", object="Pod",
         note="A DaemonSet ensures one matching Pod runs on every Node "
              "(or every Node matching a selector), adding or removing "
              "Pods as Nodes join or leave.",
         keywords=["every node", "owns", "node selector"]),
    dict(subject="Job", predicate="owns", object="Pod",
         note="A Job creates one or more Pods and tracks them to "
              "completion, retrying failed Pods up to a configured "
              "backoff limit.",
         keywords=["owns", "completions", "backoff limit"]),
    dict(subject="CronJob", predicate="creates", object="Job",
         note="A CronJob creates a new Job object on each scheduled "
              "trigger; the Job then owns its own Pods as usual.",
         keywords=["schedule", "creates a job", "cron"]),
    dict(subject="Service", predicate="selects", object="Pod",
         note="A Service finds the Pods it load-balances to via a label "
              "selector matched against Pod labels, not owner references.",
         keywords=["label selector", "selects", "matchLabels"]),
    dict(subject="Service", predicate="backed by", object="EndpointSlice",
         note="The endpoints controller watches a Service's selector and "
              "keeps a matching EndpointSlice updated with the current "
              "set of Pod IPs and ports.",
         keywords=["endpointslice", "endpoints controller", "backed"]),
    dict(subject="Ingress", predicate="routes to", object="Service",
         note="An Ingress defines host/path rules that an ingress "
              "controller uses to forward external traffic to a named "
              "Service.",
         keywords=["routes", "backend", "host", "path"]),
    dict(subject="Ingress", predicate="implemented by", object="IngressClass",
         note="An Ingress references an IngressClass to say which "
              "controller implementation should handle it, since a "
              "cluster can run more than one.",
         keywords=["ingressclass", "controller", "implementation"]),
    dict(subject="NetworkPolicy", predicate="selects", object="Pod",
         note="A NetworkPolicy applies to the Pods matched by its pod "
              "selector, restricting the ingress/egress traffic those "
              "Pods are allowed.",
         keywords=["podselector", "ingress", "egress", "network policy"]),
    dict(subject="Pod", predicate="mounts", object="ConfigMap",
         note="A Pod can consume a ConfigMap as mounted files, "
              "environment variables, or command-line arguments.",
         keywords=["mount", "volume", "configmap", "env"]),
    dict(subject="Pod", predicate="mounts", object="Secret",
         note="A Pod can consume a Secret the same way it consumes a "
              "ConfigMap - mounted files or environment variables - with "
              "extra handling conventions since the data is sensitive.",
         keywords=["mount", "volume", "secret", "env"]),
    dict(subject="Pod", predicate="claims storage via", object="PersistentVolumeClaim",
         note="A Pod references a PersistentVolumeClaim by name in its "
              "volumes list to get durable storage that outlives the Pod "
              "itself.",
         keywords=["persistentvolumeclaim", "volume", "claim"]),
    dict(subject="PersistentVolumeClaim", predicate="binds", object="PersistentVolume",
         note="A PersistentVolumeClaim is matched and bound to a "
              "PersistentVolume whose capacity, access mode, and class "
              "satisfy the claim's request.",
         keywords=["bound", "bind", "persistentvolume", "claim"]),
    dict(subject="PersistentVolumeClaim", predicate="provisioned via", object="StorageClass",
         note="If no PersistentVolume already matches a claim, the "
              "claim's StorageClass tells its provisioner to create one "
              "dynamically.",
         keywords=["storageclass", "dynamic provisioning", "provisioner"]),
    dict(subject="Pod", predicate="scheduled onto", object="Node",
         note="The scheduler assigns a Pod to a Node that satisfies its "
              "resource requests, node selector/affinity rules, and any "
              "taints the Node has that the Pod must tolerate.",
         keywords=["scheduler", "node selector", "affinity", "taint", "toleration"]),
    dict(subject="Pod", predicate="authenticates as", object="ServiceAccount",
         note="Every Pod runs under a ServiceAccount identity (default "
              "one if none is specified) used for API server "
              "authentication from inside the Pod.",
         keywords=["serviceaccount", "authenticate", "token"]),
    dict(subject="RoleBinding", predicate="grants", object="Role",
         note="A RoleBinding attaches the permissions defined in a Role "
              "to specific subjects (users, groups, or ServiceAccounts) "
              "within one Namespace.",
         keywords=["rolebinding", "subjects", "grants", "rbac"]),
    dict(subject="ClusterRoleBinding", predicate="grants", object="ClusterRole",
         note="A ClusterRoleBinding attaches the permissions in a "
              "ClusterRole to subjects cluster-wide, rather than scoped "
              "to one Namespace.",
         keywords=["clusterrolebinding", "subjects", "grants", "rbac"]),
    dict(subject="HorizontalPodAutoscaler", predicate="scales", object="Deployment",
         note="An HPA watches metrics (e.g. CPU utilization) and adjusts "
              "the replica count on the Deployment (or other scalable "
              "controller) it targets.",
         keywords=["autoscale", "target", "metrics", "replicas"]),
    dict(subject="PodDisruptionBudget", predicate="protects", object="Pod",
         note="A PodDisruptionBudget caps how many of a matching set of "
              "Pods can be evicted at once during voluntary disruptions "
              "like a Node drain or cluster upgrade.",
         keywords=["disruption budget", "eviction", "voluntary disruption"]),
    dict(subject="ResourceQuota", predicate="constrains", object="Namespace",
         note="A ResourceQuota caps the total resources (CPU, memory, "
              "object counts) that can be consumed by everything inside "
              "one Namespace.",
         keywords=["resourcequota", "namespace", "quota", "limit"]),
    dict(subject="LimitRange", predicate="constrains", object="Namespace",
         note="A LimitRange sets default and min/max per-Pod or "
              "per-Container resource constraints for everything created "
              "in one Namespace.",
         keywords=["limitrange", "namespace", "default", "min", "max"]),
    dict(subject="PriorityClass", predicate="assigns priority to", object="Pod",
         note="A Pod references a PriorityClass to get a priority value "
              "the scheduler uses to decide preemption order under "
              "resource pressure.",
         keywords=["priorityclass", "preemption", "priority"]),
    dict(subject="Pod", predicate="contains", object="Container",
         note="A Pod's spec lists one or more Containers that share the "
              "Pod's network namespace and, optionally, its volumes.",
         keywords=["container", "pod spec", "contains"]),
    dict(subject="Namespace", predicate="scopes", object="Pod",
         note="A Pod exists inside exactly one Namespace, which isolates "
              "it (by name) from same-named objects in other Namespaces.",
         keywords=["namespace", "scoped", "namespaced"]),
    dict(subject="Namespace", predicate="scopes", object="Service",
         note="A Service is namespaced; Pods in other Namespaces must use "
              "its qualified DNS name to reach it across the boundary.",
         keywords=["namespace", "scoped", "dns", "cross-namespace"]),
]
