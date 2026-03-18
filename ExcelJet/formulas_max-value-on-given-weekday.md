# Max value on given weekday - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/max-value-on-given-weekday

---

[Skip to main content](https://exceljet.net/formulas/max-value-on-given-weekday#main-content)

[](https://exceljet.net/formulas/max-value-on-given-weekday#)

*   [Previous](https://exceljet.net/formulas/max-value-ignore-all-errors)
    
*   [Next](https://exceljet.net/formulas/max-value-with-variable-column)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Max value on given weekday
==========================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[TEXT](https://exceljet.net/functions/text-function)

[MAX](https://exceljet.net/functions/max-function)

[IF](https://exceljet.net/functions/if-function)

[AGGREGATE](https://exceljet.net/functions/aggregate-function)

![Excel formula: Max value on given weekday](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/max_value_on_given_weekday.png "Excel formula: Max value on given weekday")

Summary
-------

To get the maximum value that occurs on a given weekday (i.e. Monday, Tuesday, Wednesday, Thursday, or Friday) you can use a formula based on the [FILTER function](https://exceljet.net/functions/filter-function)
 and the [MAX function](https://exceljet.net/functions/max-function)
. In the example shown, the formula in cell F5 is:

    =MAX(FILTER(values,TEXT(dates,"ddd")=F4))

Where **dates** (B5:B16) and **values** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
. With "Thu" in cell F4, the result is 95, the maximum value that appears on a Thursday in the data as shown.

Generic formula
---------------

    =MAX(FILTER(values,TEXT(dates,"ddd")=A1))

Explanation 
------------

In this example, the goal is to calculate the maximum value that occurs in a set of data on a given weekday (i.e. Monday, Tuesday, Wednesday, Thursday, Friday). In the current version of Excel, the simplest approach is to use the FILTER function. In older versions of Excel, you can use a traditional [array formula](https://exceljet.net/glossary/array-formula)
 based on the MAX function with the IF function. Both approaches are explained below.

### FILTER function

The most straightforward way to solve this problem is with the [FILTER function](https://exceljet.net/functions/filter-function)
, the [MAX function](https://exceljet.net/functions/max-function)
, and the [TEXT function](https://exceljet.net/functions/text-function)
. In the example shown, the formula in cell F5 is:

    =MAX(FILTER(values,TEXT(dates,"ddd")=F4))

Working from the inside out, the TEXT function is configured to compare the "day" for each date, abbreviated to three letters, with the day value in cell F4:

    TEXT(dates,"ddd")=F4)

Here, the TEXT function is using the [custom number format](https://exceljet.net/articles/custom-number-formats)
 "mmm" to calculate day abbreviations for the dates. Because there are 12 dates in dates (B5:B16) the TEXT function returns an array of 12 abbreviations like this:

    {"Thu";"Fri";"Mon";"Tue";"Wed";"Thu";"Fri";"Mon";"Tue";"Wed";"Thu";"Fri"}=F4

When this array is compared to cell F4, the result is an array that contains 12 TRUE and FALSE values:

    {TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE}

In this array, the TRUE values correspond to dates that are Thursdays in the data. This array is returned directly to the FILTER function as the _include_ argument with the named range values (C5:C16) as the _array_ argument. FILTER uses the array to "filter" the values and returns the three values that occur on Thursdays directly to the MAX function:

    =MAX({85;95;89})

MAX then returns 95 as a final result. If the value in F4 is changed to another day, the formula calculates a new result.

### Legacy Excel

In older versions of Excel without the FILTER function, you can use a traditional array formula based on the MAX function and the IF function:

    =MAX(IF(TEXT(dates,"ddd")=F4,values))

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

Working from the inside out, the [TEXT function](https://exceljet.net/functions/text-function)
 is used to extract a weekday value for each date:

    =TEXT(dates,"ddd")
    

The text string "ddd" is a [number format](https://exceljet.net/glossary/number-format)
 for abbreviated day names. Because there are 12 dates in B5:B16, the result is an [array](https://exceljet.net/glossary/array)
 with 12 abbreviated day names, which is then compared to cell F4:

    {"Thu";"Fri";"Mon";"Tue";"Wed";"Thu";"Fri";"Mon";"Tue";"Wed";"Thu";"Fri"}=F4

With "Thu" in F4, this operation results in another array that contains only TRUE and FALSE values:

    {TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE}

Note each TRUE corresponds to a Thursday. This array is returned to the [IF function](https://exceljet.net/functions/if-function)
 as the _logical\_test_. IF then acts as a filter to screen out values on _other_ days of the week. The final result from IF, which is returned directly to the [MAX function](https://exceljet.net/functions/max-function)
, looks like this:

    =MAX({85;FALSE;FALSE;FALSE;FALSE;95;FALSE;FALSE;FALSE;FALSE;85;FALSE})

Note the only values that survive the trip through IF are those associated with Thursdays, the other values are now FALSE. MAX automatically ignores FALSE values and returns the highest remaining value, 95.

### With AGGREGATE

For a more geeky formula that _does not_ require control + shift + enter in Legacy Excel, you can use the [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
 like this:

    =AGGREGATE(14,6,values/(TEXT(dates,"ddd")=F4),1)
    

Here we give AGGREGATE 14 for the _function_ argument ([LARGE](https://exceljet.net/functions/large-function)
) and 6 for _option_ argument (ignore errors). Then we build a logical expression using the TEXT function to check all dates for Thursdays. The result of this operation is an array of TRUE/FALSE values, which become the denominator of the original values. When used in a math operation, FALSE evaluates as zero, and throws a #DIV/0! error. TRUE evaluates as 1 and returns the original value. The final array of values and errors acts like a filter. AGGREGATE ignores all errors and returns the largest (maximum) of the surviving values.

_Note: The reason this formula works in older versions of Excel without being entered as an array formula is that AGGREGATE, [like the SUMPRODUCT function](https://exceljet.net/articles/why-sumproduct)
, can handle many array operations natively. In the future, this use of AGGREGATE will diminish since the new [dynamic array engine in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 makes this kind of workaround unnecessary._

### MAXIFS function

You might wonder why we aren't using the [MAXIFS function](https://exceljet.net/functions/maxifs-function)
, which can calculate a maximum value based on one or more criteria. The problem is that MAXIFS is a [_ranged-based function_](https://exceljet.net/articles/excels-racon-functions)
, and won't accept an array from another function like TEXT. If you want to use MAXIFS, you could add a [helper column](https://exceljet.net/glossary/helper-column)
 to the data that calculates weekday abbreviations with TEXT, then use MAXIFS with the helper column as the criteria range.

Related formulas
----------------

[![Excel formula: Max by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_by_month.png "Excel formula: Max by month")](https://exceljet.net/formulas/max-by-month)

### [Max by month](https://exceljet.net/formulas/max-by-month)

In this example, the goal is to get the maximum value in the data for each month listed in column E. The easiest way to do this is with the MAXIFS function, which is designed to return a maximum value based on one or more criteria. In older versions of Excel without the MAXIFS function, you can use...

[![Excel formula: Minimum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value_if_0.png "Excel formula: Minimum value if")](https://exceljet.net/formulas/minimum-value-if)

### [Minimum value if](https://exceljet.net/formulas/minimum-value-if)

In this example, the goal is to get the minimum value for each group in the data as shown. The easiest way to solve this problem is with the MINIFS function. However, there are actually several options. If you need more flexibility (you need to work with arrays instead of ranges), you can use the...

[![Excel formula: Maximum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value.png "Excel formula: Maximum value")](https://exceljet.net/formulas/maximum-value)

### [Maximum value](https://exceljet.net/formulas/maximum-value)

In this example, the goal is to get the maximum quiz score (i.e. the best quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MAX function or the LARGE function, as explained below. MAX function The MAX function accepts...

[![Excel formula: Minimum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value.png "Excel formula: Minimum value")](https://exceljet.net/formulas/minimum-value)

### [Minimum value](https://exceljet.net/formulas/minimum-value)

In this example, the goal is to get the minimum quiz score (i.e. the lowest quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MIN function or the SMALL function, as explained below. MIN function The MIN function...

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

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel AGGREGATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20aggregate%20function.png "Excel AGGREGATE function")](https://exceljet.net/functions/aggregate-function)

### [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)

The Excel AGGREGATE function returns an aggregate calculation like AVERAGE, COUNT, MAX, etc., optionally ignoring hidden rows and errors. A total of 19 operations are available, specified by function number in the first argument (see table for options).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Max by month](https://exceljet.net/formulas/max-by-month)
    
*   [Minimum value if](https://exceljet.net/formulas/minimum-value-if)
    
*   [Maximum value](https://exceljet.net/formulas/maximum-value)
    
*   [Minimum value](https://exceljet.net/formulas/minimum-value)
    
*   [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)
    
*   [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)
    
*   [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)
    

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