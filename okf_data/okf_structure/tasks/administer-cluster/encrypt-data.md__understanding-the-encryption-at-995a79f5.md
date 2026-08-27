---
id: okf-structure/tasks/administer-cluster/encrypt-data.md#understanding-the-encryption-at-rest-configuration
kind: section
title: Understanding the encryption at rest configuration
source: tasks/administer-cluster/encrypt-data.md
url: https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/
heading: Understanding the encryption at rest configuration
parent: okf-structure/tasks/administer-cluster/encrypt-data
children: []
prev_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#determine-whether-encryption-at-rest-is-already-enabled-determining-whether-encryption-at-rest-is-already-enabled
next_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#encrypt-your-data-encrypting-your-data
word_count: 1442
---

---
#
# CAUTION: this is an example configuration.
#          Do not use this for your own cluster!
#
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
      - configmaps
      - pandas.awesome.bears.example # a custom resource API
    providers:
      # This configuration does not provide data confidentiality. The first
      # configured provider is specifying the "identity" mechanism, which
      # stores resources as plain text.
      #
      - identity: {} # plain text, in other words NO encryption
      - aesgcm:
          keys:
            - name: key1
              secret: c2VjcmV0IGlzIHNlY3VyZQ==
            - name: key2
              secret: dGhpcyBpcyBwYXNzd29yZA==
      - aescbc:
          keys:
            - name: key1
              secret: c2VjcmV0IGlzIHNlY3VyZQ==
            - name: key2
              secret: dGhpcyBpcyBwYXNzd29yZA==
      - secretbox:
          keys:
            - name: key1
              secret: YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXoxMjM0NTY=
  - resources:
      - events
    providers:
      - identity: {} # do not encrypt Events even though *.* is specified below
  - resources:
      - '*.apps' # wildcard match requires Kubernetes 1.27 or later
    providers:
      - aescbc:
          keys:
          - name: key2
            secret: c2VjcmV0IGlzIHNlY3VyZSwgb3IgaXMgaXQ/Cg==
  - resources:
      - '*.*' # wildcard match requires Kubernetes 1.27 or later
    providers:
      - aescbc:
          keys:
          - name: key3
            secret: c2VjcmV0IGlzIHNlY3VyZSwgSSB0aGluaw==

Each `resources` array item is a separate config and contains a complete configuration. The
`resources.resources` field is an array of Kubernetes resource names (`resource` or `resource.group`)
that should be encrypted like Secrets, ConfigMaps, or other resources.

If custom resources are added to `EncryptionConfiguration` and the cluster version is 1.26 or newer,
any newly created custom resources mentioned in the `EncryptionConfiguration` will be encrypted.
Any custom resources that existed in etcd prior to that version and configuration will be unencrypted
until they are next written to storage. This is the same behavior as built-in resources.
See the Ensure all secrets are encrypted section.

The `providers` array is an ordered list of the possible encryption providers to use for the APIs that you listed.
Each provider supports multiple keys - the keys are tried in order for decryption, and if the provider
is the first provider, the first key is used for encryption.

Only one provider type may be specified per entry (`identity` or `aescbc` may be provided,
but not both in the same item).
The first provider in the list is used to encrypt resources written into the storage. When reading
resources from storage, each provider that matches the stored data attempts in order to decrypt the
data. If no provider can read the stored data due to a mismatch in format or secret key, an error
is returned which prevents clients from accessing that resource.

`EncryptionConfiguration` supports the use of wildcards to specify the resources that should be encrypted.
Use '`*.<group>`' to encrypt all resources within a group (for eg '`*.apps`' in above example) or '`*.*`'
to encrypt all resources. '`*.`' can be used to encrypt all resource in the core group. '`*.*`' will
encrypt all resources, even custom resources that are added after API server start.

 Use of wildcards that overlap within the same resource list or across multiple entries are not allowed
since part of the configuration would be ineffective. The `resources` list's processing order and precedence
are determined by the order it's listed in the configuration. 

If you have a wildcard covering resources and want to opt out of at-rest encryption for a particular kind
of resource, you achieve that by adding a separate `resources` array item with the name of the resource that
you want to exempt, followed by a `providers` array item where you specify the `identity` provider. You add
this item to the list so that it appears earlier than the configuration where you do specify encryption
(a provider that is not `identity`).

For example, if '`*.*`' is enabled and you want to opt out of encryption for Events and ConfigMaps, add a
new **earlier** item to the `resources`, followed by the providers array item with `identity` as the
provider. The more specific entry must come before the wildcard entry.

The new item would look similar to:

```yaml
  ...
  - resources:
      - configmaps. # specifically from the core API group,
                    # because of trailing "."
      - events
    providers:
      - identity: {}
  # and then other entries in resources
```

Ensure that the exemption is listed _before_ the wildcard '`*.*`' item in the resources array
to give it precedence.

For more detailed information about the `EncryptionConfiguration` struct, please refer to the
encryption configuration API.

If any resource is not readable via the encryption configuration (because keys were changed),
and you cannot restore a working configuration, your only recourse is to delete that entry from
the underlying etcd directly.

Any calls to the Kubernetes API that attempt to read that resource will fail until it is deleted
or a valid decryption key is provided.

### Available providers {#providers}

Before you configure encryption-at-rest for data in your cluster's Kubernetes API, you
need to select which provider(s) you will use.

The following table describes each available provider.

<caption style="display: none;">Providers for Kubernetes encryption at rest</caption>

  
  Name
  Encryption
  Strength
  Speed
  Key length
  

  
  
  <tt>identity</tt>
  None
  N/A
  N/A
  N/A
  
  
  Resources written as-is without encryption. When set as the first provider, the resource will be decrypted as new values are written. Existing encrypted resources are not automatically overwritten with the plaintext data.
   The <tt>identity</tt> provider is the default if you do not specify otherwise.
  

  
  <tt>aescbc</tt>
  AES-CBC with PKCS#7 padding
  Weak
  Fast
  16, 24, or 32-byte
  
  
  Not recommended due to CBC's vulnerability to padding oracle attacks. Key material accessible from control plane host.
  
  
  <tt>aesgcm</tt>
  AES-GCM with random nonce
  Must be rotated every 200,000 writes
  Fastest
  16, 24, or 32-byte
  
  
  Not recommended for use except when an automated key rotation scheme is implemented. Key material accessible from control plane host.
  
  
  <tt>kms</tt> v1 (deprecated since Kubernetes v1.28)
  Uses envelope encryption scheme with DEK per resource.
  Strongest
  Slow (compared to <tt>kms</tt> version 2)
  32-bytes
  
  
  
    Data is encrypted by data encryption keys (DEKs) using AES-GCM;
    DEKs are encrypted by key encryption keys (KEKs) according to
    configuration in Key Management Service (KMS).
    Simple key rotation, with a new DEK generated for each encryption, and
    KEK rotation controlled by the user.
    
    Read how to configure the KMS V1 provider.
    
  
  
  <tt>kms</tt> v2 
  Uses envelope encryption scheme with DEK per API server.
  Strongest
  Fast
  32-bytes
  
  
  
    Data is encrypted by data encryption keys (DEKs) using AES-GCM; DEKs
    are encrypted by key encryption keys (KEKs) according to configuration
    in Key Management Service (KMS).
    Kubernetes generates a new DEK per encryption from a secret seed.
    The seed is rotated whenever the KEK is rotated.
    A good choice if using a third party tool for key management.
    Available as stable from Kubernetes v1.29.
    
    Read how to configure the KMS V2 provider.
    
  
  
  <tt>secretbox</tt>
  XSalsa20 and Poly1305
  Strong
  Faster
  32-byte
  
  
  Uses relatively new encryption technologies that may not be considered acceptable in environments that require high levels of review. Key material accessible from control plane host.
  

The `identity` provider is the default if you do not specify otherwise. **The `identity` provider does not
encrypt stored data and provides _no_ additional confidentiality protection.**

### Key storage

#### Local key storage

Encrypting secret data with a locally managed key protects against an etcd compromise, but it fails to
protect against a host compromise. Since the encryption keys are stored on the host in the
EncryptionConfiguration YAML file, a skilled attacker can access that file and extract the encryption
keys.

#### Managed (KMS) key storage {#kms-key-storage}

The KMS provider uses _envelope encryption_: Kubernetes encrypts resources using a data key, and then
encrypts that data key using the managed encryption service. Kubernetes generates a unique data key for
each resource. The API server stores an encrypted version of the data key in etcd alongside the ciphertext;
when reading the resource, the API server calls the managed encryption service and provides both the
ciphertext and the (encrypted) data key.
Within the managed encryption service, the provider use a _key encryption key_ to decipher the data key,
deciphers the data key, and finally recovers the plain text. Communication between the control plane
and the KMS requires in-transit protection, such as TLS.

Using envelope encryption creates dependence on the key encryption key, which is not stored in Kubernetes.
In the KMS case, an attacker who intends to get unauthorised access to the plaintext
values would need to compromise etcd **and** the third-party KMS provider.

### Protection for encryption keys

You should take appropriate measures to protect the confidential information that allows decryption,
whether that is a local encryption key, or an authentication token that allows the API server to
call KMS.

Even when you rely on a provider to manage the use and lifecycle of the main encryption key (or keys), you are still responsible
for making sure that access controls and other security measures for the managed encryption service are
appropriate for your security needs.
