# Dynamic named range with INDEX - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-named-range-with-index

---

[Skip to main content](https://exceljet.net/formulas/dynamic-named-range-with-index#main-content)

[](https://exceljet.net/formulas/dynamic-named-range-with-index#)

*   [Previous](https://exceljet.net/formulas/define-range-based-on-cell-value)
    
*   [Next](https://exceljet.net/formulas/dynamic-named-range-with-offset)
    

[Range](https://exceljet.net/formulas#Range)

Dynamic named range with INDEX
==============================

by Dave Bruns · Updated 6 Feb 2025

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[COUNTA](https://exceljet.net/functions/counta-function)

[TRIMRANGE](https://exceljet.net/functions/trimrange-function)

![Excel formula: Dynamic named range with INDEX](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/dynamic%20named%20range%20with%20index1.png "Excel formula: Dynamic named range with INDEX")

Summary
-------

One way to create a [dynamic named range](https://exceljet.net/glossary/dynamic-named-range)
 in Excel is to use the [INDEX function](https://exceljet.net/functions/index-function)
.  In the example shown, the named range "data" is defined by the following formula:

    =$A$2:INDEX($A:$A,COUNTA($A:$A))
    

This formula resolves to the range $A$2:$A$10.

> Note: this formula is meant to define a [named range](https://exceljet.net/articles/named-ranges)
>  that can be used in other formulas. This range will be dynamic and expand and shrink with the data. An alternative to a formula-based dynamic named range is to use an [Excel Table](https://exceljet.net/articles/excel-tables)
> . If you are using Excel 365 another option is to use the [TRIMRANGE function](https://exceljet.net/functions/trimrange-function)
> , which is designed to create dynamic ranges.

Generic formula
---------------

    =$A$1:INDEX($A:$A,lastrow)

Explanation 
------------

This page shows an example of a [dynamic named range](https://exceljet.net/glossary/dynamic-named-range)
 created with the INDEX function together with the COUNTA function. Dynamic named ranges automatically expand and contract when data is added or removed. They are an alternative to using an [Excel Table](https://exceljet.net/glossary/excel-table)
, which also resizes as data is added or removed.

The [INDEX function](https://exceljet.net/functions/index-function)
 returns the value at a given position in a range or array. You can use INDEX to retrieve individual values or entire rows and columns in a range. What makes INDEX especially useful for dynamic named ranges is that it actually returns a reference. This means you can use INDEX to construct a [mixed reference](https://exceljet.net/glossary/mixed-reference)
 like $A$1:A100.

In the example shown, the named range "data" is defined by the following formula:

    =$A$2:INDEX($A:$A,COUNTA($A:$A))
    

which resolves to the range $A$2:$A$10. 

### How this formula works

Note first that this formula is composed of two parts that sit on either side of the range operator (:). On the left, we have the starting reference for the range, hard coded as:

    $A$2
    

On the right is the ending reference for the range, created with INDEX like this:

    INDEX($A:$A,COUNTA($A:$A))
    

Here, we feed INDEX all of column A for the array, then use the [COUNTA function](https://exceljet.net/functions/counta-function)
 to figure out the "last row" in the range. COUNTA works well here because there are 10 values in column A, including a header row. COUNTA therefore returns 10, which goes directly into INDEX as the row number. INDEX then returns a reference to $A$10, the last used row in the range:

    INDEX($A:$A,10) // resolves to $A$10
    

So, the final result of the formula is this range:

    $A$2:$A$10
    

### A two-dimensional range

The above example works for a one-dimensional range. To create a two-dimensional dynamic range where the number of columns is also dynamic, you can use the same approach, expanded like this:

    =$A$2:INDEX($1:$1048576,COUNTA($A:$A),COUNTA($1:$1))
    

![Example of two-dimensional dynamic range with INDEX](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/dynamic%20named%20range%20with%20index2.png?itok=rId5OuaC "Example of two-dimensional dynamic range with INDEX")

As before, COUNTA is used to figure out the "lastrow", and we use COUNTA again to get the "lastcolumn". These are supplied to INDEX as row\_num and column\_num respectively.

However, for the array, we supply the full worksheet, entered as all 1048576 rows, which allows INDEX to return a reference in a 2D space.

### Determining the last row

There are several ways to determine the last row (last relative position) in a set of data, depending on the structure and content of the data in the worksheet:

*   [Last row in mixed data with blanks](https://exceljet.net/formulas/last-row-in-mixed-data-with-blanks)
    
*   [Last row in mixed data with no blanks](https://exceljet.net/formulas/last-row-in-mixed-data-with-no-blanks)
    
*   [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)
    
*   [Last row in numeric data](https://exceljet.net/formulas/last-row-in-numeric-data)
    

Related formulas
----------------

[![Excel formula: Dynamic named range with OFFSET](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20named%20range%20with%20offset.png "Excel formula: Dynamic named range with OFFSET")](https://exceljet.net/formulas/dynamic-named-range-with-offset)

### [Dynamic named range with OFFSET](https://exceljet.net/formulas/dynamic-named-range-with-offset)

Dynamic ranges are also known as expanding ranges because they automatically expand and contract to accommodate new or deleted data. You can see a video demo of this approach here . This formula uses the OFFSET function to generate a range that expands and contracts by adjusting height and width...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel TRIMRANGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_trimrange_function.png "Excel TRIMRANGE function")](https://exceljet.net/functions/trimrange-function)

### [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)

The Excel TRIMRANGE function removes empty rows and columns from the outer edges of a range of data. The result is a "trimmed" range that only includes data from the used portion of the range. Because it is a formula, TRIMRANGE will update the range dynamically when data is added or removed...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20dynamic%20named%20range%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-index)

### [How to create a dynamic named range with INDEX](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-index)

In this video we'll look at how to create a dynamic named range with the INDEX function . Unlike INDIRECT and OFFSET , INDEX is a non-volatile function. This means that INDEX will not recalculate whenever a change is made to a worksheet. This makes INDEX ideal for professional models and for...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Dynamic named range with OFFSET](https://exceljet.net/formulas/dynamic-named-range-with-offset)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)
    

### Videos

*   [How to create a dynamic named range with INDEX](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-index)
    

### Articles

*   [Named Ranges in Excel](https://exceljet.net/articles/named-ranges)
    

### Links

*   [The Imposing INDEX (fantastic article by Daniel Ferry)](http://www.excelhero.com/blog/2011/03/the-imposing-index.html)
    

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