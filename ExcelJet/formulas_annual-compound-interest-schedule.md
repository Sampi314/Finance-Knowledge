# Annual compound interest schedule - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/annual-compound-interest-schedule

---

[Skip to main content](https://exceljet.net/formulas/annual-compound-interest-schedule#main-content)

[](https://exceljet.net/formulas/annual-compound-interest-schedule#)

*   [Previous](https://exceljet.net/formulas/validate-strong-password)
    
*   [Next](https://exceljet.net/formulas/annuity-solve-for-interest-rate)
    

[Financial](https://exceljet.net/formulas#Financial)

Annual compound interest schedule
=================================

by Dave Bruns · Updated 16 Mar 2019

Related functions 
------------------

[FV](https://exceljet.net/functions/fv-function)

![Excel formula: Annual compound interest schedule](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/annual%20compound%20interest%20schedule.png "Excel formula: Annual compound interest schedule")

Summary
-------

To calculate annual compound interest, you can use a formula based on the starting balance and annual interest rate. In the example shown, the formula in C6 is:

    =C5+(C5*rate)
    

Note: "rate" is the [named range](https://exceljet.net/glossary/named-range)
 F6.

Generic formula
---------------

    =start+(start*rate)

Explanation 
------------

If you have an annual interest rate, and a starting balance you can calculate interest with:

    =balance * rate
    

and the ending balance with:

    =balance+(balance*rate)
    

So, for each period in the example, we use this formula copied down the table:

    =C5+(C5*rate)
    

### With the FV function

The FV function can also be used to calculate future value. The equivalent formula is:

    =FV(rate,1,0,-C5)
    

The interest **rate** is used as-is, since we are compounding annually, **nper** is 1, since there is only one period per year, **pmt** is zero, since there are no additional payments, and **pv** is the starting balance, input as a negative value by convention.

Related formulas
----------------

[![Excel formula: Calculate simple interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20%20simple%20interest.png "Excel formula: Calculate simple interest")](https://exceljet.net/formulas/calculate-simple-interest)

### [Calculate simple interest](https://exceljet.net/formulas/calculate-simple-interest)

The general formula for simple interest is: interest=principal\*rate\*term So, using cell references, we have: =C5\*C7\*C6 =1000\*10\*0.05 =500

[![Excel formula: Calculate compound interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20compound%20interest.png "Excel formula: Calculate compound interest")](https://exceljet.net/formulas/calculate-compound-interest)

### [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)

Compound interest is a financial concept that describes how an initial investment grows over time, taking into account not only the interest earned on the initial amount but also the interest earned on the interest itself. Compound interest allows your money to grow exponentially, which makes it a...

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

*   [Calculate simple interest](https://exceljet.net/formulas/calculate-simple-interest)
    
*   [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)
    

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