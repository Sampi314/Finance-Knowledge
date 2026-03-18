# Calculate simple interest - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-simple-interest

---

[Skip to main content](https://exceljet.net/formulas/calculate-simple-interest#main-content)

[](https://exceljet.net/formulas/calculate-simple-interest#)

*   [Previous](https://exceljet.net/formulas/calculate-principal-for-given-period)
    
*   [Next](https://exceljet.net/formulas/compare-effect-of-compounding-periods)
    

[Financial](https://exceljet.net/formulas#Financial)

Calculate simple interest
=========================

by Dave Bruns · Updated 19 Oct 2016

![Excel formula: Calculate simple interest](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate%20%20simple%20interest.png "Excel formula: Calculate simple interest")

Summary
-------

To calculate simple interest in Excel (i.e. interest that is not compounded), you can use a formula that multiples principal, rate, and term.

This example assumes that $1000 is invested for 10 years at an annual interest rate of 5%. Simple interest means that interest payments are not compounded – the interest is applied to the principal only.

In the example shown, the formula in C8 is:

    =C5*C7*C6
    

Generic formula
---------------

    interest=principal*rate*term

Explanation 
------------

The general formula for simple interest is:

    interest=principal*rate*term
    

So, using cell references, we have:

    =C5*C7*C6
    =1000*10*0.05
    =500
    

Related formulas
----------------

[![Excel formula: Calculate compound interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20compound%20interest.png "Excel formula: Calculate compound interest")](https://exceljet.net/formulas/calculate-compound-interest)

### [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)

Compound interest is a financial concept that describes how an initial investment grows over time, taking into account not only the interest earned on the initial amount but also the interest earned on the interest itself. Compound interest allows your money to grow exponentially, which makes it a...

[![Excel formula: Annual compound interest schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/annual%20compound%20interest%20schedule.png "Excel formula: Annual compound interest schedule")](https://exceljet.net/formulas/annual-compound-interest-schedule)

### [Annual compound interest schedule](https://exceljet.net/formulas/annual-compound-interest-schedule)

If you have an annual interest rate, and a starting balance you can calculate interest with: =balance \* rate and the ending balance with: =balance+(balance\*rate) So, for each period in the example, we use this formula copied down the table: =C5+(C5\*rate) With the FV function The FV function can...

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
    
*   [Annual compound interest schedule](https://exceljet.net/formulas/annual-compound-interest-schedule)
    

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