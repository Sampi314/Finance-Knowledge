# Compare effect of compounding periods - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/compare-effect-of-compounding-periods

---

[Skip to main content](https://exceljet.net/formulas/compare-effect-of-compounding-periods#main-content)

[](https://exceljet.net/formulas/compare-effect-of-compounding-periods#)

*   [Previous](https://exceljet.net/formulas/calculate-simple-interest)
    
*   [Next](https://exceljet.net/formulas/currency-exchange-rate-example)
    

[Financial](https://exceljet.net/formulas#Financial)

Compare effect of compounding periods
=====================================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[FV](https://exceljet.net/functions/fv-function)

![Excel formula: Compare effect of compounding periods](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/compare%20compounding%20periods.png "Excel formula: Compare effect of compounding periods")

Summary
-------

To compare the effect of (non-annual) compounding periods on growth, you can set up a worksheet as shown, and calculate future value with the [FV function](https://exceljet.net/functions/fv-function)
. In the example shown, $1000 is invested with an annual interest rate of 5%, the formulas in column D calculate the future value of the $1000 assuming the compounding periods shown in column C. The formula in D5, copied down, is:

    =FV(rate/C5,C5*term,0,-pv)
    

where **pv** (G4), **rate** (G5), and **term** (G6) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =FV(rate,nper,pmt,pv)

Explanation 
------------

The FV function calculates compound interest and returns the future value of an investment over a specified term. To configure the function, we need to provide a rate, the number of periods, the periodic payment, and the present value:

*   Present value (**pv**) is the named range G4
*   Rate is provided as annual rate/periods, or **rate**/C5
*   Number of periods (nper) is given as periods \* term, or C5 \* **term**
*   There is no periodic payment, so we use zero (0)

By convention, the present value (pv) is input as a negative value, since the $1000 "leaves your wallet" and goes to the bank during the term.

> The named ranges automatically behave like [absolute references](https://exceljet.net/glossary/absolute-reference)
> , so there is no need to use dollar signs ($).

Related formulas
----------------

[![Excel formula: Calculate compound interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20compound%20interest.png "Excel formula: Calculate compound interest")](https://exceljet.net/formulas/calculate-compound-interest)

### [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)

Compound interest is a financial concept that describes how an initial investment grows over time, taking into account not only the interest earned on the initial amount but also the interest earned on the interest itself. Compound interest allows your money to grow exponentially, which makes it a...

[![Excel formula: Calculate simple interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20%20simple%20interest.png "Excel formula: Calculate simple interest")](https://exceljet.net/formulas/calculate-simple-interest)

### [Calculate simple interest](https://exceljet.net/formulas/calculate-simple-interest)

The general formula for simple interest is: interest=principal\*rate\*term So, using cell references, we have: =C5\*C7\*C6 =1000\*10\*0.05 =500

[![Excel formula: Annual compound interest schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/annual%20compound%20interest%20schedule.png "Excel formula: Annual compound interest schedule")](https://exceljet.net/formulas/annual-compound-interest-schedule)

### [Annual compound interest schedule](https://exceljet.net/formulas/annual-compound-interest-schedule)

If you have an annual interest rate, and a starting balance you can calculate interest with: =balance \* rate and the ending balance with: =balance+(balance\*rate) So, for each period in the example, we use this formula copied down the table: =C5+(C5\*rate) With the FV function The FV function can...

[![Excel formula: Effective annual interest rate](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/effective%20annual%20interest%20rate.png "Excel formula: Effective annual interest rate")](https://exceljet.net/formulas/effective-annual-interest-rate)

### [Effective annual interest rate](https://exceljet.net/formulas/effective-annual-interest-rate)

The Effective Annual Rate (EAR) is the interest rate after factoring in compounding. In other words, the EAR is the rate actually earned due to the effect of compounding more frequently than once a year (annually). The EFFECT function calculates the effective annual interest rate based on the...

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

*   [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)
    
*   [Calculate simple interest](https://exceljet.net/formulas/calculate-simple-interest)
    
*   [Annual compound interest schedule](https://exceljet.net/formulas/annual-compound-interest-schedule)
    
*   [Effective annual interest rate](https://exceljet.net/formulas/effective-annual-interest-rate)
    

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