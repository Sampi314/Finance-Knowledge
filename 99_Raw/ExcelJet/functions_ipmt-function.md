# Excel IPMT function | Exceljet

**Source:** https://exceljet.net/functions/ipmt-function

---

[Skip to main content](https://exceljet.net/functions/ipmt-function#main-content)

[](https://exceljet.net/functions/ipmt-function#)

*   [Previous](https://exceljet.net/functions/intrate-function)
    
*   [Next](https://exceljet.net/functions/irr-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

IPMT Function
=============

by Dave Bruns · Updated 4 Jan 2024

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

![Excel IPMT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_ipmt_function.png "Excel IPMT function")

Summary
-------

The Excel IPMT function is a financial function used to calculate the interest payment for a given period of an investment or a loan, based on constant periodic payments and a constant interest rate. For example, you can use IPMT to get the interest amount of a loan payment for the first period, the last period, or any period in between.

Purpose 
--------

Get interest in given period

Return value 
-------------

The interest amount

Syntax
------

    =IPMT(rate,per,nper,pv,[fv],[type])

*   _rate_ - The interest rate per period.
*   _per_ - The given payment period.
*   _nper_ - The total number of payment periods.
*   _pv_ - The present value, or total value of all payments now.
*   _fv_ - \[optional\] The cash balance desired after last payment is made. Defaults to 0.
*   _type_ - \[optional\] When payments are due. 0 = end of period. 1 = beginning of period. Default is 0.

Using the IPMT function 
------------------------

The IPMT function returns the interest payment for a given payment period of an investment or a loan, based on constant periodic payments and a constant interest rate. IPMT takes six arguments, four of which are required:

    =IPMT(rate,per,nper,pv,[fv],[type])

Each argument has the following meaning:

*   _rate_ - the interest rate per period. Typically, this is the annual interest rate divided by the compounding periods per year.
*   _per_ - the payment period of interest as a number (e.g. 1, 2, 3, etc.)
*   _nper_ - The total number of payment periods for the loan or investment.
*   _pv_ -  The present value, or the principal amount of the loan or investment.
*   _fv_ - Optional. The desired future value, or a cash balance after the last payment (defaults to 0)
*   _type_ - Optional. The timing of the payment: 0 = end of period (default), 1 = beginning of the period.

### Example #1 - hardcoded values

Suppose you have a 5-year loan of $10,000 with an annual interest rate of 5% and 12 compounding periods per year. You want to find out the amount of interest paid in period 1. You can determine this amount with the IPMT function like this:

    =IPMT(5%/12,1,60,-10000)

The inputs to IPMT are as follows:

*   _rate_ - 5%/12 = 0.00416 (annual interest rate with monthly compounding)
*   _per_ - 1 (interest for period 1)
*   _nper_ - 60 (a 5-year loan has 60 periods)
*   _pv_ - -10,000 (the loan amount is negative to yield a positive result)
*   _fv_ - Omitted. Defaults to 0.
*   _type_ - Omitted. Defaults to 0.

The result is 41.67. This is the interest payment for period 1 of the loan. Notice we have provided the loan balance as a negative value to get a positive result from IPMT. If we provide 10,000 as a positive number, IPMT will return -41.67. The decision to use a positive or negative value for _pv_ depends on the specific scenario.

### Example #2 - worksheet formula

In the example above, all inputs to IPMT are hardcoded to make the formula easier to read. More typically, the inputs will come from cell references. The screen below shows how the same example can be transferred to a worksheet:

![Example of using IPMT to calculate interest for period 1](https://exceljet.net/sites/default/files/images/functions/inline/excel_ipmt_function_example.png "Example of using IPMT to calculate interest for period 1")

The formula in cell C10 is evaluated like this:

    =IPMT(C5/C7,1,C6*C7,-C4)
    =IPMT(0.05/12,1,5*12,-10000)
    =IPMT(0.004167,1,60,-10000)
    41.67

Notice that we provide years \* periods per year for _nper_ instead of hardcoding the number 60. We do this so that the formula will automatically adapt to a loan with a different term in years, or a loan with a different number of periods per year.

Also, notice that the monthly payment is not an input to IPMT. This is because IPMT calculates interest based on the original principal (or present value), the interest rate, and the number of periods. The payment amount isn't needed. To calculate the payment for a loan you can use the [PMT function](https://exceljet.net/functions/pmt-function)
.

### Notes

1.  Use the [PPMT function](https://exceljet.net/functions/ppmt-function)
     to get the principal portion of a loan payment for a given period.
2.  The interest rate can be provided as a [percentage](https://exceljet.net/glossary/percentage-number-format)
     like 5% or a decimal number like 0.05.
3.  Be careful to provide the _periodic_ interest rate for _rate_. For example, 5%/12 or 0.05/12.
4.  The loan value (_pv_) can be entered as a positive value or a negative value. 
5.  The value for period (_per)_ must be in the range 1 to _nper_.

IPMT function examples
----------------------

[![Excel formula: Mortgage payment schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/mortgage_schedule_with_extra_payment.png "Excel formula: Mortgage payment schedule")](https://exceljet.net/formulas/mortgage-payment-schedule)

### [Mortgage payment schedule](https://exceljet.net/formulas/mortgage-payment-schedule)

The goal of this example is to show how to create a mortgage payment schedule using Excel formulas. A mortgage payment schedule is a detailed breakdown of every payment over the life of a loan. Each payment represents one period , typically a month. For each period, the schedule shows how much of...

[![Excel formula: Calculate principal for given period](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate%20principal%20for%20given%20period.png "Excel formula: Calculate principal for given period")](https://exceljet.net/formulas/calculate-principal-for-given-period)

### [Calculate principal for given period](https://exceljet.net/formulas/calculate-principal-for-given-period)

For this example, we want to calculate the principal portion for payment 1 of a 5-year loan of $5,000 with an interest rate of 4.5%. To do this, we set up PPMT like this: rate - The interest rate per period. We divide the value in C6 by 12 since 4.5% represents annual interest: =C6/12 per - the...

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

*   [Calculate principal for given period](https://exceljet.net/formulas/calculate-principal-for-given-period)
    
*   [Mortgage payment schedule](https://exceljet.net/formulas/mortgage-payment-schedule)
    

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

*   [Microsoft IPMT function documentation](https://support.office.com/en-us/article/ipmt-function-5cce0ad6-8402-4a41-8d29-61a0b054cb6f)
    

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