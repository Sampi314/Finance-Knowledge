# Running count group by n size - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/running-count-group-by-n-size

---

[Skip to main content](https://exceljet.net/formulas/running-count-group-by-n-size#main-content)

[](https://exceljet.net/formulas/running-count-group-by-n-size#)

*   [Previous](https://exceljet.net/formulas/map-text-to-numbers)
    
*   [Next](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)
    

[Grouping](https://exceljet.net/formulas#Grouping)

Running count group by n size
=============================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[COUNTA](https://exceljet.net/functions/counta-function)

[CEILING](https://exceljet.net/functions/ceiling-function)

![Excel formula: Running count group by n size](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/running%20count%20group%20by%20n%20size.png "Excel formula: Running count group by n size")

Summary
-------

To creating a running count of groups of a variable size, you can use the COUNTA and CEILING function. In the example shown, C5 contains this formula:

    =CEILING(COUNTA($B$5:B5)/size,1)
    

where "size" is the [named range](https://exceljet.net/glossary/named-range)
 F4.

Generic formula
---------------

    =CEILING(COUNTA(expanding_range)/size,1)

Explanation 
------------

The core of this formula is the COUNTA function, configured with an [expanding range](https://exceljet.net/glossary/expanding-reference)
 like this:

    COUNTA($B$5:B5)
    

As the formula is copied down the column, the range starting with B5 expands to include each new row, and COUNTA returns a running count of all non-blank entries in the range.

The result of COUNTA is then divided by "size", configured as a named range F4. Using a cell on the worksheet for group size allows the grouping to be changed at any time without editing the formula. The named range is used only for readability and convenience.

The resulting value is then processed by the CEILING function, with a significance of 1. CEILING is a rounding function that always rounds up to the next unit of significance. In this example, this causes fractional values to be rounded up to the next integer.

### Handling empty cells

If the range you are counting contains blank or empty cells, you can wrap the formula inside the IF function like this:

    =IF(B5<>"",CEILING(COUNTA($B$5:B5)/size,1),"")
    

Here, we run the counting and rounding operation described above only when the cell in column B is not blank. If it is blank, we skip the count and return an [empty string](https://exceljet.net/glossary/empty-string)
 ("").

Related formulas
----------------

[![Excel formula: Running count of occurrence in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20count%20of%20occurrence%20in%20list.png "Excel formula: Running count of occurrence in list")](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

### [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

In this example, the goal is to create a running count for a specific value that appears in column B. The value to count is entered in cell E5, which is the named range value . The core of the solution explained below is the COUNTIF function , with help from the IF function to suppress a count for...

Related functions
-----------------

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
    

### Functions

*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    

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