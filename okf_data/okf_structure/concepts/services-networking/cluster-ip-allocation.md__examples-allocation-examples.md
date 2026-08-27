---
id: okf-structure/concepts/services-networking/cluster-ip-allocation.md#examples-allocation-examples
kind: section
title: Examples {#allocation-examples}
source: concepts/services-networking/cluster-ip-allocation.md
url: https://kubernetes.io/docs/concepts/services-networking/cluster-ip-allocation/
heading: Examples {#allocation-examples}
parent: okf-structure/concepts/services-networking/cluster-ip-allocation
children: []
prev_sibling: okf-structure/concepts/services-networking/cluster-ip-allocation.md#how-can-you-avoid-service-clusterip-conflicts-avoid-clusterip-conflict
next_sibling: okf-structure/concepts/services-networking/cluster-ip-allocation.md#whatsnext
word_count: 174
---

### Example 1 {#allocation-example-1}

This example uses the IP address range: 10.96.0.0/24 (CIDR notation) for the IP addresses
of Services.

Range Size: 2<sup>8</sup> - 2 = 254  
Band Offset: `min(max(16, 256/16), 256)` = `min(16, 256)` = 16  
Static band start: 10.96.0.1  
Static band end: 10.96.0.16  
Range end: 10.96.0.254   

pie showData
    title 10.96.0.0/24
    "Static" : 16
    "Dynamic" : 238

### Example 2 {#allocation-example-2}

This example uses the IP address range: 10.96.0.0/20 (CIDR notation) for the IP addresses
of Services.

Range Size: 2<sup>12</sup> - 2 = 4094  
Band Offset: `min(max(16, 4096/16), 256)` = `min(256, 256)` = 256  
Static band start: 10.96.0.1  
Static band end: 10.96.1.0  
Range end: 10.96.15.254  

pie showData
    title 10.96.0.0/20
    "Static" : 256
    "Dynamic" : 3838

### Example 3 {#allocation-example-3}

This example uses the IP address range: 10.96.0.0/16 (CIDR notation) for the IP addresses
of Services.

Range Size: 2<sup>16</sup> - 2 = 65534  
Band Offset: `min(max(16, 65536/16), 256)` = `min(4096, 256)` = 256  
Static band start: 10.96.0.1  
Static band ends: 10.96.1.0  
Range end: 10.96.255.254  

pie showData
    title 10.96.0.0/16
    "Static" : 256
    "Dynamic" : 65278
