---
id: okf-structure/concepts/architecture/mixed-version-proxy.md#enabling-peer-aggregated-discovery-and-mixed-version-proxy
kind: section
title: Enabling Peer-aggregated Discovery and Mixed Version Proxy
source: concepts/architecture/mixed-version-proxy.md
url: https://kubernetes.io/docs/concepts/architecture/mixed-version-proxy/
heading: Enabling Peer-aggregated Discovery and Mixed Version Proxy
parent: okf-structure/concepts/architecture/mixed-version-proxy
children: []
prev_sibling: okf-structure/concepts/architecture/mixed-version-proxy.md#introduction
next_sibling: okf-structure/concepts/architecture/mixed-version-proxy.md#peer-aggregated-discovery
word_count: 264
---

Ensure that `UnknownVersionInteroperabilityProxy` feature gate
is enabled when you start the API Server:

```shell
kube-apiserver \
--feature-gates=UnknownVersionInteroperabilityProxy=true \
# required command line arguments for this feature
--peer-ca-file=<path to kube-apiserver CA cert>
--proxy-client-cert-file=<path to aggregator proxy cert>,
--proxy-client-key-file=<path to aggregator proxy key>,
--requestheader-client-ca-file=<path to aggregator CA cert>,
# requestheader-allowed-names can be set to blank to allow any Common Name
--requestheader-allowed-names=<valid Common Names to verify proxy client cert against>,

# optional flags for this feature
--peer-advertise-ip=`IP of this kube-apiserver that should be used by peers to proxy requests`
--peer-advertise-port=`port of this kube-apiserver that should be used by peers to proxy requests`

# …and other flags as usual
```

### Proxy transport and authentication between API servers {#transport-and-authn}

* The source kube-apiserver reuses the
  existing APIserver client authentication flags
  `--proxy-client-cert-file` and `--proxy-client-key-file` to present its identity that
  will be verified by its peer (the destination kube-apiserver). The destination API server
  verifies that peer connection based on the configuration you specify using the
  `--requestheader-client-ca-file` command line argument.

* To authenticate the destination server's serving certs, you must configure a certificate
  authority bundle by specifying the `--peer-ca-file` command line argument to the **source** API server.

### Configuration for peer API server connectivity

To set the network location of a kube-apiserver that peers will use to proxy requests, use the
`--peer-advertise-ip` and `--peer-advertise-port` command line arguments to kube-apiserver or specify
these fields in the API server configuration file.
If these flags are unspecified, peers will use the value from either `--advertise-address` or
`--bind-address` command line argument to the kube-apiserver.
If those too, are unset, the host's default interface is used.
