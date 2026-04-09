# Multiple cells have same value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/multiple-cells-have-same-value

---

[Skip to main content](https://exceljet.net/formulas/multiple-cells-have-same-value#main-content)

[](https://exceljet.net/formulas/multiple-cells-have-same-value#)

*   [Previous](https://exceljet.net/formulas/multiple-cells-are-equal)
    
*   [Next](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)
    

[Range](https://exceljet.net/formulas#Range)

Multiple cells have same value
==============================

by Dave Bruns · Updated 5 Jan 2025

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: Multiple cells have same value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/all%20cells%20have%20same%20value.png "Excel formula: Multiple cells have same value")

Summary
-------

To confirm that a range of cells all have the same value, you can use a formula based on the COUNTIF function. In the example shown, the formula in C9 is:

    =COUNTIF(C5:C8,"<>ok")=0
    

_Note: this formula is not case-sensitive, you can find a_ [_case-sensitive formula here_](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)
_._

Generic formula
---------------

    =COUNTIF(rng,"<>value")=0

Explanation 
------------

This formula relies on the standard behavior of the COUNTIF function. The range is C5:C8, the criteria is provided as not equals OK:

    =COUNTIF(C5:C8,"<>ok")
    

The COUNTIF then returns a count of any cells that do not contain "OK" which is compared to zero. If the count is zero, the formula returns TRUE. If the count is anything but zero, the formula returns FALSE.

### Ignore empty cells

To ignore empty cells, you can use a more generic version of the formula:

    =COUNTIF(range,value)=COUNTA(range)
    

This formula generates a count of all matching values and compares that count to a count of all non-empty cells.

### Non-contiguous cells

If the cells are not in a contiguous range, you can use the [AND function](https://exceljet.net/functions/and-function)
 and a more manual approach. For example, to check that cells A1, A3, A5, and A9 contain "OK", you can use a formula like this:

    =AND(A1="ok",A3="ok",A5="ok",A9="ok")

> Excel is not case-sensitive by default, so using "OK" or "ok" will return the same result.

Related formulas
----------------

[![Excel formula: Multiple cells have same value case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Multiple%20cells%20have%20same%20value%20case%20sensitive.png "Excel formula: Multiple cells have same value case sensitive")](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)

### [Multiple cells have same value case sensitive](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)

This formula uses the EXACT formula to compare a range of cells to a single value: =EXACT(B5:F5,B5) Because we give EXACT a range of values in the first argument, we get back an array result containing TRUE FALSE values: {TRUE,FALSE,TRUE,TRUE,TRUE} This array goes into the AND function, which...

[![Excel formula: All cells in range are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all_cells_in_range_are_blank.png "Excel formula: All cells in range are blank")](https://exceljet.net/formulas/all-cells-in-range-are-blank)

### [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)

When working with Excel, there are times when you need to determine if a range of cells is empty. This can be useful in various scenarios, such as data validation, error checking, or report preparation. In this article, we'll explore a couple of formulas that can help you check if all cells in a...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Multiple cells have same value case sensitive](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)
    
*   [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

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