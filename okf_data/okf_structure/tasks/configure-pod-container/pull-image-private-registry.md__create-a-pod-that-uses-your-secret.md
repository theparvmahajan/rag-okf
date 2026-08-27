---
id: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#create-a-pod-that-uses-your-secret
kind: section
title: Create a Pod that uses your Secret
source: tasks/configure-pod-container/pull-image-private-registry.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
heading: Create a Pod that uses your Secret
parent: okf-structure/tasks/configure-pod-container/pull-image-private-registry
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#inspecting-the-secret-regcred
next_sibling: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#using-images-from-multiple-registries
word_count: 245
---

Here is a manifest for an example Pod that needs access to your Docker credentials in `regcred`:

Download the above file onto your computer:

```shell
curl -L -o my-private-reg-pod.yaml https://k8s.io/examples/pods/private-reg-pod.yaml
```

In file `my-private-reg-pod.yaml`, replace `<your-private-image>` with the path to an image in a private registry such as:

```none
your.private.registry.example.com/janedoe/jdoe-private:v1
```

To pull the image from the private registry, Kubernetes needs credentials.
The `imagePullSecrets` field in the configuration file specifies that
Kubernetes should get the credentials from a Secret named `regcred`.

Create a Pod that uses your Secret, and verify that the Pod is running:

```shell
kubectl apply -f my-private-reg-pod.yaml
kubectl get pod private-reg
```

To use image pull secrets for a Pod (or a Deployment, or other object that
has a pod template that you are using), you need to make sure that the appropriate
Secret does exist in the right namespace. The namespace to use is the same
namespace where you defined the Pod.

Also, in case the Pod fails to start with the status `ImagePullBackOff`, view the Pod events:

```shell
kubectl describe pod private-reg
```

If you then see an event with the reason set to `FailedToRetrieveImagePullSecret`,
Kubernetes can't find a Secret with name (`regcred`, in this example).

Make sure that the Secret you have specified exists, and that its name is spelled properly.
```shell
Events:
  ...  Reason                           ...  Message
       ------                                -------
  ...  FailedToRetrieveImagePullSecret  ...  Unable to retrieve some image pull secrets (<regcred>); attempting to pull the image may not succeed.
```
