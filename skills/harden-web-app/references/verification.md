# Verification checklist

Use the smallest test that proves the control without harming customers.

Prefer staging with production-like routing.

Use production only with explicit approval and a tightly bounded request rate.

## WAF checks

- Resolve the public hostname and record the edge provider.
- Send one harmless request that should match a test rule.
- Confirm the rule records or blocks it as configured.
- Try the known origin address or alternate hostname.
- Confirm the origin rejects direct public traffic.
- Exercise health checks, webhooks, authentication, checkout, and static assets.
- Disable the test rule and confirm the rollback restores the prior behavior.

## Rate-limit checks

Run each case against one safe endpoint.

| Case | Expected result |
|---|---|
| Below the limit | Normal success response |
| At the limit | Documented boundary behavior |
| Above the limit | `429` and a valid `Retry-After` |
| Short burst | Burst policy works as designed |
| After expiry | Normal access returns |
| Same identity from another IP | Identity rule still applies |
| Different identity behind one IP | Legitimate users are not all blocked |
| Spoofed forwarding header | Untrusted header does not bypass the rule |
| Two app instances | Shared counter produces one combined limit |

## Alert and response checks

- Trigger a harmless alert condition.
- Confirm the alert reaches the named owner.
- Open every dashboard and command named in the response plan.
- Apply the safest mitigation in staging or preview mode.
- Run the health and customer-impact checks.
- Roll the mitigation back.
- Record how long detection, mitigation, and recovery took.

## Evidence

Save the command, timestamp, exit code, response headers, matched rule ID, log query, alert receipt, and rollback result.

Redact tokens, cookies, private addresses, customer data, and account secrets.
