# Get first text value in a row - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-first-text-value-in-a-row

---

[Skip to main content](https://exceljet.net/formulas/get-first-text-value-in-a-row#main-content)

[](https://exceljet.net/formulas/get-first-text-value-in-a-row#)

*   [Previous](https://exceljet.net/formulas/get-first-text-value-in-a-range)
    
*   [Next](https://exceljet.net/formulas/get-information-about-max-value)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get first text value in a row
=============================

by Dave Bruns · Updated 6 Jun 2023

Related functions 
------------------

[HLOOKUP](https://exceljet.net/functions/hlookup-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[ISTEXT](https://exceljet.net/functions/istext-function)

![Excel formula: Get first text value in a row](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_first_text_value_in_a_row.png "Excel formula: Get first text value in a row")

Summary
-------

To get the text value in a range you can use the [HLOOKUP function](https://exceljet.net/functions/hlookup-function)
 with the asterisk (\*) [wildcard](https://exceljet.net/glossary/wildcard)
. In the example shown, the formula in E5 is:

    =HLOOKUP("*",C5:F5,1,0)
    

In cell H5, the result is A, since "A" is the first text value in the range C5:F5. As the formula is copied down, it returns the first text value found in each row. Notice that numbers and blank cells are ignored.

_Note: A more modern approach is to use the XLOOKUP function. See below for details._

Generic formula
---------------

    =HLOOKUP("*",range,1,FALSE)

Explanation 
------------

The goal is to return the first text value in each row, ignoring both blank cells and cells that contain numbers. This problem can be solved using the HLOOKUP function. In newer versions of Excel, you can use the XLOOKUP function, which is a more modern lookup function that can look up values in vertical or horizontal ranges.

### Wildcards in Excel formulas

Some Excel functions support [wildcards](https://exceljet.net/glossary/wildcard)
, which can be used to solve this problem. In this case, we can use the asterisk (\*) as a wildcard, which will match any number of text characters. The asterisk (\*) wildcard will ignore empty cells, numbers, and errors.

###  HLOOKUP function

The HLOOKUP function is an older function in Excel widely used for common lookup problems that involve _horizontal_ ranges. Like VLOOKUP, HLOOKUP supports wildcards when operating in exact match mode. The generic syntax for HLOOKUP looks like this:

    =HLOOKUP(lookup_value,table_array,col_index_num,range_lookup)

Where each argument has the following meaning:

*   _lookup\_value_ - the value to look for
*   _table\_array_ - the horizontal range to look in
*   _row\_index\_num_ - the number of the row to retrieve _table\_array_
*   _range\_lookup_ - settings for exact and approximate matching (must be exact for wildcards)

For more details, see [How to use the HLOOKUP function](https://exceljet.net/functions/hlookup-function)
.

In the worksheet shown, we can use HLOOKUP to retrieve the first text value in C5:H5 like this:

    =HLOOKUP("*",C5:F5,1,0)

The values provided to VLOOKUP are as follows:

*   _lookup\_value_ - "\*" (the wildcard)
*   _table\_array_ - C5:F5 (one-row table)
*   _row\_index\_num_ - 1 (first row)
*   _range\_lookup_ - 0 or FALSE for an exact match (required for wildcards)

In this configuration, HLOOKUP ignores empty cells and numeric values and returns "A", which is the first text value in C5:F5. Note that HLOOKUP is limited to _horizontal ranges only_. To solve this problem in the same way with a vertical range you can use VLOOKUP or XLOOKUP, [as explained here](https://exceljet.net/formulas/get-first-text-value-in-a-range)
. 

### XLOOKUP function

The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 is a modern function that can replace both the VLOOKUP function and the HLOOKUP function. Like HLOOKUP and VLOOKUP,  XLOOKUP supports wildcards, and generic syntax for _required inputs_ in this problem is:

    =XLOOKUP(lookup_value,lookup_array,return_array,,match_mode)

Where each argument has the following meaning:

*   _lookup\_value_ - the value to look for
*   _lookup\_array_ - the range or array to search within
*   _return\_array_ - the range or array to return values from
*   _if\_not-found_ - value to return if no match is found (omitted above)
*   _match\_mode_ - settings for exact, approximate, and wildcard matching

For more details, see [How to use the XLOOKUP function](https://exceljet.net/functions/xlookup-function)
.

To solve this problem with XLOOKUP, we can use a formula like this:

    =XLOOKUP("*",C5:F5,C5:F5,,2)

Here are the values provided to XLOOKUP:

*   _lookup\_value_ - "\*" (the wildcard)
*   _lookup\_array_ - C5:F5
*   _return\_array_ - C5:F5
*   _if\_not-found_ - omitted
*   _match\_mode_ - 2 (to enable wildcard matching)

In this configuration, XLOOKUP ignores the empty cell and zero values in the first three cells and returns "A", which is the first text value in C5:F5. One of XLOOKUP's hallmark features is flexibility. For example, to retrieve the month in which the first text value occurs, we use a formula like this:

    =XLOOKUP("*",C5:F5,$C$4:$F$4,,2) // get month

This formula will return the corresponding month from the range C4:F4 that aligns with the first text value in each row, as seen below:

![Using XLOOKUP to get the month associated with first text value](https://exceljet.net/sites/default/files/images/formulas/inline/get_first_text_value_in_a_row_xlookup_option.png "Using XLOOKUP to get the month associated with first text value")

### Array formula approach

A more modern and flexible way to solve this problem with XLOOKUP is with an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 that uses the ISTEXT function. With XLOOKUP, you can use a formula like this:

    =XLOOKUP(TRUE,ISTEXT(C5:F5),C5:F5)

In a nutshell, we use the [ISTEXT function](https://exceljet.net/functions/istext-function)
 to test the values in C5:F5 and return an array of TRUE and FALSE values. We then configure XLOOKUP to search this array for the first TRUE value and return the corresponding value from C5:F5. This is a more flexible approach because it can be easily adapted to test for other types of content, like numbers, errors, and even blank cells. For a more complete explanation, [see this example](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)
.

Related formulas
----------------

[![Excel formula: Get first text value in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_first_text_value_in_a_range.png "Excel formula: Get first text value in a range")](https://exceljet.net/formulas/get-first-text-value-in-a-range)

### [Get first text value in a range](https://exceljet.net/formulas/get-first-text-value-in-a-range)

The general goal is to return the first text value in a range. Specifically, we have dates in column B and some city names in column C. We want a formula to find the first city listed in the range C5:C16. Because some cells in C5:C16 are empty, and some contain zeros, we need to ignore these cells...

[![Excel formula: Get first non-blank value in a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_non-blank_value_in_a_list.png "Excel formula: Get first non-blank value in a list")](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

### [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

The gist of this problem is that we want to get the first non-blank cell, but we don't have a direct way to do that in Excel. The easiest way to solve this problem is with the XLOOKUP function. XLOOKUP function The XLOOKUP function is a modern upgrade to the VLOOKUP function. XLOOKUP is very...

[![Excel formula: Get first numeric value in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_numeric_value_in_a_range.png "Excel formula: Get first numeric value in a range")](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)

### [Get first numeric value in a range](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)

The general goal is to return the first numeric value in a row or column. More specifically, in the worksheet shown, we have dates in column B and a numeric value in the range C5:C16. Notice that all of the cells in this range have numeric values. Some are blank and some contain text values. We...

Related functions
-----------------

[![Excel HLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hlookup%20function.png "Excel HLOOKUP function")](https://exceljet.net/functions/hlookup-function)

### [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)

The Excel HLOOKUP function finds and retrieve a value from data in a horizontal table. The "H" in HLOOKUP stands for "horizontal", and lookup values must appear in the first row of the table, moving horizontally to the right. HLOOKUP supports approximate and exact matching, and...

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel ISTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20istext%20function.png "Excel ISTEXT function")](https://exceljet.net/functions/istext-function)

### [ISTEXT Function](https://exceljet.net/functions/istext-function)

The Excel ISTEXT function returns TRUE when a cell contains a [text value](https://exceljet.net/glossary/text-value)
, and FALSE if the cell contains any other value. You can use the ISTEXT function to check if a cell contains a text value, or a numeric value entered as text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get first text value in a range](https://exceljet.net/formulas/get-first-text-value-in-a-range)
    
*   [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)
    
*   [Get first numeric value in a range](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)
    

### Functions

*   [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [ISTEXT Function](https://exceljet.net/functions/istext-function)
    

### Articles

*   [XLOOKUP vs VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)
    

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