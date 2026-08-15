# Vercel guide

Use this guide only when Vercel owns the public edge.

Recheck the linked project, current plan, and current documentation before changing rules.

## Plan gate

Vercel documents its WAF and automatic DDoS mitigation as available on all plans.

Fixed-window rate limiting is available on all plans.

Token-bucket rate limiting requires Enterprise.

Rule counts and charges vary by plan, so inspect the live pricing dialog before publishing.

Sources:

- [Vercel Firewall](https://vercel.com/docs/vercel-firewall)
- [WAF rate limiting](https://vercel.com/docs/vercel-firewall/vercel-waf/rate-limiting)
- [DDoS mitigation](https://vercel.com/docs/vercel-firewall/ddos-mitigation)

## Native setup

Keep Vercel's automatic DDoS mitigation in place.

Open the project in the Vercel dashboard.

Go to **Firewall**, select **Configure**, and create the smallest rule that protects the observed route or behavior.

Choose **Rate Limit** only after defining a narrow condition.

Start in log mode when possible.

Review matches and the pricing dialog before selecting **Publish**.

Use Attack Challenge Mode only as a short incident control with a rollback owner.

Do not put Cloudflare or another reverse proxy in front of Vercel.

Vercel states that this hides traffic signals and can weaken its WAF, bot, and DDoS protection.

Source: [Using Cloudflare with Vercel](https://vercel.com/kb/guide/cloudflare-with-vercel).

## Application-aware limits

Use application code only when the provider rule cannot see the identity or business signal needed for a safe limit.

Create the matching WAF rate-limit instrument and ID in the dashboard first.

Then call `checkRateLimit` from `@vercel/firewall` with that real ID and the request.

Return `429` only when the result reports the request as rate limited.

Do not invent the ID or install `@vercel/firewall` without authorization.

Source: [Add rate limiting to a Vercel project](https://vercel.com/kb/guide/add-rate-limiting-vercel).

## Verification

Send harmless requests below, at, and above the limit through the deployed hostname.

Confirm the rule match in the Firewall view and record the actual response headers.

Exercise login, checkout, webhooks, health checks, and static assets.

Confirm no alternate origin or hostname bypasses Vercel.

## Rollback

Change the custom rule back to log mode or disable it, then publish the change.

Repeat the affected customer flow and save the rollback evidence.
