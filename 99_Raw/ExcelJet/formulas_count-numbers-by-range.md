# Count numbers by range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-numbers-by-range

---

[Skip to main content](https://exceljet.net/formulas/count-numbers-by-range#main-content)

[](https://exceljet.net/formulas/count-numbers-by-range#)

*   [Previous](https://exceljet.net/formulas/count-numbers-by-nth-digit)
    
*   [Next](https://exceljet.net/formulas/count-numbers-that-begin-with)
    

[Count](https://exceljet.net/formulas#Count)

Count numbers by range
======================

by Dave Bruns · Updated 21 Aug 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[FREQUENCY](https://exceljet.net/functions/frequency-function)

[DROP](https://exceljet.net/functions/drop-function)

![Excel formula: Count numbers by range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20numbers%20by%20range.png "Excel formula: Count numbers by range")

Summary
-------

To count numeric data in specific ranges or brackets, you can use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. In the example shown, the formula in G5, copied down, is:

    =COUNTIFS(data[Age],">="&E5,data[Age],"<="&F5)
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:C16. As the formula is copied down, it returns a new count in each row using the Start and End values in columns E and F to determine a count.

Generic formula
---------------

    =COUNTIFS(range,">=low",range,"<=high")
    

Explanation 
------------

In this example, the goal is to count ages in column C according to the brackets defined in columns E and F. All data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data** defined in the range B5:C16. A simple way to solve this problem is with the COUNTIFS function. If you are using Excel 365 or Excel 2021, another easy way to solve this problem is with the FREQUENCY function. Both approaches are explained below.

### COUNTIFS function

The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 returns the count of cells that meet one or more criteria, and supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. Conditions are supplied to COUNTIFS in the form of _range/criteria_ pairs — each pair contains one range and the associated criteria for that range:

    =COUNTIFS(range1,criteria1,range2,criteria2,etc)
    

Using this pattern we can count ages in brackets like this:

    =COUNTIFS(data[Age],">=20",data[Age],"<=29") // 20-29
    =COUNTIFS(data[Age],">=30",data[Age],"<=39") // 30-39
    =COUNTIFS(data[Age],">=40",data[Age],"<=49") // 40-49
    

We are using the [structured reference](https://exceljet.net/glossary/structured-reference)
 **data\[Age\]** for both ranges, since **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
. Using an Excel Table means the table will expand automatically as new rows are added, and the counts will remain up to date.

Notice in the formulas above, we are hardcoding the numbers into the formula. This is generally considered a bad practice, since it's easy to make a mistake when entering the formula and it's more difficult to adjust the ranges later if needed, especially since each age bracket has its own unique formula. A better approach is to use ages already on the worksheet in columns E and F.

To do this, we need to [concatenate](https://exceljet.net/glossary/concatenation)
 the ages in columns E and F to the [logical operators](https://exceljet.net/glossary/logical-operators)
 >= and <=. The final formula in G5 looks like this:

    =COUNTIFS(data[Age],">="&E5,data[Age],"<="&F5)
    

Notice the operators are enclosed in double quotes ("") and attached to cell references E5 and F5 with an ampersand character (&). For a detailed overview of concatenation, see [How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
. As this formula is copied down, the reference to **data\[Age\]** behaves like an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 and does not change, which means we can use the same formula for all five age brackets.

If you need a final bracket that captures all ages above 70, you can use a single condition like this:

    =COUNTIFS(data[Age],">=70") // 70+
    

This formula will return a count of all ages greater than or equal to 70.

### FREQUENCY function

If you are using [Excel 365](https://exceljet.net/glossary/excel-365)
 or Excel 2021, where [array formulas are native](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, a nice way to solve this problem is with the [FREQUENCY function](https://exceljet.net/functions/frequency-function)
. The FREQUENCY function returns more than one value at a time and needs to be entered as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
 in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
. In modern Excel, you can simply use a formula like this in cell G5:

    FREQUENCY(data[Age],F5:F9)
    

Here, the _data\_array_ is given as **data\[Age\]** and the _bins\_array_ is given as F5:F9, the "End" values in column F. The FREQUENCY function performs the calculation and returns an [array](https://exceljet.net/glossary/array)
 like this:

    {3;3;1;3;2;0}
    

Each number represents a count, and the results automatically [spill](https://exceljet.net/glossary/spill)
 into multiple cells. Notice that by design, the FREQUENCY function always returns a count for _one more bin_ than is provided. This is called the overflow bin, and represents the count of any values greater than the largest value in the _bins\_array_. To suppress this last count, you can [nest](https://exceljet.net/glossary/nesting)
 the FREQUENCY function inside the [DROP function](https://exceljet.net/functions/drop-function)
 like this:

    =DROP(FREQUENCY(data[Age],F5:F9),-1)
    

The DROP function will remove the last row in the array returned by FREQUENCY and the result will match the values returned by COUNTIFS above.

### With a Pivot Table

A [Pivot Table](https://exceljet.net/articles/excel-pivot-tables)
 is another way to solve this problem. See [this video for a similar example](https://exceljet.net/videos/how-to-group-a-pivot-table-by-age-range)
.

Related formulas
----------------

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel FREQUENCY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20frequency%20function.png "Excel FREQUENCY function")](https://exceljet.net/functions/frequency-function)

### [FREQUENCY Function](https://exceljet.net/functions/frequency-function)

The Excel FREQUENCY function returns a frequency distribution, which is a list that shows the frequency of values at given intervals. FREQUENCY returns multiple values and must be entered as an [array formula](https://exceljet.net/glossary/array-formula)
 with control-shift-enter, except in...

[![Excel DROP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")](https://exceljet.net/functions/drop-function)

### [DROP Function](https://exceljet.net/functions/drop-function)

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20group%20a%20pivot%20table%20by%20age%20range-play.png)](https://exceljet.net/videos/how-to-group-a-pivot-table-by-age-range)

### [How to group a pivot table by age range](https://exceljet.net/videos/how-to-group-a-pivot-table-by-age-range)

One of the most powerful features of pivot tables is their ability to group data, especially by number or date. In this video, I'll show you how to group data by age range. Here we have a set of data that represents voting results. There are 300 results total, and, in each row, we have name, gender...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)
    
*   [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [FREQUENCY Function](https://exceljet.net/functions/frequency-function)
    
*   [DROP Function](https://exceljet.net/functions/drop-function)
    

### Videos

*   [How to group a pivot table by age range](https://exceljet.net/videos/how-to-group-a-pivot-table-by-age-range)
    

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