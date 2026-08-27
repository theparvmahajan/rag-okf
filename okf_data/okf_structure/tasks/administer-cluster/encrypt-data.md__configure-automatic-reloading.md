---
id: okf-structure/tasks/administer-cluster/encrypt-data.md#configure-automatic-reloading
kind: section
title: Configure automatic reloading
source: tasks/administer-cluster/encrypt-data.md
url: https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/
heading: Configure automatic reloading
parent: okf-structure/tasks/administer-cluster/encrypt-data
children: []
prev_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#decrypt-all-data-decrypting-all-data
next_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#whatsnext
word_count: 99
---

You can configure automatic reloading of encryption provider configuration.
That setting determines whether the
API server should
load the file you specify for `--encryption-provider-config` only once at
startup, or automatically whenever you change that file. Enabling this option
allows you to change the keys for encryption at rest without restarting the
API server.

To allow automatic reloading, configure the API server to run with:
`--encryption-provider-config-automatic-reload=true`.
When enabled, file changes are polled every minute to observe the modifications.
The `apiserver_encryption_config_controller_automatic_reload_last_timestamp_seconds`
metric identifies when the new config becomes effective. This allows
encryption keys to be rotated without restarting the API server.
