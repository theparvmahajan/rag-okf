---
id: okf-structure/tasks/debug/debug-cluster/topology.md#examples
kind: section
title: Examples
source: tasks/debug/debug-cluster/topology.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/topology/
heading: Examples
parent: okf-structure/tasks/debug/debug-cluster/topology
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/topology.md#examine-system-logs
next_sibling: okf-structure/tasks/debug/debug-cluster/topology.md#check-the-device-plugin-resource-api-device-plugin-resource-api
word_count: 314
---

### Examine the memory manager state on a node

Let us first deploy a sample `Guaranteed` pod whose specification is as follows:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: guaranteed
spec:
  containers:
  - name: guaranteed
    image: consumer
    imagePullPolicy: Never
    resources:
      limits:
        cpu: "2"
        memory: 150Gi
      requests:
        cpu: "2"
        memory: 150Gi
    command: ["sleep","infinity"]
```

Next, log into the node where it was deployed and examine the state file in
`/var/lib/kubelet/memory_manager_state`:

```json
{
   "policyName":"Static",
   "machineState":{
      "0":{
         "numberOfAssignments":1,
         "memoryMap":{
            "hugepages-1Gi":{
               "total":0,
               "systemReserved":0,
               "allocatable":0,
               "reserved":0,
               "free":0
            },
            "memory":{
               "total":134987354112,
               "systemReserved":3221225472,
               "allocatable":131766128640,
               "reserved":131766128640,
               "free":0
            }
         },
         "nodes":[
            0,
            1
         ]
      },
      "1":{
         "numberOfAssignments":1,
         "memoryMap":{
            "hugepages-1Gi":{
               "total":0,
               "systemReserved":0,
               "allocatable":0,
               "reserved":0,
               "free":0
            },
            "memory":{
               "total":135286722560,
               "systemReserved":2252341248,
               "allocatable":133034381312,
               "reserved":29295144960,
               "free":103739236352
            }
         },
         "nodes":[
            0,
            1
         ]
      }
   },
   "entries":{
      "fa9bdd38-6df9-4cf9-aa67-8c4814da37a8":{
         "guaranteed":[
            {
               "numaAffinity":[
                  0,
                  1
               ],
               "type":"memory",
               "size":161061273600
            }
         ]
      }
   },
   "checksum":4142013182
}
```

It can be deduced from the state file that the pod was pinned to both NUMA nodes, i.e.:

```json
"numaAffinity":[
   0,
   1
],
```

Pinned term means that pod's memory consumption is constrained (through `cgroups` configuration)
to these NUMA nodes.

This automatically implies that Memory Manager instantiated a new group that
comprises these two NUMA nodes, i.e. `0` and `1` indexed NUMA nodes.

In order to analyse memory resources available in a group,the corresponding entries from
NUMA nodes belonging to the group must be added up.

For example, the total amount of free "conventional" memory in the group can be computed
by adding up the free memory available at every NUMA node in the group,
i.e., in the `"memory"` section of NUMA node `0` (`"free":0`) and NUMA node `1` (`"free":103739236352`).
So, the total amount of free "conventional" memory in this group is equal to `0 + 103739236352` bytes.

The line `"systemReserved":3221225472` indicates that the administrator of this node reserved
`3221225472` bytes (i.e. `3Gi`) to serve kubelet and system processes at NUMA node `0`,
by using `--reserved-memory` flag.
