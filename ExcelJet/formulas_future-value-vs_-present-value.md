# Future value vs. Present value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/future-value-vs.-present-value

---

[Skip to main content](https://exceljet.net/formulas/future-value-vs.-present-value#main-content)

[](https://exceljet.net/formulas/future-value-vs.-present-value#)

*   [Previous](https://exceljet.net/formulas/future-value-of-annuity)
    
*   [Next](https://exceljet.net/formulas/get-current-stock-price)
    

[Financial](https://exceljet.net/formulas#Financial)

Future value vs. Present value
==============================

by Dave Bruns · Updated 3 Oct 2020

Related functions 
------------------

[PV](https://exceljet.net/functions/pv-function)

[FV](https://exceljet.net/functions/fv-function)

![Excel formula: Future value vs. Present value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/future%20value%20vs%20present%20value%20arrows.png "Excel formula: Future value vs. Present value")

Summary
-------

This example shows how present value and future value are related using the [PV function](https://exceljet.net/functions/pv-function)
 and the [FV function](https://exceljet.net/functions/fv-function)
. Even as inputs for years, compounding periods, or rate are changed, C5 will equal F9 and C9 will equal F5.

Explanation 
------------

The [FV function](https://exceljet.net/functions/fv-function)
 is a financial function that returns the future value of an investment, given periodic, constant payments with a constant interest rate. The [PV function](https://exceljet.net/functions/pv-function)
 returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate. 

This simple example shows how present value and future value are related. In the example shown, Years, Compounding periods, and Interest rate are linked in columns C and F like this:

    F5=C9
    F6=C6
    F7=C7
    F8=C8
    

The formula to calculate future value in C9 is based on the [FV function](https://exceljet.net/functions/fv-function)
:

    =FV(C8/C7,C6*C7,0,-C5,0)
    

The formula to calculate present value in F9 is based on the [PV function](https://exceljet.net/functions/pv-function)
:

    =PV(F8/F7,F6*F7,0,-F5,0)
    

No matter how years, compounding periods, or rate are changed, C5 will equal F9 and C9 will equal F5.

Related functions
-----------------

[![Excel PV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pv%20function.png "Excel PV function")](https://exceljet.net/functions/pv-function)

### [PV Function](https://exceljet.net/functions/pv-function)

The Excel PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate.

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

### Functions

*   [PV Function](https://exceljet.net/functions/pv-function)
    
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