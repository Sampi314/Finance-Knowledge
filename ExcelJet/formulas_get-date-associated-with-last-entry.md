# Get date associated with last entry - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-date-associated-with-last-entry

---

[Skip to main content](https://exceljet.net/formulas/get-date-associated-with-last-entry#main-content)

[](https://exceljet.net/formulas/get-date-associated-with-last-entry#)

*   [Previous](https://exceljet.net/formulas/formula-with-locked-absolute-reference)
    
*   [Next](https://exceljet.net/formulas/get-first-entry-by-month-and-year)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Get date associated with last entry
===================================

by Dave Bruns · Updated 14 Mar 2025

Related functions 
------------------

[LOOKUP](https://exceljet.net/functions/lookup-function)

![Excel formula: Get date associated with last entry](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20date%20associated%20with%20last%20entry.png "Excel formula: Get date associated with last entry")

Summary
-------

To retrieve a date associated with a last entry tabular data, you can use a formula based on the [LOOKUP function](https://exceljet.net/functions/lookup-function)
. In the example shown the formula in H5 is:

    =LOOKUP(2,1/(C5:G5<>""),C$4:G$4)
    

Generic formula
---------------

    =LOOKUP(2,1/(row<>""),header)

Explanation 
------------

Working from the inside out, the expression C5:G5<>"" returns an array of true and false values:

    {FALSE,TRUE,FALSE,FALSE,FALSE}
    

The number 1 is divided by this array, which creates a new array composed of either 1's or #DIV/0! errors:

    {#DIV/0!,1,#DIV/0!,#DIV/0!,#DIV/0!}
    

This array is used as the lookup\_vector.

The lookup\_value is 2, but the largest value in the lookup\_array is 1, so LOOKUP will match the last 1 in the array.

Finally, LOOKUP returns the corresponding value in result\_vector, from the dates in the range C$4:G$4.

_Note: the result in column H is a date from row 5, [formatted with the custom format](https://exceljet.net/articles/custom-number-formats)
 "mmm" to show an abbreviated month name only._

### Zeros instead of blanks

You might have a table with zeros instead of blank cells:

![LOOKUP formulas for ignoring zero values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/Get%20date%20associated%20with%20last%20entry%20with%20zero%20values.png?itok=SxNoOJW3 "LOOKUP formulas for ignoring zero values")

In that case, you can adjust the formula to match values greater than zero like so:

    =LOOKUP(2,1/(C5:G5>0),C$4:G$4)
    

### Multiple criteria

You can extend criteria by adding expressions to the denominator with [boolean logic](https://exceljet.net/glossary/boolean-logic)
. For example, to match the last value greater than 400, you can use a formula like this:

    =LOOKUP(2,1/((C5:G5<>"")*(C5:G5>400)),C$4:G$4)
    

Related formulas
----------------

[![Excel formula: Get value of last non-empty cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_value_of_last_non-empty_cell.png "Excel formula: Get value of last non-empty cell")](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

### [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

In this example, the goal is to get the last value in column B, even when data may contain empty cells. A secondary goal is to get the corresponding value in column C. This is useful for analyzing datasets where the most recent or last entry is significant. In the current version of Excel, a good...

[![Excel formula: Lookup latest price](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Lookup%20latest%20price.png "Excel formula: Lookup latest price")](https://exceljet.net/formulas/lookup-latest-price)

### [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)

The LOOKUP function assumes data is sorted, and always does an approximate match. If the lookup value is greater than all values in the lookup array, default behavior is to "fall back" to the previous value. This formula exploits this behavior by creating an array that contains only 1s and errors,...

Related functions
-----------------

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
    
*   [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)
    

### Functions

*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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