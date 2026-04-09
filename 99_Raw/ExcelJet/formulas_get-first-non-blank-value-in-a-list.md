# Get first non-blank value in a list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-first-non-blank-value-in-a-list

---

[Skip to main content](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list#main-content)

[](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list#)

*   [Previous](https://exceljet.net/formulas/get-first-match-cell-contains)
    
*   [Next](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get first non-blank value in a list
===================================

by Dave Bruns · Updated 29 Apr 2025

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[NOT](https://exceljet.net/functions/not-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Get first non-blank value in a list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_first_non-blank_value_in_a_list.png "Excel formula: Get first non-blank value in a list")

Summary
-------

To get the first non-blank value in a list you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 with the [ISBLANK function](https://exceljet.net/functions/isblank-function)
. In the example shown, the formula in E5 is:

    =XLOOKUP(TRUE,NOT(ISBLANK(C5:C16)),C5:C16)
    

The result is 10, the value in cell C6.

Generic formula
---------------

    =XLOOKUP(TRUE,NOT(ISBLANK(range)),range)

Explanation 
------------

The gist of this problem is that we want to get the first non-blank cell, but we don't have a direct way to do that in Excel. The easiest way to solve this problem is with the XLOOKUP function.

### XLOOKUP function

The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 is a modern upgrade to the VLOOKUP function. XLOOKUP is very flexible and can handle many different lookup scenarios. The generic syntax for required inputs looks like this:

    =XLOOKUP(lookup_value,lookup_array,return_array)

The meaning of these arguments is as follows:

*   _lookup\_value_ - the value to look for
*   _lookup\_array_ - the range or array to search within
*   _return\_array_ - the range or array to return values from

For more details, see [How to use the XLOOKUP function](https://exceljet.net/functions/xlookup-function)
.

### The ISBLANK function

The [ISBLANK function](https://exceljet.net/functions/isblank-function)
 simply returns TRUE when a cell is empty, and FALSE if a cell is not empty. If A1 contains "apple" and B1 contains nothing, then ISBLANK returns the following:

    =ISBLANK(A1) // returns FALSE
    =ISBLANK(B1) // returns TRUE

For more details, see [How to use the ISBLANK function](https://exceljet.net/functions/isblank-function)
.

### NOT function

The [NOT function](https://exceljet.net/functions/not-function)
 simply returns the opposite of a given logical or Boolean value:

    =NOT(FALSE) // returns TRUE
    =NOT(TRUE) // returns FALSE

You can use the NOT function to "reverse" the output from other functions like ISBLANK, as seen below.

For more details, see [How to use the NOT function](https://exceljet.net/functions/not-function)
.

### XLOOKUP formula

The formula in cell E5 combines the functions above like this:

    =XLOOKUP(TRUE,NOT(ISBLANK(C5:C16)),C5:C16)

At a high level, XLOOKUP looks for TRUE and returns a corresponding value from C5:C16. It first uses ISBLANK to create an array with TRUE for blank cells and FALSE for non-blank cells. This array is then reversed using the NOT function, resulting in TRUE for non-blank cells and FALSE for blank cells. This final array serves as the lookup array for XLOOKUP. Working from the inside out, we start with the ISBLANK function is given the range C5:C16 like this:

    ISBLANK(C5:C16)

Because C5:C16 contains 12 values, ISBLANK returns an [array](https://exceljet.net/glossary/array)
 that contains 12 TRUE and FALSE results.

    {TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE}

The TRUE values in the array indicate blank cells, and the FALSE values indicate non-blank cells. The array is returned directly to the NOT function in order to "reverse" the results. The output from NOT is a new array like this:

    {FALSE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE}

In this array, the TRUE values in the array indicate _non-blank_ cells and the FALSE values indicate _blank_ cells. This array is delivered directly to the XLOOKUP function as the _lookup\_array_:

    =XLOOKUP(TRUE,{FALSE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE},C5:C16)

With a lookup value of TRUE, XLOOKUP matches the first TRUE in the _lookup\_array_ (the second value), and returns the corresponding value from the range C5:C16 (10) as a final result.

### Testing the formula

To test the formula, we can delete the value in C6. The formula returns the value in cell C8 after the value in cell C6 is deleted:

![The value in cell C8 is returned after value in cell C6 is deleted](https://exceljet.net/sites/default/files/images/formulas/inline/get_first_non-blank_value_in_a_list_C6_deleted.png "The value in cell C8 is returned after value in cell C6 is deleted")

### More specific tests

You can easily adapt the XLOOKUP formula above to target certain types of content specifically. To find the first _numeric value_ in a list, you can modify the XLOOKUP formula to use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
:

    =XLOOKUP(TRUE,ISNUMBER(range),range)
    

To find the first text value, use the [ISTEXT function](https://exceljet.net/functions/istext-function)
:

    ​=XLOOKUP(TRUE,ISTEXT(range),range)
    

One quirk of ISBLANK is that it returns FALSE if a cell contains a formula that returns an empty string (""), even though an empty string is meant to look like a blank cell. If you need to detect cells that contain a formula returning an empty string (""), you can use the [LEN function](https://exceljet.net/functions/len-function)
:

    ​=XLOOKUP(TRUE,LEN(range)>0,range)
    

Technically, this formula is testing for cells that have _more than zero characters._

### INDEX and MATCH formula

In older versions of Excel that do not provide the XLOOKUP function, you can use an [array formula](https://exceljet.net/glossary/array-formula)
 based on INDEX and MATCH like this:

    =INDEX(C5:C16,MATCH(TRUE,NOT(ISBLANK(C5:C16)),0))

_Note: this is an array formula and must be entered with control + shift + enter in Excel 2019 and older._

This formula has basically the same logic as the XLOOKUP formula above. The MATCH function is used to find the position of the first non-blank cell in C5:C16. The NOT and ISBLANK functions create an array of TRUE (for non-blank cells) and FALSE (for blank cells) values that are used as a lookup array.

    MATCH(TRUE,NOT(ISBLANK(C5:C16)),0)

After NOT and ISBLANK are evaluated, we have an array like this:

    {FALSE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE}

The array is returned to the MATCH function as the _lookup\_array_. The _lookup\_value_ is provided as TRUE, and _match\_type_ is set to 0 to force an exact match:

    MATCH(TRUE,{FALSE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE},0)

MATCH then returns the location of the first TRUE in the array (2) as the row number to INDEX:

    =INDEX(C5:C16,2) // returns 10

INDEX takes over and returns the value from the second cell in C5:C16 (10) as a final result.

As with XLOOKUP above, you can adapt the INDEX and MATCH formula to target specific content. For example, to get the first _numeric value,_ use ISNUMBER:

    =INDEX(range,MATCH(TRUE,ISNUMBER(range),0)) // first number

To get the first text value, use ISTEXT:

    =INDEX(range,MATCH(TRUE,ISTEXT(range),0)) // first text
    

To get the value in the first cell with more than zero characters, use LEN:

    =INDEX(range,MATCH(TRUE,LEN(range)>0,0))
    

_These are all array formulas, which must be entered with control + shift + enter in Excel 2019 and older._

For more details, see [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

Related formulas
----------------

[![Excel formula: Get first text value in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_first_text_value_in_a_range.png "Excel formula: Get first text value in a range")](https://exceljet.net/formulas/get-first-text-value-in-a-range)

### [Get first text value in a range](https://exceljet.net/formulas/get-first-text-value-in-a-range)

The general goal is to return the first text value in a range. Specifically, we have dates in column B and some city names in column C. We want a formula to find the first city listed in the range C5:C16. Because some cells in C5:C16 are empty, and some contain zeros, we need to ignore these cells...

[![Excel formula: Get first numeric value in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_numeric_value_in_a_range.png "Excel formula: Get first numeric value in a range")](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)

### [Get first numeric value in a range](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)

The general goal is to return the first numeric value in a row or column. More specifically, in the worksheet shown, we have dates in column B and a numeric value in the range C5:C16. Notice that all of the cells in this range have numeric values. Some are blank and some contain text values. We...

[![Excel formula: Get value of last non-empty cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_value_of_last_non-empty_cell.png "Excel formula: Get value of last non-empty cell")](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

### [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

In this example, the goal is to get the last value in column B, even when data may contain empty cells. A secondary goal is to get the corresponding value in column C. This is useful for analyzing datasets where the most recent or last entry is significant. In the current version of Excel, a good...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

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
    
*   [Get first numeric value in a range](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)
    
*   [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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