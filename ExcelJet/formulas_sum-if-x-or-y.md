# Sum if x or y - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-x-or-y

---

[Skip to main content](https://exceljet.net/formulas/sum-if-x-or-y#main-content)

[](https://exceljet.net/formulas/sum-if-x-or-y#)

*   [Previous](https://exceljet.net/formulas/sum-if-with-multiple-ranges)
    
*   [Next](https://exceljet.net/formulas/sum-last-30-days)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if x or y
=============

by Dave Bruns · Updated 20 Dec 2022

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")

Summary
-------

To sum numbers when corresponding cells are equal to x or y, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 with the [SUM function](https://exceljet.net/functions/sum-function)
 and an [array constant](https://exceljet.net/glossary/array-constant)
. In the example shown, the formula in cell I5 is:

    =SUM(SUMIFS(data[Total],data[Color],{"red","blue"}))
    

Where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:F16. The result is $205, the sum of Total where the Color is "Red" OR "Blue". Note the SUMIFS function is _not_ case-sensitive.

Generic formula
---------------

    =SUM(SUMIFS(range1,range2,{"red","blue"}))

Explanation 
------------

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data**. This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. However, when using SUMIFS with multiple criteria, all conditions must be TRUE. This means that multiple conditions are joined with AND logic and there is no direct way to apply conditions with OR logic. One solution is to use an array constant with SUMIFS, then sum the results with the SUM function. Another option is to use SUMIFS twice.

### SUMIFS + SUMIFS

Before looking at the more advanced option shown in the example, it's important to note that we can solve this problem with two calls to SUMIFS like this:

    =SUMIFS(data[Total],data[Color],"red")+
    SUMIFS(data[Total],data[Color],"blue")

The first SUMIFS sums Total where the color is "Red", and the second SUMIFS sums Total where the color is "Blue". By adding the two functions together in one formula, we effectively get a sum of Total where the color is either "Red" or "Blue".

### SUMIFS + a**rray constant**

A more elegant solution is to give the SUMIFS function more than one value for the criteria, in an [array constant](https://exceljet.net/glossary/array-constant)
. To do this, construct a normal SUMIFS formula, but supply criteria in [array](https://exceljet.net/glossary/array)
 syntax like this:

    {"red","blue"} // array constant

Placing the array constant inside SUMIFS as _criteria1_, we have:

    SUMIFS(data[Total],data[Color],{"red","blue"})

In this configuration, SUMIFS will return two sums: one for totals where the color is "Red" and one for totals where the color is "Blue". These results will be returned in an [array](https://exceljet.net/glossary/array)
 like this:

    {86,119} // result from SUMIFS

In the latest version of Excel you will see these results [spill](https://exceljet.net/glossary/spill)
 onto the worksheet into two cells. However, we don't want two results on the worksheet (we want a single result) so we wrap the SUMIFS function inside the SUM function like this:

    =SUM(SUMIFS(data[Total],data[Color],{"red","blue"}))

Now SUMIFS will return the array to SUM:

    =SUM({86,119}) // returns 205

and the SUM function will return the final result, 205.

### Criteria as reference

You can also supply criteria as a cell reference instead of an array constant. For example, with "Red" in cell A1 and "Blue" in cell A2, you can use a formula like this:

    =SUM(SUMIFS(data[Total],data[Color],A1:A2))

In the latest version of Excel, this formula will work as-is, with no special handling. In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, you will need to enter as an [array formula](https://exceljet.net/glossary/array-formula)
 with control + shift + enter.

### SUMPRODUCT alternative

You can also use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to sum cells with OR logic with a formula like this

    =SUMPRODUCT(--ISNUMBER(MATCH(data[Color],{"red","blue"},0))*data[Total])

This formula uses the [MATCH function](https://exceljet.net/functions/match-function)
 and the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 to create a [Boolean array](https://exceljet.net/videos/boolean-operations-in-array-formulas)
 that is then multiplied by **data\[Total\]** to get a final result. This is a flexible approach that works nicely in situations where SUMIFS can't be used. 

_Note: in the current version of Excel you can use the SUM function instead of SUMPRODUCT. See [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)
_

Related formulas
----------------

[![Excel formula: SUMIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS_with_multiple_criteria_and_OR_logic.png "Excel formula: SUMIFS with multiple criteria and OR logic")](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)

### [SUMIFS with multiple criteria and OR logic](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)

In this example, the goal is to sum the value of orders that have a status of "Complete" or "Pending". This is a slightly tricky problem in Excel because the SUMIFS function is designed for conditional sums based on multiple criteria, but all criteria must be TRUE in order for a value to be...

[![Excel formula: Sum if cells are equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_equal_to.png "Excel formula: Sum if cells are equal to")](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

### [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when cells in the range C5:C15 contain "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only a single condition. SUMIFS on the other...

[![Excel formula: Sum if begins with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_begins_with.png "Excel formula: Sum if begins with")](https://exceljet.net/formulas/sum-if-begins-with)

### [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)

In this example, the goal is to sum the Price in column C when the Product in column B begins with "sha". To solve this problem, you can use either the SUMIF function or the SUMIFS function with the asterisk (\*) wildcard, as explained below. Wildcards Certain Excel functions like SUMIF and SUMIFS...

[![Excel formula: Sum if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_not_blank.png "Excel formula: Sum if not blank")](https://exceljet.net/formulas/sum-if-not-blank)

### [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)

In this example, the goal is to sum the Amounts in C5:C16 when the Lead in D5:D16 is not blank (i.e., not empty). A good way to solve this problem is to use the SUMIFS function . However, you can also use the SUMPRODUCT function or the FILTER function , as explained below. Because SUMPRODUCT and...

[![Excel formula: Sum if cells are not equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_not_equal_to.png "Excel formula: Sum if cells are not equal to")](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

### [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when corresponding cells in the range C5:C15 are not equal to "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only one criteria...

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [SUMIFS with multiple criteria and OR logic](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)
    
*   [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)
    
*   [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    
*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    

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