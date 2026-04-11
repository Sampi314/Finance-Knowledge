---
type: concept
title: "The bridge from EV to equity value"
aliases: ["Net debt", "Enterprise value to equity value bridge"]
tags: ["valuation", "modeling", "wacc"]
difficulty: intermediate
prerequisites: ["[[Enterprise value]]", "[[Equity value]]"]
related: ["[[Intrinsic vs relative valuation]]"]
sources: ["[[Project Finance - Bridge from Enterprise Value to Equity Value]]", "[[IB Interview Questions - Precedent Transactions Analysis - Step-by-Step Guide]]"]
status: draft
updated: 2026-04-11
---

# The bridge from EV to equity value

> **TL;DR.** The bridge from enterprise value (EV) to equity value involves subtracting net debt and other EV adjustments from the enterprise value to arrive at the equity value.

## When you'd use this

You would use this bridge when you have calculated a company's enterprise value (e.g., using a DCF or precedent transactions analysis) and need to determine the value of the company's equity. This is particularly relevant in M&A advisory, where deal values are often expressed as enterprise value but buyers ultimately purchase equity. It is also essential when triangulating valuations across different methodologies.

## The 30-second version

Enterprise value represents the total value of a company's operations, while equity value represents the value of the company's shares. To move from enterprise value to equity value, you must account for all claims on the company's assets other than common equity. This typically means subtracting debt and adding cash (the combination of which is known as net debt). However, the bridge must also include the fair valuation of derivatives, operating reserves, and deferred tax allocations, depending on whether those items are captured in free cash flow or not.

## The full explanation

The process of moving between enterprise value (EV) and equity value is known as the "bridge." While the simplest form of this bridge is `Equity Value = Enterprise Value - Net Debt`, the actual bridge often involves many other items. The core principle is that if an item affects the cash flows available to all investors (and thus is included in free cash flow), it should generally *not* be in the bridge. If an item is an alternative form of financing or a claim on the company's value that is not reflected in free cash flow, it *should* be in the bridge.

### Core Components

*   **Net Debt:** The most fundamental component. You subtract total debt (at market value) and add cash and cash equivalents.
*   **Working Capital:** Items like accounts payable are considered part of operating working capital. Since changes in working capital are already included in free cash flow, they are *not* included in the EV-to-equity bridge.
*   **Operating Reserves:** Similar to accounts payable, items like warranty payment provisions are included as positive cash flow items and are *not* part of the bridge.
*   **Decommissioning Accruals:** The treatment of provisions like dismantling or decommissioning costs depends on when the cash flow occurs. If the cash flow happens after the explicit forecast period, they are included in the bridge.
*   **Derivatives:** For interest rate swaps, the underlying debt should be recorded at book value, and the value of the swap should be added to the bridge. The associated tax effects should follow the valuation and also be included in the bridge. For futures contracts associated with operations, derivative gains and losses should be removed from EBITDA.
*   **Taxes:** Deferred taxes from capital expenditures and operating items are included in free cash flow and are *not* part of the bridge. Taxes payable can either be addressed in the bridge, or the interest paid to the government can be included in EBITDA.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When setting up a long-term model, you can prove the correct treatment of bridge items by working through the accounting and cash flow for each item, creating a terminal value switch, and testing alternative assumptions. Also, note that when a company's target capital structure doesn't match its current capital structure, discounting free cash flows at WACC (which theoretically remains constant) yields the same result as calculating a new cost of equity with the changing structure.

## Interview-ready answer

To bridge from enterprise value to equity value, you subtract net debt and any other non-equity claims from the enterprise value. This includes subtracting total debt, minority interest, and preferred stock, and adding cash and cash equivalents.

## Pitfalls and gotchas

*   Including working capital items like accounts payable in the bridge. Since they are part of free cash flow, they should be excluded.
*   Failing to properly account for the tax effects of items like interest rate swaps or decommissioning accruals in the bridge.
*   Confusing enterprise value and equity value, particularly when analyzing precedent transactions where deal values are typically expressed as enterprise value.

## Sources

* [[Project Finance - Bridge from Enterprise Value to Equity Value]]
* [[IB Interview Questions - Precedent Transactions Analysis - Step-by-Step Guide]]
