# Excel NOMINAL function | Exceljet

**Source:** https://exceljet.net/functions/nominal-function

---

[Skip to main content](https://exceljet.net/functions/nominal-function#main-content)

[](https://exceljet.net/functions/nominal-function#)

*   [Previous](https://exceljet.net/functions/mirr-function)
    
*   [Next](https://exceljet.net/functions/nper-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

NOMINAL Function
================

by Dave Bruns · Updated 30 Aug 2021

Related functions 
------------------

[EFFECT](https://exceljet.net/functions/effect-function)

![Excel NOMINAL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel_nominal_function.png "Excel NOMINAL function")

Summary
-------

The Excel NOMINAL function returns the nominal interest rate when given an effective annual interest rate and the number of compounding periods per year. The effective rate is the actual rate due to compounding. The nominal rate is typically the stated rate.

Purpose 
--------

Get annual nominal interest rate

Return value 
-------------

Nominal interest rate

Syntax
------

    =NOMINAL(effect_rate,npery)

*   _effect\_rate_ - The effective annual interest rate.
*   _npery_ - Number of compounding periods per year.

Using the NOMINAL function 
---------------------------

The Excel NOMINAL function calculates the nominal interest rate when given an effective annual interest rate and the number of compounding periods per year. Nominal interest rate is typically the stated rate on a financial product. Effective annual interest rate is the interest rate actually earned due to compounding.  For example, with an effective rate of 6.14% and interest compounded quarterly, NOMINAL returns 6.00%:

    =NOMINAL(0.0614,4) // returns 0.06
    

In the example shown, the formula in D6, copied down, is:

    =NOMINAL(B6,C6)
    

Format the result as a percentage to display with % symbol.

### Notes

*   _Npery_ should be an integer (Excel will truncate if not).
*   The _effect\_rate_ should be a number between 0 and 1.

Related functions
-----------------

[![Excel EFFECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_effect_function.png "Excel EFFECT function")](https://exceljet.net/functions/effect-function)

### [EFFECT Function](https://exceljet.net/functions/effect-function)

The Excel EFFECT function returns the effective annual interest rate, given a nominal interest rate and the number of compounding periods per year. Effective annual interest rate is the interest rate actually earned due to compounding. 

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [EFFECT Function](https://exceljet.net/functions/effect-function)
    

### Links

*   [Microsoft NOMINAL function documentation](https://support.office.com/en-us/article/nominal-function-7f1ae29b-6b92-435e-b950-ad8b190ddd2b)
    

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