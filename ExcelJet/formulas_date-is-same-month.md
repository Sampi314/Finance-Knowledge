# Date is same month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/date-is-same-month

---

[Skip to main content](https://exceljet.net/formulas/date-is-same-month#main-content)

[](https://exceljet.net/formulas/date-is-same-month#)

*   [Previous](https://exceljet.net/formulas/custom-weekday-abbreviation)
    
*   [Next](https://exceljet.net/formulas/date-is-same-month-and-year)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Date is same month
==================

by Dave Bruns · Updated 20 Nov 2017

Related functions 
------------------

[MONTH](https://exceljet.net/functions/month-function)

![Excel formula: Date is same month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Date%20is%20same%20month.png "Excel formula: Date is same month")

Summary
-------

To test two dates to see they both have the same month, you can do so with a simple formula that uses the MONTH function. In the example shown, the formula in cell D6 is:

    =MONTH(B6)=MONTH(C6)
    

Generic formula
---------------

    =MONTH(date1)=MONTH(date2)

Explanation 
------------

In this case, Excel extracts the month from the date in cell B6 as a number, and the month in the cell C6 as a number, then tests for equivalency using the equal sign. Both dates are in January, so the formula is solved as follows and returns TRUE.

    =MONTH(B6)=MONTH(C6)
    =1=1
    =TRUE
    

### Same month as today

If you need to test a date to see if has the same month as the current date (today), you can use this formula:

    =MONTH(date)=MONTH(TODAY())
    

### Same month and year

To test that a date is the same month and year is another date, you can use this clever formula [proposed by reader Eric Kalin](https://exceljet.net/challenges/highlight-dates-in-the-same-month-and-year)
:

    EOMONTH(date1,0)=EOMONTH(date2,0)
    

Related formulas
----------------

[![Excel formula: Date is same month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/date_is_same_month_and_year.png "Excel formula: Date is same month and year")](https://exceljet.net/formulas/date-is-same-month-and-year)

### [Date is same month and year](https://exceljet.net/formulas/date-is-same-month-and-year)

In this example, the goal is to mark dates in column D with an "x" when they have the same year and month as the date in cell B5. We don't care at all about the day. At a high level, we can easily use the IF function to return "x" for qualifying dates, so the challenge is in creating a logical test...

[![Excel formula: Highlight dates in same month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20in%20same%20month%20and%20year.png "Excel formula: Highlight dates in same month and year")](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)

### [Highlight dates in same month and year](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)

This formula uses the TEXT function to concatenate the month and year of each date. Then, the two dates are tested for equality. TEXT is a useful function that allows you to convert a number to text in the text format of your choice. In this case the format is the custom date format "myyyy", which...

Related functions
-----------------

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Date is same month and year](https://exceljet.net/formulas/date-is-same-month-and-year)
    
*   [Highlight dates in same month and year](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)
    

### Functions

*   [MONTH Function](https://exceljet.net/functions/month-function)
    

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