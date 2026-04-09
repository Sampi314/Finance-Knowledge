# Future time intervals - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/future-time-intervals

---

[Skip to main content](https://exceljet.net/formulas/future-time-intervals#main-content)

[](https://exceljet.net/formulas/future-time-intervals#)

*   [Previous](https://exceljet.net/formulas/filter-on-dates-expiring-soon)
    
*   [Next](https://exceljet.net/formulas/generate-quarter-dates)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Future time intervals
=====================

by Dave Bruns · Updated 25 Apr 2022

![Excel formula: Future time intervals](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/future%20time%20intervals.png "Excel formula: Future time intervals")

Summary
-------

To create a list of future times at set time intervals, you can use a simple formula that adds time to an existing start date. In the example shown, the formula in D5, copied down, is:

    =B5+{4,8,12,24}/24
    

where 4, 8, 12, and 24 represent hours in the future. The result is 4 dates with times based on the start date in column B that [spill](https://exceljet.net/glossary/spill)
 into columns D:G.

Generic formula
---------------

    =A1+{4,8,12,24}/24

Explanation 
------------

In this example, the goal is to create 4 times in the future at set intervals, based on a given start time. The intervals are 4 hours, 8 hours, 12 hours, and 24 hours. If a start time is changed, the future dates should recalculate as needed.

### How Excel handles times

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
 and [times are fractional parts of 1 day](https://exceljet.net/glossary/excel-time)
. This means the date and time values are just regular numbers and can be summed, added, and subtracted like other numbers. For example, to add 12 hours to a given date or time, you can use a formula like this:

    =A1+12/24
    

This works because 1 hour is 1 day divided by 24 hours (1/24), and 12 hours is half of 1 day:

    =A1+12/24
    =A1+0.5
    

### Multiple intervals

In the example shown, the formula in D5 is:

    =B5+{4,8,12,24}/24
    

This is an example of using an [array constant](https://exceljet.net/glossary/array-constant)
 to work with multiple values at the same time. Because the array constant {4,8,12,24} contains 4 numbers, after dividing by 24 we have:

    =B5+{0.166666666666667,0.333333333333333,0.5,1}
    

January 1, 2022 is the serial number 44562, so after addition, we have:

    {44562.1666666667,44562.3333333333,44562.5,44563}
    

These four values [spill](https://exceljet.net/glossary/spill)
 into the range D5:G5.

### Date formatting

The display of dates in Excel is controlled by [number formatting](https://exceljet.net/glossary/number-format)
. The custom number format used in the example is:

    mmm d, hh:mm
    

This format can be [customized](https://exceljet.net/articles/custom-number-formats)
 as needed.

### Legacy Excel

In older versions of Excel without [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you must enter the formula as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
, or as individual formulas like:

    =A1+4/24
    =A1+8/24
    =A1+12/12
    =A1+24/24
    

You could also set up the column headings to contain the numerators (4,8,12,24) and use cell references instead of hardcoding the numbers into the formula.

Related formulas
----------------

[![Excel formula: Convert decimal hours to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20hours%20to%20excel%20time.png "Excel formula: Convert decimal hours to Excel time")](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

### [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Value Time 1 1/24 0.04167 1:00 3 3/24 0.125 3:00 6 6/24 0.25 6:00 4 4/24 0.167 4:00 8 8/24 0.333 8:00 12 12/24 0.5 12:00 18 18/24 0.75 18:00 21 21/24 0...

[![Excel formula: Add decimal hours to time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_decimal_hours_to_time.png "Excel formula: Add decimal hours to time")](https://exceljet.net/formulas/add-decimal-hours-to-time)

### [Add decimal hours to time](https://exceljet.net/formulas/add-decimal-hours-to-time)

In this example, the goal is to add hours in decimal format (i.e. 1, 2, 3, etc.) to an existing Excel time. The complication is that Excel stores time as fractional values. The number 0.25 makes sense when you consider that 6 hours is one-quarter of a day, and a day in Excel equals 1. But it isn't...

[![Excel formula: Convert Excel time to decimal hours](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20excel%20time%20to%20decimal%20hours.png "Excel formula: Convert Excel time to decimal hours")](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)

### [Convert Excel time to decimal hours](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)

In the Excel time system, one 24-hour day is equal to 1. This means times and hours are fractional values of 1, as shown in the table below: Hours Time Fraction Value 1 1:00 AM 1/24 0.04167 3 3:00 AM 3/24 0.125 6 6:00 AM 6/24 0.25 4 4:00 AM 4/24 0.167 8 8:00 AM 8/24 0.333 12 12:00 PM 12/24 0.5 18 6...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)
    
*   [Add decimal hours to time](https://exceljet.net/formulas/add-decimal-hours-to-time)
    
*   [Convert Excel time to decimal hours](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)
    

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