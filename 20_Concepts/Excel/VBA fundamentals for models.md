---
type: concept
title: "VBA fundamentals for models"
aliases: ["Visual Basic for Applications", "VBA"]
tags: ["excel", "automation"]
difficulty: beginner
prerequisites: ["[[Macro recording basics]]"]
related: []
sources: ["[[Chandoo - Excel VBA - Information, Tutorials, Examples & Resources » Chandoo.org - Learn Excel, Power BI & Charting Online]]", "[[Chandoo - CP022- What's a Macro- Introduction to Excel VBA, Macros & Automation » Chandoo.org - Learn Excel, Power BI & Charting Online]]"]
status: stub
updated: 2026-04-09
---

# VBA fundamentals for models

> **TL;DR.** VBA (Visual Basic for Applications) is the programming language that Excel speaks, allowing you to write macros to automate repetitive tasks and extend Excel's capabilities.

## When you'd use this

VBA is useful when you need to perform repetitive steps, such as preparing and emailing the same type of report every week with different data. It cuts down the time spent repeating these steps and significantly improves productivity by automating tasks.

## The 30-second version

VBA stands for Visual Basic for Applications, which is the programming language built into Excel (and other MS Office programs). A macro is a set of instructions—essentially a paragraph of VBA code—given to Excel to accomplish a specific task, like generating a report or filling cells with a specific color. You can get started with VBA by using the built-in Macro Recorder, which acts like a tape recorder that listens to your actions and translates them into VBA code.

## The full explanation

VBA is the programming language of Excel, but it is relatively easy to learn because it closely resembles plain English.

To use VBA and macros, you must first enable the Developer Ribbon. In Excel, right-click on any ribbon, select "Customize Ribbon," check the "Developer tab," and click OK.

### The Macro Recorder
If you do not know VBA, the Macro Recorder is the best way to start. It translates your actions in the spreadsheet into VBA instructions.

Steps to record a basic macro:
1. Select a cell, go to the Developer Ribbon, and click "Record Macro."
2. Give the macro a name (no spaces or special characters other than underscores).
3. Perform the actions (e.g., fill the cell with a color).
4. Click "Stop Recording" on the Developer Ribbon.
5. You can then assign this macro to a button (inserted as a shape) by right-clicking it and choosing "Assign Macro."

### Why Use VBA?
- Automation of repetitive tasks.
- Extending Excel’s built-in capabilities.
- Improving overall modeling efficiency.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When naming a macro, remember that the name cannot contain spaces or special characters except for underscores. To easily run macros in a model, consider inserting shapes that act as clickable buttons and assigning the macro directly to the shape.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- Forgetting to enable the Developer Ribbon, which is hidden by default, preventing access to the Macro Recorder and Visual Basic Editor.
- Leaving the Macro Recorder running accidentally, which fills your VBA module with unintended code for every action taken.

## Gaps

- Missing exact formula
- Missing worked example
- Missing interview-ready answer

## Sources

- [[Chandoo - Excel VBA - Information, Tutorials, Examples & Resources » Chandoo.org - Learn Excel, Power BI & Charting Online]]
- [[Chandoo - CP022- What's a Macro- Introduction to Excel VBA, Macros & Automation » Chandoo.org - Learn Excel, Power BI & Charting Online]]