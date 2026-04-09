# Multiple cells are equal - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/multiple-cells-are-equal

---

[Skip to main content](https://exceljet.net/formulas/multiple-cells-are-equal#main-content)

[](https://exceljet.net/formulas/multiple-cells-are-equal#)

*   [Previous](https://exceljet.net/formulas/last-row-number-in-range)
    
*   [Next](https://exceljet.net/formulas/multiple-cells-have-same-value)
    

[Range](https://exceljet.net/formulas#Range)

Multiple cells are equal
========================

by Dave Bruns · Updated 7 Jan 2018

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[EXACT](https://exceljet.net/functions/exact-function)

![Excel formula: Multiple cells are equal](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/multiple%20cells%20are%20equal.png "Excel formula: Multiple cells are equal")

Summary
-------

To confirm two ranges of the same size contain the same values, you can use a simple array formula based on the AND function. In the example shown, the formula in C9 is:

    {=AND(B5:D12=F5:H12)}
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

Generic formula
---------------

    {=AND(range1=range2)}

Explanation 
------------

The AND function is designed to evaluate multiple logical expressions, and returns TRUE only when all expressions are TRUE.

In this case the we simply compare one range with another with a single logical expression:

    B5:D12=F5:H12
    

The two ranges, B5:B12 and F5:H12 are the same dimensions, 5 rows x 3 columns, each containing 15 cells. The result of this operation is an array of 15 TRUE FALSE values of the same dimensions:

{TRUE,TRUE,TRUE;  
TRUE,TRUE,TRUE;  
TRUE,TRUE,TRUE;  
TRUE,TRUE,TRUE;  
TRUE,TRUE,TRUE;  
TRUE,TRUE,TRUE;  
TRUE,TRUE,TRUE;  
TRUE,TRUE,TRUE}

Each TRUE FALSE value is the result of comparing corresponding cells in the two arrays.

The AND function returns TRUE only if all values in the array are TRUE. In all other cases, AND will return FALSE.

### Case-sensitive option

The formula above is not case-sensitive. To compare two ranges in a case-sensitive manner, you can use a formula like this:

    {=AND(EXACT(range1,range2))}
    

Here, the EXACT function is used to make sure the test is case-sensitive. Like the formula above, this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter.

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

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

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
    

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    

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