# Get months between dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-months-between-dates

---

[Skip to main content](https://exceljet.net/formulas/get-months-between-dates#main-content)

[](https://exceljet.net/formulas/get-months-between-dates#)

*   [Previous](https://exceljet.net/formulas/get-month-name-from-date)
    
*   [Next](https://exceljet.net/formulas/get-most-recent-day-of-week)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get months between dates
========================

by Dave Bruns · Updated 24 Feb 2024

Related functions 
------------------

[DATEDIF](https://exceljet.net/functions/datedif-function)

[YEARFRAC](https://exceljet.net/functions/yearfrac-function)

[MONTH](https://exceljet.net/functions/month-function)

[YEAR](https://exceljet.net/functions/year-function)

![Excel formula: Get months between dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_months_between_dates.png "Excel formula: Get months between dates")

Summary
-------

To calculate the number of months between two dates as a whole number, you can use the [DATEDIF function](https://exceljet.net/functions/datedif-function)
. In the example shown, the formula in D5, copied down, is:

    =DATEDIF(B5,C5,"m")
    

As the formula is copied down, it returns the count of months between the start date in column B and the end date in column C.

_Note: DATEDIF automatically rounds down to the nearest whole month. To round up to the nearest whole month, see the alternatives below._

Generic formula
---------------

    =DATEDIF(start,end,"m")

Explanation 
------------

In this example, the goal is to calculate the number of months between two [valid Excel dates](https://exceljet.net/glossary/excel-date)
. This is a curiously tricky problem in Excel because the number of days in a month varies, and the rules about how a whole month might be calculated are not obvious. In addition, there is not a modern Excel function dedicated to the task of calculating months between dates. I have no idea why. The best tool for the job is the mysterious DATEDIF function, which is kind of a black sheep in the Excel family.

### The DATEDIF function

The solutions described below are based primarily on the DATEDIF function. DATEDIF (date + dif) is designed to calculate the difference between a start date and an end date in years, months, or days. DATEDIF takes 3 arguments: _start\_date_, _end\_date_, and _unit_ and the generic syntax looks like this:

    =DATEDIF(start_date,end_date,unit)
    

For this problem, the start dates come from column B and the end dates come from column C. For unit, we need to supply "m", because we want to calculate _months_ between dates. See [this page on the DATEDIF function](https://exceljet.net/functions/datedif-function)
 for more information about the options available.

> DATEDIF is a "compatibility" function that comes originally from Lotus 1-2-3. You can use DATEDIF in all current Excel versions, but you must enter the function manually — unlike other functions, DATEDIF _will not_ appear as a suggested function in the formula bar and Excel _will not_ help you with function arguments.

### Calculate complete whole months

In the worksheet shown below, we are using the [DATEDIF function](https://exceljet.net/functions/datedif-function)
 to calculate complete whole months between a start date and an end date. The start dates come from column B and the end dates come from column C. The formula in D5, copied down, is:

    =DATEDIF(B5,C5,"m")
    

![Default DATEDIF behavior when calculating months between dates](https://exceljet.net/sites/default/files/images/formulas/inline/get_months_between_dates_default_datedif_behavior.png "Default DATEDIF behavior when calculating months between dates")

As the formula is copied down, DATEDIF returns whole months between the start date in column B and the end date in column C. Notice that the first four results in D5:D8 are exact multiples of months, but the result in D9 has been rounded down to 5 because we are 1 day short of 6 months. Also notice that results in D13:D16 are a bit quirky, due to how DATEDIF handles end-of-month dates. For example, when the days match, the result is an exact multiple of months, as expected. However, when the days don't match, the results can be unexpected. For example, with a start date of July 31 and an end date of September 30, the result is 1, though most people would count this as 2 months. One workaround to this problem is described below.

### Calculate nearest whole months

When calculating months between two dates, DATEDIF always rounds months down to the last complete number of months. This means DATEDIF rounds a result down even when it is very close to the next whole month. To calculate months to the nearest whole month, you can adjust the formula as shown below:

    =DATEDIF(start_date,end_date+15,"m")
    

In this version of the formula, we add 15 days to the end date. This ensures that end dates in the second half of the month are treated like dates in the following month, effectively rounding up the final result to the next even multiple. End dates that occur in the first half of the month also increase by 15 days, but not enough to affect the normal result from DATEDIF. The screen below shows how the original DATEDIF formula compares to the modified version:

![Modified DATEDIF formula to calculate nearest whole month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/get_months_between_dates_modified_datedif_formula.png "Modified DATEDIF formula to calculate nearest whole month")

### Calculate decimal months

As shown above, DATEDIF only calculates whole months. To calculate a decimal number that represents the number of months between two dates, you can use the [YEARFRAC function](https://exceljet.net/functions/yearfrac-function)
 like this:

    =YEARFRAC(start,end)*12
    

YEARFRAC returns fractional years between two dates, so the result is an approximate number of months between two dates, including fractional months returned as a decimal value. The screen below shows how the original DATEDIF formula compares to the YEARFRAC version:

![DATEDIF versus YEARFRAC to calculate months between dates](https://exceljet.net/sites/default/files/images/formulas/inline/get_months_between_dates_datedif_vs_yearfrac.png "DATEDIF versus YEARFRAC to calculate months between dates")

Keep in mind that the behavior of this formula depends on how YEARFRAC works. [See this page](https://exceljet.net/functions/yearfrac-function)
 for more information.

### Alternative formula to calculate months touched by dates

In some cases, you may want to count how many months are "touched" by a given date range. The generic formula for this calculation looks like this:

    =(YEAR(C5)-YEAR(B5))*12+MONTH(C5)-MONTH(B5)+1
    

This formula uses the [YEAR function](https://exceljet.net/functions/year-function)
 and the [MONTH function](https://exceljet.net/functions/month-function)
 to work out a count in two parts. First, the months associated with a year change are calculated:

    (YEAR(end)-YEAR(start))*12 // months due to year change
    

This code only affects the count if the start year and end year are different. If the start year and end year are the same, the result is zero. Next, the formula subtracts the start month from the end month and adds 1 to calculate the remaining months:

    MONTH(end)-MONTH(start)+1 // remaining months

Notice this calculation means that _any month difference_ will result in a positive number because the day of the month is completely ignored. Finally, the two parts of the formula are added together to get a total month count. The screen below shows the formula in action, compared to the original DATEDIF formula above:

![Alternative formula to calculate months touched by dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/get_months_between_dates_alternative_formula_for_months_touched.png "Alternative formula to calculate months touched by dates")

As you would expect, this formula tends to increase the month count for a date range, since even a small portion of a month will be included in the result. You can see this effect if you compare results from the original DATEDIF formula in column E to results from the alternative formula in column F.

Related formulas
----------------

[![Excel formula: Get days between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20between%20dates.png "Excel formula: Get days between dates")](https://exceljet.net/formulas/get-days-between-dates)

### [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)

Dates in Excel are serial numbers that start on 1/1/1900, which is represented by the number 1. In the example shown, the formula in cell D6 simply subtracts the numeric value of 1/1/1999 (36161) from the numeric value of 1/1/2000 (36526) to get a result of 365. The steps look like this: =C6-B6 =...

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

[![Excel formula: Get days, months, and years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20months%20and%20years%20between%20dates.png "Excel formula: Get days, months, and years between dates")](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

### [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

In this example, the goal is to output the time between a start date and an end date as a text string that lists years, months, and days separately. For example, given a start date of 1-Jan-2018 and an end date of 1-Jul-2018, the result should be a string like this: "1 years, 6 months, 0 days"...

Related functions
-----------------

[![Excel DATEDIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_datedif_function_0.png "Excel DATEDIF function")](https://exceljet.net/functions/datedif-function)

### [DATEDIF Function](https://exceljet.net/functions/datedif-function)

The Excel DATEDIF function returns the difference between two date values in years, months, or days. DATEDIF supports six unit codes that let you calculate complete years, complete months, total days, and partial intervals. DATEDIF is a "compatibility" function inherited from Lotus 1-2-3....

[![Excel YEARFRAC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_yearfrac_function.png "Excel YEARFRAC function")](https://exceljet.net/functions/yearfrac-function)

### [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)

The Excel YEARFRAC function returns a decimal value that represents fractional years between two dates. You can use YEARFRAC to do things like calculate age with a birthdate....

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)
    
*   [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)
    
*   [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
    

### Functions

*   [DATEDIF Function](https://exceljet.net/functions/datedif-function)
    
*   [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    

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