---
type: concept
title: "Form controls"
aliases: ["combo boxes", "spinner boxes", "check boxes", "user forms", "buttons"]
tags: ["Excel", "modeling", "interactivity"]
difficulty: intermediate
prerequisites: []
related: []
sources: ["[[ExcelJet - Native checkboxes in Excel - Exceljet]]", "[[Project Finance - Spinners, Drop-Down, Check Boxes]]", "[[Pivotal180 - How to Change the Scenario Input From Any Spreadsheet]]", "[[Financial Modelling Handbook - How to attach a VBA macro to a button in Excel]]", "[[Chandoo - A simple trick to make your dashboards user friendly [video] » Chandoo.org - Learn Excel, Power BI & Charting Online]]", "[[Project Finance - Spinner Boxes, Dropdown Boxes and Other Forms]]"]
status: stub
updated: 2026-04-09
---

# Form controls

> **TL;DR.** Form controls are interactive elements like check boxes, drop-downs, and spinners that allow users to change inputs and scenarios across an Excel model.

## When you'd use this

Form controls are ideal for scenario analysis, interactive dashboards, and making complex financial models user-friendly. They let users toggle inputs (like growth rates or project scenarios) without navigating away from summary sheets or graphs.

## The 30-second version

Form controls (also known as user forms) sit on the Excel grid and link directly to a cell. When a user interacts with a control—such as ticking a check box, clicking a spinner, or selecting from a drop-down (combo box)—it updates the linked cell. This linked cell can then drive calculations throughout the model. Adding them requires enabling the Developer tab in Excel.

## The full explanation

### Types of form controls

- **Check boxes**: Allow users to toggle an option on or off, returning TRUE or FALSE in the linked cell. Recently, Excel 365 introduced a native checkbox feature that lives directly in the grid.
- **Combo boxes (Drop-downs)**: Let users select an item from a list. These are highly effective for changing scenarios (e.g., "Base", "Upside", "Downside") from any sheet in the model.
- **Spinner boxes**: Provide up and down arrows to incrementally increase or decrease a number in a linked cell.
- **Buttons**: Often used to run VBA macros.

### How they work

Form controls are linked to specific cells. It is essential to include the sheet name in the cell link so the control functions correctly even if placed on a different sheet, such as a dashboard or summary page. When the control is used, the linked cell changes, which recalculates dependent formulas across the model.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

- To use traditional form controls, you must first enable the Developer tab via Excel Options -> Customize Ribbon.
- For dashboards that span multiple views or require scrolling, place duplicate sets of the same form controls linked to the exact same cell in different locations so users always have access to them.
- Buttons are frequently used to trigger solver macros or complex iterative calculations.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- Forgetting to include the sheet name in the cell link, causing the control to break if moved or used on a separate summary sheet.

## Gaps

- Missing exact formula
- Missing worked example
- Missing interview-ready answer

## Sources

- [[ExcelJet - Native checkboxes in Excel - Exceljet]]
- [[Project Finance - Spinners, Drop-Down, Check Boxes]]
- [[Pivotal180 - How to Change the Scenario Input From Any Spreadsheet]]
- [[Financial Modelling Handbook - How to attach a VBA macro to a button in Excel]]
- [[Chandoo - A simple trick to make your dashboards user friendly [video] » Chandoo.org - Learn Excel, Power BI & Charting Online]]
- [[Project Finance - Spinner Boxes, Dropdown Boxes and Other Forms]]
