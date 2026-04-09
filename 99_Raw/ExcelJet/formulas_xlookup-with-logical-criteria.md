# XLOOKUP with logical criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-with-logical-criteria

---

[Skip to main content](https://exceljet.net/formulas/xlookup-with-logical-criteria#main-content)

[](https://exceljet.net/formulas/xlookup-with-logical-criteria#)

*   [Previous](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP with logical criteria
=============================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

![Excel formula: XLOOKUP with logical criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP%20with%20logical%20criteria.png "Excel formula: XLOOKUP with logical criteria")

Summary
-------

To use XLOOKUP with multiple logical, build expressions with boolean logic and then look for the number 1. In the example shown, XLOOKUP is used to look up the first sale to Chicago over $250. The formula in G6 is:

    =XLOOKUP(1,(D5:D14="chicago")*(E5:E14>250),B5:B14)
    

which returns 0347, the order number of the first record that meets the supplied criteria.

_Note: XLOOKUP is not case-sensitive._

Generic formula
---------------

    =XLOOKUP(1,(rng1="red")*(rng2>100),results)

Explanation 
------------

XLOOKUP can handle arrays natively, which makes it a very useful function when constructing criteria based on multiple logical expressions.

In the example shown, we are looking for the order number of the first order to Chicago over $250. We are constructing a lookup [array](https://exceljet.net/glossary/array)
 using the following expression and [boolean logic](https://exceljet.net/glossary/boolean-logic)
:

    (D5:D14="chicago")*(E5:E14>250)
    

When this expression is evaluated, we first get two arrays of TRUE FALSE values like this:

    {FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE}*
    {FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE}
    

When the two arrays are multiplied by one another, the math operation results in a single array of 1's and 0's like this:

    {0;0;0;0;0;0;0;1;0;0}
    

We now have the following formula, and you can see why we are using 1 for the lookup value:

    =XLOOKUP(1,{0;0;0;0;0;0;0;1;0;0},B5:B14)
    

XLOOKUP matches the 1 in the 8th position and returns the corresponding 8th value from B5:B14, which is 0347.

### With a single criteria

As seen above, math operations automatically coerce TRUE and FALSE values to 1's and 0's. Therefore, when using multiple expressions, a lookup value of 1 makes sense. In cases where you have only a single condition, say, "amount > 250", you can look for TRUE instead like this:

    =XLOOKUP(TRUE,E5:E14>250,B5:B14)
    

Alternatively, [you can force the TRUE FALSE values to 1's and 0's](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
, and use 1 like this.

    =XLOOKUP(1,--(E5:E14>250),B5:B14)
    

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

### [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for lookup\_value and lookup\_array . How can we...

[![Excel formula: VLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20muliple%20criteria.png "Excel formula: VLOOKUP with multiple criteria")](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

### [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

In the example shown, we want to look up employee departments and groups using VLOOKUP by matching the first and last name of an employee. One limitation of VLOOKUP is that it only handles one condition: the lookup\_value, which is matched against the first column in the table. This makes it...

[![Excel formula: XLOOKUP with Boolean OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20boolean%20OR%20logic.png "Excel formula: XLOOKUP with Boolean OR logic")](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)

### [XLOOKUP with Boolean OR logic](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)

In this example, the goal is to use XLOOKUP to find the first "red" or "pink" record in the data as shown. All data is in an Excel Table named data in the range B5:E14. This means the formulas below use structured references . As a result, the formulas will automatically include new data added to...

[![Excel formula: INDEX and MATCH with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20and%20MATCH%20with%20multiple%20criteria.png "Excel formula: INDEX and MATCH with multiple criteria")](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

### [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

This is a more advanced formula. For basics, see How to use INDEX and MATCH . Normally, an INDEX MATCH formula is configured with MATCH set to look through a one-column range and provide a match based on given criteria. Without concatenating values in a helper column , or in the formula itself,...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
    
*   [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
    
*   [XLOOKUP with Boolean OR logic](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)
    
*   [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

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