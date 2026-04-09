# Dynamic two-way average - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-two-way-average

---

[Skip to main content](https://exceljet.net/formulas/dynamic-two-way-average#main-content)

[](https://exceljet.net/formulas/dynamic-two-way-average#)

*   [Previous](https://exceljet.net/formulas/dynamic-summary-count)
    
*   [Next](https://exceljet.net/formulas/dynamic-two-way-count)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Dynamic two-way average
=======================

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

![Excel formula: Dynamic two-way average](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/dynamic%20two%20way%20average.png "Excel formula: Dynamic two-way average")

Summary
-------

To perform a dynamic two-way average with a formula, you can use an [Excel Table](https://exceljet.net/glossary/excel-table)
, the [UNIQUE function](https://exceljet.net/functions/unique-function)
, and the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
 connected to the [spill ranges](https://exceljet.net/glossary/spill-range)
 returned by UNIQUE. In the example shown, the formula in cell G5 is:

    =AVERAGEIFS(data[Rating],data[Age],F5#,data[Gender],G4#)
    

Where **data** is an Excel Table based on the data in B5:D16. The result from AVERAGEIFS [spills](https://exceljet.net/glossary/spill)
 into the range G5:H7. 

_Note: [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 are only available in [Excel 365](https://exceljet.net/glossary/excel-365)
 and Excel 2021._ 

Generic formula
---------------

    =AVERAGEIFS(table[col],table[col],spill1#,table[col],spill2#)

Explanation 
------------

In this example, the goal is to create a formula that performs a dynamic two-way average of all age and gender combinations in the range B5:D16 . The solution shown requires four general steps:

1.  Create an [Excel Table](https://exceljet.net/glossary/excel-table)
     called **data**
2.  List unique age groups with [UNIQUE function](https://exceljet.net/functions/unique-function)
    
3.  List unique genders with [UNIQUE function](https://exceljet.net/functions/unique-function)
    
4.  Generate all averages in [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
    

### Create the Excel Table

One of the key features of an [Excel Table](https://exceljet.net/articles/excel-tables)
 is its ability to dynamically resize when rows are added or removed. In this case, all we need to do is create a new table named **data** with the data shown in B5:D16.  You can use the [keyboard shortcut Control + T](https://exceljet.net/shortcuts/insert-table)
.

Video: [How to create an Excel table](https://exceljet.net/videos/how-to-create-an-excel-table)

The table will now automatically expand or contract as needed.

### List unique age groups

The next step is to list the unique age groups in the "Age" column starting in cell F5. For this we use the [UNIQUE function](https://exceljet.net/functions/unique-function)
. The formula in F5 is:

    =UNIQUE(data[Age]) // unique age groups
    

The result from UNIQUE is a spill range starting in cell F5 listing all of the unique age groups in the Age column of the table. This is what makes this solution fully dynamic. The UNIQUE function will continue to output a list of unique age groups, even as data in the table changes. 

Video: [Intro to the UNIQUE function](https://exceljet.net/videos/the-unique-function)

### List unique genders

Two perform a two-way average, we also need a list of unique genders starting in cell G4. We can do this with a formula like the one we used for age groups:

    UNIQUE(data[Gender]) // unique genders
    

However, unlike age groups, we need this list to run _horizontally_ across the top of the averages_._ To change the output from vertical to horizontal, we [nest](https://exceljet.net/glossary/nesting)
 the UNIQUE formula in the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
. The final formula in G4 is:

    =TRANSPOSE(UNIQUE(data[Gender])) // horizontal array
    

The UNIQUE function returns a vertical [array](https://exceljet.net/glossary/array)
 like this:

    {"Male";"Female"}
    

And the TRANSPOSE function converts this array into a horizontal array like this:

    {"Male","Female"}
    

Note the comma instead of semicolon in the second array. The UNIQUE function will continue to output a list of unique genders, even if data in the table changes. 

Video: [What is an array](https://exceljet.net/videos/what-is-an-array)
?

### Calculate unique averages

We now have what we need to calculate the averages. Because we have both unique age groups and unique genders on the worksheet as [spill ranges](https://exceljet.net/glossary/spill-range)
, we can use the AVERAGEIFS function for this task. The formula in G5 is:

    =AVERAGEIFS(data[Rating],data[Age],F5#,data[Gender],G4#)
    

The first [argument](https://exceljet.net/glossary/function-argument)
 in AVERAGEIFS is _average\_range_. This is the range that contains numbers to average. In this example, this is the Rating column in the table:

    data[Rating] // average_range
    

The other arguments are _range/criteria_ pairs. The first pair targets ages:

    data[Age],F5# // all ages, unique ages
    

The second _range/criteria_ pair targets gender:

    data[Gender],G4# // all genders, unique genders
    

### When data changes

The key advantage to this formula approach is that it responds instantly to changes in the data. If new rows are added that refer to _existing_ age groups and genders, the [spill ranges](https://exceljet.net/glossary/spill-range)
 returned by AVERAGEIFS remain unchanged, and AVERAGEIFS simply returns an updated set of averages. If new rows are added that include _new_ age groups and/or _new_ genders, these are captured by the UNIQUE function, which expands the spill ranges in F5 and G4 as needed. If rows are deleted from the table, spill ranges contract as needed. In all cases, the spill ranges represent the current list of unique age groups and genders, and the AVERAGEIFS function uses these values to return a current set of averages.

### Pivot Table option

A [pivot table](https://exceljet.net/articles/excel-pivot-tables)
 would also be a [good way to solve this problem](https://exceljet.net/pivot-tables/pivot-table-two-way-average)
, and would provide additional capabilities. However, one drawback is that pivot tables need to be refreshed to show the latest data. Formulas, on the other hand, update instantly when data changes.

### Dynamic Array Training

If you need training for dynamic arrays in Excel, see our course: [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
.

Related formulas
----------------

[![Excel formula: Dynamic two-way count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20count.png "Excel formula: Dynamic two-way count")](https://exceljet.net/formulas/dynamic-two-way-count)

### [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)

In this example, the goal is to create a formula that performs a dynamic two-way count of all color and size combinations in the range B5:D16. The solution shown requires four general steps: Create an Excel Table called data List unique colors with UNIQUE function List unique sizes with UNIQUE...

[![Excel formula: Dynamic two-way sum](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20sum.png "Excel formula: Dynamic two-way sum")](https://exceljet.net/formulas/dynamic-two-way-sum)

### [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)

In this example, the goal is to create a formula that performs a dynamic two-way sum of all City and Size combinations in the range B5:D17 . The solution shown requires four basic steps: Create an Excel Table called data List unique cities with the UNIQUE function List unique sizes with the UNIQUE...

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
    
*   [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)
    

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