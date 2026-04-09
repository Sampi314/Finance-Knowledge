# If cell is not blank - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-cell-is-not-blank

---

[Skip to main content](https://exceljet.net/formulas/if-cell-is-not-blank#main-content)

[](https://exceljet.net/formulas/if-cell-is-not-blank#)

*   [Previous](https://exceljet.net/formulas/if-cell-is-greater-than)
    
*   [Next](https://exceljet.net/formulas/if-cell-is-this-or-that)
    

[If](https://exceljet.net/formulas#If)

If cell is not blank
====================

by Dave Bruns · Updated 27 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

[NOT](https://exceljet.net/functions/not-function)

![Excel formula: If cell is not blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_cell_is_not_blank_0.png "Excel formula: If cell is not blank")

Summary
-------

To test if a cell is not blank (i.e. has content), you can use a formula based on the [IF function](https://exceljet.net/videos/the-if-function)
. In the example shown, the formula in cell E5 is:

    =IF(D5<>"","Done","")
    

As the formula is copied down it returns "Done" when a cell in column D _is not_ blank and an [empty string](https://exceljet.net/glossary/empty-string)
 ("") if the cell _is_ blank.

Generic formula
---------------

    =IF(A1<>"","not blank","blank")

Explanation 
------------

The goal is to create a formula that returns "Done" in column E when a cell in column D is not blank (i.e., contains a value). In the worksheet shown, column D records the date a task is completed. If column D contains a date (i.e. is not empty), we can assume the task is complete. This problem can be solved with the IF function alone or with the IF function and the ISBLANK function. It can also be solved with the LEN function. All three approaches are explained below.

### IF function

The [IF function](https://exceljet.net/functions/if-function)
 runs a logical test and returns one value for a TRUE result, and another value for a FALSE result. Use IF to test for a blank cell like this:

    =IF(A1="",TRUE) // IF A1 is blank
    =IF(A1<>"",TRUE) // IF A1 is not blank

In the first example, we test if A1 is empty with ="". In the second example, the <> symbol is a [logical operator](https://exceljet.net/glossary/logical-operators)
 that means "not equal to", so the expression A1<>"" means A1 is "not empty". In the worksheet shown, we use the second concept in cell E5 like this:

    =IF(D5<>"","Done","")
    

If D5 is "not empty", the result is "Done". If D5 is empty, IF returns an empty string ("") which displays as nothing in Excel. As the formula is copied down, it returns "Done" only for cells in column D that contain a value. To display both "Done" and "Not done", you can adjust the formula like this:

    =IF(D5<>"","Done","Not done")
    

### ISBLANK function

Another way to solve this problem is with the [ISBLANK function](https://exceljet.net/functions/isblank-function)
. The ISBLANK function returns TRUE when a cell is empty and FALSE if not. To use ISBLANK only, you can rewrite the formula like this:

    =IF(ISBLANK(D5),"","Done")
    

Notice the TRUE and FALSE results have been reversed. The logic now is _if cell D5 is blank_. To maintain the original logic, you can [nest](https://exceljet.net/glossary/nesting)
 ISBLANK inside the [NOT function](https://exceljet.net/functions/not-function)
 like this:

    =IF(NOT(ISBLANK(D5)),"Done","")
    

The NOT function reverses the output from ISBLANK. 

### LEN function

One problem with testing for blank cells in Excel is that ISBLANK(A1) or A1="" will return FALSE if A1 contains a formula that returns an empty string. In other words, if a formula returns an empty string in a cell, Excel interprets the cell as "not empty" even though it looks empty. To work around this problem, you can use the [LEN function](https://exceljet.net/functions/len-function)
 to test for characters in a cell like this:

    =IF(LEN(A1)<>0,"Open","")

This is a more literal formula. We are not asking Excel if A1 is blank, we are literally counting the characters in A1. The LEN function will return a non-zero number only when a cell contains actual characters. Using the LEN function this way works for cells containing formulas as well as cells without formulas.

###  Conditional formatting

Another way to highlight tasks based on a cell that is not blank is to use [conditional formatting](https://exceljet.net/articles/conditional-formatting-with-formulas)
. In the screen below, this formula is used to highlight rows that do not contain a completion date:

    =$D5<>""

![Conditional formatting to highlight cells based on a cell that is not blank](https://exceljet.net/sites/default/files/images/formulas/inline/if_cell_is_not_blank_with_conditional_formatting.png "Conditional formatting to highlight cells based on a cell that is not blank")

This is an example of applying conditional formatting with a formula. When a date is entered in column D, the formatting will be applied. [More examples here](https://exceljet.net/conditional-formatting-formulas)
.

Related formulas
----------------

[![Excel formula: If cell is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_blank.png "Excel formula: If cell is blank")](https://exceljet.net/formulas/if-cell-is-blank)

### [If cell is blank](https://exceljet.net/formulas/if-cell-is-blank)

In the example worksheet, column D contains a date when a task is completed. If the task is not yet complete, the cell in column D will be empty (blank). In column E, the goal is to display the word "Open" when there is no date in column D. If there is a date in column D, the formula in column E...

[![Excel formula: If cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains.png "Excel formula: If cell contains")](https://exceljet.net/formulas/if-cell-contains)

### [If cell contains](https://exceljet.net/formulas/if-cell-contains)

The goal is to do something if a cell contains a given substring. For example, in the worksheet above, a formula returns "x" when a cell contains "abc". If you are familiar with Excel, you will probably think first of the IF function. However, one limitation of IF is that it does not support...

[![Excel formula: Return blank if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/return_blank_if.png "Excel formula: Return blank if")](https://exceljet.net/formulas/return-blank-if)

### [Return blank if](https://exceljet.net/formulas/return-blank-if)

The goal is to display a blank cell based on a specific condition. In the worksheet shown, we want to return the value from column C, but only when the value in column B is "A". If the value in column B is anything else, we want to display nothing. The easiest way to solve this problem is with the...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

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
    
*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    
*   [Return blank if](https://exceljet.net/formulas/return-blank-if)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

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