# If not blank multiple cells - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-not-blank-multiple-cells

---

[Skip to main content](https://exceljet.net/formulas/if-not-blank-multiple-cells#main-content)

[](https://exceljet.net/formulas/if-not-blank-multiple-cells#)

*   [Previous](https://exceljet.net/formulas/if-else)
    
*   [Next](https://exceljet.net/formulas/if-not-this-or-that)
    

[If](https://exceljet.net/formulas#If)

If not blank multiple cells
===========================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

[NOT](https://exceljet.net/functions/not-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

![Excel formula: If not blank multiple cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_not_blank_multiple_cells.png "Excel formula: If not blank multiple cells")

Summary
-------

To test multiple cells, and return the value from the first non-blank cell, you can use a formula based on the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the formula in cell G5 is:

    =IF(B5<>"",B5,IF(C5<>"",C5,IF(D5<>"",D5,IF(E5<>"",E5,"no value"))))
    

The result is the first non-blank cell: B5, C5, D5, or E5, respectively. When all cells are blank, the formula returns "no value". The value returned when all cells are blank can be adjusted as desired.

_Feeling underwhelmed by the manual complexity of this formula? See below for a more elegant solution based on the XLOOKUP function. -Dave_

Generic formula
---------------

    =IF(A1<>"",A1,IF(B1<>"",B1,IF(C1<>"",C1,IF(D1<>"",D1,"no value"))))

Explanation 
------------

The goal is to return the first non-blank value in each row from columns B:E, moving left to right. One way to solve this problem is with a series of nested IF statements. Since all cells are contiguous (connected) another way to get the first value is with the XLOOKUP function. Both approaches are explained below.

### Nested IF solution

In the worksheet shown, the formula in cell G5 is:

    =IF(B5<>"",B5,IF(C5<>"",C5,IF(D5<>"",D5,IF(E5<>"",E5,"no value"))))

In Excel, empty double quotes ("") mean an [empty string](https://exceljet.net/glossary/empty-string)
. The <> symbol is a [logical operator](https://exceljet.net/glossary/logical-operators)
 that means "not equal to", so the following expression means "A1 is not empty":

    =B5<>"" // B5 is not empty
    

The overall structure of this formula is what is called a "[nested IF formula](https://exceljet.net/articles/nested-ifs)
". Each IF statement checks a cell to see if a particular cell is not empty. If a cell is _not empty_, the IF returns the value from that cell. If the cell _is empty_, the IF statement hands off processing to the following IF function. The flow of a nested IF is somewhat easier to understand if we add line breaks to the formula to separate each IF function like this:

    =
    IF(B5<>"",B5,
    IF(C5<>"",C5,
    IF(D5<>"",D5,
    IF(E5<>"",E5,
    "no value"))))
    

Video: [How to make a nested if formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

### With ISBLANK

It is also possible to use the [ISBLANK function](https://exceljet.net/functions/isblank-function)
, which returns TRUE when a cell is blank:

    =ISBLANK(A1) // A1 is blank
    

The behavior can be "reversed" by nesting the ISBLANK function inside the [NOT function](https://exceljet.net/functions/not-function)
:

    =NOT(ISBLANK(A1)) // A1 is not blank
    

The original formula above can be re-written to use ISBLANK as follows:

    =IF(NOT(ISBLANK(B5)),B5,IF(NOT(ISBLANK(C5)),C5,IF(NOT(ISBLANK(D5)),D5,IF(NOT(ISBLANK(E5)),E5,"no value"))))
    

### XLOOKUP solution

Another way to solve this problem is with the XLOOKUP formula like this:

    =XLOOKUP(TRUE,ISNUMBER(B5:E5),B5:E5)

We can use XLOOKUP in this case because the four cells in B5:E5 are together, so they can be provided as a single range. The ISNUMBER function checks the range and returns an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values like this:

    {TRUE,TRUE,TRUE,TRUE}

XLOOKUP matches the first TRUE in the array and returns the corresponding value in B5:E5. Note that this approach only works because all the cells being checked are in a contiguous range. You can read [more about XLOOKUP here](https://exceljet.net/functions/xlookup-function)
.

Related formulas
----------------

[![Excel formula: Get first non-blank value in a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_non-blank_value_in_a_list.png "Excel formula: Get first non-blank value in a list")](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

### [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

The gist of this problem is that we want to get the first non-blank cell, but we don't have a direct way to do that in Excel. The easiest way to solve this problem is with the XLOOKUP function. XLOOKUP function The XLOOKUP function is a modern upgrade to the VLOOKUP function. XLOOKUP is very...

[![Excel formula: If cell is not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_not_blank_0.png "Excel formula: If cell is not blank")](https://exceljet.net/formulas/if-cell-is-not-blank)

### [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)

The goal is to create a formula that returns "Done" in column E when a cell in column D is not blank (i.e., contains a value). In the worksheet shown, column D records the date a task is completed. If column D contains a date (i.e. is not empty), we can assume the task is complete. This problem can...

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

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20make%20a%20nested%20IF%20formula%20easier%20to%20read.png)](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

### [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

In this video we're going to look at how to make a nested IF formula more readable by adding line breaks. Here I have a worksheet that calculates sales commissions based on the commission structure shown in the table. For example, we can see that King sold $124,500 and gets a commission of 5%,...

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
    
*   [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)
    
*   [If cell is blank](https://exceljet.net/formulas/if-cell-is-blank)
    
*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    
*   [Return blank if](https://exceljet.net/formulas/return-blank-if)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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