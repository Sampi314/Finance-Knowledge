---
type: concept
title: Real estate development pro forma
aliases: ["Real estate pro-forma", "RE Pro-Forma"]
tags: ["real-estate", "underwriting", "modeling"]
difficulty: beginner
prerequisites: ["[[Cap rate]]", "[[Net operating income]]"]
related: ["[[Gross potential rent]]", "[[Operating expenses in RE]]"]
sources: ["[[BIWS - Real Estate Pro-Forma- Calculations, Examples, and Scenarios (Video)]]"]
status: stub
updated: 2026-04-17
---

# Real estate development pro forma

> **TL;DR.** The real estate pro-forma is a combined and simplified Income Statement and Cash Flow Statement for projecting a property's cash flows over time.

## When you'd use this

You use a real estate pro-forma when you need to understand, model, or value a real estate property development or acquisition. It strips out non-cash items like depreciation to focus strictly on the core business cash flows that affect investors.

## The 30-second version

The pro-forma starts at the top with "Potential Revenue" (assuming 100% occupancy at market rates). It then subtracts vacancy, loss-to-lease, and credit losses to arrive at Effective Gross Income (EGI). Next, it deducts regular operating expenses and property taxes to reach Net Operating Income (NOI). Finally, capital costs (CapEx, tenant improvements, leasing commissions) and reserves are subtracted to calculate the unlevered cash flows available before debt service.

## The full explanation

### Revenue and EGI
The pro-forma begins with **Base Rental Income** assuming the building is completely full. Deductions are then made:
- **Absorption & Turnover Vacancy:** Foregone rent when a tenant leaves and space is empty.
- **Concessions & Free Rent:** Free rent periods used as an incentive for new or renewing tenants.
- **General Vacancy:** Space that is expected to be permanently empty.

Adding **Expense Reimbursements** (where tenants pay proportional shares of taxes or utilities) produces **Effective Gross Income (EGI)**, the real estate equivalent of Net Revenue on a cash basis.

### Operating Expenses
These include items like property management fees, utilities, insurance, maintenance, and property taxes. Notably, the real estate pro-forma generally excludes income taxes and depreciation.

### Capital Costs
Items lasting more than a year are tracked below operating expenses.
- **Capital Expenditures (CapEx):** Non-tenant-specific building upgrades (e.g., a new roof).
- **Tenant Improvements (TIs):** Customizations specific to individual tenant spaces.
- **Leasing Commissions (LCs):** Fees paid to brokers, usually based on total lease value.

### Net Operating Income and Cash Flow
- **Net Operating Income (NOI):** EGI minus Operating Expenses & Property Taxes. It is similar to EBITDA but is specific to real estate. Some models also deduct reserve allocations directly from NOI.
- **Adjusted NOI:** NOI minus Net Capital Costs. It serves as a close proxy for Unlevered Free Cash Flow.
- **Cash Flow to Equity:** Adjusted NOI minus Debt Service (principal and interest).

## Formula

(none)

## Worked example

Here are examples of the adjustments commonly applied to reach EGI and NOI:

**Absorption & Turnover Vacancy:**
If a tenant renting 2,000 square feet for $50 per square foot leaves, and it takes 6 months to find a new tenant:
`2,000 sq ft * $50 * (6 / 12) = $50,000 foregone rent`

**Expense Reimbursements:**
If a tenant renting 2,000 square feet out of a 10,000 square foot building is responsible for their share of property taxes, and total property taxes are $50,000:
`(2,000 / 10,000) * $50,000 = $10,000 paid by tenant`

**General Vacancy:**
If a 10,000 square foot building has 1,000 square feet that is always empty at a $50 rate:
`10,000 sq ft * 10% * $50 = $50,000`

**Leasing Commissions (LCs):**
If a tenant signs a 5-year lease for 10,000 square feet starting at $50 per square foot, increasing to $52, $54, $56, and $58:
`5% * ($50 + $52 + $54 + $56 + $58) * 10,000 = $135,000 in LCs`

## Excel and modeling notes

When building scenarios into a multifamily pro-forma, everything must be connected. A downside recession scenario should show market rents falling, vacancy and bad debt rising (e.g., from 3% to 6%), tenant improvements growing (e.g., 10%), and leasing commissions jumping (e.g., 8% of effective rent) as it becomes harder to find tenants. Lenders focus heavily on downside and extreme downside cases since their upside is capped.

## Interview-ready answer

The real estate pro-forma projects the operating cash flows of a property by starting with potential gross revenue, deducting vacancy and concessions to find EGI, and then subtracting operating expenses to calculate NOI. From NOI, we subtract capital costs like CapEx and tenant improvements to find Adjusted NOI, which is similar to unlevered free cash flow.

## Pitfalls and gotchas

- Excluding capital reserves from NOI can overstate the "true" ongoing profitability of the property, which is why many lenders prefer to see reserves deducted *above* the NOI line.
- Forgetting that TIs and LCs do not recur every year; they are only incurred when new tenants sign or existing tenants renew.

## Gaps

- Missing exact formula

## Sources

- [[BIWS - Real Estate Pro-Forma- Calculations, Examples, and Scenarios (Video)]]