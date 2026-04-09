# Basic & Diluted EPS Calculator (GAAP): Treasury Stock Method & If-Converted Method Under ASC 260 | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/diluted-eps-gaap-calculator

---

Diluted EPS Calculator (GAAP)
=============================

Basic & Diluted Earnings Per Share Under ASC 260

Treasury Stock Method for options • If-Converted Method for convertible bonds

Embed This Calculator

Enter Values
------------

###### Income & Shares

Net Income ?

$ 

Net income before preferred dividend deduction

Preferred Dividends ?

$ 

Preferred dividends declared or accrued

Weighted Average Common Shares ?

 shares

Pre-computed weighted average shares outstanding

* * *

###### Stock Options / Warrants

Options Outstanding ?

 options

Plain options/warrants outstanding (not RSUs)

Exercise Price ?

$ 

Strike price per option

Average Market Price ?

$ 

Average market price during the period

* * *

###### Convertible Bonds

Bond Face Value ?

$ 

Par value of convertible bonds

Bond Interest Rate ?

 %

Annual coupon rate

Shares on Conversion ?

 shares

Shares issuable upon bond conversion

* * *

###### Tax

Tax Rate ?

 %

Flat enacted corporate tax rate

Reset to Defaults

##### EPS Formulas (ASC 260)

Basic EPS = (NI − Pref Div) ÷ WACS

**Treasury Stock Method:**  
Net Shares = Options − (Proceeds ÷ Market Price)  
  
**If-Converted Method:**  
Add back: Interest × (1 − Tax Rate)  
Add shares: Conversion Shares

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### EPS Results

Basic EPS $4.80

Diluted EPS $4.45 7.29% Dilution

Dilution Amount $0.35

Dilution % 7.29%

Options Dilutive? Yes

Bonds Dilutive? Yes

Treasury Stock Net Shares 37,500

After-Tax Interest Add-Back $39,500

### Step-by-Step Breakdown

### Model Assumptions

*   Single reporting period (no interim/quarterly adjustments)
*   Weighted average shares are pre-computed by user (stock splits and issuances already factored in)
*   Covers plain stock options/warrants only (not RSUs or share-based awards with unrecognized compensation cost)
*   Convertible bonds assumed issued at par with no premium/discount or issuance-cost amortization
*   Convertible bonds outstanding for the full period (not issued mid-year)
*   Single flat tax rate applied uniformly (no deferred tax complexities)
*   No contingently issuable shares
*   No convertible preferred stock, no multiple tranches, no two-class method
*   Anti-dilution tested sequentially per ASC 260-10-45-18 through 45-20
*   Exercise price and market price are period averages

For educational purposes only. Not financial or accounting advice. Actual EPS computations may involve additional complexities including partial-period adjustments, multiple classes of convertibles, and contingent issuances.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/diluted-eps-gaap-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is the difference between basic and diluted EPS?

Basic EPS uses only shares currently outstanding (weighted average), while diluted EPS includes the potential impact of all dilutive securities — such as stock options, warrants, and convertible bonds — that could increase the number of shares outstanding. Diluted EPS is a more conservative GAAP measure and is required to be reported by public companies under ASC 260.

### How does the Treasury Stock Method work for stock options?

The Treasury Stock Method assumes that stock options are exercised at the beginning of the period (or issuance date if later). The company receives cash proceeds (options × exercise price), which it uses to repurchase shares at the average market price. The net dilutive effect is the difference: shares issued upon exercise minus shares repurchased. Options are only dilutive when the exercise price is below the average market price (i.e., “in the money”).

### What is the If-Converted Method for convertible bonds?

The If-Converted Method assumes convertible bonds were converted to common stock at the beginning of the period (or issuance date if later). Two adjustments are made: (1) the after-tax interest savings (face value × coupon rate × (1 − tax rate)) is added back to the numerator, since interest would not have been paid; and (2) the shares that would be issued upon conversion are added to the denominator.

### When is a potentially dilutive security considered anti-dilutive?

A security is anti-dilutive when including it in the diluted EPS calculation would actually increase earnings per share (or reduce the loss per share). For options, this occurs when the exercise price equals or exceeds the average market price. For convertible bonds, this occurs when the incremental EPS (after-tax interest savings ÷ conversion shares) equals or exceeds the current EPS before including that security. Anti-dilutive securities must be excluded from diluted EPS per ASC 260.

### How does a net loss affect diluted EPS?

When income available to common shareholders is zero or negative (either from a net loss or because preferred dividends exceed net income), all potentially dilutive securities are automatically anti-dilutive under GAAP. This is because adding shares to the denominator would reduce the loss per share (make it closer to zero), which is anti-dilutive. In these scenarios, diluted EPS equals basic EPS — no dilutive adjustments are made.

### What does a high dilution percentage indicate under ASC 260?

A high dilution percentage indicates that a company has significant potentially dilutive securities outstanding relative to its current share base. Under ASC 260, this means the gap between basic and diluted EPS is large, reflecting substantial potential increases in the share count if all convertible securities are converted and all options are exercised. The color thresholds in this calculator (green < 5%, yellow 5–15%, red > 15%) are heuristic guidelines, not GAAP-defined significance levels.

##### Disclaimer

This calculator is for educational purposes only and covers a simplified GAAP EPS computation (one option tranche and one convertible bond issue). It does not account for convertible preferred stock, multiple dilutive tranches, contingently issuable shares, RSU/share-based award proceeds adjustments, two-class method, partial-period issuances, or cash-settlement features. For actual financial reporting, consult a qualified accountant or auditor.

Related Calculators
-------------------

[![Professional finance illustration representing Lease Payment & Classification Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Lease Payment & Classification Calculator\
\
Calculate lease payments under ASC 842.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/lease-payment-calculator/)

[![Professional finance illustration representing Deferred Tax Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Deferred Tax Calculator\
\
Compute deferred tax assets and liabilities under ASC 740.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/deferred-tax-calculator/)

[![Professional finance illustration representing DuPont Analysis Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### DuPont Analysis Calculator\
\
Decompose return on equity using the DuPont three-step and five-step analysis. Identify profitability, efficiency, and...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/dupont-analysis-calculator/)

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