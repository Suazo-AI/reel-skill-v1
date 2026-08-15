# Cloudflare guide

Use this guide only when Cloudflare owns the public edge.

This includes Cloudflare Pages, Workers, or a proxied origin behind Cloudflare.

Do not use Cloudflare in front of Vercel as a security shortcut.

Recheck the zone, current plan, and current documentation before changing rules.

## Plan gate

Cloudflare documents automatic, unmetered DDoS protection for layers 3, 4, and 7 on all plans.

WAF features exist on all plans, but managed rules, custom rules, rate-limit capacity, and analytics vary by plan.

Free zones receive the Free Managed Ruleset and a small rule allowance.

Sources:

- [Cloudflare WAF](https://developers.cloudflare.com/waf/)
- [DDoS protection](https://developers.cloudflare.com/ddos-protection/)
- [WAF getting started](https://developers.cloudflare.com/waf/get-started/)

## Native setup

Confirm the public DNS record is proxied and the request reaches Cloudflare.

Start with the managed rulesets available on the live plan.

Add the smallest custom rule needed for an observed gap.

Create a rate-limit rule from **Security**, **WAF**, and **Rate limiting rules**.

On the newer dashboard, use **Security rules** and create a rate-limiting rule.

Define the match, counting characteristics, threshold, period, action, and mitigation duration from real traffic evidence.

Save as draft or use a non-blocking action first when the live product supports it.

Then deploy and watch Security Events or Security Analytics.

Source: [Create a rate limiting rule in the dashboard](https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/).

Do not use the deprecated Firewall Rules API or the deprecated Terraform resources `cloudflare_firewall_rule` and `cloudflare_filter`.

Use WAF custom rules through the Rulesets API or current Terraform resources.

Source: [Upgrade legacy Firewall Rules](https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/).

Restrict the origin so it accepts traffic only from Cloudflare through an approved control such as Cloudflare IP allowlisting, Tunnel, or Authenticated Origin Pulls.

Treat DNS and origin-firewall changes as external mutations that need authorization and a tested rollback.

## Verification

Send harmless requests below, at, and above the limit through the public hostname.

Confirm the event, action, rule ID, and actual response headers in Security Events or Security Analytics.

Test direct origin access and confirm it is blocked without breaking health checks or provider callbacks.

Exercise login, checkout, webhooks, health checks, and static assets.

## Rollback

Disable the custom or rate-limit rule, or return it to a non-blocking action.

Repeat the affected customer flow and save the rollback evidence.

Restore DNS or origin-firewall state only through the approved rollback plan.
