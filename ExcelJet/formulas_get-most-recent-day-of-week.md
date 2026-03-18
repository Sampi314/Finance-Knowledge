# Get most recent day of week - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-most-recent-day-of-week

---

[Skip to main content](https://exceljet.net/formulas/get-most-recent-day-of-week#main-content)

[](https://exceljet.net/formulas/get-most-recent-day-of-week#)

*   [Previous](https://exceljet.net/formulas/get-months-between-dates)
    
*   [Next](https://exceljet.net/formulas/get-next-day-of-week)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get most recent day of week
===========================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

![Excel formula: Get most recent day of week](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_most_recent_day_of_week.png "Excel formula: Get most recent day of week")

Summary
-------

To find the most recent day of the week (i.e. most recent Monday, Tuesday, Wednesday, etc.) with a given starting date, you can use a formula based on the [MOD function](https://exceljet.net/functions/mod-function)
. In the example shown, the formula in cell D5 is:

    =B5-MOD(B5-7,7)

With a start date of 16-Jan-2016 in cell B6 and the target day of the week (dow) given as 7 (for Saturday), the result is 10-Jan-2015, a Saturday.

Generic formula
---------------

    =date-MOD(date-dow,7)

Explanation 
------------

In this example, the goal is to create a formula that will return the most recent day of the week, given a date and a target day of the week, abbreviated as "dow" in the generic formula. Excel tracks the day of the week internally as a specific number for each of the seven days. By default, Excel assigns 1 to Sunday and 7 to Saturday as seen below:

| Day of week | Number |
| --- | --- |
| Sunday | 1   |
| Monday | 2   |
| Tuesday | 3   |
| Wednesday | 4   |
| Thursday | 5   |
| Friday | 6   |
| Saturday | 7   |

### The formula solution

The generic version of the formula looks like this:

    =date-MOD(date-dow,7)

In the example shown, cell B5 contains the date 1/16/2015, and the formula in D5 is:

    =B5-MOD(B5-7,7)

The number 7 is the target dow (day of week). Excel first subtracts the dow (7 in this case) from the date, then feeds the result into the MOD function as the _number_ with 7 as the _divisor._ MOD returns the remainder after division, which is subtracted from the start date. At a high level, the formula works like this:

*   **date - dow** - Shifts the original date back by dow days to create a reference point in the past.
*   **MOD(date - dow, 7)** - Normalizes the shift to a value within the current week (0-6 days). This value represents how many days back we are from a complete week cycle.
*   **B5-MOD(B5-7,7)** - Subtracting the normalized value from the original date gives the most recent target day of the week.

The code below shows how Excel evaluates the formula step-by-step:

    =B5-MOD(B5-7,7)
    =B5-MOD(42020-7,7)
    =B5-MOD(42013,7)
    =B5-6
    =42014 // 10-Jan-2015, a Saturday

The result is 42014, which is January 10, 2015, (a Saturday) in Excel's date system.

### Most recent day of the week today

If you want to get the most recent day of the week from the current date, you can use the TODAY function like this:

    =TODAY()-MOD(TODAY()-dow,7)

Note: If the date is already the target day of the week, the date will be returned unchanged.

Related formulas
----------------

[![Excel formula: Get next day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_next_day_of_week.png "Excel formula: Get next day of week")](https://exceljet.net/formulas/get-next-day-of-week)

### [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)

In this example, the goal is to get the next specified weekday, starting on a given start date. So for example, with a valid start date in column B, we want to be able to ask for the next Monday, the next Tuesday, the next Wednesday, and so on. This article describes two different ways of solving...

Related functions
-----------------

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)
    

### Functions

*   [MOD Function](https://exceljet.net/functions/mod-function)
    

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