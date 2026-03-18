# Transpose table without zeros - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/transpose-table-without-zeros

---

[Skip to main content](https://exceljet.net/formulas/transpose-table-without-zeros#main-content)

[](https://exceljet.net/formulas/transpose-table-without-zeros#)

*   [Previous](https://exceljet.net/formulas/text-is-greater-than-number)
    
*   [Next](https://exceljet.net/formulas/unwrap-column-into-fields)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Transpose table without zeros
=============================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Transpose table without zeros](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/transpose%20table%20without%20zeros.png "Excel formula: Transpose table without zeros")

Summary
-------

To dynamically transpose a table that contains blanks, you can use an array formula based on the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 and [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the multi-cell array formula in H5:I9 is:

    {=TRANSPOSE(IF(B5:F6="","",B5:F6))}
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 that must be entered with Control + Shift + Enter across the entire range H5:I9, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Generic formula
---------------

    {=TRANSPOSE(IF(rng="","",rng))}

Explanation 
------------

The TRANSPOSE function automatically transposes values in a horizontal orientation to vertical orientation and vice versa.

However, if a source cell is blank (empty) TRANSPOSE will output a zero. To fix that problem, this formula contains an IF function that checks first to see if a cell is blank or not. When a cell is blank, the IF function supplied an [empty string](https://exceljet.net/glossary/empty-string)
 ("") to transpose. If not, IF supplies the value normally.

Without IF, the array going into TRANSPOSE looks like this:

    {"Item","apples","pears","limes",0;"Qty",14,10,4,0}
    

After IF, it looks like this:

    {"Item","apples","pears","limes","";"Qty",14,10,4,""}
    

Related functions
-----------------

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

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