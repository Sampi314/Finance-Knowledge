# Two-way summary count - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/two-way-summary-count

---

[Skip to main content](https://exceljet.net/formulas/two-way-summary-count#main-content)

[](https://exceljet.net/formulas/two-way-summary-count#)

*   [Previous](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
    
*   [Next](https://exceljet.net/formulas/calculate-running-total)
    

[Count](https://exceljet.net/formulas#Count)

Two-way summary count
=====================

by Dave Bruns · Updated 6 Dec 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[LET](https://exceljet.net/functions/let-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[HSTACK](https://exceljet.net/functions/hstack-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7422/download?token=8kv8TT23)
 (20.35 KB)

![Excel formula: Two-way summary count](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Two-way%20summary%20count.png "Excel formula: Two-way summary count")

Summary
-------

To build a two-way summary count, you can use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. In the example shown, the formula in G5 is:

    =COUNTIFS(dept,$F5,group,G$4)
    

where **dept** (B5:B16) and **group** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
. The explanation below also includes a solution where source data is in an [Excel Table](https://exceljet.net/glossary/excel-table)
.

Generic formula
---------------

    =COUNTIFS(range1,criteria1,range2,criteria2)

Explanation 
------------

In this example, the goal is to count the people shown in the table by both Department (Dept) and Group as shown in the worksheet. A simple way to do this is with the COUNTIFS function.

### COUNTIFS function

The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 is designed to count things based on more than one condition. Conditions are supplied to COUNTIFS in range/criteria "pairs" like this:

    =COUNTIFS(range1,criteria1,range2,criteria2)
    

In this problem, the first step is to create the shell of the summary table that contains one set of criteria in the left-most column, and the second set of criteria in the top row as column headers like this:

![Two-way summary count criteria setup](https://exceljet.net/sites/default/files/images/formulas/inline/Two-way%20summary%20count%20criteria%20setup.png "Two-way summary count criteria setup")

The next step is to enter the COUNTIFS function in cell G5 with the first condition for Department:

    =COUNTIFS(dept,$F5
    

For _criteria\_range1_, we use the [named range](https://exceljet.net/glossary/named-range)
 **dept** (B5:B16). For _criteria1_, we use the [mixed reference](https://exceljet.net/glossary/mixed-reference)
 $F5. Cell F5 contains the value "Engineering", which will be used for criteria. We use a mixed reference to lock the column only so that the formula will still refer to column F when we copy it to the next column. We leave the row relative because we want the row to change as we copy the formula down. Note that a named range automatically behaves like an [absolute reference](https://exceljet.net/glossary/absolute-reference)
, so we don't need to do anything special with the range; it will not change when copied.

Next, we enter the second range/criteria pair to target values for Group:

    =COUNTIFS(dept,$F5,group,G$4)
    

For _criteria\_range2_, we use the [named range](https://exceljet.net/glossary/named-range)
 **group** (C5:C16). For _criteria2_, we use the [mixed reference](https://exceljet.net/glossary/mixed-reference)
 G$4. Cell G4 contains the value "A", which will be used for criteria. We use a mixed reference to lock the _row only_ so that the formula will still refer to row 4 when we copy it down.

This is the final formula entered in cell G5, and copied into the range G5:H8. To recap, the named ranges **dept** and **group** automatically behave like absolute references and will not change. The references to $F5 and G$4 however are mixed. As the formula is copied, the row in $F5 changes and the column in G$4 changes, which allows the COUNTIFS function to generate correct counts for all combinations of Department and Group.

### Excel Table option

When you use an [Excel Table](https://exceljet.net/articles/excel-tables)
 to hold source data, you get some nice benefits, including a table that automatically expands when rows are added. Excel Tables use [structured references](https://exceljet.net/glossary/structured-reference)
, which appear automatically in formulas that refer to them. In the screen below, the formula in G5 is:

    =COUNTIFS(data[[Dept]:[Dept]],$F5,data[[Group]:[Group]],G$4)
    

![Two-way summary count with an excel table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/Two-way%20summary%20count%20with%20an%20excel%20table.png?itok=t0zuAPCp "Two-way summary count with an excel table")

This formula is a bit more complex than usual, because the Dept and Group columns need to be locked in a special way with the double square brackets and a colon to allow the formula to be copied across the summary tabled. The two references below show this difference in syntax:

    data[Dept] // normal
    data[[Dept]:[Dept]] // locked
    

For more on Excel Tables and structured references, see the videos below. One of the videos shows an easy way to lock a structured reference. If you are new to Excel Tables, see [What is an Excel Table](https://exceljet.net/videos/what-is-an-excel-table)
?

### Dynamic array option

In the latest version of Excel, which [supports dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can adapt this example to automatically extract the values for Dept and Group with the [UNIQUE function](https://exceljet.net/functions/unique-function)
. If fact, if we throw in the [LET function](https://exceljet.net/functions/let-function)
 and two new functions, [HSTACK](https://exceljet.net/functions/hstack-function)
 and [VSTACK](https://exceljet.net/functions/vstack-function)
, it is possible to write a _single_ all-in-one formula that builds a complete summary table like this:

    =LET(
      depts,UNIQUE(data[Dept]),
      groups,TRANSPOSE(UNIQUE(data[Group])),
      counts,COUNTIFS(data[Dept],depts,data[Group],groups),
      HSTACK(VSTACK({"Department"},depts),VSTACK(groups,counts))
    )
    

![All in one formula with new dynamic array functions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/Two-way%20summary%20count%20all%20in%20one%20dynamic%20array.png?itok=_xUgfqfV "All in one formula with new dynamic array functions")

_Note: VSTACK and HSTACK are still in beta, available via the Beta Channel for Excel 365._

In a nutshell, we use the UNIQUE function to extract unique departments and groups, and the COUNTIFS function to generate all counts. The [LET function](https://exceljet.net/functions/let-function)
 is used to assign all three intermediate results to the variables _depts_, _groups_, and _counts_. Next, the [HSTACK](https://exceljet.net/functions/hstack-function)
 and [VSTACK](https://exceljet.net/functions/vstack-function)
 functions are used to assemble the final table. Because HSTACK is the last function to run, it returns the final result, which is an [array](https://exceljet.net/glossary/array)
 of values that [spill](https://exceljet.net/glossary/spill)
 into multiple cells. To learn more about how to convert a formula to use LET, see this [detailed LET function example](https://exceljet.net/formulas/detailed-let-function-example)
.

The best thing about this approach is that any changes to the source data will be reflected in the summary table instantly, with no need to refresh or edit the formula. As a bonus, there is no need to lock specific cell references. The formula above is a great example of how dynamic array formulas will completely change formula solutions in the future. See [this example](https://exceljet.net/formulas/dynamic-two-way-count)
 for another related problem with a more complete walkthrough.

Related formulas
----------------

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

[![Excel formula: Summary count with percentage breakdown](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20%20couunt%20with%20percentage%20breakdown_0.png "Excel formula: Summary count with percentage breakdown")](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

### [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

In this example, the goal is to calculate a count and percentage for each category shown in column B. For convenience, the category values in column B are in the named range category (B5:B122). To generate the count, we use the COUNTIF function . The formula in G5, copied through the range G5:G9 is...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20is%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/what-is-an-excel-table)

### [What is an Excel Table](https://exceljet.net/videos/what-is-an-excel-table)

In this video, we'll introduce the idea of an Excel Table. So, what is an Excel Table? An Excel table is a rectangular range of data that has been defined and named in a particular way. To illustrate, here I have two rectangular ranges of data. Both ranges contain exactly the same data but neither...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Introduction%20to%20structured%20references_thumb.png)](https://exceljet.net/videos/introduction-to-structured-references)

### [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)

In this video, I'll give a brief introduction to structured references. A structured reference is a term for using a table name in a formula instead of a normal cell reference. Structured references are optional, and can be used with formulas both inside or outside an Excel table. Let's take a look...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20copy%20and%20lock%20structured%20references-Thumb.png)](https://exceljet.net/videos/how-to-copy-and-lock-structured-references)

### [How to copy and lock structured references](https://exceljet.net/videos/how-to-copy-and-lock-structured-references)

In this video, we'll look at how to copy and lock structured references in a formula. Structured references behave differently from other references when copied. Let's look at some examples. First, notice if I copy and paste a formula that contains structured references, column names won't change...

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
    
*   [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    

### Videos

*   [What is an Excel Table](https://exceljet.net/videos/what-is-an-excel-table)
    
*   [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)
    
*   [How to copy and lock structured references](https://exceljet.net/videos/how-to-copy-and-lock-structured-references)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Excel Tables](https://exceljet.net/training/excel-tables)
    

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