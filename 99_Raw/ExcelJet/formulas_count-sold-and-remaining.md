# Count sold and remaining - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-sold-and-remaining

---

[Skip to main content](https://exceljet.net/formulas/count-sold-and-remaining#main-content)

[](https://exceljet.net/formulas/count-sold-and-remaining#)

*   [Previous](https://exceljet.net/formulas/count-rows-with-or-logic)
    
*   [Next](https://exceljet.net/formulas/count-total-matches-in-two-ranges)
    

[Count](https://exceljet.net/formulas#Count)

Count sold and remaining
========================

by Dave Bruns · Updated 10 Jul 2022

Related functions 
------------------

[COUNTA](https://exceljet.net/functions/counta-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Count sold and remaining](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20sold%20and%20remaining.png "Excel formula: Count sold and remaining")

Summary
-------

To count how many items have been sold, and how many items remain, you can use the [COUNTA function](https://exceljet.net/functions/counta-function)
. In the example shown, the formula in F7 is:

    =COUNTA(B5:B16)-COUNTA(C5:C16)
    

The result is 5, since 7 out of 12 items have been sold. You can also use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 to solve this problem. Both approaches are described below.

Generic formula
---------------

    =COUNTA(range1)-COUNTA(range2)

Explanation 
------------

In this example, the goal is to count the number of items sold and remaining, based on the data visible in columns B and C. The ID column holds unique ids, and the Sold column is used to record a sale. An "x" in the Sold column indicates the item has been sold. As is typical in Excel, there are several ways to solve this problem. The article below explains two approaches. 

### COUNTA function

The [COUNTA function](https://exceljet.net/functions/counta-function)
 counts non-blank cells in a range. Unlike the COUNT function, which only counts _numeric_ values, COUNTA will count _any value_ in a cell, including numbers and text. The first formula in F5 counts the total items available:

    =COUNTA(B5:B16) // returns 12
    

The result is 12 since there are 12 values in the ID column. The second formula counts the number of items that have been sold:

    =COUNTA(C5:C16) // returns 7
    

The result is 7 since there are 7 values in the Sold column. Note that COUNTA doesn't care what value is in a cell. In the example shown, we are using an "x" to indicate sold items, but COUNTA would count "y" or "z" in the same way. The last formula counts the number of remaining items:

    =COUNTA(B5:B16)-COUNTA(C5:C16) // returns 5
    

The result is 5 since 12 minus 7 equals 5. In this example, last formula above is an all-in-one formula, to provide more detail. However, in this particular case, the best practice would be to write the last formula like this:

    =F5-F6 // use existing values
    

In other words, we simply re-use existing results. This minimizes the number of calculations performed and reduces errors.

### COUNTIF function

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 counts values in a range based on supplied _criteria_. With COUNTIF the problem can be solved a bit differently. To count total items, you can use COUNTIF like this:

    =COUNTIF(B5:B16,"<>") // count not blank
    

To count sold items you can use either of these formulas:

    =COUNTIF(C5:C16,"x") // count equal to "x" 
    =COUNTIF(C5:C16,"<>") // count not blank
    

To count items not sold, you can use COUNTIF like this:

    =COUNTIF(C5:C16,"") // count blank
    

### Match test

If you need to make sure that the value in column C matches the value in column B, in the same row, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 instead:

    =SUMPRODUCT(--(B5:B11=C5:C11))
    

For more information about how this formula works, see [this explanation](https://exceljet.net/formulas/count-matches-between-two-columns)
.

Related formulas
----------------

[![Excel formula: Count matches between two columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20matches%20between%20two%20columns.png "Excel formula: Count matches between two columns")](https://exceljet.net/formulas/count-matches-between-two-columns)

### [Count matches between two columns](https://exceljet.net/formulas/count-matches-between-two-columns)

In this example, the goal is to compare two columns and return the count of matches in corresponding rows. A good way to solve this problem is to use the SUMPRODUCT function or the SUM function, as explained below. SUMPRODUCT function The SUMPRODUCT function is a versatile function that handles...

[![Excel formula: Basic inventory formula example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20inventory%20formula%20example.png "Excel formula: Basic inventory formula example")](https://exceljet.net/formulas/basic-inventory-formula-example)

### [Basic inventory formula example](https://exceljet.net/formulas/basic-inventory-formula-example)

This formula demonstrates a very simple inventory concept where current inventory is simply the result of all incoming stock minus all outgoing stock. In the example, colors are treated as unique item identifiers – imagine a product available in one size only in just three colors: red, blue, or...

Related functions
-----------------

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

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

*   [Count matches between two columns](https://exceljet.net/formulas/count-matches-between-two-columns)
    
*   [Basic inventory formula example](https://exceljet.net/formulas/basic-inventory-formula-example)
    

### Functions

*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
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