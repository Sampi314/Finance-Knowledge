# SUMIFS multiple criteria lookup in table - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sumifs-multiple-criteria-lookup-in-table

---

[Skip to main content](https://exceljet.net/formulas/sumifs-multiple-criteria-lookup-in-table#main-content)

[](https://exceljet.net/formulas/sumifs-multiple-criteria-lookup-in-table#)

*   [Previous](https://exceljet.net/formulas/sum-range-with-index)
    
*   [Next](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)
    

[Lookup](https://exceljet.net/formulas#Lookup)

SUMIFS multiple criteria lookup in table
========================================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: SUMIFS multiple criteria lookup in table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/SUMIFS%20multiple%20criteria%20lookup%20in%20table.png "Excel formula: SUMIFS multiple criteria lookup in table")

Summary
-------

In some situations, you can use the SUMIFS function to perform multiple-criteria lookups on numeric data. To use SUMIFS like this, the lookup values must be numeric and unique to each set of possible criteria. In the example shown, the formula in H8 is:

    =SUMIFS(Table1[Price],Table1[Item],H5,Table1[Size],H6,Table1[Color],H7)
    

Where Table1 is an [Excel Table](https://exceljet.net/glossary/excel-table)
 as seen in the screenshot.

Generic formula
---------------

    =SUMIFS(table[values],table[col1],c1,table[col2],c2,table[col3],c3)

Explanation 
------------

This example shows how the SUMIFS function can sometimes be used to "lookup" numeric values, as an alternative to more complicated multi-criteria lookup formulas. This approach is less flexible than more general lookup formulas based on [INDEX and MATCH](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
 (or VLOOKUP) but it's also more straightforward since SUMIFS is designed to easily handle multiple criteria. It's also very fast.

In the example shown, we are using the SUMIFS function to "look up" the price of an item based on the item name, color, and size. The inputs for these criteria are the cells H5, H6, and H7.

Inside the SUMIFS function, the sum range is supplied as the "Price" column in Table1:

    Table1[Price]
    

Criteria are supplied in 3 range/criteria pairs as follows:

    Table1[Item],H5 // item
    Table1[Size],H6 // size
    Table1[Color],H7 // color
    

With this configuration, the SUMIFS function finds matching values in the "Price" column and returns the sum of matching prices for the specific criteria entered in H5:H7. Because only one price exists for each possible combination of criteria, the sum of the matching price is the same as the sum of all matching prices.

Notes:

1.  Each combination of criteria must match one result only.
2.  Lookup values (the sum range) must be numeric.
3.  SUMIFS will return zero if no match occurs.

Related formulas
----------------

[![Excel formula: VLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20muliple%20criteria.png "Excel formula: VLOOKUP with multiple criteria")](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

### [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

In the example shown, we want to look up employee departments and groups using VLOOKUP by matching the first and last name of an employee. One limitation of VLOOKUP is that it only handles one condition: the lookup\_value, which is matched against the first column in the table. This makes it...

[![Excel formula: INDEX and MATCH with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20and%20MATCH%20with%20multiple%20criteria.png "Excel formula: INDEX and MATCH with multiple criteria")](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

### [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

This is a more advanced formula. For basics, see How to use INDEX and MATCH . Normally, an INDEX MATCH formula is configured with MATCH set to look through a one-column range and provide a match based on given criteria. Without concatenating values in a helper column , or in the formula itself,...

[![Excel formula: SUMIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS_with_multiple_criteria_and_OR_logic.png "Excel formula: SUMIFS with multiple criteria and OR logic")](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)

### [SUMIFS with multiple criteria and OR logic](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)

In this example, the goal is to sum the value of orders that have a status of "Complete" or "Pending". This is a slightly tricky problem in Excel because the SUMIFS function is designed for conditional sums based on multiple criteria, but all criteria must be TRUE in order for a value to be...

[![Excel formula: SUMIFS with Excel Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS%20with%20Excel%20Table.png "Excel formula: SUMIFS with Excel Table")](https://exceljet.net/formulas/sumifs-with-excel-table)

### [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)

This formula uses structured references to feed table ranges into the SUMIFS function. The sum range is provided as Table1\[Total\] , the criteria range is provided as Table1\[Item\] , and criteria comes from values in column I. The formula in I5 is: =SUMIFS(Table1\[Total\],Table1\[Item\],H5) which...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
    
*   [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
    
*   [SUMIFS with multiple criteria and OR logic](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)
    
*   [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

### Articles

*   [Excel Tables](https://exceljet.net/articles/excel-tables)
    

### Training

*   [Excel Tables](https://exceljet.net/training/excel-tables)
    

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