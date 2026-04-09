# Odometer gas mileage log - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/odometer-gas-mileage-log

---

[Skip to main content](https://exceljet.net/formulas/odometer-gas-mileage-log#main-content)

[](https://exceljet.net/formulas/odometer-gas-mileage-log#)

*   [Previous](https://exceljet.net/formulas/number-is-whole-number)
    
*   [Next](https://exceljet.net/formulas/one-or-the-other-not-both)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Odometer gas mileage log
========================

by Dave Bruns · Updated 5 Oct 2020

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

[MAX](https://exceljet.net/functions/max-function)

[MIN](https://exceljet.net/functions/min-function)

![Excel formula: Odometer gas mileage log](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/odometer%20gas%20mileage%20log.png "Excel formula: Odometer gas mileage log")

Summary
-------

To calculate gas (MPG) based on odometer readings you can build a table with a few simple formulas. In the example shown, the formulas in E5 and F5 are:

    =[@Mileage]-SUM(C4) // E5 calculate mileage
    =[@Distance]/[@Gallons] // F5 calculate mpg

These formulas use the [structured references](https://exceljet.net/glossary/structured-reference)
 available in [Excel Tables](https://exceljet.net/glossary/excel-table)
.

Explanation 
------------

_Note:  this example assumes that fuel is added to capacity at each gas stop, in order to calculate miles per gallon (MPG) based on the miles driven and fuel used since the last stop. In addition, this example keeps all data in an [Excel Table](https://exceljet.net/articles/excel-tables)
 called "data" to illustrate how Tables can make some formulas easier to maintain._

The formula in E5 subtracts the mileage in the row above from mileage in the current row to calculate distance (miles driven) since the last gas stop:

    [@Mileage]-SUM(C4)
    

The SUM formula is used only to prevent errors on the first row, where the row above contains a text value. Without SUM, the first row formula will return the [#VALUE error](https://exceljet.net/formulas/how-to-fix-the-value-error)
. The [SUM function](https://exceljet.net/functions/sum-function)
 however will treat the text in C4 as zero and prevent the error.

The formula in F5 calculates MPG (miles per gallon) by dividing miles driven by gallons used:

    =[@Distance]/[@Gallons]
    

The result is [formatted as a number](https://exceljet.net/articles/custom-number-formats)
 with one decimal place.

### Summary stats

The formulas in I4:I6 calculate best, worst, and average MPG like this:

    =MAX(data[MPG]) // best
    =MIN(data[MPG]) // worst
    =SUM(data[Distance])/SUM(data[Gallons]) // average
    

Because we are using an [Excel Table](https://exceljet.net/articles/excel-tables)
 to hold the data, these formulas will continue to show correct results as more data is added to the table.

Related functions
-----------------

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    

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