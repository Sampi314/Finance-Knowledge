# Sum if cells contain either x or y - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y

---

[Skip to main content](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y#main-content)

[](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y#)

*   [Previous](https://exceljet.net/formulas/sum-if-cells-contain-both-x-and-y)
    
*   [Next](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if cells contain either x or y
==================================

by Dave Bruns · Updated 28 Apr 2025

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[FIND](https://exceljet.net/functions/find-function)

[SEARCH](https://exceljet.net/functions/search-function)

![Excel formula: Sum if cells contain either x or y](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_cells_contain_either_x_or_y.png "Excel formula: Sum if cells contain either x or y")

Summary
-------

To sum cells that contain either x or y as substrings, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 together with [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [SEARCH](https://exceljet.net/functions/search-function)
. In the example shown, the formula in cell F5 is:

    =SUMPRODUCT(--((ISNUMBER(SEARCH("red",B5:B16)) + ISNUMBER(SEARCH("blue",B5:B16)))>0),C5:C16)

The result is 23, the sum of numbers in C5:C16 when text in B5:B16 contains the substring "red" or the substring "blue".

Generic formula
---------------

    =SUMPRODUCT(--((ISNUMBER(SEARCH("red",range1)) + ISNUMBER(SEARCH("blue",range1)))>0),range2)

Explanation 
------------

In this example, the goal is to sum numbers in the range C5:C16 when text in the range B5:B16 contains the substring "red" OR the substring "blue". In other words, if the text in B5:B16 contains either of these two text values in any location, the corresponding number in C5:C16 should be included in the sum. We can't use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 with two criteria because SUMIFS is based on AND logic, and _both criteria_ would need to be TRUE. And if we try to use two SUMIFS formulas (i.e., SUMIFS + SUMIFS), we will double count some numbers because some cells in B5:B16 contain both "red" and "blue". One solution is to use the SUMPRODUCT function together with the ISNUMBER and SEARCH functions.

### SEARCH + ISNUMBER for substrings

The core of this formula is based on the SEARCH function together with the ISNUMBER function. The [SEARCH function](https://exceljet.net/functions/search-function)
 is designed to find a specific substring in a text string. If SEARCH finds the substring, it returns the _position_ of the substring in the text as a number. If the substring is not found, SEARCH returns a #VALUE error. For example:

    =SEARCH("p","apple") // returns 2
    =SEARCH("z","apple") // returns #VALUE!

To force a TRUE or FALSE result, we can use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
. ISNUMBER returns TRUE for numeric values and FALSE for anything else. So, if SEARCH finds the substring, it returns the position as a number, and ISNUMBER returns TRUE:

    =ISNUMBER(SEARCH("p","apple")) // returns TRUE
    =ISNUMBER(SEARCH("z","apple")) // returns FALSE

If SEARCH _doesn't_ find the substring, it returns an error, which causes the ISNUMBER to return FALSE. For a more detailed explanation of this approach, [see this page](https://exceljet.net/formulas/cell-contains-specific-text)
.

### SUMPRODUCT function

In the example shown, the formula in cell F5 is:

    =SUMPRODUCT(--((ISNUMBER(SEARCH("red",B5:B16)) + ISNUMBER(SEARCH("blue",B5:B16)))>0),C5:C16)

Working from the inside out, the _array1_ inside SUMPRODUCT is composed of this snippet:

    --((ISNUMBER(SEARCH("red",B5:B16)) + ISNUMBER(SEARCH("blue",B5:B16)))>0)

On the left, SEARCH is configured to look for "red". Because there are 12 values in the range B5:B16, ISNUMBER returns an [array](https://exceljet.net/glossary/array)
 with 12 results:

    {TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE}

Each TRUE in the array represents a cell in B5:B16 that contains "red". On the right, SEARCH is configured to look for "blue". This results in the array below:

    {TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;TRUE;FALSE;FALSE;FALSE;TRUE;TRUE}

Each TRUE in this array represents a cell in B5:B16 that contains "blue". Next, we add these arrays together. We use addition (+) because [addition corresponds to OR logic in Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
.

Video: [Boolean Algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

The math operation automatically coerces the TRUE and FALSE values to 1s and 0s, so we can now rewrite the original formula like this:

    =SUMPRODUCT(--(({1;0;1;0;0;0;0;1;1;0;1;0} +{1;0;1;0;0;1;1;0;0;0;1;1})>0),C5:C16)

After adding the two Boolean arrays together, we have:

    =SUMPRODUCT(--({2;0;2;0;0;1;1;1;1;0;2;1}>0),C5:C16)

The 2s in this array represent cells that contain both "red" and "blue". To avoid double counting, we force the numbers back to TRUE and FALSE by comparing to zero, then use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to convert the TRUE and FALSE values to 1s and 0s. The final value of _array1_ in SUMPRODUCT is now:

    =SUMPRODUCT({1;0;1;0;0;1;1;1;1;0;1;1},C5:C16)

Next, SUMPRODUCT multiplies corresponding elements of the two arrays together and sums the result:

    =SUMPRODUCT({1;0;1;0;0;1;1;1;1;0;1;1},C5:C16)
    =SUMPRODUCT({1;0;1;0;0;1;1;1;1;0;1;1},{2;5;3;3;4;5;1;4;2;5;1;5})
    =SUMPRODUCT({2;0;3;0;0;5;1;4;2;0;1;5})
    =23

The final result is 23, the sum of numbers in C5:C16 that correspond to text in B5:B16 that contains either "red" or "blue".

_Note: In_ [_Excel 365_](https://exceljet.net/glossary/excel-365)
_, you can replace SUMPRODUCT with the_ [_SUM function_](https://exceljet.net/functions/sum-function)
_. To read more about this, see_ [_Why SUMPRODUCT?_](https://exceljet.net/articles/why-sumproduct)

### Case-sensitive option

The SEARCH function ignores case. If you need a sensitive option, you can replace the SEARCH function in this formula with the [FIND function](https://exceljet.net/functions/find-function)
.

Related formulas
----------------

[![Excel formula: Sum if cells contain both x and y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_both_x_and_y.png "Excel formula: Sum if cells contain both x and y")](https://exceljet.net/formulas/sum-if-cells-contain-both-x-and-y)

### [Sum if cells contain both x and y](https://exceljet.net/formulas/sum-if-cells-contain-both-x-and-y)

In this example, the goal is to sum the numbers in column C when the text in column B contains specific pairs of colors. For example, the formula should sum a number when the text contains both "red" and "blue". Order is not important; the two colors can appear anywhere in the cell. However, both...

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

[![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")](https://exceljet.net/formulas/sum-if-x-or-y)

### [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an Excel Table named data . This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the SUMIFS function . However, when...

[![Excel formula: Sum if one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_one_of_many_things.png "Excel formula: Sum if one of many things")](https://exceljet.net/formulas/sum-if-one-of-many-things)

### [Sum if one of many things](https://exceljet.net/formulas/sum-if-one-of-many-things)

In this example, the goal is to sum the numbers in column E when the item in column B appears in the range G5:G7. The named range things is not required. It is used only for convenience and can be expanded as needed to include additional criteria. The article below explains several ways to solve...

[![Excel formula: Count cells that contain either x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20either%20x%20or%20y.png "Excel formula: Count cells that contain either x or y")](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

### [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

In this example, the goal is to count cells in the range B5:B15 that contain either "x" or "y", where x and y are both text strings . When you count cells with "OR logic", you need to be careful not to double count. For example, if you are counting cells that contain "blue" or "green", you can't...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

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

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if cells contain both x and y](https://exceljet.net/formulas/sum-if-cells-contain-both-x-and-y)
    
*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    
*   [Sum if one of many things](https://exceljet.net/formulas/sum-if-one-of-many-things)
    
*   [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    

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