# Basic Agent Secured Baseline  
**Phase 1 – Foundations of Secure Agentic AI Development**

Secure-by-design research agent built with CrewAI  
Demonstrates security hygiene applied **before** writing functional logic

<br>

<p align="center">
  <img src="https://img.shields.io/badge/Phase-1%20Foundations-blue?style=for-the-badge&logo=shield&logoColor=white" alt="Phase 1">
  <img src="https://img.shields.io/badge/Security%20First-orange?style=for-the-badge" alt="Security First">
  <img src="https://img.shields.io/badge/CrewAI-0.80+-blueviolet?style=for-the-badge&logo=python" alt="CrewAI">
  <img src="https://img.shields.io/badge/OWASP%20Agentic-2026-important?style=for-the-badge" alt="OWASP Agentic">
</p>

<br>

## 🎯 Purpose of this repository

This is **not** a production research agent.

This is a **deliberately minimal, security-annotated baseline** that shows:

- how security thinking starts **before the first line of logic**
- how to apply basic agentic-specific security controls from day zero
- how easily a vanilla agent can be broken (and what small changes already help)

It serves as the **anchor artifact** of the "Agentic AI Security – Security-by-Design" 8–12 week learning path.

<br>

## 🔐 Security posture – what was added vs vanilla CrewAI

| Control                              | Vanilla CrewAI | This baseline                          | Why it matters                                      |
|:-------------------------------------|:--------------:|:---------------------------------------|:----------------------------------------------------|
| Prompts stored in Git                | ❌             | ✅ (prompts/ folder)                   | Prompts are **code** → version, review, sign       |
| Structured audit logging (JSONL)     | ❌ (only console) | ✅ full event trail (thought/tool/output) | Mandatory for forensic reconstruction              |
| Tool allow-list                      | ❌             | ✅ strict function in tools.py          | Prevents surprise tool registration                |
| Max iterations limit                 | ❌             | ✅ (8 by default)                      | Basic protection against infinite loops            |
| No delegation by default             | ❌             | ✅                                     | Reduces privilege escalation surface               |
| .env + .gitignore hygiene            | partial        | ✅ strict                              | Prevents key leaks                                 |
| Attack demonstrations documented     | —              | ✅ three concrete attacks + logs        | Proves understanding of real agentic threats       |

<br>

## 🛡️ Alignment with IBM Agentic AI Security Principles (2026)

| Principle                            | How it is addressed in this baseline                              |
|:-------------------------------------|:------------------------------------------------------------------|
| 1. Keep an eye on them               | Verbose logging + final report requires human review             |
| 2. Contain and compartmentalize      | Strict tool allow-list + no delegation + iteration limit         |
| 3. Remember the full ML lifecycle    | Prompts versioned → can be hardened / red-teamed like code       |
| 4. Secure the action layer           | Only pre-approved tools can be called → no dynamic tool discovery|

<br>

## ⚔️ Attacks performed & documented (Phase 1 lab requirement)

All attacks were run against **slightly modified versions** of the agent (removing one or more of the controls above) to demonstrate realistic failure modes.

| # | Attack name                        | OWASP ASI ref       | Success on vanilla? | Mitigated by baseline? | Folder                          |
|---|------------------------------------|---------------------|----------------------|------------------------|---------------------------------|
| 1 | Goal hijacking via prefix prompt   | ASI01               | Yes                  | Partial (role refusal) | `attacks/01_goal_hijack.md`     |
| 2 | Tool misuse – attempted code exfil | ASI02               | Yes                  | Yes (no code exec tool)| `attacks/02_tool_misuse.md`     |
| 3 | Indirect prompt injection          | ASI02 / ASI07       | Yes                  | Partial                | `attacks/03_indirect_injection.md` |

Detailed evidence (prompts used, agent responses, log excerpts) → see [`/attacks/`](./attacks) folder.

<br>

## 🏗️ Architecture

```mermaid
graph LR
    A[User Query] --> B[Researcher Agent]
    B -->|allowed only| C[Tavily Search Tool]
    C --> B
    B --> D[Reporting Analyst Agent]
    D --> E[Markdown Report]
    style B fill:#2d6a4f,stroke:#fff,stroke-width:2px
    style D fill:#2d6a4f,stroke:#fff,stroke-width:2px
