# Harden Web App

`harden-web-app` helps an AI audit and protect a public web application from abusive traffic.

It covers a provider WAF, adaptive rate limiting, a DDoS response plan, and real verification.

## Install

Copy `skills/harden-web-app` into the `skills` folder used by your AI coding tool.

The folder follows the shared `SKILL.md` format used by Codex and Claude Code.

## Use

Ask:

```text
Use $harden-web-app to protect this web app from abusive traffic and DDoS attacks.
```

The skill inspects the real project and provider before changing anything.

It never claims that a WAF alone makes an app DDoS-proof.

## Source

The method was derived from a public Reel by Matt Murphy.

See [SOURCE.md](SOURCE.md) for the source link, transcript, and attribution.

## License

Apache-2.0.
