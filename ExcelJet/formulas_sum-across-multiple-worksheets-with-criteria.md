# Sum across multiple worksheets with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria#main-content)

[](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria#)

*   [Previous](https://exceljet.net/formulas/sum-across-multiple-worksheets)
    
*   [Next](https://exceljet.net/formulas/sum-and-ignore-errors)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum across multiple worksheets with criteria
============================================

by Dave Bruns · Updated 28 Feb 2025

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[SUMIF](https://exceljet.net/functions/sumif-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Sum across multiple worksheets with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20across%20multiple%20worksheets%20with%20criteria.png "Excel formula: Sum across multiple worksheets with criteria")

Summary
-------

To conditionally sum identical ranges in separate worksheets, you can use a formula based on the [SUMIF function](https://exceljet.net/functions/sumif-function)
, the [INDIRECT function](https://exceljet.net/functions/indirect-function)
, and the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in F5 is:

    =SUMPRODUCT(SUMIF(INDIRECT("'"&sheets&"'!"&"D5:D16"),E5,INDIRECT("'"&sheets&"'!"&"E5:E16")))
    

where **sheets** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B7. As the formula is copied down, it returns total hours in Sheet1, Sheet2, and Sheet3 for the projects shown in column E.

_Note: you might wonder why we don't use the SUMIF function with a 3D reference to sum multiple worksheets with criteria? The problem is that SUMIFS, COUNTIFS, AVERAGEIFS, etc. are in a [group of functions](https://exceljet.net/articles/excels-racon-functions)
 that do not support 3D references._

Generic formula
---------------

    =SUMPRODUCT(SUMIF(INDIRECT("'"&sheets&"'!"&"rng"),criteria,INDIRECT("'"&sheets&"'!"&"sum_rng")))

Explanation 
------------

In this example, the goal is to sum hours per project across three different worksheets: Sheet1, Sheet2, and Sheet3. The data on each of the three sheets has the same structure as Sheet1, as seen below:

![Example of data structure on Sheet1](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sum%20across%20multiple%20worksheets%20with%20criteria%20sheet1.png?itok=32MeWJ0i "Example of data structure on Sheet1")

### 3D reference won't work

Before we look at a solution, let's look at something that doesn't work. You might wonder if we can provide the [SUMIF function](https://exceljet.net/functions/sumif-function)
 with a 3D reference like this:

    Sheet1:Sheet3!D5:D16
    

This is the standard 3D reference syntax, but if you try to use it with SUMIF, you'll get a #VALUE error.  The problem is that SUMIFS, COUNTIFS, AVERAGEIFS, etc. are in a [group of functions](https://exceljet.net/articles/excels-racon-functions)
 that do not support 3D references.

### Workaround with INDIRECT

To workaround this problem we can use a [named range](https://exceljet.net/glossary/named-range)
 "sheets" that holds the name of each worksheet that should be included in the calculation. In the example shown, **sheets** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B7, which holds three values: "Sheet1", "Sheet2", and "Sheet3". The formula in F5 is:

    =SUMPRODUCT(SUMIF(INDIRECT("'"&sheets&"'!"&"D5:D16"),E5,INDIRECT("'"&sheets&"'!"&"E5:E16")))
    

Notice we are [concatenating](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the sheet names to the ranges we need to work with. Once the concatenation is performed, the formula looks like this:

    =SUMPRODUCT(SUMIF(INDIRECT({"'Sheet1'!D5:D16";"'Sheet2'!D5:D16";"'Sheet3'!D5:D16"}),E5,INDIRECT({"'Sheet1'!E5:E16";"'Sheet2'!E5:E16";"'Sheet3'!E5:E16"})))
    

Notice we now have complete references based on the three sheet names provided in **sheets** (B5:B7). However, because we assembled these references with concatenation, these values are not actual cell references but are in fact _text values_. To coerce these values into valid cell references we use the [INDIRECT function](https://exceljet.net/functions/indirect-function)
.

INDIRECT converts the text values to valid references and returns the result to the SUMIF function for the _range_ and _sum\_range_ arguments. The value for _criteria_ is provided by the reference to cell E5 ("Alpha"), which changes as the formula is copied down the column. Because the [named range](https://exceljet.net/glossary/named-range)
 "sheets" contains _three_ values, SUMIF actually runs _three_ times, one for each reference. The result is an [array](https://exceljet.net/glossary/array)
 with three results like this:

    {24;20;20}
    

This array is returned directly to the SUMPRODUCT function:

    =SUMPRODUCT({24;20;20})
    

With a single array to process, SUMPRODUCT sums the array and returns 64 for the Alpha project in cell F5. This number is the total number of hours logged to the Alpha project in all three worksheets. As the formula is copied down, it returns a total for each project shown in column E.

_Note: In the latest version of Excel, you can use the [SUM function](https://exceljet.net/functions/sum-function)
 instead of the SUMPRODUCT function with the same result. In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, [SUMPRODUCT is used frequently](https://exceljet.net/articles/why-sumproduct)
 because it can handle [arrays](https://exceljet.net/glossary/array)
 natively without requiring Ctrl-Shift-Enter._

Related formulas
----------------

[![Excel formula: Sum across multiple worksheets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sum%20across%20multiple%20worksheets.png "Excel formula: Sum across multiple worksheets")](https://exceljet.net/formulas/sum-across-multiple-worksheets)

### [Sum across multiple worksheets](https://exceljet.net/formulas/sum-across-multiple-worksheets)

In this example, the goal is to sum total points for each student across five worksheets that all have the same structure. This can be accomplished with a 3D reference, as explained below. Standard reference Before we look at how 3D references work, let's look at the standard approach. To solve...

[![Excel formula: Lookup with variable sheet name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup_with_variable_sheet_name.png "Excel formula: Lookup with variable sheet name")](https://exceljet.net/formulas/lookup-with-variable-sheet-name)

### [Lookup with variable sheet name](https://exceljet.net/formulas/lookup-with-variable-sheet-name)

In this example, the goal is to create a lookup formula with a variable sheet name. In other words, a formula that uses a sheet name typed into a cell to construct a reference to a range on that sheet. If the sheet name is changed, the reference should update automatically. The key to the solution...

[![Excel formula: VLOOKUP with variable table array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20variable%20table%20array.png "Excel formula: VLOOKUP with variable table array")](https://exceljet.net/formulas/vlookup-with-variable-table-array)

### [VLOOKUP with variable table array](https://exceljet.net/formulas/vlookup-with-variable-table-array)

In this example, the goal is to set up VLOOKUP to retrieve costs based on a variable vendor name. In other words, we want a formula that allows us to switch tables dynamically based on a user-supplied value. There are two cost tables in the worksheet, one for Vendor A and one for Vendor B. Both...

[![Excel formula: Sum if with multiple ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sum_if_with_multiple_ranges.png "Excel formula: Sum if with multiple ranges")](https://exceljet.net/formulas/sum-if-with-multiple-ranges)

### [Sum if with multiple ranges](https://exceljet.net/formulas/sum-if-with-multiple-ranges)

In this example, the goal is to calculate a total quantity for each color across the two ranges shown in the worksheet. The two ranges are "non-contiguous", which means they are not connected or touching. Both ranges contain a list of colors in the first column and quantities in the second column...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%203d%20references-thumb.png)](https://exceljet.net/videos/how-to-create-3d-references)

### [How to create 3D references](https://exceljet.net/videos/how-to-create-3d-references)

Sometimes in Excel you may want to reference a large number of sheets that have the same structure. In this case, you can use a special trick called a "3D reference". Here are the test scores we looked at earlier. The Summary sheet is pulling in the results from Week1 through Week5. Suppose we want...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum across multiple worksheets](https://exceljet.net/formulas/sum-across-multiple-worksheets)
    
*   [Lookup with variable sheet name](https://exceljet.net/formulas/lookup-with-variable-sheet-name)
    
*   [VLOOKUP with variable table array](https://exceljet.net/formulas/vlookup-with-variable-table-array)
    
*   [Sum if with multiple ranges](https://exceljet.net/formulas/sum-if-with-multiple-ranges)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    

### Videos

*   [How to create 3D references](https://exceljet.net/videos/how-to-create-3d-references)
    

### Links

*   [Mr Excel discussion](http://www.mrexcel.com/forum/excel-questions/549723-sumif-across-sheets-without-indirect.html)
    

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