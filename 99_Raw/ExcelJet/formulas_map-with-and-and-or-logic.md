# MAP with AND and OR logic - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/map-with-and-and-or-logic

---

[Skip to main content](https://exceljet.net/formulas/map-with-and-and-or-logic#main-content)

[](https://exceljet.net/formulas/map-with-and-and-or-logic#)

*   [Previous](https://exceljet.net/formulas/list-upcoming-birthdays)
    
*   [Next](https://exceljet.net/formulas/minimum-value-if-unique)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

MAP with AND and OR logic
=========================

by Dave Bruns · Updated 26 Aug 2022

Related functions 
------------------

[MAP](https://exceljet.net/functions/map-function)

[AND](https://exceljet.net/functions/and-function)

[OR](https://exceljet.net/functions/or-function)

![Excel formula: MAP with AND and OR logic](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/map%20with%20and%20and%20or%20logic.png "Excel formula: MAP with AND and OR logic")

Summary
-------

To apply AND and OR logic to an array using the [AND function](https://exceljet.net/functions/and-function)
 and the [OR function](https://exceljet.net/functions/or-function)
, you can use the [MAP function](https://exceljet.net/functions/map-function)
. In the example shown, the formula in cell E5 is:

    =MAP(data[Color],data[Qty],LAMBDA(a,b,AND(OR(a="red",a="blue"),b>10)))
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:C15.

Generic formula
---------------

    =MAP(array1,array2,LAMBDA(a,b,AND(OR(a="red",a="blue"),b>10)))

Explanation 
------------

In this example, the goal is to apply AND and OR logic to an [array](https://exceljet.net/glossary/array)
 using the [AND function](https://exceljet.net/functions/and-function)
 and the [OR function](https://exceljet.net/functions/or-function)
. The challenge is that the AND function and the OR function both _aggregate_ values to a single result. This means you can't use them in an array operation where the goal is to return more than one result. One workaround to this limitation is to use the MAP function, as explained below. All data is in an [Excel Table](https://exceljet.net/glossary/excel-table)
 named **data** in the range B5:C15.

### AND and OR limitations

In this example, we want to test each row in the table with the following logic:  Color is "Red" OR "Blue" AND Qty > 10. For each row in the table, we want a TRUE or FALSE result. If we try to use a formula like this:

    =AND(OR(data[Color]="red",data[Color]="blue"),data[Qty]>10)
    

The formula will fail because the AND function and the OR function both _aggregate_ values to a _single_ result.

### MAP function

One solution to implementing the logic above is to use the [MAP function](https://exceljet.net/functions/map-function)
. The MAP function "maps" a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array. The MAP function is useful when you want to process each item in an array individually, but as an array operation that yields an array result. 

In this example, we supply the MAP function with two arrays: **data\[Color\]**, and **data\[Qty\]**:

    =MAP(data[Color],data[Qty],
    

Next, we need supply a LAMBDA function that implements the logic we need:

    =MAP(data[Color],data[Qty],LAMBDA(a,b,AND(OR(a="red",a="blue"),b>10)))
    

Notice that inside the LAMBDA function, **data\[Color\]** becomes "a", and **data\[Qty\]** becomes "b". These names are arbitrary and you can use any valid name you like . The arrays provided to the MAP function are named by the parameters in the LAMBDA in the order that they appear.

The MAP function works through each value in **data\[Color\]** and **data\[Qty\]** and implements the logic created by the AND and OR functions. Since there are 11 rows in the table, the result is an [array](https://exceljet.net/glossary/array)
 of 11 TRUE and FALSE values like this:

    {FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE}
    

These values are returned to cell E5 and [spill](https://exceljet.net/glossary/spill)
 into the range E5:E15.

### Counting results

The formula in cell G5 shows a practical application of the MAP formula explained above:

    =SUM(MAP(data[Color],data[Qty],LAMBDA(a,b,--AND(OR(a="red",a="blue"),b>10))))
    

Here, the goal is to _count_ all TRUE results from MAP. To do that, we add a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) before the AND function to convert TRUE and FALSE values to 1s and 0s, then we [nest](https://exceljet.net/glossary/nesting)
 the entire formula inside the [SUM function](https://exceljet.net/functions/sum-function)
. The MAP function returns the numeric array to SUM:

    =SUM({0;1;0;1;0;0;0;1;0;0;0}) // returns 3
    

The SUM function then returns a final result of 3.

Related formulas
----------------

[![Excel formula: Count rows with OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20with%20OR%20logic.png "Excel formula: Count rows with OR logic")](https://exceljet.net/formulas/count-rows-with-or-logic)

### [Count rows with OR logic](https://exceljet.net/formulas/count-rows-with-or-logic)

One of the trickier problems in Excel is to count rows in a set of data with "OR logic". There are two basic scenarios: (1) you want to count rows where a value in a column is "x" OR "y" (2) you want to count rows where a value, "x", exists in one column OR another. In this example, the goal is to...

Related functions
-----------------

[![Excel MAP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20map%20function.png "Excel MAP function")](https://exceljet.net/functions/map-function)

### [MAP Function](https://exceljet.net/functions/map-function)

The Excel MAP function "maps" a custom LAMBDA function to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array.

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count rows with OR logic](https://exceljet.net/formulas/count-rows-with-or-logic)
    

### Functions

*   [MAP Function](https://exceljet.net/functions/map-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    

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