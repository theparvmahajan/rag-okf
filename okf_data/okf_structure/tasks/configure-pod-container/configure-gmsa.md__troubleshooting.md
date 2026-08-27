---
id: okf-structure/tasks/configure-pod-container/configure-gmsa.md#troubleshooting
kind: section
title: Troubleshooting
source: tasks/configure-pod-container/configure-gmsa.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/
heading: Troubleshooting
parent: okf-structure/tasks/configure-pod-container/configure-gmsa
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#authenticating-to-network-shares-using-hostname-or-fqdn
next_sibling: null
word_count: 389
---

If you are having difficulties getting GMSA to work in your environment,
there are a few troubleshooting steps you can take.

First, make sure the credspec has been passed to the Pod. To do this you will need
to `exec` into one of your Pods and check the output of the `nltest.exe /parentdomain` command.

In the example below the Pod did not get the credspec correctly:

```PowerShell
kubectl exec -it iis-auth-7776966999-n5nzr powershell.exe
```

`nltest.exe /parentdomain` results in the following error:

```output
Getting parent domain failed: Status = 1722 0x6ba RPC_S_SERVER_UNAVAILABLE
```

If your Pod did get the credspec correctly, then next check communication with the domain.
First, from inside of your Pod, quickly do an nslookup to find the root of your domain.

This will tell us 3 things:

1. The Pod can reach the DC
1. The DC can reach the Pod
1. DNS is working correctly.

If the DNS and communication test passes, next you will need to check if the Pod has
established secure channel communication with the domain. To do this, again,
`exec` into your Pod and run the `nltest.exe /query` command.

```PowerShell
nltest.exe /query
```

Results in the following output:

```output
I_NetLogonControl failed: Status = 1722 0x6ba RPC_S_SERVER_UNAVAILABLE
```

This tells us that for some reason, the Pod was unable to logon to the domain using
the account specified in the credspec. You can try to repair the secure channel by running the following:

```PowerShell
nltest /sc_reset:domain.example
```

If the command is successful you will see and output similar to this:

```output
Flags: 30 HAS_IP  HAS_TIMESERV
Trusted DC Name \\dc10.domain.example
Trusted DC Connection Status Status = 0 0x0 NERR_Success
The command completed successfully
```

If the above corrects the error, you can automate the step by adding the following
lifecycle hook to your Pod spec.  If it did not correct the error, you will need to
examine your credspec again and confirm that it is correct and complete.

```yaml
        image: registry.domain.example/iis-auth:1809v1
        lifecycle:
          postStart:
            exec:
              command: ["powershell.exe","-command","do { Restart-Service -Name netlogon } while ( $($Result = (nltest.exe /query); if ($Result -like '*0x0 NERR_Success*') {return $true} else {return $false}) -eq $false)"]
        imagePullPolicy: IfNotPresent
```

If you add the `lifecycle` section show above to your Pod spec, the Pod will execute
the commands listed to restart the `netlogon` service until the `nltest.exe /query` command exits without error.
