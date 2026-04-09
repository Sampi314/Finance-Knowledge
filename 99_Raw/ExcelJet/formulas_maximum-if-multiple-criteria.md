# Maximum if multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/maximum-if-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/maximum-if-multiple-criteria#main-content)

[](https://exceljet.net/formulas/maximum-if-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/maximum-change)
    
*   [Next](https://exceljet.net/formulas/maximum-value)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Maximum if multiple criteria
============================

by Dave Bruns · Updated 29 Apr 2025

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[IF](https://exceljet.net/functions/if-function)

[MAXIFS](https://exceljet.net/functions/maxifs-function)

[FILTER](https://exceljet.net/functions/filter-function)

![Excel formula: Maximum if multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/maximum_if_multiple_criteria.png "Excel formula: Maximum if multiple criteria")

Summary
-------

To get the maximum value in a set of data that meets multiple criteria, you can use a formula based on the [MAXIFS function](https://exceljet.net/functions/maxifs-function)
. In the example shown, the formula in H5 is:

    =MAXIFS(data[Value],data[Group],F5,data[Temp],"<"&G5)
    

With "A" in cell F5 and the number 73 in cell G5, the result is 88. This is the maximum value in group "A" below a temperature of 73.

Generic formula
---------------

    =MAXIFS(data,range1,criteria1,range2,criteria2)

Explanation 
------------

In this example, the goal is to get the maximum value for a given group below a specific temperature. In other words, we want the max value after applying multiple criteria. The easiest way to solve this problem is with the MAXIFS function. However, if you need more flexibility (i.e., you need to work with arrays and not ranges), you can use the MAX function with the FILTER function. In older versions of Excel without MAXIFS or FILTER, you can use a traditional [array formula](https://exceljet.net/glossary/array-formula)
 based on the MAX function and the IF function. Each approach is explained below.

### Excel Table

For convenience, all data is in an [Excel Table](https://exceljet.net/glossary/excel-table)
 named **data** in the range B5:D16. Excel Tables are a convenient way to work with data in Excel because they (1) automatically expand to include new data and (2) offer [structured references](https://exceljet.net/glossary/structured-reference)
, which allow you to refer to data by name instead of by address. If you are new to Excel Tables, [this article provides an overview](https://exceljet.net/articles/excel-tables)
.

> Video: [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)

### MAXIFS function

One way to solve this problem is with the [MAXIFS functio](https://exceljet.net/functions/maxifs-function)
n, which can get the maximum value in a range based on one or more criteria. The generic syntax for MAXIFS with two conditions looks like this:

    =MAXIFS(max_range,range1,criteria1,range2,criteria2)
    

Note that each condition is defined by two [arguments](https://exceljet.net/glossary/function-argument)
: _range1_ and _criteria1_ define the first condition, and _range2_ and _criteria2_ define the second condition. All conditions must be true in order for the value to be considered. We start off with the _max\_range_, which is the Value column in the table:

    =MAXIFS(data[Value],

Next, we add criteria to test for the group value entered in cell F5:

    =MAXIFS(data[Value],data[Group],F5

If we enter the formula above as-is, we will get the maximum value in group "A". Next, we need to add a second condition to further restrict values below the temperature entered in cell G5:

    =MAXIFS(data[Value],data[Group],F5,data[Temp],"<"&G5)

Notice we need to concatenate the less than operator ("<") to cell F5. This is a requirement of the MAXIFS function, which uses an [unusual formula syntax](https://exceljet.net/articles/excels-racon-functions)
 shared by SUMIFS, COUNTIFS, etc. When we enter this formula, it returns the maximum value in group "A" below a temperature of 73. For reference, the same formula with conditions hardcoded looks like this:

    =MAXIFS(data[Value],data[Group],"A",data[Temp],"<73")

> MAXIFS will automatically _ignore_ empty cells that meet the criteria. In other words, MAXIFS will not treat empty cells that meet the criteria as zero. On the other hand, MAXIFS _will_ return zero (0) if no cells match the given criteria.

The MAXIFS function works well, but it does have one significant limitation: the range arguments inside MAXIFS must be actual _ranges_, you can't substitute _arrays_. If you need to use arrays, see the MAX + FILTER option below.

### MAX + FILTER

In the [dynamic array version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, another way to solve this problem is with [MAX](https://exceljet.net/functions/max-function)
 and [FILTER,](https://exceljet.net/functions/filter-function)
 like this:

    =MAX(FILTER(data[Value],(data[Group]=F5)*(data[Temp]<G5)))

Inside the MAX function, the FILTER function is configured to filter values by group and temperature:

    FILTER(data[Value],(data[Group]=F5)*(data[Temp]<G5))

_Array_ is provided as the Value column in the table. The _include_ argument is a simple expression:

    (data[Group]=F5)*(data[Temp]<G5)

This is an example of using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 in Excel. Because there are 12 values in the table, each expression above generates an array of 12 TRUE and FALSE values like this:

    {TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE}*{TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}

The math operation of multiplication (\*) converts the TRUE and FALSE values to 1s and 0s:

    {1;0;0;1;0;0;1;0;0;1;0;0}*{1;1;1;1;1;1;0;0;0;0;0;0}

And the result is a single array as the _include_ argument, like this:

    FILTER(data[Value],{1;0;0;1;0;0;0;0;0;0;0;0})

Note that the 1s in this array correspond to values that are in group "A" with a temperature below 73. FILTER returns the two values that meet these criteria directly to the MAX function:

    =MAX({83;88})

And MAX returns 88 as a final result. The primary advantage of using the MAX function with the FILTER function is that you don't need to provide a _range_ of values on the worksheet. You can instead provide an _array_ of values created with another operation. This is important when source data needs to be manipulated before a max value is calculated.

### MAX + IF

In older versions of Excel that do not have the MAXIFS function or the FILTER function, you can solve this problem with an [array formula](https://exceljet.net/glossary/array-formula)
 based on the [MAX function](https://exceljet.net/functions/max-function)
 and the [IF function,](https://exceljet.net/functions/if-function)
 like this:

    =MAX(IF((data[Group]=F5)*(data[Temp]<G5),data[Value]))

_Note: This is an_ [_array formula_](https://exceljet.net/videos/what-is-an-array-formula)
 _and must be entered with control + shift + enter in_ [_Legacy Excel_](https://exceljet.net/glossary/legacy-excel)
_._

Working from the inside out, the [IF function](https://exceljet.net/functions/if-function)
 is evaluated first. The logical test inside IF is exactly the same as the logic explained above for FILTER:

    (data[Group]=F5)*(data[Temp]<G5) // logical test
    

After the logic is evaluated, we have an array of 1s and 0s like this:

    =MAX(IF({1;0;0;1;0;0;0;0;0;0;0;0},data[Value]))

The 1s correspond to rows where the group is "A" and the temperature is less than 73. The final result from IF is an [array](https://exceljet.net/glossary/array)
 like this:

    {83;FALSE;FALSE;88;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

Looking at the values in this array, you can see that the IF function acts like a filter: only values associated with group "A" and a temperature less than 73 make it through the filter. The other values are replaced with FALSE. The IF function delivers this array directly to the [MAX function](https://exceljet.net/functions/max-function)
:

    =MAX({83;FALSE;FALSE;88;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE})

The MAX function automatically ignores FALSE values and returns the maximum number in the array: 88.

### Alternative syntax with nested IFs

The array formula above uses [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 to streamline the formula, but another option you might run into is [nesting](https://exceljet.net/glossary/nesting)
 one IF formula inside another, like this:

    =MAX(IF(data[Group]=F5,IF(data[Temp]<G5,data[Value])))
    

_Note: This is an_ [_array formula_](https://exceljet.net/videos/what-is-an-array-formula)
 _and must be entered with control + shift + enter in_ [_Legacy Excel_](https://exceljet.net/glossary/legacy-excel)
_._

Each IF formula applies a separate condition, so the values are filtered in two steps instead of one. This works fine, but the formula gets more complicated as additional criteria are added, since each condition requires another IF function. The advantage Boolean logic version of the formula is that you can add additional criteria without adding more IF functions.

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

[![Excel formula: Get next scheduled event](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20next%20scheduled%20event.png "Excel formula: Get next scheduled event")](https://exceljet.net/formulas/get-next-scheduled-event)

### [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)

The first part of the solution uses the MIN and TODAY functions to find the "next date" based on the date today. This is done by filtering the dates through the IF function: IF((date>=TODAY()),date) The logical test generates an array of TRUE / FALSE values, where TRUE corresponds to dates greater...

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel MAXIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxifs%20function.png "Excel MAXIFS function")](https://exceljet.net/functions/maxifs-function)

### [MAXIFS Function](https://exceljet.net/functions/maxifs-function)

The Excel MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MAXIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20maximum%20and%20minimum%20values-thumb.png)](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

### [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

In this video we'll look at how to calculate minimum and maximum values in Excel. Let's take a look. Here we have a list of properties, that includes an address, a price, and a variety of other information. Let's calculate the maximum and minimum values in this list. First, I'm going to create a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20operations%20in%20array%20formulas-Play.png)](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

In this video, we'll look at why boolean operations are important in array formulas. Boolean operations are a key building block in the world of dynamic array formulas. To illustrate, let's look at some simple order data. Given the data shown, how can we total orders from Texas using an array...

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
    
*   [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [MAXIFS Function](https://exceljet.net/functions/maxifs-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Videos

*   [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
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