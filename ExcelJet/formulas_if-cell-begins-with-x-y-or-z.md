# If cell begins with x, y, or z - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z

---

[Skip to main content](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z#main-content)

[](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z#)

*   [Previous](https://exceljet.net/formulas/calculate-sales-commission-with-if)
    
*   [Next](https://exceljet.net/formulas/if-cell-contains)
    

[If](https://exceljet.net/formulas#If)

If cell begins with x, y, or z
==============================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[OR](https://exceljet.net/functions/or-function)

[LEFT](https://exceljet.net/functions/left-function)

[IF](https://exceljet.net/functions/if-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7838/download?token=7qO3L7hj)
 (15.58 KB)

![Excel formula: If cell begins with x, y, or z](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_cell_begins_with_x_y_or_z_0.png "Excel formula: If cell begins with x, y, or z")

Summary
-------

To test if a cell contains x, y, or z, you can create a logical test with the [OR function](https://exceljet.net/functions/or-function)
 and use the [IF function](https://exceljet.net/functions/if-function)
 to evaluate the result. In the example shown, the formula in C5 is:

    =IF(OR(LEFT(B5)={"x","y","z"}),"x","")
    

The result in cell D5 is "x" since "ZQR" begins with "z". The result from IF can be adjusted as desired.

Generic formula
---------------

    =IF(OR(LEFT(A1)={"x","y","z"}),"x","")

Explanation 
------------

The goal is to take a specific action when a value begins with "x", "y", or "z". As is often the case in Excel, there are multiple ways to approach this problem. The simplest way is to use the OR function with the LEFT function to create the required logical test. Another option is to use the COUNTIF function. Both approaches are explained below.

_Note: this formula is more advanced because we need to test for "cell begins with". For a more basic example of "cell equals this or that" [see this page](https://exceljet.net/formulas/if-cell-is-this-or-that)
 or [this video](https://exceljet.net/videos/if-this-or-that)
._

### OR + LEFT

The [OR function](https://exceljet.net/functions/or-function)
 returns TRUE if any argument is TRUE. For example, if cell A1 contains "apple" then:

    =OR(A1="orange",A1="apple") // returns TRUE
    =OR(A1="orange",A1="pear") // returns FALSE

For this problem, instead of an "equals to" test, we need a "begins with" test." For that, we can use the [LEFT function](https://exceljet.net/functions/left-function)
, which is designed to extract text from the left side of a text string. For example:

    =LEFT("apple",1) // returns "a"
    =LEFT("apple",2) // returns "ap"
    =LEFT("apple",3) // returns "app"

Putting these two functions together, we can test the value in cell A1 to see if it begins with "x", "y", or "z" like this:

    =OR(LEFT(A1)="x",LEFT(A1)="y",LEFT(A1)="z")

If cell A1 contains "dog", the formula above will return FALSE:

    =OR(FALSE,FALSE,FALSE) // returns FALSE

If cell A1 contains "zebra", the formula above will return TRUE:

    =OR(FALSE,FALSE,TRUE) // returns TRUE

While this formula works well, it can be cumbersome to enter more values to test. One way to simplify the formula is to use an [array constant](https://exceljet.net/glossary/array-constant)
 with a single expression like this:

    =IF(OR(LEFT(A1)={"x","y","z"}),"x","")

An array constant is a structure that holds multiple values. It works like a range in Excel, except the values in an array constant are hard coded. Because the result from LEFT is compared to three separate values in the array constant, the expression returns three separate results and the OR function evaluates these results as before. Putting this all altogether, we can use the formula above inside the IF function as the logical test. This is the approach used in the example shown, where the formula in cell D5 is:

    =IF(OR(LEFT(B5,1)={"x","y","z"}),"x","")

In cell D5, the formula evaluates like this:

    =IF(OR(LEFT(B5,1)={"x","y","z"}),"x","")
    =IF(OR({FALSE,FALSE,TRUE}),"x","")
    =IF(TRUE,"x","")
    ="x"

In cell D6, the formula evaluates like this:

    =IF(OR(LEFT(B6,1)={"x","y","z"}),"x","")
    =IF(OR({FALSE,FALSE,FALSE}),"x","")
    =IF(FALSE,"x","")
    =""

_Notes: (1) The above formula uses an array constant to hold three hard-coded values to test. However, you can also use a normal range on the worksheet. Using a range makes it easy to provide more values to test, and to change these values at any time. (2) In this example, we are testing the first character only, so the num\_chars argument in LEFT is 1. To test more than one character, adjust num\_chars as needed._

### COUNTIF function

Another way to solve this problem is with the COUNTIF function. [COUNTIF](https://exceljet.net/functions/countif-function)
 counts cells in a range that meet a given condition (criteria). If no cells meet the criteria, COUNTIF returns zero. The generic syntax for COUNTIF is:

    =COUNTIF(range,criteria)

For example, to count cells that equal "apple", we can use COUNTIF like this:

    =COUNTIF(range,"apple")

COUNTIF supports [wildcards](https://exceljet.net/glossary/wildcard)
. To count cells that begin with "a", we can use a formula like this:

    =COUNTIF(range,"a*")

The asterisk (\*) is a wildcard that means zero or more characters, so the meaning here is: _begins with "a"_. In the example shown, the formula in cell D5 is:

    =IF(SUM(COUNTIF(B5,{"x*","y*","z*"})),"x","")

Working from the inside out, the core of this formula is COUNTIF, which is configured to count three separate values using wildcards and the [array constant](https://exceljet.net/glossary/array-constant)
 {"x\*","y\*","z\*"} for criteria:

    COUNTIF(B5,{"x*","y*","z*"})
    

The values in the criteria are supplied in an "array constant", a hard-coded list of items with curly braces on either side. When COUNTIF receives the criteria in an array constant, it will return multiple counts, one count per item. For cell B5, COUNTIF returns the array {0,0,1}. The first count (0) is the count for cells that begin with "x". The second count (0) is for cells that begin with "y". The third count (1) is for cells that begin with "z". Note that because we only give COUNTIF a one-cell range, it can return only one of two values: 1 or 0. Here are the result for the first 4 cells:

    =COUNTIF(B5,{"x*","y*","z*"}) // returns {0,0,1}
    =COUNTIF(B6,{"x*","y*","z*"}) // returns {0,0,0}
    =COUNTIF(B7,{"x*","y*","z*"}) // returns {0,0,0}
    =COUNTIF(B8,{"x*","y*","z*"}) // returns {1,0,0}

Because we are testing for 3 criteria with OR logic, we only care if _any_ result is not zero. To check this, we add up all items using the SUM function. Excel will automatically evaluate any number as TRUE and zero (0) as FALSE. In cell B5, the formula evaluates like this:

    =IF(SUM({0,0,1}),"x","")
    =IF(1,"x","")
    ="x"

In other words, IF will return "x" whenever the result from SUM is _not zero_. However, if the result from SUM _is zero_, IF will return an empty string (""). In cell D6, the formula evaluates like this:

    =IF(SUM({0,0,0}),"x","")
    =IF(0,"x","")
    =""

Note that this example uses 3 criteria: begins with x, y, or z. As with the LEFT formula above, you can add more values to test and the formula will continue to work. 

### TRUE or FALSE result

Both formulas above use the IF function to return "x" if a match is found and an empty string ("") if a match is not found. If you only need a TRUE or FALSE result the IF function is not required:

    OR(LEFT(B5,1)={"x","y","z"}) // returns TRUE or FALSE

For the COUNTIF version, the logic needs to be adjusted a bit:

    SUM(COUNTIF(B5,{"x*","y*","z*"}))>0 // returns TRUE or FALSE

Here we check if the result from SUM is greater than zero in order to force a TRUE or FALSE result.

### Notes

1.  If you are testing many values, you can use a _range_ instead of an _array constant_ to provide values to check. In Excel 2019 and earlier, using a range will make the formula an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
     that must be entered with control + shift + enter. In the current version of Excel, no special handling is required. 
2.  The COUNTIF function [will accept ranges only](https://exceljet.net/articles/excels-racon-functions)
     for the _range_ argument; you can't feed COUNTIF an _array_ that comes from another formula. This can be a problem when working with [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    , where it is more common to pass arrays from one formula to another. The LEFT formula option does not have this limitation.

Related formulas
----------------

[![Excel formula: If cell is this OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20is%20this%20or%20that.png "Excel formula: If cell is this OR that")](https://exceljet.net/formulas/if-cell-is-this-or-that)

### [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)

In the example shown, we want to mark or "flag" records where the color is red OR green. In other words, we want to check the color in column B, and then leave a marker (x) if we find the word "red" or "green". In D6, the formula is: =IF(OR(B6="red",B6="green"),"x","") This is an example of nesting...

[![Excel formula: If cell is x or y and z](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_x_or_y_and_z.png "Excel formula: If cell is x or y and z")](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z)

### [If cell is x or y and z](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z)

The goal is to identify records where the color is "Red" or "Green" and the quantity is greater than 10. If a row meets all conditions, the formula should return "x". If any condition is not true, the formula should return an empty string (""). This problem can be solved with the IF function...

[![Excel formula: If cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains.png "Excel formula: If cell contains")](https://exceljet.net/formulas/if-cell-contains)

### [If cell contains](https://exceljet.net/formulas/if-cell-contains)

The goal is to do something if a cell contains a given substring. For example, in the worksheet above, a formula returns "x" when a cell contains "abc". If you are familiar with Excel, you will probably think first of the IF function. However, one limitation of IF is that it does not support...

[![Excel formula: If cell is not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_not_blank_0.png "Excel formula: If cell is not blank")](https://exceljet.net/formulas/if-cell-is-not-blank)

### [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)

The goal is to create a formula that returns "Done" in column E when a cell in column D is not blank (i.e., contains a value). In the worksheet shown, column D records the date a task is completed. If column D contains a date (i.e. is not empty), we can assume the task is complete. This problem can...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: If cell contains this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains_this_or_that.png "Excel formula: If cell contains this or that")](https://exceljet.net/formulas/if-cell-contains-this-or-that)

### [If cell contains this or that](https://exceljet.net/formulas/if-cell-contains-this-or-that)

The goal is to do something if a cell contains one substring or another. Most users will think first of the IF function. However, one problem with IF is that it does not support wildcards like "?" and "\*". This means we can't use IF by itself to test for a substring like "abc" or "xyz" that might...

Related functions
-----------------

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

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
    
*   [If cell is x or y and z](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z)
    
*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    
*   [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [If cell contains this or that](https://exceljet.net/formulas/if-cell-contains-this-or-that)
    

### Functions

*   [OR Function](https://exceljet.net/functions/or-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

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