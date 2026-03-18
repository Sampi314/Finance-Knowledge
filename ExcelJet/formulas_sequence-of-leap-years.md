# Sequence of leap years - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sequence-of-leap-years

---

[Skip to main content](https://exceljet.net/formulas/sequence-of-leap-years#main-content)

[](https://exceljet.net/formulas/sequence-of-leap-years#)

*   [Previous](https://exceljet.net/formulas/sequence-of-days)
    
*   [Next](https://exceljet.net/formulas/sequence-of-months)
    

[Date series](https://exceljet.net/formulas#Date-series)

Sequence of leap years
======================

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[LET](https://exceljet.net/functions/let-function)

[FILTER](https://exceljet.net/functions/filter-function)

[MOD](https://exceljet.net/functions/mod-function)

[BYROW](https://exceljet.net/functions/byrow-function)

[AND](https://exceljet.net/functions/and-function)

[OR](https://exceljet.net/functions/or-function)

![Excel formula: Sequence of leap years](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sequence_of_leap_years.png "Excel formula: Sequence of leap years")

Summary
-------

To generate a list of leap years between two given years, you can use a formula based on the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 and the [FILTER function](https://exceljet.net/functions/filter-function)
. In the example shown, the formula in D5 is:

    =LET(
    start,B5,
    end,B8,
    years,SEQUENCE(end-start+1,,start),
    leaps,(MOD(years,400)=0)+((MOD(years,4)=0)*(MOD(years,100)<>0)),
    FILTER(years,leaps))

The result is a list of the 13 leap years between 1980 and 2030. If the values for _start_ (B5) and _end_ (B8) are updated, a new list of leap years will be generated.

Generic formula
---------------

    =LET(
    start,1980,
    end,2030,
    years,SEQUENCE(end-start+1,,start),
    leaps,(MOD(years,400)=0)+((MOD(years,4)=0)*(MOD(years,100)<>0)),
    FILTER(years,leaps))

Explanation 
------------

In this example, the goal is to generate a list of leap years between a given start year and end year. The worksheet is set up so that the start year is an input in cell B5 and the end year is an input in cell B8. If either value changes, the formula should generate a new list of leap years. In the current version of Excel, the easiest way to do this is with the SEQUENCE function and the FILTER function in a formula like this:

    =LET(
    start,B5,
    end,B8,
    years,SEQUENCE(end-start+1,,start),
    leaps,(MOD(years,400)=0)+((MOD(years,4)=0)*(MOD(years,100)<>0)),
    FILTER(years,leaps))

At a high level, this formula uses the SEQUENCE function to generate a list of all years between the start and end. Then it checks for leap years using logic implemented with the MOD function and filters out all non-leap years. At the start, the [LET function](https://exceljet.net/functions/let-function)
 defines four variables:

*   _start_ - the start year entered in cell B5
*   _end_ - the end year entered B8
*   _years_ - a sequence of all years between the start and end year
*   _leaps_ - a logical test that flags all leap years

Using LET this way keeps the formula efficient and readable. For example, the calculation for _years_ (see below) only runs one time, even though it is used four times in the formula.

### Generating a list of years

The next step in solving this problem is to generate a complete list of all years between the start and end years. We can do this with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
, which is designed to create numeric arrays. For example, to generate the numbers 1 through 10, you can use SEQUENCE like this:

    =SEQUENCE(10) // returns {1;2;3;4;5;6;7;8;9;10}

To create a list of numbers between a given _start_ and _end_, we can use a generic pattern like this:

    =SEQUENCE(end-start+1,,start)

With the start year given as 1980 and the end year given as 2030, we have:

    =SEQUENCE(end-start+1,,start)
    =SEQUENCE(2030-1980+1,,1980)
    =SEQUENCE(50+1,,1980)
    =SEQUENCE(51,,1980)

The result is an array with the 51 years between 1980 and 2020, inclusive:

    {1980;1981;1982;1983;1984;1985;1986;1987;1988;1989;1990;1991;1992;1993;1994;1995;1996;1997;1998;1999;2000;2001;2002;2003;2004;2005;2006;2007;2008;2009;2010;2011;2012;2013;2014;2015;2016;2017;2018;2019;2020;2021;2022;2023;2024;2025;2026;2027;2028;2029;2030}

This array is then assigned to the _years_ variable defined by LET.

### Testing for leap years

The next step is to test each year in _years_ to identify leap years. This is done with the following snippet:

    (MOD(years,400)=0)+((MOD(years,4)=0)*(MOD(years,100)<>0))

This logic here is based on the following leap year rule, which is explained in detail [on this page](https://exceljet.net/formulas/year-is-a-leap-year)
:

_To be a leap year, the year number must be divisible by four, except for end-of-century years, which must be divisible by 400. This means that 2000 is a leap year, but 1700, 1800, and 1900 are not leap years._

The test is implemented with [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
 and the [MOD function](https://exceljet.net/functions/mod-function)
 as follows:

1.  If the year is divisible by 400, it's a leap year (TRUE).
2.  Or if the year is divisible by 4 and not divisible by 100, it's a leap year (TRUE)
3.  Otherwise, the year is not a leap year (FALSE).

The result is an array of 51 TRUE and FALSE values. The TRUE values in this array correspond to leap years in the original _years_ array, and the FALSE values indicate non-leap years. The array is assigned to the _leaps_ variable defined by LET.

### Removing the non-leap years

The final step is removing non-leap years, which is done with the [FILTER function](https://exceljet.net/functions/filter-function)
 like this:

    FILTER(years,leaps)

Recall that the two arrays, _years_ and _leaps_, are the same size; each array contains 51 rows. The FILTER function uses the _leaps_ array to filter out non-leap years. The final result is an array that contains only leap years. This array lands in cell D5 and spills down the worksheet. If the values for _start_ (B5) or _end_ (B8) are changed, the entire process is repeated and a new list of leap years is generated.

### Pro-tip: implement AND and OR

The formula above uses [Boolean algebra](https://exceljet.net/glossary/boolean-logic)
 to test for leap years, a compact yet cryptic way to apply conditions based on AND and OR logic. However, if you look at the [formula explained here](https://exceljet.net/formulas/year-is-a-leap-year)
 (which tests a single year) you'll notice that it uses the [AND function](https://exceljet.net/functions/and-function)
 and the [OR function](https://exceljet.net/functions/or-function)
 instead:

    =OR(MOD(A1,400)=0,AND(MOD(A1,4)=0,MOD(A1,100)<>0))

Can we use this same approach here? We can, but we need to adjust the formula first. AND and OR are "aggregating functions", which means they return a _single_ aggregated result. This won't work in this case, because we are running a test on 51 years and need to get 51 results back in a single array so FILTER can use the array to remove non-leap years. The solution is to implement the AND and OR inside the [BYROW function](https://exceljet.net/functions/byrow-function)
 like this:

    =LET(
    start,B5,
    end,B8,
    years,SEQUENCE(end-start+1,,start),
    leaps,BYROW(years,LAMBDA(y,OR(MOD(y,400)=0,AND(MOD(y,4)=0,MOD(y,100)<>0)))),
    FILTER(years,leaps))

In this version, _leaps_ is defined with BYROW like this:

    BYROW(years,LAMBDA(y,OR(MOD(y,400)=0,AND(MOD(y,4)=0,MOD(y,100)<>0))))

BYROW processes values in a row-by-row fashion, so each year (defined as y above) is tested separately. The result for each year is a _single_ TRUE or FALSE value. The BYROW function packages the results into a single array, which we hand off to FILTER as before.

> There is no difference in the output from both versions of the formula. The choice of which to use is a personal preference.

Related formulas
----------------

[![Excel formula: Sequence of years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence%20of%20years.png "Excel formula: Sequence of years")](https://exceljet.net/formulas/sequence-of-years)

### [Sequence of years](https://exceljet.net/formulas/sequence-of-years)

The goal is to generate a series of dates one year apart. In the current version of Excel, the easiest way to do this is with the SEQUENCE function together with the DATE, YEAR, MONTH, and DAY functions. In older versions of Excel, you can use the same date functions and a more manual approach...

[![Excel formula: Year is a leap year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/year_is_leap_year.png "Excel formula: Year is a leap year")](https://exceljet.net/formulas/year-is-a-leap-year)

### [Year is a leap year](https://exceljet.net/formulas/year-is-a-leap-year)

In this example, the goal is to write a formula that will return TRUE if a year is a leap year and FALSE if not. This is a surprisingly challenging problem in Excel for two reasons: (1) Excel thinks 1900 is a leap year due to a long-standing bug inherited from Lotus 1-2-3 and (2) The logic for...

Related functions
-----------------

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

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

*   [Sequence of years](https://exceljet.net/formulas/sequence-of-years)
    
*   [Year is a leap year](https://exceljet.net/formulas/year-is-a-leap-year)
    

### Functions

*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
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