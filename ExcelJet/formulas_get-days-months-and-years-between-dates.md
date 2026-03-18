# Get days, months, and years between dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-days-months-and-years-between-dates

---

[Skip to main content](https://exceljet.net/formulas/get-days-months-and-years-between-dates#main-content)

[](https://exceljet.net/formulas/get-days-months-and-years-between-dates#)

*   [Previous](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)
    
*   [Next](https://exceljet.net/formulas/get-earliest-and-latest-project-dates)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get days, months, and years between dates
=========================================

by Dave Bruns · Updated 5 Mar 2026

Related functions 
------------------

[DATEDIF](https://exceljet.net/functions/datedif-function)

[LET](https://exceljet.net/functions/let-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6943/download?token=1kxVM0de)
 (14.97 KB)

![Excel formula: Get days, months, and years between dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20days%20months%20and%20years%20between%20dates.png "Excel formula: Get days, months, and years between dates")

Summary
-------

To calculate and display the time between two dates in days, months, and years, you can use a formula based on the [DATEDIF function](https://exceljet.net/functions/datedif-function)
. In the example shown, the formula in E5 is:

    =DATEDIF(B5,C5,"y")&" years, "&DATEDIF(B5,C5,"ym")&" months, " &DATEDIF(B5,C5,"md")&" days"
    

where start dates are in column B, and end dates are in column C.

Note: [See below](https://exceljet.net/formulas/get-days-months-and-years-between-dates#LET_function_example)
 for a few options that use the [LET function](https://exceljet.net/functions/let-function)
 to simplify and extend the formula.

Generic formula
---------------

    =DATEDIF(start,end,"y") &" years,"&DATEDIF(start,end,"ym") &" months," &DATEDIF(start,end,"md") &" days"
    

Explanation 
------------

In this example, the goal is to output the time between a start date and an end date as a [text string](https://exceljet.net/glossary/text-value)
 that lists years, months, and days separately. For example, given a start date of 1-Jan-2018 and an end date of 1-Jul-2018, the result should be a string like this:

    "1 years, 6 months, 0 days"
    

### DATEDIF solution

The DATEDIF function is designed to calculate the difference between dates in years, months, and days. There are several variations available (e.g. time in months, time in months ignoring days and years, etc.) and these are set by the "unit" argument in the function. See [this page on the DATEDIF function](https://exceljet.net/functions/datedif-function)
 for a full list of available units.

In the example shown, we calculate years, months, and days separately, then "glue" the results together with [concatenation](https://exceljet.net/glossary/concatenation)
. To get whole years, whole months, and days between the dates, we use DATEDIF like this, altering only the _unit_ argument.

    DATEDIF(B5,C5,"y") // years
    DATEDIF(B5,C5,"ym") // months
    DATEDIF(B5,C5,"md") // days
    

Because we want to create a string that appends the units to each number, we [concatenate](https://exceljet.net/glossary/concatenation)
 the number returned by DATEDIF to the unit name with the ampersand (&) [operator](https://exceljet.net/glossary/math-operators)
 like this:

    DATEDIF(B5,C5,"y")&" years" // years string
    DATEDIF(B5,C5,"ym")&" months" // months string
    DATEDIF(B5,C5,"md")&" days" // days string
    

Finally, we need to extend the idea above to include spaces and commas and join everything together in one string:

    =DATEDIF(B5,C5,"y")&" years, "&DATEDIF(B5,C5,"ym")&" months, " &DATEDIF(B5,C5,"md")&" days"
    

### Implementing the LET function

The [LET function](https://exceljet.net/functions/let-function)
 (new in [Excel 365](https://exceljet.net/glossary/excel-365)
) can simplify some formulas by making it possible to define and reuse variables. In order to use the LET function on this formula, we need to think about variables. The main purpose of variables is to define a useful name that can be reused elsewhere in the formula code. Looking at the formula, there are at least five opportunities to declare variables. The first two are the _start_ date and the _end_ date, which are reused throughout the formula. Once we assign values to _start_ and _end_, we only need to refer to cells C5 and D5 one time. As a first step, we can [add line breaks](https://exceljet.net/shortcuts/insert-line-break-in-cell)
 and then define variables for _start_ and _end_ like this:

    =LET(
      start,B5,
      end,C5,
      DATEDIF(start,end,"y")&" years, "&
      DATEDIF(start,end,"ym")&" months, "&
      DATEDIF(start,end,"md")&" days"
    )
    

Notice all instances of B5 and C5 in DATEDIF have been replaced by _start_ and _end_. The result from this formula is the same as the original formula above, but the reference to B5 and C5 occurs only once. The _start_ and _end_ dates are then reused throughout the formula. This makes it easier to read the formula and helps reduce errors.

The next three opportunities for variables are the results from DATEDIF for _years_, _months_, and _days_. If we assign these values to named variables, we can more easily combine them later in different ways, which becomes more useful in the extended version of the formula explained below. Here is the formula updated to include new variables for _years_, _months_, and _days_:

    =LET(
      start,B5,
      end,C5,
      years,DATEDIF(start,end,"y"),
      months,DATEDIF(start,end,"ym"),
      days,DATEDIF(start,end,"md"),
      years&" years,"&months &" months," &days &" days"
    )
    

Notice we have assigned results from DATEDIF to the variables _years_, _months_, and _days_, and these values are concatenated together in the last line inside the LET function. With the LET function, the last [argument](https://exceljet.net/glossary/function-argument)
 is the calculation or value that returns a final result.

### Getting fancy with LET

Once we have the basic LET version working, we can easily extend the formula to do more complex processing, without redundantly running the same calculations over again. For example, one thing we might want to do is make the units plural or singular depending on the actual unit number.  The formula below adds three new variables: _ys_, _ms_, and _ds_ to hold the strings associated with each unit:

    =LET(
      start,B5,
      end,C5,
      years,DATEDIF(start,end,"y"),
      months,DATEDIF(start,end,"ym"),
      days,DATEDIF(start,end,"md"),
      ys,years&" year"&IF(years<>1,"s",""),
      ms,months&" month"&IF(months<>1,"s",""),
      ds,days&" day"&IF(days<>1,"s",""),
      ys&", "&ms&", "&ds
    )
    

The strings start out singular (i.e. " year" not "years"). Then we use the IF function to conditionally tack on an "s" only when the number is _not_ 1. If the number _is_ 1, IF returns an [empty string](https://exceljet.net/glossary/empty-string)
 ("") and the unit name remains singular. Because we add the unit name to the unit number when we define _ys_, _ms_, and _ds_, the last step inside LET is simpler; we only need to [concatenate](https://exceljet.net/glossary/concatenation)
 the units with a comma and space.

See more details about the [LET function here](https://exceljet.net/functions/let-function)
. Also, see the [Detailed LET function example](https://exceljet.net/formulas/detailed-let-function-example)
 for another explanation of converting an existing formula to use LET.

> The DATEDIF function can return incorrect results with date pairs that touch specific edge cases. One workaround is to build your own alternative with a custom lambda function. For details, see: [How to replace Excel's DATEDIF function](https://exceljet.net/articles/how-to-replace-excels-datedif-function)
> .

Related formulas
----------------

[![Excel formula: Get days, hours, and minutes between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20hours%20and%20minutes%20between%20dates2.png "Excel formula: Get days, hours, and minutes between dates")](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

### [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

Most of the work in this formula is done by the TEXT function, which applies a custom number format for hours and minutes to a value created by subtracting the start date from the end date. TEXT(C5-B5,"h"" hrs ""m"" mins """) This is an example of embedding text into a custom number format, and...

[![Excel formula: Get days between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20between%20dates.png "Excel formula: Get days between dates")](https://exceljet.net/formulas/get-days-between-dates)

### [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)

Dates in Excel are serial numbers that start on 1/1/1900, which is represented by the number 1. In the example shown, the formula in cell D6 simply subtracts the numeric value of 1/1/1999 (36161) from the numeric value of 1/1/2000 (36526) to get a result of 365. The steps look like this: =C6-B6 =...

[![Excel formula: Get months between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_months_between_dates.png "Excel formula: Get months between dates")](https://exceljet.net/formulas/get-months-between-dates)

### [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)

In this example, the goal is to calculate the number of months between two valid Excel dates . This is a curiously tricky problem in Excel because the number of days in a month varies, and the rules about how a whole month might be calculated are not obvious. In addition, there is not a modern...

[![Excel formula: Detailed LET function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/let%20function%20example.png "Excel formula: Detailed LET function example")](https://exceljet.net/formulas/detailed-let-function-example)

### [Detailed LET function example](https://exceljet.net/formulas/detailed-let-function-example)

In this example, we have a simple set of data in B5:D16 that includes ID, Name, and Points. The goal is to generate a custom message for any name in the list by entering a valid ID in cell G5. The message uses the name from column C and the points in column D like this: "Hi \[name\], you have \[points...\
\
Related functions\
-----------------\
\
[![Excel DATEDIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_datedif_function_0.png "Excel DATEDIF function")](https://exceljet.net/functions/datedif-function)\
\
### [DATEDIF Function](https://exceljet.net/functions/datedif-function)\
\
The Excel DATEDIF function returns the difference between two date values in years, months, or days. DATEDIF supports six unit codes that let you calculate complete years, complete months, total days, and partial intervals. DATEDIF is a "compatibility" function inherited from Lotus 1-2-3....\
\
[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)\
\
### [LET Function](https://exceljet.net/functions/let-function)\
\
The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....\
\
Was this page helpful? Yes No Report a problem\
\
Cancel Submit\
\
![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)\
\
Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)\
\
### Dave Bruns\
\
Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.\
\
Related Information\
-------------------\
\
### Formulas\
\
*   [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)\
    \
*   [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)\
    \
*   [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)\
    \
*   [Detailed LET function example](https://exceljet.net/formulas/detailed-let-function-example)\
    \
\
### Functions\
\
*   [DATEDIF Function](https://exceljet.net/functions/datedif-function)\
    \
*   [LET Function](https://exceljet.net/functions/let-function)\
    \
\
Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!\
\
Thierry\
\
[More Testimonials](https://exceljet.net/feedback)\
\
Get [Training](https://exceljet.net/training)\
\
----------------------------------------------\
\
### Quick, clean, and to the point training\
\
Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.\
\
[View Paid Training & Bundles](https://exceljet.net/training)\
\
[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)\
\
[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)\
\
[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)\
\
[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)\
\
[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)\
\
[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)