# Excel VARP function | Exceljet

**Source:** https://exceljet.net/functions/varp-function

---

[Skip to main content](https://exceljet.net/functions/varp-function#main-content)

[](https://exceljet.net/functions/varp-function#)

*   [Previous](https://exceljet.net/functions/vara-function)
    
*   [Next](https://exceljet.net/functions/varpa-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

VARP Function
=============

by Dave Bruns · Updated 19 Dec 2017

Related functions 
------------------

[STDEVP](https://exceljet.net/functions/stdevp-function)

[STDEV](https://exceljet.net/functions/stdev-function)

[STDEV.S](https://exceljet.net/functions/stdev.s-function)

[VAR.P](https://exceljet.net/functions/var.p-function)

[VAR.S](https://exceljet.net/functions/var.s-function)

[VAR](https://exceljet.net/functions/var-function)

![Excel VARP function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_varp.png "Excel VARP function")

Summary
-------

The Excel VARP function calculates the variance of an entire population of data. If data represents a sample, use the VAR function or the newer VAR.S function. VARP ignores text values and logicals in references.

Purpose 
--------

Get variation of a population

Return value 
-------------

Computed variance

Syntax
------

    =VARP(number1,[number2],...)

*   _number1_ - First number or reference.
*   _number2_ - \[optional\] Second number or reference.

Using the VARP function 
------------------------

The VARP function calculates the variance of an entire population of data. Variance provides a general idea of the spread of data.  In the example shown, the formula in F5 is:

    =VARP(C5:C10)
    

VARP ignores text and logicals passed into as cell references. For example, VARP will ignore FALSE when it appears in a range like A1:A10. However, VARP will evaluate logical values, and text representations of numbers hardcoded directly as arguments.

_Note: Microsoft classifies VARP as a "[compatibility function](https://exceljet.net/glossary/compatibility-function)
", now replaced by the [VAR.P function](https://exceljet.net/functions/var.p-function)
._

### Variation functions in Excel

The table below summarizes the variation functions available in Excel.

| Name | Data set | Text and logicals |
| --- | --- | --- |
| [VAR](https://exceljet.net/functions/var-function) | Sample | Ignored |
| [VARP](https://exceljet.net/functions/varp-function) | Population | Ignored |
| [VAR.S](https://exceljet.net/functions/var.s-function) | Sample | Ignored |
| [VAR.P](https://exceljet.net/functions/var.p-function) | Population | Ignored |
| [VARA](https://exceljet.net/functions/vara-function) | Sample | Evaluated |
| [VARPA](https://exceljet.net/functions/varpa-function) | Population | Evaluated |

### Notes

*   VARP assumes data is an entire population. If data represents a sample, use VAR or VAR.S
*   VARP only evaluates numbers in references, ignoring empty cells, text, and logical values like TRUE or FALSE.
*   Arguments can either be numbers or names, arrays, or references that contain numbers.
*   Arguments can be hard-coded values instead of references.
*   To evaluate logical values and/or text in references, use the VARA function.

Related functions
-----------------

[![Excel STDEVP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdevp.png "Excel STDEVP function")](https://exceljet.net/functions/stdevp-function)

### [STDEVP Function](https://exceljet.net/functions/stdevp-function)

The STDEVP function calculates the standard deviation for data that represents a population. STDEVP has been replaced with a newer function called STDEV.P, which has the same behavior.

[![Excel STDEV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdev.png "Excel STDEV function")](https://exceljet.net/functions/stdev-function)

### [STDEV Function](https://exceljet.net/functions/stdev-function)

The Excel STDEV function returns the standard deviation for data that represents a sample. To calculate the standard deviation for an entire population, use STDEVP or STDEV.P.

[![Excel STDEV.S function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdev.s.png "Excel STDEV.S function")](https://exceljet.net/functions/stdev.s-function)

### [STDEV.S Function](https://exceljet.net/functions/stdev.s-function)

The Excel STDEV.S function calculates the standard deviation for a sample set of data. STDEV.S replaces the older STDEV function, with the same behavior.

[![Excel VAR.P function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_var.p.png "Excel VAR.P function")](https://exceljet.net/functions/var.p-function)

### [VAR.P Function](https://exceljet.net/functions/var.p-function)

The Excel VAR.P function returns the variance in an entire population.  If data represents a sample of the population, use the VAR.S function.

[![Excel VAR.S function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_var.s.png "Excel VAR.S function")](https://exceljet.net/functions/var.s-function)

### [VAR.S Function](https://exceljet.net/functions/var.s-function)

The Excel VAR.S function returns the variance of a sample. If data represents the entire population, use the VAR.P function. VAR.S ignores text values and logicals in references.

[![Excel VAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_var.png "Excel VAR function")](https://exceljet.net/functions/var-function)

### [VAR Function](https://exceljet.net/functions/var-function)

The Excel VAR function estimates the variance of a sample of data. If data represents the entire population, use the VARP function or the newer VAR.P function. VAR ignores text values and logicals in references.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [STDEVP Function](https://exceljet.net/functions/stdevp-function)
    
*   [STDEV Function](https://exceljet.net/functions/stdev-function)
    
*   [STDEV.S Function](https://exceljet.net/functions/stdev.s-function)
    
*   [VAR.P Function](https://exceljet.net/functions/var.p-function)
    
*   [VAR.S Function](https://exceljet.net/functions/var.s-function)
    
*   [VAR Function](https://exceljet.net/functions/var-function)
    

### Links

*   [Microsoft VARP function documentation](https://support.office.com/en-us/article/varp-function-26a541c4-ecee-464d-a731-bd4c575b1a6b)
    

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