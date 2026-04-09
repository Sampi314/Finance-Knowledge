# Excel RATE function | Exceljet

**Source:** https://exceljet.net/functions/rate-function

---

[Skip to main content](https://exceljet.net/functions/rate-function#main-content)

[](https://exceljet.net/functions/rate-function#)

*   [Previous](https://exceljet.net/functions/pv-function)
    
*   [Next](https://exceljet.net/functions/received-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

RATE Function
=============

by Dave Bruns · Updated 6 Jun 2024

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

![Excel RATE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20rate%20function.png "Excel RATE function")

Summary
-------

The Excel RATE function is a financial function that returns the interest rate per period of an annuity. You can use RATE to calculate the periodic interest rate, then multiply as required to derive the annual interest rate. The RATE function calculates by iteration.

Purpose 
--------

Get the interest rate per period of an annuity

Return value 
-------------

The interest rate per period

Syntax
------

    =RATE(nper,pmt,pv,[fv],[type],[guess])

*   _nper_ - The total number of payment periods.
*   _pmt_ - The payment made each period.
*   _pv_ - The present value, or total value of all loan payments now.
*   _fv_ - \[optional\] The future value, or desired cash balance after last payment. Default is 0.
*   _type_ - \[optional\] When payments are due. 0 = end of period. 1 = beginning of period. Default is 0.
*   _guess_ - \[optional\] Your guess on the rate. Default is 10%.

Using the RATE function 
------------------------

The RATE function returns the interest rate per period of an annuity. You can use RATE to calculate the periodic interest rate, then multiply as required to derive an annual interest rate. The RATE function is commonly multiplied by 12 to arrive at an annual rate.

The RATE function takes six [arguments](https://exceljet.net/glossary/function-argument)
, the first three of which are required:

*   _nper_ (required) - The total number of payment periods in the annuity. For example, a 5-year car loan with monthly payments has 60 periods. You can enter _nper_ as 5\*12 to show how the number was determined.
*   _pmt_ (required) - The payment made each period. This number cannot change over the life of the annuity. In annuity functions, cash paid out is represented by a negative number. Note: If _pmt_ is not provided, the optional _fv_ argument must be supplied.
*   _pv_ (required) - The present value. This is the cash balance required after all payments have been made.
*   fv (optional) - The future value, or a cash balance required after the last payment is made. When _fv_ is omitted, it defaults to zero (0) and _pmt_ must be provided.
*   _type_ (optional) - _type_ is a boolean that controls when payments are due. Use 0 for payments due at the end of the period (regular annuities) and 1 for payments due at the beginning of the period (annuities due). _Type_ defaults to 0 (end of period).
*   _guess_ (optional) - _guess_ is a seed value to use for iteration. When omitted, _guess_ defaults to 10%. Ordinarily, you can safely omit _guess_. If RATE does not converge, RATE will return a #NUM! error. Try different values for _guess_ between 0 and 1.

> RATE is calculated by iteration. If the results do not converge within 20 iterations, RATE returns a #NUM! error.

### Example

To calculate the annual interest rate for a $5000 loan with payments of $93.22 per month over 5 years, you can use RATE in a formula like this:

    =RATE(60,-93.22,5000)*12 // returns 4.5%
    

In the example shown, the formula in C10 is:

    =RATE(C7,-C6,C5)*C8 // returns 4.5%
    

Notice the value for _pmt_ from C6 is entered as a negative value.

> Use consistent values for _guess_ and _nper._ If you make _monthly_ payments on a five-year loan at 10 percent annual interest, use 10%/12 for _guess_ and 5\*12 for _nper_. If you make _annual_ payments on the same loan, use 10% for _guess_ and 5 for _nper._

### Notes

*   The RATE formula is commonly multiplied by 12 to arrive at an annual rate.
*   Be sure to use consistent values for _guess_ and _nper._

RATE function examples
----------------------

[![Excel formula: Annuity solve for interest rate](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/annuity%20solve%20for%20rate.png "Excel formula: Annuity solve for interest rate")](https://exceljet.net/formulas/annuity-solve-for-interest-rate)

### [Annuity solve for interest rate](https://exceljet.net/formulas/annuity-solve-for-interest-rate)

An annuity is a series of equal cash flows, spaced equally in time. The goal in this example is to have $100,000 at the end of 10 years, with an annual payment of $7,500 made at the end of each year. What interest rate is required? To solve for the interest rate, the RATE function is configured...

[![Excel formula: Calculate interest rate for loan](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20interest%20rate%20for%20loan.png "Excel formula: Calculate interest rate for loan")](https://exceljet.net/formulas/calculate-interest-rate-for-loan)

### [Calculate interest rate for loan](https://exceljet.net/formulas/calculate-interest-rate-for-loan)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term) and a payment amount per period. One use of the RATE function is to calculate the periodic interest rate when the amount, number of payment periods, and payment amount are known. In...

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

*   [Calculate interest rate for loan](https://exceljet.net/formulas/calculate-interest-rate-for-loan)
    
*   [Annuity solve for interest rate](https://exceljet.net/formulas/annuity-solve-for-interest-rate)
    

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

*   [Microsoft RATE function documentation](https://support.office.com/en-us/article/rate-function-9f665657-4a7e-4bb7-a030-83fc59e748ce)
    

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