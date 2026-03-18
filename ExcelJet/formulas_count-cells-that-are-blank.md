# Count cells that are blank - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-are-blank

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-are-blank#main-content)

[](https://exceljet.net/formulas/count-cells-that-are-blank#)

*   [Previous](https://exceljet.net/formulas/count-cells-over-n-characters)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-are-not-blank)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that are blank
==========================

by Dave Bruns · Updated 19 Mar 2025

Related functions 
------------------

[COUNTBLANK](https://exceljet.net/functions/countblank-function)

[COUNTA](https://exceljet.net/functions/counta-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count cells that are blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20are%20blank_0.png "Excel formula: Count cells that are blank")

Summary
-------

To count the number of cells that are blank (i.e. empty), you can use the [COUNTBLANK function](https://exceljet.net/functions/countblank-function)
. In the example shown, the formula in cell E5 is:

    =COUNTBLANK(C5:C16)
    

Because there are three empty cells in the range C5:C16, COUNTBLANK returns 3.

Generic formula
---------------

    =COUNTBLANK(range)

Explanation 
------------

In this example, the goal is to count cells in a [range](https://exceljet.net/glossary/range)
 that are blank. Counting blank cells in Excel can be tricky because cells can _look_ blank even when they are not actually empty. The article below explains three different approaches.

### COUNTBLANK function

The simplest way to count empty cells in a range is to use the [COUNTBLANK function](https://exceljet.net/functions/countblank-function)
. In the example shown, the formula in F6 is:

    =COUNTBLANK(C5:C16) // returns 3
    

Because there are three empty cells in the range C5:C16 , COUNTBLANK returns 3. COUNTBLANK is fully automatic, so there is nothing to configure.

### COUNTIFS function

You can also use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 to count empty cells by passing in an [empty string](https://exceljet.net/glossary/empty-string)
 ("") as criteria like this:

    =COUNTIFS(C5:C16,"") // returns 3
    

COUNTIF returns the same result as COUNTBLANK: 3.

Because [COUNTIFS can handle multiple criteria](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)
, you can easily extend this formula to count empty cells in Group "A" like this:

    =COUNTIFS(B5:B16,"A",C5:C16,"") // returns 2
    

The first _range/criteria_ pair selects cells that are in Group A only. The second _range/criteria_ pair selects empty cells. The result from COUNTIFS is 2, since there are two empty cells in Group A. You can swap the order of the _range/criteria_ pairs with the same result.

See also: [50 examples of formula criteria](https://exceljet.net/articles/how-to-use-formula-criteria)
.

### SUMPRODUCT function

Another way to count blank cells is with the SUMPRODUCT function. You can use the SUMPRODUCT function to count empty cells like this:

    =SUMPRODUCT(--(C5:C16=""))
    

The expression C5:C16="" returns an [array](https://exceljet.net/glossary/array)
 that contains 12 TRUE and FALSE values, and the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) converts the TRUE and FALSE values to 1s and 0s:

    {0;0;1;0;0;1;0;0;0;1;0;0} // returns 3
    

The result is 3 as before. 

You can extend the logic used in SUMPRODUCT with other functions as needed. For example, the variant below uses the [LEN function](https://exceljet.net/functions/len-function)
 to count cells that have a length equal to zero:

    =SUMPRODUCT(--(LEN(C5:C16)=0)) // returns 3
    

You can adapt this formula to count empty cells in Group A like this:

    =SUMPRODUCT((LEN(C5:C16)=0)*(B5:B16="A"))
    

This is an example of using [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
 in a formula. The double negative (--) is no longer needed in this case because the math operation of multiplying the two arrays together automatically converts the TRUE and FALSE values to 1s and 0s:

    =SUMPRODUCT({0;0;1;0;0;1;0;0;0;0;0;0}) // returns 2
    

The final result is 2, since there are two empty cells in Group A.

_Note: one reason the SUMPRODUCT syntax above is useful is because you can drop the same logical expressions into a newer function like the_ [_FILTER function_](https://exceljet.net/functions/filter-function)
 _to extract cells that meet the same criteria. The SUMPRODUCT function is more versatile than_ [_RACON functions_](https://exceljet.net/articles/excels-racon-functions)
 _like COUNTIFS, SUMIFS, etc. and you will often see it used in formulas that solve tricky problems. You can read_ [_more about SUMPRODUCT here_](https://exceljet.net/functions/sumproduct-function)
_._ 

Related formulas
----------------

[![Excel formula: All cells in range are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all_cells_in_range_are_blank.png "Excel formula: All cells in range are blank")](https://exceljet.net/formulas/all-cells-in-range-are-blank)

### [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)

When working with Excel, there are times when you need to determine if a range of cells is empty. This can be useful in various scenarios, such as data validation, error checking, or report preparation. In this article, we'll explore a couple of formulas that can help you check if all cells in a...

[![Excel formula: Count cells that are not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20are%20not%20blank.png "Excel formula: Count cells that are not blank")](https://exceljet.net/formulas/count-cells-that-are-not-blank)

### [Count cells that are not blank](https://exceljet.net/formulas/count-cells-that-are-not-blank)

In this example, the goal is to count cells in a range that are not blank (i.e. not empty). There are several ways to go about this task, depending on your needs. The article below explains different approaches. COUNTA function While the COUNT function only counts numbers, the COUNTA function...

[![Excel formula: Sum if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_not_blank.png "Excel formula: Sum if not blank")](https://exceljet.net/formulas/sum-if-not-blank)

### [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)

In this example, the goal is to sum the Amounts in C5:C16 when the Lead in D5:D16 is not blank (i.e., not empty). A good way to solve this problem is to use the SUMIFS function . However, you can also use the SUMPRODUCT function or the FILTER function , as explained below. Because SUMPRODUCT and...

[![Excel formula: If cell is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_blank.png "Excel formula: If cell is blank")](https://exceljet.net/formulas/if-cell-is-blank)

### [If cell is blank](https://exceljet.net/formulas/if-cell-is-blank)

In the example worksheet, column D contains a date when a task is completed. If the task is not yet complete, the cell in column D will be empty (blank). In column E, the goal is to display the word "Open" when there is no date in column D. If there is a date in column D, the formula in column E...

Related functions
-----------------

[![Excel COUNTBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20countblank%20function.png "Excel COUNTBLANK function")](https://exceljet.net/functions/countblank-function)

### [COUNTBLANK Function](https://exceljet.net/functions/countblank-function)

The Excel COUNTBLANK function returns a count of empty cells in a [range](https://exceljet.net/glossary/range)
. Cells that contain text, numbers, errors, spaces, etc. are _not_ counted. Formulas that return empty strings ("") _are_ counted as blank.

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)
    
*   [Count cells that are not blank](https://exceljet.net/formulas/count-cells-that-are-not-blank)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [If cell is blank](https://exceljet.net/formulas/if-cell-is-blank)
    

### Functions

*   [COUNTBLANK Function](https://exceljet.net/functions/countblank-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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