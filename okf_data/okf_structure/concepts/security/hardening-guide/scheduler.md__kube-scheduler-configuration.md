---
id: okf-structure/concepts/security/hardening-guide/scheduler.md#kube-scheduler-configuration
kind: section
title: kube-scheduler configuration
source: concepts/security/hardening-guide/scheduler.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/scheduler/
heading: kube-scheduler configuration
parent: okf-structure/concepts/security/hardening-guide/scheduler
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/scheduler.md#introduction
next_sibling: okf-structure/concepts/security/hardening-guide/scheduler.md#scheduling-configurations-for-custom-schedulers
word_count: 305
---

### Scheduler authentication & authorization command line options

When setting up authentication configuration, it should be made sure that
kube-scheduler's authentication remains consistent with kube-api-server's authentication. 
If any request has missing authentication headers, the authentication should happen through the kube-api-server
allowing all authentication to be consistent in the cluster.

- `authentication-kubeconfig`: Make sure to provide a proper kubeconfig so that
  the scheduler can retrieve authentication configuration options from the API Server.
  This kubeconfig file should be protected with strict file permissions.
- `authentication-tolerate-lookup-failure`: Set this to `false` to make sure
  the scheduler _always_ looks up its authentication configuration from the API server.
- `authentication-skip-lookup`: Set this to `false` to make sure
  the scheduler _always_ looks up its authentication configuration from the API server.
- `authorization-always-allow-paths`: These paths should respond with data that is appropriate
  for anonymous authorization. Defaults to `/healthz,/readyz,/livez`.
- `profiling`: Set to `false` to disable the profiling endpoints which are provide debugging information
  but which should not be enabled on production clusters as they present a risk of denial of service
  or information leakage. The `--profiling` argument is deprecated and can now be provided through the
  KubeScheduler DebuggingConfiguration.
  Profiling can be disabled through the kube-scheduler config by setting `enableProfiling` to `false`. 
- `requestheader-client-ca-file`: Avoid passing this argument.

### Scheduler networking command line options

- `bind-address`: In most cases, the kube-scheduler does not need to be externally accessible.
  Setting the bind address to `localhost` is a secure practice.
- `permit-address-sharing`: Set this to `false` to  disable connection sharing through `SO_REUSEADDR`.
  `SO_REUSEADDR` can lead to reuse of terminated connections that are in `TIME_WAIT` state.
- `permit-port-sharing`: Default `false`. Use the default unless you are confident you understand the security implications.

### Scheduler TLS command line options

- `tls-cipher-suites`: Always provide a list of preferred cipher suites.
  This ensures encryption never happens with insecure cipher suites.
