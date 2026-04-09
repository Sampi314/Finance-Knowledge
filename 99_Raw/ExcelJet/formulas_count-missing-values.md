# Count missing values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-missing-values

---

[Skip to main content](https://exceljet.net/formulas/count-missing-values#main-content)

[](https://exceljet.net/formulas/count-missing-values#)

*   [Previous](https://exceljet.net/formulas/count-matching-values-in-matching-columns)
    
*   [Next](https://exceljet.net/formulas/count-non-blank-cells-by-category)
    

[Count](https://exceljet.net/formulas#Count)

Count missing values
====================

by Dave Bruns · Updated 30 Apr 2023

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUM](https://exceljet.net/functions/sum-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[MATCH](https://exceljet.net/functions/match-function)

[ISNA](https://exceljet.net/functions/isna-function)

![Excel formula: Count missing values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count_missing_values.png "Excel formula: Count missing values")

Summary
-------

To count the values in one list that are missing from another list, you can use a formula based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the example shown, the formula in F5 is:

    =SUM(--(COUNTIF(D5:D12,B5:B16)=0))
    

This formula returns 4 because there are 4 names in B5:B16 that are missing from D5:D12.

_Note: In the current version of Excel, the SUM function "just works" with no special handling. In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, this is an [array formula](https://exceljet.net/glossary/array-formula)
 that must be entered with control + shift + enter. To avoid this requirement, you can [replace the SUM function with the SUMPRODUCT function](https://exceljet.net/articles/why-sumproduct)
._

Generic formula
---------------

    =SUM(--(COUNTIF(list2,list1)=0))
    

Explanation 
------------

In this example, the goal is to count the number of names in the range B5:B16 (Invited) that are missing from the range D5:D12 (Attended). This problem can be solved with the COUNTIF function or the MATCH function, as explained below. Both approaches work well. The advantage of the MATCH approach is that it will work with [arrays](https://exceljet.net/glossary/array)
 or [ranges](https://exceljet.net/glossary/range)
. The COUNTIF function is limited to ranges only, like [other functions in this group](https://exceljet.net/articles/excels-racon-functions)
.

### COUNTIF solution

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 counts cells that meet a single condition, which is referred to as "criteria". The generic syntax for COUNTIF looks like this:

    =COUNTIF(range,criteria)

For example, to count the cells in A1:A10 that are equal to "apple", you could use COUNTIF like this:

    =COUNTIF(A1:A10,"apple")

In this example, we are doing something interesting. We are giving COUNTIF more than one value to count, supplied in the range B5:B16, and we are asking COUNTIF to count these values in the range D5:D12:

    =COUNTIF(D5:D12,B5:B16)

Literally, this formula means "count the values in B5:B16 that appear in D5:D12". Because we are giving COUNTIF a range that contains 12 values, COUNTIF returns 12 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {1;1;0;1;0;1;0;1;1;0;1;1}

The 1s in this array signify names in B5:B16 that appear in D5:D12. The 0s indicate names in B5:B16 that don't appear in D5:D12. If the goal was to count _matching values_, we could sum the result from COUNTIF with the SUM function like this:

    =SUM(COUNTIF(D5:D12,B5:B16)) // returns 8

The result would be 8 since there are 8 names in B5:B16 that appear in D5:D12. However, in this problem, the goal is to count _missing values_, so we need to "reverse" the result from COUNTIF before we sum. In other words, we need to convert the 1s to 0s and the 0s to 1s. We can do that by first comparing the result from COUNTIF to zero:

    COUNTIF(D5:D12,B5:B16)=0

This will result in an array with 12 TRUE and FALSE values like this:

    {FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE}

Notice that in this array, the FALSE values correspond to 1s in the previous array, and the TRUE values correspond to 0s. If we try to add these values up with the SUM function, the result will be zero, because SUM is programmed to ignore the logical values TRUE and FALSE. Before we sum, we need to convert the TRUE and FALSE values to 1s and 0s again. We do that with a [double negative](https://exceljet.net/glossary/double-unary)
 (--) operation:

    --(COUNTIF(D5:D12,B5:B16)=0) // returns {0;0;1;0;1;0;1;0;0;1;0;0}

The result is a numeric array:

    {0;0;1;0;1;0;1;0;0;1;0;0}

In this array, 0s represent names in B5:B16 that appear in D5:D12, and 1s represent missing names. This array is returned directly to the SUM function, and SUM returns 4 as a final result:

    =SUM({0;0;1;0;1;0;1;0;0;1;0;0}) // returns 4

_Note: In the current version of Excel, the SUM function works without special handling. In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter. To avoid this requirement, you can [replace SUM with SUMPRODUCT](https://exceljet.net/articles/why-sumproduct)
, and control + shift + enter is not required._

### MATCH solution

Another way to solve this problem in a more literal way is to use the MATCH function to match names. The [MATCH function](https://exceljet.net/functions/match-function)
 returns the position of a value in a range. For example, if the range A1:A3 contains "orange", "apple", and "pear", then the MATCH function will return 2 if we look for "apple", because "apple" appears in the 2nd cell:

    =MATCH("apple",A1:A3,0) // returns 2

If we look for a value that _does not_ exist in the range, MATCH will return an #N/A error:

    =MATCH("banana",A1:A3,0) // returns #N/A

We can use the behavior above to solve the problem in this example with a formula like this:

    =SUM(--ISNA(MATCH(B5:B16,D5:D12,0)))

Working from the inside out, MATCH is configured to match the values in B5:B16 against the values in D5:D12:

    MATCH(B5:B16,D5:D12,0)

Note that the value for _match\_type_ is zero (0) to specify an exact match. Like the COUNTIF formula above, we are asking MATCH to look for the values in B5:B16 (Invited) in the values in D5:D12 (attended). Because we are looking for 12 values, MATCH will return an array with 12 results like this:

    {5;6;#N/A;1;#N/A;3;#N/A;7;8;#N/A;2;4}

In this array, numbers represent the position of a name that was found, and #N/A errors represent names that were not found. This array is returned directly to the [ISNA function](https://exceljet.net/functions/isna-function)
:

    ISNA({5;6;#N/A;1;#N/A;3;#N/A;7;8;#N/A;2;4})

ISNA returns TRUE for #N/A errors and FALSE for anything else, so the result from ISNA looks like this:

    {FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE}

As with the COUNTIF formula, we want to count these results, but we first need to convert the TRUE and FALSE values to 1s and 0s. We do this with a double negative (--) operation:

    =SUM(--{FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE})
    =SUM({0;0;1;0;1;0;1;0;0;1;0;0})
    =4

The final result is 4 since there are 4 names in B5:B16 that do not appear in D5:D12.

_Note: One advantage of the MATCH function is that it will work with data in arrays or ranges, while the COUNTIF function is [limited to ranges only](https://exceljet.net/articles/excels-racon-functions)
._

Related formulas
----------------

[![Excel formula: Find missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_missing_values.png "Excel formula: Find missing values")](https://exceljet.net/formulas/find-missing-values)

### [Find missing values](https://exceljet.net/formulas/find-missing-values)

The goal is to identify invoice numbers in range D5:D11 that are missing in range B5:B16 (named list ). Two good ways to solve this problem in Excel are the COUNTIF function and the MATCH function . Both approaches are explained below. COUNTIF function COUNTIF counts cells in a range that meet a...

[![Excel formula: List missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_missing_values.png "Excel formula: List missing values")](https://exceljet.net/formulas/list-missing-values)

### [List missing values](https://exceljet.net/formulas/list-missing-values)

In this example, the goal is to generate a list of people who were invited but did not attend an unspecified event. More specifically, we need to compare the names in B5:B16 against the names in D5:D12 and return the missing names. For convenience, list1 (B5:B16) and list2 (D5:D12) are named ranges...

[![Excel formula: Highlight missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20that%20don%27t%20exist.png "Excel formula: Highlight missing values")](https://exceljet.net/formulas/highlight-missing-values)

### [Highlight missing values](https://exceljet.net/formulas/highlight-missing-values)

This formula is evaluated for each of the 10 cells in A1:D10. A1 will change to the address of the cell being evaluated, while C1:C10 is entered as an absolute address, so it won't change at all. The key to this formula is the =0 at the end, which "flips" the logic of the formula. For each value in...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

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

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ISNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isna%20function.png "Excel ISNA function")](https://exceljet.net/functions/isna-function)

### [ISNA Function](https://exceljet.net/functions/isna-function)

The Excel ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countif-function)

### [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)

In this video we'll look at how to use the COUNTIF function to count cells that meet a single criteria. Let's take a look. The COUNTIF function counts cells that satisfy a single condition that you supply. It takes two arguments: range and criteria. For example, if I want to count the cells in this...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20MATCH%20Function%20for%20exact%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

### [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

The MATCH function finds the relative position of an item in a list. MATCH can find exact matches or approximate matches. In this video, we'll look at how to use MATCH to find an exact match. The MATCH function takes three arguments: the lookup\_value, which is the value you're looking up, the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Find missing values](https://exceljet.net/formulas/find-missing-values)
    
*   [List missing values](https://exceljet.net/formulas/list-missing-values)
    
*   [Highlight missing values](https://exceljet.net/formulas/highlight-missing-values)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    

### Videos

*   [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    

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