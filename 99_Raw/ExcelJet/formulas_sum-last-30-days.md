# Sum last 30 days - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-last-30-days

---

[Skip to main content](https://exceljet.net/formulas/sum-last-30-days#main-content)

[](https://exceljet.net/formulas/sum-last-30-days#)

*   [Previous](https://exceljet.net/formulas/sum-if-x-or-y)
    
*   [Next](https://exceljet.net/formulas/sum-last-n-columns)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum last 30 days
================

by Dave Bruns · Updated 30 Dec 2022

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[TODAY](https://exceljet.net/functions/today-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[FILTER](https://exceljet.net/functions/filter-function)

![Excel formula: Sum last 30 days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_last_30_days.png "Excel formula: Sum last 30 days")

Summary
-------

To sum values in the last 30 dates by date, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 together with the [TODAY function](https://exceljet.net/functions/today-function)
. In the example shown, the formula in E5, copied down, is:

    =SUMIFS(C5:C16,B5:B16,">="&TODAY()-30)
    

The result is $21,875. This is the total of amounts in column C that occur in the last 30 days, based on a current date of December 30, 2022.

Generic formula
---------------

    =SUMIFS(values,dates,">="&TODAY()-30)

Explanation 
------------

In this example, the goal is to calculate total amounts in column C that occur in the last 30 days, based on a current date of December 30, 2022. There are three basic approaches to solving this problem: (1) a traditional approach based on the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
, (2) a more flexible approach that uses [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 and the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
, a modern approach based on the [FILTER function](https://exceljet.net/functions/filter-function)
. Each approach is explained below.

### Excel date logic

To understand the logic of the formulas explained below, the first step is to understand Excel's date system, where [dates are serial numbers](https://exceljet.net/glossary/excel-date)
 beginning on January 1, 1900. January 1, 1900 is 1, January 2, 1900 is 2, and so on. More recent dates are much larger numbers. For example, January 1, 1999 is 36161, January 1, 2010 is 40179, and January 1, 2020 is 43831. Because dates are just numbers, you can easily perform arithmetic on dates. For example, with January 1, 2020 in cell A1:

    =A1+10 // Jan 11, 2020
    =A1-10 // Dec 22, 2019

This also means we can use the [TODAY function](https://exceljet.net/functions/today-function)
 to return the current date, then subtract 30 days to get a date 30 days earlier. For example, as I write this, the current date is December 30, 2022 so:

    =TODAY() // Dec 30, 2022
    =TODAY()-30 // Nov 30, 2022

Therefore, to test if a date in cell A1 occurs within the last 30 days, we can use a formula like this:

    =A1>=TODAY()-30

The above will return TRUE if the date is within the last 30 days of the current date and FALSE if not.

### SUMIFS function

As mentioned above, the traditional way to solve a problem like this is to use the SUMIFS function. The SUMIFS function sums cells in a [range](https://exceljet.net/glossary/range)
 that meet one or more conditions, referred to as _criteria_. To apply criteria, the SUMIFS function supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. The generic syntax for SUMIFS looks like this:

    =SUMIFS(sum_range,range1,criteria1) // 1 condition

where _sum\_range_ contains the values to sum, _range_ is the cell range to test, and _criteria1_ is the criteria to apply to _range_. To solve this problem, we begin with the _sum\_range_, which is C5:C16:

    =SUMIFS(C5:C16,

Next, we add the range, which contains the dates in B5:B16:

    =SUMIFS(C5:C16,B5:B16,

Finally, we add the criteria:

    =SUMIFS(C5:C16,B5:B16,">="&TODAY()-30)

This is the tricky part of the formula because the [operator](https://exceljet.net/glossary/logical-operators)
 must be enclosed in double quotes (">=") and [concatenated](https://exceljet.net/glossary/concatenation)
 to the [TODAY function](https://exceljet.net/functions/today-function)
 less 30. This is because the SUMIFS function is in a group of [eight functions](https://exceljet.net/articles/excels-racon-functions)
 that split logical criteria into two parts. You can read more about the details of using logical operators with SUMIFS, [see this page](https://exceljet.net/functions/sumifs-function)
.

### SUMPRODUCT function

Another way to solve this problem is with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 like this:

    =SUMPRODUCT((B5:B16>=TODAY()-30)*C5:C16)

In this case, we are multiplying all values in C5:C16 by an expression designed to "zero out" values that should not be included in the final sum:

    (B5:B16>=TODAY()-30)

The result from the expression above is an array of TRUE and FALSE values like this:

    {TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}

The TRUE values in this array represent dates that occur in the last 30 days, based on a current date of December 30, 2022 returned by the TODAY function. These are the first five dates in the data as shown.

Next, the array above is multiplied by the values in C5:C16. In Excel, TRUE and FALSE values are automatically coerced to 1s and 0s by any math operation, so the multiplication step converts the arrays above to ones and zeros. We can visualize this operation inside of SUMPRODUCT like this:

    =SUMPRODUCT({1;1;1;1;1;0;0;0;0;0;0;0}*C5:C16)

After multiplication, we have just a single array:

    =SUMPRODUCT({5550;7450;1000;725;7150;0;0;0;0;0;0;0})

Notice that values associated with dates that are not within the past 30 days have been "zeroed out". With just one array to process, SUMPRODUCT returns the sum of all items in the array: 21,875.

_Note: Why would you use SUMPRODUCT instead of SUMIFS? The biggest reason is flexibility. Unlike SUMPRODUCT, SUMIFS [requires a cell range](https://exceljet.net/articles/excels-racon-functions)
; you can't use an array. This means SUMIFS won't work in [formulas that need to manipulate values](https://exceljet.net/formulas/sum-by-weekday)
 before conditional logic is applied._

### FILTER function

In the latest version of Excel, you can solve this problem with the [FILTER function](https://exceljet.net/functions/filter-function)
 like this:

    =SUM(FILTER(C5:C16,B5:B16>=TODAY()-30,0))

In this formula, we use the same logic explained above to target dates in the past 30 days:

    B5:B16>=TODAY()-30 // last 30 days

The expression above returns an array of TRUE and FALSE values like this:

    {TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}

And this array is used to filter the values in C5:C16. The result from FILTER is then returned directly to the SUM function:

    =SUM({5550;7450;1000;725;7150})

SUM then returns a final result of 21,875.

Video: [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

Related formulas
----------------

[![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")](https://exceljet.net/formulas/sum-by-month)

### [Sum by month](https://exceljet.net/formulas/sum-by-month)

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the SUMIFS function , which can sum numeric values based on multiple criteria. The second approach is based on the SUMPRODUCT...

[![Excel formula: Sum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_multiple_criteria.png "Excel formula: Sum if multiple criteria")](https://exceljet.net/formulas/sum-if-multiple-criteria)

### [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)

In this example, the goal is to sum the values in F5:F16 when the Color in C5:C16 is "Red" and the State in D5:D16 is "TX". This is an example of a conditional sum with multiple criteria and the SUMIFS function is the easiest way to solve this problem. SUMIFS function The SUMIFS function sums cells...

[![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")](https://exceljet.net/formulas/sum-by-month)

### [Sum by month](https://exceljet.net/formulas/sum-by-month)

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the SUMIFS function , which can sum numeric values based on multiple criteria. The second approach is based on the SUMPRODUCT...

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Sum by weekday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20weekday.png "Excel formula: Sum by weekday")](https://exceljet.net/formulas/sum-by-weekday)

### [Sum by weekday](https://exceljet.net/formulas/sum-by-weekday)

In this example, the goal is to sum amounts by weekday. In other words, we want to sum amounts by Monday, Tuesday, Wednesday, and so on. Column B contains valid Excel dates formatted with a custom number format explained below. For convenience, all source data is in an Excel Table named data . The...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20operations%20in%20array%20formulas-Play.png)](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

In this video, we'll look at why boolean operations are important in array formulas. Boolean operations are a key building block in the world of dynamic array formulas. To illustrate, let's look at some simple order data. Given the data shown, how can we total orders from Texas using an array...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum by month](https://exceljet.net/formulas/sum-by-month)
    
*   [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)
    
*   [Sum by month](https://exceljet.net/formulas/sum-by-month)
    
*   [Sum by year](https://exceljet.net/formulas/sum-by-year)
    
*   [Sum by weekday](https://exceljet.net/formulas/sum-by-weekday)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

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