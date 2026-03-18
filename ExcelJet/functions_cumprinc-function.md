# Excel CUMPRINC function | Exceljet

**Source:** https://exceljet.net/functions/cumprinc-function

---

[Skip to main content](https://exceljet.net/functions/cumprinc-function#main-content)

[](https://exceljet.net/functions/cumprinc-function#)

*   [Previous](https://exceljet.net/functions/cumipmt-function)
    
*   [Next](https://exceljet.net/functions/db-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

CUMPRINC Function
=================

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[FV](https://exceljet.net/functions/fv-function)

[PV](https://exceljet.net/functions/pv-function)

[RATE](https://exceljet.net/functions/rate-function)

[NPER](https://exceljet.net/functions/nper-function)

[PMT](https://exceljet.net/functions/pmt-function)

[PPMT](https://exceljet.net/functions/ppmt-function)

[IPMT](https://exceljet.net/functions/ipmt-function)

[CUMPRINC](https://exceljet.net/functions/cumprinc-function)

[CUMIPMT](https://exceljet.net/functions/cumipmt-function)

![Excel CUMPRINC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_cumprinc_function.png "Excel CUMPRINC function")

Summary
-------

The Excel CUMPRINC function is a financial function that returns the cumulative principal paid on a loan between a start period and an end period. You can use CUMPRINC to calculate and verify the total principal paid on a loan, or the principal paid between any two payment periods.

Purpose 
--------

Get cumulative principal paid on a loan

Return value 
-------------

The principal amount

Syntax
------

    =CUMPRINC(rate,nper,pv,start_period,end_period,type)

*   _rate_ - The interest rate per period.
*   _nper_ - The total number of payments for the loan.
*   _pv_ - The present value, or total value of all payments now.
*   _start\_period_ - First payment in calculation.
*   _end\_period_ - Last payment in calculation.
*   _type_ - When payments are due. 0 = end of period. 1 = beginning of period.

Using the CUMPRINC function 
----------------------------

The CUMPRINC function calculates the cumulative principal amount paid over a specified range of time, defined by the start and end periods of a loan. This function is important for financial analysis, particularly in managing loans and amortization schedules. By calculating the principal portion of loan payments over specific periods, the CUMPRINC function provides useful insights into loan dynamics and helps show the trajectory of loan repayment over time. Typical use cases include evaluating the principal repayment structure of mortgages over various durations, analyzing the principal component in different loan offers, or planning financial budgets. 

### Example

Assume a 5-year loan for $10,000 with an annual interest rate of 5%. Payments are monthly and there are 12 compounding periods per year. You want to confirm the total principal paid over the full term of the loan. You can calculate the total principal paid with the CUMPRINC function like this:

    =CUMPRINC(5%/12,5*12,10000,1,5*12,0)

The inputs to CUMPRINC are as follows:

*   _rate_ = 5%/12 = 0.00416 (the annual interest rate divided by 12)
*   _nper_ = 5\*12 = 60 (a 5-year loan has 60 periods)
*   _pv_ = 10,000 (the loan amount)
*   _start\_period_ = 1 (the first period)
*   _end\_period_ = 60 (the last period)
*   _type_ = 0 (payments at the end of each month)

The result is -10,000, which is the total principal paid over the full term of the loan. As expected, this is the original loan amount. The CUMPRINC returns a negative value because it represents an outflow of money. If you need a positive value, you can wrap the formula in the [ABS function](https://exceljet.net/functions/abs-function)
 like this:

    =ABS(CUMPRINC(5%/12,5*12,10000,1,5*12,0))

### Worksheet example

In the example above, all inputs to CUMPRINC are hardcoded to make the formula easier to read. In most cases, however, the main inputs will come from cell references. The screen below shows the same example can be set up in a worksheet:

![How to use the CUMIPMT function to calculate the total principal paid on a loan](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_cumprinc_function_example.png "How to use the CUMIPMT function to calculate the total principal paid on a loan")

The formula in cell C10 is evaluated like this:

    =CUMPRINC(C5/C7,C6*C7,C4,1,C6*C7,0)
    =CUMPRINC(0.05/12,5*12,10000,1,5*12,0)
    =CUMPRINC(0.0041667,60,10000,1,60,0)
    =-10000

Notice that we provide the _term_ as years \* periods per year, instead of hardcoding the number 60 into the formula. Excel then calculates a value of 60 for _nper_ before the CUMPRINC function runs. One reason to do it this way is to let Excel handle the math and provide a reminder of how we are deriving _nper_. More importantly, this also makes it possible for the formula to automatically adapt to a loan with a different term or a loan with a different number of compounding periods per year.

Also, notice that the monthly payment is not an input to CUMPRINC. This is because Excel can determine the regular payment amount based on the interest rate, number of periods, and principal amount. Excel calculates the interest due for a period and subtracts this amount from the payment to determine the principal payment.  To calculate a payment for a loan directly you can use the [PMT function](https://exceljet.net/functions/pmt-function)
.

### Notes

1.  The interest rate can be provided as a [percentage](https://exceljet.net/glossary/percentage-number-format)
     like 5% or a decimal number like 0.05.
2.  Be consistent with inputs for rate. For example, for a 5-year loan with 6% annual interest, enter the rate as 6%/12.
3.  The loan value (_pv_) must be entered as a positive value or CUMPRINC will return a #NUM! error.
4.  The values for _start\_period_ and _end\_period_ should be integers between 1 and the total number of periods.
5.  The value for _start\_period_ must be less than or equal to the value for _end\_period_.

CUMPRINC function examples
--------------------------

[![Excel formula: Calculate cumulative loan principal payments](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate%20cumulative%20loan%20principal%20payments.png "Excel formula: Calculate cumulative loan principal payments")](https://exceljet.net/formulas/calculate-cumulative-loan-principal-payments)

### [Calculate cumulative loan principal payments](https://exceljet.net/formulas/calculate-cumulative-loan-principal-payments)

For this example, we want to calculate cumulative principal payments over the full term of a 5-year loan of $5,000 with an interest rate of 4.5%. To do this, we set up CUMPRINC like this: rate - The interest rate per period. We divide the value in C6 by 12 since 4.5% represents annual interest: =C6...

Related functions
-----------------

[![Excel FV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_fv.png "Excel FV function")](https://exceljet.net/functions/fv-function)

### [FV Function](https://exceljet.net/functions/fv-function)

The Excel FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate.

[![Excel PV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pv%20function.png "Excel PV function")](https://exceljet.net/functions/pv-function)

### [PV Function](https://exceljet.net/functions/pv-function)

The Excel PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate.

[![Excel RATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rate%20function.png "Excel RATE function")](https://exceljet.net/functions/rate-function)

### [RATE Function](https://exceljet.net/functions/rate-function)

The Excel RATE function is a financial function that returns the interest rate per period of an annuity. You can use RATE to calculate the periodic interest rate, then multiply as required to derive the annual interest rate. The RATE function calculates by iteration.

[![Excel NPER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_nper.png "Excel NPER function")](https://exceljet.net/functions/nper-function)

### [NPER Function](https://exceljet.net/functions/nper-function)

The Excel NPER function is a financial function that returns the number of periods for a loan or investment. You can use the NPER function to get the number of payment periods for a loan, given the amount, the interest rate, and periodic payment amount.

[![Excel PMT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_pmt.png "Excel PMT function")](https://exceljet.net/functions/pmt-function)

### [PMT Function](https://exceljet.net/functions/pmt-function)

The Excel PMT function is a financial function that returns the periodic payment for a loan. You can use the PMT function to figure out payments for a loan, given the loan amount, number of periods, and interest rate.

[![Excel PPMT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ppmt_function.png "Excel PPMT function")](https://exceljet.net/functions/ppmt-function)

### [PPMT Function](https://exceljet.net/functions/ppmt-function)

The Excel PPMT function can be used to calculate the principal portion of a given loan payment. For example, you can use PPMT to calculate the principal amount of a payment for the first period, the last period, or any period in between.

[![Excel IPMT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ipmt_function.png "Excel IPMT function")](https://exceljet.net/functions/ipmt-function)

### [IPMT Function](https://exceljet.net/functions/ipmt-function)

The Excel IPMT function is a financial function used to calculate the interest payment for a given period of an investment or a loan, based on constant periodic payments and a constant interest rate. For example, you can use IPMT to get the interest amount of a loan payment for the...

[![Excel CUMPRINC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_cumprinc_function.png "Excel CUMPRINC function")](https://exceljet.net/functions/cumprinc-function)

### [CUMPRINC Function](https://exceljet.net/functions/cumprinc-function)

The Excel CUMPRINC function is a financial function that returns the cumulative principal paid on a loan between a start period and an end period. You can use CUMPRINC to calculate and verify the total principal paid on a loan, or the principal paid between any two payment periods.

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

*   [Calculate cumulative loan principal payments](https://exceljet.net/formulas/calculate-cumulative-loan-principal-payments)
    

### Functions

*   [FV Function](https://exceljet.net/functions/fv-function)
    
*   [PV Function](https://exceljet.net/functions/pv-function)
    
*   [RATE Function](https://exceljet.net/functions/rate-function)
    
*   [NPER Function](https://exceljet.net/functions/nper-function)
    
*   [PMT Function](https://exceljet.net/functions/pmt-function)
    
*   [PPMT Function](https://exceljet.net/functions/ppmt-function)
    
*   [IPMT Function](https://exceljet.net/functions/ipmt-function)
    
*   [CUMPRINC Function](https://exceljet.net/functions/cumprinc-function)
    
*   [CUMIPMT Function](https://exceljet.net/functions/cumipmt-function)
    

### Links

*   [Microsoft CUMPRINC function documentation](https://support.office.com/en-us/article/cumprinc-function-94a4516d-bd65-41a1-bc16-053a6af4c04d)
    

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