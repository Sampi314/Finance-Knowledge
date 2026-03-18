# Sum time by week and project - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-time-by-week-and-project

---

[Skip to main content](https://exceljet.net/formulas/sum-time-by-week-and-project#main-content)

[](https://exceljet.net/formulas/sum-time-by-week-and-project#)

*   [Previous](https://exceljet.net/formulas/sum-time)
    
*   [Next](https://exceljet.net/formulas/sum-time-over-30-minutes)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Sum time by week and project
============================

by Dave Bruns · Updated 8 Apr 2019

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: Sum time by week and project](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20time%20by%20week%20and%20project.png "Excel formula: Sum time by week and project")

Summary
-------

To sum up hours by week and project, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. In the example shown, the formula in G5 is:

    =SUMIFS(time,date,">="&$F5,date,"<"&$F5+7,project,G$4)
    

where "time" (D5:D15), "date" (B5:B15), and "project" (C5:C15) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =SUMIFS(time,date,">="&A1,date,"<"&A1+7,project,"A")

Explanation 
------------

In this example, the sum range is the named range "time", entered as an [Excel time](https://exceljet.net/glossary/excel-time)
 in hh:mm format. The first criteria inside SUMIFS includes dates that are greater than or equal to week date in column F:

    date,">="&$F5
    

The second criteria limits dates to one week from the original date:

    date,"<"&$F5+7
    

The last criteria, restricts data by project, by using the project identifier in row 4:

    project,G$4
    

When this formula is copied across the range G5:H7, the SUMIFS function returns a sum of time by week and project. Notice all three criteria use mixed references to lock rows and columns as needed to allow copying.

### Durations over 24 hours

To display time durations over 24 hours use a [custom number format](https://exceljet.net/articles/custom-number-formats)
 with hours in square brackets:

    [h]:mm
    

Related formulas
----------------

[![Excel formula: Sum race time splits](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sum%20race%20time%20splits.png "Excel formula: Sum race time splits")](https://exceljet.net/formulas/sum-race-time-splits)

### [Sum race time splits](https://exceljet.net/formulas/sum-race-time-splits)

Excel times are fractional numbers . This means you can add times together with the SUM function to get total durations. However, you must take care to enter times with the right syntax and use a suitable time format to display results, as explained below. Enter times in the correct format You must...

[![Excel formula: Calculate hours between two times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_hours_between_two_times.png "Excel formula: Calculate hours between two times")](https://exceljet.net/formulas/calculate-hours-between-two-times)

### [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)

In this example, the goal is to calculate the difference between two times in Excel in hours and minutes. This basic problem comes up frequently when tracking time and may be described in various ways: Calculate elapsed working time in hours. Calculate the duration of an activity in hours...

[![Excel formula: Get work hours between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20work%20hours%20between%20dates2.png "Excel formula: Get work hours between dates")](https://exceljet.net/formulas/get-work-hours-between-dates)

### [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)

This formula uses the NETWORKDAYS function calculate total working days between two dates, taking into account weekends and (optionally) holidays. Holidays, if provided, must be a range of valid Excel dates. Once total work days are known, they are simply multiplied by a fixed number of hours per...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum race time splits](https://exceljet.net/formulas/sum-race-time-splits)
    
*   [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)
    
*   [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

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