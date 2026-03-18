# Minimum if multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/minimum-if-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/minimum-if-multiple-criteria#main-content)

[](https://exceljet.net/formulas/minimum-if-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/maximum-value-if)
    
*   [Next](https://exceljet.net/formulas/minimum-value)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Minimum if multiple criteria
============================

by Dave Bruns · Updated 20 Mar 2023

Related functions 
------------------

[MIN](https://exceljet.net/functions/min-function)

[IF](https://exceljet.net/functions/if-function)

[MINIFS](https://exceljet.net/functions/minifs-function)

![Excel formula: Minimum if multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/minimum_if_multiple_criteria.png "Excel formula: Minimum if multiple criteria")

Summary
-------

To get the minimum value in a set of data that meets multiple criteria, you can use a formula based on the [MINIFS function](https://exceljet.net/functions/minifs-function)
. In the example shown, the formula in H5 is:

    =MINIFS(data[Value],data[Group],F5,data[Temp],">"&G5)

With "A" in cell F5 and the number 72 in cell G5, the result is 94. This is the minimum value in group "A" above a temperature of 72.

Generic formula
---------------

    =MINIFS(data,range1,criteria1,range2,criteria2)

Explanation 
------------

In this example, the goal is to get the minimum value for a given group above a specific temperature. In other words, we want the min value _after_ applying multiple criteria. The easiest way to solve this problem is with the MINIFS function. However, if you need more flexibility (for example, you need to work with arrays and not ranges), you can use the MIN function with the FILTER function. In older versions of Excel without MINIFS or FILTER, you can use a traditional [array formula](https://exceljet.net/glossary/array-formula)
 based on the MIN function and the IF function. Each method is explained below.

### Excel Table

For convenience, all data is in an [Excel Table](https://exceljet.net/glossary/excel-table)
 named **data** in the range B5:D16. Excel Tables are a convenient way to work with data in Excel because they (1) automatically expand to include new data and (2) offer [structured references](https://exceljet.net/glossary/structured-reference)
, which allow you to refer to data by name instead of by address. If you are new to Excel Tables, [this article provides an overview](https://exceljet.net/articles/excel-tables)
.

Video: [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)

### MINIFS function

One way to solve this problem is with the [MINIFS function](https://exceljet.net/functions/minifs-function)
, which can get the minimum value in a range based on one or more criteria. The generic syntax for MINIFS with two conditions looks like this:

    =MINIFS(min_range,range1,criteria1,range2,criteria2)
    

Note that each condition requires two [arguments](https://exceljet.net/glossary/function-argument)
: _range1_ and _criteria1_ define the first condition, and _range2_ and _criteria2_ define the second condition. All conditions must be true in order for value to be considered. We start off with the _min\_range_, which is the Value column in the table:

    =MINIFS(data[Value],

Next, we add criteria to test for the group value entered in cell F5:

    =MINIFS(data[Value],data[Group],F5

If we enter the formula above as-is, we will get the minimum value in group "A". Next, we need to add a second condition to further restrict values to those above the temperature entered in cell G5:

    =MINIFS(data[Value],data[Group],F5,data[Temp],"<"&G5)

Notice we need to [concatenate](https://exceljet.net/glossary/concatenation)
 the greater than operator ("<") to cell F5. This is a requirement of the MINIFS function, which uses an [unusual formula syntax](https://exceljet.net/articles/excels-racon-functions)
 shared by SUMIFS, COUNTIFS, etc. When we enter this formula, it returns the minimum value in group "A" above a temperature of 72. For reference, the same formula with conditions hardcoded looks like this:

    =MINIFS(data[Value],data[Group],"A",data[Temp],">72")

Note that MINIFS will automatically _ignore_ empty cells that meet criteria. In other words, MINIFS will not treat empty cells that meet criteria as zero. On the other hand, MINIFS _will_ return zero (0) if no cells match criteria. The MINIFS function works well, but it does have a significant limitation: the range arguments inside MINIFS must be actual _ranges_, you can't substitute _arrays_. If you need to use arrays, see the MIN + FILTER option below.

### MIN + FILTER

In the [dynamic array version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, another way to solve this problem is with [MIN](https://exceljet.net/functions/min-function)
  and [FILTER](https://exceljet.net/functions/filter-function)
 like this:

    =MIN(FILTER(data[Value],(data[Group]=F5)*(data[Temp]>G5)))

Inside the MIN function, the FILTER function is configured to filter values by group and temperature:

    FILTER(data[Value],(data[Group]=F5)*(data[Temp]>G5))

_Array_ is provided as the Value column in the table. The _include_ argument is a simple expression:

    (data[Group]=F5)*(data[Temp]>G5)

This is an example of using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 in Excel. Because there are 12 values in the table, each expression above generates an array of 12 TRUE and FALSE values like this:

    {TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE}*{FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE}

In the first array, the TRUE values indicate values in group "A". In the second array, TRUE values indicate values above a temperature of 72. The math operation of multiplication (\*) converts the TRUE and FALSE values to 1s and 0s:

    {1;0;0;1;0;0;1;0;0;1;0;0}*{0;0;0;0;0;0;1;1;1;1;1;1}

And the result is a single array as the _include_ argument like this:

    FILTER(data[Value],{0;0;0;0;0;0;1;0;0;1;0;0})

Note the 1s in this array correspond to values that are in group "A" with a temperature above 72. FILTER returns the two values that meet this criteria directly to the MIN function:

    =MIN({94;101})

and MIN returns 94 as a final result. The primary advantage of using the MIN function with the FILTER function is that you don't need to provide a _range_ of values on the worksheet. You can instead provide an _array_ of values created with another operation. This is important when source data needs to be manipulated before a minimum value is calculated. 

### MIN + IF

In older versions of Excel that do not have the MINIFS function or the FILTER function, you can solve this problem with an [array formula](https://exceljet.net/glossary/array-formula)
 based on the [MIN function](https://exceljet.net/functions/min-function)
 and the [IF function](https://exceljet.net/functions/if-function)
 like this:

    =MIN(IF((data[Group]=F5)*(data[Temp]>G5),data[Value]))

_Note: this is an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 and must be entered with control + shift + enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

Working from the inside out, the [IF function](https://exceljet.net/functions/if-function)
 is evaluated first. The logical test inside IF is exactly the same as the logic explained above for FILTER:

    (data[Group]=F5)*(data[Temp]>G5) // logical test

After the logic is evaluated, we have an array of 1s and 0s like this:

    =MIN(IF({0;0;0;0;0;0;1;0;0;1;0;0},data[Value]))

The 1s correspond to rows where the group is "A" and the Temp is greater than 72. The final result from IF is an [array](https://exceljet.net/glossary/array)
 like this:

    {FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;94;FALSE;FALSE;101;FALSE;FALSE}
    

Looking at the values in this array, you can see that the IF function acts like a filter. Only values associated with group "A" and a temperature greater than 72 make it through the filter. The other values are replaced with FALSE. The IF function delivers this array directly to the [MIN function](https://exceljet.net/functions/min-function)
:

    =MIN({FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;94;FALSE;FALSE;101;FALSE;FALSE})

The MIN function automatically ignores FALSE values and returns the minimum number in the array: 94.

### Alternative syntax with nested IFs

The array formula above uses [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 to streamline the formula, but another option you might run into is [nesting](https://exceljet.net/glossary/nesting)
 one IF formula inside another like this:

    =MIN(IF(data[Group]=F5,IF(data[Temp]>G5,data[Value])))
    

_Note: this is an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 and must be entered with control + shift + enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

Each IF formula applies a separate condition, so the values are filtered in two steps instead of one. This works fine, but the formula gets more complicated as additional criteria are added, since each condition requires another IF function. The advantage Boolean logic version of the formula is that you can add additional criteria without adding more IF functions.

Related formulas
----------------

[![Excel formula: Maximum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value.png "Excel formula: Maximum value")](https://exceljet.net/formulas/maximum-value)

### [Maximum value](https://exceljet.net/formulas/maximum-value)

In this example, the goal is to get the maximum quiz score (i.e. the best quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MAX function or the LARGE function, as explained below. MAX function The MAX function accepts...

[![Excel formula: Minimum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value.png "Excel formula: Minimum value")](https://exceljet.net/formulas/minimum-value)

### [Minimum value](https://exceljet.net/formulas/minimum-value)

In this example, the goal is to get the minimum quiz score (i.e. the lowest quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MIN function or the SMALL function, as explained below. MIN function The MIN function...

[![Excel formula: Maximum change](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_change.png "Excel formula: Maximum change")](https://exceljet.net/formulas/maximum-change)

### [Maximum change](https://exceljet.net/formulas/maximum-change)

In the example shown, the goal is to calculate the maximum difference between the "High" values in column C and the "Low" values in column D. Because the difference between High and Low is not part of the data, the calculation must occur in the formula itself. This is a classic example of an array...

[![Excel formula: Maximum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_if_multiple_criteria.png "Excel formula: Maximum if multiple criteria")](https://exceljet.net/formulas/maximum-if-multiple-criteria)

### [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)

In this example, the goal is to get the maximum value for a given group below a specific temperature. In other words, we want the max value after applying multiple criteria. The easiest way to solve this problem is with the MAXIFS function. However, if you need more flexibility (i.e., you need to...

[![Excel formula: Lookup lowest Monday tide](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20lowest%20monday%20tide.png "Excel formula: Lookup lowest Monday tide")](https://exceljet.net/formulas/lookup-lowest-monday-tide)

### [Lookup lowest Monday tide](https://exceljet.net/formulas/lookup-lowest-monday-tide)

At a high level, this example is about finding a minimum value based on multiple criteria. To do that, we are using the MIN function together with two nested IF functions : {=MIN(IF(day=I5,IF(tide="L",pred)))} working from the inside out, the first IF checks if the day is "Mon", based on the value...

[![Excel formula: Get next scheduled event](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20next%20scheduled%20event.png "Excel formula: Get next scheduled event")](https://exceljet.net/formulas/get-next-scheduled-event)

### [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)

The first part of the solution uses the MIN and TODAY functions to find the "next date" based on the date today. This is done by filtering the dates through the IF function: IF((date>=TODAY()),date) The logical test generates an array of TRUE / FALSE values, where TRUE corresponds to dates greater...

Related functions
-----------------

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel MINIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_minifs.png "Excel MINIFS function")](https://exceljet.net/functions/minifs-function)

### [MINIFS Function](https://exceljet.net/functions/minifs-function)

The Excel MINIFS function returns the smallest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MINIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers,...

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
    
*   [Maximum change](https://exceljet.net/formulas/maximum-change)
    
*   [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)
    
*   [Lookup lowest Monday tide](https://exceljet.net/formulas/lookup-lowest-monday-tide)
    
*   [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)
    

### Functions

*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [MINIFS Function](https://exceljet.net/functions/minifs-function)
    

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