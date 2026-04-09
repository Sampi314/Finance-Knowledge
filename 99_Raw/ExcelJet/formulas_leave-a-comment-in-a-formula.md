# Leave a comment in a formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/leave-a-comment-in-a-formula

---

[Skip to main content](https://exceljet.net/formulas/leave-a-comment-in-a-formula#main-content)

[](https://exceljet.net/formulas/leave-a-comment-in-a-formula#)

*   [Previous](https://exceljet.net/formulas/increment-cell-reference-with-indirect)
    
*   [Next](https://exceljet.net/formulas/link-to-multiple-sheets)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Leave a comment in a formula
============================

by Dave Bruns · Updated 30 Mar 2017

Related functions 
------------------

[N](https://exceljet.net/functions/n-function)

![Excel formula: Leave a comment in a formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Leave%20a%20comment%20in%20a%20formula.png "Excel formula: Leave a comment in a formula")

Summary
-------

To leave a comment in a formula that returns a numeric result, you can use the N function. In the example shown, the formula in F9 is:

    =SUM(F5:F8)+N("Q4 numbers are estimates")
    

Generic formula
---------------

    =formula+N("comment")

Explanation 
------------

This is a tricky use of N() that allows you to use it as a way to leave in-cell comments. It only works for formulas that return numeric results.

The N function takes a value and returns a number. When given a text value, the N function returns zero.

In this case, the primary formula the SUM function, and the N function simply evaluates the comment text and returns zero:

    =SUM(F5:F8)+N("Q4 numbers are estimates")
    =SUM(F5:F8) + 0
    =410,750
    

The comment is visible in the formula bar when the cell is selected.

Related functions
-----------------

[![Excel N function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20n%20function.png "Excel N function")](https://exceljet.net/functions/n-function)

### [N Function](https://exceljet.net/functions/n-function)

The Excel N function returns a number when given a value. The N function can be used to convert TRUE and FALSE to 1 and 0 respectively. When given a text value, the N function returns zero.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [N Function](https://exceljet.net/functions/n-function)
    

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