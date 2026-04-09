# Count cells that contain numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-contain-numbers

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-contain-numbers#main-content)

[](https://exceljet.net/formulas/count-cells-that-contain-numbers#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that contain numbers
================================

by Dave Bruns · Updated 17 Aug 2022

Related functions 
------------------

[COUNT](https://exceljet.net/functions/count-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: Count cells that contain numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20contain%20numbers.png "Excel formula: Count cells that contain numbers")

Summary
-------

To count numbers in a [range](https://exceljet.net/glossary/range)
, you can use the [COUNT function](https://exceljet.net/functions/count-function)
. In the example shown, cell E6 contains this formula

    =COUNT(B5:B15)
    

The result is 8, since there are eight cells in the range B5:B15 that contain numeric values.

Generic formula
---------------

    =COUNT(range)

Explanation 
------------

In this example, the goal is to count the number of cells in a [range](https://exceljet.net/glossary/range)
 that contain numbers. This problem can be solved with the COUNT function or the SUMPRODUCT function. Both methods are explained below.

### COUNT function

The [COUNT function](https://exceljet.net/functions/count-function)
 counts the number of cells in a range that contain numeric values. In this example, we simply need to give COUNT the range B5:B15:

    =COUNT(B5:B15) // returns 8
    

The COUNT function is fully automatic, so there is nothing to configure. The result is 8, since there are eight cells in the range B5:B15 that contain numeric values. Cell B9 is not included because it is empty. Cells B11 and B12 are not included because they contain [text values](https://exceljet.net/glossary/text-value)
.

_Note: the [COUNTA function](https://exceljet.net/functions/counta-function)
 counts numbers and text, but does not count empty cells._

### SUMPRODUCT function

Another way to solve this problem is with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and [Boolean algebra](https://exceljet.net/glossary/boolean-logic)
:

    =SUMPRODUCT(--ISNUMBER(B5:B15))
    

Working from the inside out, the ISNUMBER function is used to test the values in B5:B15:

    ISNUMBER(B5:B15)
    

Because the range B5:B15 contains 11 values, the result is an [array](https://exceljet.net/glossary/array)
 that contains 11 TRUE and FALSE values:

    {TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;TRUE;TRUE}
    

The TRUE values correspond to cells that contain numbers, and the FALSE values represent cells that do not contain numbers. To convert the TRUE and FALSE values to 1s and 0s, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--):

    --{TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;TRUE;TRUE}
    

The resulting array inside the SUMPRODUCT function looks like this:

    =SUMPRODUCT({1;1;1;1;0;1;0;0;1;1;1}) // returns 8
    

With a single array to process, SUMPRODUCT sums the array and returns 8 as the result.

_Note: you might wonder why you should go to the trouble of using SUMPRODUCT and Boolean logic, when the COUNT function will do the job? The main reason is flexibility and extensibility. SUMPRODUCT can easily perform calculations that the COUNT function, or even COUNTIF or COUNTIFS simply can't perform. One example is the formula below, which adds the NOT function to reverse behavior. Another basic example [is this formula](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)
, which uses the ISODD function to count odd numbers._

### Count cells that do not contain numbers

To count the number of cells in a range that _do not_ contain numbers, you can modify the SUMPRODUCT formula above to use the [NOT function](https://exceljet.net/functions/not-function)
 like this:

    =SUMPRODUCT(--NOT(ISNUMBER(B5:B15)))
    

The NOT function reverses the output from ISNUMBER, and the final array inside SUMPRODUCT looks like this:

    =SUMPRODUCT({0;0;0;0;1;0;1;1;0;0;0}) // returns 3
    

The result is 3, since there are three cells in B5:B15 that do not contain numbers.

Related formulas
----------------

[![Excel formula: Count cells that contain positive numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cell%20that%20contain%20positive%20numbers.png "Excel formula: Count cells that contain positive numbers")](https://exceljet.net/formulas/count-cells-that-contain-positive-numbers)

### [Count cells that contain positive numbers](https://exceljet.net/formulas/count-cells-that-contain-positive-numbers)

In this example, the goal is to count the number of cells in a range that contain positive numbers. For convenience, the range B5:B15 is named data . This problem can be solved with the COUNTIF function or the SUMPRODUCT function. Both methods are explained below. COUNTIF function The COUNT...

[![Excel formula: Count cells that contain negative numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20negative%20numbers.png "Excel formula: Count cells that contain negative numbers")](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)

### [Count cells that contain negative numbers](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)

In this example, the goal is to count the number of cells in a range that contain negative numbers. For convenience, the range B5:B15 is named data . This problem can be solved with the COUNTIF function or the SUMPRODUCT function. Both methods are explained below. COUNTIF function The COUNT...

[![Excel formula: Count cells that contain errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20errors.png "Excel formula: Count cells that contain errors")](https://exceljet.net/formulas/count-cells-that-contain-errors)

### [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)

In this example, the goal is to count errors in the range B5:B15, which is named data for convenience. The article below explains several different approaches, depending on your needs. For background, this article: Excel Formula Errors . COUNTIF function One way to count individual errors is with...

[![Excel formula: Count cells that contain text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20text.png "Excel formula: Count cells that contain text")](https://exceljet.net/formulas/count-cells-that-contain-text)

### [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)

In this example, the goal is to count cells in a range that contain text values. This could be hard-coded text like "apple" or "red", numbers entered as text, or formulas that return text values. Empty cells and cells that contain numeric values or errors should not be included in the count. This...

Related functions
-----------------

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

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

*   [Count cells that contain positive numbers](https://exceljet.net/formulas/count-cells-that-contain-positive-numbers)
    
*   [Count cells that contain negative numbers](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)
    
*   [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)
    
*   [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)
    

### Functions

*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

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