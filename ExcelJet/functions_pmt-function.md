# Excel PMT function | Exceljet

**Source:** https://exceljet.net/functions/pmt-function

---

[Skip to main content](https://exceljet.net/functions/pmt-function#main-content)

[](https://exceljet.net/functions/pmt-function#)

*   [Previous](https://exceljet.net/functions/pduration-function)
    
*   [Next](https://exceljet.net/functions/ppmt-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

PMT Function
============

by Dave Bruns · Updated 31 Aug 2021

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

![Excel PMT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_pmt.png "Excel PMT function")

Summary
-------

The Excel PMT function is a financial function that returns the periodic payment for a loan. You can use the PMT function to figure out payments for a loan, given the loan amount, number of periods, and interest rate.

Purpose 
--------

Get the periodic payment for a loan

Return value 
-------------

loan payment as a number

Syntax
------

    =PMT(rate,nper,pv,[fv],[type])

*   _rate_ - The interest rate for the loan.
*   _nper_ - The total number of payments for the loan.
*   _pv_ - The present value, or total value of all loan payments now.
*   _fv_ - \[optional\] The future value, or a cash balance you want after the last payment is made. Defaults to 0 (zero).
*   _type_ - \[optional\] When payments are due. 0 = end of period. 1 = beginning of period. Default is 0.

Using the PMT function 
-----------------------

The PMT function can be used to figure out the future payments for a loan, assuming constant payments and a constant interest rate.  For example, if you are borrowing $10,000 on a 24 month loan with an annual interest rate of 8 percent, PMT can tell you what your monthly payments be and how much principal and interest you are paying each month.

Notes:

*   The payment returned by PMT includes principal and interest but will not include any taxes, reserve payments, or fees.
*   Be sure you are consistent with the units you supply for _rate_ and _nper_. If you make monthly payments on a three-year loan at an annual interest rate of 12 percent, use 12%/12 for _rate_ and 3\*12 for _nper_. For annual payments on the same loan, use 12 percent for _rate_ and 3 for _nper_.

PMT function examples
---------------------

[![Excel formula: Estimate mortgage payment](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/estimate_mortgage_payment.png "Excel formula: Estimate mortgage payment")](https://exceljet.net/formulas/estimate-mortgage-payment)

### [Estimate mortgage payment](https://exceljet.net/formulas/estimate-mortgage-payment)

In this example, the goal is to calculate a monthly mortgage payment based on three inputs: The loan amount The annual interest rate The loan term in years The worksheet shown also takes into account the down payment, which is calculated using a simple formula in C8 (see below) and then subtracted...

[![Excel formula: Payment for annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/annuity%20payment%20amount.png "Excel formula: Payment for annuity")](https://exceljet.net/formulas/payment-for-annuity)

### [Payment for annuity](https://exceljet.net/formulas/payment-for-annuity)

The PMT function is a financial function that returns the periodic payment for a loan. You can use the PMT function to figure out payments for a loan, given the loan amount, number of periods, and interest rate. An annuity is a series of equal cash flows, spaced equally in time. The goal in this...

[![Excel formula: Calculate payment for a loan](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20payment%20for%20a%20loan.png "Excel formula: Calculate payment for a loan")](https://exceljet.net/formulas/calculate-payment-for-a-loan)

### [Calculate payment for a loan](https://exceljet.net/formulas/calculate-payment-for-a-loan)

Loans have four primary components: the amount, the interest rate, the number of periodic payments (the loan term) and a payment amount per period. You can use the PMT function to get the payment when you have the other 3 components. For this example, we want to find the payment for a $5000 loan...

[![Excel formula: Calculate periods for annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20periods%20for%20annuity.png "Excel formula: Calculate periods for annuity")](https://exceljet.net/formulas/calculate-periods-for-annuity)

### [Calculate periods for annuity](https://exceljet.net/formulas/calculate-periods-for-annuity)

The NPER function returns the number of periods for loan or investment. You can NPER to get the number of payment periods for a loan, given the amount, the interest rate, and periodic payment amount. An annuity is a series of equal cash flows, spaced equally in time. The goal in this example is to...

[![Excel formula: Mortgage payment schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/mortgage_schedule_with_extra_payment.png "Excel formula: Mortgage payment schedule")](https://exceljet.net/formulas/mortgage-payment-schedule)

### [Mortgage payment schedule](https://exceljet.net/formulas/mortgage-payment-schedule)

The goal of this example is to show how to create a mortgage payment schedule using Excel formulas. A mortgage payment schedule is a detailed breakdown of every payment over the life of a loan. Each payment represents one period , typically a month. For each period, the schedule shows how much of...

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

*   [Calculate payment for a loan](https://exceljet.net/formulas/calculate-payment-for-a-loan)
    
*   [Calculate periods for annuity](https://exceljet.net/formulas/calculate-periods-for-annuity)
    
*   [Mortgage payment schedule](https://exceljet.net/formulas/mortgage-payment-schedule)
    
*   [Estimate mortgage payment](https://exceljet.net/formulas/estimate-mortgage-payment)
    
*   [Payment for annuity](https://exceljet.net/formulas/payment-for-annuity)
    

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

*   [Microsoft PMT function documentation](https://support.office.com/en-us/article/pmt-function-0214da64-9a63-4996-bc20-214433fa6441)
    

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