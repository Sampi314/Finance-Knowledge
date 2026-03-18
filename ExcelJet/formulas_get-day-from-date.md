# Get day from date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-day-from-date

---

[Skip to main content](https://exceljet.net/formulas/get-day-from-date#main-content)

[](https://exceljet.net/formulas/get-day-from-date#)

*   [Previous](https://exceljet.net/formulas/get-date-from-day-number)
    
*   [Next](https://exceljet.net/formulas/get-day-name-from-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get day from date
=================

by Dave Bruns · Updated 17 Jun 2020

Related functions 
------------------

[DAY](https://exceljet.net/functions/day-function)

![Excel formula: Get day from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/exceljet_get_day_from_date.png "Excel formula: Get day from date")

Summary
-------

If you need to extract the day from a date, you can use the [DAY function](https://exceljet.net/functions/day-function)
. The date must be in a form that [Excel recognizes as a valid date](https://exceljet.net/glossary/excel-date)
. In the example shown, the formula in cell B5 is:

    =DAY(B5)
    

Generic formula
---------------

    =DAY(date)

Explanation 
------------

The DAY function takes just one argument, the date from which you want to extract the day. In the example, the formula is:

    =DAY(B5)
    

B5 contains a date value for January 5, 2016. The DAY function returns the number 5 representing the day component of the date.

Note that you can use DAY to extract the day from a day entered as text:

    =DAY("1/5/2016")
    

But this can produce unpredictable results on computers using different regional date settings. In general it's better (and more flexible) to supply an address to a cell that already contains a valid date value as the argument for DAY.

Related formulas
----------------

[![Excel formula: Get day name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20day%20name%20from%20date.png "Excel formula: Get day name from date")](https://exceljet.net/formulas/get-day-name-from-date)

### [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)

In this example, the goal is to get the day name (i.e. Monday, Tuesday, Wednesday, etc.) from a given date. There are several ways to go about this in Excel, depending on your needs. This article explains three approaches: Display date with a custom number format Convert date to day name with TEXT...

[![Excel formula: Get month from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_month_from_date.png "Excel formula: Get month from date")](https://exceljet.net/formulas/get-month-from-date)

### [Get month from date](https://exceljet.net/formulas/get-month-from-date)

The MONTH function takes just one argument, the date from which to extract the month. In the example shown, the formula is: =MONTH(B4) where B4 contains the date January 5, 2016. The MONTH function returns the number 1 representing the month( January) of the date. Note that you can use MONTH to...

[![Excel formula: Get year from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_year_from_date.png "Excel formula: Get year from date")](https://exceljet.net/formulas/get-year-from-date)

### [Get year from date](https://exceljet.net/formulas/get-year-from-date)

In this example, the goal is to extract the year number from a list of dates in column B. This can be easily achieved with the YEAR function . The YEAR function takes just one argument, the date from which you want to extract the year. For example, in the formula below, we pass the "12-Dec-1999"...

Related functions
-----------------

[![Excel DAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_day_function.png "Excel DAY function")](https://exceljet.net/functions/day-function)

### [DAY Function](https://exceljet.net/functions/day-function)

The Excel DAY function returns the day of the month as a number between 1 and 31 from a given date. DAY is commonly combined with the [YEAR function](https://exceljet.net/functions/year-function)
 and [MONTH function](https://exceljet.net/functions/month-function)
 to take apart dates for manipulation, and...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)
    
*   [Get month from date](https://exceljet.net/formulas/get-month-from-date)
    
*   [Get year from date](https://exceljet.net/formulas/get-year-from-date)
    

### Functions

*   [DAY Function](https://exceljet.net/functions/day-function)
    

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