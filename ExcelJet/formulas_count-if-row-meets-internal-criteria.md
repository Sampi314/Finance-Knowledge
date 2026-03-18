# Count if row meets internal criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-if-row-meets-internal-criteria

---

[Skip to main content](https://exceljet.net/formulas/count-if-row-meets-internal-criteria#main-content)

[](https://exceljet.net/formulas/count-if-row-meets-internal-criteria#)

*   [Previous](https://exceljet.net/formulas/count-dates-in-given-year)
    
*   [Next](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)
    

[Count](https://exceljet.net/formulas#Count)

Count if row meets internal criteria
====================================

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count if row meets internal criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20if%20row%20meets%20internal%20criteria.png "Excel formula: Count if row meets internal criteria")

Summary
-------

To count rows in a table that meet internal, calculated criteria, without using a [helper column](https://exceljet.net/glossary/helper-column)
, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in cell G5 is:

    =SUMPRODUCT(--(C5:C15>D5:D15))
    

The result is 3, since there are three rows where Previous sales are greater than Current sales.

Generic formula
---------------

    =SUMPRODUCT(--(logical_expression))

Explanation 
------------

In this example the goal is to count products (rows) where sales have increased and sales have decreased, where previous sales are in column C (Previous) and current sales are in column D (Current). In this case, we can't use [COUNTIFS](https://exceljet.net/functions/countifs-function)
 directly, because COUNTIFS is a [range-based function](https://exceljet.net/articles/excels-racon-functions)
 and it won't accept a calculation for a range argument. One option is to add a [helper column](https://exceljet.net/glossary/helper-column)
 that subtracts Previous sales from Current sales and use COUNTIF to count results less than or greater than zero. But what if we don't want to (or can't) add a helper column? In that case, we can use the SUMPRODUCT function with [Boolean logic](https://exceljet.net/glossary/boolean-logic)
.

### SUMPRODUCT function

The [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 is designed to work with arrays. It multiplies corresponding elements in two or more arrays and sums the resulting products. One of SUMPRODUCT's special features is that it can handle "[array operations](https://exceljet.net/glossary/array-operation)
" natively, without requiring Control + Shift + Enter. This allows us to perform a comparison between current and previous sales directly in _array1_. To count rows where sales have decreased, we simply compare the values in column C to the values in column D using a logical expression like this:

    C5:C15>D5:D15
    

The result is an [array](https://exceljet.net/glossary/array)
 of TRUE FALSE values like this:

    {FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE}
    

To coerce the TRUE and FALSE values to 1s and 0s, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--):

    --(C5:C15>D5:D15)
    

This operation creates an array like this:

    {0;1;0;1;0;0;0;0;1;0;0}
    

Notice the 1s correspond to TRUE values in the previous array. The numeric array is returned to SUMPRODUCT as _array1_:

    =SUMPRODUCT({0;1;0;1;0;0;0;0;1;0;0}) // returns 3
    

Since there is only one array to process, SUMPRODUCT simply returns a sum. The result is 3 since there are three rows where the value in column C is greater than the value in column D.

### Sales increased

To count rows where sales have increased, we can simply reverse the logic. The formula in G6 is:

    =SUMPRODUCT(--(C5:C15<D5:D15))
    

The result is 8, since there are 8 rows where Previous sales are less than Current sales.

Related formulas
----------------

[![Excel formula: Count if row meets multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20if%20row%20meets%20multiple%20criteria.png "Excel formula: Count if row meets multiple criteria")](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)

### [Count if row meets multiple criteria](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)

In this example, the goal is to count orders (rows) where the state is Texas ("TX"), the amount is greater than $100, and the month is March. In this case, we can't use COUNTIFS , because COUNTIFS is a range-based function and it won't accept a calculation for a range argument, which we need to...

[![Excel formula: Count rows with multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20with%20multiple%20OR%20criteria.png "Excel formula: Count rows with multiple OR criteria")](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)

### [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)

In this example, the goal is to count rows using OR logic based on the criteria shown in column F. For example, in cell G5 we want to count rows where Color is "Blue" OR Pet is "Dog". This can be done with Boolean logic and the SUMPRODUCT function , as explained below. Notes This formula uses an...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count if row meets multiple criteria](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)
    
*   [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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