# Basic timesheet formula with breaks - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/basic-timesheet-formula-with-breaks

---

[Skip to main content](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks#main-content)

[](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks#)

*   [Previous](https://exceljet.net/formulas/assign-points-based-on-late-time)
    
*   [Next](https://exceljet.net/formulas/calculate-date-overlap-in-days)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Basic timesheet formula with breaks
===================================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

![Excel formula: Basic timesheet formula with breaks](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/basic%20timesheet%20formula%20with%20breaks.png "Excel formula: Basic timesheet formula with breaks")

Summary
-------

To calculate work hours, taking into account break time that needs to be subtracted, you can use a formula based on the MOD function. MOD is used to handle start and end times that cross midnight. In the example shown, the formula in F6 is:

    =MOD(C6-B6,1)-MOD(E6-D6,1)
    

Generic formula
---------------

    =MOD(workend-workstart,1)-MOD(breakstart-breakend,1)

Explanation 
------------

At the core, this formula subtracts start time from end time to get duration in hours. This is done to calculate both work time and break time.

    MOD(C6-B6,1) // get work time
    MOD(E6-D6,1) // get break time
    

Next, break time is subtracted from work time to get "net" work hours.

This formula uses the MOD function to handle times that cross a day boundary (midnight). By using MOD with a divisor of 1, positive results are unchanged, but negative results (which occur when the start time is greater than the end time) are "flipped" to get a correct duration.

For more details, see: [How to calculate number of hours between two times](https://exceljet.net/formulas/calculate-number-of-hours-between-two-times)

### Formatting time durations

In cases where the calculated time exceeds 24 hours, you may want to use a [custom format](https://exceljet.net/articles/custom-number-formats)
 like \[h\]:mm. The square bracket syntax \[h\] tells Excel to display hour durations greater than 24 hours. If you don't use the brackets, Excel will simply "roll over" when the duration hits 24 hours (like a clock).

### Alternative timesheet layout

The screenshot below shows an alternative format to capture time worked. Instead of logging work and break time separately, this version captures two separate in/out times for a single shift.

![Alternative timesheet layout](https://exceljet.net/sites/default/files/images/formulas/inline/basic%20timesheet%20formula.png "Alternative timesheet layout")

For this layout, the formula used in F5 is:

    =MOD(C5-B5,1)+MOD(E5-D5,1)
    

Instead of subtracting break time from work time, we add together the two work times.

Related formulas
----------------

[![Excel formula: Calculate hours between two times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_hours_between_two_times.png "Excel formula: Calculate hours between two times")](https://exceljet.net/formulas/calculate-hours-between-two-times)

### [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)

In this example, the goal is to calculate the difference between two times in Excel in hours and minutes. This basic problem comes up frequently when tracking time and may be described in various ways: Calculate elapsed working time in hours. Calculate the duration of an activity in hours...

[![Excel formula: Timesheet overtime calculation formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20overtime%20calculation.png "Excel formula: Timesheet overtime calculation formula")](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)

### [Timesheet overtime calculation formula](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)

Note: it's important to understand that Excel deals with time as fractions of a day . So, 12:00 PM is .5, 6:00 AM is .25, 6 PM is .75, and so on. This works fine for standard time and date calculations, but in many cases you'll want to convert times to decimal hours to make other calculations more...

[![Excel formula: Convert time to time zone](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20time%20to%20time%20zone.png "Excel formula: Convert time to time zone")](https://exceljet.net/formulas/convert-time-to-time-zone)

### [Convert time to time zone](https://exceljet.net/formulas/convert-time-to-time-zone)

Times in Excel are fractional values of the number 1 . So, 12 PM is 12/24 = .5, 6:00 AM is 6/24 = .25, and so on. So, to convert a time by a given number, you need to divide the number of hours by 24 to get required decimal value: E5/24 // convert adjustment to Excel time We add the result to the...

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

*   [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)
    
*   [Timesheet overtime calculation formula](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)
    
*   [Convert time to time zone](https://exceljet.net/formulas/convert-time-to-time-zone)
    

### Functions

*   [MOD Function](https://exceljet.net/functions/mod-function)
    

### Articles

*   [How to use the MOD function to repeat values](https://exceljet.net/articles/how-to-use-the-mod-function-to-repeat-values)
    

### Links

*   [An Introduction to Modular Math (Khan Academy)](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic)
    
*   [Calculating working hours (Chandoo video)](http://chandoo.org/wp/2015/06/22/calculating-billys-total-working-hours/)
    

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