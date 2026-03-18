# Calculate compound interest - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-compound-interest

---

[Skip to main content](https://exceljet.net/formulas/calculate-compound-interest#main-content)

[](https://exceljet.net/formulas/calculate-compound-interest#)

*   [Previous](https://exceljet.net/formulas/cagr-formula-examples)
    
*   [Next](https://exceljet.net/formulas/calculate-cumulative-loan-interest)
    

[Financial](https://exceljet.net/formulas#Financial)

Calculate compound interest
===========================

by Dave Bruns · Updated 9 Jan 2025

Related functions 
------------------

[FV](https://exceljet.net/functions/fv-function)

![Excel formula: Calculate compound interest](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate%20compound%20interest.png "Excel formula: Calculate compound interest")

Summary
-------

To calculate compound interest in Excel, you can use the [FV function](https://exceljet.net/functions/fv-function)
. This example assumes that $1000 is invested for 10 years at an annual interest rate of 5%, compounded monthly. In the example shown, the formula in C10 is:

    =FV(C6/C8,C7*C8,0,-C5)
    

The FV function returns approximately 1647 as a final result.

Generic formula
---------------

    =FV(rate,nper,pmt,pv)

Explanation 
------------

Compound interest is a financial concept that describes how an initial investment grows over time, taking into account not only the interest earned on the initial amount but also the interest earned on the interest itself. Compound interest allows your money to grow exponentially, which makes it a powerful tool for building wealth over the long term. To calculate the effect of compound interest in Excel, you can use the FV function, which is designed to calculate the future value of an investment. 

### FV function

The [FV function](https://exceljet.net/functions/fv-function)
, short for "Future Value," calculates the future value of an investment taking into account a constant interest rate and optional periodic payments. The FV function uses the following syntax:

    =FV(rate,nper,pmt,[pv],[type])

Each argument has the following meaning:

*   _rate:_ The interest rate for each period.
*   _nper:_ The number of periods.
*   _pmt:_ The payment made each period (optional).
*   _pv:_ The present value or initial investment.
*   _\[type\]:_ Optional argument to indicate when payments are due.

To calculate compound interest in this example, we need to provide the FV function with the number of periods, the periodic payment, and the present value like this:

    =FV(C6/C8,C7*C8,0,-C5)
    

*   _rate_: C6/C8 (5%/12)
*   _nper_: C7\*C8 (10\*12)
*   _pmt_: 0 (no payment)
*   _pv_: -C5 (-1000)
*   _\[type\]_: Not needed

To get the _rate_ (which is the period rate), we divide the annual rate (5%) by the compounding periods per year (12). To get the number of periods (_nper_), we multiply the term in years (10) by the periods per term (12). There is no periodic payment in this example, so we use zero for _pmt_. Finally, we provide the present value (_pv_) as -1000. By convention, the present value is input as a negative value because the initial investment of $1000 "leaves your wallet" and is transferred to the bank for the investment term. Putting it all together, Excel evaluates the formula like this:

    =FV(C6/C8,C7*C8,0,-C5)
    =FV(0.05/12,10*12,0,-1000)
    =FV(0.00417,120,0,-1000)
    =1647

The FV function returns approximately 1647 as a final result. This is the value of a $1,000 investment, compounded monthly with a 5% annual interest rate over 10 years.

> For a more detailed example, see this page: [Simple investing worksheet](https://exceljet.net/formulas/simple-investing-worksheet)

Related formulas
----------------

[![Excel formula: Simple investing worksheet](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/simple_investing_worksheet.png "Excel formula: Simple investing worksheet")](https://exceljet.net/formulas/simple-investing-worksheet)

### [Simple investing worksheet](https://exceljet.net/formulas/simple-investing-worksheet)

A while back, I got from a reader about investing for his grandkids. The email asks the following question: I hope you can assist me with an Excel calculation. I am keen to show my grandchildren the power of compound interest and the value of investing (patiently) for the long term. And I want to...

[![Excel formula: Calculate simple interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20%20simple%20interest.png "Excel formula: Calculate simple interest")](https://exceljet.net/formulas/calculate-simple-interest)

### [Calculate simple interest](https://exceljet.net/formulas/calculate-simple-interest)

The general formula for simple interest is: interest=principal\*rate\*term So, using cell references, we have: =C5\*C7\*C6 =1000\*10\*0.05 =500

[![Excel formula: Annual compound interest schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/annual%20compound%20interest%20schedule.png "Excel formula: Annual compound interest schedule")](https://exceljet.net/formulas/annual-compound-interest-schedule)

### [Annual compound interest schedule](https://exceljet.net/formulas/annual-compound-interest-schedule)

If you have an annual interest rate, and a starting balance you can calculate interest with: =balance \* rate and the ending balance with: =balance+(balance\*rate) So, for each period in the example, we use this formula copied down the table: =C5+(C5\*rate) With the FV function The FV function can...

[![Excel formula: Compare effect of compounding periods](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/compare%20compounding%20periods.png "Excel formula: Compare effect of compounding periods")](https://exceljet.net/formulas/compare-effect-of-compounding-periods)

### [Compare effect of compounding periods](https://exceljet.net/formulas/compare-effect-of-compounding-periods)

The FV function calculates compound interest and returns the future value of an investment over a specified term. To configure the function, we need to provide a rate, the number of periods, the periodic payment, and the present value: Present value ( pv ) is the named range G4 Rate is provided as...

Related functions
-----------------

[![Excel FV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_fv.png "Excel FV function")](https://exceljet.net/functions/fv-function)

### [FV Function](https://exceljet.net/functions/fv-function)

The Excel FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Simple investing worksheet](https://exceljet.net/formulas/simple-investing-worksheet)
    
*   [Calculate simple interest](https://exceljet.net/formulas/calculate-simple-interest)
    
*   [Annual compound interest schedule](https://exceljet.net/formulas/annual-compound-interest-schedule)
    
*   [Compare effect of compounding periods](https://exceljet.net/formulas/compare-effect-of-compounding-periods)
    

### Functions

*   [FV Function](https://exceljet.net/functions/fv-function)
    

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