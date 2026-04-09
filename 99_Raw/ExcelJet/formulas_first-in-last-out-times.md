# First in last out times - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/first-in-last-out-times

---

[Skip to main content](https://exceljet.net/formulas/first-in-last-out-times#main-content)

[](https://exceljet.net/formulas/first-in-last-out-times#)

*   [Previous](https://exceljet.net/formulas/find-lowest-n-values)
    
*   [Next](https://exceljet.net/formulas/large-with-criteria)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

First in last out times
=======================

by Dave Bruns · Updated 4 Mar 2023

Related functions 
------------------

[MINIFS](https://exceljet.net/functions/minifs-function)

[MAXIFS](https://exceljet.net/functions/maxifs-function)

[MIN](https://exceljet.net/functions/min-function)

[MAX](https://exceljet.net/functions/max-function)

[IF](https://exceljet.net/functions/if-function)

[FILTER](https://exceljet.net/functions/filter-function)

![Excel formula: First in last out times](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/first_in_last_out_time.png "Excel formula: First in last out times")

Summary
-------

To find the earliest time in and the latest time out, you can use the [MINIFS function](https://exceljet.net/functions/minifs-function)
 and the [MAXIFS function](https://exceljet.net/functions/maxifs-function)
. In the example shown, the formula in H6 is:

    =MINIFS(data[Time],data[Name],G5,data[Action],H$4)
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D16. When the formula is entered, the result is 6:55 AM. This is the earliest "In" time for Juan. When the formula is copied down to the next row, the result is 7:45 AM. This is the earliest "In" time for Sarah.

Generic formula
---------------

    =MINIFS(times,names,"name",actions,"action")

Explanation 
------------

In this problem, the goal is to find the first (earliest) time in and the last (latest) time out for a given name. This is essentially a lookup problem and the solution shown in the worksheet is an example of how you can sometimes use minimum and maximum functions to perform lookups. This works because [Excel times](https://exceljet.net/glossary/excel-time)
 and [Excel dates](https://exceljet.net/glossary/excel-date)
 are _numeric_ values.

### Excel Table

For convenience, all data is in an [Excel Table](https://exceljet.net/glossary/excel-table)
 named **data** in the range B5:D16. Excel Tables are a convenient way to work with data in Excel because they (1) automatically expand to include new data and (2) offer [structured references](https://exceljet.net/videos/introduction-to-structured-references)
, which let you refer to data by name instead of by address. If you are new to Excel Tables, [this article provides an overview](https://exceljet.net/articles/excel-tables)
. Also see this short video:

Video: [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)

### MINIFS function

To get the first (earliest) time in time for a given name, you can use the [MINIFS function](https://exceljet.net/functions/minifs-function)
. The MINIFS function returns the smallest numeric value that meets one or more supplied criteria. Each condition is entered with a range and criteria, and the generic syntax for MINIFS with two criteria looks like this:

    =MINIFS(min_range,range1,criteria1,range2,criteria2)

In this case, we will need to apply two conditions: (1) check for the correct name and (2) check for the correct "action". The actions in the data are the text values "In" and "Out". We start off with the _min\_range_, which is the range that contains the numeric time values. We supply the Time column using the [structured reference](https://exceljet.net/glossary/structured-reference)
 **data\[Time\]**:

    =MINIFS(data[Time],

Next, we provide the first condition, which checks if the name in the data equals the name in cell G5:

    =MINIFS(data[Time],data[Name],G5,

The _criteria\_range_ is given as **data\[Name\]** and _criteria_ is supplied as cell G5. The second condition tests for the "In" action:

    =MINIFS(data[Time],data[Name],G5,data[Action],H$4)

In this case, _range_ is provided as **data\[Action\]** and _criteria_ is provided as H4. Notice that H$4 is a [mixed reference](https://exceljet.net/glossary/mixed-reference)
 with the row locked. We do this so we can copy the formula down in the next row and while keeping the action locked to cell H4.

When the formula is entered, the result is 6:55 AM. This is the earliest "In" time for Juan. When the formula is copied down to the next row, the result is 7:45 AM. This is the earliest "In" time for Sarah.

### MAXIFS function

To get the last (latest) time out for a given name, you can use the [MAXIFS function](https://exceljet.net/functions/maxifs-function)
. Like the MINIFS function, the MAXIFS function retrieves a value that meets one or more supplied criteria. The generic syntax for MAXIFS with two criteria looks like this:

    =MAXIFS(max_range,range1,criteria1,range2,criteria2)

To retrieve the last time out for a given name, we need to apply two conditions: (1) check for the correct name and (2) check for the "out" action.  We start off with the _max\_range_, which contains times:

    =MAXIFS(data[Time],

Then we provide a condition to check the name in the data against the name in cell G5:

    =MAXIFS(data[Time],data[Name],G5,

The _criteria\_range_ is given as **data\[Name\]** and _criteria_ is supplied as cell G5. Then we add the second condition to test for the "Out" action:

    =MAXIFS(data[Time],data[Name],G5,data[Action],I$4)

As above with the MINIFS function, we use a [mixed reference](https://exceljet.net/glossary/mixed-reference)
 for I$4 to look at the row. When the formula is entered, the result is 5:40 PM. This is the last "Out" time for Juan. When the formula is copied down to the next row, the result is 6:45 PM. This is the last "Out" time for Sarah.

### FILTER function

The MINIFS and MAXIFS functions are in a group of eight functions I call "RACON functions". These functions are built for convenience, but they have some quirks, [explained in more detail here](https://exceljet.net/articles/excels-racon-functions)
. The biggest limitation is that you can't use RACON functions on [_arrays_](https://exceljet.net/glossary/array)
 of data, you must provide an actual [range](https://exceljet.net/glossary/range)
. If you need to calculate minimum and maximum values based on one or more criteria with data in an array, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the MIN and MAX functions like this:

    =MIN(FILTER(data[Time],(data[Name]=G5)*(data[Action]=H$4)))
    =MAX(FILTER(data[Time],(data[Name]=G5)*(data[Action]=I$4)))

These are drop-in replacements for the MINIFS and MAXIFS formulas described above. The gist is that the FILTER function applies criteria and hands off the filtered times to MIN and MAX, which return a final result. I personally prefer this option because it uses standard syntax and will work on ranges as well as arrays. However, FILTER is a newer function in Excel and not available in older versions.

Video: [The FILTER function with two criteria](https://exceljet.net/videos/filter-function-with-two-criteria)

### Array formula alternatives

The MAXIFS and MINIFS functions were introduced in Excel 2016. If you are using an older version of Excel, you can use an [array formula](https://exceljet.net/glossary/array-formula)
 instead:

    {=MIN(IF(data[Name]=G5,IF(data[Action]=H$4,data[Time])))}
    {=MAX(IF(data[Name]=G5,IF(data[Action]=I$4,data[Time])))}

_Note: these are array formulas and must be entered with control + shift + enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

Related formulas
----------------

[![Excel formula: Maximum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value.png "Excel formula: Maximum value")](https://exceljet.net/formulas/maximum-value)

### [Maximum value](https://exceljet.net/formulas/maximum-value)

In this example, the goal is to get the maximum quiz score (i.e. the best quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MAX function or the LARGE function, as explained below. MAX function The MAX function accepts...

[![Excel formula: Minimum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value.png "Excel formula: Minimum value")](https://exceljet.net/formulas/minimum-value)

### [Minimum value](https://exceljet.net/formulas/minimum-value)

In this example, the goal is to get the minimum quiz score (i.e. the lowest quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MIN function or the SMALL function, as explained below. MIN function The MIN function...

[![Excel formula: Maximum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_if_multiple_criteria.png "Excel formula: Maximum if multiple criteria")](https://exceljet.net/formulas/maximum-if-multiple-criteria)

### [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)

In this example, the goal is to get the maximum value for a given group below a specific temperature. In other words, we want the max value after applying multiple criteria. The easiest way to solve this problem is with the MAXIFS function. However, if you need more flexibility (i.e., you need to...

[![Excel formula: Minimum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_if_multiple_criteria.png "Excel formula: Minimum if multiple criteria")](https://exceljet.net/formulas/minimum-if-multiple-criteria)

### [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)

In this example, the goal is to get the minimum value for a given group above a specific temperature. In other words, we want the min value after applying multiple criteria. The easiest way to solve this problem is with the MINIFS function. However, if you need more flexibility (for example, you...

Related functions
-----------------

[![Excel MINIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_minifs.png "Excel MINIFS function")](https://exceljet.net/functions/minifs-function)

### [MINIFS Function](https://exceljet.net/functions/minifs-function)

The Excel MINIFS function returns the smallest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MINIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers,...

[![Excel MAXIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxifs%20function.png "Excel MAXIFS function")](https://exceljet.net/functions/maxifs-function)

### [MAXIFS Function](https://exceljet.net/functions/maxifs-function)

The Excel MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MAXIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and...

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20maximum%20and%20minimum%20values-thumb.png)](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

### [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

In this video we'll look at how to calculate minimum and maximum values in Excel. Let's take a look. Here we have a list of properties, that includes an address, a price, and a variety of other information. Let's calculate the maximum and minimum values in this list. First, I'm going to create a...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Maximum value](https://exceljet.net/formulas/maximum-value)
    
*   [Minimum value](https://exceljet.net/formulas/minimum-value)
    
*   [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)
    
*   [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)
    

### Functions

*   [MINIFS Function](https://exceljet.net/functions/minifs-function)
    
*   [MAXIFS Function](https://exceljet.net/functions/maxifs-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Videos

*   [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)
    

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