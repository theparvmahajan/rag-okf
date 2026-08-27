---
id: okf-structure/tasks/job/job-with-pod-to-pod-communication.md#starting-a-job-with-pod-to-pod-communication
kind: section
title: Starting a Job with pod-to-pod communication
source: tasks/job/job-with-pod-to-pod-communication.md
url: https://kubernetes.io/docs/tasks/job/job-with-pod-to-pod-communication/
heading: Starting a Job with pod-to-pod communication
parent: okf-structure/tasks/job/job-with-pod-to-pod-communication
children: []
prev_sibling: okf-structure/tasks/job/job-with-pod-to-pod-communication.md#prerequisites
next_sibling: null
word_count: 376
---

To enable pod-to-pod communication using pod hostnames in a Job, you must do the following:

1. Set up a headless Service
   with a valid label selector for the pods created by your Job. The headless service must be
   in the same namespace as the Job. One easy way to do this is to use the
   `job-name: <your-job-name>` selector, since the `job-name` label will be automatically added
   by Kubernetes. This configuration will trigger the DNS system to create records of the hostnames
   of the pods running your Job.

1. Configure the headless service as subdomain service for the Job pods by including the following
   value in your Job template spec:

   ```yaml
   subdomain: <headless-svc-name>
   ```

### Example

Below is a working example of a Job with pod-to-pod communication via pod hostnames enabled.
The Job is completed only after all pods successfully ping each other using hostnames.

In the Bash script executed on each pod in the example below, the pod hostnames can be prefixed
by the namespace as well if the pod needs to be reached from outside the namespace.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: headless-svc
spec:
  clusterIP: None # clusterIP must be None to create a headless service
  selector:
    job-name: example-job # must match Job name
---
apiVersion: batch/v1
kind: Job
metadata:
  name: example-job
spec:
  completions: 3
  parallelism: 3
  completionMode: Indexed
  template:
    spec:
      subdomain: headless-svc # has to match Service name
      restartPolicy: Never
      containers:
      - name: example-workload
        image: bash:latest
        command:
        - bash
        - -c
        - |
          for i in 0 1 2
          do
            gotStatus="-1"
            wantStatus="0"             
            while [ $gotStatus -ne $wantStatus ]
            do                                       
              ping -c 1 example-job-${i}.headless-svc > /dev/null 2>&1
              gotStatus=$?                
              if [ $gotStatus -ne $wantStatus ]; then
                echo "Failed to ping pod example-job-${i}.headless-svc, retrying in 1 second..."
                sleep 1
              fi
            done                                                         
            echo "Successfully pinged pod: example-job-${i}.headless-svc"
          done
```

After applying the example above, reach each other over the network
using: `<pod-hostname>.<headless-service-name>`. You should see output similar to the following:

```shell
kubectl logs example-job-0-qws42
```

```
Failed to ping pod example-job-0.headless-svc, retrying in 1 second...
Successfully pinged pod: example-job-0.headless-svc
Successfully pinged pod: example-job-1.headless-svc
Successfully pinged pod: example-job-2.headless-svc
```

Keep in mind that the `<pod-hostname>.<headless-service-name>` name format used
in this example would not work with DNS policy set to `None` or `Default`.
Refer to Pod's DNS Policy.
