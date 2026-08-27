---
id: okf-structure/concepts/security/controlling-access.md#authentication
kind: section
title: Authentication
source: concepts/security/controlling-access.md
url: https://kubernetes.io/docs/concepts/security/controlling-access/
heading: Authentication
parent: okf-structure/concepts/security/controlling-access
children: []
prev_sibling: okf-structure/concepts/security/controlling-access.md#transport-security
next_sibling: okf-structure/concepts/security/controlling-access.md#authorization
word_count: 190
---

Once TLS is established, the HTTP request moves to the Authentication step.
This is shown as step **1** in the diagram.
The cluster creation script or cluster admin configures the API server to run
one or more Authenticator modules.
Authenticators are described in more detail in
Authentication.

The input to the authentication step is the entire HTTP request; however, it typically
examines the headers and/or client certificate.

Authentication modules include client certificates, password, and plain tokens,
bootstrap tokens, and JSON Web Tokens (used for service accounts).

Multiple authentication modules can be specified, in which case each one is tried in sequence,
until one of them succeeds.

If the request cannot be authenticated, it is rejected with HTTP status code 401.
Otherwise, the user is authenticated as a specific `username`, and the user name
is available to subsequent steps to use in their decisions.  Some authenticators
also provide the group memberships of the user, while other authenticators
do not.

While Kubernetes uses usernames for access control decisions and in request logging,
it does not have a `User` object nor does it store usernames or other information about
users in its API.
