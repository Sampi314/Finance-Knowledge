# Highlight unprotected cells - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-unprotected-cells

---

[Skip to main content](https://exceljet.net/formulas/highlight-unprotected-cells#main-content)

[](https://exceljet.net/formulas/highlight-unprotected-cells#)

*   [Previous](https://exceljet.net/formulas/highlight-unique-values)
    
*   [Next](https://exceljet.net/formulas/highlight-values-between)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight unprotected cells
===========================

by Dave Bruns · Updated 12 Jun 2020

Related functions 
------------------

[CELL](https://exceljet.net/functions/cell-function)

![Excel formula: Highlight unprotected cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/conditional%20formatting%20unprotected%20cells.png "Excel formula: Highlight unprotected cells")

Summary
-------

To highlight unprotected cells (cells that are unlocked) with conditional formatting, you can use a formula based on the CELL function. In the example shown, the custom formula used to set up conditional formatting is:

    =CELL("PROTECT",A1)=0
    

Where A1 represents the active cell in the selection when the rule was defined.

Generic formula
---------------

    =CELL("PROTECT",A1)=0

Explanation 
------------

The CELL function can provide a wide range of information about cell properties. One property is called "protect" and indicates whether a cell is unlocked or locked. All cells start out "locked" in a new Excel workbook, but this setting has no effect until a worksheet is protected.

The CELL function returns either 1 or zero to indicate "on" or "off". In this case we are comparing the result to zero, so when CELL returns 0, the expression returns TRUE and the conditional formatting is triggered. When CELL returns 1, the expression returns FALSE and no conditional formatting is applied.

Related functions
-----------------

[![Excel CELL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20cell%20function.png "Excel CELL function")](https://exceljet.net/functions/cell-function)

### [CELL Function](https://exceljet.net/functions/cell-function)

The Excel CELL function returns information about a cell in a worksheet. The type of information to be returned is specified as _info\_type_. CELL can get things like address and filename, as well as detailed info about the formatting used in the cell. See below for a full list of...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20test%20conditional%20formatting%20with%20dummy%20formulas-thumb.png)](https://exceljet.net/videos/how-to-test-conditional-formatting-with-dummy-formula)

### [How to test conditional formatting with dummy formula](https://exceljet.net/videos/how-to-test-conditional-formatting-with-dummy-formula)

In this video, I'll show you how to quickly test your conditional formatting rules with dummy formulas. When you apply conditional formatting with formulas, it can be hard to get the formulas to work properly, because you can't see what happens to the formula when the rule is applied. You can think...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [CELL Function](https://exceljet.net/functions/cell-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [How to test conditional formatting with dummy formula](https://exceljet.net/videos/how-to-test-conditional-formatting-with-dummy-formula)
    

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