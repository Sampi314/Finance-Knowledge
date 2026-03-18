# Calculate interest rate for loan - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-interest-rate-for-loan

---

[Skip to main content](https://exceljet.net/formulas/calculate-interest-rate-for-loan#main-content)

[](https://exceljet.net/formulas/calculate-interest-rate-for-loan#)

*   [Previous](https://exceljet.net/formulas/calculate-interest-for-given-period)
    
*   [Next](https://exceljet.net/formulas/calculate-loan-interest-in-given-year)
    

[Financial](https://exceljet.net/formulas#Financial)

Calculate interest rate for loan
================================

by Dave Bruns · Updated 2 Nov 2021

Related functions 
------------------

[RATE](https://exceljet.net/functions/rate-function)

![Excel formula: Calculate interest rate for loan](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate%20interest%20rate%20for%20loan.png "Excel formula: Calculate interest rate for loan")

Summary
-------

To calculate the periodic interest rate for a loan, given the loan amount, the number of payment periods, and the payment amount, you can use the [RATE function](https://exceljet.net/functions/rate-function)
. In the example shown, the formula in C10 is:

    =RATE(C7,C6,-C5)*12

Generic formula
---------------

    =RATE(periods,-payment,amount)*12

Explanation 
------------

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term) and a payment amount per period. One use of the [RATE function](https://exceljet.net/formulas/calculate-interest-rate-for-loan)
 is to calculate the periodic interest rate when the amount, number of payment periods, and payment amount are known.

In this example, we want to calculate the annual interest rate for 5-year, $5000 loan, and with monthly payments of $93.22. The RATE function is used like this:

    =RATE(C7,-C6,C5)*C8
    

The function arguments are configured as follows:

_nper_ - The number of periods is 60 (5 \* 12), and comes from cell C7.

_pmt_ - The payment is $93.22, and comes from cell C6. Note _pmt_ is input as a negative value. In annuity functions, cash paid out is represented by a negative number. Note: If pmt is not provided, the optional fv argument must be supplied.

_pv_ - The present value is $5000, and comes from C5. 

With these inputs, the RATE function returns 0.375%, which is the periodic interest rate. To get an annual interest rate, we multiply by 12:

    =RATE(C7,C6,-C5)*12
    =0.003751*12
    =0.0450
    

With the [percent number format](https://exceljet.net/glossary/percentage-number-format)
 applied to cell C10, the result is displayed as 4.50%.

Related formulas
----------------

[![Excel formula: Calculate compound interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20compound%20interest.png "Excel formula: Calculate compound interest")](https://exceljet.net/formulas/calculate-compound-interest)

### [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)

Compound interest is a financial concept that describes how an initial investment grows over time, taking into account not only the interest earned on the initial amount but also the interest earned on the interest itself. Compound interest allows your money to grow exponentially, which makes it a...

[![Excel formula: Calculate payment periods for loan](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20payment%20periods%20for%20loan.png "Excel formula: Calculate payment periods for loan")](https://exceljet.net/formulas/calculate-payment-periods-for-loan)

### [Calculate payment periods for loan](https://exceljet.net/formulas/calculate-payment-periods-for-loan)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term) and a payment amount per period. One use of the NPER function is to calculate the number of periodic payments for loan. For this example, we want to calculate the number of payments...

[![Excel formula: Calculate original loan amount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20original%20loan%20amount.png "Excel formula: Calculate original loan amount")](https://exceljet.net/formulas/calculate-original-loan-amount)

### [Calculate original loan amount](https://exceljet.net/formulas/calculate-original-loan-amount)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term), and the payment amount per period. One use of the PV function is to calculate the original loan amount, when given the other 3 components. For this example, we want to find the...

[![Excel formula: Calculate payment for a loan](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20payment%20for%20a%20loan.png "Excel formula: Calculate payment for a loan")](https://exceljet.net/formulas/calculate-payment-for-a-loan)

### [Calculate payment for a loan](https://exceljet.net/formulas/calculate-payment-for-a-loan)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term) and a payment amount per period. You can use the PMT function to get the payment when you have the other 3 components. For this example, we want to find the payment for a $5000 loan...

Related functions
-----------------

[![Excel RATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rate%20function.png "Excel RATE function")](https://exceljet.net/functions/rate-function)

### [RATE Function](https://exceljet.net/functions/rate-function)

The Excel RATE function is a financial function that returns the interest rate per period of an annuity. You can use RATE to calculate the periodic interest rate, then multiply as required to derive the annual interest rate. The RATE function calculates by iteration.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)
    
*   [Calculate payment periods for loan](https://exceljet.net/formulas/calculate-payment-periods-for-loan)
    
*   [Calculate original loan amount](https://exceljet.net/formulas/calculate-original-loan-amount)
    
*   [Calculate payment for a loan](https://exceljet.net/formulas/calculate-payment-for-a-loan)
    

### Functions

*   [RATE Function](https://exceljet.net/functions/rate-function)
    

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