# Minimum value if - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/minimum-value-if

---

[Skip to main content](https://exceljet.net/formulas/minimum-value-if#main-content)

[](https://exceljet.net/formulas/minimum-value-if#)

*   [Previous](https://exceljet.net/formulas/minimum-value)
    
*   [Next](https://exceljet.net/formulas/name-of-nth-largest-value)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Minimum value if
================

by Dave Bruns · Updated 29 Mar 2023

Related functions 
------------------

[MINIFS](https://exceljet.net/functions/minifs-function)

[MIN](https://exceljet.net/functions/min-function)

[FILTER](https://exceljet.net/functions/filter-function)

[IF](https://exceljet.net/functions/if-function)

[BYROW](https://exceljet.net/functions/byrow-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

[HSTACK](https://exceljet.net/functions/hstack-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

![Excel formula: Minimum value if](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/minimum_value_if_0.png "Excel formula: Minimum value if")

Summary
-------

To get the minimum value if a condition is true, you can use the [MINIFS function](https://exceljet.net/functions/minifs-function)
. In the example shown, the formula in cell F5 is:

    =MINIFS(data[Value],data[Group],E5)

Where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:C16. As the formula is copied down, the result is the minimum value for each group listed in column E. There are several ways to approach this problem. See below for other formula options, including an all-in-one formula that creates a dynamic summary table and an array formula for older versions of Excel without the MINIFS function.

Generic formula
---------------

    =MINIFS(data,range,criteria)

Explanation 
------------

In this example, the goal is to get the minimum value for each group in the data as shown. The easiest way to solve this problem is with the MINIFS function. However, there are actually several options. If you need more flexibility (you need to work with arrays instead of ranges), you can use the MIN function with the FILTER function. To create a dynamic summary table with a single all-in-one formula, you can use the BYROW function. In older versions of Excel without the MINIFS function, you can use an [array formula](https://exceljet.net/glossary/array-formula)
 based on the MIN function and the IF function. Each approach is explained below. For convenience, all data is in an Excel Table named **data** in the range B5:C16. If you are new to Excel Tables, [this article provides an overview](https://exceljet.net/articles/excel-tables)
.

### MINIFS function

The [MINIFS function](https://exceljet.net/functions/minifs-function)
 can get the minimum value in a range based on one or more criteria. The generic syntax for MINIFS with a single condition looks like this:

    =MINIFS(min_range,range1,criteria1)
    

Note that the condition is defined with two [arguments](https://exceljet.net/glossary/function-argument)
: _range1_ and _criteria1_. In this problem, the condition is that the group value in column B must equal the group value in column E. We start off with the _min\_range_, which is the Value column:

    =MINIFS(data[Value],

Next, we add the criteria range, which is the Group column:

    =MINIFS(data[Value],data[Group],

Finally, we add the criteria itself, which comes from cell E5:

    =MINIFS(data[Value],data[Group],E5)

As the formula is copied down, the [table references](https://exceljet.net/glossary/structured-reference)
 behave like [absolute references](https://exceljet.net/glossary/absolute-reference)
 and don't change. The reference to E5 is relative and changes at each new row. The result is the minimum value for each group listed in column E.

The MINIFS function is a straightforward solution that works well. However, it does have one significant limitation: the range arguments inside MINIFS must be actual ranges, you can't substitute arrays. If you need to use arrays, see the MIN + FILTER option, or the all-in-one summary table formula based on the [BYROW function](https://exceljet.net/functions/byrow-function)
 below.

### MIN + FILTER

In the dynamic array version of Excel, another way to solve this problem is with the [MIN function](https://exceljet.net/functions/min-function)
 and the [FILTER function](https://exceljet.net/functions/filter-function)
 like this:

    =MIN(FILTER(data[Value],data[Group]=E5))

Inside the MIN function, the FILTER function is configured to filter values by group:

    FILTER(data[Value],data[Group]=E5)

_Array_ is provided as the Value column in the table, and the _include_ argument is a simple expression:

    data[Group]=E5

With "A" in cell E5, the expression above returns an array like this:

    {TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE}

Because there are 12 values in Group, there are 12 TRUE and FALSE results. The TRUE values correspond to values in the table associated with group A. With the array above acting as a filter, the FILTER function returns an array that contains the four values in group A directly to the MIN function:

    =MIN({81;131;127;140})

MIN then returns a final result of 81. The primary advantage of using the MIN function with the FILTER function is that you are not required to supply a range of values on the worksheet. You can instead provide an array of values created with another operation. This is very useful when the source data needs to be manipulated in some way before a min value is calculated. 

### Summary table with BYROW

In the latest version of Excel, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can create a single all-in-one formula that builds the entire summary table, including headers, like this:

    =LET(
    groups,data[Group],
    values,data[Value],
    ugroups,UNIQUE(groups),
    results,BYROW(ugroups,LAMBDA(r,MIN(FILTER(values,groups=r)))),
    VSTACK({"Group","Min"},HSTACK(ugroups, results))
    )

The [LET function](https://exceljet.net/functions/let-function)
 is used to assign four intermediate variables: _groups_, _values,_ _ugroups_, and _results_. Both groups and values are simple assignments to rows in the table:

    groups,data[Group],
    values,data[Value],
    

This is done primarily to make the formula more portable. Defining these variables here keeps all of the worksheet references at the top of the formula where they can be easily changed.

In our summary table, we want a list of unique groups, so we define _ugroups_ (unique groups) with the [UNIQUE function](https://exceljet.net/functions/unique-function)
 like this:

    ugroups,UNIQUE(groups), // get unique groups
    

From the 12 rows in the data, the UNIQUE function returns just 3 _unique_ groups:

    {"A";"B";"C"} // unique groups

_Note: you could run groups through the [SORT function](https://exceljet.net/functions/sort-function)
 to ensure that groups are in the correct order. In this case the source data already shows groups in order, so it is not necessary._

At this point, we are ready to calculate the minimum values for each group. We do this with the [BYROW function](https://exceljet.net/functions/byrow-function)
 which uses a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to calculate the minimum values and assigns the result to the _results_ variable:

    results,BYROW(ugroups,LAMBDA(r,MIN(FILTER(values,groups=r))))
    

BYROW runs through the _ugroups_ values row by row. At each row, it applies this calculation:

    LAMBDA(r,MIN(FILTER(values,groups=r)))
    

The value _r_ is the unique group in the "current" row in the summary table. Inside the MIN function, the FILTER function is configured to filter values by group like this:

    FILTER(values,groups=r)
    

In the first row (group A), the result from FILTER is an array like this:

    {81;131;127;140}

This array is delivered directly to the MIN function, which returns the minimum number. When BYROW is finished, we have an array with 3 numbers (one for each group) like this:

    {81;97;82} // results
    

This array is the value assigned to _results_. Finally the [HSTACK](https://exceljet.net/functions/hstack-function)
 and [VSTACK](https://exceljet.net/functions/vstack-function)
 functions are used to assemble a complete table:

    VSTACK({"Group","Min"},HSTACK(ugroups, results))
    

At the top of the table, the [array constant](https://exceljet.net/glossary/array-constant)
 {"Group","Min"} creates a header row. The HSTACK function combines _ugroups_ and _results_ horizontally, and VSTACK combines the header row and the data to make the final table. The final result [spills](https://exceljet.net/glossary/spill)
 into multiple cells on the worksheet.

### MIN + IF

In older versions of Excel that do not have the MINIFS function, you can solve this problem with an [array formula](https://exceljet.net/glossary/array-formula)
 based on the [MIN function](https://exceljet.net/functions/min-function)
 and the [IF function](https://exceljet.net/functions/if-function)
 like this:

    =MIN(IF(data[Group]=E5,data[Value]))

_Note: this is an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 and must be entered with control + shift + enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

Working from the inside out, the [IF function](https://exceljet.net/functions/if-function)
 is evaluated first. The logical test is an expression that tests the entire Group column against the value in cell E5:

    =IF(data[Group]=E5 // logical test
    

Because there are 12 values in **data\[Group\]**, the result is an [array](https://exceljet.net/glossary/array)
 with 12 TRUE / FALSE values like this:

    {TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE}
    

The TRUE values correspond to rows where the group is "A". For all other groups, the value is FALSE. For _value\_if\_true_, we supply the Value column, and we omit _value\_if\_false_ altogether:

    IF(data[Group]=E5,data[Value])
    

The final result from IF is an [array](https://exceljet.net/glossary/array)
 like this:

    {81;FALSE;FALSE;131;FALSE;FALSE;127;FALSE;FALSE;140;FALSE;FALSE}
    

Looking at the values in this array, you can see that the IF function acts like a filter. Only numbers associated with group "A" make it through the filter, and other values are replaced with FALSE. The IF function delivers this array directly to the [MIN function](https://exceljet.net/functions/min-function)
:

    =MIN({81;FALSE;FALSE;131;FALSE;FALSE;127;FALSE;FALSE;140;FALSE;FALSE})

 The MIN function automatically ignores FALSE values and returns the minimum number in the array: 81.

Related formulas
----------------

[![Excel formula: Maximum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value.png "Excel formula: Maximum value")](https://exceljet.net/formulas/maximum-value)

### [Maximum value](https://exceljet.net/formulas/maximum-value)

In this example, the goal is to get the maximum quiz score (i.e. the best quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MAX function or the LARGE function, as explained below. MAX function The MAX function accepts...

[![Excel formula: Minimum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value.png "Excel formula: Minimum value")](https://exceljet.net/formulas/minimum-value)

### [Minimum value](https://exceljet.net/formulas/minimum-value)

In this example, the goal is to get the minimum quiz score (i.e. the lowest quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MIN function or the SMALL function, as explained below. MIN function The MIN function...

[![Excel formula: Maximum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value_if.png "Excel formula: Maximum value if")](https://exceljet.net/formulas/maximum-value-if)

### [Maximum value if](https://exceljet.net/formulas/maximum-value-if)

In this example, the goal is to get the maximum value for each group in the data as shown. The easiest way to solve this problem is with the MAXIFS function. However, there are actually several options. If you need more flexibility (i.e. you need to work with arrays and not ranges), you can use the...

[![Excel formula: Minimum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_if_multiple_criteria.png "Excel formula: Minimum if multiple criteria")](https://exceljet.net/formulas/minimum-if-multiple-criteria)

### [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)

In this example, the goal is to get the minimum value for a given group above a specific temperature. In other words, we want the min value after applying multiple criteria. The easiest way to solve this problem is with the MINIFS function. However, if you need more flexibility (for example, you...

[![Excel formula: Maximum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_if_multiple_criteria.png "Excel formula: Maximum if multiple criteria")](https://exceljet.net/formulas/maximum-if-multiple-criteria)

### [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)

In this example, the goal is to get the maximum value for a given group below a specific temperature. In other words, we want the max value after applying multiple criteria. The easiest way to solve this problem is with the MAXIFS function. However, if you need more flexibility (i.e., you need to...

[![Excel formula: Get next scheduled event](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20next%20scheduled%20event.png "Excel formula: Get next scheduled event")](https://exceljet.net/formulas/get-next-scheduled-event)

### [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)

The first part of the solution uses the MIN and TODAY functions to find the "next date" based on the date today. This is done by filtering the dates through the IF function: IF((date>=TODAY()),date) The logical test generates an array of TRUE / FALSE values, where TRUE corresponds to dates greater...

Related functions
-----------------

[![Excel MINIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_minifs.png "Excel MINIFS function")](https://exceljet.net/functions/minifs-function)

### [MINIFS Function](https://exceljet.net/functions/minifs-function)

The Excel MINIFS function returns the smallest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MINIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers,...

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

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
    
*   [Maximum value if](https://exceljet.net/formulas/maximum-value-if)
    
*   [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)
    
*   [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)
    
*   [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)
    

### Functions

*   [MINIFS Function](https://exceljet.net/functions/minifs-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    
*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    

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