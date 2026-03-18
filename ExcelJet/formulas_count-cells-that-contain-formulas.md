# Count cells that contain formulas - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-contain-formulas

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-contain-formulas#main-content)

[](https://exceljet.net/formulas/count-cells-that-contain-formulas#)

*   [Previous](https://exceljet.net/formulas/calculate-running-total)
    
*   [Next](https://exceljet.net/formulas/subtotal-by-color)
    

[Sum](https://exceljet.net/formulas#Sum)

Count cells that contain formulas
=================================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISFORMULA](https://exceljet.net/functions/isformula-function)

[NOT](https://exceljet.net/functions/not-function)

![Excel formula: Count cells that contain formulas](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count_cells_that_contain_formulas.png "Excel formula: Count cells that contain formulas")

Summary
-------

To count cells that contain formulas, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 with the [ISFORMULA function](https://exceljet.net/functions/isformula-function)
. In the example shown, the formula in F6 is:

    =SUMPRODUCT(--ISFORMULA(data))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 C5:C16. The result is 4 since the four values in C13:C16 are created with formulas.

Generic formula
---------------

    =SUMPRODUCT(--ISFORMULA(range))

Explanation 
------------

In this example, the goal is to count the number of cells in a range that contain formulas. This problem can be solved with a formula based on the SUMPRODUCT and ISFORMULA functions, as explained below.

### Forecast values

The values in the range C13:C16 are forecasts created with a formula based on the [MROUND function](https://exceljet.net/functions/mround-function)
. The formula in C13, copied down, is:

    =MROUND(C12*1.05,25)
    

This formula generates values that are 5% higher than the previous month, rounded to the nearest multiple of 25.

### ISFORMULA function

The [ISFORMULA function](https://exceljet.net/functions/isformula-function)
 returns TRUE if a cell contains a formula, and FALSE if not. For example, if cell A1 contains the =1+1 the following formula will return TRUE:

    =ISFORMULA(A1) // returns TRUE

if cell A1 contains the number 2 (hard coded), ISFORMULA will return FALSE:

    =ISFORMULA(A1) // returns FALSE

### Count cells with formulas

In the worksheet shown, the range C5:C16 is named "data". To count cells in this range that contain formulas, the formula in cell F6 is:

    =SUMPRODUCT(--ISFORMULA(data))

Working from the inside out, the [ISFORMULA function](https://exceljet.net/functions/isformula-function)
 checks all cells in **data** with this formula:

    ISFORMULA(data)
    

Because there are 12 cells in the range, ISFORMULA returns 12 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE}
    

The FALSE values in this array represent cells that _do not_ contain a formula. Each TRUE value represents a cell that _does_ contain a formula. Notice the last 4 values are TRUE, which makes sense because these cells are forecast values created with a formula. The next step is to convert the TRUE and FALSE values to 1s and 0s. We do this with a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) operation:

    --{FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE}
    

The result is a numeric array that contains only 1s and 0s:

    {0;0;0;0;0;0;0;0;1;1;1;1}
    

This array is delivered directly to the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
:

    =SUMPRODUCT({0;0;0;0;0;0;0;0;1;1;1;1}) // returns 4
    

With only one array to process, SUMPRODUCT simply sums the array and returns a final result of 4.

### Not formulas

To count cells in **data** that do not contain formulas, you can add the [NOT function](https://exceljet.net/functions/not-function)
 like so:

    =SUMPRODUCT(--NOT(ISFORMULA(data)))
    

This is the formula in cell F7. The NOT function _reverses_ the TRUE FALSE results returned by the ISFORMULA function, and returns the resulting array directly to SUMPRODUCT:

    =SUMPRODUCT({1;1;1;1;1;1;1;1;0;0;0;0}) // returns 8
    

As before, SUMPRODUCT sums the values in the array and returns a result of 8.

_Note: in the [dynamic array version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can use the SUM function instead of the SUMPRODUCT function with the same result. To learn more about this topic, see [Why SUMPRODUCT](https://exceljet.net/articles/why-sumproduct)
?_

Related formulas
----------------

[![Excel formula: Sum formulas only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20formulas%20only.png "Excel formula: Sum formulas only")](https://exceljet.net/formulas/sum-formulas-only)

### [Sum formulas only](https://exceljet.net/formulas/sum-formulas-only)

In this example, the goal is to calculate a sum of the values in a range that are generated with a formula. In other words, we want to sum values in a range while ignoring the values that have been entered manually. In the context of this example, the hardcoded values in C5:C12 represent actual...

[![Excel formula: Count cells that contain odd numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20odd%20numbers.png "Excel formula: Count cells that contain odd numbers")](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)

### [Count cells that contain odd numbers](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)

In this example, the goal is to count odd numbers in the range B5:B15, which is named data . This can be done with the SUMPRODUCT function together with the ISODD function. Instead of ISODD, the MOD function can also be used. Both approaches are explained below. SUMPRODUCT with ISODD The SUMPRODUCT...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISFORMULA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isformula%20function.png "Excel ISFORMULA function")](https://exceljet.net/functions/isformula-function)

### [ISFORMULA Function](https://exceljet.net/functions/isformula-function)

The Excel ISFORMULA function returns TRUE if a cell contains a formula, and FALSE if not. When a cell contains a formula ISFORMULA will return TRUE regardless of the formula's output or error conditions.

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20operations%20in%20array%20formulas-Play.png)](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

In this video, we'll look at why boolean operations are important in array formulas. Boolean operations are a key building block in the world of dynamic array formulas. To illustrate, let's look at some simple order data. Given the data shown, how can we total orders from Texas using an array...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum formulas only](https://exceljet.net/formulas/sum-formulas-only)
    
*   [Count cells that contain odd numbers](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISFORMULA Function](https://exceljet.net/functions/isformula-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

### Videos

*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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