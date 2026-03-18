# Subtotal invoices by age - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/subtotal-invoices-by-age

---

[Skip to main content](https://exceljet.net/formulas/subtotal-invoices-by-age#main-content)

[](https://exceljet.net/formulas/subtotal-invoices-by-age#)

*   [Previous](https://exceljet.net/formulas/subtotal-by-invoice-number)
    
*   [Next](https://exceljet.net/formulas/sum-across-multiple-worksheets)
    

[Sum](https://exceljet.net/formulas#Sum)

Subtotal invoices by age
========================

by Dave Bruns · Updated 12 Aug 2022

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

![Excel formula: Subtotal invoices by age](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Subtotal%20invoices%20by%20age.png "Excel formula: Subtotal invoices by age")

Summary
-------

To subtotal invoice amounts by age, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 and the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. In the example shown, the formula in I5 is:

    =SUMIFS(amount,age,"<=30")
    

Where **age** (E5:E16) and **amount** (D5:D16) are [named ranges](https://exceljet.net/glossary/named-range)
. See below for the formulas in I6 and I7, and the formulas in H5:H7.

Generic formula
---------------

    =SUMIF(amount,age,criteria)

Explanation 
------------

In this example, the goal is to subtotal invoices by age, where age represents the number of days since the invoice was issued. This problem can be solved with the SUMIFS function and the COUNTIFS function, as explained below. For convenience, **age** (E5:E16) and **amount** (D5:D16) are [named ranges](https://exceljet.net/glossary/named-range)
. 

### SUMIFS function

The [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 is designed to sum cells that meet multiple criteria. SUMIFS takes at least three arguments like this:

    =SUMIFS(sum_range,range1,criteria1)
    

Notice _sum\_range_ appears first. Additional criteria are added in range/criteria pairs like this:

    =SUMIFS(sum_range,range1,criteria1,range2,criteria2)
    

The formulas used to sum invoices by age in I5:I7 are as follows:

    SUMIFS(amount,age,"<=30")
    SUMIFS(amount,age,">30",age,"<=45")
    SUMIFS(amount,age,">45")
    

Notice that criteria appear in double quotes (""). SUMIFS is in a [group of eight functions](https://exceljet.net/articles/excels-racon-functions)
 that share this syntax.

### COUNTIFS function

To _count_ invoices by age, you can use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
, which is designed to count cells based on multiple criteria. Like SUMIFS, COUNTIFS accepts arguments as range/criteria pairs:

    =COUNTIFS(range1,criteria1,range2,criteria2)
    

The formulas used to count invoices by age in H5:H7 are as follows:

    COUNTIFS(age,"<=30")
    COUNTIFS(age,">30",age,"<=45")
    COUNTIFS(age,">45")
    

Notice the criteria used by COUNTIFS is exactly the same as that used by SUMIFS. The difference is that COUNTIFS does not have a _sum\_range_ argument.

Related formulas
----------------

[![Excel formula: Sum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_multiple_criteria.png "Excel formula: Sum if multiple criteria")](https://exceljet.net/formulas/sum-if-multiple-criteria)

### [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)

In this example, the goal is to sum the values in F5:F16 when the Color in C5:C16 is "Red" and the State in D5:D16 is "TX". This is an example of a conditional sum with multiple criteria and the SUMIFS function is the easiest way to solve this problem. SUMIFS function The SUMIFS function sums cells...

[![Excel formula: Subtotal by color](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/subtotal%20by%20color_0.png "Excel formula: Subtotal by color")](https://exceljet.net/formulas/subtotal-by-color)

### [Subtotal by color](https://exceljet.net/formulas/subtotal-by-color)

In this example, the goal is to subtotal (count and sum) values based on cell color. This is a tricky problem, because there is no Excel function that will let you count cells by color directly. There are several different approaches, as explained below. Standard formula logic If color is being...

[![Excel formula: Dynamic summary count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20summary%20count.png "Excel formula: Dynamic summary count")](https://exceljet.net/formulas/dynamic-summary-count)

### [Dynamic summary count](https://exceljet.net/formulas/dynamic-summary-count)

In this example, the goal is to build a simple summary count table with a formula. Once created, the summary table should automatically update to show new values and counts when data changes. The article below walks through several options, from simple to very advanced. The more advanced options...

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIFS%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countifs-function)

### [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)

In this video, we'll look at how to use the COUNTIFS function to count cells that meet multiple criteria. Let's take a look. In this first set of tables, we have two named ranges , "number" and "color." In column G, I'll enter a formula that satisfies the conditions in column E. The COUNTIFS...

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
    
*   [Subtotal by color](https://exceljet.net/formulas/subtotal-by-color)
    
*   [Dynamic summary count](https://exceljet.net/formulas/dynamic-summary-count)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)
    

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