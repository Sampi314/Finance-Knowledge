# Count cells that contain text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-contain-text

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-contain-text#main-content)

[](https://exceljet.net/formulas/count-cells-that-contain-text#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-do-not-contain)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that contain text
=============================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISTEXT](https://exceljet.net/functions/istext-function)

[NOT](https://exceljet.net/functions/not-function)

![Excel formula: Count cells that contain text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20contain%20text.png "Excel formula: Count cells that contain text")

Summary
-------

To count cells in a range that contain [text values](https://exceljet.net/glossary/text-value)
, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 and the asterisk (\*) [wildcard](https://exceljet.net/glossary/wildcard)
. In the example shown, the formula in cell H5 is:

    =COUNTIF(data,"*")
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15. The result is 4 because four cells in the range B5:B15 contain text values.

_Related formulas: [Count cells with specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
, [Count cells that are not empty](https://exceljet.net/formulas/count-cells-that-are-not-blank)
._

Generic formula
---------------

    =COUNTIF(range,"*")

Explanation 
------------

In this example, the goal is to count cells in a range that contain text values. This could be hard-coded text like "apple" or "red", numbers entered as text, or formulas that return text values. Empty cells and cells that contain numeric values or errors should not be included in the count. This problem can be solved with the COUNTIF function or the SUMPRODUCT function. Both approaches are explained below. For convenience, **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15.

### COUNTIF function

The simplest way to solve this problem is with the [COUNTIF function](https://exceljet.net/glossary/wildcard)
 and the asterisk (\*) [wildcard](https://exceljet.net/glossary/wildcard)
. The asterisk (\*) matches zero or more characters of any kind. For example, to count cells in a range that begin with "a", you can use COUNTIF like this:

    =COUNTIF(range,"a*") // begins with "a"
    

In this example, however, we don't want to match any specific text value. We want to match _all_ text values. To do this, we provide the asterisk (\*) by itself for criteria. The formula in H5 is:

    =COUNTIF(data,"*") // any text value
    

The result is 4 because there are four cells in **data** (B5:B15) that contain text values.

To reverse the operation of the formula and count all cells that _do not_ contain text, add the not equal to (<>) [logical operator](https://exceljet.net/glossary/logical-operators)
 like this:

    =COUNTIF(data,"<>*") // non-text values
    

This is the formula used in cell H6. The result is 7, since there are seven cells in **data** (B5:B15) that _do not_ contain text values.

### COUNTIFS function

To apply more specific criteria, you can switch to the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
, which supports multiple conditions. For example, to count cells with text, but exclude cells that contain only a space character, you can use a formula like this:

    =COUNTIFS(range,"*",range,"<> ")
    

This formula will count cells that contain any text value except a single space (" ").

### SUMPRODUCT function

Another way to solve this problem is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 with the [ISTEXT function](https://exceljet.net/functions/istext-function)
.  SUMPRODUCT makes it easy to perform a [logical test](https://exceljet.net/glossary/logical-test)
 on a range, and then count the results. The test is performed with the ISTEXT function. True to its name, the ISTEXT function only returns TRUE when given a text value:

    =ISTEXT("apple")// returns TRUE
    =ISTEXT(70) // returns FALSE
    

To count cells with text values in the example shown, you can use a formula like this:

    =SUMPRODUCT(--ISTEXT(data))
    

Working from the inside out, the logical test is based on the ISTEXT function:

    ISTEXT(data)
    

Because **data** (B5:B15) contains 11 values, ISTEXT returns 11 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {TRUE;TRUE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

In this array, the TRUE values correspond to cells that contain text values, and the FALSE values represent cells that do not contain text. To convert the TRUE and FALSE values to 1s and 0s, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--):

    --{TRUE;TRUE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

The resulting array inside the SUMPRODUCT function looks like this:

    =SUMPRODUCT({1;1;1;0;0;1;0;0;0;0;0}) // returns 4
    

With a single array to process, SUMPRODUCT sums the array and returns 4 as the result.

To reverse the formula and count all cells that _do not_ contain text, you can [nest](https://exceljet.net/glossary/nesting)
 the ISTEXT function inside the [NOT function](https://exceljet.net/functions/not-function)
 like this:

    =SUMPRODUCT(--NOT(ISTEXT(data)))
    

The NOT function reverses the results from ISTEXT. The double negative (--) converts the array to numbers, and the array inside SUMPRODUCT looks like this:

    =SUMPRODUCT({0;0;0;1;1;0;1;1;1;1;1}) // returns 7
    

The result is 7, since there are seven cells in **data** (B5:B15) that _do not_ contain text values.

_Note: the SUMPRODUCT formulas above may seem complex, but u__sing [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
 is powerful and flexible. It is also a__n important skill in modern functions like [FILTER](https://exceljet.net/functions/filter-function)
 and [XLOOKUP](https://exceljet.net/functions/xlookup-function)
, which often use this technique to select the right data. The syntax used by COUNTIF on the other hand is unique to [a group of eight functions](https://exceljet.net/articles/excels-racon-functions)
 and is therefore not as useful or portable._

Related formulas
----------------

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

[![Excel formula: Count cells equal to case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20case%20sensitive.png "Excel formula: Count cells equal to case sensitive")](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)

### [Count cells equal to case sensitive](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)

In this example, the goal is to count codes in a case-sensitive way. The COUNTIF function and the COUNTIFS function are both good options for counting text values, but neither is case-sensitive, so they can't be used to solve this problem. The solution is to use the EXACT function to compare codes...

[![Excel formula: Count cells that contain numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20numbers.png "Excel formula: Count cells that contain numbers")](https://exceljet.net/formulas/count-cells-that-contain-numbers)

### [Count cells that contain numbers](https://exceljet.net/formulas/count-cells-that-contain-numbers)

In this example, the goal is to count the number of cells in a range that contain numbers. This problem can be solved with the COUNT function or the SUMPRODUCT function. Both methods are explained below. COUNT function The COUNT function counts the number of cells in a range that contain numeric...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20istext%20function.png "Excel ISTEXT function")](https://exceljet.net/functions/istext-function)

### [ISTEXT Function](https://exceljet.net/functions/istext-function)

The Excel ISTEXT function returns TRUE when a cell contains a [text value](https://exceljet.net/glossary/text-value)
, and FALSE if the cell contains any other value. You can use the ISTEXT function to check if a cell contains a text value, or a numeric value entered as text.

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Count cells equal to case sensitive](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
    
*   [Count cells that contain numbers](https://exceljet.net/formulas/count-cells-that-contain-numbers)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISTEXT Function](https://exceljet.net/functions/istext-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

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