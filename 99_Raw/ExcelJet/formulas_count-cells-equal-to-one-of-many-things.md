# Count cells equal to one of many things - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things

---

[Skip to main content](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things#main-content)

[](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things#)

*   [Previous](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
    
*   [Next](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)
    

[Count](https://exceljet.net/formulas#Count)

Count cells equal to one of many things
=======================================

by Dave Bruns · Updated 14 May 2022

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Count cells equal to one of many things](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20equal%20to%20one%20of%20many%20things.png "Excel formula: Count cells equal to one of many things")

Summary
-------

To count the number of cells equal to one of many values, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 inside of the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the generic form of the formula above, **range** is the data, and **things** represents the values to count. In the example shown, cell G5 contains this formula:

    =SUMPRODUCT(COUNTIF(B5:B10,things))
    

where **things** is the [named range](https://exceljet.net/glossary/named-range)
 E5:E7.

_Note: COUNTIF is not case-sensitive._

Generic formula
---------------

    =SUMPRODUCT(COUNTIF(range,things))

Explanation 
------------

In this example, the goal is to count the values in column B listed in the range E5:E7. One way to do this is to give the COUNTIF function all three values in the [named range](https://exceljet.net/glossary/named-range)
 **things** (E5:E7) as criteria, then use the SUMPRODUCT function to get a total. The formula in G4 is:

    =SUMPRODUCT(COUNTIF(B5:B15,things))
    

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 counts the number of cells in a range that meet criteria. When you give COUNTIF a range of cells as the criteria, it returns an [array](https://exceljet.net/glossary/array)
 of numbers as the result, where each number represents the count of one thing in the criteria range. In this case, the [named range](https://exceljet.net/glossary/named-range)
 **things** (D5:D7) contains 3 values, so COUNTIF returns 3 results in an array as shown below:

    =COUNTIF(B5:B15,things)
    =COUNTIF(B5:B15,{"apples";"pears";"kiwis"})
    ={2;3;1} // result from COUNTIF
    

Since "apple" appears twice, "pears" appears three times, and "kiwis" appears once, the array contains the numbers 2, 3, and 1. This array is returned directly to the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
:

    =SUMPRODUCT({2;3;1})
    

With a single array to process, SUMPRODUCT simply sums the array and returns 6.

### With an array constant

With a limited number of values, you can use an [array constant](https://exceljet.net/glossary/array-constant)
 in your formula like this:

    =SUMPRODUCT(COUNTIF(B5:B15,{"apples","pears","kiwis"}))
    

### ISNUMBER and MATCH

The above formula works fine, but has some limitations due to the [nature of COUNTIF](https://exceljet.net/articles/excels-racon-functions)
. As an alternative, you can use the formula below, which uses the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 with the [MATCH function](https://exceljet.net/functions/match-function)
 to achieve the same result:

    =SUMPRODUCT(--ISNUMBER(MATCH(B5:B15,things,0)))
    
    

This is a more flexible formula in cases where logical conditions become [more complex](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
. It's also useful when you need to extract a value from a range in the data to use in a condition.

Related formulas
----------------

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Count cells equal to this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20this%20or%20that.png "Excel formula: Count cells equal to this or that")](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)

### [Count cells equal to this or that](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)

In this example, the goal is to count cells in the range D5:D15 that contain "red" or "blue". For convenience, the D5:D15 is named color . Counting cells equal to this OR that is more complicated than it first appears because there is no built-in function for counting with OR logic. The COUNTIFS...

[![Excel formula: Count total matches in two ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20total%20matches%20in%20two%20ranges.png "Excel formula: Count total matches in two ranges")](https://exceljet.net/formulas/count-total-matches-in-two-ranges)

### [Count total matches in two ranges](https://exceljet.net/formulas/count-total-matches-in-two-ranges)

In this example, the goal is to count the number of exact matches in two ranges, ignoring the sort order or location of the values in each range. This problem can be solved with the COUNTIF function or with the MATCH function. Each approach is explained below. Note: Both formulas below use the...

[![Excel formula: Sum if one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_one_of_many_things.png "Excel formula: Sum if one of many things")](https://exceljet.net/formulas/sum-if-one-of-many-things)

### [Sum if one of many things](https://exceljet.net/formulas/sum-if-one-of-many-things)

In this example, the goal is to sum the numbers in column E when the item in column B appears in the range G5:G7. The named range things is not required. It is used only for convenience and can be expanded as needed to include additional criteria. The article below explains several ways to solve...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

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

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)
    
*   [Count cells equal to this or that](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)
    
*   [Count total matches in two ranges](https://exceljet.net/formulas/count-total-matches-in-two-ranges)
    
*   [Sum if one of many things](https://exceljet.net/formulas/sum-if-one-of-many-things)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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