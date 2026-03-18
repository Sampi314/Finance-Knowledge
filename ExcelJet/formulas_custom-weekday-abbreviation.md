# Custom weekday abbreviation - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/custom-weekday-abbreviation

---

[Skip to main content](https://exceljet.net/formulas/custom-weekday-abbreviation#main-content)

[](https://exceljet.net/formulas/custom-weekday-abbreviation#)

*   [Previous](https://exceljet.net/formulas/create-date-range-from-two-dates)
    
*   [Next](https://exceljet.net/formulas/date-is-same-month)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Custom weekday abbreviation
===========================

by Dave Bruns · Updated 22 Apr 2016

Related functions 
------------------

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

![Excel formula: Custom weekday abbreviation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Custom%20weekday%20abbreviation.png "Excel formula: Custom weekday abbreviation")

Summary
-------

To create a custom weekday abbreviation, you can use a formula based on the CHOOSE and WEEKDAY functions. With this approach, you can generate a custom one-letter abbreviation, two-letter abbreviation, or any weekday that makes sense in your particular situation.

In the example shown, the formula in C5 is:

    =CHOOSE(WEEKDAY(B5),"S","M","T","W","T","F","S")
    

Generic formula
---------------

    =CHOOSE(WEEKDAY(date),"S","M","T","W","T","F","S")

Explanation 
------------

Working from the inside-out, the WEEKDAY function takes a date and returns a number between 1 and 7. With default settings, the number 1 corresponds to Sunday and the number 7 corresponds to Saturday.

The CHOOSE function simply maps numbers to values. The first argument is the number to map, and subsequent arguments represent associated values.

In this case, 7 values have been provided in the order required to work with WEEKDAY's Sunday through Saturday scheme.

With a date from column B, WEEKDAY returns a number which is fed to the CHOOSE function. CHOOSE returns the value at that position in the list of abbreviations.

Related formulas
----------------

[![Excel formula: Get day name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20day%20name%20from%20date.png "Excel formula: Get day name from date")](https://exceljet.net/formulas/get-day-name-from-date)

### [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)

In this example, the goal is to get the day name (i.e. Monday, Tuesday, Wednesday, etc.) from a given date. There are several ways to go about this in Excel, depending on your needs. This article explains three approaches: Display date with a custom number format Convert date to day name with TEXT...

Related functions
-----------------

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

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
    

### Functions

*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    

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