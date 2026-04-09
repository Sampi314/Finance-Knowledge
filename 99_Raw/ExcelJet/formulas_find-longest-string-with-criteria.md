# Find longest string with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/find-longest-string-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/find-longest-string-with-criteria#main-content)

[](https://exceljet.net/formulas/find-longest-string-with-criteria#)

*   [Previous](https://exceljet.net/formulas/find-longest-string)
    
*   [Next](https://exceljet.net/formulas/find-missing-values)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Find longest string with criteria
=================================

by Dave Bruns · Updated 29 Apr 2025

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[MAX](https://exceljet.net/functions/max-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: Find longest string with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Find_longest_string_with_criteria.png "Excel formula: Find longest string with criteria")

Summary
-------

To find the longest string (text value) in a range that meets supplied criteria, you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 together with [LEN](https://exceljet.net/functions/len-function)
 and [MAX](https://exceljet.net/functions/max-function)
. In the example shown, the formula in E6 is:

    =XLOOKUP(MAX(LEN(name)*(group=F5)),LEN(name)*(group=F5),name)
    

Where **group** (B5:B16) and **name** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is "Jonathan", which contains 8 characters and is the longest name in Group A.

Generic formula
---------------

    =XLOOKUP(MAX(LEN(range)*(criteria)),LEN(range)*(criteria),range)

Explanation 
------------

In this example, the goal is to find the longest text string in the range C5:C16 that belongs to the group entered in cell F5. The group is a variable that may be changed at any time. At the core, this is a lookup problem, and the challenge is that the value we need to look up (the string length) does not exist in the data. We need to create this as part of the formula. The easiest way to solve this problem is with the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
. However, in older versions of Excel without the XLOOKUP function, you can use an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
. Both approaches are explained below. For convenience, **group** (B5:B16) and **name** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
, but you can use regular cell references as well.

### XLOOKUP solution

In the workbook shown, the XLOOKUP function returns the longest name in the range C5:C16 when the group value in B5:B16 equals the group entered in cell F5 (which contains "A" in the example shown). The formula in E6 is:

    =XLOOKUP(MAX(LEN(name)*(group=F5)),LEN(name)*(group=F5),name)

where **group** (B5:B16) and **name** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is "Jonathan", which contains 8 characters and is the longest name in group A. The tricky part of this formula is the way we apply the criteria for **group**, which is done with [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
. Working from the inside out, we first use the LEN and MAX functions to get the length of the longest name in group A like this:

    MAX(LEN(name)*(group=F5))
    

The [LEN function](https://exceljet.net/functions/len-function)
 returns the length of a text string in characters. In this case, there are 12 names in **data** (C5:C16), so LEN returns 12 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {5;6;8;6;6;5;6;8;9;6;8;6}

We then multiply this array by the expression (group = F5):

    =MAX({5;6;8;6;6;5;6;8;9;6;8;6})*(group=F5))
    =MAX({5;6;8;6;6;5;0;0;0;0;0;0})
    =8

What happens here is that the results from LEN that are _not_ part of group A are "cancelled out" and become zero. The result is returned directly to the MAX function, which returns 8. The result from MAX is delivered to the XLOOKUP function as the _lookup\_value_:

    =XLOOKUP(8,LEN(name)*(group=F5),name)
    

At this point, we have a lookup value of 8, and we need to create a lookup array that holds all string lengths that belong to group A. To do this, we repeat the same process above to create the _lookup\_array_:

    =LEN(name)*(group=F5)
    ={5;6;8;6;6;5;6;8;9;6;8;6}*(group=F5)
    ={5;6;8;6;6;5;0;0;0;0;0;0}

We can now simplify the formula to this:

    =XLOOKUP(8,{5;6;8;6;6;5;0;0;0;0;0;0},name)

XLOOKUP performs an exact match by default. It matches the 8 in the lookup array and returns the corresponding value in **name** ("Jonathan") as a final result.

### INDEX and MATCH solution

In older versions of Excel without the XLOOKUP function, you can use an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 based on INDEX and MATCH like this:

    =INDEX(name,MATCH(MAX(LEN(name)*(group=F5)),LEN(name)*(group=F5),0))

_Note: This is an_ [_array formula_](https://exceljet.net/glossary/array-formula)
 _and must be entered with control + shift + enter in Excel 2019 and earlier._

Related formulas
----------------

[![Excel formula: Find longest string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_longest_string.png "Excel formula: Find longest string")](https://exceljet.net/formulas/find-longest-string)

### [Find longest string](https://exceljet.net/formulas/find-longest-string)

The goal is to find the longest text string in the range B5:B16. At the core, this is a lookup problem that requires creating a value (the string length) that does not exist in the data as part of the formula. The easiest way to solve this problem is with the XLOOKUP function or the FILTER function...

[![Excel formula: Get information about max value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_information_corresponding_to_max_value.png "Excel formula: Get information about max value")](https://exceljet.net/formulas/get-information-about-max-value)

### [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)

An interesting problem in Excel is how to look up information related to the maximum value in a set of data. For example, if you have a dataset of property listings and prices, you might want to find details about the property with the highest price. The best way to solve this problem depends on...

[![Excel formula: Position of max value in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/position%20of%20max%20value%20in%20list.png "Excel formula: Position of max value in list")](https://exceljet.net/formulas/position-of-max-value-in-list)

### [Position of max value in list](https://exceljet.net/formulas/position-of-max-value-in-list)

In this formula, the goal is to return the numeric position of the most expensive property in the list. The formula in cell I5 is: =MATCH(MAX(C3:C11),C3:C11,0) The MAX function extracts the maximum value from the range C3:C11. In this case, that value is 849900. This number is then supplied to the...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20operations%20in%20array%20formulas-Play.png)](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

In this video, we'll look at why boolean operations are important in array formulas. Boolean operations are a key building block in the world of dynamic array formulas. To illustrate, let's look at some simple order data. Given the data shown, how can we total orders from Texas using an array...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

### [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

In this video we're going to combine INDEX and MATCH together to look things up. Here we have the city population data we looked at before. We used the INDEX function to retrieve information about a city with a hard-coded position value. When we supply a number, INDEX retrieves information for the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Find longest string](https://exceljet.net/formulas/find-longest-string)
    
*   [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)
    
*   [Position of max value in list](https://exceljet.net/formulas/position-of-max-value-in-list)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

### Videos

*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    
*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    
*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    
*   [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)
    

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