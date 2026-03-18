# Range contains one of many substrings - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/range-contains-one-of-many-substrings

---

[Skip to main content](https://exceljet.net/formulas/range-contains-one-of-many-substrings#main-content)

[](https://exceljet.net/formulas/range-contains-one-of-many-substrings#)

*   [Previous](https://exceljet.net/formulas/range-contains-duplicates)
    
*   [Next](https://exceljet.net/formulas/range-contains-one-of-many-values)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Range contains one of many substrings
=====================================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Range contains one of many substrings](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Range%20contains%20one%20of%20many%20substrings.png "Excel formula: Range contains one of many substrings")

Summary
-------

To test a range and determine if it contains one of many substrings (partial matches, specific text, etc.) you can use a formula based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
 nested in the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
.

Generic formula
---------------

    =SUMPRODUCT(COUNTIF(rng,"*"&substrings&"*"))>0

Explanation 
------------

All the hard work is done by the COUNTIF function, which is configured to count the values in the named range "substrings" that appear the [named range](https://exceljet.net/glossary/named-range)
 "rng" with like this:

    COUNTIF(rng,"*"&substrings&"*"))
    

By wrapping substrings in the asterisks, Excel evaluates the formula like this:

    =SUMPRODUCT(COUNTIF(rng,{"*dog*";"*green*";"*sun*";"*every*"}))>0
    

COUNTIF counts the values wherever they appear in the cell. Since we are giving COUNTIF multiple values to look for, we receive a count for each value in an array like this: {1;0;1;1} `.`

Finally, SUMPRODUCT returns the sum of all items in the array. Any result greater than zero returns TRUE.

Related formulas
----------------

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

[![Excel formula: Range contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20specific%20text.png "Excel formula: Range contains specific text")](https://exceljet.net/formulas/range-contains-specific-text)

### [Range contains specific text](https://exceljet.net/formulas/range-contains-specific-text)

The COUNTIF function counts cells that meet supplied criteria, and returns a count of occurrences found. If no cells meet criteria, COUNTIF returns zero. The asterisk (\*) is a wildcard for one or more characters. By concatenating asterisks before and after the value in D5, the formula will count...

[![Excel formula: Range contains one of many values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20one%20of%20many%20values.png "Excel formula: Range contains one of many values")](https://exceljet.net/formulas/range-contains-one-of-many-values)

### [Range contains one of many values](https://exceljet.net/formulas/range-contains-one-of-many-values)

Each item in rng is compared to each item in values and the result is an array of TRUE or FALSE values. The double negative will force the TRUE and FALSE values to 1 and 0 respectively. Since SUMPRODUCT receives just one array, it simply adds up the items in the array and returns the result...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

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
    
*   [Range contains specific text](https://exceljet.net/formulas/range-contains-specific-text)
    
*   [Range contains one of many values](https://exceljet.net/formulas/range-contains-one-of-many-values)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

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