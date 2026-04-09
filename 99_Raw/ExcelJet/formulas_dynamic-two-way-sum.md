# Dynamic two-way sum - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-two-way-sum

---

[Skip to main content](https://exceljet.net/formulas/dynamic-two-way-sum#main-content)

[](https://exceljet.net/formulas/dynamic-two-way-sum#)

*   [Previous](https://exceljet.net/formulas/dynamic-two-way-count)
    
*   [Next](https://exceljet.net/formulas/extract-common-values-from-text-strings)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Dynamic two-way sum
===================

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6987/download?token=6b5eOpWO)
 (15.9 KB)

![Excel formula: Dynamic two-way sum](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/dynamic%20two%20way%20sum.png "Excel formula: Dynamic two-way sum")

Summary
-------

To perform a dynamic two-way sum with a formula, you can use an [Excel Table](https://exceljet.net/glossary/excel-table)
, the [UNIQUE function](https://exceljet.net/functions/unique-function)
, and the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 connected to the [spill ranges](https://exceljet.net/glossary/spill-range)
 returned by UNIQUE. In the example shown, the formula in cell G5 is:

    =SUMIFS(data[Qty],data[City],F5#,data[Size],G4#)
    

Where **data** is an Excel Table based on the data in B5:D17. The result from SUMIF [spills](https://exceljet.net/glossary/spill)
 into the range G5:I9, and the results show the sum of Qty for each City and Size combination.

_Note: [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 are only available in [Excel 365](https://exceljet.net/glossary/excel-365)
 and Excel 2021._ 

Generic formula
---------------

    =SUMIFS(sum_range,range1,spill1#,range2,spill2#)

Explanation 
------------

In this example, the goal is to create a formula that performs a dynamic two-way sum of all City and Size combinations in the range B5:D17 . The solution shown requires four basic steps:

1.  Create an [Excel Table](https://exceljet.net/glossary/excel-table)
     called **data**
2.  List unique cities with the [UNIQUE function](https://exceljet.net/functions/unique-function)
    
3.  List unique sizes with the [UNIQUE function](https://exceljet.net/functions/unique-function)
    
4.  Generate sums with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
    

### Create the Excel Table

One of the key features of an [Excel Table](https://exceljet.net/articles/excel-tables)
 is its ability to dynamically resize when rows are added or removed. In this case, all we need to do is create a new table named **data** with the data shown in B5:D17.  You can use the [keyboard shortcut Control + T](https://exceljet.net/shortcuts/insert-table)
.

Video: [How to create an Excel table](https://exceljet.net/videos/how-to-create-an-excel-table)

The table will now automatically expand or contract as needed.

### List unique cities

The next step is to list the unique cities in the "City" column starting in cell F5. For this we use the [UNIQUE function](https://exceljet.net/functions/unique-function)
. The formula in F5 is:

    =UNIQUE(data[City]) // unique city names
    

The result from UNIQUE is a spill range starting in cell F5 listing all of the unique city names in the City column of the table. This is what makes this solution fully dynamic. The UNIQUE function will continue to return a list of unique cities, even as data in the table changes. 

Video: [Intro to the UNIQUE function](https://exceljet.net/videos/the-unique-function)

### List unique sizes

Two perform a two-way sum, we also need a list of unique sizes starting in cell G4. We can do this with a similar formula:

    UNIQUE(data[Size]) // unique sizes
    

However, unlike cities, we need the list of sizes to run _horizontally_ across above the sums_._ To change the output from vertical to horizontal, we [nest](https://exceljet.net/glossary/nesting)
 the UNIQUE formula in the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
. The final formula in G4 is:

    =TRANSPOSE(UNIQUE(data[Size])) // horizontal array
    

The UNIQUE function returns a vertical [array](https://exceljet.net/glossary/array)
 like this:

    {"L";"M";"S"}
    

And the TRANSPOSE function converts this array into a horizontal array like this:

    {"L","M","S"}
    

Note the comma instead of a semicolon in the second array. The UNIQUE function will continue to return a list of unique sizes, even if data in the table changes and sizes are added or removed.

Video: [What is an array](https://exceljet.net/videos/what-is-an-array)
?

### Generate the sums

We now have what we need to calculate the sums. Because we have both unique cities and unique sizes on the worksheet as [spill ranges](https://exceljet.net/glossary/spill-range)
, we can use the SUMIFS function for this task. The formula in G5 is:

    =SUMIFS(data[Qty],data[City],F5#,data[Size],G4#)
    

The first [argument](https://exceljet.net/glossary/function-argument)
 in SUMIFS is _sum\_range_. This is the range that contains numbers to sum. In this example, this is the Qty column in the table:

    data[Qty] // sum_range
    

The other arguments are _range/criteria_ pairs. The first pair targets cities:

    data[City],F5# // all cities, unique cities
    

The second _range/criteria_ pair targets sizes:

    data[Size],G4# // all sizes, unique sizes
    

### When data changes

The key advantage to this formula approach is that it responds instantly to changes in the data. If new rows are added that refer to _existing_ cities and sizes, the [spill range](https://exceljet.net/glossary/spill-range)
 remains the same size, and SUMIFS simply returns an updated set of sums. If new rows are added that include _new_ cities and/or _new_ sizes, these are captured by the UNIQUE function, which expands the spill ranges in F5 and G4 as needed. Likewise, if rows are deleted from the table, spill ranges are reduced by UNIQUE as needed. In all cases, the spill ranges represent the current list of unique cities and sizes, and the SUMIFS function returns a current set of sums.

### Legacy Excel workaround

[Dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 are new in Excel 365 and Excel 2021. In legacy versions of Excel that don't support dynamic array formulas, it is still possible to compute the sums in G5:I9 with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. However, certain references must be carefully locked\* so that the formula can be copied across and down:

    =SUMIFS(data[[Qty]:[Qty]],data[[City]:[City]],$F5,data[[Size]:[Size]],G$4)
    

Since the UNIQUE function is not available in older versions of Excel, this formula requires that Cities in F5:F9 and Sizes in G4:I4 be created manually.

_\* This is a good illustration of a key benefit of dynamic array formulas: because there is just one formula, there is no need to use complicated [mixed](https://exceljet.net/glossary/mixed-reference)
 and [absolute references](https://exceljet.net/glossary/absolute-reference)
. Dynamic array formulas are therefore easier to create and maintain._

### Pivot Table option

A [pivot table](https://exceljet.net/articles/excel-pivot-tables)
 would also be a [good way to solve this problem](https://exceljet.net/pivot-tables/pivot-table-two-way-sum)
 and would provide additional capabilities. However, one drawback is that pivot tables need to be refreshed to show the latest data. Formulas, on the other hand, update instantly when data changes.

### Dynamic Array Training

If you need training for dynamic arrays in Excel, see our course: [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
.

Related formulas
----------------

[![Excel formula: Dynamic two-way count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20count.png "Excel formula: Dynamic two-way count")](https://exceljet.net/formulas/dynamic-two-way-count)

### [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)

In this example, the goal is to create a formula that performs a dynamic two-way count of all color and size combinations in the range B5:D16. The solution shown requires four general steps: Create an Excel Table called data List unique colors with UNIQUE function List unique sizes with UNIQUE...

[![Excel formula: Dynamic two-way average](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20average.png "Excel formula: Dynamic two-way average")](https://exceljet.net/formulas/dynamic-two-way-average)

### [Dynamic two-way average](https://exceljet.net/formulas/dynamic-two-way-average)

In this example, the goal is to create a formula that performs a dynamic two-way average of all age and gender combinations in the range B5:D16 . The solution shown requires four general steps: Create an Excel Table called data List unique age groups with UNIQUE function List unique genders with...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)
    
*   [Dynamic two-way average](https://exceljet.net/formulas/dynamic-two-way-average)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    
*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    

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