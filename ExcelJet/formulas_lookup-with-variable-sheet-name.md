# Lookup with variable sheet name - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lookup-with-variable-sheet-name

---

[Skip to main content](https://exceljet.net/formulas/lookup-with-variable-sheet-name#main-content)

[](https://exceljet.net/formulas/lookup-with-variable-sheet-name#)

*   [Previous](https://exceljet.net/formulas/lookup-value-between-two-numbers)
    
*   [Next](https://exceljet.net/formulas/match-first-does-not-begin-with)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Lookup with variable sheet name
===============================

by Dave Bruns · Updated 22 Jan 2024

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Lookup with variable sheet name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lookup_with_variable_sheet_name.png "Excel formula: Lookup with variable sheet name")

Summary
-------

To create a lookup with a variable sheet name, you can use the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 together with the [INDIRECT function](https://exceljet.net/functions/indirect-function)
. In the example shown, the formula in C5 is:

    =VLOOKUP($B5,INDIRECT("'"&C$4&"'!"&"B5:C12"),2,0)
    

As the formula is copied down and across, it looks up the make in column B on each of the three worksheets (Jan, Feb, and Mar) and returns the value for that month.

Generic formula
---------------

    =VLOOKUP(val,INDIRECT("'"&sheet&"'!"&"range"),col,0)

Explanation 
------------

In this example, the goal is to create a lookup formula with a variable sheet name. In other words, a formula that uses a sheet name typed into a cell to construct a reference to a range on that sheet. If the sheet name is changed, the reference should update automatically. The key to the solution explained below is the INDIRECT function which is designed to evaluate text as a worksheet reference. When the evaluation succeeds, INDIRECT converts the text into a valid reference. This makes it possible to build a formula to assemble a reference as text using [concatenation](https://exceljet.net/glossary/concatenation)
, and use the resulting text as a valid reference.

### Workbook setup

The workbook contains four worksheets:

1.  Summary - the sheet that looks up data on the other sheets
2.  Jan - data for January
3.  Feb - data for February
4.  Mar - data for March 

Each of the monthly sheets has the same structure, which looks like this:

![Example of month data sheet for January](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/lookup_with_variable_sheet_name_january_data.png "Example of month data sheet for January")

### VLOOKUP solution

The formulas on the summary tab lookup and extract data from the month tabs, by creating a dynamic reference to the sheet name for each month, where the names for each sheet are the month names in row 4. The [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 is used to perform the lookup. The formula in cell C5 is:

    =VLOOKUP($B5,INDIRECT("'"&C$4&"'!"&"B5:C12"),2,0)
    

Inside VLOOKUP, the lookup value is entered as the [mixed reference](https://exceljet.net/glossary/mixed-reference)
 $B5, with the column [locked](https://exceljet.net/shortcuts/toggle-absolute-and-relative-references)
 to allow copying across the table. The table array is created using the [INDIRECT function](https://exceljet.net/functions/indirect-function)
 like this:

    INDIRECT("'"&C$4&"'!"&"B5:C12")

The mixed reference C$4 refers to the column headings in row 4, which match sheet names in the workbook (i.e. "Jan", "Feb", "Mar"). A single quote character is joined to either side of C$4 using the [concatenation](https://exceljet.net/glossary/concatenation)
 [operator](https://exceljet.net/glossary/math-operators)
 (&).

> The single quotes are not required in this particular example, but they allow the formula to handle sheet names that contain spaces in other workbooks. 

Next, the exclamation point (!) is joined on the right to create a proper sheet reference, which is followed by the range to use as the table array. Note that the result of this concatenation is _text._ Next, the INDIRECT function evaluates the text and converts it to a proper reference:

    =VLOOKUP($B5,INDIRECT("'"&C$4&"'!"&"B5:C12"),2,0)
    =VLOOKUP($B5,INDIRECT("'Jan'!B5:C12"),2,0)
    =VLOOKUP($B5,Jan!B5:C12,2,0)
    

Finally, VLOOKUP can finish the job. Since the data we want to retrieve is in the second column, the column index number is provided as 2. We provide zero (0) for _range\_lookup_ to force an exact match. As the formula is copied down and across, VLOOKUP retrieves the correct values from each sheet.

Notice that the sort order on the summary page is different from the sort order used on each data sheet. However, because we are using a _lookup operation_ to retrieve the monthly values, this does not matter. VLOOKUP correctly finds and retrieves the monthly values for each make on each data sheet regardless of the order in which they appear.

Related formulas
----------------

[![Excel formula: Dynamic worksheet reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/formula%20with%20dynamic%20sheet%20name.png "Excel formula: Dynamic worksheet reference")](https://exceljet.net/formulas/dynamic-worksheet-reference)

### [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)

The INDIRECT function tries to evaluate text as a worksheet reference. This makes it possible to build formulas that assemble a reference as text using concatenation , and use the resulting text as a valid reference. In this example, we have Sheet names in column B, so we join the sheet name to the...

[![Excel formula: Dynamic workbook reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20workbook%20reference.png "Excel formula: Dynamic workbook reference")](https://exceljet.net/formulas/dynamic-workbook-reference)

### [Dynamic workbook reference](https://exceljet.net/formulas/dynamic-workbook-reference)

In this example, the goal is to create a reference to an external workbook with variable information. The easiest way to do this is to assemble the reference to a range or cell in another workbook as a text value , then use the INDIRECT function to convert the text to an actual reference. In Excel...

[![Excel formula: VLOOKUP with variable table array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20variable%20table%20array.png "Excel formula: VLOOKUP with variable table array")](https://exceljet.net/formulas/vlookup-with-variable-table-array)

### [VLOOKUP with variable table array](https://exceljet.net/formulas/vlookup-with-variable-table-array)

In this example, the goal is to set up VLOOKUP to retrieve costs based on a variable vendor name. In other words, we want a formula that allows us to switch tables dynamically based on a user-supplied value. There are two cost tables in the worksheet, one for Vendor A and one for Vendor B. Both...

[![Excel formula: Sum across multiple worksheets with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20across%20multiple%20worksheets%20with%20criteria.png "Excel formula: Sum across multiple worksheets with criteria")](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria)

### [Sum across multiple worksheets with criteria](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria)

In this example, the goal is to sum hours per project across three different worksheets: Sheet1, Sheet2, and Sheet3. The data on each of the three sheets has the same structure as Sheet1, as seen below: 3D reference won't work Before we look at a solution, let's look at something that doesn't work...

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20replace%20nested%20IFs%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

### [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

You might build or inherit a worksheet that uses a series of nested IF statements to assign values of some kind. Many people use nested IF statements this way because the approach is easy once you get the hang of it. But nested IF statements can be difficult to maintain and debug. Let's look at how...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20for%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

### [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

In a lot of cases, you'll use VLOOKUP to find exact matches based on some kind of unique id, but there are many situations where you'll want to use VLOOKUP to find non-exact matches. A classic case is using VLOOKUP to find a commission rate based on a sales number. Let's take a look. Here we have...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Why%20VLOOKUP%20is%20better%20than%20nested%20IFs-thumb.png)](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

### [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

In this video we look at a few reasons why VLOOKUP is a better option than nested IF statements. In our last video, we used nested IF statements to calculate a commission rate based on a sales number. As a quick recap: The first formula is created with nested IF statements normally. The second...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)
    
*   [Dynamic workbook reference](https://exceljet.net/formulas/dynamic-workbook-reference)
    
*   [VLOOKUP with variable table array](https://exceljet.net/formulas/vlookup-with-variable-table-array)
    
*   [Sum across multiple worksheets with criteria](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    
*   [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    

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