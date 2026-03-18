# Count dates by day of week - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-dates-by-day-of-week

---

[Skip to main content](https://exceljet.net/formulas/count-dates-by-day-of-week#main-content)

[](https://exceljet.net/formulas/count-dates-by-day-of-week#)

*   [Previous](https://exceljet.net/formulas/count-columns-that-contain-specific-values)
    
*   [Next](https://exceljet.net/formulas/count-dates-in-given-year)
    

[Count](https://exceljet.net/formulas#Count)

Count dates by day of week
==========================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Count dates by day of week](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Count%20dates%20by%20day%20of%20week.png "Excel formula: Count dates by day of week")

Summary
-------

To count dates by day of the week (i.e. count Mondays, Tuesdays, Wednesdays, etc.), you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 together with the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
. In the example shown, the formula in F5 is:

    =SUMPRODUCT(--(WEEKDAY(dates,2)=E5))
    

where "dates" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15. As the formula is copied down, it returns a count for each day shown in column D.

Generic formula
---------------

    =SUMPRODUCT(--(WEEKDAY(dates)=day_num))

Explanation 
------------

You might wonder why we aren't using [COUNTIF](https://exceljet.net/functions/countif-function)
 or [COUNTIFS](https://exceljet.net/functions/countifs-function)
. These functions seem like the obvious solution. However, without adding a helper column that contains a weekday value, there is no way to create criteria for COUNTIF to count weekdays in a range of dates. Instead, we use the versatile [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
, which handles [arrays](https://exceljet.net/glossary/array)
 gracefully without the need to use Control + Shift + Enter. We are using SUMPRODUCT with just one argument, which consists of this expression:

    --(WEEKDAY(dates,2)=E5)
    

Working from the inside out, the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
 is configured with the optional [argument](https://exceljet.net/glossary/function-argument)
 2, which causes it to return numbers 1-7 for the days Monday-Sunday, respectively. This makes it easier to list the days in order with the numbers in column E in sequence. WEEKDAY evaluates each date in **dates** (B5:B15) and returns a number. Because we are giving WEEKDAY 11 dates, we get back an [array](https://exceljet.net/glossary/array)
 that contains 11 results like this:

    {6;1;1;6;3;7;5;6;5;3;2}
    

Each number in this array corresponds to a day of the week, with Mondays equal to 1 and Sundays equal to 7. Next, the numbers returned by WEEKDAY are compared to the value in E5, which is 1:

    {6;1;1;6;3;7;5;6;5;3;2}=1
    

The result is an array of TRUE/FALSE values like this:

    {FALSE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

In this array, TRUE corresponds to dates that fall on Monday and FALSE represents other days of the week. SUMPRODUCT only works with numbers (not text or Booleans) so we use a [double-negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to coerce the TRUE/FALSE values to 1s and 0s. The result is delivered directly to the SUMPRODUCT function:

    =SUMPRODUCT({0;1;1;0;0;0;0;0;0;0;0}) // returns 2
    

With just one array to process, SUMPRODUCT sums the items and returns 2 as a final result, since there are two Mondays in the dates.

### Dealing with blank dates

If you have blank cells in the list of dates, you will get incorrect results, since the WEEKDAY function will return a result even when there is no date. To handle empty cells, you can adjust the formula as follows:

    =SUMPRODUCT((WEEKDAY(dates,2)=E5)*(dates<>""))
    

Multiplying by the expression (dates<>"") is one way to "cancel out" empty cells.

### Without day numbers

The day numbers in column E make the formula easier to understand and write. However, since the day names are already in the range D5:D11, which is named **days**, it is possible to write a formula that doesn't use column E at all by using the MATCH function like this:

    =SUMPRODUCT(--(WEEKDAY(dates,2)=MATCH(D5,days,0)))
    

This works because the [MATCH function](https://exceljet.net/functions/match-function)
 simply returns the position of each day name in **days**:

    MATCH(D5,days,0) // returns 1
    MATCH(D6,days,0) // returns 2
    MATCH(D7,days,0) // returns 3
    

Otherwise, the formula works the same way and returns the same counts as the original formula.

Related formulas
----------------

[![Excel formula: Sum by weekday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20weekday.png "Excel formula: Sum by weekday")](https://exceljet.net/formulas/sum-by-weekday)

### [Sum by weekday](https://exceljet.net/formulas/sum-by-weekday)

In this example, the goal is to sum amounts by weekday. In other words, we want to sum amounts by Monday, Tuesday, Wednesday, and so on. Column B contains valid Excel dates formatted with a custom number format explained below. For convenience, all source data is in an Excel Table named data . The...

[![Excel formula: Count day of week between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20day%20of%20week%20between%20dates.png "Excel formula: Count day of week between dates")](https://exceljet.net/formulas/count-day-of-week-between-dates)

### [Count day of week between dates](https://exceljet.net/formulas/count-day-of-week-between-dates)

At the core, this formula uses the WEEKDAY function to test a number of dates to see if they land on a given day of week (dow) and the SUMPRODUCT function to tally up the total. When given a date, WEEKDAY simply returns a number between 1 and 7 that corresponds to a particular day of the week. With...

[![Excel formula: Count birthdays by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20birthdays%20by%20month.png "Excel formula: Count birthdays by month")](https://exceljet.net/formulas/count-birthdays-by-month)

### [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)

You would think you could use the COUNTIF function to count birthdays, but the trouble is COUNTIF only works with ranges , and won't let you use something like MONTH to extract just the month number from dates. So, we use the SUMPRODUCT function with custom logic instead. Inside SUMPRODUCT, we have...

[![Excel formula: Count dates in given year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20dates%20in%20given%20year.png "Excel formula: Count dates in given year")](https://exceljet.net/formulas/count-dates-in-given-year)

### [Count dates in given year](https://exceljet.net/formulas/count-dates-in-given-year)

The YEAR function extracts the year from a valid Excel date . For example: =YEAR("15-Jun-2021") // returns 2021 In this case, we are giving YEAR and array of dates in the named range dates : YEAR(dates) Because dates contains 11 cells, we get back 11 results in an array like this: {2018;2017;2019;...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum by weekday](https://exceljet.net/formulas/sum-by-weekday)
    
*   [Count day of week between dates](https://exceljet.net/formulas/count-day-of-week-between-dates)
    
*   [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)
    
*   [Count dates in given year](https://exceljet.net/formulas/count-dates-in-given-year)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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