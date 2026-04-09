# Count cells equal to this or that - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-equal-to-this-or-that

---

[Skip to main content](https://exceljet.net/formulas/count-cells-equal-to-this-or-that#main-content)

[](https://exceljet.net/formulas/count-cells-equal-to-this-or-that#)

*   [Previous](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)
    
*   [Next](https://exceljet.net/formulas/count-cells-greater-than)
    

[Count](https://exceljet.net/formulas#Count)

Count cells equal to this or that
=================================

by Dave Bruns · Updated 17 Aug 2022

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUM](https://exceljet.net/functions/sum-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count cells equal to this or that](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20equal%20to%20this%20or%20that.png "Excel formula: Count cells equal to this or that")

Summary
-------

To count the number of cells equal to one value OR another value, you can use a formula based on the COUNTIF function. In the example shown, the formula in H6 is:

    =SUM(COUNTIF(color,{"red","blue"}))
    

where **color** is the [named range](https://exceljet.net/glossary/named-range)
 D5:D15. The result is 7, since "red" appears 4 times and "blue" appears 3 times in the range D5:D16. See below for an explanation and for other ways to solve this problem.

_Note: we are using COUNTIF in this example since it does what we need, but the [COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)
 would work equally well. Also note that because we are counting text values "red" and "blue" are enclosed in double quotes. If we were counting numbers, the quotes would not be needed._

Generic formula
---------------

    =SUM(COUNTIF(range,{"value1","value2"}))

Explanation 
------------

In this example, the goal is to count cells in the range D5:D15 that contain "red" or "blue". For convenience, the D5:D15 is [named](https://exceljet.net/glossary/named-range)
 **color**. Counting cells equal to this OR that is more complicated than it first appears because there is no built-in function for counting with OR logic. The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 will allow multiple conditions, but all conditions are joined with AND logic. The article below explains several options.

### COUNTIF + COUNTIF

A simple, manual way to count with OR is to use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 more than once:

    =COUNTIF(color,"red") + COUNTIF(color,"blue")
    

In both cases, the _range_ argument inside COUNTIF is **color** (D5:D15). However, _criteria_ is "red" in the first COUNTIF and "blue" in the second. The first COUNTIF returns 4 and the second COUNTIF returns 3, so the final result is 7. This formula works fine, but it is somewhat redundant.

### COUNTIF with array constant

Another way to configure COUNTIF is with an [array constant](https://exceljet.net/glossary/array-constant)
 that contains more than one value to use for _criteria_. This is the method used in the example shown above:

    =SUM(COUNTIF(color,{"red","blue"}))
    

Inside the SUM function, the COUNTIF function is given **color** (D5:D16) for _range_ and {"red","blue"} for _criteria_:

    COUNTIF(color,{"red","blue"}) // returns {4,3}
    

This causes the COUNTIF function to return two counts: one for "red" and one for "blue". These counts are returned directly to the [SUM function](https://exceljet.net/videos/how-to-use-the-sum-function)
 in a single [array](https://exceljet.net/glossary/array)
:

    =SUM({4,3}) // returns 7
    

And SUM returns 7 as the result. In other words, COUNTIF returns multiple counts to SUM, and SUM returns a final result. This is an example of [nesting](https://exceljet.net/glossary/nesting)
 one formula inside another.

For more complicated scenarios, see: [COUNTIFS with multiple criteria and or logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

### SUMPRODUCT function

Another way to solve this problem is with the SUMPRODUCT function like this:

    =SUMPRODUCT((D5:D15="red")+(D5:D15="blue"))
    

This is an example of using Boolean logic. Inside SUMPRODUCT there are two expressions joined by the addition (+) [operator](https://exceljet.net/glossary/math-operators)
. Because color contains 11 values, each expression creates an [array](https://exceljet.net/glossary/array)
 with 11 TRUE and FALSE values:

    =SUMPRODUCT({TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE}+{FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE})
    

In the first array, the TRUE values correspond to cells that contain "red". In the second array, the TRUE values correspond to cells that contain "blue". When the two arrays are added together, the math operation converts the TRUE and FALSE values to 1s and 0s:

    =SUMPRODUCT({1;1;1;0;1;0;1;0;1;1;0})
    

With just one array to process SUMPRODUCT sums the items in the array and returns 7 as a result. Another way to configure SUMPRODUCT is like this:

    =SUMPRODUCT(--(D5:D15={"red","blue"}))
    

In this formula, the expression:

    D5:D15={"red","blue"})
    

Returns a single array with 11 rows and 2 columns. The double negative coerces the TRUE and FALSE values to 1s and 0s:

    =SUMPRODUCT({1,0;1,0;0,1;0,0;0,1;0,0;1,0;0,0;0,1;1,0;0,0})
    

And SUMPRODUCT again returns 7 as a final result.

For more complex scenarios see: [SUMPRODUCT with multiple criteria and OR logic](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
 and [Count cells equal to one of many things](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)
.

### Double-counting risk

When counting with OR logic, be aware of the risk of double-counting. In this particular example, the values "red" and "blue" are values in the _same_ field, so there is no danger in double-counting. However, if you are counting records where one field is "red" OR _another_ field is "blue", [take care not to double-count](https://exceljet.net/formulas/count-rows-with-or-logic)
, since both can be true at the same time in the same record.

Related formulas
----------------

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

[![Excel formula: COUNTIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/COUNTIFS%20with%20multiple%20criteria%20and%20OR%20logic.png "Excel formula: COUNTIFS with multiple criteria and OR logic")](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

### [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

In this example, the goal is to use the COUNTIFS function to count data with "OR logic". The challenge is the COUNTIFS function applies AND logic by default. COUNTIFS function The COUNTIFS function returns the count of cells that meet one or more criteria, and supports logical operators (>,...

[![Excel formula: Count cells equal to one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20one%20of%20many%20things.png "Excel formula: Count cells equal to one of many things")](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)

### [Count cells equal to one of many things](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)

In this example, the goal is to count the values in column B listed in the range E5:E7. One way to do this is to give the COUNTIF function all three values in the named range things (E5:E7) as criteria, then use the SUMPRODUCT function to get a total. The formula in G4 is: =SUMPRODUCT(COUNTIF(B5:...

[![Excel formula: Range contains one of many values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20one%20of%20many%20values.png "Excel formula: Range contains one of many values")](https://exceljet.net/formulas/range-contains-one-of-many-values)

### [Range contains one of many values](https://exceljet.net/formulas/range-contains-one-of-many-values)

Each item in rng is compared to each item in values and the result is an array of TRUE or FALSE values. The double negative will force the TRUE and FALSE values to 1 and 0 respectively. Since SUMPRODUCT receives just one array, it simply adds up the items in the array and returns the result...

[![Excel formula: SUMPRODUCT count multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT%20count%20multiple%20OR%20criteria2.png "Excel formula: SUMPRODUCT count multiple OR criteria")](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

### [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

In this example, the goal is to count rows where the value in column one is "A" or "B" and the value in column two is "X", "Y", or "Z". In the worksheet shown, we are using array constants to hold the values of interest, but the article also shows how to use cell references instead. In simple...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

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
    
*   [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
    
*   [Count cells equal to one of many things](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)
    
*   [Range contains one of many values](https://exceljet.net/formulas/range-contains-one-of-many-values)
    
*   [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

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