# Sum if cells contain specific text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-cells-contain-specific-text

---

[Skip to main content](https://exceljet.net/formulas/sum-if-cells-contain-specific-text#main-content)

[](https://exceljet.net/formulas/sum-if-cells-contain-specific-text#)

*   [Previous](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y)
    
*   [Next](https://exceljet.net/formulas/sum-if-date-is-between)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if cells contain specific text
==================================

by Dave Bruns · Updated 16 Dec 2022

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[FIND](https://exceljet.net/functions/find-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7624/download?token=DwA_vBih)
 (14.34 KB)

![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")

Summary
-------

To sum if cells contain specific text, you can use the [SUMIFS](https://exceljet.net/functions/sumifs-function)
 or [SUMIF](https://exceljet.net/functions/sumif-function)
 function with a [wildcard](https://exceljet.net/glossary/wildcard)
. In the example shown, the formula in cell F5 is:

    =SUMIFS(C5:C16,B5:B16,"*hoodie*")

This formula sums the quantity in column C when the text in column B contains "hoodie". Note that SUMIFS is _not_ case-sensitive. However, see below for a case-sensitive option.

Generic formula
---------------

    =SUMIFS(sum_range,range,"*text*")

Explanation 
------------

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are _embedded_ in a text string that also contains size and color. This means we need to apply criteria that looks for a _substring_ in the item text. To solve this problem, you can use either the SUMIFS function or the SUMIF function with a [wildcard](https://exceljet.net/glossary/wildcard)
. If you need a case-sensitive formula, you can use the SUMPRODUCT function with the FIND function. All three approaches are explained below.

_Note: this example embeds wildcards together with the search substring to keep things simple. However, you can also use wildcards with text in another cell, as explained in this [more advanced example](https://exceljet.net/formulas/sum-if-cell-contains-text-in-another-cell)
._

### Wildcards

Excel functions like SUMIF and SUMIFS support the [wildcard](https://exceljet.net/glossary/wildcard)
 characters "?" (any one character) and "\*" (zero or more characters), which can be used in criteria. Wildcards allow you to create criteria to target cells that "begin with", "end with", "contain 3 characters" and so on. The table below shows some examples. For this problem, we want to use the "Cells that contain text in xyz" pattern, which uses two asterisks (\*), one before and one after the search string like this "\*xyz\*".

| Target | Criteria |
| --- | --- |
| Cells with 3 characters | "???" |
| Cells equal to "xyz", "xaz", "xbz", etc | "x?z" |
| Cells that begin with "xyz" | "xyz\*" |
| Cells that end with "xyz" | "\*xyz" |
| Cells that contain "xyz" | "\*xyz\*" |
| Cells that contain text in A1 | "\*"&A1&"\*" |

Note that wildcards are enclosed in double quotes ("") when they appear in criteria.

### SUMIFS solution

One way to solve this problem is with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. SUMIFS can handle _multiple_ criteria, and the generic syntax for a single condition looks like this:

    =SUMIFS(sum_range,criteria_range1,criteria1)

Notice that the sum range always comes _first_ in the SUMIFS function. In our case, the _sum\_range_ is C5:C16, _criteria\_range1_ is B5:B16, and _criteria1_ is "\*hoodie\*". Putting it all together, the formula in cell F5 of the worksheet shown is:

    =SUMIFS(C5:C16,B5:B16,"*hoodie*")
    

Notice the text and both wildcards (\*) are enclosed in double quotes (""). The meaning of this criteria is to match the substring "hoodie" anywhere in a text string. When the formula is entered in cell F5, it returns 22, the total quantity of "hoodie" products in the data.

### SUMIF solution

This problem can also be solved with the [SUMIF function](https://exceljet.net/functions/sumif-function)
, where the equivalent formula is:

    =SUMIF(B5:B16,"*hoodie*",C5:C16)

Note that _sum\_range_ is the _last_ argument in the SUMIF function. However, the criteria itself is identical to what we used in SUMIFS above. The result returned by SUMIF is also the same: 22.

### Case-sensitive option

As mentioned above, the SUMIF and SUMIFS functions are _not_ case-sensitive. If you need a case-sensitive solution, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and the [FIND function](https://exceljet.net/functions/find-function)
 like this:

    =SUMPRODUCT(--ISNUMBER(FIND("Hoodie",B5:B16))*C5:C16)

Inside SUMPRODUCT, the left side of the expression tests for "Hoodie" with ISNUMBER and FIND:

    --ISNUMBER(FIND("Hoodie",B5:B16))

Note the "H" in hoodie is capitalized. The FIND function is _always_ case-sensitive, and returns the position of _find\_text_ as a number when found, and a #VALUE! error when not found. We do not need to use a wildcard like (\*) because FIND automatically searches for a substring. Because there are 12 values in B5:B16, FIND returns an [array](https://exceljet.net/glossary/array)
 of 12 results like this:

    {6;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;7;#VALUE!;6;6}

Notice that FIND returns numbers for rows 1, 9, 11, and 12 in the data. These are the rows where the substring "Hoodie" appears in the text. Next, the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 converts the results from FIND into TRUE and FALSE values, and the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) converts the TRUE and FALSE values to 1s and 0s. Inside SUMPRODUCT we now have:

    =SUMPRODUCT({1;0;0;0;0;0;0;0;1;0;1;1}*C5:C16)

_Note: technically, the double negative (--) is unnecessary in this formula, because multiplying the TRUE and FALSE values by the numeric values in C5:C16 will automatically convert TRUE and FALSE values to 1s and 0s. However, the double negative does no harm and it makes the formula a bit easier to understand, because it indicates a [Boolean operation](https://exceljet.net/videos/boolean-operations-in-array-formulas)
._

Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

When the two arrays are multiplied together, the zeros in the first array work like a filter to "cancel out" the quantity for items that are not "Hoodies". The result inside SUMPRODUCT is a single array like this:

    =SUMPRODUCT({9;0;0;0;0;0;0;0;6;0;4;3})

With only one array to process, SUMPRODUCT sums the array and returns 22 as a final result. For a more detailed explanation of FIND + ISNUMBER [see this article](https://exceljet.net/formulas/cell-contains-specific-text)
. To adapt this formula to use text in cell references, [see this example](https://exceljet.net/formulas/sum-if-cell-contains-text-in-another-cell)
.

_Note: In [Excel 365](https://exceljet.net/glossary/excel-365)
, you can replace SUMPRODUCT with the [SUM function](https://exceljet.net/functions/sum-function)
. To read more about this, see [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)
_

Related formulas
----------------

[![Excel formula: Sum if begins with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_begins_with.png "Excel formula: Sum if begins with")](https://exceljet.net/formulas/sum-if-begins-with)

### [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)

In this example, the goal is to sum the Price in column C when the Product in column B begins with "sha". To solve this problem, you can use either the SUMIF function or the SUMIFS function with the asterisk (\*) wildcard, as explained below. Wildcards Certain Excel functions like SUMIF and SUMIFS...

[![Excel formula: Sum if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_not_blank.png "Excel formula: Sum if not blank")](https://exceljet.net/formulas/sum-if-not-blank)

### [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)

In this example, the goal is to sum the Amounts in C5:C16 when the Lead in D5:D16 is not blank (i.e., not empty). A good way to solve this problem is to use the SUMIFS function . However, you can also use the SUMPRODUCT function or the FILTER function , as explained below. Because SUMPRODUCT and...

[![Excel formula: Sum if cells are equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_equal_to.png "Excel formula: Sum if cells are equal to")](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

### [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when cells in the range C5:C15 contain "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only a single condition. SUMIFS on the other...

[![Excel formula: Sum if cells are not equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_not_equal_to.png "Excel formula: Sum if cells are not equal to")](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

### [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when corresponding cells in the range C5:C15 are not equal to "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only one criteria...

[![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")](https://exceljet.net/formulas/sum-if-x-or-y)

### [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an Excel Table named data . This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the SUMIFS function . However, when...

[![Excel formula: SUMIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS_with_multiple_criteria_and_OR_logic.png "Excel formula: SUMIFS with multiple criteria and OR logic")](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)

### [SUMIFS with multiple criteria and OR logic](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)

In this example, the goal is to sum the value of orders that have a status of "Complete" or "Pending". This is a slightly tricky problem in Excel because the SUMIFS function is designed for conditional sums based on multiple criteria, but all criteria must be TRUE in order for a value to be...

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumif-function)

### [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)

In this video we'll look at how to use the SUMIF function to sum cells that meet a single criteria. Let's take a look. The SUMIF function sums cells that satisfy a single condition that you supply. It takes three arguments: range, criteria, and sum range. Note that sum range is optional. If you don...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)
    
*   [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    
*   [SUMIFS with multiple criteria and OR logic](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

### Videos

*   [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)
    

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