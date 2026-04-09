# Excel LOG10 function | Exceljet

**Source:** https://exceljet.net/functions/log10-function

---

[Skip to main content](https://exceljet.net/functions/log10-function#main-content)

[](https://exceljet.net/functions/log10-function#)

*   [Previous](https://exceljet.net/functions/log-function)
    
*   [Next](https://exceljet.net/functions/mdeterm-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

LOG10 Function
==============

by Dave Bruns · Updated 13 Dec 2025

Related functions 
------------------

[LOG](https://exceljet.net/functions/log-function)

[POWER](https://exceljet.net/functions/power-function)

![Excel LOG10 function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_log10_new.png "Excel LOG10 function")

Summary
-------

The Excel LOG10 function returns the base 10 logarithm of a number. For example, LOG10(100) returns 2, and LOG10(1000) returns 3.

Purpose 
--------

Get the base-10 logarithm of a number

Return value 
-------------

The logarithm

Syntax
------

    =LOG10(number)

*   _number_ - The positive number for which you want the base-10 logarithm.

Using the LOG10 function 
-------------------------

LOG10 returns the base-10 logarithm of a number. In simple terms, it answers the question: "10 raised to what power gives me this number?" The table below shows how LOG10 works and how it is related to raising 10 to a specific power: 

| Number | LOG10 | Because |
| --- | --- | --- |
| 1000 | 3   | 10³ = 1000 |
| 100 | 2   | 10² = 100 |
| 10  | 1   | 10¹ = 10 |
| 1   | 0   | 10⁰ = 1 |
| 0.1 | \-1 | 10⁻¹ = 0.1 |
| 0.01 | \-2 | 10⁻² = 0.01 |

For numbers that aren't exact powers of 10, LOG10 will return get decimals:

| Number | LOG10 |
| --- | --- |
| 50  | 1.699 |
| 3697 | 3.568 |
| 0.3697 | \-0.432 |

To use Excel's LOG10 function, just supply a number:

    =LOG10(1000) // returns 3
    =LOG10(100) // returns 2
    =LOG10(10) // returns 1
    =LOG10(1) // returns 0
    =LOG10(0.1) // returns -1
    =LOG10(0.01) // returns -2
    

LOG10 function examples
-----------------------

[![Excel formula: Round number to n significant figures](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round_number_to_n_significant_figures.png "Excel formula: Round number to n significant figures")](https://exceljet.net/formulas/round-number-to-n-significant-figures)

### [Round number to n significant figures](https://exceljet.net/formulas/round-number-to-n-significant-figures)

In this example, the goal is to round a number to a given number of significant figures while preserving trailing zeros when needed. This is a tricky problem because Excel's rounding functions return numbers, and numbers don't preserve trailing zeros. This article uses "significant figures" and "...

Related functions
-----------------

[![Excel LOG function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_log_new.png "Excel LOG function")](https://exceljet.net/functions/log-function)

### [LOG Function](https://exceljet.net/functions/log-function)

The Excel LOG function returns the logarithm of a given number, using a supplied base. The base argument defaults to 10 if not supplied.

[![Excel POWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20power%20function.png "Excel POWER function")](https://exceljet.net/functions/power-function)

### [POWER Function](https://exceljet.net/functions/power-function)

The Excel POWER function returns a number raised to a given power. The POWER function is an alternative to the [exponent operator](https://exceljet.net/glossary/math-operators)
 (^).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Round number to n significant figures](https://exceljet.net/formulas/round-number-to-n-significant-figures)
    

### Functions

*   [LOG Function](https://exceljet.net/functions/log-function)
    
*   [POWER Function](https://exceljet.net/functions/power-function)
    

### Links

*   [Microsoft LOG10 function documentation](https://support.office.com/en-us/article/log10-function-c75b881b-49dd-44fb-b6f4-37e3486a0211)
    

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