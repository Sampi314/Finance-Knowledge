# Multiple columns are equal - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/multiple-columns-are-equal

---

[Skip to main content](https://exceljet.net/formulas/multiple-columns-are-equal#main-content)

[](https://exceljet.net/formulas/multiple-columns-are-equal#)

*   [Previous](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)
    
*   [Next](https://exceljet.net/formulas/range-contains-a-value-not-in-another-range)
    

[Range](https://exceljet.net/formulas#Range)

Multiple columns are equal
==========================

by Dave Bruns · Updated 29 Jul 2022

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Multiple columns are equal](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/multiple%20columns%20are%20equal.png "Excel formula: Multiple columns are equal")

Summary
-------

To test if values in multiple columns are the same, you can use a simple array formula based on the [AND function](https://exceljet.net/functions/and-function)
. In the example shown, the formula in H5 is:

    {=AND(B5=C5:F5)}
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, unless you are using [Excel 365](https://exceljet.net/glossary/excel-365)
, where array formulas are native._

Explanation 
------------

In the example shown, we want to test if all values in each row are equal. To do this, we use an expression that compares the value in the first column (B5) to the rest of the columns (C5:F5):

    B5=C5:F5
    

Because we are comparing one cell value to values in four other cells, the result is an [array](https://exceljet.net/glossary/array)
 with four TRUE or FALSE values. In row 5, all values are equal, so all values are TRUE:

    {TRUE,TRUE,TRUE,TRUE}
    

This array is returned directly to the AND function, which returns TRUE, since all values in the array are TRUE.

    =AND({TRUE,TRUE,TRUE,TRUE}) // returns TRUE
    

In cell H6, B6=C6:F6 creates an array with two FALSE values, since D6 and F6 are different.

    {TRUE,FALSE,TRUE,FALSE}
    

This array is delivered to the AND function, which returns FALSE:

    =AND({TRUE,FALSE,TRUE,FALSE}) // returns FALSE
    

### Counting differences

The formula in I5 uses the [COUNTIF function](https://exceljet.net/functions/countif-function)
 to count differences in each row like this:

    =COUNTIF(C5:F5,"<>"&B5)
    

The criteria is provided as "<>"&B5, which means "is not equal to B5".

You can adjust the formula to mimic the behavior of the AND formula above like this:

    =COUNTIF(C5:F5,"<>"&B5)=0
    

Here, we simply compare the result from COUNTIF to zero. A count of zero returns TRUE, and any other number returns FALSE.

This is _not_ an array formula, so it does not require special handling.

Related formulas
----------------

[![Excel formula: Multiple cells have same value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all%20cells%20have%20same%20value.png "Excel formula: Multiple cells have same value")](https://exceljet.net/formulas/multiple-cells-have-same-value)

### [Multiple cells have same value](https://exceljet.net/formulas/multiple-cells-have-same-value)

This formula relies on the standard behavior of the COUNTIF function. The range is C5:C8, the criteria is provided as not equals OK: =COUNTIF(C5:C8,"<>ok") The COUNTIF then returns a count of any cells that do not contain "OK" which is compared to zero. If the count is zero, the formula...

[![Excel formula: Multiple cells have same value case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Multiple%20cells%20have%20same%20value%20case%20sensitive.png "Excel formula: Multiple cells have same value case sensitive")](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)

### [Multiple cells have same value case sensitive](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)

This formula uses the EXACT formula to compare a range of cells to a single value: =EXACT(B5:F5,B5) Because we give EXACT a range of values in the first argument, we get back an array result containing TRUE FALSE values: {TRUE,FALSE,TRUE,TRUE,TRUE} This array goes into the AND function, which...

[![Excel formula: All cells in range are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all_cells_in_range_are_blank.png "Excel formula: All cells in range are blank")](https://exceljet.net/formulas/all-cells-in-range-are-blank)

### [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)

When working with Excel, there are times when you need to determine if a range of cells is empty. This can be useful in various scenarios, such as data validation, error checking, or report preparation. In this article, we'll explore a couple of formulas that can help you check if all cells in a...

[![Excel formula: Multiple cells are equal](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple%20cells%20are%20equal.png "Excel formula: Multiple cells are equal")](https://exceljet.net/formulas/multiple-cells-are-equal)

### [Multiple cells are equal](https://exceljet.net/formulas/multiple-cells-are-equal)

The AND function is designed to evaluate multiple logical expressions, and returns TRUE only when all expressions are TRUE. In this case the we simply compare one range with another with a single logical expression: B5:D12=F5:H12 The two ranges, B5:B12 and F5:H12 are the same dimensions, 5 rows x 3...

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Multiple cells have same value](https://exceljet.net/formulas/multiple-cells-have-same-value)
    
*   [Multiple cells have same value case sensitive](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)
    
*   [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)
    
*   [Multiple cells are equal](https://exceljet.net/formulas/multiple-cells-are-equal)
    

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

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