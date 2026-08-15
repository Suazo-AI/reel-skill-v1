# Netlify guide

Use this guide only when Netlify owns the public edge.

Recheck the linked project, current plan, and current documentation before changing rules.

## Plan gate

Netlify documents basic rate limiting as available on all plans.

Full rate-limiting features and the managed WAF require Enterprise with High-Performance Edge.

Netlify includes automatic DDoS detection and mitigation in its network security controls.

Sources:

- [Rate limiting](https://docs.netlify.com/manage/security/secure-access-to-sites/rate-limiting/)
- [Web Application Firewall](https://docs.netlify.com/manage/security/secure-access-to-sites/web-application-firewall/)
- [Security overview](https://docs.netlify.com/security/overview/)

## Choose the correct control

Use **Project configuration**, **Access & security**, and **Rate limiting** for dashboard-managed rules.

Define a Function or Edge Function limit in that function's exported `config` object:

```ts
export const config = {
  path: "/",
  rateLimit: {
    windowLimit: 100,
    windowSize: 60,
    aggregateBy: ["ip", "domain"],
  },
};
```

Treat those numbers as syntax examples, not recommended production limits.

Do not define a Function limit in `netlify.toml`.

Define a redirect proxy or whole-site limit in `netlify.toml`, not `_redirects`:

```toml
[[redirects]]
  from = "/search"
  to = "https://api.example.com"
  status = 200
  force = true
    [redirects.rate_limit]
    window_limit = 50
    window_size = 60
    aggregate_by = ["ip", "domain"]
```

Replace the example route, upstream, and limits with values supported by real traffic evidence.

Use `domain` alone as an aggregation key only when the live plan supports that Enterprise feature.

## Verification

Deploy to a preview or staging site first.

Read the deploy post-processing log after every configuration change.

Netlify warns that an invalid rate-limit rule may not fail the deploy or show a clear error.

Send harmless requests below, at, and above the limit through the Netlify hostname.

Confirm the matched rule and response in logs, then exercise critical customer flows.

## Rollback

Remove or disable the dashboard rule, or revert the function or `netlify.toml` change.

Redeploy, read the post-processing log, and repeat the affected customer flow.
