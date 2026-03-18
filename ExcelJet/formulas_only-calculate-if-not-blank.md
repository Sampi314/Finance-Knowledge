# Only calculate if not blank - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/only-calculate-if-not-blank

---

[Skip to main content](https://exceljet.net/formulas/only-calculate-if-not-blank#main-content)

[](https://exceljet.net/formulas/only-calculate-if-not-blank#)

*   [Previous](https://exceljet.net/formulas/nested-if-with-multiple-and)
    
*   [Next](https://exceljet.net/formulas/return-blank-if)
    

[If](https://exceljet.net/formulas#If)

Only calculate if not blank
===========================

by Dave Bruns · Updated 30 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[COUNT](https://exceljet.net/functions/count-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

[COUNTBLANK](https://exceljet.net/functions/countblank-function)

[AND](https://exceljet.net/functions/and-function)

[OR](https://exceljet.net/functions/or-function)

![Excel formula: Only calculate if not blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/If%20not%20blank%20then%20calculate2.png "Excel formula: Only calculate if not blank")

Summary
-------

To keep a formula from calculating when certain cells are blank, you can use the [IF function](https://exceljet.net/functions/if-function)
 with a suitable logical test. In the example shown, the formula in E5 is:

    =IF(COUNT(C5:C7)=3,SUM(C5:C7),"")
    

Since cell C7 is empty, the formula displays no result. In the screen below, C7 contains a number and the sum is displayed:

![Same formula with calculation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/If%20not%20blank%20then%20calculate%20with%20calculation.png?itok=Z8A_e5Jc "Same formula with calculation")

Generic formula
---------------

    =IF(logical_test,formula(),"")

Explanation 
------------

The goal is to verify the input of all required values before calculating a result. In the worksheet shown, the SUM function is used as an example only. You can use the same approach with any formula to prevent calculation until all required values are available. The logic can be adjusted in many ways to suit the situation. Below are several examples of how you can approach this problem. The best solution depends on the requirements of the project and your personal preference.

### IF + COUNT

In the example shown, we are using the IF function together with the [COUNT function](https://exceljet.net/functions/count-function)
:

    =IF(COUNT(C5:C7)=3,SUM(C5:C7),"")
    

_Translation: if the count of numbers in C5:C7 is 3, sum the range C5:C7. Otherwise, display nothing._

The logical test is based on the COUNT function, which counts _numeric_ values:

    COUNT(C5:C7)=3 // returns TRUE or FALSE
    

This test will return FALSE until the range C5:C7 contains three numbers. This will cause the IF function to return the _value\_if\_false_, which has been supplied as an [empty string](https://exceljet.net/glossary/empty-string)
 (""). In Excel, an empty string will look like an empty cell. Since C7 has no value in the original worksheet, the formula displays no result. Once the range C5:C7 contains three numbers, the test will return TRUE and IF will run the SUM function, which will return the sum of C5:C7 as a final result.

There are many ways to check for blank cells, and several other options are explained below.

### IF + COUNTBLANK

The [COUNTBLANK function](https://exceljet.net/functions/countblank-function)
 counts empty cells in a _range_, so we can write a slightly more compact formula like this:

    =IF(COUNTBLANK(C5:C7),"",SUM(C5:C7))
    

If COUNTBLANK returns any non-zero number, the IF function will evaluate the number as TRUE, and return an empty string (""). If COUNTBLANK returns zero, IF will evaluate zero as FALSE and return the result from the SUM function.

### IF + ISBLANK

Another approach is to use the [ISBLANK function.](https://exceljet.net/functions/isblank-function)
 ISBLANK returns TRUE when a cell reference is empty. ISBLANK was originally designed to test one cell only, but you can use ISBLANK three times inside the [OR function](https://exceljet.net/functions/or-function)
 together like this:

    =IF(OR(ISBLANK(C5),ISBLANK(C6),ISBLANK(C7)),"",SUM(C5:C7))
    

OR will return TRUE if any supplied value is TRUE. In other words, the OR function will return TRUE if any of the ISBLANK functions return TRUE. Alternatively, can use a formula like this:

    =IF(OR(ISBLANK(C5:C7),"",SUM(C5:C7))
    

_Note: this is an [array formula](https://exceljet.net/articles/what-is-an-array-formula)
 and must be entered with control + shift + enter in Excel 2019 and older. In the current version of Excel, it will work fine as-is._

In this formula, we pass a range into ISBLANK and ISBLANK returns an [array](https://exceljet.net/glossary/array)
 that contains 3 results. If any value in the array is TRUE, the OR function returns TRUE, causing IF to return an empty string (""). If all values in the array are FALSE (i.e. all three cells contain values), OR returns FALSE, and IF returns the result from SUM:

    SUM(C5:C7)
    

### IF with logical operators

Another option is to use standard [logical operators](https://exceljet.net/glossary/logical-operators)
 like ="" and <>"" to test for empty and non-empty cells. To test for any empty cells, use a formula like this:

    =IF(OR(C5="",C6="",C7=""),"",SUM(C5:C7))
    

To test for non-empty cells use <>"" inside the [AND function](https://exceljet.net/functions/and-function)
 like this:

    =IF(AND(C5<>"",C6<>"",C7<>""),SUM(C5:C7),"")
    

In this formula, notice the SUM function has been moved to the _value\_if\_true_ argument, and will only run if all 3 cells are _not empty_.

### IF + COUNTA

Finally, you also use the COUNTA function to test for non-empty cells like this:

    =IF(COUNTA(C5:C7)=3,SUM(C5:C7),"")
    

While the [COUNT function](https://exceljet.net/functions/count-function)
 only counts numeric values, the [COUNTA function](https://exceljet.net/functions/counta-function)
 counts any kind of value (i.e. numbers or text). As long as the range C5:C5 contains three values (numbers or text), the result will be TRUE and the SUM function will run. This doesn't really make sense for the example shown (which requires numeric input) but it can be used in other situations.

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

[![Excel formula: If cell is not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_not_blank_0.png "Excel formula: If cell is not blank")](https://exceljet.net/formulas/if-cell-is-not-blank)

### [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)

The goal is to create a formula that returns "Done" in column E when a cell in column D is not blank (i.e., contains a value). In the worksheet shown, column D records the date a task is completed. If column D contains a date (i.e. is not empty), we can assume the task is complete. This problem can...

[![Excel formula: All cells in range are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all_cells_in_range_are_blank.png "Excel formula: All cells in range are blank")](https://exceljet.net/formulas/all-cells-in-range-are-blank)

### [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)

When working with Excel, there are times when you need to determine if a range of cells is empty. This can be useful in various scenarios, such as data validation, error checking, or report preparation. In this article, we'll explore a couple of formulas that can help you check if all cells in a...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

[![Excel COUNTBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20countblank%20function.png "Excel COUNTBLANK function")](https://exceljet.net/functions/countblank-function)

### [COUNTBLANK Function](https://exceljet.net/functions/countblank-function)

The Excel COUNTBLANK function returns a count of empty cells in a [range](https://exceljet.net/glossary/range)
. Cells that contain text, numbers, errors, spaces, etc. are _not_ counted. Formulas that return empty strings ("") _are_ counted as blank.

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

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
    
*   [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)
    
*   [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [COUNTBLANK Function](https://exceljet.net/functions/countblank-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [101 Excel Functions you should know](https://exceljet.net/articles/101-excel-functions)
    
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