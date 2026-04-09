# Text is greater than number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/text-is-greater-than-number

---

[Skip to main content](https://exceljet.net/formulas/text-is-greater-than-number#main-content)

[](https://exceljet.net/formulas/text-is-greater-than-number#)

*   [Previous](https://exceljet.net/formulas/sum-text-values-like-numbers)
    
*   [Next](https://exceljet.net/formulas/transpose-table-without-zeros)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Text is greater than number
===========================

by Dave Bruns · Updated 20 May 2022

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: Text is greater than number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/text%20is%20greater%20than%20number.png "Excel formula: Text is greater than number")

Summary
-------

One of Excel's quirks is that text can sometimes be evaluated as greater than a number, even a large number. In the example shown, the formula in D5 is:

    =B5>100
    

As the formula is copied down, you can see that Excel evaluates text values in D9:D11 as greater than the number 100.

Explanation 
------------

Excel's formula engine has some quirks that you should be aware of. One of these quirks is that Excel will treat a text value as larger than a number by default. For example:

    =90>100 // returns FALSE
    ="A">100 // returns TRUE
    

The second formula above returns TRUE when you probably expect it to return FALSE. You can see this behavior in the worksheet shown in cells D9:D11. We are comparing each value in column B to 100, and the values in these cells return TRUE because they contain text. Essentially, any text value (even a space " ") will be evaluated as greater than any number.

### Counting values greater than

This behavior can affect how other formulas count values that are greater than a specific number. For example, the [COUNTIF](https://exceljet.net/functions/countif-function)
 and [COUNTIFS](https://exceljet.net/functions/countifs-function)
 functions don't exhibit this behavior. The formula in G5 returns 1:

    =COUNTIF(B5:B11,">100") // returns 1
    

However a formula that deals with logical expressions directly will show Excel's native behavior. For example, the [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 formula in cell F7 returns 4:

    =SUMPRODUCT(--(B5:B11>100)) // returns 4
    

This is an example of using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 in a formula.

### Ignoring text values

To ignore text values in a formula like this, you can add an additional check with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
. The SUMPRODUCT formula below has been modified to check that values are (1) larger than 100 and (2) actually numeric:

    =SUMPRODUCT(--(B5:B11>100)*ISNUMBER(B5:B11)) // returns 1
    

This formula returns 1 as a result. 

Related formulas
----------------

[![Excel formula: Count cells that contain text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20text.png "Excel formula: Count cells that contain text")](https://exceljet.net/formulas/count-cells-that-contain-text)

### [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)

In this example, the goal is to count cells in a range that contain text values. This could be hard-coded text like "apple" or "red", numbers entered as text, or formulas that return text values. Empty cells and cells that contain numeric values or errors should not be included in the count. This...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

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