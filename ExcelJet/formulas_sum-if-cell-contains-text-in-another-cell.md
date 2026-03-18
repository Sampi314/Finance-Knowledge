# Sum if cell contains text in another cell - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-cell-contains-text-in-another-cell

---

[Skip to main content](https://exceljet.net/formulas/sum-if-cell-contains-text-in-another-cell#main-content)

[](https://exceljet.net/formulas/sum-if-cell-contains-text-in-another-cell#)

*   [Previous](https://exceljet.net/formulas/sum-if-case-sensitive)
    
*   [Next](https://exceljet.net/formulas/sum-if-cells-are-equal-to)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if cell contains text in another cell
=========================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[FIND](https://exceljet.net/functions/find-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7623/download?token=UJmzHbLp)
 (15.75 KB)

![Excel formula: Sum if cell contains text in another cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_cells_contain_text_in_another_cell.png "Excel formula: Sum if cell contains text in another cell")

Summary
-------

To sum numbers if cells contain text in another cell, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 or the [SUMIF function](https://exceljet.net/functions/sumif-function)
 with a [wildcard](https://exceljet.net/glossary/wildcard)
. In the example shown the formula in cell F5 is:

    =SUMIFS(data[Amount],data[Location],"*, "&E5&" *")
    

Where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:C16. As the formula is copied down, it returns a sum for each state in column E. Note the formula is using a wildcard (\*) and extra space in the criteria. See below for details and for a case-sensitive option.

Generic formula
---------------

    =SUMIFS(sum_range,range,"*"&A1&"*")

Explanation 
------------

In this example, the goal is to sum Amounts in column C by state using the two-letter codes in column E. Note the states are abbreviated, "CA" is California, "FL" is Florida, "TX" is Texas, and "WA" is Washington. The challenge in this case is that the state abbreviations are _embedded_ in a text string. This means we need to construct criteria that performs a "contains" type match. To solve this problem, you can use either the SUMIF function or the SUMIFS function with a [wildcard](https://exceljet.net/glossary/wildcard)
. If you need a case-sensitive formula, you can use the SUMPRODUCT function with the FIND function. All three approaches are explained below.

_Note: this example pulls together a number of ideas, which makes it more advanced. If you find this example challenging, [this formula is a simpler introduction](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
 to the same idea, without using text from another cell for criteria._

### Data in an Excel Table

For convenience, all data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data** in the range B5:C16. This allows us to use a [structured reference](https://exceljet.net/glossary/structured-reference)
 like **data\[Amount\]** to refer to the Amount column without using an [absolute reference](https://exceljet.net/glossary/absolute-reference)
. It also means that the formula will continue to work correctly if new data is added to the table.

Video: What is an Excel Table?

### Wildcards

Excel functions like SUMIF and SUMIFS support the [wildcard](https://exceljet.net/glossary/wildcard)
 characters "?" (any one character) and "\*" (zero or more characters), which can be used in criteria. Wildcards allow you to create criteria such as "begins with", "ends with", "contains 3 characters" and so on. The table below shows some possible wildcard configurations. For the data in this problem, we want to use the "Cells that contain text in A1" pattern, which uses two asterisks (\*) concatenated to a cell reference like "\*"&A1&"\*".

| Target | Criteria |
| --- | --- |
| Cells with 3 characters | "???" |
| Cells equal to "xyz", "xaz", "xbz", etc | "x?z" |
| Cells that begin with "xyz" | "xyz\*" |
| Cells that end with "xyz" | "\*xyz" |
| Cells that contain "xyz" | "\*xyz\*" |
| Cells that contain text in A1 | "\*"&A1&"\*" |

Note that wildcards are enclosed in double quotes ("") when they appear in criteria. Also notice that cell references are _not_ enclosed in double quotes. Instead, they are [_concatenated_](https://exceljet.net/glossary/concatenation)
 to wildcards.

### SUMIFS solution

One way to solve this problem is with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. SUMIFS can handle _multiple_ criteria, and the generic syntax for a single condition looks like this:

    =SUMIFS(sum_range,range1,criteria1)

Notice that the sum range always comes _first_ in the SUMIFS function. Following this pattern, the formula in cell F5 of the worksheet shown looks like this:

    =SUMIFS(data[Amount],data[Location],"*, "&E5&" *")
    

The sum range is **data\[Amount\]** and the criteria range is **data\[Location\]**. The criteria itself is the tricky part of this formula:

    "*, "&E5&" *" // criteria includes comma and space

Notice the text and wildcard (\*) are both enclosed in double quotes ("") and we are _including_ a comma and space (", ") on the left and a space (" ") on the right to prevent false matches. These extra characters make this criteria more _specific_, so that we don't accidentally match "CA" in another word, like "cat" or "FL" in "flood". This is important partly because the SUMIFS and SUMIF function are _not_ case-sensitive. Also notice that the cell reference E5 is _not_ enclosed in double quotes. Instead, it is _concatenated_ to wildcards on either side. We can't use criteria like "\*, E5 \*" because that will match only the literal text ", E5 ".

When Excel evaluates the SUMIF formula, it will retrieve the value from E5 ("CA"), perform concatenation, and assemble the criteria into a single text string like this:

    =SUMIFS(data[Amount],data[Location],"*, CA *")

When the formula is entered in cell F5, it returns $600, the sum for amounts in California ("CA"). As the formula is copied down, it returns a sum of amounts for each state in column E. 

### SUMIF solution

This problem can also be solved with the [SUMIF function](https://exceljet.net/functions/sumif-function)
, where the equivalent formula is:

    =SUMIF(data[Location],"*, "&E5&" *",data[Amount])

Note that _sum\_range_ comes last in the SUMIF function. However, the criteria is identical to what we used in SUMIFS above. The result returned by SUMIF is the same, $600 in cell F5 for the sum of amounts in California.

### Case-sensitive solution

As mentioned above, the SUMIF and SUMIFS functions are _not_ case-sensitive. If you need a case-sensitive solution, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and the [FIND function](https://exceljet.net/functions/find-function)
 like this:

    =SUMPRODUCT(--ISNUMBER(FIND(E5,data[Location]))*data[Amount])

Inside SUMPRODUCT, the left side of the expression tests for state with ISNUMBER and FIND:

    --ISNUMBER(FIND(E5,data[Location]))

The FIND function is case-sensitive by default and returns the position of _find\_text_ as a number when found, and a #VALUE! error when not found. We do not need to use a wildcard character like (\*) because FIND automatically performs a "contains" type search for a substring. Because there are 12 values in **data\[Location\]**, FIND returns an array of 12 results like this:

    {#VALUE!;14;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;12;10;#VALUE!;#VALUE!}

Notice that FIND returns numbers for the second, ninth, and tenth rows in the data. These are the rows where the state is "CA". The [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 converts the results from FIND into TRUE and FALSE values, and the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) converts the TRUE and FALSE values to 1s and 0s. Inside the SUMPRODUCT we now have:

    =SUMPRODUCT({0;1;0;0;0;0;0;0;1;1;0;0}*data[Amount])

_Note: technically, the double negative (--) is unnecessary in this formula, because multiplying the TRUE and FALSE values by the numeric values in **data\[Amount\]** will automatically convert TRUE and FALSE values to 1s and 0s. However, the double negative does no harm and it makes the formula a bit easier to understand, because it signals a [Boolean operation](https://exceljet.net/videos/boolean-operations-in-array-formulas)
._

Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

When the two arrays are multiplied together, the zeros in the first array act like a filter to cancel out amounts for all states except "CA":

    =SUMPRODUCT({0;225;0;0;0;0;0;0;200;175;0;0})

With just one array to process, SUMPRODUCT sums the values in the array and returns 600 as a final result. As the formula is copied down, we get a case-sensitive sum of amounts for each state abbreviation in column E.

One thing you might notice in this formula is that we are not concatenating the comma and space to the cell value E5, because it is not likely that the uppercase "CA" will match the wrong text. However, we could add this step to make the search more specific:

    =SUMPRODUCT(ISNUMBER(FIND(", "&E5&" ",data[Location]))*data[Amount])

As mentioned above, there is no need to use a wildcard in this case because FIND automatically looks for _find\_text_ as a substring that might appear anywhere in the text. For a more detailed explanation of FIND + ISNUMBER [see this article](https://exceljet.net/formulas/cell-contains-specific-text)
.

_Note: In [Excel 365](https://exceljet.net/glossary/excel-365)
, you can replace SUMPRODUCT with the [SUM function](https://exceljet.net/functions/sum-function)
. To read more about this, see [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)
_

Related formulas
----------------

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

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

[![Excel formula: Sum if multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_multiple_columns.png "Excel formula: Sum if multiple columns")](https://exceljet.net/formulas/sum-if-multiple-columns)

### [Sum if multiple columns](https://exceljet.net/formulas/sum-if-multiple-columns)

In this example, the goal is to calculate a sum for any given group ("A", "B", or "C") across all three months of data in the range C5:E16. In other words, we want to perform a "sum if" with a data range that contains three columns. For convenience only, data (C5:E16) and group (B5:B16) are named...

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

*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    
*   [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)
    
*   [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    
*   [Sum if multiple columns](https://exceljet.net/formulas/sum-if-multiple-columns)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

### Videos

*   [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)
    
*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    

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