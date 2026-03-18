# If cell contains this or that - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-cell-contains-this-or-that

---

[Skip to main content](https://exceljet.net/formulas/if-cell-contains-this-or-that#main-content)

[](https://exceljet.net/formulas/if-cell-contains-this-or-that#)

*   [Previous](https://exceljet.net/formulas/if-cell-contains)
    
*   [Next](https://exceljet.net/formulas/if-cell-equals)
    

[If](https://exceljet.net/formulas#If)

If cell contains this or that
=============================

by Dave Bruns · Updated 21 May 2024

Related functions 
------------------

[SEARCH](https://exceljet.net/functions/search-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[OR](https://exceljet.net/functions/or-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: If cell contains this or that](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_cell_contains_this_or_that.png "Excel formula: If cell contains this or that")

Summary
-------

To test if a cell contains x, y, or z, you can create a logical test with the [OR function](https://exceljet.net/functions/or-function)
 and use the [IF function](https://exceljet.net/functions/if-function)
 to evaluate the result. In the example shown, the formula in D5 is:

    =IF(OR(ISNUMBER(SEARCH({"abc","xyz"},B5))),"x","")
    

The result in cell D5 is "x" since "jim@abc" contains "abc". The result from IF can be adjusted as desired.

Generic formula
---------------

    =IF(OR(ISNUMBER(SEARCH({"abc","xyz"},A1))),"x","")

Explanation 
------------

The goal is to do something if a cell contains one substring or another. Most users will think first of the IF function. However, one problem with IF is that it does [not support wildcards](https://exceljet.net/formulas/if-with-wildcards)
 like "?" and "\*". This means we can't use IF by itself to test for a substring like "abc" or "xyz" that might appear _anywhere in a cell_. One option (seen in the example) is to create a logical test with ISNUMBER, SEARCH, and OR, then use the IF function to return a final result. Another approach is to use the COUNTIF function with the SUM function to create the logical test. Both approaches are explained below.

### OR + SEARCH + ISNUMBER

The [SEARCH function](https://exceljet.net/functions/search-function)
 is designed to look inside a text string for a given substring. If SEARCH finds the substring, it returns the _position_ of the substring in the text as a number. If the substring is not found, SEARCH returns a #VALUE error. For example:

    =SEARCH("p","apple") // returns 2
    =SEARCH("z","apple") // returns #VALUE!

The [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
. ISNUMBER returns TRUE for numeric values and FALSE for anything else:

    =ISNUMBER(2) // returns TRUE
    =ISNUMBER("a") // returns FALSE
    
    

We can use ISNUMBER to convert the result from SEARCH into a TRUE or FALSE value like this:

    =ISNUMBER(SEARCH("p","apple")) // returns TRUE
    =ISNUMBER(SEARCH("z","apple")) // returns FALSE

If SEARCH finds the substring, it returns the position as a number, and ISNUMBER returns TRUE. If SEARCH _doesn't_ find the substring, it returns an error, and ISNUMBER returns FALSE. This works fine, but the challenge in this problem is that we need to test for _two substrings_, not one. We can do this by using SEARCH and ISNUMBER twice inside the OR function:

    =OR(ISNUMBER(SEARCH("abc",B5)),ISNUMBER(SEARCH("xyz",B5)))

Now if either of the expressions returns TRUE, the OR function will return TRUE and trigger the IF function. One way to simplify the formula a bit is to use an [array constant](https://exceljet.net/glossary/array-constant)
 and a single expression like this:

    =OR(ISNUMBER(SEARCH({"abc","xyz"},B5)))

An array constant is a structure that holds multiple values. It works like a range in Excel, except the values in an array constant are hard coded. Because we are giving SEARCH two substrings, it will return two results. The ISNUMBER function will also return two results to the OR function, which will evaluate these results as before.

_Note: the SEARCH function is not case-sensitive. If you need a case-sensitive option you can switch to the [FIND function](https://exceljet.net/functions/find-function)
 as [explained here](https://exceljet.net/formulas/cell-contains-specific-text)
._

### IF function

Putting this all together, we can use the formula above inside the IF function as the logical test like this:

    =IF(OR(ISNUMBER(SEARCH({"abc","xyz"},B5))),"x","")

This is the formula used in cell D5 of the example. As the formula is copied down, it returns "x" if an email address contains either "abc" or "xyz" and an empty string ("") if not. You are free to adjust the IF formula to return whatever values you like.

_Note: the IF function simply leaves an "x" in a cell as a marker. I__f the goal is to retrieve all matching cells or records, see the [FILTER function](https://exceljet.net/formulas/filter-text-contains)
._

### COUNTIF + SUM

Another way to solve this problem is with the [COUNTIF function](https://exceljet.net/functions/countif-function)
 together with the SUM function like this:

    =IF(SUM(COUNTIF(B5,{"*abc*","*xyz*"})),"x","")

The core of this formula is COUNTIF, which returns zero if none of the substrings is found, and a positive number if at least one substring is found. The twist is that we are giving COUNTIF more than one substring to look for in the criteria, supplied as an "[array constant](https://exceljet.net/glossary/array-constant)
". As a result, COUNTIF will return an [array](https://exceljet.net/glossary/array)
 of counts, one count per condition. Because we are getting back an array from COUNTIF, we use the SUM function to sum all items in the array. The result goes into the IF function as the _logical\_test_. Any non-zero number will be evaluated as TRUE.

Note that we are also using the asterisk (\*) as a [wildcard](https://exceljet.net/glossary/wildcard)
 for zero or more characters on either side of the substrings. This is what allows COUNTIF to count the substrings anywhere in the text (i.e. this provides the "contains" behavior).

### Notes

1.  If you are testing many values, you can use a _range_ instead of an _array constant_ to provide values to check. In Excel 2019 and earlier, using a range will make the formula an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
     that must be entered with control + shift + enter. In the current version of Excel, no special handling is required. 
2.  The COUNTIF function [will accept ranges only](https://exceljet.net/articles/excels-racon-functions)
     for the _range_ argument; you can't feed COUNTIF an _array_ that comes from another formula. This can be a problem when working with [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    , where it is more common to pass arrays from one formula to another. The OR + SEARCH + ISNUMBER formula does not have this limitation.

Related formulas
----------------

[![Excel formula: If cell is this OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20is%20this%20or%20that.png "Excel formula: If cell is this OR that")](https://exceljet.net/formulas/if-cell-is-this-or-that)

### [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)

In the example shown, we want to mark or "flag" records where the color is red OR green. In other words, we want to check the color in column B, and then leave a marker (x) if we find the word "red" or "green". In D6, the formula is: =IF(OR(B6="red",B6="green"),"x","") This is an example of nesting...

[![Excel formula: If cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains.png "Excel formula: If cell contains")](https://exceljet.net/formulas/if-cell-contains)

### [If cell contains](https://exceljet.net/formulas/if-cell-contains)

The goal is to do something if a cell contains a given substring. For example, in the worksheet above, a formula returns "x" when a cell contains "abc". If you are familiar with Excel, you will probably think first of the IF function. However, one limitation of IF is that it does not support...

[![Excel formula: If cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20contains%20one%20of%20many%20things.png "Excel formula: If cell contains one of many things")](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

### [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

This formula uses two named ranges : things , and results . If you are porting this formula directly, be sure to use named ranges with the same names (defined based on your data). If you don't want to use named ranges, use absolute references instead. The core of this formula is this snippet:...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

Related functions
-----------------

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/If%20this%20OR%20that-thumb.png)](https://exceljet.net/videos/if-this-or-that)

### [If this OR that](https://exceljet.net/videos/if-this-or-that)

Sometimes, you might need to write a formula that uses the IF function to test for this OR that, or this AND that. There are two special functions, AND and OR, that make this easy to do. Let's take a look. In this first worksheet, we have a list of employees. Let's assume that you need to group...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)
    
*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    
*   [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    

### Functions

*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [If this OR that](https://exceljet.net/videos/if-this-or-that)
    

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