# Timesheet overtime calculation formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/timesheet-overtime-calculation-formula

---

[Skip to main content](https://exceljet.net/formulas/timesheet-overtime-calculation-formula#main-content)

[](https://exceljet.net/formulas/timesheet-overtime-calculation-formula#)

*   [Previous](https://exceljet.net/formulas/time-since-start-in-day-ranges)
    
*   [Next](https://exceljet.net/formulas/workdays-per-month)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Timesheet overtime calculation formula
======================================

by Dave Bruns · Updated 3 Nov 2023

Related functions 
------------------

[MIN](https://exceljet.net/functions/min-function)

![Excel formula: Timesheet overtime calculation formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/basic%20overtime%20calculation.png "Excel formula: Timesheet overtime calculation formula")

Summary
-------

To calculate overtime and pay associated with overtime, you can use the formulas explained on this page. In formula in cell I5 is:

    =(F5*H5)+(G5*H5*1.5)
    

Generic formula
---------------

    =(reg_hrs*rate)+(ot_hrs*rate*1.5)

Explanation 
------------

_Note: it's important to understand that [Excel deals with time as fractions of a day](https://exceljet.net/glossary/excel-time)
. So, 12:00 PM is .5, 6:00 AM is .25, 6 PM is .75, and so on. This works fine for standard time and date calculations, but in many cases you'll want to convert times to decimal hours to make other calculations more straightforward. In the example shown on this page, we capture time in native units, but then [convert to decimal hours](https://exceljet.net/formulas/time-difference-in-hours-as-decimal-value)
 in column E._

To calculate total hours worked, cell E5 contains:

    =(D5-C5)*24
    

This is simply end time minus start time, multiplied by 24 to convert to decimal hours. If you need to calculate elapsed time that crosses midnight, [see this page for options and general explanation](https://exceljet.net/formulas/calculate-number-of-hours-between-two-times)
.

To calculate regular time, F5 contains:

    =MIN(8,E5)
    

This is [an example of using MIN instead of IF to simplify](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
. The result is the smaller of two options: 8 hours, or regular time as calculated above.

To calculate OT (overtime), G5 contains:

    =E5-F5
    

Not much to see here. We simply subtract regular time from total hours to get overtime. Note the result will be zero if total time = regular time. This is important because it effectively "zeroes out" the overtime component of the formula in I5 when there is no overtime.

To calculate the Total, I5 contains:

    (F5*H5)+(G5*H5*1.5)
    

This is where we finally calculate a total based on rate and hours, taking into account overtime paid at 1.5 times the normal rate. (Adjust the multiplier as needed). We first multiply regular time by the normal rate. Then we multiply overtime by the same rate times 1.5. As mentioned above, when overtime is zero, this part of the formula returns zero.

Finally, the sum of both calculations above is returned as the Total in column I.

Related formulas
----------------

[![Excel formula: Calculate hours between two times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_hours_between_two_times.png "Excel formula: Calculate hours between two times")](https://exceljet.net/formulas/calculate-hours-between-two-times)

### [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)

In this example, the goal is to calculate the difference between two times in Excel in hours and minutes. This basic problem comes up frequently when tracking time and may be described in various ways: Calculate elapsed working time in hours. Calculate the duration of an activity in hours...

[![Excel formula: Smaller of two values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/smaller_of_two_values.png "Excel formula: Smaller of two values")](https://exceljet.net/formulas/smaller-of-two-values)

### [Smaller of two values](https://exceljet.net/formulas/smaller-of-two-values)

In this example, the goal is to return the smaller of two values which appear in columns B and C. Although this problem could be solved with the IF function (see below), the simplest solution is to use the MIN function. MIN function The MIN function returns the smallest numeric value in the data...

Related functions
-----------------

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)
    
*   [Smaller of two values](https://exceljet.net/formulas/smaller-of-two-values)
    

### Functions

*   [MIN Function](https://exceljet.net/functions/min-function)
    

### Articles

*   [Replace ugly IFs with MAX or MIN](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
    

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