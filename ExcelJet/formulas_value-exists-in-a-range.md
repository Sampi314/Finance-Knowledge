# Value exists in a range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/value-exists-in-a-range

---

[Skip to main content](https://exceljet.net/formulas/value-exists-in-a-range#main-content)

[](https://exceljet.net/formulas/value-exists-in-a-range#)

*   [Previous](https://exceljet.net/formulas/validate-input-with-check-mark)
    
*   [Next](https://exceljet.net/formulas/value-is-between-two-numbers)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Value exists in a range
=======================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[MATCH](https://exceljet.net/functions/match-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")

Summary
-------

To test if a value exists in a range of cells, you can use a simple formula based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
 and the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the formula in F5, copied down, is:

    =IF(COUNTIF(data,E5)>0,"Yes","No")

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16. As the formula is copied down it returns "Yes" if the value in column E exists in B5:B16 and "No" if not.

Generic formula
---------------

    =IF(COUNTIF(range,value)>0,"Yes","No")

Explanation 
------------

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result.

### COUNTIF function

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 counts cells that meet the supplied criteria. The generic syntax looks like this:

    =COUNTIF(range,criteria)

_Range_ is the range of cells to test, and _criteria_ is a condition that should be tested. COUNTIF returns the number of cells in _range_ that meet the condition defined by _criteria_. If no cells meet _criteria_, COUNTIF returns zero. In the example shown, we can use COUNTIF to count the values we are looking for like this

    COUNTIF(data,E5)

Once the [named range](https://exceljet.net/glossary/named-range)
 **data** (B5:B16) and cell E5 have been evaluated, we have:

    =COUNTIF(data,E5)
    =COUNTIF(B5:B16,"Blue")
    =1

COUNTIF returns 1 because "Blue" occurs in the range B5:B16 once. Next, we use the greater than [operator](https://exceljet.net/glossary/logical-operators)
 (>) to run a simple test to force a TRUE or FALSE result:

    =COUNTIF(data,B5)>0 // returns TRUE or FALSE

By itself, the formula above will return TRUE or FALSE. The last part of the problem is to return a "Yes" or "No" result. To handle this, we [nest](https://exceljet.net/glossary/nesting)
 the formula above into the [IF function](https://exceljet.net/functions/if-function)
 like this:

    =IF(COUNTIF(data,E5)>0,"Yes","No")

This is the formula shown in the worksheet above. As the formula is copied down, COUNTIF returns a count of the value in column E. If the count is greater than zero, the IF function returns "Yes". If the count is zero, IF returns "No".

### Slightly abbreviated

It is possible to shorten this formula slightly and get the same result like this:

    =IF(COUNTIF(data,E5),"Yes","No")

Here, we have removed the ">0" test. Instead, we simply return the count to IF as the _logical\_test_. This works because Excel will treat any non-zero number as TRUE when the number is evaluated as a [Boolean](https://exceljet.net/videos/introduction-to-booleans)
.

### Testing for a partial match

To test a range to see if it contains a _substring_ (a partial match), you can add a [wildcard](https://exceljet.net/glossary/wildcard)
 to the formula. For example, if you have a value to look for in cell C1, and you want to check the range A1:A100 for partial matches, you can configure COUNTIF to look for the value in C1 anywhere in a cell by [concatenating](https://exceljet.net/articles/how-to-concatenate-in-excel)
 asterisks on both sides:

    =COUNTIF(A1:A100,"*"&C1&"*")>0
    

The asterisk (\*) is a wildcard for one or more characters. By concatenating asterisks before and after the value in C1, the formula will count the text in C1 anywhere it appears in each cell in the range. To return "Yes" or "No", nest the formula inside the IF function as above.

### An alternative formula using MATCH

As an alternative, you can use a formula that uses the [MATCH function](https://exceljet.net/functions/match-function)
 with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 instead of COUNTIF:

    =ISNUMBER(MATCH(value,range,0))
    

The MATCH function returns the position of a match (as a number) if found, and #N/A if not found. By wrapping MATCH inside ISNUMBER, the final result will be TRUE when MATCH finds a match and FALSE when MATCH returns #N/A.

Related formulas
----------------

[![Excel formula: Range contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20specific%20text.png "Excel formula: Range contains specific text")](https://exceljet.net/formulas/range-contains-specific-text)

### [Range contains specific text](https://exceljet.net/formulas/range-contains-specific-text)

The COUNTIF function counts cells that meet supplied criteria, and returns a count of occurrences found. If no cells meet criteria, COUNTIF returns zero. The asterisk (\*) is a wildcard for one or more characters. By concatenating asterisks before and after the value in D5, the formula will count...

[![Excel formula: Range contains one of many values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20one%20of%20many%20values.png "Excel formula: Range contains one of many values")](https://exceljet.net/formulas/range-contains-one-of-many-values)

### [Range contains one of many values](https://exceljet.net/formulas/range-contains-one-of-many-values)

Each item in rng is compared to each item in values and the result is an array of TRUE or FALSE values. The double negative will force the TRUE and FALSE values to 1 and 0 respectively. Since SUMPRODUCT receives just one array, it simply adds up the items in the array and returns the result...

[![Excel formula: Range contains one of many substrings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20one%20of%20many%20substrings.png "Excel formula: Range contains one of many substrings")](https://exceljet.net/formulas/range-contains-one-of-many-substrings)

### [Range contains one of many substrings](https://exceljet.net/formulas/range-contains-one-of-many-substrings)

All the hard work is done by the COUNTIF function, which is configured to count the values in the named range "substrings" that appear the named range "rng" with like this: COUNTIF(rng,"\*"&substrings&"\*")) By wrapping substrings in the asterisks, Excel evaluates the formula like this: =...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Range contains specific date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/range%20contains%20specific%20date2.png "Excel formula: Range contains specific date")](https://exceljet.net/formulas/range-contains-specific-date)

### [Range contains specific date](https://exceljet.net/formulas/range-contains-specific-date)

First, it's important to note first that Excel dates are simply large serial numbers . When we check for a date with a formula, we are looking for a specific large number, not text . This formula is a basic example of using the COUNTIFS function with just one condition. The named range dates is...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Range contains specific text](https://exceljet.net/formulas/range-contains-specific-text)
    
*   [Range contains one of many values](https://exceljet.net/formulas/range-contains-one-of-many-values)
    
*   [Range contains one of many substrings](https://exceljet.net/formulas/range-contains-one-of-many-substrings)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [Range contains specific date](https://exceljet.net/formulas/range-contains-specific-date)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

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