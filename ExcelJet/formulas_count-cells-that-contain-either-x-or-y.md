# Count cells that contain either x or y - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y#main-content)

[](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-contain-errors)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that contain either x or y
======================================

by Dave Bruns · Updated 17 Aug 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[FIND](https://exceljet.net/functions/find-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Count cells that contain either x or y](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20contain%20either%20x%20or%20y.png "Excel formula: Count cells that contain either x or y")

Summary
-------

To count cells that contain either x or y, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in cell E5 is:

    =SUMPRODUCT(--((ISNUMBER(FIND("blue",data)) + ISNUMBER(FIND("green",data)))>0))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15. The result is 7, because there are seven cells in the range B5:B15 that contain "blue" or "green". This formula is case-sensitive because the [FIND function](https://exceljet.net/functions/find-function)
 is case-sensitive.

_Note: It is also possible to use a simpler formula based on a [helper column](https://exceljet.net/glossary/helper-column)
, as explained below._

Generic formula
---------------

    =SUMPRODUCT(--((ISNUMBER(FIND("abc",range))+ISNUMBER(FIND("def",range)))>0))

Explanation 
------------

In this example, the goal is to count cells in the range B5:B15 that contain either "x" or "y", where x and y are both [text strings](https://exceljet.net/glossary/text-value)
. When you count cells with "OR logic", you need to be careful not to double count. For example, if you are counting cells that contain "blue" or "green", you can't just add together two COUNTIF functions, because you may double count cells that contain both "blue" and "green". The article below explains two options, a single formula based on the SUMPRODUCT function, and a second option based on the COUNTIF function and a helper column. For convenience, the range B5:B15 is [named](https://exceljet.net/glossary/named-range)
 **data**.

Note: The main formula described on this page is case-sensitive because the [FIND function](https://exceljet.net/functions/find-function)
 is case-sensitive. If you want a formula that is not case-sensitive, you can substitute the [SEARCH function](https://exceljet.net/functions/search-function)
 for the FIND function.

### SUMPRODUCT formula

One way to solve this problem is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 with [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 + [FIND](https://exceljet.net/functions/find-function)
. The formula in E5 is:

    =SUMPRODUCT(--((ISNUMBER(FIND("blue",data))+ISNUMBER(FIND("green",data)))>0))
    

This formula is based on a [formula explained here](https://exceljet.net/formulas/cell-contains-specific-text)
 that finds text in a cell. The main work is done with the [FIND function](https://exceljet.net/functions/find-function)
 and the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
, like this:

    ISNUMBER(FIND("red","A red hat") // returns TRUE
    

FIND returns the number 4 since "red" starts at character 4, and ISNUMBER returns TRUE because 4 is a number. If the text is not found, FIND returns a #VALUE! error and ISNUMBER returns FALSE:

    ISNUMBER(FIND("blue","A red hat") // returns FALSE
    

When given a range of cells, this snippet will return an [array](https://exceljet.net/glossary/array)
 of TRUE/FALSE values, one value for each cell in the range. Going back to the formula in the example, and working from the inside out, we look for "blue" like this:

    ISNUMBER(FIND("blue",data)
    

Since the named range **data** (B5:B15) contains 11 values, we get back an [array](https://exceljet.net/glossary/array)
 with 11 TRUE/FALSE values like this:

    {TRUE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;TRUE}
    

Each TRUE corresponds to a cell in **data** that contains "blue". We look for "green" in the same way:

    ISNUMBER(FIND("green",data)
    

And this snippet also returns an array with 11 results:

    {TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;TRUE}
    

Next, we add these arrays together with the addition [operator](https://exceljet.net/glossary/math-operators)
 (+). The math operation changes the TRUE and FALSE values to 1s and 0s, and the result is a single array:

    {2;1;1;2;0;2;0;0;0;2;2}
    

In this array, a 1 indicates a cell that contains either "blue" or "green" and a 2 indicates a cell that contains both "blue" and "green". Next, we need to add these numbers up, but we don't want to double count. To make sure that any value greater than zero is just counted once, we first force all values to TRUE or FALSE with ">0":

    {2;1;1;2;0;2;0;0;0;2;2})>0
    

This again creates an array of TRUE and FALSE values:

    {TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;TRUE}
    

Because we want numbers, we use a [double-negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to change the TRUE and FALSE values to 1s and 0s to yield an array like this:

    {1;1;1;1;0;1;0;0;0;1;1}
    

In this array, a 1 indicates a cell in data that contains "blue" or "green" and a 0 indicates a cell that does not contain "blue" or "green". To summarize the operations above:

    =SUMPRODUCT(--(({2;1;1;2;0;2;0;0;0;2;2})>0))
    =SUMPRODUCT({1;1;1;1;0;1;0;0;0;1;1})
    

Finally, SUMPRODUCT returns the sum of all values in the array, 7, as a final result.

_Note: this formula is an example of [using Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
 to apply "OR logic" in a formula._ 

### Helper column solution

Another way to solve this problem is with a [helper column](https://exceljet.net/glossary/helper-column)
. This breaks up a more complex problem into parts. To check each cell in B5:B15 for "blue" or "green", we can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 with an [array constant](https://exceljet.net/glossary/array-constant)
 like this:

    =SUM(COUNTIF(B5,{"*blue*","*green*"}))>0
    

Because we give COUNTIF an array that contains two items for criteria, [it returns an array](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)
 that contains two counts: one for "blue" and one for "green". The asterisk (\*) is a [wildcard](https://exceljet.net/glossary/wildcard)
 we can use for a contains search. To prevent double counting, we add the counts up with the [SUM function](https://exceljet.net/functions/sum-function)
 and then force the result to TRUE/FALSE with ">0".  As the formula is copied down, we get a TRUE or FALSE value in column C for each value in column B.

This is how the helper column looks on the worksheet:

![Count cells that contain either x or y with a helper column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20cells%20that%20contain%20either%20x%20or%20y%20helper.png?itok=3tYIvZiq "Count cells that contain either x or y with a helper column")

To sum up all TRUE in C5:C15, we can use the SUMPRODUCT function. The formula in F5 is:

    =SUMPRODUCT(--C5:C15)
    

The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) coerces the TRUE and FALSE values to 1s and 0s:

    =SUMPRODUCT({1;1;1;1;0;1;0;0;0;1;1}) // returns 7
    

and SUMPRODUCT returns 7 as a final result.

Related formulas
----------------

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

[![Excel formula: Count cells equal to this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20this%20or%20that.png "Excel formula: Count cells equal to this or that")](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)

### [Count cells equal to this or that](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)

In this example, the goal is to count cells in the range D5:D15 that contain "red" or "blue". For convenience, the D5:D15 is named color . Counting cells equal to this OR that is more complicated than it first appears because there is no built-in function for counting with OR logic. The COUNTIFS...

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

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

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

*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Count cells equal to this or that](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
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