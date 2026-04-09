# Get first numeric value in a range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-first-numeric-value-in-a-range

---

[Skip to main content](https://exceljet.net/formulas/get-first-numeric-value-in-a-range#main-content)

[](https://exceljet.net/formulas/get-first-numeric-value-in-a-range#)

*   [Previous](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)
    
*   [Next](https://exceljet.net/formulas/get-first-text-value-in-a-range)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get first numeric value in a range
==================================

by Dave Bruns · Updated 2 Jun 2023

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Get first numeric value in a range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_first_numeric_value_in_a_range.png "Excel formula: Get first numeric value in a range")

Summary
-------

To get the first number in a row or column you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
. In the example shown, the formula in E5 is:

    =XLOOKUP(TRUE,ISNUMBER(C5:C16),C5:C16)
    

This formula finds the first numeric value in the range C5:C16, which in this case, is 10.

Generic formula
---------------

    =XLOOKUP(TRUE,ISNUMBER(range),range)

Explanation 
------------

The general goal is to return the first numeric value in a row or column. More specifically, in the worksheet shown, we have dates in column B and a numeric value in the range C5:C16. Notice that all of the cells in this range have numeric values. Some are blank and some contain text values. We want the _first number_ that appears in the range C5:C16. This problem can be solved using the XLOOKUP function or, in older versions of Excel, an INDEX and MATCH formula.  Both methods are explained below.

### XLOOKUP function

The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 is a modern upgrade to the VLOOKUP function. XLOOKUP is flexible and can handle many different lookup scenarios. The generic syntax for _required inputs_ looks like this:

    =XLOOKUP(lookup_value,lookup_array,return_array)

Where each argument has the following meaning:

*   _lookup\_value_ - the value to look for
*   _lookup\_array_ - the range or array to search within
*   _return\_array_ - the range or array to return values from

For more details, see [How to use the XLOOKUP function](https://exceljet.net/functions/xlookup-function)
.

### The ISNUMBER function

The [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 returns TRUE when a cell contains a number, and FALSE if a cell is empty or contains a text value. If A1 contains "Age", A2 contains 32, and cell A3 is empty, the ISNUMBER function returns the following:

    =ISNUMBER(A1) // returns FALSE
    =ISNUMBER(A2) // returns TRUE
    =ISNUMBER(A3) // returns FALSE

For more details, see [How to use the ISNUMBER function](https://exceljet.net/functions/isnumber-function)
.

### XLOOKUP formula

In the worksheet shown, the formula in cell E5 combined XLOOKUP and ISNUMBER like this:

    =XLOOKUP(TRUE,ISNUMBER(C5:C16),C5:C16)

At a high level, the XLOOKUP function is configured with the _lookup\_value_ set to TRUE. The _lookup\_array_ is generated with the ISNUMBER function here:

    ISNUMBER(C5:C16)

Because the range C5:C16 contains 12 cells, ISNUMBER returns an [array](https://exceljet.net/glossary/array)
 that contains 12 TRUE and FALSE results like this:

    {FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE}

The TRUE values in this array indicate cells that contain numbers. The FALSE values indicate cells that either contain text values or are empty, such as cell C16. This array is then returned directly to the XLOOKUP function as the _lookup\_array_. At this point, we have the following:

    =XLOOKUP(TRUE,{FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE},C5:C16)

With a lookup value of TRUE, XLOOKUP matches the first TRUE in the _lookup\_array_ (the fourth value), and returns the corresponding value from the range C5:C16 (10) as a final result.

### Testing the formula

This formula is dynamic and will always return the first numeric value. To test the formula, we can add the number 12 to cell C7. Now the formula returns the 12, since 12 becomes the first numeric value in the range C5:C16.

![The result of typing the number 12 into cell C7](https://exceljet.net/sites/default/files/images/formulas/inline/get_first_numeric_value_in_a_range_test.png "The result of typing the number 12 into cell C7")

### INDEX and MATCH formula

In older versions of Excel that do not provide the XLOOKUP function, you can use an [array formula](https://exceljet.net/glossary/array-formula)
 based on INDEX and MATCH like this:

    =INDEX(C5:C16,MATCH(TRUE,ISNUMBER(C5:C16),0))

_Note: this is an array formula and must be entered with control + shift + enter in Excel 2019 and older._

This formula uses the same logic as the XLOOKUP formula above. The MATCH function is used to find the position of the first numeric value in C5:C16.

    MATCH(TRUE,ISNUMBER(C5:C16),0)

The ISNUMBER function returns an array of TRUE (numeric) and FALSE (not numeric) values:

    {FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE}

The array is returned to the MATCH function as the _lookup\_array_. The _lookup\_value_ is given as TRUE and _match\_type_ is set to 0 to require an exact match:

    MATCH(TRUE,{FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE},0)

MATCH then returns the location of the first TRUE in the array (4) as the row number to INDEX:

    =INDEX(C5:C16,4) // returns 10

INDEX then returns the value from the fourth cell in C5:C16 (10) as a final result.

For more details, see [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

Related formulas
----------------

[![Excel formula: Get first text value in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_first_text_value_in_a_range.png "Excel formula: Get first text value in a range")](https://exceljet.net/formulas/get-first-text-value-in-a-range)

### [Get first text value in a range](https://exceljet.net/formulas/get-first-text-value-in-a-range)

The general goal is to return the first text value in a range. Specifically, we have dates in column B and some city names in column C. We want a formula to find the first city listed in the range C5:C16. Because some cells in C5:C16 are empty, and some contain zeros, we need to ignore these cells...

[![Excel formula: Get first non-blank value in a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_non-blank_value_in_a_list.png "Excel formula: Get first non-blank value in a list")](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

### [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

The gist of this problem is that we want to get the first non-blank cell, but we don't have a direct way to do that in Excel. The easiest way to solve this problem is with the XLOOKUP function. XLOOKUP function The XLOOKUP function is a modern upgrade to the VLOOKUP function. XLOOKUP is very...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

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

*   [Get first text value in a range](https://exceljet.net/formulas/get-first-text-value-in-a-range)
    
*   [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    
*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    

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