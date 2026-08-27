---
id: okf-structure/concepts/extend-kubernetes/_index.md#api-access-extensions
kind: section
title: API access extensions
source: concepts/extend-kubernetes/_index.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/
heading: API access extensions
parent: okf-structure/concepts/extend-kubernetes/_index
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/_index.md#api-extensions
next_sibling: okf-structure/concepts/extend-kubernetes/_index.md#infrastructure-extensions
word_count: 260
---

When a request reaches the Kubernetes API Server, it is first _authenticated_, then _authorized_,
and is then subject to various types of _admission control_ (some requests are in fact not
authenticated, and get special treatment). See
Controlling Access to the Kubernetes API
for more on this flow.

Each of the steps in the Kubernetes authentication / authorization flow offers extension points.

### Authentication

Authentication maps headers or certificates
in all requests to a username for the client making the request.

Kubernetes has several built-in authentication methods that it supports. It can also sit behind an
authenticating proxy, and it can send a token from an `Authorization:` header to a remote service for
verification (an authentication webhook)
if those don't meet your needs.

### Authorization

Authorization determines whether specific
users can read, write, and do other operations on API resources. It works at the level of whole
resources -- it doesn't discriminate based on arbitrary object fields.

If the built-in authorization options don't meet your needs, an
authorization webhook
allows calling out to custom code that makes an authorization decision.

### Dynamic admission control

After a request is authorized, if it is a write operation, it also goes through
Admission Control steps.
In addition to the built-in steps, there are several extensions:

* The Image Policy webhook
  restricts what images can be run in containers.
* To make arbitrary admission control decisions, a general
  Admission webhook
  can be used. Admission webhooks can reject creations or updates.
  Some admission webhooks modify the incoming request data before it is handled further by Kubernetes.
