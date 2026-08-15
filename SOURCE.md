# Source

- Platform: Instagram
- Creator: Matt Murphy
- Title: Video by mattmurphyai
- Source: https://www.instagram.com/reel/DbjN2IVCeEm/?igsh=MXA5OXJ3M2ZyZXlxeg==
- Fetched: 2026-08-15
- Transcript language: English
- Transcript quality: real speech, 343 words, language probability `0.999`, average log probability `-0.101`

## Caption

One kid with a laptop can take your entire product offline right now.

Not a nation-state hacker.

A teenager with a YouTube tutorial and a loop that sends 10,000 requests per second.

Your app goes dark.
Every customer.
Every transaction.
Gone.
Because your AI never built a firewall.

Direct your AI to fix that today.

-MM

`#vibecoding #aidirectedengineering #ddos #waf #production`

## Transcript

Do you know that one kid with a laptop can take your entire product offline right now? Not a nation state hacker and not a sophisticated criminal organization, but a teenager who watched a YouTube tutorial and wrote a loop that sends 10,000 requests per second to your API. Your app goes down, every customer is dark, every page, every transaction, gone. Because your AI never built a proper firewall. So here's what you direct your AI to set up before someone decides to test you. Step one, a web application firewall that sits in front of your entire stack. Not rate limiting on individual endpoints, but a WAF that filters malicious traffic patterns before they ever reach your server. Your AI deployed your app directly to the internet with nothing between the user and your infrastructure. And unfortunately, that's the equivalent of opening a store with no front door and no security camera. You don't want that. So direct your AI to configure a WAF through your hosting provider or a service like Cloudflare. Takes an afternoon, you'll nail it. Without it, your uptime depends entirely whether anyone has decided to hack you today. Step two, adaptive rate limiting that recognizes attack patterns. Basic rate limiting caps requests per user per minute. Sure, not bad, but adaptive limiting detects when request volume frequency and origin patterns shift to attack behavior. And then it throttles it automatically. So direct your AI to implement IP-based anomaly detection that escalates from throttle to temporary ban based on behavior, not just volume. That's a win. Step three, a DDoS response plan documented before the attack starts. When your app goes down under a flood of traffic, you need a predefined playbook. Who gets notified? What gets toggled? Where traffic gets redirected? So direct your AI to build a plan right now. Not during the outage when you are panicking and your customers are leaving because the front door is wide open. You need to direct your AI to put a wall in front of it today.

## Attribution

The transcript is stored only as source provenance.

The reusable skill restates the method and adds implementation guardrails, verification, and rollback steps.
