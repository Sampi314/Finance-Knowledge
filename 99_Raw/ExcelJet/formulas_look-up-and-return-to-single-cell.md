# Look up and return to single cell - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/look-up-and-return-to-single-cell

---

[Skip to main content](https://exceljet.net/formulas/look-up-and-return-to-single-cell#main-content)

[](https://exceljet.net/formulas/look-up-and-return-to-single-cell#)

*   [Previous](https://exceljet.net/formulas/list-missing-values)
    
*   [Next](https://exceljet.net/formulas/look-up-entire-column)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Look up and return to single cell
=================================

by Dave Bruns · Updated 8 May 2025

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[GROUPBY](https://exceljet.net/functions/groupby-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[ARRAYTOTEXT](https://exceljet.net/functions/arraytotext-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9114/download?token=5d2BbTSM)
 (18.35 KB)

![Excel formula: Look up and return to single cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lookup_and_return_to_single_cell.png "Excel formula: Look up and return to single cell")

Summary
-------

To look up and return all matches to a single cell, you can use a formula based on the [FILTER function](https://exceljet.net/functions/filter-function)
 and the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
. In the worksheet shown, the formula in cell F5, copied down, looks like this:

    =TEXTJOIN(", ",1,FILTER(name,team=E5))
    

As the formula is copied down, it returns the names for each team in column E, separated by commas. Because the result is a single text string, it fits neatly into one cell without [spilling](https://exceljet.net/glossary/spill)
. For convenience only, the worksheet contains two [named ranges](https://exceljet.net/articles/named-ranges)
: **name** (B5:B16) and **team** (C5:C16). 

Generic formula
---------------

    =TEXTJOIN(", ",1,FILTER(range2,range1=A1))

Explanation 
------------

In this example, the goal is to look up and retrieve all names for a given team and return them in a single cell as a comma‑separated list. At the core, this is a lookup problem, but the twist is that we want to return _multiple matches_ for each team, not just one. That means traditional lookup functions like VLOOKUP, XLOOKUP, etc., won't work because they only return the _first match_. Although this example deals with team members, it is applicable to many other real-world problems, including:

*   Project staffing – list everyone assigned to the same project code.
*   Class schedules – show all students in a given class period.
*   Class list - show all classes for a given student.
*   Sales analysis – list products in the same category.

What makes the task unique is that we want to locate multiple matches (i.e., all members of a given team), but we the result to be delivered to a single cell formatted as a clean, readable list (i.e., “Doug, Katy, Luis”) instead of a block names in different cells. In this article, we’ll explore two ways to solve the problem:

1.  FILTER + TEXTJOIN – simple and flexible
2.  GROUPBY + LAMBDA – an all‑in‑one summary table

We'll also look at replacing TEXTJOIN with the ARRAYTOTEXT function to create even simpler formulas.

> Note: For convenience only, the worksheet contains two [named ranges](https://exceljet.net/articles/named-ranges)
> : **name** (B5:B16) and **team** (C5:C16). Named ranges make the formulas below easier to read and write, but they are not required.

### Option 1: FILTER and TEXTJOIN

A straightforward solution to this problem is to use a formula based on the [FILTER function](https://exceljet.net/formulas/look-up-and-return-to-single-cell)
 combined with the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
. This is the approach seen in the worksheet above, where the formula in F5 is:

    =TEXTJOIN(", ",1,FILTER(name,team=E5))
    

At a high level, this formula uses FILTER to look up the names for a given team, and TEXTJOIN to join the names together with commas. Working from the inside out, FILTER is configured like this:

    FILTER(name,team=E5)
    

In this configuration, **name** (B5:B16) is the _array_ argument, which represents the values to return. The expression `team=E5` is the _include_ argument, which returns a Boolean array where each value is TRUE if the corresponding team matches the value in E5. FILTER uses this array to return only the names associated with the selected team. Since the team in E5 is “Red”, FILTER returns an array in the form `{"Adam";"Alex";"Susan"}` as a result. This array is returned directly to the TEXTJOIN function as the _text1_ argument. Simplifying, the formula becomes:

    =TEXTJOIN(", ",1,{"Adam";"Alex";"Susan"})
    

Here, the delimiter is set to a comma and a space to separate values, and the _ignore\_empty_ argument is set to 1 (or TRUE) to ignore any empty values. Finally, TEXTJOIN concatenates the values using “, ” as a delimiter:

    "Adam, Alex, Susan"
    

Because the result is a single text string, it fits neatly into one cell without spilling. As the formula is copied down, it returns names for each of the remaining teams. A key advantage of this approach is the flexibility provided by FILTER. Although we are using FILTER to test for an exact match on team name, this logic could be easily adjusted to suit other situations. For example, you could adjust FILTER to test for cells that _contain_ "red" with a generic formula like this:

    =FILTER(range,ISNUMBER(SEARCH("red",range)))

For details on the formula above, see: [FILTER text contains](https://exceljet.net/formulas/filter-text-contains)
. See our main [FILTER page](https://exceljet.net/functions/filter-function)
 for more examples of how filter logic can be extended.

### Listing team names

The formula above assumes that teams are _already_ listed in column E. You can either enter the team names manually or retrieve them with another formula. To get a list of unique teams with a formula, you can use the [UNIQUE function](https://exceljet.net/functions/unique-function)
 like this in cell E5:

    =UNIQUE(C5:C16)
    

UNIQUE will return the team names as shown, and then you can use the formula based on FILTER and TEXTJOIN.

### Option 2: GROUPBY and LAMBDA

Another option for solving this problem is to use the new [GROUPBY function](https://exceljet.net/functions/groupby-function)
, which essentially builds a lightweight pivot table with a formula. With GROUPBY, you can build the entire summary table with one formula like this in cell E5:

    =GROUPBY(team,name,LAMBDA(a,TEXTJOIN(", ",1,a)),,0)
    

![Using GROUPBY to create the entire summary in one step](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/lookup_and_return_to_single_cell_with_groupby.png "Using GROUPBY to create the entire summary in one step")

This is a great formula to demonstrate the flexibility and power of GROUPBY. The basic configuration looks like this:

*   _row\_fields_ – team (C5:C16)
*   _values_ – name (B5:B16)
*   _function_ – custom LAMBDA, explained below
*   _field\_headers_ – not provided
*   _total\_depth_ – 0 (no totals)

At a high level, we are grouping the names by teams. For the calculation, we are using a custom LAMBDA that joins names together, separated by commas, using the TEXTJOIN function. The total depth is set to zero because we don't want totals. Let’s look at the custom LAMBDA in more detail:

    LAMBDA(a,TEXTJOIN(", ",1,a))
    

The first argument, `a`, stands for the [array](https://exceljet.net/glossary/array)
 of names in each group. The second part is the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
, configured to join the values in `a` using a comma and space. We have also set the ignore\_empty argument to 1 (TRUE) to ignore any empty values that might creep into the array. This could happen if a team appeared in column B, but the corresponding cell in column C was empty.

At a high level, the GROUPBY function gathers names by team and feeds the resulting arrays into the LAMBDA. The LAMBDA then joins the values separated by commas using TEXTJOIN. The result is a two-column table that lists every unique team alongside the names associated with that team. A nice advantage of this approach is that there is no separate step to get a list of unique teams. The GROUPBY function handles that automatically. This makes GROUPBY ideal for dashboards or pivot-table-style summaries that need to accommodate changing data. 

> The idea of a "custom LAMBDA" sounds complicated. However, as you can see above, custom LAMBDAs can be quite simple. You will see them pop up frequently in other functions like [GROUPBY](https://exceljet.net/functions/groupby-function)
> , [PIVOTBY](https://exceljet.net/functions/pivotby-function)
> , [BYCOL](https://exceljet.net/functions/bycol-function)
> , and [BYROW](https://exceljet.net/functions/byrow-function)
>  that need to loop over data and perform a specific operation that requires some configuration. They are simply a generic container to deliver a custom calculation. 

### ARRAYTOTEXT option

An interesting way to make the formulas above simpler is to use the [ARRAYTOTEXT function](https://exceljet.net/functions/arraytotext-function)
 instead of the TEXTJOIN function. ARRAYTOTEXT is a utility function that converts an array or range into a text string. You can use ARRAYTOTEXT as a shortcut when the goal is to return comma-separated text. Below are the formulas above modified to use the ARRAYTOTEXT function:

    =ARRAYTOTEXT(FILTER(name,team=E5))
    =GROUPBY(team,name,ARRAYTOTEXT,,0)

As you can see, ARRAYTOTEXT is a drop-in replacement for the TEXTJOIN function, and it doesn't even require configuration, which makes both formulas notably shorter. This works because ARRAYTOTEXT will automatically output comma-separated text by default. However, one thing to remember with the ARRAYTOTEXT function is that its delimiters are based on regional settings, which vary by user. For example, if regional settings are for French/France, you will see semicolons (;) instead of commas. The other potential issue is that ARRAYTOTEXT has no way to suppress empty values, which will appear in the output as a repeated delimiter. If you need to define delimiters precisely or ignore empty values, TEXTJOIN is a better option.

### Summary

In this article, we looked at two ways to perform a lookup in Excel and return all matches to a single cell:

*   **FILTER + TEXTJOIN** is a flexible everyday solution. It’s short, transparent, and easy to adapt. It's a bit more work to set up because we need to get a list of unique teams first in column E, but it's easier to understand.
*   **GROUPBY + LAMBDA** goes further, producing a complete one-formula summary table. The main advantage is that you get the entire summary in one formula. The trade-off is that the formula is a bit harder to read and understand.

> For simplicity, the examples above use simple static ranges in all formulas. However, if you have a lot of data or if the data changes frequently, you may want to use an [Excel Table](https://exceljet.net/articles/excel-tables)
>  as the source. Another is to use a dynamic range created with the [TRIMRANGE function](https://exceljet.net/functions/trimrange-function)
> . In both cases, the ranges will be dynamic. This means the table will instantly update as rows are added or removed. 

Related formulas
----------------

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

[![Excel formula: Get all matches cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_all_matches_cell_contains.png "Excel formula: Get all matches cell contains")](https://exceljet.net/formulas/get-all-matches-cell-contains)

### [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)

In this example the goal is to check a cell for several things at once, and return a comma separated list of the things that were found. In other words, we want check for the colors seen in column E and list the colors found in column C. The formula in C5, copied down, is: =TEXTJOIN(", ",1,FILTER(...

[![Excel formula: INDEX and MATCH all matches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20data%20with%20helper%20column4.png "Excel formula: INDEX and MATCH all matches")](https://exceljet.net/formulas/index-and-match-all-matches)

### [INDEX and MATCH all matches](https://exceljet.net/formulas/index-and-match-all-matches)

Note: in more recent versions of Excel, the FILTER function is a better way to solve this problem. The INDEX and MATCH formula explained here is meant for legacy versions of Excel that do not provide the FILTER function. By default, lookup formulas in Excel like VLOOKUP and INDEX + MATCH will find...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel GROUPBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_groupby_function.png "Excel GROUPBY function")](https://exceljet.net/functions/groupby-function)

### [GROUPBY Function](https://exceljet.net/functions/groupby-function)

The Excel GROUPBY function is designed to summarize data by grouping rows and aggregating values. The result is a summary table created with a single formula.

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel ARRAYTOTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20arraytotext%20function.png "Excel ARRAYTOTEXT function")](https://exceljet.net/functions/arraytotext-function)

### [ARRAYTOTEXT Function](https://exceljet.net/functions/arraytotext-function)

The Excel ARRAYTOTEXT function converts an array or range to a text string. The result can optionally include or omit curly braces.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
    
*   [INDEX and MATCH all matches](https://exceljet.net/formulas/index-and-match-all-matches)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [GROUPBY Function](https://exceljet.net/functions/groupby-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [ARRAYTOTEXT Function](https://exceljet.net/functions/arraytotext-function)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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