# Sum range with INDEX - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-range-with-index

---

[Skip to main content](https://exceljet.net/formulas/sum-range-with-index#main-content)

[](https://exceljet.net/formulas/sum-range-with-index#)

*   [Previous](https://exceljet.net/formulas/sum-lookup-values-using-sumif)
    
*   [Next](https://exceljet.net/formulas/sumifs-multiple-criteria-lookup-in-table)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Sum range with INDEX
====================

by Dave Bruns · Updated 10 Sep 2018

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Sum range with INDEX](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Sum%20range%20with%20INDEX.png "Excel formula: Sum range with INDEX")

Summary
-------

To sum all values in a column or row, you can use the INDEX function to retrieve the values, and the SUM function to return the sum. This technique is useful in situations where the row or column being summed is dynamic, and changes based on user input. In the example shown, the formula in H6 is:

    =SUM(INDEX(data,0,H5))
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 C5:E9.

Generic formula
---------------

    =SUM(INDEX(data,0,column))

Explanation 
------------

The INDEX function looks up values by position. For example, this formula retrieves the value for Acme sales in Jan:

    =INDEX(data,1,1)
    

The INDEX function has a special and non-obvious behavior: when the row number argument is supplied as zero or null, INDEX retrieves all values in the column referenced by the column number argument. Likewise, when the column number is supplied as zero or nothing, INDEX retrieves all values in the row referenced by the row number argument:

    =INDEX(data,0,1) // all of column 1
    =INDEX(data,1,0) // all of row 1
    

In the example for formula, we supply the named range "data" for array, and we pick up the column number from H2. For row number, we deliberately supply zero. This causes INDEX to retrieve all values in column 2 of "data'. The formula is solved like this:

    =SUM(INDEX(data,0,2))
    =SUM({9700;2700;23700;16450;17500})
    =70050
    

### Other calculations

You can use the same approach for other calculations by replacing SUM with AVERAGE, MAX, MIN, etc. For example, to get an average of values in the third month, you can use:

    =AVERAGE(INDEX(data,0,3))
    

### More than one column or row

To handle return more than one row or column with INDEX, see the [approach described here](https://exceljet.net/formulas/return-array-with-index-function)
 to "dereference" INDEX.

Related formulas
----------------

[![Excel formula: Lookup and sum column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Lookup%20and%20sum%20column.png "Excel formula: Lookup and sum column")](https://exceljet.net/formulas/lookup-and-sum-column)

### [Lookup and sum column](https://exceljet.net/formulas/lookup-and-sum-column)

The core of this formula uses the INDEX and MATCH function in a special way to return a full column instead of a single value. Working from the inside out, the MATCH function is used to find the correct column number for the fruit in I6: MATCH(I6,C4:F4,0) MATCH return 2 inside the INDEX function as...

[![Excel formula: Return array with INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/return%20array%20with%20INDEX%20function.png "Excel formula: Return array with INDEX function")](https://exceljet.net/formulas/return-array-with-index-function)

### [Return array with INDEX function](https://exceljet.net/formulas/return-array-with-index-function)

It is surprisingly tricky to get INDEX to return more than one value to another function. To illustrate, the following formula can be used to return the first three items in the named range "data", when entered as a multi-cell array formula. {=INDEX(data,{1,2,3})} The results can be seen in the...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Lookup and sum column](https://exceljet.net/formulas/lookup-and-sum-column)
    
*   [Return array with INDEX function](https://exceljet.net/formulas/return-array-with-index-function)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

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