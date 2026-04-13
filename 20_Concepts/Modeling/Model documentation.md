---
type: concept
title: "Model documentation"
aliases: []
tags: ["modeling", "best-practices", "audit"]
difficulty: beginner
prerequisites: ["[[Three-statement model]]", "[[Model checks and balances]]"]
related: []
sources: ["[[Gridlines - Model Risk Management in Project Finance (5 Success Tips)]]", "[[Sumproduct - Claude Excel Add-in - A Review]]", "[[Forvis Mazars - AI in Project Finance Modelling]]"]
status: stub
updated: 2026-04-13
---

# Model documentation

> **TL;DR.** Model documentation is the process of recording the assumptions, structure, logic, and limitations of a financial model so that reviewers, users, and auditors can understand, trust, and maintain it.

## When you'd use this
Whenever you hand off a financial model to another team, submit it for formal model audit by lenders or investors, or rely on it for critical business decisions over an extended period. Documentation is especially important in high-stakes project finance deals, when external auditors review the model, or when using AI tools that generate complex calculations.

## The 30-second version
A well-built financial model is not just a calculation tool; it is a communication tool. Model documentation ensures transparency by detailing what the model does, how it works, and what data it relies on. Effective documentation includes an organized inputs sheet, clear model descriptions, logic summaries, and explicit notes on assumptions. This helps mitigate model risk—the danger that flaws in the model lead to bad financial decisions.

## The full explanation
Model documentation acts as the "user manual" and "developer log" for a financial model. As models scale to support billion-dollar infrastructure deals or multi-faceted corporate scenarios, their complexity increases. Without documentation, a model becomes a "black box" where even minor assumption mismatches or structural flaws can cause multi-million dollar mistakes.

### Types of Documentation
1. **In-model documentation:** This includes clearly separated input sheets, control accounts, color-coded cells, and dashboard notes or integrity checks built directly into the spreadsheet.
2. **External documentation:** This includes assumption logs, model logic descriptions, and risk/mitigant tables explaining the scenarios being tested.

### Managing Model Risk
Model risk arises from incorrect assumptions, implementation errors, or misinterpretation of the model's purpose. Documentation directly combats implementation and interpretation risks. As highlighted in model audits, transparently tracking the rationale behind traffic growth forecasts or debt tranches is critical for debt restructuring or bid submissions.

### The Role of AI in Documentation
Recent AI advancements (such as Claude for Excel) show promise in rapidly drafting model logic, identifying missing elements (like a tax payable account), and generating descriptive notes for dashboards. AI tools can also extract assumptions from transaction documents into structured input sheets, or convert complex formulas into plain English to support model reviews. However, AI outputs require rigorous human oversight to correct blindspots or volatile functions.

## Gaps
- More extensive source material is needed to expand on specific documentation frameworks like FAST modeling standard or internal bank protocols.
- We need deeper insights on the exact process of writing model manuals for handovers.

## Formula
(none)

## Worked example
(none)

## Excel and modeling notes
When building a model, dedicate a specific worksheet (often an "Inputs" or "Dashboard" tab) to list the model's purpose, key assumptions, version history, and integrity checks. If using AI tools to assist with model building or documentation, remember that AI often misunderstands context; you must still verify the logic (for instance, ensuring a "Deferred Revenue" account is properly placed and linked) and review the AI-generated documentation for accuracy.

## Interview-ready answer
Model documentation is the practice of clearly detailing a financial model's assumptions, logic, structure, and integrity checks. It's essential for mitigating model risk, facilitating model audits, and ensuring that all stakeholders—from internal users to external lenders—can interpret and rely on the model's outputs confidently.

## Pitfalls and gotchas
- **Treating it as an afterthought:** Failing to document assumptions as you build leads to "black box" models that are impossible to audit or hand over.
- **Over-reliance on AI:** Trusting AI tools to automatically document complex formulas without verifying that the AI correctly understood the business logic or standard practices.
- **Lack of version control:** Not recording changes and the reasons for updates, which causes confusion when multiple scenarios or audits are run.

## Sources
- [[Gridlines - Model Risk Management in Project Finance (5 Success Tips)]]
- [[Sumproduct - Claude Excel Add-in - A Review]]
- [[Forvis Mazars - AI in Project Finance Modelling]]
