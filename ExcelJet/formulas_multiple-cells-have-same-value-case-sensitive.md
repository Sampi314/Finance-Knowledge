# Multiple cells have same value case sensitive - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive

---

[Skip to main content](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive#main-content)

[](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive#)

*   [Previous](https://exceljet.net/formulas/multiple-cells-have-same-value)
    
*   [Next](https://exceljet.net/formulas/multiple-columns-are-equal)
    

[Range](https://exceljet.net/formulas#Range)

Multiple cells have same value case sensitive
=============================================

by Dave Bruns · Updated 19 Sep 2020

Related functions 
------------------

[EXACT](https://exceljet.net/functions/exact-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[COUNTA](https://exceljet.net/functions/counta-function)

![Excel formula: Multiple cells have same value case sensitive](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Multiple%20cells%20have%20same%20value%20case%20sensitive.png "Excel formula: Multiple cells have same value case sensitive")

Summary
-------

To verify that multiple cells have the same value with a case-sensitive formula, you can use a simple array formula based on the [EXACT function](https://exceljet.net/functions/exact-function)
 with the [AND function](https://exceljet.net/functions/and-function)
. In the example shown, the formula in G5 is:

    =AND(EXACT(B5:F5,B5))
    

_This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter_

Generic formula
---------------

    {=AND(EXACT(range,value))}

Explanation 
------------

This formula uses the EXACT formula to compare a range of cells to a single value:

    =EXACT(B5:F5,B5)
    

Because we give EXACT a range of values in the first argument, we get back an array result containing TRUE FALSE values:

    {TRUE,FALSE,TRUE,TRUE,TRUE}
    

This array goes into the AND function, which returns TRUE only if all values in the array are TRUE.

### Ignore empty cells

To ignore empty cells, but still treat non-empty cells in a case-sensitive manner, you can use a version of the formula based on SUMPRODUCT:

    =SUMPRODUCT(--(EXACT(range,value)))=COUNTA(range)
    

Here, we count exact matches using the same EXACT formula above, get a total count with SUMPRODUCT, and compare the result to a count of all non-empty cells, determined by COUNTA.

This is an array formula but control + shift + enter is not required because SUMPRODUCT handles the array natively.

Related formulas
----------------

[![Excel formula: All cells in range are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all_cells_in_range_are_blank.png "Excel formula: All cells in range are blank")](https://exceljet.net/formulas/all-cells-in-range-are-blank)

### [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)

When working with Excel, there are times when you need to determine if a range of cells is empty. This can be useful in various scenarios, such as data validation, error checking, or report preparation. In this article, we'll explore a couple of formulas that can help you check if all cells in a...

[![Excel formula: Multiple cells have same value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all%20cells%20have%20same%20value.png "Excel formula: Multiple cells have same value")](https://exceljet.net/formulas/multiple-cells-have-same-value)

### [Multiple cells have same value](https://exceljet.net/formulas/multiple-cells-have-same-value)

This formula relies on the standard behavior of the COUNTIF function. The range is C5:C8, the criteria is provided as not equals OK: =COUNTIF(C5:C8,"<>ok") The COUNTIF then returns a count of any cells that do not contain "OK" which is compared to zero. If the count is zero, the formula...

Related functions
-----------------

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

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
    
*   [Multiple cells have same value](https://exceljet.net/formulas/multiple-cells-have-same-value)
    

### Functions

*   [EXACT Function](https://exceljet.net/functions/exact-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    

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