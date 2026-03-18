# Get first day of previous month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-first-day-of-previous-month

---

[Skip to main content](https://exceljet.net/formulas/get-first-day-of-previous-month#main-content)

[](https://exceljet.net/formulas/get-first-day-of-previous-month#)

*   [Previous](https://exceljet.net/formulas/get-first-day-of-month)
    
*   [Next](https://exceljet.net/formulas/get-fiscal-quarter-from-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get first day of previous month
===============================

by Dave Bruns · Updated 18 Nov 2015

Related functions 
------------------

[EOMONTH](https://exceljet.net/functions/eomonth-function)

![Excel formula: Get first day of previous month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20first%20day%20of%20previous%20month.png "Excel formula: Get first day of previous month")

Summary
-------

To get the first day of the previous month for a given date, you can use a simple formula based on the EOMONTH function.

In the example shown, the formula in cell B5 is:

    =EOMONTH(B5,-2)+1
    

Generic formula
---------------

    =EOMONTH(date,-2)+1

Explanation 
------------

The EOMONTH function returns the last day of a month based on a given date. The 2nd argument is _months_, which specifies how many months in the future or past to move before returning the last day. By traveling back 2 months, then adding one day, we can calculate the first day of the previous month from any given date.

In the example shown, months is supplied as -2, which causes EOMONTH to return 4/30/2015. Then, 1 day is added to get 5/1/2015.

Related formulas
----------------

[![Excel formula: Get first day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_day_of_month.png "Excel formula: Get first day of month")](https://exceljet.net/formulas/get-first-day-of-month)

### [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)

In this example, the goal is to get the first day of the month based on any valid date. This problem can be solved by combining the EOMONTH function with simple addition. The EOMONTH Function The EOMONTH function returns the last day of the month, a given number of months in the past or future. For...

[![Excel formula: Get last day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_day_of_month.png "Excel formula: Get last day of month")](https://exceljet.net/formulas/get-last-day-of-month)

### [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)

In this example, the goal is to get the last day of the month based on any valid date. This problem can be solved most easily with the EOMONTH function. However, it can also be solved with the DATE function as explained below. The EOMONTH function The EOMONTH function returns the last day of the...

Related functions
-----------------

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
    
*   [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)
    

### Functions

*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

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