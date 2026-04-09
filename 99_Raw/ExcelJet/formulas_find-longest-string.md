# Find longest string - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/find-longest-string

---

[Skip to main content](https://exceljet.net/formulas/find-longest-string#main-content)

[](https://exceljet.net/formulas/find-longest-string#)

*   [Previous](https://exceljet.net/formulas/find-closest-match)
    
*   [Next](https://exceljet.net/formulas/find-longest-string-with-criteria)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Find longest string
===================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[FILTER](https://exceljet.net/functions/filter-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[MAX](https://exceljet.net/functions/max-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: Find longest string](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/find_longest_string.png "Excel formula: Find longest string")

Summary
-------

To find the longest string (text value) in a range, you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 together with [LEN](https://exceljet.net/functions/len-function)
 and [MAX](https://exceljet.net/functions/max-function)
. In the example shown, the formula in E6 is:

    =XLOOKUP(MAX(LEN(data)),LEN(data),data)
    

Where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16. The result is "Esmeralda", which contains 9 characters.

Generic formula
---------------

    =XLOOKUP(MAX(LEN(range)),LEN(range),range)

Explanation 
------------

The goal is to find the longest text string in the range B5:B16. At the core, this is a lookup problem that requires creating a value (the string length) that does not exist in the data as part of the formula. The easiest way to solve this problem is with the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 or the [FILTER function](https://exceljet.net/functions/filter-function)
. However in older versions of Excel without the XLOOKUP function, you can use an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
. Both approaches are explained below. For convenience, the range B5:B16 is named **data**. However, you can use a regular cell reference as well.

### XLOOKUP solution

In the workbook shown, the XLOOKUP function is used to return the longest name in the range B5:B16. The formula in E6 is:

    =XLOOKUP(MAX(LEN(data)),LEN(data),data)
    

Where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16. The result is "Esmeralda", which contains 9 characters. Working from the inside out, we first use the LEN and MAX functions to get the length of the longest name like this:

    MAX(LEN(data))
    

The [LEN function](https://exceljet.net/functions/len-function)
 returns the length of a text string in characters. In this case, there are 12 names in **data** (B5:B16) so LEN returns 12 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {5;6;8;6;6;5;6;8;9;6;8;6}

Each number represents the length in characters of one name in the data. The result from LEN is returned directly to the MAX function, which returns 9:

    MAX({5;6;8;6;6;5;6;8;9;6;8;6}) // returns 9

The result from MAX is delivered to XLOOKUP as the _lookup\_value_:

    =XLOOKUP(9,LEN(data),data)
    

At this point, we have a lookup value of 9 and we need to create a lookup array that holds all string lengths. To do this we call the LEN function again, the same as before:

    LEN(data) // returns {5;6;8;6;6;5;6;8;9;6;8;6}
    

The result from LEN becomes the _lookup\_array_:

    =XLOOKUP(9,{5;6;8;6;6;5;6;8;9;6;8;6},data)

XLOOKUP performs an exact match by default. It matches the 9 in the lookup array and returns the corresponding value in **data** ("Esmeralda") as a final result. 

_Note: with the worksheet as shown, the result from XLOOKUP and FILTER is the same, since there are no ties. However, if there were two names with a length of 9 characters, FILTER would return both names and the XLOOKUP formula would return just the first name with 9 characters._

### FILTER solution

Another way to solve this problem is with the [FILTER function](https://exceljet.net/functions/filter-function)
, which is designed to retrieve multiple matching records. This makes sense in cases where there may be ties, and you would like to report all results. To get the longest string with FILTER, including any tie values, the formula is:

    =FILTER(data,LEN(data)=MAX(LEN(data)))

The logic in this formula is similar to what we used above with XLOOKUP. We are asking FILTER for _all values_ in **data** where the length of the text string equals the max length found in **data**.

### INDEX and MATCH solution

In older versions of Excel without the XLOOKUP function, you can use an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 based on INDEX and MATCH like this:

    {=INDEX(data,MATCH(MAX(LEN(data)),LEN(data),0))}

_Note: enter as an [array formula](https://exceljet.net/glossary/array-formula)
 with control + shift + enter in Excel 2019 and earlier._

Most of the hard work in this formula is done with the MATCH function, which is set up like this:

    MATCH(MAX(LEN(data)),LEN(data),0)

Here, MATCH is set up to perform an exact match by supplying zero for _match\_type_. For _lookup\_value_, we supply the maximum string length found in all data:

    MAX(LEN(data))
    

LEN returns an [array](https://exceljet.net/glossary/array)
 of results (lengths), one for each name in the list:

    {5;6;8;6;6;5;6;8;9;6;8;6}

MAX then returns the largest value in the array (9):

    MAX({5;6;8;6;6;5;6;8;9;6;8;6}) // returns 9

For the _lookup\_array_, LEN is again used to return an array that contains all lengths:

    LEN(data) // returns {5;6;8;6;6;5;6;8;9;6;8;6}
    

After LEN and MAX run, we have the following:

    MATCH(9,{5;6;8;6;6;5;6;8;9;6;8;6},0)
    

MATCH then returns the position of the max value (9) directly to the INDEX function as the _row\_num_:

    =INDEX(data,9)
    

Finally, the [INDEX function](https://exceljet.net/functions/index-function)
 returns the value in the 9th row of **data**, which is "Esmeralda".

_Note: it is a coincidence only that the longest name (9 characters), happens to be in the 9th row!_

Related formulas
----------------

[![Excel formula: Find longest string with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Find_longest_string_with_criteria.png "Excel formula: Find longest string with criteria")](https://exceljet.net/formulas/find-longest-string-with-criteria)

### [Find longest string with criteria](https://exceljet.net/formulas/find-longest-string-with-criteria)

In this example, the goal is to find the longest text string in the range C5:C16 that belongs to the group entered in cell F5. The group is a variable that may be changed at any time. At the core, this is a lookup problem, and the challenge is that the value we need to look up (the string length)...

[![Excel formula: Position of max value in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/position%20of%20max%20value%20in%20list.png "Excel formula: Position of max value in list")](https://exceljet.net/formulas/position-of-max-value-in-list)

### [Position of max value in list](https://exceljet.net/formulas/position-of-max-value-in-list)

In this formula, the goal is to return the numeric position of the most expensive property in the list. The formula in cell I5 is: =MATCH(MAX(C3:C11),C3:C11,0) The MAX function extracts the maximum value from the range C3:C11. In this case, that value is 849900. This number is then supplied to the...

[![Excel formula: Get information about max value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_information_corresponding_to_max_value.png "Excel formula: Get information about max value")](https://exceljet.net/formulas/get-information-about-max-value)

### [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)

An interesting problem in Excel is how to look up information related to the maximum value in a set of data. For example, if you have a dataset of property listings and prices, you might want to find details about the property with the highest price. The best way to solve this problem depends on...

[![Excel formula: Find closest match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_closest_match_0.png "Excel formula: Find closest match")](https://exceljet.net/formulas/find-closest-match)

### [Find closest match](https://exceljet.net/formulas/find-closest-match)

In this example, the goal is to find the closest match to a target value entered in cell E5. Although it may not look like it, this is essentially a look-up problem. The easiest way to solve this problem is with the XLOOKUP function . However in older versions of Excel without the XLOOKUP function...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

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

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Find longest string with criteria](https://exceljet.net/formulas/find-longest-string-with-criteria)
    
*   [Position of max value in list](https://exceljet.net/formulas/position-of-max-value-in-list)
    
*   [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)
    
*   [Find closest match](https://exceljet.net/formulas/find-closest-match)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

### Videos

*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    
*   [XLOOKUP vs VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
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