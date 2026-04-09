# Count dates in current month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-dates-in-current-month

---

[Skip to main content](https://exceljet.net/formulas/count-dates-in-current-month#main-content)

[](https://exceljet.net/formulas/count-dates-in-current-month#)

*   [Previous](https://exceljet.net/formulas/count-calls-at-specific-times)
    
*   [Next](https://exceljet.net/formulas/count-day-of-week-between-dates)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Count dates in current month
============================

by Dave Bruns · Updated 25 Feb 2021

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[N](https://exceljet.net/functions/n-function)

![Excel formula: Count dates in current month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20dates%20in%20current%20month.png "Excel formula: Count dates in current month")

Summary
-------

To count dates in the current month, you can use a formula based on the [COUNTIFS](https://exceljet.net/functions/countifs-function)
 or [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 function as explained below. In the example shown above, the formula in E7 is:

    =COUNTIFS(dates,">="&EOMONTH(TODAY(),-1)+1,dates,"<"&EOMONTH(TODAY(),0)+1)
    

where "dates" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B104.

Generic formula
---------------

    =COUNTIFS(rng,">="&EOMONTH(TODAY(),-1)+1,rng,"<"&EOMONTH(TODAY(),0)+1)

Explanation 
------------

At the core, this formula uses the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 to count dates that are greater than or equal to the first day of the _current_ month, and less than the first day of the _next_ month. The EOMONTH function is used to create both dates based on the current date, which is supplied by the [TODAY function](https://exceljet.net/functions/today-function)
.

    =COUNTIFS(dates,">="&EOMONTH(TODAY(),-1)+1,dates,"<"&EOMONTH(TODAY(),0)+1)
    

To get the first day of the month, we use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 like this:

    EOMONTH(TODAY(),-1)+1
    

EOMONTH returns the _last_ day of the _previous_ month, to which 1 is added to get the _first_ day of the _current_ month. In a similar way, we use EOMONTH to get the _first_ day of the _next_ month:

    EOMONTH(TODAY(),0)+1
    

EOMONTH returns the _last_ day of the _current_ month, to which 1 is added to get the _first_ day of the _next_ month. The literal translation of the logic in COUNTIFS is: _greater than or equal to the first day in the current month AND less than the first day of the next month._

Alternatively, you could use less than or equal (<=) [operator](https://exceljet.net/glossary/logical-operators)
 for the last day like this:

    =COUNTIFS(dates,">="&EOMONTH(TODAY(),-1)+1,dates,"<="&EOMONTH(TODAY(),0))
    

### Previous and next months

To count dates in the previous month:

    =COUNTIFS(dates,">="&EOMONTH(TODAY(),-2)+1,dates,"<"&EOMONTH(TODAY(),-1)+1) 
    

To count dates in the next month:

    =COUNTIFS(dates,">="&EOMONTH(TODAY(),0)+1,dates,"<"&EOMONTH(TODAY(),1)+1)
    

### SUMPRODUCT alternative

You can also count dates in the previous, current, and next month using [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 together with the [TEXT function](https://exceljet.net/functions/text-function)
 like this:

    =SUMPRODUCT(N(TEXT(EOMONTH(TODAY(),-1),"mmyy")=TEXT(rng,"mmyy")))
    =SUMPRODUCT(N(TEXT(TODAY(),"mmyy")=TEXT(rng,"mmyy")))
    =SUMPRODUCT(N(TEXT(EOMONTH(TODAY(),1),"mmyy")=TEXT(rng,"mmyy")))
    

Here, dates are fed into the TEXT function to get a month and year string, which is used for comparison in an array operation inside SUMPRODUCT. The result is an array of TRUE FALSE values, where TRUE represents dates in the month of interest.

The [N function](https://exceljet.net/functions/n-function)
 is used to [change these values to ones and zeros](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
, and SUMPRODUCT simply sums and returns the array.

Related formulas
----------------

[![Excel formula: Count dates by day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20dates%20by%20day%20of%20week.png "Excel formula: Count dates by day of week")](https://exceljet.net/formulas/count-dates-by-day-of-week)

### [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)

You might wonder why we aren't using COUNTIF or COUNTIFS . These functions seem like the obvious solution. However, without adding a helper column that contains a weekday value, there is no way to create criteria for COUNTIF to count weekdays in a range of dates. Instead, we use the versatile...

[![Excel formula: Get first day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_day_of_month.png "Excel formula: Get first day of month")](https://exceljet.net/formulas/get-first-day-of-month)

### [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)

In this example, the goal is to get the first day of the month based on any valid date. This problem can be solved by combining the EOMONTH function with simple addition. The EOMONTH Function The EOMONTH function returns the last day of the month, a given number of months in the past or future. For...

[![Excel formula: Count dates in given year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20dates%20in%20given%20year.png "Excel formula: Count dates in given year")](https://exceljet.net/formulas/count-dates-in-given-year)

### [Count dates in given year](https://exceljet.net/formulas/count-dates-in-given-year)

The YEAR function extracts the year from a valid Excel date . For example: =YEAR("15-Jun-2021") // returns 2021 In this case, we are giving YEAR and array of dates in the named range dates : YEAR(dates) Because dates contains 11 cells, we get back 11 results in an array like this: {2018;2017;2019;...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel N function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20n%20function.png "Excel N function")](https://exceljet.net/functions/n-function)

### [N Function](https://exceljet.net/functions/n-function)

The Excel N function returns a number when given a value. The N function can be used to convert TRUE and FALSE to 1 and 0 respectively. When given a text value, the N function returns zero.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)
    
*   [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
    
*   [Count dates in given year](https://exceljet.net/formulas/count-dates-in-given-year)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [N Function](https://exceljet.net/functions/n-function)
    

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