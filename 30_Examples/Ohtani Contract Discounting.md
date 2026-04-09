---
type: example
title: "Ohtani Contract Discounting"
illustrates: ["[[Discount rate]]", "[[Present value]]"]
updated: 2026-04-09
---

# Ohtani Contract Discounting

## Setup

Professional baseball player Shohei Ohtani signed a record-breaking $700 million contract with the Los Angeles Dodgers. However, the contract included extreme deferrals, paying him a fraction of the amount over the 10-year term and deferring the bulk of the payments to be paid out over the subsequent 10 years. We model the present value of this contract to understand the impact of the discount rate and time value of money.

## Assumptions

- Nominal contract value: $700 million
- Contract term: 10 years
- Deferral period: The deferred payments are paid out over 10 years *after* the initial 10-year contract term.
- Annual salary during term: $2 million per year (Years 1-10)
- Deferred payments: $68 million per year (Years 11-20)
- Discount rate: 4.43% (the Federal mid-term rate as of October prior to the contract, used by MLB for CBT purposes).

## Walk-through

1. **Identify the cash flows:**
   - Years 1-10: $2 million per year
   - Years 11-20: $68 million per year
2. **Apply the discount rate:** Because of the time value of money, a dollar received in year 15 is worth less today than a dollar received in year 1. Each future cash flow must be discounted back to the present using the 4.43% discount rate.
3. **Discounting the deferred payments for CBT purposes:** For the Competitive Balance Tax (CBT) calculation, MLB rules require discounting the deferred portion back by exactly 10 years. So, the $68M paid in Year 11 is discounted to Year 1; the $68M in Year 12 is discounted to Year 2, and so on.
   - $68M / (1 + 0.0443)^10 = $44.08 million.
4. **Calculate the average annual value:** The average salary for CBT purposes is the $2 million base salary plus the $44.08 million discounted deferred payment, totaling $46.08 million per year.
5. **Calculate the true present value:** To find the real-world present value on the day the contract was signed, *all* payments (both the $2M and the $68M) are discounted all the way back to Year 0 using the 4.43% discount rate.

## Result

While the headline nominal value is $700 million, the present value of the contract on the day it was signed (assuming a 4.43% discount rate) is approximately $374 million, which is just 53% of the nominal value. The extreme deferrals drastically reduce the present value.

## What this teaches

- **The power of discounting:** Future cash flows are worth significantly less than present cash flows, and pushing payments further into the future destroys present value.
- **Headline numbers can be misleading:** In finance and sports, large nominal numbers often ignore the time value of money. You must calculate the present value using an appropriate discount rate to understand true economic value.
