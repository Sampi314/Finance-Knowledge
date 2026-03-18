# Customer is new - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/customer-is-new

---

[Skip to main content](https://exceljet.net/formulas/customer-is-new#main-content)

[](https://exceljet.net/formulas/customer-is-new#)

*   [Previous](https://exceljet.net/formulas/cube-root-of-number)
    
*   [Next](https://exceljet.net/formulas/display-sorted-values-with-helper-column)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Customer is new
===============

by Dave Bruns · Updated 14 Apr 2019

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

![Excel formula: Customer is new](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/customer%20is%20new..png "Excel formula: Customer is new")

Summary
-------

To mark a customer as new in a list or table, you can use the COUNTIFS function and an expanding range in a [helper column](https://exceljet.net/glossary/helper-column)
. In the example shown, the formula in E5, copied down, is:

    =(COUNTIFS($B$5:B5,B5)=1)+0
    

The first time a customer appears in the list, the formula returns 1. Subsequent occurrences return zero.

Generic formula
---------------

    =(COUNTIFS($A$1:A1,A1)=1)+0

Explanation 
------------

This formula uses an [expanding range](https://exceljet.net/glossary/expanding-reference)
 for the criteria range inside COUNTIFS:

    COUNTIFS($B$5:B5,B5)
    

Because the first reference is absolute and the second reference is relative, the range expands as the formula is copied down the column. The criteria is simply the value in the current row of column B.

COUNTIFS returns the count of the current customer up to that point in the data. This means the first occurrence of a customer is 1, the second is 2, and so on. Because we only care about the first occurrence, we compare the count to 1:

    COUNTIFS($B$5:B5,B5)=1
    

This expression will return TRUE when the count is 1 and FALSE for any other value.

Finally, to force a 1 or 0 result, we add zero. The math operation causes Excel to coerce TRUE and FALSE to equivalent numbers, 1 and 0.

_Note: The example above uses first name for customer id. This is not realistic, but it makes it easy for the human eye to track. In normal data, customer id will be a unique number of some kind._

Related formulas
----------------

[![Excel formula: New customers per month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/new%20customers%20per%20month.png "Excel formula: New customers per month")](https://exceljet.net/formulas/new-customers-per-month)

### [New customers per month](https://exceljet.net/formulas/new-customers-per-month)

This formula relies on a helper column, which is column E in the example shown. The formula in E5, copied down, is: =(COUNTIFS($B$5:B5,B5)=1)+0 This formula returns a 1 for new customers and a 0 for repeat customers, and is explained in detail here . Once this formula is in place, the COUNTIFS...

[![Excel formula: Flag first duplicate in a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/flag%20first%20duplicate%20in%20a%20list.png "Excel formula: Flag first duplicate in a list")](https://exceljet.net/formulas/flag-first-duplicate-in-a-list)

### [Flag first duplicate in a list](https://exceljet.net/formulas/flag-first-duplicate-in-a-list)

At the core, this formula is composed of two sets of the COUNTIF function wrapped in the IF function . The outer IF + COUNTIF first checks to see if the value in question (B4) appears more than once in the list: =IF(COUNTIF($B$4:$B$11,B4)>1 If not, the outer IF function returns an empty string...

[![Excel formula: Highlight duplicate values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20duplicate%20values.png "Excel formula: Highlight duplicate values")](https://exceljet.net/formulas/highlight-duplicate-values)

### [Highlight duplicate values](https://exceljet.net/formulas/highlight-duplicate-values)

COUNTIF simply counts the number of times each value appears in the range. When the count is more than 1, the formula returns TRUE and triggers the rule. When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [New customers per month](https://exceljet.net/formulas/new-customers-per-month)
    
*   [Flag first duplicate in a list](https://exceljet.net/formulas/flag-first-duplicate-in-a-list)
    
*   [Highlight duplicate values](https://exceljet.net/formulas/highlight-duplicate-values)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

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