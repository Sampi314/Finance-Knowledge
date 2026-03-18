# Count or sum variance - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-or-sum-variance

---

[Skip to main content](https://exceljet.net/formulas/count-or-sum-variance#main-content)

[](https://exceljet.net/formulas/count-or-sum-variance#)

*   [Previous](https://exceljet.net/formulas/count-occurrences-in-entire-workbook)
    
*   [Next](https://exceljet.net/formulas/count-or-sum-whole-numbers-only)
    

[Count](https://exceljet.net/formulas#Count)

Count or sum variance
=====================

by Dave Bruns · Updated 22 Jun 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[SUM](https://exceljet.net/functions/sum-function)

[ABS](https://exceljet.net/functions/abs-function)

![Excel formula: Count or sum variance](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20or%20sum%20variance.png "Excel formula: Count or sum variance")

Summary
-------

To count or sum variances, you can use formulas based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and [ABS function](https://exceljet.net/functions/abs-function)
. In the example shown, the formula in F6 sums _absolute_ variances:

    =SUMPRODUCT(ABS(variance))
    

where **variance** is the [named range](https://exceljet.net/glossary/named-range)
 D5:D15. In other words, the result is the sum of the values in D5:D15 converted to absolute values. See below for details about the other formulas that appear in this example.

Explanation 
------------

In this example, the goal is to sum or count a set of variances in different ways. Variances are listed in D5:D15, which is also the [named range](https://exceljet.net/glossary/named-range)
 **variance**. The first formula in F5 simply sums all variances with the [SUM function](https://exceljet.net/functions/sum-function)
.

    =SUM(variance) // returns -175
    

### Sum absolute variances

The formula in F6 calculates the sum of absolute variances with the [ABS function](https://exceljet.net/functions/abs-function)
 together with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
:

    =SUMPRODUCT(ABS(variance)) // returns 975
    

In this formula, ABS returns the absolute value of variances to SUMPRODUCT in a single [array](https://exceljet.net/glossary/array)
:

    =SUMPRODUCT({25;150;200;225;50;100;25;75;0;75;50})
    

SUMPRODUCT then returns the sum, 975.

_Note: we use the SUMPRODUCT function here instead of the SUM function because SUMPRODUCT can handle many [array operations](https://exceljet.net/glossary/array-operation)
 natively without entering the formula in a special way. This means it will work in any version of Excel without special handling. See [Why SUMPRODUCT](https://exceljet.net/articles/why-sumproduct)
 for more information._

### Count non-zero variance

The formula in F7 counts the number of absolute variances that are greater than zero (0):

    =SUMPRODUCT(--(ABS(variance)>0)) // returns 10
    

In this formula, ABS returns the absolute values for all variances in an array as explained above:

    {25;150;200;225;50;100;25;75;0;75;50}
    

A logical expression is used to check for variances greater than zero:

    {25;150;200;225;50;100;25;75;0;75;50}>0
    

This returns an array of TRUE and FALSE values:

    --{TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE}
    

The [double negative](https://exceljet.net/glossary/double-unary)
 (--) converts the TRUE and FALSE values to 1s and 0s and the result is delivered directly to the SUMPRODUCT function:

    =SUMPRODUCT({1;1;1;1;1;1;1;1;0;1;1}) // returns 10
    

which returns a final result of 10.

### Count positive and negative variances

The formula in F8 counts the number of _positive_ variances:

    =SUMPRODUCT(--(variance>0))
    =SUMPRODUCT(--({25;-150;200;-225;-50;100;-25;75;0;-75;-50}>0))
    =SUMPRODUCT({1;0;1;0;0;1;0;1;0;0;0})
    =4
    

The formula in F9 counts _negative_ variances:

    =SUMPRODUCT(--(variance<0))
    =SUMPRODUCT(--({25;-150;200;-225;-50;100;-25;75;0;-75;-50}<0))
    =SUMPRODUCT({0;1;0;1;1;0;1;0;0;1;1})
    =6
    

### Count absolute variance greater than 100

Finally, the formula in F10 counts absolute variances greater than 100:

    =SUMPRODUCT(--(ABS(variance)>100))
    =SUMPRODUCT(--({25;150;200;225;50;100;25;75;0;75;50}>100))
    =SUMPRODUCT({0;1;1;1;0;0;0;0;0;0;0})
    =3
    

### Direct array operation

In the example shown, the variances in column D act as a [helper column](https://exceljet.net/glossary/helper-column)
. However, you can calculate the variances directly in an [array operation](https://exceljet.net/glossary/array-operation)
 if needed with the same results. For example, to count positive variances, the formula in F8 is:

    =SUMPRODUCT(--(variance>0)) // returns 4
    

This formula can be rewritten to calculate variance internally like this:

    =SUMPRODUCT(--(C5:C15-B5:B15>0)) // returns 4
    

The [named range](https://exceljet.net/glossary/named-range)
 **variance** can be replaced with C5:C15-B5:B15 in all formulas above.

Related formulas
----------------

[![Excel formula: Forecast vs actual variance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/forecast%20vs%20actual%20variance.png "Excel formula: Forecast vs actual variance")](https://exceljet.net/formulas/forecast-vs-actual-variance)

### [Forecast vs actual variance](https://exceljet.net/formulas/forecast-vs-actual-variance)

This is a pretty standard use of the SUMIFS function. In this case, we need to sum amounts based on two criteria: type (forecast or actual) and group. To sum by type, the range/criteria pair is: type,G$4 where type is the named range D5:D14, and G4 is a mixed reference with the row locked in order...

[![Excel formula: Calculate percent variance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20percent%20variance.png "Excel formula: Calculate percent variance")](https://exceljet.net/formulas/calculate-percent-variance)

### [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)

In this example, the goal is to calculate the variance between a Forecast (column C) and Actual (column D) as a percentage. For example, with a Forecast value of 100,000 and an Actual value of 112,000, we want to return a variance of 12%. The concept of variance requires a baseline value and a "new...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel ABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20abs%20function.png "Excel ABS function")](https://exceljet.net/functions/abs-function)

### [ABS Function](https://exceljet.net/functions/abs-function)

The Excel ABS function returns the absolute value of a number. ABS converts negative numbers to positive numbers, and positive numbers are unaffected.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Forecast vs actual variance](https://exceljet.net/formulas/forecast-vs-actual-variance)
    
*   [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [ABS Function](https://exceljet.net/functions/abs-function)
    

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