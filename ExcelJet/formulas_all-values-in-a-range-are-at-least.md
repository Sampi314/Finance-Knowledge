# All values in a range are at least - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/all-values-in-a-range-are-at-least

---

[Skip to main content](https://exceljet.net/formulas/all-values-in-a-range-are-at-least#main-content)

[](https://exceljet.net/formulas/all-values-in-a-range-are-at-least#)

*   [Previous](https://exceljet.net/formulas/all-cells-in-range-are-blank)
    
*   [Next](https://exceljet.net/formulas/automatic-row-numbers)
    

[Range](https://exceljet.net/formulas#Range)

All values in a range are at least
==================================

by Dave Bruns · Updated 29 Apr 2018

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[NOT](https://exceljet.net/functions/not-function)

![Excel formula: All values in a range are at least](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/All%20values%20in%20a%20range%20are%20at%20least.png "Excel formula: All values in a range are at least")

Summary
-------

To test if all values in a range are at least a certain threshold value, you can use the COUNTIF function together with the NOT function. In the example shown, the formula in G5 is:

    =NOT(COUNTIF(B5:F5,"<65"))
    

Generic formula
---------------

    =NOT(COUNTIF(range,"<65"))

Explanation 
------------

At the core, this formula uses the COUNTIF function to count any cells that fall below a given value, which is hardcoded as 65 in the formula:

    COUNTIF(B5:F5,"<65")
    

In this part of the formula, COUNTIF will return a positive number if any cell in the range is less than 65, and zero if not. In the range B5:F5, there is one score below 65 so COUNTIF will return 1.

The NOT function is used to convert the number of from COUNTIF into a TRUE or FALSE result. The trick is that NOT also "flips" the result at the same time:

*   If any values are less than 65, COUNTIF returns a positive number and NOT returns FALSE
*   f no values are less than 65, COUNTIF returns a zero and NOT returns TRUE

This is the equivalent of wrapping COUNTIF inside IF and providing a "reversed" TRUE and FALSE result like this:

    =IF(COUNTIF(B5:F5,"<65"),FALSE,TRUE)
    

Related formulas
----------------

[![Excel formula: All cells in range are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all_cells_in_range_are_blank.png "Excel formula: All cells in range are blank")](https://exceljet.net/formulas/all-cells-in-range-are-blank)

### [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)

When working with Excel, there are times when you need to determine if a range of cells is empty. This can be useful in various scenarios, such as data validation, error checking, or report preparation. In this article, we'll explore a couple of formulas that can help you check if all cells in a...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

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
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

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