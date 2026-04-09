# Max by month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/max-by-month

---

[Skip to main content](https://exceljet.net/formulas/max-by-month#main-content)

[](https://exceljet.net/formulas/max-by-month#)

*   [Previous](https://exceljet.net/formulas/larger-of-two-values)
    
*   [Next](https://exceljet.net/formulas/max-of-every-nth-column)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Max by month
============

by Dave Bruns · Updated 28 Apr 2025

Related functions 
------------------

[MAXIFS](https://exceljet.net/functions/maxifs-function)

[MAX](https://exceljet.net/functions/max-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Max by month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/max_by_month.png "Excel formula: Max by month")

Summary
-------

To get the maximum value in a given month, you can use the [MAXIFS function](https://exceljet.net/functions/maxifs-function)
. In the example shown, the formula in F5 is:

    =MAXIFS(amount,date,">="&E5,date,"<"&EDATE(E5,1))
    

where **amount** (C5:C16) and **date** (B5:B16) are [named ranges](https://exceljet.net/glossary/named-range)
. As the formula is copied down, it returns the max value in each month listed in column E.

_Note: The values in E5:E10 are valid_ [_Excel dates_](https://exceljet.net/glossary/excel-date)
 _with the_ [_number format_](https://exceljet.net/glossary/number-format)
 _"mmm" applied._

Generic formula
---------------

    =MAXIFS(values,dates,">="&A1,dates,"<"&EDATE(A1,1))

Explanation 
------------

In this example, the goal is to get the maximum value in the data for each month listed in column E. The easiest way to do this is with the MAXIFS function, which is designed to return a maximum value based on one or more criteria. In older versions of Excel without the MAXIFS function, you can use a traditional array formula. The article below explains both approaches. For convenience only, the formulas below use the [named ranges](https://exceljet.net/glossary/named-range)
 **amount** (C5:C16) and **date** (B5:B16).

_Note: the values in E5:E10 are valid_ [_Excel dates_](https://exceljet.net/glossary/excel-date)
_, formatted to display the month name only with the_ [_number format_](https://exceljet.net/glossary/number-format)
 _"mmm". See below for more information._

### MAXIFS solution

The [MAXIFS function](https://exceljet.net/functions/maxifs-function)
 can get the maximum value in a range based on multiple criteria. The generic syntax looks like this:

    =MAXIFS(max_range,range1,criteria1,range2,criteria2,...)
    

Note that each condition is applied in pairs: _range1_ and _criteria1_ define the first condition, _range2_ and _criteria2_ define the second condition, and so on. In this problem, we need to configure MAXIFS to get the max value by month using two conditions: one for a start date, and one for an end date. We start off with the _max\_range_, which contains the values in **amount** (C5:C16):

    =SUMIFS(amount,

To enter the condition for the start date, we use the named range **date** (B5:B16) followed by a greater than or equal to operator (>=) [concatenated](https://exceljet.net/glossary/concatenation)
 to cell E5:

    =SUMIFS(amount,date,">="&E5,

This works because cell E5 already contains the first day of the month, formatted to display the month only. To enter the condition for the end date, we use the [EDATE function](https://exceljet.net/functions/edate-function)
 to advance one whole month to the _first day of the next month_:

    =EDATE(E5,1) // first of next month
    

We can then use the less than operator (<) to target the correct dates. The final formula in F5, copied down, is:

    =SUMIFS(amount,date,">="&E5,date,"<"&EDATE(E5,1))
    

Roughly translated, the meaning of this formula is "Get the maximum value in C6:C16 when the date in B5:B16 is greater than or equal to the date in E5 and less than the first day of the _next_ month". Notice we need to [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the dates to [logical operators](https://exceljet.net/glossary/logical-operators)
, as required by the MAXIFS function. As the formula is copied down, it returns the max value for each month listed in column E. The named ranges behave like [absolute references](https://exceljet.net/glossary/absolute-reference)
 and don't change, while the reference to E5 is [relative](https://exceljet.net/glossary/relative-reference)
 and changes at each new row.

> Another option would be to use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
>  to get the last day of the current month, then use "<=" as the second logical operator. However, because EOMONTH returns a date that is technically midnight, there is a danger of excluding [dates with times](https://exceljet.net/glossary/excel-datetime)
>  that occur on the last day of the month. Using EDATE is therefore simpler and more robust.

### With hardcoded dates

To use the MAXIFS function with hardcoded dates, the best approach is to use the [DATE function](https://exceljet.net/functions/date-function)
 like this:

    =MAXIFS(amount,date,">="&DATE(2023,1,1),date,"<"&DATE(2023,2,1))
    

This formula uses the DATE function to create the first day of January 2023 and the first day of February 2023. This is a safer option than entering a date as text, because it guarantees that Excel will interpret the date correctly.

### MAX with TEXT

In older versions of Excel without the MAXIFS function, another way to solve this problem is with the MAX function and the TEXT function in a traditional [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 like this:

    =MAX((TEXT(date,"mmyy")=TEXT(E5,"mmyy"))*amount)
    

_Note: this is an array formula and must be entered with control + shift + enter in_ [_Legacy Excel_](https://exceljet.net/glossary/legacy-excel)
_._

In this version, we use the [TEXT function](https://exceljet.net/functions/text-function)
 to convert the **dates** to [text strings](https://exceljet.net/glossary/text-value)
 in the format "mmyy". Because there are 12 dates in the list, the result is an [array](https://exceljet.net/glossary/array)
 with 12 values like this:

    {"0123";"0123";"0123";"0223";"0223";"0223";"0223";"0323";"0323";"0323";"0423";"0423"}
    

Next, the TEXT function is used in the same way to extract the month and year from the date in E5:

    TEXT(E5,"mmyy") // returns "0123"
    

The two results above are then compared to each other. The result is an array of TRUE and FALSE values like this:

    {TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}

The TRUE values in this array indicate dates in B5:B16 that are in the same month and year as the date in E5. This array is then multiplied by the values in **amount**. The math operation automatically coerces the TRUE and FALSE values to 1s and 0s, so the formula is evaluated like this:

    =MAX((TEXT(date,"mmyy")=TEXT(E5,"mmyy"))*amount)
    =MAX({1;1;1;0;0;0;0;0;0;0;0;0}*amount)
    =MAX({1000;500;1275;0;0;0;0;0;0;0;0;0})
    =1275
    

Note that the zeroes effectively cancel out values in other months, and the MAX function returns 1275 as the max value in January 2023. As the formula is copied down, the [relative reference](https://exceljet.net/glossary/relative-reference)
 E5 changes at each new row, and the formula returns a maximum amount for each date listed in column E. One nice feature of this formula is that it automatically tests for year and month, while ignoring day, making the logic simple and elegant. It would be nice to use this same logic inside the MAXIFS formula as well, but the MAXIFS function is in a group of [eight functions](https://exceljet.net/articles/excels-racon-functions)
 that won't accept an array operation as a range argument.

### Display dates as names

To display the dates in E5:E10 as names only, you can apply the [custom number format](https://exceljet.net/articles/custom-number-formats)
 "mmm". Select the dates, then use Control + 1 to bring up the [Format Cells Dialog](https://exceljet.net/shortcuts/format-almost-anything)
 box and apply the date format as shown below:

![Custom number format to display months in column E](https://exceljet.net/sites/default/files/images/formulas/inline/max_by_month_custom_number_format.png "Custom number format to display months in column E")

This allows you to use [valid Excel dates](https://exceljet.net/glossary/excel-date)
 in column E (required for the formula) and display them as you like.

### Pivot Table solution

A [pivot table](https://exceljet.net/articles/excel-pivot-tables)
 is another excellent solution when you need to summarize data by year, month, quarter, and so on, because it can do this kind of grouping for you without any formulas at all. For a side-by-side comparison of formulas vs. pivot tables, see this video: [Why pivot tables](https://exceljet.net/plc/why-pivot-tables)
.

Related formulas
----------------

[![Excel formula: Max value on given weekday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_value_on_given_weekday.png "Excel formula: Max value on given weekday")](https://exceljet.net/formulas/max-value-on-given-weekday)

### [Max value on given weekday](https://exceljet.net/formulas/max-value-on-given-weekday)

In this example, the goal is to calculate the maximum value that occurs in a set of data on a given weekday (i.e. Monday, Tuesday, Wednesday, Thursday, Friday). In the current version of Excel, the simplest approach is to use the FILTER function. In older versions of Excel, you can use a...

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

[![Excel MAXIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxifs%20function.png "Excel MAXIFS function")](https://exceljet.net/functions/maxifs-function)

### [MAXIFS Function](https://exceljet.net/functions/maxifs-function)

The Excel MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MAXIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and...

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

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

*   [Max value on given weekday](https://exceljet.net/formulas/max-value-on-given-weekday)
    
*   [Minimum value if](https://exceljet.net/formulas/minimum-value-if)
    
*   [Maximum value](https://exceljet.net/formulas/maximum-value)
    
*   [Minimum value](https://exceljet.net/formulas/minimum-value)
    
*   [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)
    
*   [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)
    
*   [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)
    

### Functions

*   [MAXIFS Function](https://exceljet.net/functions/maxifs-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

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