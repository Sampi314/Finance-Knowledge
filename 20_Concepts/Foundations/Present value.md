---
type: concept
title: "Present value"
aliases: ["PV"]
tags: ["foundations", "time-value-of-money", "discounting"]
difficulty: beginner
prerequisites: ["[[Time value of money]]"]
related: []
sources: ["[[Pivotal180 - Present Value Math (PV)]]", "[[Pivotal180 - Net Present Value (NPV )]]", "[[Pivotal180 - Understanding Discount Rates Through Real-World Examples in Finance]]"]
status: draft
updated: 2026-04-09
---

# Present value

> **TL;DR.** Present value is the current worth of a future sum of money or stream of cash flows given a specified rate of return.

## When you'd use this

You would use present value when deciding how much you should pay today for an investment that will produce cash flows in the future. It allows investors to compare the value of money received at different points in time, making it fundamental to project finance, valuation, and capital budgeting decisions. Present value is also critical when valuing things like long-term contracts (e.g. major sports contracts with deferred salaries) to determine their actual cost today.

## The 30-second version

Because of the time value of money, a dollar today is worth more than a dollar tomorrow. If you have a dollar today, you can invest it to earn a return. Conversely, a dollar received in the future is worth less today. Present value calculates exactly how much less that future dollar is worth today by applying a "discount rate"—which acts as an expected rate of return or hurdle rate. By discounting future payments back to the present, you can determine exactly how much you would be willing to pay today for those future cash flows.

## The full explanation

Present value (PV) is the core mechanism for translating future cash flows into today's dollars. The process of converting future values to present values is called "discounting." It requires two main inputs: the future cash flow amount and the discount rate.

The discount rate reflects the risk of the investment and the investor's required rate of return. High-risk investments demand a higher discount rate, meaning their future cash flows are worth less today. Conversely, lower-risk investments are discounted at a lower rate. If an investment's net present value (the present value of its future cash flows minus the initial cost) is zero, it means the investment perfectly achieves the investor's required rate of return. Anything above zero means the investment exceeds the hurdle rate.

This concept is essential for "apples-to-apples" comparisons of investments that pay out over different time horizons. For example, if a baseball player signs a $700 million contract but defers $680 million of it to be paid out 10 to 20 years in the future, the present value of that contract is much lower than the headline $700 million figure.

## Formula

![[Present value]]

## Worked example

(none)

## Excel and modeling notes

When building financial models in Excel, calculating present value is done in a few different ways:
- **Manual calculation:** You can explicitly calculate the discount factor for each period (e.g., `(1 + rate)^year`) and divide each future cash flow by its corresponding discount factor. This is often necessary in complex project finance models with changing rates or irregular periods.
- **NPV function:** Excel has a built-in `=NPV(rate, value1, [value2], ...)` function. Note a crucial detail: the `NPV` function assumes the first cash flow occurs at the *end of period 1*. It does not discount cash flows at time zero. Therefore, you must apply the `NPV` function only to future cash flows (from period 1 onwards) and separately subtract the initial investment (period 0) outside the function.

## Interview-ready answer

Present value is the current worth of future cash flows, discounted at a specific rate that reflects the investment's risk. We use it because money today is worth more than money in the future, and discounting allows us to evaluate whether the returns of an investment will meet or exceed our required hurdle rate.

## Pitfalls and gotchas

- **Using the NPV function incorrectly:** A common mistake in Excel is including "Year 0" cash flows inside the `=NPV()` function. Because Excel discounts the first value you give it, doing this will discount your initial investment, leading to an incorrect valuation. Year 0 cash flows must be added or subtracted outside the `NPV` function.
- **Incorrect discount rate:** Applying a low discount rate to a high-risk cash flow will artificially inflate the present value, making a bad investment look attractive.

## Sources

- [[Pivotal180 - Present Value Math (PV)]]
- [[Pivotal180 - Net Present Value (NPV )]]
- [[Pivotal180 - Understanding Discount Rates Through Real-World Examples in Finance]]