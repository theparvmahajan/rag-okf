---
id: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#choose-an-admission-control-mechanism-choose-admission-mechanism
kind: section
title: Choose an admission control mechanism {#choose-admission-mechanism}
source: concepts/cluster-administration/admission-webhooks-good-practices.md
url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
heading: Choose an admission control mechanism {#choose-admission-mechanism}
parent: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices
children: []
prev_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#identify-whether-you-use-admission-webhooks-identify-admission-webhooks
next_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#performance-and-latency-performance-latency
word_count: 288
---

Kubernetes includes multiple admission control and policy enforcement options.
Knowing when to use a specific option can help you to improve latency and
performance, reduce management overhead, and avoid issues during version
upgrades. The following table describes the mechanisms that let you mutate or
validate resources during admission:

  <caption>Mutating and validating admission control in Kubernetes</caption>
  
    
      Mechanism
      Description
      Use cases
    
  
  
    
      Mutating admission webhook
      Intercept API requests before admission and modify as needed using
        custom logic.
      
        Make critical modifications that must happen before resource
          admission.
        Make complex modifications that require advanced logic, like calling
          external APIs.
      
    
    
      Mutating admission policy
      Intercept API requests before admission and modify as needed using
        Common Expression Language (CEL) expressions.
      
        Make critical modifications that must happen before resource
          admission.
        Make simple modifications, such as adjusting labels or replica
        counts.
      
    
    
      Validating admission webhook
      Intercept API requests before admission and validate against complex
        policy declarations.
      
        Validate critical configurations before resource admission.
        Enforce complex policy logic before admission.
      
    
    
      Validating admission policy
      Intercept API requests before admission and validate against CEL
        expressions.
      
        Validate critical configurations before resource admission.
        Enforce policy logic using CEL expressions.
      
    
  

In general, use _webhook_ admission control when you want an extensible way to
declare or configure the logic. Use built-in CEL-based admission control when
you want to declare simpler logic without the overhead of running a webhook
server. The Kubernetes project recommends that you use CEL-based admission
control when possible.

### Use built-in validation and defaulting for CustomResourceDefinitions {#no-crd-validation-defaulting}

If you use
CustomResourceDefinitions,
don't use admission webhooks to validate values in CustomResource specifications
or to set default values for fields. Kubernetes lets you define validation rules
and default field values when you create CustomResourceDefinitions.

To learn more, see the following resources:

* Validation rules
* Defaulting
