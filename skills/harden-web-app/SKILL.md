---
name: harden-web-app
description: Audits and hardens public web applications against abusive traffic and DDoS attacks with a provider WAF, adaptive rate limiting, and an incident response plan. Use when a user asks to secure a public app, add a WAF or rate limits, prepare for DDoS, or review production edge protection.
---

# Harden Web App

Reduce traffic-attack risk with three layers: an edge firewall, adaptive limits, and a response plan.

Never promise that any control makes a system DDoS-proof.

## Guardrails

- Inspect the repository, provider, routing, and live configuration before proposing a change.
- Capture real schemas, command help, or API responses before writing provider configuration.
- Never invent field names, plan features, thresholds, traffic baselines, account IDs, or contact details.
- Keep secrets in the provider's normal authentication flow.
- Treat DNS, firewall, deployment, and account changes as external mutations that need clear user authorization.
- Test with staging or a small approved load.
- Never launch an uncontrolled load test against production.

## 1. Map the traffic path

Identify the public hostname, CDN or reverse proxy, load balancer, origin, and every public API entry point.

Find existing WAF rules, rate limits, logs, alerts, health checks, webhooks, authentication routes, and expensive endpoints.

Check for an origin address or alternate hostname that can bypass the edge.

Record the normal request rate and legitimate peak when evidence exists.

If no baseline exists, use conservative starting values and label them as assumptions.

## 2. Put a WAF before the full stack

Prefer the hosting provider or CDN's managed WAF when it covers every public hostname.

Enable managed rules in log, preview, or count mode first when the provider supports it.

Review matches before blocking so normal customers, health checks, and trusted integrations keep working.

Restrict direct access to the origin so attackers cannot skip the WAF.

Add the smallest custom rules needed for observed malicious patterns.

Keep a tested rollback for every blocking rule.

## 3. Add adaptive rate limiting

Layer limits instead of relying on one global number.

- Add a broad emergency ceiling for the whole service.
- Add route-specific limits for login, search, uploads, checkout, and expensive API work.
- Use authenticated identity or API key when available.
- Combine identity with IP and behavior signals instead of trusting IP alone.
- Trust forwarded client-IP headers only from known proxies.
- Use a shared counter store when several app instances serve the same route.

Escalate responses in stages: observe, throttle, return `429` with `Retry-After`, then apply a short temporary block.

Base escalation on request rate, burst shape, repeated failures, route cost, and origin changes.

Define how limits fail when the counter store or provider is unavailable.

Choose fail-open or fail-closed per route based on customer impact and security risk.

## 4. Write the DDoS response plan

Create `docs/ddos-response.md` in the target project unless its documentation uses another clear location.

Include these facts:

- Detection signals and alert thresholds.
- The person or team that owns the response.
- The exact dashboard, logs, and provider controls to open.
- The first safe mitigation and its rollback.
- The emergency rule or traffic-shaping procedure.
- Health-check and customer-impact checks.
- Internal and customer communication owners.
- Evidence to preserve for the review after the incident.

Leave unknown people, contacts, URLs, and thresholds as explicit blanks.

## 5. Verify the real path

Read [references/verification.md](references/verification.md) before testing.

Verify that the public hostname reaches the WAF and that the origin cannot be reached directly.

Exercise requests below, at, and above each limit.

Confirm the response code, `Retry-After`, logs, alerts, counter sharing, expiry, and recovery.

Recheck login, checkout, webhooks, health checks, and other critical legitimate flows.

Save command output, provider screenshots or exports, and relevant log entries as evidence.

## Deliver the result

Report these items in order:

1. The exposed traffic path and highest risk.
2. The WAF, rate-limit, and response-plan changes made.
3. Fresh verification evidence.
4. Assumptions and work still pending.
5. The rollback path.

Do not call the app protected, ready, or verified until the public path and the limits were exercised successfully.
