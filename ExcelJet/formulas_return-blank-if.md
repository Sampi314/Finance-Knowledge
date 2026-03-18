# Return blank if - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/return-blank-if

---

[Skip to main content](https://exceljet.net/formulas/return-blank-if#main-content)

[](https://exceljet.net/formulas/return-blank-if#)

*   [Previous](https://exceljet.net/formulas/only-calculate-if-not-blank)
    
*   [Next](https://exceljet.net/formulas/categorize-text-with-keywords)
    

[If](https://exceljet.net/formulas#If)

Return blank if
===============

by Dave Bruns · Updated 24 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

[COUNTBLANK](https://exceljet.net/functions/countblank-function)

![Excel formula: Return blank if](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/return_blank_if.png "Excel formula: Return blank if")

Summary
-------

To return a blank result (i.e. display nothing) based on a conditional test, you can use the [IF function](https://exceljet.net/functions/if-function)
 with an [empty string](https://exceljet.net/glossary/empty-string)
 (""). In the example shown, the formula in E5 is:

    =IF(B5="a",C5,"")
    

As the formula is copied down, the IF function returns the value in column C when the value in column B is "A". Otherwise, IF returns an empty string ("") which looks like an empty cell in Excel.

_Note: Excel is not case-sensitive by default, so B5="a" and B5="A" will return the same result._

Generic formula
---------------

    =IF(A1="a",B1,"")

Explanation 
------------

The goal is to display a blank cell based on a specific condition. In the worksheet shown, we want to return the value from column C, but only when the value in column B is "A". If the value in column B is anything else, we want to display nothing. The easiest way to solve this problem is with the IF function and an empty string ("").

### IF function

The [IF function](https://exceljet.net/functions/if-function)
 runs a logical test and returns one value for a TRUE result, and another value for a FALSE result. For example, if cell A1 contains "Red", then:

    =IF(A1="red",TRUE) // returns TRUE
    =IF(A1="blue",TRUE) // returns FALSE

Notice the IF function automatically returns FALSE even though no value is provided for a false result. It is important to understand that the IF function is not case-sensitive. If cell A1 contains "Red", then:

    =IF(A1="red",TRUE) // returns TRUE
    =IF(A1="RED",TRUE) // returns TRUE
    =IF(A1="Red",TRUE) // returns TRUE

Notice that text values inside IF must be enclosed in double quotes (""). However, numeric values _should not_ appear in quotes. For example, if cell A1 contains 100, then _do not_ use quotes to test for 100:

    =IF(A1=100,TRUE) // returns TRUE

Enclosing a number in quotes ("100") causes Excel to interpret the value _as text_, which will cause the logical test to fail:

    =IF(A1="100",TRUE) // returns FALSE

For more details about IF, see: [How to use the IF function](https://exceljet.net/functions/if-function)
.

### Empty strings in Excel

When the goal is to display nothing with a formula in Excel use two double quotes like this "". This is called an [empty string](https://exceljet.net/glossary/empty-string)
 ("") and it will display like an empty or blank cell on the worksheet. Note if you type "" directly into a cell in Excel, you _will see_ the double quote characters. However, when you enter the quotes as a formula like this:

    =""
    

You won't see anything, the cell will look empty.

### IF with empty string

In the example shown, the formula in E5 is:

    =IF(B5="a",C5,"") // returns 82

In this formula, the _logical\_test_ is B5="a", the _value\_if\_true_ is C5, and the _value\_if\_false_ is an empty string (""). As the formula is copied down, the IF function returns the value in column C when the value in column B is "A". If B5 contains _any other value_, IF returns an empty string ("") which looks like an empty cell in Excel. Although we are using a lowercase "a", an uppercase "A" produce the same result:

    =IF(B5="A",C5,"") // returns 82

### Testing for blank cells

There are many ways to check for blank cells in Excel, see [this article for several options](https://exceljet.net/formulas/only-calculate-if-not-blank)
. If you need to check the result of a formula that returns an empty string (""), be aware that the [ISBLANK function](https://exceljet.net/functions/isblank-function)
 will return FALSE when checking a formula that returns "" as a final result. In other words, while you would expect ISBLANK to return TRUE, it actually returns FALSE.  For example, if cell A1 contains a formula that returns an empty string, then:

    =ISBLANK(A1) // returns FALSE
    

One workaround is to use the COUNTBLANK function instead like this:

    =COUNTBLANK(A1) // returns 1
    =COUNTBLANK(A1)>0 // returns TRUE
    

You can use COUNTBLANK inside the IF function like this:

    =IF(COUNTBLANK(A1)>0,true_result,false_result)
    

For more details on COUNTBLANK, see: [How to use the COUNTBLANK function](https://exceljet.net/functions/countblank-function)
. 

Related formulas
----------------

[![Excel formula: If cell is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_blank.png "Excel formula: If cell is blank")](https://exceljet.net/formulas/if-cell-is-blank)

### [If cell is blank](https://exceljet.net/formulas/if-cell-is-blank)

In the example worksheet, column D contains a date when a task is completed. If the task is not yet complete, the cell in column D will be empty (blank). In column E, the goal is to display the word "Open" when there is no date in column D. If there is a date in column D, the formula in column E...

[![Excel formula: If cell is not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_not_blank_0.png "Excel formula: If cell is not blank")](https://exceljet.net/formulas/if-cell-is-not-blank)

### [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)

The goal is to create a formula that returns "Done" in column E when a cell in column D is not blank (i.e., contains a value). In the worksheet shown, column D records the date a task is completed. If column D contains a date (i.e. is not empty), we can assume the task is complete. This problem can...

[![Excel formula: If cell is greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_greater_than.png "Excel formula: If cell is greater than")](https://exceljet.net/formulas/if-cell-is-greater-than)

### [If cell is greater than](https://exceljet.net/formulas/if-cell-is-greater-than)

The aim is to mark records with an "x" if a score is greater than 80 and leave the cell blank if the score is less than 80. This can be achieved using the IF function in Excel. IF function The IF function runs a logical test and returns one value for a TRUE result, and another value for a FALSE...

[![Excel formula: Only calculate if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20not%20blank%20then%20calculate2.png "Excel formula: Only calculate if not blank")](https://exceljet.net/formulas/only-calculate-if-not-blank)

### [Only calculate if not blank](https://exceljet.net/formulas/only-calculate-if-not-blank)

The goal is to verify the input of all required values before calculating a result. In the worksheet shown, the SUM function is used as an example only. You can use the same approach with any formula to prevent calculation until all required values are available. The logic can be adjusted in many...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

[![Excel COUNTBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20countblank%20function.png "Excel COUNTBLANK function")](https://exceljet.net/functions/countblank-function)

### [COUNTBLANK Function](https://exceljet.net/functions/countblank-function)

The Excel COUNTBLANK function returns a count of empty cells in a [range](https://exceljet.net/glossary/range)
. Cells that contain text, numbers, errors, spaces, etc. are _not_ counted. Formulas that return empty strings ("") _are_ counted as blank.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [If cell is blank](https://exceljet.net/formulas/if-cell-is-blank)
    
*   [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)
    
*   [If cell is greater than](https://exceljet.net/formulas/if-cell-is-greater-than)
    
*   [Only calculate if not blank](https://exceljet.net/formulas/only-calculate-if-not-blank)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [COUNTBLANK Function](https://exceljet.net/functions/countblank-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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