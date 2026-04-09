# Excel FV function | Exceljet

**Source:** https://exceljet.net/functions/fv-function

---

[Skip to main content](https://exceljet.net/functions/fv-function#main-content)

[](https://exceljet.net/functions/fv-function#)

*   [Previous](https://exceljet.net/functions/effect-function)
    
*   [Next](https://exceljet.net/functions/fvschedule-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

FV Function
===========

by Dave Bruns · Updated 19 Sep 2025

Related functions 
------------------

[PV](https://exceljet.net/functions/pv-function)

[RATE](https://exceljet.net/functions/rate-function)

[NPER](https://exceljet.net/functions/nper-function)

[PMT](https://exceljet.net/functions/pmt-function)

[PPMT](https://exceljet.net/functions/ppmt-function)

[IPMT](https://exceljet.net/functions/ipmt-function)

[CUMPRINC](https://exceljet.net/functions/cumprinc-function)

[CUMIPMT](https://exceljet.net/functions/cumipmt-function)

[FVSCHEDULE](https://exceljet.net/functions/fvschedule-function)

![Excel FV function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_fv.png "Excel FV function")

Summary
-------

The Excel FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate.

Purpose 
--------

Get the future value of an investment

Return value 
-------------

future value

Syntax
------

    =FV(rate,nper,pmt,[pv],[type])

*   _rate_ - The interest rate per period.
*   _nper_ - The total number of payment periods.
*   _pmt_ - The payment made each period. Must be entered as a negative number.
*   _pv_ - \[optional\] The present value of future payments. If omitted, assumed to be zero. Must be entered as a negative number.
*   _type_ - \[optional\] When payments are due. 0 = end of period, 1 = beginning of period. Default is 0.

Using the FV function 
----------------------

The future value (FV) function calculates the future value of an investment assuming periodic, constant payments with a constant interest rate.

Notes:

1\. Units for _rate_ and _nper_ must be consistent. For example, if you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 (annual rate/12 = monthly interest rate) for _rate_ and 4\*12 (48 payments total) for _nper_. If you make annual payments on the same loan, use 12% (annual interest) for _rate_ and 4 (4 payments total) for _nper_.

2\. If _pmt_ is for cash out (i.e deposits to saving, etc), payment value must be negative; for cash received (income, dividends), payment value must be positive.

FV function examples
--------------------

[![Excel formula: Bond valuation example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Bond%20valuation%20example.png "Excel formula: Bond valuation example")](https://exceljet.net/formulas/bond-valuation-example)

### [Bond valuation example](https://exceljet.net/formulas/bond-valuation-example)

In the example shown, we have a 3-year bond with a face value of $1,000. The coupon rate is 7% so the bond will pay 7% of the $1,000 face value in interest every year, or $70. However, because interest is paid semiannually in two equal payments, there will be 6 coupon payments of $35 each. The $1,...

[![Excel formula: Calculate periods for annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20periods%20for%20annuity.png "Excel formula: Calculate periods for annuity")](https://exceljet.net/formulas/calculate-periods-for-annuity)

### [Calculate periods for annuity](https://exceljet.net/formulas/calculate-periods-for-annuity)

The NPER function returns the number of periods for loan or investment. You can NPER to get the number of payment periods for a loan, given the amount, the interest rate, and periodic payment amount. An annuity is a series of equal cash flows, spaced equally in time. The goal in this example is to...

[![Excel formula: Present value of annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/present%20value%20of%20annuity.png "Excel formula: Present value of annuity")](https://exceljet.net/formulas/present-value-of-annuity)

### [Present value of annuity](https://exceljet.net/formulas/present-value-of-annuity)

The PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate. An annuity is a series of equal cash flows,...

[![Excel formula: Annual compound interest schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/annual%20compound%20interest%20schedule.png "Excel formula: Annual compound interest schedule")](https://exceljet.net/formulas/annual-compound-interest-schedule)

### [Annual compound interest schedule](https://exceljet.net/formulas/annual-compound-interest-schedule)

If you have an annual interest rate, and a starting balance you can calculate interest with: =balance \* rate and the ending balance with: =balance+(balance\*rate) So, for each period in the example, we use this formula copied down the table: =C5+(C5\*rate) With the FV function The FV function can...

[![Excel formula: Calculate compound interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20compound%20interest.png "Excel formula: Calculate compound interest")](https://exceljet.net/formulas/calculate-compound-interest)

### [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)

Compound interest is a financial concept that describes how an initial investment grows over time, taking into account not only the interest earned on the initial amount but also the interest earned on the interest itself. Compound interest allows your money to grow exponentially, which makes it a...

[![Excel formula: Simple investing worksheet](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/simple_investing_worksheet.png "Excel formula: Simple investing worksheet")](https://exceljet.net/formulas/simple-investing-worksheet)

### [Simple investing worksheet](https://exceljet.net/formulas/simple-investing-worksheet)

A while back, I got from a reader about investing for his grandkids. The email asks the following question: I hope you can assist me with an Excel calculation. I am keen to show my grandchildren the power of compound interest and the value of investing (patiently) for the long term. And I want to...

[![Excel formula: Future value vs. Present value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20vs%20present%20value%20arrows.png "Excel formula: Future value vs. Present value")](https://exceljet.net/formulas/future-value-vs.-present-value)

### [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)

The FV function is a financial function that returns the future value of an investment, given periodic, constant payments with a constant interest rate. The PV function returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future...

[![Excel formula: Estimate mortgage payment](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/estimate_mortgage_payment.png "Excel formula: Estimate mortgage payment")](https://exceljet.net/formulas/estimate-mortgage-payment)

### [Estimate mortgage payment](https://exceljet.net/formulas/estimate-mortgage-payment)

In this example, the goal is to calculate a monthly mortgage payment based on three inputs: The loan amount The annual interest rate The loan term in years The worksheet shown also takes into account the down payment, which is calculated using a simple formula in C8 (see below) and then subtracted...

[![Excel formula: Compare effect of compounding periods](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/compare%20compounding%20periods.png "Excel formula: Compare effect of compounding periods")](https://exceljet.net/formulas/compare-effect-of-compounding-periods)

### [Compare effect of compounding periods](https://exceljet.net/formulas/compare-effect-of-compounding-periods)

The FV function calculates compound interest and returns the future value of an investment over a specified term. To configure the function, we need to provide a rate, the number of periods, the periodic payment, and the present value: Present value ( pv ) is the named range G4 Rate is provided as...

[![Excel formula: Payment for annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/annuity%20payment%20amount.png "Excel formula: Payment for annuity")](https://exceljet.net/formulas/payment-for-annuity)

### [Payment for annuity](https://exceljet.net/formulas/payment-for-annuity)

The PMT function is a financial function that returns the periodic payment for a loan. You can use the PMT function to figure out payments for a loan, given the loan amount, number of periods, and interest rate. An annuity is a series of equal cash flows, spaced equally in time. The goal in this...

[![Excel formula: Future value of annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20of%20annuity.png "Excel formula: Future value of annuity")](https://exceljet.net/formulas/future-value-of-annuity)

### [Future value of annuity](https://exceljet.net/formulas/future-value-of-annuity)

The FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate. An annuity is a series of equal cash flows, spaced equally in time. In...

Related functions
-----------------

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

[![Excel FVSCHEDULE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_fvschedule_function.png "Excel FVSCHEDULE function")](https://exceljet.net/functions/fvschedule-function)

### [FVSCHEDULE Function](https://exceljet.net/functions/fvschedule-function)

The Excel FVSCHEDULE function returns the future value of a single sum based on a schedule of given interest rates. FVSCHEDULE can be used to find the future value of an investment with a variable or adjustable rate.

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
    
*   [Estimate mortgage payment](https://exceljet.net/formulas/estimate-mortgage-payment)
    
*   [Bond valuation example](https://exceljet.net/formulas/bond-valuation-example)
    
*   [Compare effect of compounding periods](https://exceljet.net/formulas/compare-effect-of-compounding-periods)
    
*   [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)
    
*   [Calculate periods for annuity](https://exceljet.net/formulas/calculate-periods-for-annuity)
    
*   [Payment for annuity](https://exceljet.net/formulas/payment-for-annuity)
    
*   [Future value of annuity](https://exceljet.net/formulas/future-value-of-annuity)
    
*   [Present value of annuity](https://exceljet.net/formulas/present-value-of-annuity)
    
*   [Simple investing worksheet](https://exceljet.net/formulas/simple-investing-worksheet)
    

### Functions

*   [PV Function](https://exceljet.net/functions/pv-function)
    
*   [RATE Function](https://exceljet.net/functions/rate-function)
    
*   [NPER Function](https://exceljet.net/functions/nper-function)
    
*   [PMT Function](https://exceljet.net/functions/pmt-function)
    
*   [PPMT Function](https://exceljet.net/functions/ppmt-function)
    
*   [IPMT Function](https://exceljet.net/functions/ipmt-function)
    
*   [CUMPRINC Function](https://exceljet.net/functions/cumprinc-function)
    
*   [CUMIPMT Function](https://exceljet.net/functions/cumipmt-function)
    
*   [FVSCHEDULE Function](https://exceljet.net/functions/fvschedule-function)
    

### Links

*   [Microsoft FV function documentation](https://support.office.com/en-us/article/fv-function-2eef9f44-a084-4c61-bdd8-4fe4bb1b71b3)
    

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