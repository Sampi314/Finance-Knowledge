---
type: concept
title: "Tax schedule"
aliases: ["Taxable income schedule", "Tax model"]
tags: ["modeling", "accounting", "corporate-finance"]
difficulty: intermediate
prerequisites: ["[[Three-statement model]]", "[[Depreciation schedule]]"]
related: ["[[Working capital schedule]]"]
sources: ["[[Macabacus - Taxable Income- Federal & State Tax Rates 40%]]", "[[Macabacus - Depreciation Expense - Examples, Templates]]"]
status: draft
updated: 2026-04-13
---

# Tax schedule

> **TL;DR.** A tax schedule calculates a company's taxable income by bridging the gap between accounting (book) pre-tax income and tax income, accounting for differences such as straight-line versus accelerated MACRS depreciation.

## When you'd use this

You build a tax schedule in a full operating model to accurately project a company's cash tax obligations. It's especially crucial when modeling the creation of deferred tax assets and liabilities, as these balance sheet items arise from the difference between book taxes and actual cash taxes paid.

## The 30-second version

Income before tax on the book P&L uses accrual accounting, but cash accounting and different expense recognition rules are used for tax purposes. To calculate taxable income, you start with EBITDA (since revenues and operating expenses generally align) and adjust for differences. Most notably, tax depreciation often follows an accelerated schedule like MACRS, whereas book depreciation is straight-line. You subtract tax depreciation and add only the cash distributions from equity investments to reach taxable income. Applying the bifurcated federal and state tax rates to this figure gives the actual cash tax expense.

## The full explanation

The primary reason for a standalone tax schedule is that a company maintains two sets of books: one for accounting purposes (GAAP/IFRS) and one for the IRS or local tax authority.

### Book vs. Tax Depreciation
The largest difference usually stems from depreciation. For accounting, companies use straight-line depreciation to spread the cost evenly. For tax purposes, they often use an accelerated schedule like the Modified Accelerated Cost Recovery System (MACRS). Accelerated depreciation increases the present value of tax shields by front-loading deductions, reducing cash taxes in the early years of an asset's life.

### Building the Schedule
The schedule begins with EBITDA, assuming line items above it match for both book and tax. Next, you subtract specific tax-deductible expenses. Instead of accounting depreciation, you subtract tax depreciation. Rather than recognizing all income from equity investments, you only add earnings distributed as cash.

### Bifurcating Tax Rates
Rather than using a single blended rate, robust models bifurcate taxes into federal and state/local components. You apply a state tax rate and dial in a federal tax rate that achieves the target combined effective rate. This allows for more granular sensitivity analysis and accurate statutory rate modeling.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When modeling tax depreciation in the US, you select a "property class" from the MACRS schedule that aligns with the asset's useful life and use HLOOKUPs to compute the accelerated depreciation. A best practice is to build a toggle switch between book (straight-line) and MACRS depreciation. This helps isolate and test the impact of deferred taxes on the balance sheet.

## Interview-ready answer

A tax schedule bridges book pre-tax income to taxable income, primarily by adjusting for differences in depreciation. Because companies use accelerated MACRS for taxes and straight-line for accounting, cash taxes are usually lower than book taxes early on, creating a deferred tax liability.

## Pitfalls and gotchas

- Assuming a blended 40% tax rate without breaking out state vs federal taxes can mask the nuances of statutory tax rate changes.
- Forgetting that the difference between book and tax depreciation creates a deferred tax liability (DTL). If your tax schedule doesn't flow correctly into the DTL line on the balance sheet, the model won't balance.

## Sources

- [[Macabacus - Taxable Income- Federal & State Tax Rates 40%]]
- [[Macabacus - Depreciation Expense - Examples, Templates]]
