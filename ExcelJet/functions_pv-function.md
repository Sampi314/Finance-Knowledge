# Excel PV function | Exceljet

**Source:** https://exceljet.net/functions/pv-function

---

[Skip to main content](https://exceljet.net/functions/pv-function#main-content)

[](https://exceljet.net/functions/pv-function#)

*   [Previous](https://exceljet.net/functions/pricemat-function)
    
*   [Next](https://exceljet.net/functions/rate-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

PV Function
===========

by Dave Bruns · Updated 16 May 2024

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

![Excel PV function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20pv%20function.png "Excel PV function")

Summary
-------

The Excel PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate.

Purpose 
--------

Get the present value of an investment

Return value 
-------------

Present value

Syntax
------

    =PV(rate,nper,pmt,[fv],[type])

*   _rate_ - The interest rate per period.
*   _nper_ - The number of payment periods.
*   _pmt_ - The payment made each period.
*   _fv_ - \[optional\] Future value. If omitted, defaults to zero.
*   _type_ - \[optional\] Payment type, 0 = end of period, 1 = beginning of period. Default is 0.

Using the PV function 
----------------------

The PV function returns the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate. You can use the PV function to calculate the present value of a loan or investment when the interest rate and cash flows are constant. The PV function takes five separate [arguments](https://exceljet.net/glossary/function-argument)
, three of which are required as explained below.

_rate_ (required) - the interest rate per period. For example, if the annual interest rate is 6% and periods are monthly, then the interest rate is =6%/12 = 0.5% (0.005). You can enter the _rate_ as 6%/12 as a reminder of how it is derived.

_nper_ (required) - The total number of payment periods in the annuity. For example, a 5-year car loan with monthly payments has 60 periods. You can enter _nper_ as 5\*12 to note how the number was determined.

_pmt_ (required) - The payment made each period. This number cannot change over the life of the annuity. In annuity functions, cash paid out is represented by a negative number. Note: If _pmt_ is not provided, the optional _fv_ argument must be supplied.

_fv_ (optional) - The future value. This is the cash balance required after all payments have been made. When _fv_ is omitted, it defaults to zero, and _pmt_ must be supplied. 

_type_ (optional) - _type_ is a boolean that controls when payments are due. Supply 0 for payments due at the end of the period (regular annuities) and 1 for payments due at the end of the period (annuities due). _Type_ defaults to 0 (end of period).

### Examples

The PV function can be used to calculate the present value of a loan, when the interest rate, payment, and number of periods are known. For example, the present value of a 5-year loan with an annual interest rate of 4.5% and monthly payments of $93.22 is approximately $5,000:

    =PV(4.5%/12,5*12,-93.22) // returns 5000.26
    

In the worksheet shown above, the formula in C10 is:

    =PV(C5/C8,C7,C6)
    

### Present value of annuity

To calculate the present value of an annuity that pays 10,000 per year for 25 years, with an annual interest rate of 7%:

    =PV(7%,25,10000) // returns -116,535.832
    

To return a positive present value, enter the payment as a negative number:

    =PV(7%,25,-10000) // returns 116,535.832
    

Also, see [Present value of an annuity](https://exceljet.net/formulas/present-value-of-annuity)
.

### Investment goal

To calculate the initial investment required to reach $15,000 in 10 years with an annual interest rate of 5%:

    =PV(5%,10,0,15000) // returns -9,208.70
    

Enter the future value as a negative number to get a positive result:

    =PV(5%,10,0,-15000) // returns 9,208.70
    

### PV versus NPV

Both the PV function and the [NPV function](https://exceljet.net/functions/npv-function)
 calculate present value, but there are differences in the way they operate:

*   The PV function can only be used when cash flows are constant and don't change. The NPV function can be used to calculate the present value of _uneven_ cash flows spaced evenly in time.
*   The PV function has a _type_ argument to handle regular annuities and annuities due. The NPV function always assumes a regular annuity, where payments are due at the end of the period.

### Notes

*   A stream of cash flows that includes the same amount of cash outflow (or inflow) each period is called an annuity. For example, a car loan or a mortgage is an annuity. When each period's interest rate is the same, an annuity can be valued using the PV function.
*   In annuity functions, the cash you pay out (such as a deposit to savings) is represented by a negative number; cash you receive, such as a dividend check, is represented by a positive number. For a $2,500 deposit to a bank, the _pmt_ would be -2500 if you are the depositor, and 2500 if you are the bank.

PV function examples
--------------------

[![Excel formula: Estimate mortgage payment](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/estimate_mortgage_payment.png "Excel formula: Estimate mortgage payment")](https://exceljet.net/formulas/estimate-mortgage-payment)

### [Estimate mortgage payment](https://exceljet.net/formulas/estimate-mortgage-payment)

In this example, the goal is to calculate a monthly mortgage payment based on three inputs: The loan amount The annual interest rate The loan term in years The worksheet shown also takes into account the down payment, which is calculated using a simple formula in C8 (see below) and then subtracted...

[![Excel formula: Bond valuation example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Bond%20valuation%20example.png "Excel formula: Bond valuation example")](https://exceljet.net/formulas/bond-valuation-example)

### [Bond valuation example](https://exceljet.net/formulas/bond-valuation-example)

In the example shown, we have a 3-year bond with a face value of $1,000. The coupon rate is 7% so the bond will pay 7% of the $1,000 face value in interest every year, or $70. However, because interest is paid semiannually in two equal payments, there will be 6 coupon payments of $35 each. The $1,...

[![Excel formula: Future value of annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20of%20annuity.png "Excel formula: Future value of annuity")](https://exceljet.net/formulas/future-value-of-annuity)

### [Future value of annuity](https://exceljet.net/formulas/future-value-of-annuity)

The FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate. An annuity is a series of equal cash flows, spaced equally in time. In...

[![Excel formula: Future value vs. Present value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20vs%20present%20value%20arrows.png "Excel formula: Future value vs. Present value")](https://exceljet.net/formulas/future-value-vs.-present-value)

### [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)

The FV function is a financial function that returns the future value of an investment, given periodic, constant payments with a constant interest rate. The PV function returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future...

[![Excel formula: Calculate original loan amount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20original%20loan%20amount.png "Excel formula: Calculate original loan amount")](https://exceljet.net/formulas/calculate-original-loan-amount)

### [Calculate original loan amount](https://exceljet.net/formulas/calculate-original-loan-amount)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term), and the payment amount per period. One use of the PV function is to calculate the original loan amount, when given the other 3 components. For this example, we want to find the...

[![Excel formula: Present value of annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/present%20value%20of%20annuity.png "Excel formula: Present value of annuity")](https://exceljet.net/formulas/present-value-of-annuity)

### [Present value of annuity](https://exceljet.net/formulas/present-value-of-annuity)

The PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate. An annuity is a series of equal cash flows,...

[![Excel formula: Calculate periods for annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20periods%20for%20annuity.png "Excel formula: Calculate periods for annuity")](https://exceljet.net/formulas/calculate-periods-for-annuity)

### [Calculate periods for annuity](https://exceljet.net/formulas/calculate-periods-for-annuity)

The NPER function returns the number of periods for loan or investment. You can NPER to get the number of payment periods for a loan, given the amount, the interest rate, and periodic payment amount. An annuity is a series of equal cash flows, spaced equally in time. The goal in this example is to...

[![Excel formula: Payment for annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/annuity%20payment%20amount.png "Excel formula: Payment for annuity")](https://exceljet.net/formulas/payment-for-annuity)

### [Payment for annuity](https://exceljet.net/formulas/payment-for-annuity)

The PMT function is a financial function that returns the periodic payment for a loan. You can use the PMT function to figure out payments for a loan, given the loan amount, number of periods, and interest rate. An annuity is a series of equal cash flows, spaced equally in time. The goal in this...

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

*   [Calculate original loan amount](https://exceljet.net/formulas/calculate-original-loan-amount)
    
*   [Estimate mortgage payment](https://exceljet.net/formulas/estimate-mortgage-payment)
    
*   [Present value of annuity](https://exceljet.net/formulas/present-value-of-annuity)
    
*   [Bond valuation example](https://exceljet.net/formulas/bond-valuation-example)
    
*   [Calculate periods for annuity](https://exceljet.net/formulas/calculate-periods-for-annuity)
    
*   [Payment for annuity](https://exceljet.net/formulas/payment-for-annuity)
    
*   [Future value of annuity](https://exceljet.net/formulas/future-value-of-annuity)
    
*   [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)
    

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

*   [Microsoft PV function documentation](https://support.office.com/en-us/article/pv-function-23879d31-0e02-4321-be01-da16e8168cbd)
    

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