---
id: okf-structure/tasks/access-application-cluster/web-ui-dashboard.md#deploying-containerized-applications
kind: section
title: Deploying containerized applications
source: tasks/access-application-cluster/web-ui-dashboard.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/
heading: Deploying containerized applications
parent: okf-structure/tasks/access-application-cluster/web-ui-dashboard
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/web-ui-dashboard.md#welcome-view
next_sibling: okf-structure/tasks/access-application-cluster/web-ui-dashboard.md#using-dashboard
word_count: 851
---

Dashboard lets you create and deploy a containerized application as a Deployment and optional Service with a simple wizard.
You can either manually specify application details, or upload a YAML or JSON _manifest_ file containing application configuration.

Click the **CREATE** button in the upper right corner of any page to begin.

### Specifying application details

The deploy wizard expects that you provide the following information:

- **App name** (mandatory): Name for your application.
  A label with the name will be
  added to the Deployment and Service, if any, that will be deployed.

  The application name must be unique within the selected Kubernetes namespace.
  It must start with a lowercase character, and end with a lowercase character or a number,
  and contain only lowercase letters, numbers and dashes (-). It is limited to 24 characters.
  Leading and trailing spaces are ignored.

- **Container image** (mandatory):
  The URL of a public Docker container image on any registry,
  or a private image (commonly hosted on the Google Container Registry or Docker Hub).
  The container image specification must end with a colon.

- **Number of pods** (mandatory): The target number of Pods you want your application to be deployed in.
  The value must be a positive integer.

  A Deployment will be created to
  maintain the desired number of Pods across your cluster.

- **Service** (optional): For some parts of your application (e.g. frontends) you may want to expose a
  Service onto an external,
  maybe public IP address outside of your cluster (external Service).

  
  For external Services, you may need to open up one or more ports to do so.
  

  Other Services that are only visible from inside the cluster are called internal Services.

  Irrespective of the Service type, if you choose to create a Service and your container listens
  on a port (incoming), you need to specify two ports.
  The Service will be created mapping the port (incoming) to the target port seen by the container.
  This Service will route to your deployed Pods. Supported protocols are TCP and UDP.
  The internal DNS name for this Service will be the value you specified as application name above.

If needed, you can expand the **Advanced options** section where you can specify more settings:

- **Description**: The text you enter here will be added as an
  annotation
  to the Deployment and displayed in the application's details.

- **Labels**: Default labels to be used
  for your application are application name and version.
  You can specify additional labels to be applied to the Deployment, Service (if any), and Pods,
  such as release, environment, tier, partition, and release track.

  Example:

  ```conf
  release=1.0
  tier=frontend
  environment=pod
  track=stable
  ```

- **Namespace**: Kubernetes supports multiple virtual clusters backed by the same physical cluster.
  These virtual clusters are called namespaces.
  They let you partition resources into logically named groups.

  Dashboard offers all available namespaces in a dropdown list, and allows you to create a new namespace.
  The namespace name may contain a maximum of 63 alphanumeric characters and dashes (-) but can not contain capital letters.
  Namespace names should not consist of only numbers.
  If the name is set as a number, such as 10, the pod will be put in the default namespace.

  In case the creation of the namespace is successful, it is selected by default.
  If the creation fails, the first namespace is selected.

- **Image Pull Secret**:
  In case the specified Docker container image is private, it may require
  pull secret credentials.

  Dashboard offers all available secrets in a dropdown list, and allows you to create a new secret.
  The secret name must follow the DNS domain name syntax, for example `new.image-pull.secret`.
  The content of a secret must be base64-encoded and specified in a
  `.dockercfg` file.
  The secret name may consist of a maximum of 253 characters.

  In case the creation of the image pull secret is successful, it is selected by default. If the creation fails, no secret is applied.

- **CPU requirement (cores)** and **Memory requirement (MiB)**:
  You can specify the minimum resource limits
  for the container. By default, Pods run with unbounded CPU and memory limits.

- **Run command** and **Run command arguments**:
  By default, your containers run the specified Docker image's default
  entrypoint command.
  You can use the command options and arguments to override the default.

- **Run as privileged**: This setting determines whether processes in
  privileged containers
  are equivalent to processes running as root on the host.
  Privileged containers can make use of capabilities like manipulating the network stack and accessing devices.

- **Environment variables**: Kubernetes exposes Services through
  environment variables.
  You can compose environment variable or pass arguments to your commands using the values of environment variables.
  They can be used in applications to find a Service.
  Values can reference other variables using the `$(VAR_NAME)` syntax.

### Uploading a YAML or JSON file

Kubernetes supports declarative configuration.
In this style, all configuration is stored in manifests (YAML or JSON configuration files).
The manifests use Kubernetes API resource schemas.

As an alternative to specifying application details in the deploy wizard,
you can define your application in one or more manifests, and upload the files using Dashboard.
