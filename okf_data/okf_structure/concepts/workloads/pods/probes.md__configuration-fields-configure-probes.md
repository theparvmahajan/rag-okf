---
id: okf-structure/concepts/workloads/pods/probes.md#configuration-fields-configure-probes
kind: section
title: Configuration fields {#configure-probes}
source: concepts/workloads/pods/probes.md
url: https://kubernetes.io/docs/concepts/workloads/pods/probes/
heading: Configuration fields {#configure-probes}
parent: okf-structure/concepts/workloads/pods/probes
children: []
prev_sibling: okf-structure/concepts/workloads/pods/probes.md#probe-results-probe-results
next_sibling: okf-structure/concepts/workloads/pods/probes.md#probe-mechanism-details-probe-mechanism-details
word_count: 587
---

Probes
have a number of fields that you can use to more precisely control the behavior of startup,
liveness and readiness checks. For example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: probe-example
spec:
  containers:
  - name: app
    image: registry.k8s.io/e2e-test-images/agnhost:2.40
    ports:
    - containerPort: 8080
    startupProbe:
      httpGet:
        path: /healthz
        port: 8080
      failureThreshold: 30
      periodSeconds: 10
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 10
      periodSeconds: 5
      timeoutSeconds: 3
      failureThreshold: 3
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      periodSeconds: 5
```

`initialDelaySeconds`
: Number of seconds after the container has started before startup, liveness or readiness probes are initiated. If a startup probe is defined, liveness and readiness probe delays do not begin until the startup probe has succeeded. In some older Kubernetes versions, the initialDelaySeconds might be ignored if periodSeconds was set to a value higher than initialDelaySeconds. However, in current versions, initialDelaySeconds is always honored and the probe will not start until after this initial delay. Defaults to 0 seconds. Minimum value is 0.

`periodSeconds`
: How often (in seconds) to perform the probe. Default to 10 seconds. The minimum value is 1. While a container is not Ready, the readiness probe may be executed at times other than the configured `periodSeconds` interval. This is to make the Pod ready faster.

`timeoutSeconds`
: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1.

`successThreshold`
: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup Probes. Minimum value is 1.

`failureThreshold`
: After a probe fails `failureThreshold` times in a row, Kubernetes considers that the overall check has failed: the container is _not_ ready/healthy/live. Defaults to 3. Minimum value is 1. For the case of a startup or liveness probe, if at least `failureThreshold` probes have failed, Kubernetes treats the container as unhealthy and triggers a restart for that specific container. The kubelet honors the setting of `terminationGracePeriodSeconds` for that container. For a failed readiness probe, the kubelet continues running the container that failed checks, and also continues to run more probes; because the check failed, the kubelet sets the `Ready` condition on the Pod to `false`.

`terminationGracePeriodSeconds`
: configure a grace period for the kubelet to wait between triggering a shut down of the failed container, and then forcing the container runtime to stop that container. The default is to inherit the Pod-level value for `terminationGracePeriodSeconds` (30 seconds if not specified), and the minimum value is 1. See probe-level `terminationGracePeriodSeconds` for more detail.

Incorrect implementation of readiness probes may result in an ever growing
number of processes in the container, and resource starvation if this is left
unchecked.

### Probe-level `terminationGracePeriodSeconds` {#probe-level-terminationgraceperiodseconds}

In 1.25 and above, users can specify a probe-level `terminationGracePeriodSeconds`
as part of the probe specification. When both a pod- and probe-level
`terminationGracePeriodSeconds` are set, the kubelet will use the probe-level
value.

When setting the `terminationGracePeriodSeconds`, note the following:

* The kubelet always honors the probe-level `terminationGracePeriodSeconds`
  field if it is present on a Pod.
* If you have existing Pods where the `terminationGracePeriodSeconds` field is
  set and you no longer wish to use per-probe termination grace periods, you
  must delete those existing Pods.

For example:

```yaml
spec:
  terminationGracePeriodSeconds: 3600  # pod-level
  containers:
  - name: test
    image: ...

    ports:
    - name: liveness-port
      containerPort: 8080

    livenessProbe:
      httpGet:
        path: /healthz
        port: liveness-port
      failureThreshold: 1
      periodSeconds: 60
      # Override pod-level terminationGracePeriodSeconds
      terminationGracePeriodSeconds: 60
```

Probe-level `terminationGracePeriodSeconds` **cannot** be set for readiness probes.
It will be rejected by the API server.
