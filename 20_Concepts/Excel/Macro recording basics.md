---
type: concept
title: "Macro recording basics"
aliases: ["macro recording", "VBA macro recording"]
tags: ["excel", "vba", "automation"]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[Trump Excel - How to Record a Macro in Excel - A Step by Step Guide]]", "[[Financial Modelling Handbook - How to add a VBA macro to a financial model]]"]
status: stub
updated: 2026-04-09
---

# Macro recording basics

> **TL;DR.** Macro recording is a feature in Excel that translates your clicks and keystrokes into VBA code, allowing you to automate repetitive tasks without needing to write code manually.

## When you'd use this

You would use macro recording to automate highly repetitive, identical tasks that you perform frequently, such as applying specific formatting, inserting boilerplate text, or copying and pasting data in a consistent pattern. It is also an excellent tool for learning VBA syntax, as you can record an action and review the generated code to see how Excel handles it programmatically.

## The 30-second version

A macro recorder acts like a tape recorder for your actions in Excel. Once you click "Record Macro" from the Developer tab, Excel watches everything you do (selecting cells, typing text, formatting) and writes down those steps in Visual Basic for Applications (VBA). When you stop recording, Excel saves this code as a macro. You can then run this macro anytime to have Excel repeat the exact same steps in a fraction of a second.

## The full explanation

To record a macro, you first need the **Developer tab** visible in the Excel ribbon. From there, you can click "Record Macro", give it a name (with no spaces), and optionally assign a keyboard shortcut. Once recording begins, every action is converted into VBA code and stored in a new Module within the Visual Basic Editor (accessible via `ALT + F11`).

There are two main modes for recording macros:
- **Absolute Reference:** The macro hardcodes exact cell addresses (e.g., it always goes to `A2` regardless of where your cursor is). This is the default.
- **Relative Reference:** The macro records actions relative to the active cell (e.g., moving one cell down and one cell right). You must toggle "Use Relative References" on before recording to use this mode.

While powerful, the macro recorder has limitations. It cannot create custom functions, loops, or conditional logic (like `If...Then` statements), and it often records unnecessary "fluff" code. Workbooks containing macros must be saved with the `.xlsm` (macro-enabled) extension, as the standard `.xlsx` format will strip out all VBA code.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

In financial modeling, the macro recorder is often used to create a simple "wrapper" for complex operations, such as a "Master Solve" macro that breaks circularities. You can record a macro to set up the basic VBA container, and then manually edit the code in the Visual Basic Editor (`ALT + F11`) to add logic like a `Do Until` loop to iterate calculations until a condition is met.

## Interview-ready answer

Macro recording is a built-in Excel tool that captures user actions and translates them into VBA code. While it's great for automating simple, repetitive tasks or learning syntax, it has limitations because it hardcodes specific actions and cannot generate loops or conditional logic, which require manual coding.

## Pitfalls and gotchas

- **Unnecessary code:** The recorder captures everything, including mistakes and unnecessary scrolling, creating bloated code.
- **Absolute vs. Relative:** By default, macros record absolute cell references. If you intend for the macro to work on the current active cell, you must explicitly enable "Use Relative References".
- **File format:** You must save your file as an `.xlsm` (Excel Macro-Enabled Workbook); saving as a standard `.xlsx` will delete your recorded macro.
- **No logic or loops:** The recorder cannot generate dynamic code involving `If...Then` statements or `For/Do` loops.

## Gaps

- Missing exact formula
- Missing worked example

## Sources

- [[Trump Excel - How to Record a Macro in Excel - A Step by Step Guide]]
- [[Financial Modelling Handbook - How to add a VBA macro to a financial model]]