# Find missing values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/find-missing-values

---

[Skip to main content](https://exceljet.net/formulas/find-missing-values#main-content)

[](https://exceljet.net/formulas/find-missing-values#)

*   [Previous](https://exceljet.net/formulas/find-longest-string-with-criteria)
    
*   [Next](https://exceljet.net/formulas/get-address-of-lookup-result)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Find missing values
===================

by Dave Bruns · Updated 1 May 2023

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[IF](https://exceljet.net/functions/if-function)

[MATCH](https://exceljet.net/functions/match-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: Find missing values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/find_missing_values.png "Excel formula: Find missing values")

Summary
-------

To find values in one list that are missing in another list, you can use a formula based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
 combined with the [IF function](https://exceljet.net/videos/the-if-function)
. In the example shown, the formula in G5 is:

    =IF(COUNTIF(list,D5),"OK","Missing")

where **list** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16. As the formula is copied down, it returns "OK" when an invoice is found in B5:B16 and "Missing" when an invoice cannot be found.

_Note: If you want to list missing values, [see this page](https://exceljet.net/formulas/list-missing-values)
._

Generic formula
---------------

    =IF(COUNTIF(list,value),"OK","Missing")
    

Explanation 
------------

The goal is to identify invoice numbers in range D5:D11 that are missing in range B5:B16 (named **list**). Two good ways to solve this problem in Excel are the [COUNTIF function](https://exceljet.net/functions/countif-function)
 and the [MATCH function](https://exceljet.net/functions/match-function)
. Both approaches are explained below.

### COUNTIF function

[COUNTIF](https://exceljet.net/functions/countif-function)
 counts cells in a range that meet a given condition (criteria). If no cells meet the criteria, COUNTIF returns zero. The generic syntax for COUNTIF is:

    =COUNTIF(range,criteria)

To check for missing invoices, combine COUNTIF with the [IF function](https://exceljet.net/functions/if-function)
. The formula in G5 is:

    =IF(COUNTIF(list,D5),"OK","Missing")

Notice the COUNTIF formula appears inside the IF function as the _logical\_test_ argument. Normally, the IF function requires a logical test to return TRUE or FALSE. However, Excel will automatically evaluate any non-zero number as TRUE and the number zero (0) as FALSE. As the formula is copied down column E, COUNTIF returns the count of each invoice in column D in the named range **list** (B5:B16). When the count is non-zero, The IF function returns "OK". If the invoice is not found in **list**, COUNTIF returns zero (0), which evaluates as FALSE, and IF returns "Missing".

### Alternative with MATCH

Another approach is to use the [MATCH function](https://exceljet.net/functions/match-function)
. MATCH locates the position of a value in a row, column, or table. The generic syntax for MATCH in exact match mode is:

    =MATCH(value,array,0)

The last value, match\_type, is set to zero for an exact match. When MATCH finds the lookup value, it returns the _position_ of that value in the array as a _number_. If MATCH doesn't find the lookup value, it returns an #N/A error. Use this behavior to build a formula that returns "Missing" or "OK" by testing the result of MATCH with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
:

    =IF(ISNUMBER(MATCH(D5,list,0)),"OK","Missing")

As the formula is copied down column E, MATCH returns the position of each invoice in column D in the named range **list** (B5:B16). When an invoice number is not found, MATCH returns #N/A. The ISNUMBER function returns TRUE or FALSE, depending on the result from MATCH. The result from ISNUMBER is returned to the IF function as the _logical\_test_, and IF then returns "OK" when an invoice is found and "Missing" when an invoice is not found. The screen below shows this formula in use:

![Using the MATCH function to find missing values in a column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/find_missing_values_MATCH_function.png "Using the MATCH function to find missing values in a column")

### Summary

The COUNTIF version of this formula and the MATCH version work equally well, but in different ways. Choose based on personal preference. However, one advantage that the MATCH function has over the COUNTIF function is that it will work with in-memory arrays as well as ranges. The COUNTIF function requires a range. This might be important when using [dynamic array formulas](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
. To read more about this limitation, [see this article](https://exceljet.net/articles/excels-racon-functions)
.

Related formulas
----------------

[![Excel formula: Count missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_missing_values.png "Excel formula: Count missing values")](https://exceljet.net/formulas/count-missing-values)

### [Count missing values](https://exceljet.net/formulas/count-missing-values)

In this example, the goal is to count the number of names in the range B5:B16 (Invited) that are missing from the range D5:D12 (Attended). This problem can be solved with the COUNTIF function or the MATCH function, as explained below. Both approaches work well. The advantage of the MATCH approach...

[![Excel formula: Highlight missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20that%20don%27t%20exist.png "Excel formula: Highlight missing values")](https://exceljet.net/formulas/highlight-missing-values)

### [Highlight missing values](https://exceljet.net/formulas/highlight-missing-values)

This formula is evaluated for each of the 10 cells in A1:D10. A1 will change to the address of the cell being evaluated, while C1:C10 is entered as an absolute address, so it won't change at all. The key to this formula is the =0 at the end, which "flips" the logic of the formula. For each value in...

[![Excel formula: List missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_missing_values.png "Excel formula: List missing values")](https://exceljet.net/formulas/list-missing-values)

### [List missing values](https://exceljet.net/formulas/list-missing-values)

In this example, the goal is to generate a list of people who were invited but did not attend an unspecified event. More specifically, we need to compare the names in B5:B16 against the names in D5:D12 and return the missing names. For convenience, list1 (B5:B16) and list2 (D5:D12) are named ranges...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countif-function)

### [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)

In this video we'll look at how to use the COUNTIF function to count cells that meet a single criteria. Let's take a look. The COUNTIF function counts cells that satisfy a single condition that you supply. It takes two arguments: range and criteria. For example, if I want to count the cells in this...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20MATCH%20Function%20for%20exact%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

### [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

The MATCH function finds the relative position of an item in a list. MATCH can find exact matches or approximate matches. In this video, we'll look at how to use MATCH to find an exact match. The MATCH function takes three arguments: the lookup\_value, which is the value you're looking up, the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Introduction%20to%20Booleans-Play.png)](https://exceljet.net/videos/introduction-to-booleans)

### [Introduction to Booleans](https://exceljet.net/videos/introduction-to-booleans)

In this video, we’ll introduce the idea of boolean values in Excel. A boolean is a data type with only two possible values. In Excel, these are the logical values TRUE and FALSE. You’ll notice that Excel treats TRUE and FALSE in a special way. If I type the word “true” in lowercase, Excel...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count missing values](https://exceljet.net/formulas/count-missing-values)
    
*   [Highlight missing values](https://exceljet.net/formulas/highlight-missing-values)
    
*   [List missing values](https://exceljet.net/formulas/list-missing-values)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

### Videos

*   [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    
*   [Introduction to Booleans](https://exceljet.net/videos/introduction-to-booleans)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    
*   [Danger: beware VLOOKUP defaults](https://exceljet.net/articles/danger-beware-vlookup-defaults)
    

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