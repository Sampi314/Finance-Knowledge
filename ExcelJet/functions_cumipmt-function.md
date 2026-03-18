# Excel CUMIPMT function | Exceljet

**Source:** https://exceljet.net/functions/cumipmt-function

---

[Skip to main content](https://exceljet.net/functions/cumipmt-function#main-content)

[](https://exceljet.net/functions/cumipmt-function#)

*   [Previous](https://exceljet.net/functions/couppcd-function)
    
*   [Next](https://exceljet.net/functions/cumprinc-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

CUMIPMT Function
================

by Dave Bruns · Updated 11 Nov 2023

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

![Excel CUMIPMT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_cumipmt_function.png "Excel CUMIPMT function")

Summary
-------

The Excel CUMIPMT function is a financial function that returns the cumulative interest paid on a loan between a start period and an end period. You can use CUMIPMT to determine the total interest paid on a loan, or the interest paid between any two payment periods.

Purpose 
--------

Get cumulative interest paid on a loan

Return value 
-------------

The interest amount

Syntax
------

    =CUMIPMT(rate,nper,pv,start_period,end_period,type)

*   _rate_ - The interest rate per period.
*   _nper_ - The total number of payments for the loan.
*   _pv_ - The present value, or total value of all payments now.
*   _start\_period_ - First payment in calculation.
*   _end\_period_ - Last payment in calculation.
*   _type_ - When payments are due. 0 = end of period. 1 = beginning of period.

Using the CUMIPMT function 
---------------------------

The CUMIPMT function returns the cumulative interest over a range of time defined by a given start and end period. CUMIPMT is useful for financial analysis, particularly in scenarios involving loans and investments. It allows users to calculate the cumulative interest over specific periods, which makes it an important tool for understanding the financial impact of different loan terms or investment strategies. Typical use cases include assessing the total interest outlay on mortgages over various time frames, comparing interest accruals on different loan offers, or analyzing investment growth over time. The CUMIPMT function provides a useful view of financial obligations or growth which can help with more informed decision-making and effective financial planning

### Example

Suppose you have a 5-year loan of $10,000 with an annual interest rate of 5% and 12 compounding periods per year. You want to find out the total interest you would pay over the full term of the loan. You can make this calculation with the CUMIPMT function like this:

    =CUMIPMT(5%/12,5*12,10000,1,5*12,0)

The inputs to CUMIPMT are as follows:

*   _rate_ = 5%/12 = 0.00416 (since it's an annual interest rate with monthly compounding)
*   _nper_ = 5\*12 = 60 (a 5-year loan has 60 periods)
*   _pv_ = 10,000 (the loan amount)
*   _start\_period_ = 1 (the first period)
*   _end\_period_ = 60 (the last period)
*   _type_ = 0 (payments at the end of each month)

The result is -1,322.74. This is the total interest paid over the full term of the loan. Notice that the CUMIPMT function in Excel returns a negative value because it represents an outflow of money. If you need a positive value, you can wrap the formula in the [ABS function](https://exceljet.net/functions/abs-function)
.

### Worksheet example

In the example above, all inputs to CUMIPMT are hardcoded to make the formula easier to read. More typically, the inputs will come from cell references. The screen below shows the same example transferred to a worksheet:

![Example of the CUMIPMT function to calculate total interest paid](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_cumipmt_function_example.png "Example of the CUMIPMT function to calculate total interest paid")

The formula in cell C10 is evaluated like this:

    =CUMIPMT(C5/C7,C6*C7,C4,1,C6*C7,0)
    =CUMIPMT(0.05/12,5*12,10000,1,5*12,0)
    =CUMIPMT(0.0041667,60,10000,1,60,0)
    -1322.75

Notice that we use the term in years \* the periods per year to calculate total periods, instead of hardcoding the number 60. We do this so that the formula will automatically adapt to a different number of compounding periods per year.

Also, notice that the monthly payment is not an input to CUMIPMT. This is because CUMIPMT calculates cumulative interest based on the original principal (or present value), the interest rate, and the provided periods. The periodic (e.g., monthly) payment amount isn't needed to determine how much interest accumulates across the given period range. To calculate a payment for a loan you can use the [PMT function](https://exceljet.net/functions/pmt-function)
.

### Notes

1.  The interest rate can be provided as a [percentage](https://exceljet.net/glossary/percentage-number-format)
     like 5% or a decimal number like 0.05.
2.  Be consistent with inputs for rate. For example, for a 5-year loan with 6% annual interest, enter the rate as 6%/12.
3.  The loan value (_pv_) must be entered as a positive value or CUMIPMT will return a #NUM! error.
4.  The values for _start\_period_ and _end\_period_ should be integers between 1 and the total number of periods.
5.  The value for _start\_period_ must be less than or equal to the value for _end\_period_.

CUMIPMT function examples
-------------------------

[![Excel formula: Calculate loan interest in given year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20loan%20interest%20in%20given%20year.png "Excel formula: Calculate loan interest in given year")](https://exceljet.net/formulas/calculate-loan-interest-in-given-year)

### [Calculate loan interest in given year](https://exceljet.net/formulas/calculate-loan-interest-in-given-year)

For this example, we want to calculate the interest paid during each year in a 5-year loan of $30,000 with an interest rate of 5%. To do this, we set up CUMIPMT like this: rate - The interest rate per period. We divide 5% by 12 because 5% represents annual interest. nper - the total number of...

[![Excel formula: Calculate cumulative loan interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate%20cumulative%20loan%20interest.png "Excel formula: Calculate cumulative loan interest")](https://exceljet.net/formulas/calculate-cumulative-loan-interest)

### [Calculate cumulative loan interest](https://exceljet.net/formulas/calculate-cumulative-loan-interest)

For this example, we want to calculate cumulative interest over the full term of a 5-year loan of $5,000 with an interest rate of 4.5%. To do this, we set up CUMIPMT like this: rate - The interest rate per period. We divide the value in C6 by 12 since 4.5% represents annual interest: =C6/12 nper -...

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

*   [Calculate cumulative loan interest](https://exceljet.net/formulas/calculate-cumulative-loan-interest)
    
*   [Calculate loan interest in given year](https://exceljet.net/formulas/calculate-loan-interest-in-given-year)
    

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

*   [Microsoft CUMIPMT function documentation](https://support.office.com/en-us/article/cumipmt-function-61067bb0-9016-427d-b95b-1a752af0e606)
    

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