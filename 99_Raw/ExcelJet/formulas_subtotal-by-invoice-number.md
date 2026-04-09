# Subtotal by invoice number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/subtotal-by-invoice-number

---

[Skip to main content](https://exceljet.net/formulas/subtotal-by-invoice-number#main-content)

[](https://exceljet.net/formulas/subtotal-by-invoice-number#)

*   [Previous](https://exceljet.net/formulas/subtotal-by-color)
    
*   [Next](https://exceljet.net/formulas/subtotal-invoices-by-age)
    

[Sum](https://exceljet.net/formulas#Sum)

Subtotal by invoice number
==========================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Subtotal by invoice number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/subtotal%20by%20invoice.png "Excel formula: Subtotal by invoice number")

Summary
-------

To subtotal values by invoice number, you can use a formula based on [COUNTIF](https://exceljet.net/functions/countif-function)
 and [SUMIF](https://exceljet.net/functions/sumif-function)
. In the example shown, the formula in E5 is:

    =IF(COUNTIF($B$5:B5,B5)=1,SUMIF($B:$B,B5,$D:$D),"")
    

Generic formula
---------------

    =IF(COUNTIF(range,criteria)=1,SUMIF(range,criteria,sumrange,"")

Explanation 
------------

This formula uses COUNTIF with an [expanding range](https://exceljet.net/glossary/expanding-reference)
 to first check if the current row is the first occurrence of a given invoice number:

    COUNTIF($B$5:B5,B5)=1
    

This expression only returns TRUE when this is the first occurrence of a given invoice number. If so, a SUMIF calculation is run:

    SUMIF($B:$B,B5,$D:$D)
    

Here, SUMIF generates a total sum by invoice number, using the amounts in column D. If the count is not 1, the formula simply returns an [empty string](https://exceljet.net/glossary/empty-string)
 ("")

Related formulas
----------------

[![Excel formula: Sum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_multiple_criteria.png "Excel formula: Sum if multiple criteria")](https://exceljet.net/formulas/sum-if-multiple-criteria)

### [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)

In this example, the goal is to sum the values in F5:F16 when the Color in C5:C16 is "Red" and the State in D5:D16 is "TX". This is an example of a conditional sum with multiple criteria and the SUMIFS function is the easiest way to solve this problem. SUMIFS function The SUMIFS function sums cells...

[![Excel formula: Subtotal invoices by age](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Subtotal%20invoices%20by%20age.png "Excel formula: Subtotal invoices by age")](https://exceljet.net/formulas/subtotal-invoices-by-age)

### [Subtotal invoices by age](https://exceljet.net/formulas/subtotal-invoices-by-age)

In this example, the goal is to subtotal invoices by age, where age represents the number of days since the invoice was issued. This problem can be solved with the SUMIFS function and the COUNTIFS function, as explained below. For convenience, age (E5:E16) and amount (D5:D16) are named ranges ...

[![Excel formula: Subtotal by color](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/subtotal%20by%20color_0.png "Excel formula: Subtotal by color")](https://exceljet.net/formulas/subtotal-by-color)

### [Subtotal by color](https://exceljet.net/formulas/subtotal-by-color)

In this example, the goal is to subtotal (count and sum) values based on cell color. This is a tricky problem, because there is no Excel function that will let you count cells by color directly. There are several different approaches, as explained below. Standard formula logic If color is being...

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countif-function)

### [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)

In this video we'll look at how to use the COUNTIF function to count cells that meet a single criteria. Let's take a look. The COUNTIF function counts cells that satisfy a single condition that you supply. It takes two arguments: range and criteria. For example, if I want to count the cells in this...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumif-function)

### [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)

In this video we'll look at how to use the SUMIF function to sum cells that meet a single criteria. Let's take a look. The SUMIF function sums cells that satisfy a single condition that you supply. It takes three arguments: range, criteria, and sum range. Note that sum range is optional. If you don...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)
    
*   [Subtotal invoices by age](https://exceljet.net/formulas/subtotal-invoices-by-age)
    
*   [Subtotal by color](https://exceljet.net/formulas/subtotal-by-color)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Videos

*   [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
    
*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    
*   [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)
    

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