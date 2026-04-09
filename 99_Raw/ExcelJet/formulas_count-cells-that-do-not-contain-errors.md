# Count cells that do not contain errors - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-do-not-contain-errors

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors#main-content)

[](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-do-not-contain)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that do not contain errors
======================================

by Dave Bruns · Updated 25 May 2022

Related functions 
------------------

[ISERROR](https://exceljet.net/functions/iserror-function)

[NOT](https://exceljet.net/functions/not-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISERR](https://exceljet.net/functions/iserr-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Count cells that do not contain errors](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20do%20not%20contain%20errors.png "Excel formula: Count cells that do not contain errors")

Summary
-------

To count the number of cells that _do not_ contain errors, you can use the [ISERROR](https://exceljet.net/functions/iserror-function)
 and [NOT](https://exceljet.net/functions/not-function)
 functions, wrapped in the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in E5 is:

    =SUMPRODUCT(--NOT(ISERROR(B5:B14)))
    

The result is 7, since there are seven cells in B5:B14 that do not contain error values.

Generic formula
---------------

    =SUMPRODUCT(--NOT(ISERROR(range)))

Explanation 
------------

In this example, the goal is to count the number of cells in a range that _do not_ contain errors. The best way to solve this problem is to use the SUMPRODUCT function together with the ISERROR function. You can also use the COUNTIF function or COUNTIFS function to exclude specific errors. Both approaches are explained below.

### COUNTIF function

One way to count cells that do not contain errors is to use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 like this:

    =COUNTIF(B5:B14,"<>#N/A") // returns 9
    

For criteria, we use the not equal to operator (<>) with #N/A. Notice both values are enclosed in double quotes. COUNTIF returns 9 since there are nine cells in B5:B15 that do not contain the #N/A error. If we switch to the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
, we can exclude more than one kind of error like this:

    =COUNTIFS(B5:B14,"<>#N/A",B5:B14,"<>#VALUE!") // returns 8
    

COUNTIFS returns 9 since there are eight cells in B5:B15 that do not contain the #N/A error or the #VALUE! error. However, this approach is tedious if the goal is to exclude all types of errors from the count. In that case, the SUMPRODUCT option below is more straightforward.

### SUMPRODUCT function

The SUMPRODUCT function works directly with arrays and ranges. One thing you can do quite easily with SUMPRODUCT is perform a logical test on a range, then count the results. In this case, we want to count cells that do not contain errors and the simplest way to do that is with the ISERROR function and the NOT function. In the worksheet shown above, the formula in cell E5 is:

    =SUMPRODUCT(--NOT(ISERROR(B5:B14)))
    

Working from the inside out, we first use the [ISERROR function](https://exceljet.net/functions/iserror-function)
 on the range B5:B14.

    ISERROR(B5:B14) // check all 10 cells
    

Since there are ten cells in the range B5:B14, ISERROR returns an [array](https://exceljet.net/glossary/array)
 with ten results like this:

    {FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE}
    

Here, each TRUE value indicates a cell value that _is_ an error. Since the goal is to count cells that _do not_ contain errors, we reverse these results with the [NOT function](https://exceljet.net/functions/not-function)
:

    NOT({FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE})
    

which returns a new array like this:

    {TRUE;FALSE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;FALSE}
    

Notice that each TRUE value now corresponds to a cell that _does not_ contain an error. This array is now in the correct form. However, SUMPRODUCT only works with numeric data so the next step is to convert the TRUE and FALSE values to their numeric equivalents, 1 and 0. We do this with a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--):

    --{TRUE;FALSE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;FALSE}
    

The resulting array looks like this:

    {1;0;1;1;1;0;1;1;1;0}
    

Finally, SUMPRODUCT sums the items in this array and returns the total, which in the example is the number 3:

    =SUMPRODUCT({1;0;1;1;1;0;1;1;1;0}) // returns 7
    

### ISERR function

Like the ISERROR function, the [ISERR function](https://exceljet.net/functions/iserr-function)
 returns TRUE when a value is an error. The difference is that ISERR ignores #N/A errors. If you want to count cells that do not contain errors, and ignore #N/A errors, you can substitute ISERR for ISERROR:

    =SUMPRODUCT(--NOT(ISERR(B5:B14))) // returns 8
    

SUMPRODUCT returns 8 since there are eight cells that do not contain errors, ignoring the #N/A error in cell B14.

Related formulas
----------------

[![Excel formula: Count cells that contain errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20errors.png "Excel formula: Count cells that contain errors")](https://exceljet.net/formulas/count-cells-that-contain-errors)

### [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)

In this example, the goal is to count errors in the range B5:B15, which is named data for convenience. The article below explains several different approaches, depending on your needs. For background, this article: Excel Formula Errors . COUNTIF function One way to count individual errors is with...

[![Excel formula: Count cells that contain numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20numbers.png "Excel formula: Count cells that contain numbers")](https://exceljet.net/formulas/count-cells-that-contain-numbers)

### [Count cells that contain numbers](https://exceljet.net/formulas/count-cells-that-contain-numbers)

In this example, the goal is to count the number of cells in a range that contain numbers. This problem can be solved with the COUNT function or the SUMPRODUCT function. Both methods are explained below. COUNT function The COUNT function counts the number of cells in a range that contain numeric...

Related functions
-----------------

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISERR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserr%20function.png "Excel ISERR function")](https://exceljet.net/functions/iserr-function)

### [ISERR Function](https://exceljet.net/functions/iserr-function)

The Excel ISERR function returns TRUE for any error type except the #N/A error. You can use the ISERR function together with the IF function to test for an error and display a custom message, or perform a different calculation if found.

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

*   [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)
    
*   [Count cells that contain numbers](https://exceljet.net/formulas/count-cells-that-contain-numbers)
    

### Functions

*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISERR Function](https://exceljet.net/functions/iserr-function)
    
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