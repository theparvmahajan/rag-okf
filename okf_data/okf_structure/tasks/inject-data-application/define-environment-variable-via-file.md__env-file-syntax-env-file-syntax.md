---
id: okf-structure/tasks/inject-data-application/define-environment-variable-via-file.md#env-file-syntax-env-file-syntax
kind: section
title: Env file syntax {#env-file-syntax}
source: tasks/inject-data-application/define-environment-variable-via-file.md
url: https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-via-file/
heading: Env file syntax {#env-file-syntax}
parent: okf-structure/tasks/inject-data-application/define-environment-variable-via-file
children: []
prev_sibling: okf-structure/tasks/inject-data-application/define-environment-variable-via-file.md#how-the-design-works
next_sibling: okf-structure/tasks/inject-data-application/define-environment-variable-via-file.md#whatsnext
word_count: 225
---

The env file format used by Kubernetes is a well-defined subset of the environment variable semantics for POSIX-compliant bash. Any env file supported by Kubernetes will produce the same environment variables as when interpreted by a POSIX-compliant bash. However, POSIX-compliant bash supports some additional formats that Kubernetes does not accept.

Example:

```
MY_VAR='my-literal-value'
```

### Rules

* Variable declaration: Use the form `VAR='value'`. Spaces surrounding `=` are ignored; leading spaces on a line are ignored; blank lines are ignored.
* Quoted values: Values must be enclosed in single quotes (`'`).
  * The content inside single quotes is preserved literally. No escape-sequence processing, whitespace folding, or character interpretation is applied.
  * Newlines inside single quotes are preserved (multi-line values are supported).
* Comments: Lines that begin with `#` are treated as comments and ignored. A `#` character inside a single-quoted value is not a comment.

Examples:

```
# comment
DB_ADDRESS='address'

MULTI='line1
line2'
```

### Unsupported forms

* Unquoted values are **prohibited**:
  * `VAR=value` — not supported.
* Double-quoted values are **prohibited**:
  * `VAR="value"` — not supported.
* Multiple adjacent quoted strings are **not** supported:
  * `VAR='val1''val2'` — not supported.
* Any form of interpolation, expansion, or concatenation is **not** supported:
  * `VAR='a'$OTHER` or `VAR=${OTHER}` — not supported.

The strict single-quote requirement ensures the value is taken literally by the kubelet when loading environment variables from files.
