# Count cells between two numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-between-two-numbers

---

[Skip to main content](https://exceljet.net/formulas/count-cells-between-two-numbers#main-content)

[](https://exceljet.net/formulas/count-cells-between-two-numbers#)

*   [Previous](https://exceljet.net/formulas/count-cells-between-dates)
    
*   [Next](https://exceljet.net/formulas/count-cells-equal-to)
    

[Count](https://exceljet.net/formulas#Count)

Count cells between two numbers
===============================

by Dave Bruns · Updated 15 Aug 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count cells between two numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Count%20cells%20between%20two%20numbers_0.png "Excel formula: Count cells between two numbers")

Summary
-------

To count the number of cells that contain values between two numbers, you can use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. In the generic form of the formula (above), **range** represents a range of cells that contain numbers, A1 represents the lower boundary, and B1 represents the upper boundary of the numbers you want to count. In the example shown, the formula in G5, copied down, is:

    =COUNTIFS(data,">="&E5,data,"<="&F5)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 C5:C16. As the formula is copied down, it returns a count for each of the number ranges shown in columns E and F.

Generic formula
---------------

    =COUNTIFS(range,">="&A1,range,"<"&B1)

Explanation 
------------

In this example, the goal is to count numbers that fall within specific ranges. The lower value comes from the "Start" column, and the upper value comes from the "End" column. For each range, we want to _include_ both the lower value and the upper value. For convenience, the numbers being counted are in the [named range](https://exceljet.net/glossary/named-range)
 **data** (C5:C16). This problem can be solved with both the COUNTIFS function and the SUMPRODUCT function, as explained below.

### COUNTIFS function

In the example shown, the formula used to solve this problem is based on the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
, which is designed to count cells that meet multiple criteria. The formula in cell G5, copied down, is:

    =COUNTIFS(data,">="&E5,data,"<="&F5)
    

COUNTIFS accepts criteria in range/criteria pairs. The first range/criteria pair checks for values in **data** that are greater than or equal to (>=) the "Start" value in column E:

    data,">="&E5
    

The second range/criteria pair checks for values in **data** that are less than or equal to (<=) the "End" value in column F:

    data,"<="&F5
    

Because we supply the same range (**data**) for both criteria, each cell in **data** must meet both conditions in order to be included in the final count. Note in both cases, we need to [concatenate](https://exceljet.net/glossary/concatenation)
 the cell reference to the [logical operator](https://exceljet.net/glossary/logical-operators)
. This is a quirk of [RACON functions in Excel](https://exceljet.net/articles/excels-racon-functions)
, which use a different syntax than other formulas.

As the formula is copied down column G, it returns the count of numbers that fall in the range defined by columns E and F.

### SUMPRODUCT alternative

Another option for solving this problem is the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 with a formula like this:

    =SUMPRODUCT((data>=E5)*(data<=F5))
    

This is an example of using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
.  Because there are 12 values in the named range **data**, each logical expression inside SUMPRODUCT generates an [array](https://exceljet.net/glossary/array)
 that contains 12 TRUE and FALSE values. The expression:

    data>=E5
    

returns:

    {TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE}
    

And the expression:

    data<=F5
    

returns:

    {TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;TRUE;FALSE}
    

When these two arrays are multiplied together, the math operation causes TRUE values to be coerced to 1 and FALSE values to be coerced to zero. The result is a single array of 1s and 0s like this:

    =SUMPRODUCT({1;0;0;0;1;0;0;0;1;0;1;0})
    

Each 1 corresponds to a number in **data** that meets both conditions and each 0 represents a number that fails at least one condition. With only a single array to process, SUMPRODUCT returns the sum of the numbers in the array, 4, as a final result.

Video: [Boolean logic in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

### Benefits of standard syntax

The nice thing about SUMPRODUCT is that it will handle array operations natively (no need to enter with control + shift + enter) and will accept the more standard syntax for logical expressions seen above. The standard syntax is more useful in other modern formulas. For example you could use the same exact logic with the [FILTER function](https://exceljet.net/functions/filter-function)
 to return the actual numbers that meet these same conditions:

    =FILTER(data,(data>=E5)*(data<=F5))
    

Becomes:

    =FILTER(data,{1;0;0;0;1;0;0;0;1;0;1;0})
    

And FILTER returns the numbers greater than or equal to 70 and less than or equal to 79:

    {79;77;75;70}
    

Video: [Basic FILTER function example](https://exceljet.net/videos/filter-function-basic-example)

Related formulas
----------------

[![Excel formula: Count cells between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20dates_0.png "Excel formula: Count cells between dates")](https://exceljet.net/formulas/count-cells-between-dates)

### [Count cells between dates](https://exceljet.net/formulas/count-cells-between-dates)

In this example, the goal is to count the number of cells in column D that contain dates that are between two variable dates in G4 and G5. This problem can be solved with the COUNTIFS function or the SUMPRODUCT function, as explained below. For convenience, the worksheet contains two named ranges...

[![Excel formula: Highlight values between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20between.png "Excel formula: Highlight values between")](https://exceljet.net/formulas/highlight-values-between)

### [Highlight values between](https://exceljet.net/formulas/highlight-values-between)

When you use a formula to apply conditional formatting, the formula is evaluated for each cell in the range, relative to the active cell in the selection at the time the rule is created. So, in this case, if you apply the rule to B4:G11, with B4 as the active cell, the rule is evaluated for each of...

[![Excel formula: Count matches between two columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20matches%20between%20two%20columns.png "Excel formula: Count matches between two columns")](https://exceljet.net/formulas/count-matches-between-two-columns)

### [Count matches between two columns](https://exceljet.net/formulas/count-matches-between-two-columns)

In this example, the goal is to compare two columns and return the count of matches in corresponding rows. A good way to solve this problem is to use the SUMPRODUCT function or the SUM function, as explained below. SUMPRODUCT function The SUMPRODUCT function is a versatile function that handles...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

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

*   [Count cells between dates](https://exceljet.net/formulas/count-cells-between-dates)
    
*   [Highlight values between](https://exceljet.net/formulas/highlight-values-between)
    
*   [Count matches between two columns](https://exceljet.net/formulas/count-matches-between-two-columns)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Articles

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