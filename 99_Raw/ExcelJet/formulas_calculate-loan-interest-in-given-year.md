# Calculate loan interest in given year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-loan-interest-in-given-year

---

[Skip to main content](https://exceljet.net/formulas/calculate-loan-interest-in-given-year#main-content)

[](https://exceljet.net/formulas/calculate-loan-interest-in-given-year#)

*   [Previous](https://exceljet.net/formulas/calculate-interest-rate-for-loan)
    
*   [Next](https://exceljet.net/formulas/calculate-original-loan-amount)
    

[Financial](https://exceljet.net/formulas#Financial)

Calculate loan interest in given year
=====================================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[CUMIPMT](https://exceljet.net/functions/cumipmt-function)

![Excel formula: Calculate loan interest in given year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate%20loan%20interest%20in%20given%20year.png "Excel formula: Calculate loan interest in given year")

Summary
-------

To calculate the total interest for a loan in a given year, you can use the CUMIPMT function. In the example shown, the total interest paid in year 1 is calculated by using 1 for the start period and 12 for the end period. The formula in F5 is:

    =CUMIPMT(5%/12,60,30000,1,12,0)
    

_Note: values are hardcoded for readability only._

Generic formula
---------------

    =CUMIPMT(rate,nper,pv,start,end,type)

Explanation 
------------

For this example, we want to calculate the interest paid during each year in a 5-year loan of $30,000 with an interest rate of 5%. To do this, we set up CUMIPMT like this:

*   **rate** - The interest rate per period. We divide 5% by 12 because 5% represents annual interest.
*   **nper** - the total number of payment periods for the loan, 60.
*   **pv** - The present value, or total value of all payments now, 30000.
*   **start\_period** - the starting period for a given year.
*   **end\_period** - the ending period for a given year.

In the range F5:F9, here are the formulas used:

    =CUMIPMT(5%/12,60,30000,1,12,0) // year 1
    =CUMIPMT(5%/12,60,30000,13,24,0) // year 2
    =CUMIPMT(5%/12,60,30000,25,36,0) // year 3
    =CUMIPMT(5%/12,60,30000,37,48,0) // year 4
    =CUMIPMT(5%/12,60,30000,49,60,0) // year 5
    

Note many values could be picked up directly with cell references, but are hardcoded in this example for readability.

### Other periods

In this example, we are calculating interest by year, so periods are set up accordingly. However, you can adjust periods to calculate interest in any timeframe desired.

Related formulas
----------------

[![Excel formula: Calculate interest for given period](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate%20interest%20for%20given%20period.png "Excel formula: Calculate interest for given period")](https://exceljet.net/formulas/calculate-interest-for-given-period)

### [Calculate interest for given period](https://exceljet.net/formulas/calculate-interest-for-given-period)

For this example, we want to calculate the interest portion for payment 1 of a 5-year loan of $5,000 with an interest rate of 4.5%. To do this, we set up PPMT like this: rate - The interest rate per period. We divide the value in C6 by 12 since 4.5% represents annual interest: =C6/12 per - the...

[![Excel formula: Calculate principal for given period](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate%20principal%20for%20given%20period.png "Excel formula: Calculate principal for given period")](https://exceljet.net/formulas/calculate-principal-for-given-period)

### [Calculate principal for given period](https://exceljet.net/formulas/calculate-principal-for-given-period)

For this example, we want to calculate the principal portion for payment 1 of a 5-year loan of $5,000 with an interest rate of 4.5%. To do this, we set up PPMT like this: rate - The interest rate per period. We divide the value in C6 by 12 since 4.5% represents annual interest: =C6/12 per - the...

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

[![Excel formula: Calculate cumulative loan principal payments](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate%20cumulative%20loan%20principal%20payments.png "Excel formula: Calculate cumulative loan principal payments")](https://exceljet.net/formulas/calculate-cumulative-loan-principal-payments)

### [Calculate cumulative loan principal payments](https://exceljet.net/formulas/calculate-cumulative-loan-principal-payments)

For this example, we want to calculate cumulative principal payments over the full term of a 5-year loan of $5,000 with an interest rate of 4.5%. To do this, we set up CUMPRINC like this: rate - The interest rate per period. We divide the value in C6 by 12 since 4.5% represents annual interest: =C6...

Related functions
-----------------

[![Excel CUMIPMT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_cumipmt_function.png "Excel CUMIPMT function")](https://exceljet.net/functions/cumipmt-function)

### [CUMIPMT Function](https://exceljet.net/functions/cumipmt-function)

The Excel CUMIPMT function is a financial function that returns the cumulative interest paid on a loan between a start period and an end period. You can use CUMIPMT to determine the total interest paid on a loan, or the interest paid between any two payment periods.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate interest for given period](https://exceljet.net/formulas/calculate-interest-for-given-period)
    
*   [Calculate principal for given period](https://exceljet.net/formulas/calculate-principal-for-given-period)
    
*   [Calculate interest rate for loan](https://exceljet.net/formulas/calculate-interest-rate-for-loan)
    
*   [Calculate original loan amount](https://exceljet.net/formulas/calculate-original-loan-amount)
    
*   [Calculate payment for a loan](https://exceljet.net/formulas/calculate-payment-for-a-loan)
    
*   [Calculate payment periods for loan](https://exceljet.net/formulas/calculate-payment-periods-for-loan)
    
*   [Calculate cumulative loan principal payments](https://exceljet.net/formulas/calculate-cumulative-loan-principal-payments)
    

### Functions

*   [CUMIPMT Function](https://exceljet.net/functions/cumipmt-function)
    

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