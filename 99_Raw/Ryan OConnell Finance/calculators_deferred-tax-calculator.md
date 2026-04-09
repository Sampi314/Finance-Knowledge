# Deferred Tax Calculator: DTA, DTL & Temporary Differences | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/deferred-tax-calculator

---

Deferred Tax Calculator
=======================

DTA, DTL & Temporary Differences Tool

Calculate deferred tax assets, liabilities, taxable income, and effective tax rate under ASC 740

Embed This Calculator

Enter Values
------------

Pre-Tax Book Income ?

$ 

Income before taxes per books

Enacted Tax Rate ?

 %

Enter as percentage (e.g., 21 for 21%)

###### Temporary Differences

Book Basis > Tax Basis = DTL. Tax Basis > Book Basis = DTA.

Add Temporary Difference

###### Permanent Differences

Permanent Differences ?

$ 

Positive = non-deductible, negative = non-taxable

Valuation Allowance ?

 %

% of gross DTA requiring allowance

Reset to Defaults

##### Model Assumptions

*   Single enacted tax rate applied to all items
*   Zero opening balances (single-period model)
*   All temporary differences reverse in future periods
*   No tax planning strategies considered
*   Valuation allowance applied as flat % of gross DTA
*   U.S. GAAP (ASC 740) asset-liability method
*   No state/local taxes (single-rate simplification)

For educational purposes only. Not tax or financial advice. Simplified single-period model.

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Deferred Tax Results

Net Deferred Tax Position $6,300 Net DTA

Total DTL $21,000

Total DTA (Gross) $27,300

Valuation Allow. $0

Net DTA (After VA) $27,300

### Temporary Differences Breakdown

| Item | Book Basis | Tax Basis | Difference | Type | Deferred Tax |
| --- | --- | --- | --- | --- | --- |

### Income Tax Provision

Pre-Tax Book Income $1,000,000

\+ Permanent Differences $10,000

− DTL-Creating Differences $100,000

\+ DTA-Creating Differences $130,000

**Taxable Income** **$1,040,000**

Current Tax Payable $218,400

Deferred Tax Expense (Benefit) ($6,300)

**Total Income Tax Expense** **$212,100**

Effective Tax Rate 21.21%

Statutory Tax Rate 21.00%

### Classification Guide

| Scenario | Condition | Result |
| --- | --- | --- |
| Future Taxable Amount | Book Basis > Tax Basis | DTL |
| Future Deductible Amount | Tax Basis > Book Basis | DTA |
| No Temporary Difference | Book Basis = Tax Basis | None |

Understanding Deferred Taxes (ASC 740)
--------------------------------------

### What Are Deferred Taxes?

**Deferred taxes** arise because of timing differences between when income and expenses are recognized under GAAP (book) versus the tax code. Under ASC 740, companies use the **asset-liability method** to measure deferred tax assets and liabilities at the enacted tax rate.

Core Deferred Tax Formulas

**DTL** = Taxable Temporary Difference × Tax Rate  
**DTA** = Deductible Temporary Difference × Tax Rate  
**Net Position** = Total DTL − Net DTA (after VA)  
Positive = Net Liability | Negative = Net Asset

### Temporary vs. Permanent Differences

#### Temporary Differences

**Reverse over time**  
Total tax paid is the same; timing differs. Create DTAs or DTLs. Examples: depreciation methods, warranty accruals, unearned revenue.

#### Permanent Differences

**Never reverse**  
Treated differently forever under book and tax rules. Do NOT create deferred taxes. Examples: fines, municipal bond interest, life insurance proceeds.

### The Tax Provision Process

The income tax provision reconciles book income to taxable income and computes total tax expense:

1.  **Start with pre-tax book income** (GAAP income before taxes)
2.  **Add/subtract permanent differences** (items that never reverse)
3.  **Add/subtract temporary differences** to arrive at taxable income
4.  **Compute current tax** = Taxable income × tax rate
5.  **Compute deferred tax expense** = Change in DTL − Change in DTA + Change in VA
6.  **Total tax expense** = Current tax + Deferred tax expense

**Valuation Allowance:** Under ASC 740, a valuation allowance must be recorded against a DTA when it is "more likely than not" (>50%) that some or all of the DTA will not be realized. The VA increase is recorded as a deferred tax expense.

### Common Examples

*   **Depreciation (DTL):** Accelerated depreciation for tax, straight-line for book. Tax basis < book carrying amount.
*   **Warranty Accrual (DTA):** Estimated warranty expense recognized for book, deductible for tax only when paid. Tax basis > book basis.
*   **Unearned Revenue (DTA):** Cash received and taxable immediately, but revenue deferred for book purposes.
*   **Fines (Permanent):** Expensed for book but never deductible for tax.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/deferred-tax-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is a deferred tax asset (DTA)?

A deferred tax asset arises when a company pays more tax now than it owes under GAAP, creating a future tax benefit. Common sources include warranty accruals, unearned revenue, and bad debt allowances where the tax deduction is available in a different period than the book expense. Under ASC 740, DTAs are recognized at the enacted tax rate and classified as noncurrent on the balance sheet.

### What is a deferred tax liability (DTL)?

A deferred tax liability arises when a company owes more tax in the future than it currently recognizes under GAAP. The most common example is accelerated depreciation, where tax depreciation exceeds book depreciation, creating a future taxable amount. DTLs represent the additional taxes that will be payable when temporary differences reverse.

### What is the difference between temporary and permanent differences?

Temporary differences reverse over time — the total tax paid is the same, just the timing differs (e.g., depreciation methods). Permanent differences never reverse — certain items are treated differently for book and tax purposes forever (e.g., fines and penalties are never tax-deductible; municipal bond interest is never taxable). Only temporary differences create deferred tax assets or liabilities.

### What is a valuation allowance?

Under ASC 740, a valuation allowance reduces the carrying amount of a deferred tax asset when it is "more likely than not" (greater than 50% probability) that some or all of the DTA will not be realized. Companies assess future taxable income, tax planning strategies, and reversing temporary differences to determine the appropriate allowance. The VA does not eliminate the gross DTA — it reduces the net reported amount.

### Why does the effective tax rate differ from the statutory rate?

The effective tax rate (income tax expense / pre-tax book income) differs from the statutory rate primarily because of permanent differences. Items like non-deductible fines increase the effective rate, while non-taxable income like municipal bond interest decreases it. Changes in valuation allowance can also affect the effective rate, since an increase in VA raises deferred tax expense without changing pre-tax income.

### How are deferred taxes reported on the balance sheet?

Under current U.S. GAAP (ASC 740), all deferred tax assets and liabilities are classified as noncurrent on the balance sheet. Companies offset DTAs and DTLs within the same tax jurisdiction and present a single net noncurrent asset or liability. The income statement shows total income tax expense split between current and deferred components.

##### Disclaimer

This calculator is for educational purposes only and uses a simplified single-period, single-rate model under ASC 740. Actual deferred tax calculations involve multi-period analysis, state/local taxes, tax planning strategies, and detailed realizability assessments. Consult a tax professional for real-world tax provision work.

Related Calculators
-------------------

[![Professional finance illustration representing Basic & Diluted EPS Calculator (GAAP)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Basic & Diluted EPS Calculator (GAAP)\
\
Compute diluted EPS with convertible securities and stock options.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/diluted-eps-gaap-calculator/)

[![Professional finance illustration representing Lease Payment & Classification Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Lease Payment & Classification Calculator\
\
Calculate lease payments and present value under ASC 842.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/lease-payment-calculator/)

[![Professional finance illustration representing Financial Ratio Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Financial Ratio Calculator\
\
Analyze financial ratios for liquidity, profitability, and leverage.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/financial-ratio-calculator/)

Contact Me
----------

Have a question or want to work together? Fill out the form below and we’ll get back to you as soon as possible.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20378'%3E%3C/svg%3E)

Contact Form Demo

First Name

Last Name

Email

Subject

Your Message

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy)
 and [Terms of Service](https://policies.google.com/terms)
 apply.

Submit Form