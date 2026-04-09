# Count if row meets multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-if-row-meets-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria#main-content)

[](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)
    
*   [Next](https://exceljet.net/formulas/count-if-two-criteria-match)
    

[Count](https://exceljet.net/formulas#Count)

Count if row meets multiple criteria
====================================

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7364/download?token=JwRcCW0i)
 (18.42 KB)

![Excel formula: Count if row meets multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20if%20row%20meets%20multiple%20criteria.png "Excel formula: Count if row meets multiple criteria")

Summary
-------

To count rows in a table that meet multiple criteria, without using a [helper column](https://exceljet.net/glossary/helper-column)
, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in cell H5 is:

    =SUMPRODUCT((E5:E15="tx")*(C5:C15>100)*(MONTH(F5:F15)=3))
    

The result is 2, since there are two rows where the state is Texas ("TX"), the amount is greater than 100, and the month is March.

Generic formula
---------------

    =SUMPRODUCT((logical1)*(logical2)*(logical3))

Explanation 
------------

In this example, the goal is to count orders (rows)  where the state is Texas ("TX"), the amount is greater than $100, and the month is March. In this case, we can't use [COUNTIFS](https://exceljet.net/functions/countifs-function)
, because COUNTIFS is a [range-based function](https://exceljet.net/articles/excels-racon-functions)
 and it won't accept a calculation for a _range_ argument, which we need to determine the month. We could optionally add a [helper column](https://exceljet.net/glossary/helper-column)
 that uses the MONTH function to extract the month, then use COUNTIFS, but a better option is to use the SUMPRODUCT function with [Boolean logic](https://exceljet.net/glossary/boolean-logic)
.

### COUNTIFS function

You would think the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 would be the perfect tool for this job, but if we try to use COUNTIFS, we'll run into a problem. The first two conditions are straightforward. We can count orders from Texas ("TX") with amounts greater than $100, like this:

    =COUNTIFS(E5:E15,"tx",C5:C15,">100") // returns 4
    

COUNTIFS returns 4, since there are 4 orders that meet these conditions. However,  when we try to extend the criteria to test for orders in March, we run into a problem. The formula below looks fine, but Excel will not let you enter it:

    =COUNTIFS(E5:E15,"tx",C5:C15,">100",MONTH(F5:F15),3)
    

Instead, Excel displays the generic "There's a problem with this formula error" message. This happens because [COUNTIFS is a range-based function](https://exceljet.net/articles/excels-racon-functions)
 and it won't accept the [array](https://exceljet.net/glossary/array)
 returned by the MONTH function above. The SUMPRODUCT function does not have this limitation and is happy to work with ranges _or_ arrays.

### SUMPRODUCT function

The [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 is programmed to handle [array operations](https://exceljet.net/glossary/array-operation)
 natively, without requiring Control + Shift + Enter. Its default behavior is to multiply corresponding elements in one or more [arrays](https://exceljet.net/glossary/array)
 together, then sum the products. When given a single array, it returns the sum of the elements in the array. In the example shown, the formula in H5 is:

    =SUMPRODUCT((E5:E15="tx")*(C5:C15>100)*(MONTH(F5:F15)=3))
    

In this example, we are using three logical expressions inside a single array [argument](https://exceljet.net/glossary/function-argument)
, _array1_. This is typical when using SUMPRODUCT to solve a problem like this because it saves steps and provides full control over the logic used to select data. We could place each expression into a separate argument, but then we would need to coerce logical TRUE and FALSE values to 1s and 0s with another operator like the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--). By placing all expressions into one argument, the math operation of [multiplication](https://exceljet.net/glossary/math-operators)
 (\*) will automatically convert TRUE and FALSE to 1 and 0.

We have three conditions to apply. The first condition is that the order is from Texas ("TX"):

    E5:E15="tx" // state is "tx"
    

Excel formulas are not case-sensitive, so there is no need to use an uppercase "TX". Because the range E5:E15 contains 11 values, the result is an [array](https://exceljet.net/glossary/array)
 that contains 11 TRUE and FALSE values:

    {TRUE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE}
    

The second condition is that the amount is greater than $100:

    C5:C15>100 // amount > 100
    

This expression also returns 11 results:

    {TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE}
    

The third condition is that the month is March. To get the month, we use the [MONTH function](https://exceljet.net/functions/month-function)
, which returns a number between 1-12 when given a date:

    MONTH(F5:F15)=3 // month is 3
    

The MONTH function returns an array of 11 month numbers:

    ={2;2;2;3;3;3;3;3;3;4;4}=3
    

And the full expression returns this array:

    {FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE}
    

All three [arrays](https://exceljet.net/glossary/array)
 are multiplied together because all conditions must be TRUE in order to be included in the final count. In Boolean algebra, [multiplication (\*) corresponds to AND logic](https://exceljet.net/videos/boolean-algebra-in-excel)
 and addition (+) corresponds to OR logic. The math operation automatically converts the TRUE and FALSE values to 1s and 0s. You can visualize the arrays inside of SUMPRODUCT like this:

    =SUMPRODUCT({1;0;0;1;1;0;1;0;0;1;0}*{1;1;0;1;0;0;1;1;1;1;1}*{0;0;0;1;1;1;1;1;1;0;0})
    

After the corresponding values of each array are multiplied together, we have a single array inside the SUMPRODUCT function like this:

    =SUMPRODUCT({0;0;0;1;0;0;1;0;0;0;0}) // returns 2
    

With only one array to process, SUMPRODUCT sums the array and returns 2 as a final result.

_Note: The SUMPRODUCT function has been traditionally used to solve problems like this because it has always been able to handle [array operations](https://exceljet.net/glossary/array-operation)
 natively, without Control + Shift + Enter. In [Excel 365](https://exceljet.net/glossary/excel-365)
 and Excel 2021, [arrays are native](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 and [you can use the SUM function instead if you prefer](https://exceljet.net/articles/why-sumproduct)
._

Related formulas
----------------

[![Excel formula: Count if row meets internal criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20if%20row%20meets%20internal%20criteria.png "Excel formula: Count if row meets internal criteria")](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)

### [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)

In this example the goal is to count products (rows) where sales have increased and sales have decreased, where previous sales are in column C (Previous) and current sales are in column D (Current). In this case, we can't use COUNTIFS directly, because COUNTIFS is a range-based function and it won'...

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

*   [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)
    
*   [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Videos

*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    

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