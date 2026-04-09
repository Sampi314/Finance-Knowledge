# All dates in chronological order - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/all-dates-in-chronological-order

---

[Skip to main content](https://exceljet.net/formulas/all-dates-in-chronological-order#main-content)

[](https://exceljet.net/formulas/all-dates-in-chronological-order#)

*   [Previous](https://exceljet.net/formulas/add-leading-zeros-to-numbers)
    
*   [Next](https://exceljet.net/formulas/basic-array-formula-example)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

All dates in chronological order
================================

by Dave Bruns · Updated 27 Feb 2021

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[SORT](https://exceljet.net/functions/sort-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6500/download?token=3NxPNaw5)
 (15.52 KB)

![Excel formula: All dates in chronological order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/all%20dates%20are%20in%20order.png "Excel formula: All dates in chronological order")

Summary
-------

To check if a range of dates are in chronological order,  you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in H5 is:

    =IF(SUMPRODUCT(--(A5:E5>=B5:F5))=0,"✓","")
    

This formula returns a check mark character (✓) if all dates are in chronological order and an [empty string](https://exceljet.net/glossary/empty-string)
 ("") if not.

Generic formula
---------------

    =IF(SUMPRODUCT(--(range1>=range2))=0,"✓","")

Explanation 
------------

This is a good example of how the SUMPRODUCT function can help in situations where the [COUNTIF](https://exceljet.net/functions/countif-function)
 or [COUNTIFS](https://exceljet.net/functions/countifs-function)
 functions do not work. In this case, the goal is to check all dates in a given range and show a check mark (✓) only when dates are in chronological order.

The logic itself is quite simple, but perhaps not intuitive. Rather than check that _all_ dates are greater than the previous date, we check if _any_ previous date is _greater_ than the next date. If we find even one, the dates are not in order. If we find none (zero), they are.

At the core, this formula is based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
, which counts the number of dates in A5:E5 that are greater than or equal to B5:F5:

    SUMPRODUCT(--(A5:E5>=B5:F5)) // count invalid dates
    

Note we are using the greater than or equal to (>=) operator, we will _disallow_ consecutive duplicate dates.

This is an [array operation](https://exceljet.net/glossary/array-operation)
 where both ranges contain five dates. The result is an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values like this:

    {FALSE,FALSE,FALSE,FALSE,FALSE}
    

Each FALSE signifies a date in B5:F5 that is _not_ greater or equal to the preceding date. Notice the range A5:E5 deliberately includes empty cells in column A, which has the practical effect of treating any blank dates in column B as invalid. But it also requires that relevant cells in column A be empty.

The next step is to coerce the TRUE and FALSE values into 1s and 0s so they can be counted. [There are a number of ways](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 to do this in Excel, but in this case we use a [double negative](https://exceljet.net/glossary/double-unary)
 (--):

    --({FALSE,FALSE,FALSE,FALSE,FALSE}} // returns {0,0,0,0,0}
    

which returns an array of 5 zeros. This array is returned to the SUMPRODUCT function, which sums the array:

    SUMPRODUCT({0,0,0,0,0}) // returns zero
    

Because the result we want is zero (i.e. no invalid dates) we test for zero, which returns TRUE:

    =SUMPRODUCT({0,0,0,0,0})=0
    =0=0
    =TRUE
    

This result is returned directly to the [IF function](https://exceljet.net/functions/if-function)
 as the logical test.

    =IF(TRUE,"✓","")
    ="✓"
    

IF then returns a check mark since all dates are in order. The way the formula is structured, any number of dates out of sequence will cause the test to return a number greater than zero, and the IF function to return an empty string ("") instead of a check mark ("✓"). For example, in row 8, which has one date out of sequence, the formula evaluates like this:

    =IF(SUMPRODUCT(--(A8:E8>=B8:F8))=0,"✓","")
    =IF(SUMPRODUCT(--({FALSE,FALSE,TRUE,FALSE,FALSE}))=0,"✓","")
    =IF(SUMPRODUCT({0,0,1,0,0})=0,"✓","")
    =IF(1=0,"✓","")
    =IF(FALSE,"✓","")
    =""
    

Although this example has just five dates in each row, the same approach will scale up to any number of dates.

### With SORT

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the [SORT function](https://exceljet.net/functions/sort-function)
 provides a nice alternative solution:

    =IF(SUM(--(B5:F5<>SORT(B5:F5,1,1,1)))=0,"✓","")
    

In this version, the dates in B5:F5 are compared to the same dates, after sorting with SORT. Similar to the original formula above, we are counting any case where a date is not the same (i.e. any date moved by SORT). If we find zero dates that are different, the check mark is returned.

Unlike the original formula, the SORT version won't automatically check for blank (empty) cells or for duplicate dates. The version below adds this additional check for blank cells:

    =IF(SUM(((B5:F5<>SORT(B5:F5,1,1,1)))+(B5:F5=""))=0,"✓","")
    

And this version checks for both empty and duplicate values:

    =IF(SUM(((B5:F5<>SORT(B5:F5,1,1,1)))+(B5:F5="")+(A5:E5=B5:F5))=0,"✓","")
    

The addition (+) operator works like OR logic in [Boolean Algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
. The math operation automatically coerces TRUE and FALSE values to 1s and 0s, so we no longer need the double negative (--).

_Note: we use the [SUM function](https://exceljet.net/videos/how-to-use-the-sum-function)
 here instead of SUMPRODUCT because the [dynamic array support in Excel 365](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 means SUM can handle the array operation natively, without control + shift + enter._

### Check mark character (✓)

Inserting a check mark character in Excel can be tricky. The easiest way to get the check mark character (✓) used in this formula into Excel is simply to copy and paste it into the [formula bar](https://exceljet.net/glossary/formula-bar)
. If you have trouble, you can use the [UNICHAR function](https://exceljet.net/functions/unichar-function)
 like this:

    =UNICHAR(10003) // returns "✓"
    

The original formula can then be written like this:

    =IF(SUMPRODUCT(--(A5:E5>=B5:F5))=0,UNICHAR(10003),"")
    

and return the same results. The UNICHAR function was introduced in Excel 2013.

### Conditional Formatting

You can also use [conditional formatting](https://exceljet.net/conditional-formatting-formulas)
 to highlight invalid dates. In the example shown, dates that are out of sequence are highlighted with a simple rule, based on this formula:

    =B5<=A5
    

The rule is applied to all dates in the range B5:F15.

Related formulas
----------------

[![Excel formula: All values in a range are at least](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/All%20values%20in%20a%20range%20are%20at%20least.png "Excel formula: All values in a range are at least")](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)

### [All values in a range are at least](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)

At the core, this formula uses the COUNTIF function to count any cells that fall below a given value, which is hardcoded as 65 in the formula: COUNTIF(B5:F5,"<65") In this part of the formula, COUNTIF will return a positive number if any cell in the range is less than 65, and zero if not. In the...

[![Excel formula: Validate input with check mark](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/validate_input_with_check_mark.png "Excel formula: Validate input with check mark")](https://exceljet.net/formulas/validate-input-with-check-mark)

### [Validate input with check mark](https://exceljet.net/formulas/validate-input-with-check-mark)

This formula is a good example of nesting one function inside another. At the core, this formula uses the IF function to return a check mark (✓) when a logical test returns TRUE: =IF(logical\_test,"✓","") If the test returns FALSE, the formula returns an empty string (""). For the logical test, we...

[![Excel formula: If cell begins with x, y, or z](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_begins_with_x_y_or_z_0.png "Excel formula: If cell begins with x, y, or z")](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)

### [If cell begins with x, y, or z](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)

The goal is to take a specific action when a value begins with "x", "y", or "z". As is often the case in Excel, there are multiple ways to approach this problem. The simplest way is to use the OR function with the LEFT function to create the required logical test. Another option is to use the...

[![Excel formula: All cells in range are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all_cells_in_range_are_blank.png "Excel formula: All cells in range are blank")](https://exceljet.net/formulas/all-cells-in-range-are-blank)

### [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)

When working with Excel, there are times when you need to determine if a range of cells is empty. This can be useful in various scenarios, such as data validation, error checking, or report preparation. In this article, we'll explore a couple of formulas that can help you check if all cells in a...

[![Excel formula: Data validation must not exist in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20must%20not%20exist%20in%20list.png "Excel formula: Data validation must not exist in list")](https://exceljet.net/formulas/data-validation-must-not-exist-in-list)

### [Data validation must not exist in list](https://exceljet.net/formulas/data-validation-must-not-exist-in-list)

Data validation rules are triggered when a user adds or changes a cell value. In this case, the COUNTIF function is part of an expression that returns TRUE when a value does not exist in a defined list. The COUNTIF function simply counts occurrences of the value in the list. As long as the count is...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [All values in a range are at least](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)
    
*   [Validate input with check mark](https://exceljet.net/formulas/validate-input-with-check-mark)
    
*   [If cell begins with x, y, or z](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)
    
*   [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)
    
*   [Data validation must not exist in list](https://exceljet.net/formulas/data-validation-must-not-exist-in-list)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    

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