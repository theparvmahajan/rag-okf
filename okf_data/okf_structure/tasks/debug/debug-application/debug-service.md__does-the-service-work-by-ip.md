---
id: okf-structure/tasks/debug/debug-application/debug-service.md#does-the-service-work-by-ip
kind: section
title: Does the Service work by IP?
source: tasks/debug/debug-application/debug-service.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/
heading: Does the Service work by IP?
parent: okf-structure/tasks/debug/debug-application/debug-service
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-service.md#does-the-service-work-by-dns-name
next_sibling: okf-structure/tasks/debug/debug-application/debug-service.md#is-the-service-defined-correctly
word_count: 83
---

Assuming you have confirmed that DNS works, the next thing to test is whether your
Service works by its IP address.  From a Pod in your cluster, access the
Service's IP (from `kubectl get` above).

```shell
for i in $(seq 1 3); do 
    wget -qO- 10.0.1.175:80
done
```

This should produce something like:

```
hostnames-632524106-bbpiw
hostnames-632524106-ly40y
hostnames-632524106-tlaok
```

If your Service is working, you should get correct responses.  If not, there
are a number of things that could be going wrong.  Read on.
