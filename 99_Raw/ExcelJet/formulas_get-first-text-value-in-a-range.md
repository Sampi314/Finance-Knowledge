# Get first text value in a range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-first-text-value-in-a-range

---

[Skip to main content](https://exceljet.net/formulas/get-first-text-value-in-a-range#main-content)

[](https://exceljet.net/formulas/get-first-text-value-in-a-range#)

*   [Previous](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)
    
*   [Next](https://exceljet.net/formulas/get-first-text-value-in-a-row)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get first text value in a range
===============================

by Dave Bruns · Updated 6 Jun 2023

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[ISTEXT](https://exceljet.net/functions/istext-function)

![Excel formula: Get first text value in a range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get_first_text_value_in_a_range.png "Excel formula: Get first text value in a range")

Summary
-------

To get the text value in a range you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 with the asterisk (\*) [wildcard](https://exceljet.net/glossary/wildcard)
. In the example shown, the formula in E5 is:

    =XLOOKUP("*",C5:C16,C5:C16,,2)
    

This formula finds the text value in the range C5:C16. After ignoring C5, which is empty, and C6 and C7, which contain zeros, the formula returns "New York" - the first text value in the range.

_Note: it is also possible to solve this problem with a more modern array formula based on the [ISTEXT function](https://exceljet.net/functions/istext-function)
. See below for more information._

Generic formula
---------------

    =XLOOKUP("*",range,range,,2)

Explanation 
------------

The general goal is to return the first text value in a range. Specifically, we have dates in column B and some city names in column C. We want a formula to find the first city listed in the range C5:C16. Because some cells in C5:C16 are empty, and some contain zeros, we need to ignore these cells in the process. This problem can be solved using the XLOOKUP function. In older versions of Excel, you can use the VLOOKUP function or an INDEX and MATCH formula. It is also possible to solve this problem with a more modern array formula based on the ISTEXT function. See below for details

### Wildcards in Excel formulas

Some Excel functions support [wildcards](https://exceljet.net/glossary/wildcard)
, which can be used to solve this problem. In this case, the wildcard we want is the asterisk (\*) which will match any one or more characters. It's not obvious from the description, but the asterisk (\*) wildcard will only match _text characters_. It will ignore empty cells, numbers, and errors.

### XLOOKUP function

The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
, a modern upgrade of the VLOOKUP function, offers one solution to this problem. When XLOOKUP is used with wildcards, the generic syntax for _required inputs_ looks like this:

    =XLOOKUP(lookup_value,lookup_array,return_array,,match_mode)

Where each argument has the following meaning:

*   _lookup\_value_ - the value to look for
*   _lookup\_array_ - the range or array to search within
*   _return\_array_ - the range or array to return values from
*   _if\_not-found_ - value to return if no match is found (omitted above)
*   _match\_mode_ - settings for exact, approximate, and wildcard matching

For more details, see [How to use the XLOOKUP function](https://exceljet.net/functions/xlookup-function)
.

In the worksheet shown, the formula in E5 is:

    =XLOOKUP("*",C5:C16,C5:C16,,2)

Here are the values provided to XLOOKUP:

*   _lookup\_value_ - "\*" (the wildcard)
*   _lookup\_array_ - C5:C16
*   _return\_array_ - C5:C16
*   _if\_not-found_ - omitted
*   _match\_mode_ - 2 (to enable wildcard matching)

In this configuration, XLOOKUP ignores the empty cell and zero values in the first three cells and returns "New York", which is the first text value in C5:C16. Although the range in this example is organized vertically, XLOOKUP can be used in the same way with a horizontal range. Also, we can easily adapt this formula to return the date (as seen in F5) like this:

    =XLOOKUP("*",C5:C16,B5:B16,,2) // get date

This formula will return the corresponding date from the range B5:B16 that aligns with the first text value in C5:C16 - in this case, 04-Aug-23.

### VLOOKUP function

The VLOOKUP function is an older function in Excel widely used for common lookup problems that involve _vertical_ ranges. Like XLOOKUP, VLOOKUP supports wildcards. The generic syntax for VLOOKUP looks like this:

    =VLOOKUP(lookup_value,table_array,col_index_num,range_lookup)

Where each argument has the following meaning:

*   _lookup\_value_ - the value to look for
*   _table\_array_ - the table to look within
*   _col\_index\_num_ - the number of the column to retrieve
*   _range\_lookup_ - settings for exact and approximate matching (must be exact for wildcards)

For more details, see [How to use the VLOOKUP function](https://exceljet.net/functions/vlookup-function)
.

In the worksheet shown, you can use VLOOKUP to retrieve the first City in the range C5:C16 like this:

    =VLOOKUP("*",C5:C16,1,0)

The values provided to VLOOKUP are as follows:

*   _lookup\_value_ - "\*" (the wildcard)
*   _table\_array_ - C5:C16 (one-column table)
*   _col\_index\_num_ - 1 (first column)
*   _range\_lookup_ - 0 or FALSE for an exact match (required for wildcards)

In this configuration, VLOOKUP ignores the empty cell and zero values in the first three cells and returns "New York", which is the first text value in C5:C16. Note that VLOOKUP is limited to _vertical ranges only_. To solve this problem in the same way with a horizontal range you can use the [HLOOKUP function](https://exceljet.net/formulas/get-first-text-value-with-hlookup)
. Alternatively, you can use an INDEX and MATCH formula, as explained below.

### INDEX and MATCH

One problem with VLOOKUP in this problem is that we can't return the date in B5:B16 that corresponds to the first text value in C5:C16. This is one of the [limitations of VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)
, which requires the lookup values to be the _first column in a table_. However, we can use INDEX and MATCH to get both the city and the date like this:

    =INDEX(C5:C16,MATCH("*",C5:C16,0)) // get city
    =INDEX(B5:B16,MATCH("*",C5:C16,0)) // get date

The approach is the same as with XLOOKUP and VLOOKUP above - we are using MATCH with the (\*) wildcard to find the first text value. The location is then provided to INDEX, which returns the final result.

For more details on INDEX with MATCH, see: [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

### Array formula approach

A more modern and flexible way to solve this problem is with an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 that uses the ISTEXT function. With XLOOKUP, you can use a formula like this:

    =XLOOKUP(TRUE,ISTEXT(C5:C16),C5:C16,,2)

In a nutshell, we use the [ISTEXT function](https://exceljet.net/functions/istext-function)
 to test the values in C5:C16 and return an array of TRUE and FALSE values. We then configure XLOOKUP to search this array for the first TRUE value. This is a more flexible approach because it can be easily adapted to test for other types of content, like numbers, errors, and even blank cells. For a more complete explanation, [see this example](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)
.

Related formulas
----------------

[![Excel formula: Get first non-blank value in a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_non-blank_value_in_a_list.png "Excel formula: Get first non-blank value in a list")](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

### [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

The gist of this problem is that we want to get the first non-blank cell, but we don't have a direct way to do that in Excel. The easiest way to solve this problem is with the XLOOKUP function. XLOOKUP function The XLOOKUP function is a modern upgrade to the VLOOKUP function. XLOOKUP is very...

[![Excel formula: Get first numeric value in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_numeric_value_in_a_range.png "Excel formula: Get first numeric value in a range")](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)

### [Get first numeric value in a range](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)

The general goal is to return the first numeric value in a row or column. More specifically, in the worksheet shown, we have dates in column B and a numeric value in the range C5:C16. Notice that all of the cells in this range have numeric values. Some are blank and some contain text values. We...

[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)

### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ISTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20istext%20function.png "Excel ISTEXT function")](https://exceljet.net/functions/istext-function)

### [ISTEXT Function](https://exceljet.net/functions/istext-function)

The Excel ISTEXT function returns TRUE when a cell contains a [text value](https://exceljet.net/glossary/text-value)
, and FALSE if the cell contains any other value. You can use the ISTEXT function to check if a cell contains a text value, or a numeric value entered as text.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20for%20wildcard%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-for-wildcard-matches)

### [How to use VLOOKUP for wildcard matches](https://exceljet.net/videos/how-to-use-vlookup-for-wildcard-matches)

In this video we'll look at how to use the VLOOKUP function with wildcards. This is useful when you want to allow a lookup based on a partial match. Let's take a look. Here we have the employee list we've looked at previously. This time, however, notice that the ID column has been moved into the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)
    
*   [Get first numeric value in a range](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)
    
*   [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISTEXT Function](https://exceljet.net/functions/istext-function)
    

### Videos

*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    
*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to use VLOOKUP for wildcard matches](https://exceljet.net/videos/how-to-use-vlookup-for-wildcard-matches)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    

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