# Dynamic two-way count - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-two-way-count

---

[Skip to main content](https://exceljet.net/formulas/dynamic-two-way-count#main-content)

[](https://exceljet.net/formulas/dynamic-two-way-count#)

*   [Previous](https://exceljet.net/formulas/dynamic-two-way-average)
    
*   [Next](https://exceljet.net/formulas/dynamic-two-way-sum)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Dynamic two-way count
=====================

by Dave Bruns · Updated 4 Oct 2023

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[LET](https://exceljet.net/functions/let-function)

[HSTACK](https://exceljet.net/functions/hstack-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6974/download?token=8l0IPbCV)
 (15.5 KB)

![Excel formula: Dynamic two-way count](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/dynamic%20two%20way%20count.png "Excel formula: Dynamic two-way count")

Summary
-------

To perform a dynamic two-way count with a formula, you can use an [Excel Table](https://exceljet.net/glossary/excel-table)
, the [UNIQUE function](https://exceljet.net/functions/unique-function)
, and the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 connected to the [spill ranges](https://exceljet.net/glossary/spill-range)
 returned by UNIQUE. In the example shown, the formula in cell G5 is:

    =COUNTIFS(data[Color],F5#,data[Size],G4#)
    

Where **data** is an Excel Table based on the data in B5:D16. The result from COUNTIFS spills into the range G5:I9. Note the result from COUNTIFS is a _count of records_ that meet criteria. [See below](https://exceljet.net/formulas/dynamic-two-way-count#dynamic_two_way_sum)
 for a formula to _sum the Qty column_ using the same criteria.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are only available in [Excel 365](https://exceljet.net/glossary/excel-365)
>  and Excel 2021. 

Generic formula
---------------

    =COUNTIFS(table[column1],spill1#,table[column2],spill2#)

Explanation 
------------

In this example, the goal is to create a formula that performs a dynamic two-way count of all color and size combinations in the range B5:D16. The solution shown requires four general steps:

1.  Create an [Excel Table](https://exceljet.net/glossary/excel-table)
     called **data**
2.  List unique colors with [UNIQUE function](https://exceljet.net/functions/unique-function)
    
3.  List unique sizes with [UNIQUE function](https://exceljet.net/functions/unique-function)
    
4.  Generate counts in [COUNTIFS function](https://exceljet.net/functions/countifs-function)
    

### Create the Excel Table

One of the key benefits of an [Excel Table](https://exceljet.net/articles/excel-tables)
 is its ability to resize when rows are added or removed. In this case, all we need to do is create a new table named **data** with the data shown in B5:D16. 

Video: [How to create an Excel table](https://exceljet.net/videos/how-to-create-an-excel-table)

The table will now automatically expand or contract as needed.

### List unique colors

The next step is to list the unique colors in the "Color" column starting in cell F5. For this we use the [UNIQUE function](https://exceljet.net/functions/unique-function)
. The formula in F5 is:

    =UNIQUE(data[Color]) // unique colors
    

This is what makes this solution dynamic. The UNIQUE function will continue to output a list of unique colors, even when data in the table changes. 

Video: [Intro to the UNIQUE function](https://exceljet.net/videos/the-unique-function)

### List unique sizes

Two perform a two-way count, we also need a list of unique sizes starting in cell G4. We can do this with a formula just like the one we used for colors:

    UNIQUE(data[Size]) // unique sizes
    

However, unlike colors, we need this list to run _horizontally_. To change the output from vertical to horizontal, we nest the UNIQUE formula in the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
. The formula in G4 is:

    =TRANSPOSE(UNIQUE(data[Size])) // horizontal array
    

The UNIQUE function returns a vertical [array](https://exceljet.net/glossary/array)
 like this:

    {"L";"M";"S"}
    

And the TRANSPOSE function converts this array into a horizontal array like this:

    {"L","M","S"}
    

Note the commas instead of semicolons in the second array.

Video: [What is an array](https://exceljet.net/videos/what-is-an-array)
?

### Calculate unique counts

We now have what we need to calculate the counts. Because we have both unique sizes and unique colors on the worksheet as [spill ranges](https://exceljet.net/glossary/spill-range)
, we can use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 for this task. The formula in G5 is:

    =COUNTIFS(data[Color],F5#,data[Size],G4#)
    

With COUNTIFS, conditions are entered in _range/criteria_ pairs. The first pair targets colors:

    data[Color],F5# // all colors, unique colors
    

The second _range/criteria_ pair targets sizes:

    data[Size],G4# // all sizes, unique sizes
    

### When data changes

The key advantage to this formula approach is that it instantly responds to changes in the data. If new rows are added that refer to _existing_ colors and sizes, the [spill ranges](https://exceljet.net/glossary/spill-range)
 returned by COUNTIFS are unchanged, and COUNTIFS simply returns an updated set of counts. If new rows are added that include _new_ colors and/or _new_ sizes, these are captured by the UNIQUE function, which expands the spill ranges as needed. If rows are deleted from the table, spill ranges contract if needed. In all cases, the spill ranges represent the current list of unique colors and sizes, and the COUNTIFS function uses these values to return a current set of counts.

### All in one formula

In the latest version of Excel, we can use the [LET function](https://exceljet.net/functions/let-function)
 and two new functions, [HSTACK](https://exceljet.net/functions/hstack-function)
 and [VSTACK](https://exceljet.net/functions/vstack-function)
, to write a _single_ all-in-one formula that builds a complete summary table like this:

    =LET(
      colors,UNIQUE(data[Color]),
      sizes,TRANSPOSE(UNIQUE(data[Size])),
      counts,COUNTIFS(data[Color],colors,data[Size],sizes),
      HSTACK(VSTACK({"Color"},colors),VSTACK(sizes,counts))
    )
    

_Note: VSTACK and HSTACK are still in beta, available via the Beta Channel for Excel 365._

In a nutshell, we use the UNIQUE function to extract unique colors and sizes, and the COUNTIFS function to generate all counts. The [LET function](https://exceljet.net/functions/let-function)
 is used to assign all three of these results to the variables _colors_, _sizes_, and _counts_. Then, we use the [HSTACK](https://exceljet.net/functions/hstack-function)
 and [VSTACK](https://exceljet.net/functions/vstack-function)
 functions to assemble the final table. Because HSTACK is the last function to run, it returns the final result, which is an [array](https://exceljet.net/glossary/array)
 of values that [spills](https://exceljet.net/glossary/spill)
 into multiple cells. For more information on LET, [this example](https://exceljet.net/formulas/detailed-let-function-example)
 walks through using the LET function in detail.

The formula above is a great example of how dynamic array formulas will completely change formula solutions in the future. 

### Pivot Table option

A [pivot table](https://exceljet.net/articles/excel-pivot-tables)
 would also be an [excellent way to solve this problem](https://exceljet.net/pivot-tables/pivot-table-two-way-count)
, and would provide additional capabilities. However, one drawback is that pivot tables need to be refreshed to show the latest data. Formulas, on the other hand, update instantly when data changes.

### Dynamic two-way sum

The example above performs a dynamic two-way _count_. However, you can easily create a dynamic two-way _sum_ with the same approach. To calculate a two-way sum on the Qty column, simply replace COUNTIFS with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
:

    =SUMIFS(data[Qty],data[Color],F5#,data[Size],G4#)
    

![Dynamic two-way sum with SUMIFS](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/dynamic%20two%20way%20sum.png?itok=YqGqdnO8 "Dynamic two-way sum with SUMIFS")

Notice the SUMIFS function takes an extra (first) [argument](https://exceljet.net/glossary/function-argument)
, _sum\_range_, which specifies the range to sum. The _range/criteria_ pairs used to target color and size combinations are the same as that used in the COUNTIFS formula. [Detailed walkthrough here](https://exceljet.net/formulas/dynamic-two-way-sum)
.

### Non-dynamic solution

If you are using an older version of Excel without the UNIQUE function, you can still build a non-dynamic count with the COUNTIFS function. See this video: [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
 and [this formula](https://exceljet.net/formulas/two-way-summary-count)
.

### Dynamic Array Training

Need structured training for dynamic arrays in Excel? See our course: [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
.

Related formulas
----------------

[![Excel formula: Dynamic two-way average](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20average.png "Excel formula: Dynamic two-way average")](https://exceljet.net/formulas/dynamic-two-way-average)

### [Dynamic two-way average](https://exceljet.net/formulas/dynamic-two-way-average)

In this example, the goal is to create a formula that performs a dynamic two-way average of all age and gender combinations in the range B5:D16 . The solution shown requires four general steps: Create an Excel Table called data List unique age groups with UNIQUE function List unique genders with...

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

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Dynamic two-way average](https://exceljet.net/formulas/dynamic-two-way-average)
    
*   [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    

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