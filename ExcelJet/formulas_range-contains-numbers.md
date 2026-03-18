# Range contains numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/range-contains-numbers

---

[Skip to main content](https://exceljet.net/formulas/range-contains-numbers#main-content)

[](https://exceljet.net/formulas/range-contains-numbers#)

*   [Previous](https://exceljet.net/formulas/range-contains-a-value-not-in-another-range)
    
*   [Next](https://exceljet.net/formulas/range-contains-specific-date)
    

[Range](https://exceljet.net/formulas#Range)

Range contains numbers
======================

by Dave Bruns · Updated 24 Oct 2019

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: Range contains numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/range%20contains%20numbers.png "Excel formula: Range contains numbers")

Summary
-------

To test a range for numbers, you can use a formula based on the ISNUMBER and SUMPRODUCT functions. In the example shown, the formula in G5 is:

    =SUMPRODUCT(--ISNUMBER(C5:C9))>0
    

Generic formula
---------------

    =SUMPRODUCT(--ISNUMBER(range))>0

Explanation 
------------

Working from the inside out, the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 will return TRUE when given a number and FALSE if not. When you supply a range to ISNUMBER (i.e. an [array](https://exceljet.net/glossary/array)
), ISNUMBER will return an array of results. In the example, the range C5:C9 contains 5 cells, so the array returned by ISNUMBER contains 5 results:

    {FALSE;FALSE;FALSE;TRUE;FALSE}
    

TRUE values represent numeric values.

We want to know if this result contains _any_ TRUE values, so we use the [double negative operator](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to force the TRUE and FALSE values to 1 and 0 respectively. This is an example of [boolean logic](https://exceljet.net/glossary/boolean-logic)
, and the result is an array of 1's and 0's:

    {0;0;0;1;0}
    

We use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to sum the array:

    =SUMPRODUCT({0;0;0;1;0})
    

Any sum greater than zero means at least one number exists in the range, so we use ">0" to force a final result of TRUE or FALSE.

Related formulas
----------------

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

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