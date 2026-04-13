---
type: concept
title: "Model audit"
aliases: ["Financial model audit", "Model review"]
tags: ["modeling", "audit", "best-practices", "due-diligence"]
difficulty: intermediate
prerequisites: ["[[FAST modeling standard]]", "[[Model checks and balances]]"]
related: ["[[Color coding conventions]]", "[[Model documentation]]"]
sources: ["[[CFI - Model Audit - Overview, Scope and Purpose, Categories]]", "[[Forvis Mazars - Financial Model Audit]]", "[[Gridlines - What is a model audit- - Gridlines]]", "[[Finexmod - How to make your financial models easier to audit- – Finexmod]]", "[[Sumproduct - Financial Model Auditing]]", "[[Project Finance - Model Audits]]"]
status: draft
updated: 2026-04-13
---

# Model audit

> **TL;DR.** A model audit is an independent review of a financial model to minimize the risk of error by validating its arithmetic accuracy, logical consistency, and alignment with documentation.

## When you'd use this

Model audits are predominantly used in large transactions, such as project finance or M&A, where funding decisions are based on the outputs of a financial model. Lenders and investors require assurance that the model functions correctly before committing capital, meaning an audit is a formal prerequisite to reach financial close. Additionally, companies use lighter model reviews internally for quality assurance and to support management decisions.

## The 30-second version

A financial model audit ensures that a spreadsheet is free from material errors, mathematically sound, and logically consistent. Model auditors perform tasks ranging from cell-by-cell formula checks to verifying that model inputs match project agreements and ensuring that sensitivity runs operate correctly. In formal funder due diligence, auditors provide a signed letter backed by liability cover assuring lenders that the model is correct. Lighter reviews exist for clients merely wanting a second pair of eyes without formal sign-off.

## The full explanation

### Purpose and Scope
The primary goal of a model audit is to ensure the model does what it is expected to do, preventing expensive errors or lawsuits resulting from flawed decision-making. The scope of an audit typically includes:
- **Arithmetic Accuracy and Integrity:** Checking that calculations function correctly and logically, often using specialized software to find embedded constants, hidden cells, or inconsistent calculations.
- **Documentation and Inputs:** Ensuring the model inputs correctly reflect project agreements, reports, and term sheets.
- **Tax and Accounting:** Verifying that the model handles tax and accounting legislation correctly.
- **Sensitivities:** Running scenarios to ensure that changes in inputs produce expected, accurate results.

### Categories of Audits
Audits generally fall into two categories:
1. **High-Level Review (Model Review):** A lighter touch exercise focused on the "big picture." It points out logic issues or potential problems without formally verifying every single cell, making it quicker and less expensive. It does not typically come with formal sign-off.
2. **Formal Model Audit (Funder Due Diligence):** A rigorous, comprehensive, cell-by-cell check required by senior lenders. It culminates in an assurance opinion backed by liability cover.

### Auditing Approaches
When assessing accuracy, auditors generally use two main approaches:
- **Cell by Cell:** A manual process where the auditor reviews every unique formula. This approach is highly flexible and suited for novel, bespoke models.
- **Shadow Build:** The auditor recreates the logic of the model under test using template models and reconciles the outputs. This approach provides confidence that the overall output is materially correct, even if minor formula differences exist.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

To make a model easier to audit, you should adhere to strict modeling standards: keep inputs separate from calculations, apply consistent color coding (e.g., blue for hardcoded inputs, black for calculations), use simple and consistent formulas across rows, avoid hard-coding numbers within formulas, eliminate circular references, and include clear guide and reference sheets that map inputs back to their source documents.

## Interview-ready answer

A financial model audit is an independent review that verifies the mechanical accuracy, logical integrity, and document consistency of a model. It provides lenders and investors the necessary assurance to rely on the model's outputs when making major capital commitments.

## Pitfalls and gotchas

- **Inconsistent formatting and long formulas:** Ignoring best practices by using complex, nested formulas or inconsistent color coding makes auditing significantly more time-consuming and expensive.
- **Focusing on proofreading over logic:** A common criticism is when auditors focus on tabulating minor cosmetic issues rather than identifying material logical or structural errors that actually impact the business outcome.
- **Inconsistent sign conventions:** Using positive and negative numbers inconsistently (e.g., for expenses) makes auditing exceptionally difficult and can lead to major miscalculations.

## Sources

- [[CFI - Model Audit - Overview, Scope and Purpose, Categories]]
- [[Forvis Mazars - Financial Model Audit]]
- [[Gridlines - What is a model audit- - Gridlines]]
- [[Finexmod - How to make your financial models easier to audit- – Finexmod]]
- [[Sumproduct - Financial Model Auditing]]
- [[Project Finance - Model Audits]]
