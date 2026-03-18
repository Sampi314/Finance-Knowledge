# Excel EFFECT function | Exceljet

**Source:** https://exceljet.net/functions/effect-function

---

[Skip to main content](https://exceljet.net/functions/effect-function#main-content)

[](https://exceljet.net/functions/effect-function#)

*   [Previous](https://exceljet.net/functions/duration-function)
    
*   [Next](https://exceljet.net/functions/fv-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

EFFECT Function
===============

by Dave Bruns · Updated 26 Aug 2021

Related functions 
------------------

[NOMINAL](https://exceljet.net/functions/nominal-function)

![Excel EFFECT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel_effect_function.png "Excel EFFECT function")

Summary
-------

The Excel EFFECT function returns the effective annual interest rate, given a nominal interest rate and the number of compounding periods per year. Effective annual interest rate is the interest rate actually earned due to compounding. 

Purpose 
--------

Get effective annual interest rate

Return value 
-------------

Effective annual interest rate

Syntax
------

    =EFFECT(nominal_rate,npery)

*   _nominal\_rate_ - The nominal or stated interest rate.
*   _npery_ - Number of compounding periods per year.

Using the EFFECT function 
--------------------------

The EFFECT function calculates the effective annual interest rate, given a nominal interest rate and the number of compounding periods per year. Nominal interest rate is the stated rate on the financial product. Effective annual interest rate is the interest rate actually earned due to compounding.  For example, with a nominal rate of 6.00% and interest compounded quarterly, EFFECT returns 6.09%:

    =EFFECT(0.06,4) // returns 0.0614
    
    

In the example shown, the formula in D5, copied down, is:

    =EFFECT(B5,C5)
    

Format the result as a Percentage to display with % symbol.

### Notes

*   _Npery_ should be an integer (Excel will truncate if not).
*   The _nominal\_rate_ should be a number between 0 and 1.

EFFECT function examples
------------------------

[![Excel formula: Effective annual interest rate](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/effective%20annual%20interest%20rate.png "Excel formula: Effective annual interest rate")](https://exceljet.net/formulas/effective-annual-interest-rate)

### [Effective annual interest rate](https://exceljet.net/formulas/effective-annual-interest-rate)

The Effective Annual Rate (EAR) is the interest rate after factoring in compounding. In other words, the EAR is the rate actually earned due to the effect of compounding more frequently than once a year (annually). The EFFECT function calculates the effective annual interest rate based on the...

Related functions
-----------------

[![Excel NOMINAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_nominal_function.png "Excel NOMINAL function")](https://exceljet.net/functions/nominal-function)

### [NOMINAL Function](https://exceljet.net/functions/nominal-function)

The Excel NOMINAL function returns the nominal interest rate when given an effective annual interest rate and the number of compounding periods per year. The effective rate is the actual rate due to compounding. The nominal rate is typically the stated rate.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Effective annual interest rate](https://exceljet.net/formulas/effective-annual-interest-rate)
    

### Functions

*   [NOMINAL Function](https://exceljet.net/functions/nominal-function)
    

### Links

*   [Microsoft EFFECT function documentation](https://support.office.com/en-us/article/effect-function-910d4e4c-79e2-4009-95e6-507e04f11bc4)
    

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