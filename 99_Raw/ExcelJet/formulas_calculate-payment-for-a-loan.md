# Calculate payment for a loan - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-payment-for-a-loan

---

[Skip to main content](https://exceljet.net/formulas/calculate-payment-for-a-loan#main-content)

[](https://exceljet.net/formulas/calculate-payment-for-a-loan#)

*   [Previous](https://exceljet.net/formulas/calculate-original-loan-amount)
    
*   [Next](https://exceljet.net/formulas/calculate-payment-periods-for-loan)
    

[Financial](https://exceljet.net/formulas#Financial)

Calculate payment for a loan
============================

by Dave Bruns · Updated 27 Jun 2022

Related functions 
------------------

[PMT](https://exceljet.net/functions/pmt-function)

![Excel formula: Calculate payment for a loan](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate%20payment%20for%20a%20loan.png "Excel formula: Calculate payment for a loan")

Summary
-------

To calculate a loan payment amount, given an interest rate, the loan term, and the loan amount, you can use the [PMT function](https://exceljet.net/functions/pmt-function)
. In the example shown, the formula in C10 is:

    =PMT(C6/12,C7,-C5)
    

Generic formula
---------------

    =PMT(rate,periods,-amount)

Explanation 
------------

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term) and a payment amount per period. You can use the PMT function to get the payment when you have the other 3 components.

For this example, we want to find the payment for a $5000 loan with a 4.5% interest rate, and a term of 60 months. To do this, we configure the PMT function as follows:

**rate** - The interest rate per period. We divide the value in C6 by 12 since 4.5% represents annual interest, and we need the periodic interest.

**nper** - the number of periods comes from cell C7; 60 monthly periods for a 5 year loan.

**pv** - the loan amount comes from C5. We use the minus operator to make this value negative, since a loan represents money owed.

With these inputs, the PMT function returns 93.215, rounded to $92.22 in the example using the currency [number format](https://exceljet.net/glossary/number-format)
.

Related formulas
----------------

[![Excel formula: Calculate compound interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20compound%20interest.png "Excel formula: Calculate compound interest")](https://exceljet.net/formulas/calculate-compound-interest)

### [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)

Compound interest is a financial concept that describes how an initial investment grows over time, taking into account not only the interest earned on the initial amount but also the interest earned on the interest itself. Compound interest allows your money to grow exponentially, which makes it a...

[![Excel formula: Calculate interest rate for loan](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20interest%20rate%20for%20loan.png "Excel formula: Calculate interest rate for loan")](https://exceljet.net/formulas/calculate-interest-rate-for-loan)

### [Calculate interest rate for loan](https://exceljet.net/formulas/calculate-interest-rate-for-loan)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term) and a payment amount per period. One use of the RATE function is to calculate the periodic interest rate when the amount, number of payment periods, and payment amount are known. In...

[![Excel formula: Calculate payment periods for loan](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20payment%20periods%20for%20loan.png "Excel formula: Calculate payment periods for loan")](https://exceljet.net/formulas/calculate-payment-periods-for-loan)

### [Calculate payment periods for loan](https://exceljet.net/formulas/calculate-payment-periods-for-loan)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term) and a payment amount per period. One use of the NPER function is to calculate the number of periodic payments for loan. For this example, we want to calculate the number of payments...

[![Excel formula: Calculate original loan amount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20original%20loan%20amount.png "Excel formula: Calculate original loan amount")](https://exceljet.net/formulas/calculate-original-loan-amount)

### [Calculate original loan amount](https://exceljet.net/formulas/calculate-original-loan-amount)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term), and the payment amount per period. One use of the PV function is to calculate the original loan amount, when given the other 3 components. For this example, we want to find the...

Related functions
-----------------

[![Excel PMT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_pmt.png "Excel PMT function")](https://exceljet.net/functions/pmt-function)

### [PMT Function](https://exceljet.net/functions/pmt-function)

The Excel PMT function is a financial function that returns the periodic payment for a loan. You can use the PMT function to figure out payments for a loan, given the loan amount, number of periods, and interest rate.

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
    
*   [Calculate interest rate for loan](https://exceljet.net/formulas/calculate-interest-rate-for-loan)
    
*   [Calculate payment periods for loan](https://exceljet.net/formulas/calculate-payment-periods-for-loan)
    
*   [Calculate original loan amount](https://exceljet.net/formulas/calculate-original-loan-amount)
    

### Functions

*   [PMT Function](https://exceljet.net/functions/pmt-function)
    

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