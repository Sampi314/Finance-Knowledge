# Get days between dates ignoring years - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-days-between-dates-ignoring-years

---

[Skip to main content](https://exceljet.net/formulas/get-days-between-dates-ignoring-years#main-content)

[](https://exceljet.net/formulas/get-days-between-dates-ignoring-years#)

*   [Previous](https://exceljet.net/formulas/get-days-between-dates)
    
*   [Next](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get days between dates ignoring years
=====================================

by Dave Bruns · Updated 26 Apr 2016

Related functions 
------------------

[DATEDIF](https://exceljet.net/functions/datedif-function)

![Excel formula: Get days between dates ignoring years](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20days%20between%20dates%20ignoring%20years.png "Excel formula: Get days between dates ignoring years")

Summary
-------

To calculate days between two dates, ignoring year values, use the DATEDIF function. In the example shown, the formula in D6 is:

    =DATEDIF(B6,C6,"yd")
    

Generic formula
---------------

    =DATEDIF(start_date,end_date,"yd")

Explanation 
------------

The DATEDIF function can handle a variety of "date difference" calculations to calculate the difference between two dates in years, months, and days. DATEDIF takes 3 arguments: start date, end\_date, and "unit", which controls which result is returned.

In this case, we want days ignoring years so we supply "yd" for unit. (For the full list of options, see the [DATEDIF](https://exceljet.net/functions/datedif-function)
 page).

Once configured, the function is fully automatic and returns a result in the unit requested.

Related formulas
----------------

[![Excel formula: Get days between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20between%20dates.png "Excel formula: Get days between dates")](https://exceljet.net/formulas/get-days-between-dates)

### [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)

Dates in Excel are serial numbers that start on 1/1/1900, which is represented by the number 1. In the example shown, the formula in cell D6 simply subtracts the numeric value of 1/1/1999 (36161) from the numeric value of 1/1/2000 (36526) to get a result of 365. The steps look like this: =C6-B6 =...

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

[![Excel formula: Get months between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_months_between_dates.png "Excel formula: Get months between dates")](https://exceljet.net/formulas/get-months-between-dates)

### [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)

In this example, the goal is to calculate the number of months between two valid Excel dates . This is a curiously tricky problem in Excel because the number of days in a month varies, and the rules about how a whole month might be calculated are not obvious. In addition, there is not a modern...

Related functions
-----------------

[![Excel DATEDIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_datedif_function_0.png "Excel DATEDIF function")](https://exceljet.net/functions/datedif-function)

### [DATEDIF Function](https://exceljet.net/functions/datedif-function)

The Excel DATEDIF function returns the difference between two date values in years, months, or days. DATEDIF supports six unit codes that let you calculate complete years, complete months, total days, and partial intervals. DATEDIF is a "compatibility" function inherited from Lotus 1-2-3....

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
    
*   [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)
    

### Functions

*   [DATEDIF Function](https://exceljet.net/functions/datedif-function)
    

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