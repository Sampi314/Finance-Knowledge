# Calculate interest for given period - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-interest-for-given-period

---

[Skip to main content](https://exceljet.net/formulas/calculate-interest-for-given-period#main-content)

[](https://exceljet.net/formulas/calculate-interest-for-given-period#)

*   [Previous](https://exceljet.net/formulas/calculate-cumulative-loan-principal-payments)
    
*   [Next](https://exceljet.net/formulas/calculate-interest-rate-for-loan)
    

[Financial](https://exceljet.net/formulas#Financial)

Calculate interest for given period
===================================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[PPMT](https://exceljet.net/functions/ppmt-function)

![Excel formula: Calculate interest for given period](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Calculate%20interest%20for%20given%20period.png "Excel formula: Calculate interest for given period")

Summary
-------

To calculate the interest portion of a loan payment in a given period, you can use the [IPMT function](https://exceljet.net/functions/ipmt-function)
. In the example shown, the formula in C10 is:

    =IPMT(C6/12,1,C8,-C5)
    

Generic formula
---------------

    =IPMT(rate,period,periods,-loan)

Explanation 
------------

For this example, we want to calculate the interest portion for payment 1 of a 5-year loan of $5,000 with an interest rate of 4.5%. To do this, we set up PPMT like this:

**rate** - The interest rate per period. We divide the value in C6 by 12 since 4.5% represents annual interest:

    =C6/12
    

**per** - the period we want to work with. Supplied as 1 since we are interested in the principal amount of the first payment.

**pv** - The present value, or total value of all payments now. In the case of a loan, this is input as a negative value by adding a negative sign in front of C5 to supply -5000.

With these inputs, the IPMT function returns 74.465, which is rounded to $74.47 when the Currency [number format](https://exceljet.net/glossary/number-format)
 is applied.

Related formulas
----------------

[![Excel formula: Calculate principal for given period](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate%20principal%20for%20given%20period.png "Excel formula: Calculate principal for given period")](https://exceljet.net/formulas/calculate-principal-for-given-period)

### [Calculate principal for given period](https://exceljet.net/formulas/calculate-principal-for-given-period)

For this example, we want to calculate the principal portion for payment 1 of a 5-year loan of $5,000 with an interest rate of 4.5%. To do this, we set up PPMT like this: rate - The interest rate per period. We divide the value in C6 by 12 since 4.5% represents annual interest: =C6/12 per - the...

[![Excel formula: Calculate compound interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20compound%20interest.png "Excel formula: Calculate compound interest")](https://exceljet.net/formulas/calculate-compound-interest)

### [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)

Compound interest is a financial concept that describes how an initial investment grows over time, taking into account not only the interest earned on the initial amount but also the interest earned on the interest itself. Compound interest allows your money to grow exponentially, which makes it a...

[![Excel formula: Calculate interest rate for loan](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20interest%20rate%20for%20loan.png "Excel formula: Calculate interest rate for loan")](https://exceljet.net/formulas/calculate-interest-rate-for-loan)

### [Calculate interest rate for loan](https://exceljet.net/formulas/calculate-interest-rate-for-loan)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term) and a payment amount per period. One use of the RATE function is to calculate the periodic interest rate when the amount, number of payment periods, and payment amount are known. In...

[![Excel formula: Calculate original loan amount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20original%20loan%20amount.png "Excel formula: Calculate original loan amount")](https://exceljet.net/formulas/calculate-original-loan-amount)

### [Calculate original loan amount](https://exceljet.net/formulas/calculate-original-loan-amount)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term), and the payment amount per period. One use of the PV function is to calculate the original loan amount, when given the other 3 components. For this example, we want to find the...

[![Excel formula: Calculate payment for a loan](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20payment%20for%20a%20loan.png "Excel formula: Calculate payment for a loan")](https://exceljet.net/formulas/calculate-payment-for-a-loan)

### [Calculate payment for a loan](https://exceljet.net/formulas/calculate-payment-for-a-loan)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term) and a payment amount per period. You can use the PMT function to get the payment when you have the other 3 components. For this example, we want to find the payment for a $5000 loan...

[![Excel formula: Calculate payment periods for loan](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20payment%20periods%20for%20loan.png "Excel formula: Calculate payment periods for loan")](https://exceljet.net/formulas/calculate-payment-periods-for-loan)

### [Calculate payment periods for loan](https://exceljet.net/formulas/calculate-payment-periods-for-loan)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term) and a payment amount per period. One use of the NPER function is to calculate the number of periodic payments for loan. For this example, we want to calculate the number of payments...

Related functions
-----------------

[![Excel PPMT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ppmt_function.png "Excel PPMT function")](https://exceljet.net/functions/ppmt-function)

### [PPMT Function](https://exceljet.net/functions/ppmt-function)

The Excel PPMT function can be used to calculate the principal portion of a given loan payment. For example, you can use PPMT to calculate the principal amount of a payment for the first period, the last period, or any period in between.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate principal for given period](https://exceljet.net/formulas/calculate-principal-for-given-period)
    
*   [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)
    
*   [Calculate interest rate for loan](https://exceljet.net/formulas/calculate-interest-rate-for-loan)
    
*   [Calculate original loan amount](https://exceljet.net/formulas/calculate-original-loan-amount)
    
*   [Calculate payment for a loan](https://exceljet.net/formulas/calculate-payment-for-a-loan)
    
*   [Calculate payment periods for loan](https://exceljet.net/formulas/calculate-payment-periods-for-loan)
    

### Functions

*   [PPMT Function](https://exceljet.net/functions/ppmt-function)
    

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)