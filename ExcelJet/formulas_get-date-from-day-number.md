# Get date from day number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-date-from-day-number

---

[Skip to main content](https://exceljet.net/formulas/get-date-from-day-number#main-content)

[](https://exceljet.net/formulas/get-date-from-day-number#)

*   [Previous](https://exceljet.net/formulas/get-age-from-birthday)
    
*   [Next](https://exceljet.net/formulas/get-day-from-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get date from day number
========================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[DATE](https://exceljet.net/functions/date-function)

[RIGHT](https://exceljet.net/functions/right-function)

[LEFT](https://exceljet.net/functions/left-function)

![Excel formula: Get date from day number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20date%20from%20day%20number.png "Excel formula: Get date from day number")

Summary
-------

To get a real date from day number, or "nth day of year" you can use the [DATE function](https://exceljet.net/functions/date-function)
. In the example shown, the formula in C5 is:

    =DATE(2015,1,B5)
    

Generic formula
---------------

    =DATE(year,1,daynum)

Explanation 
------------

The DATE function builds dates from separate year, month, and day values. One of its tricks is the ability to roll forward to correct dates when given days and months that are "out of range". For example, DATE returns April 9, 2016, with the following arguments:

    =DATE(2016,1,100)
    

There is no 100th day in January, so DATE simply moves forward 100 days from January 1 and returns the correct date.

The formula on this page takes advantage of this behavior. The year is assumed to be 2015 in this case, so 2015 is hard-coded for the year, and 1 is used for the month. The day value comes from column B, and the DATE function calculates the date as explained above.

### Extracting a year value from a Julian date

If you have a date in a Julian format, for example, 10015, where the format is "dddyy", you can adapt the formula as follows:

    =DATE(RIGHT(A1,2),1,LEFT(A1,3))
    

Here, we use RIGHT to extract the 2 characters from the right for the _year_, and LEFT to extract 3 characters from the left for the _day_. The _month_ is supplied as 1, as in the first example.

Related formulas
----------------

[![Excel formula: Convert date to Julian format](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20Julian%20format.png "Excel formula: Convert date to Julian format")](https://exceljet.net/formulas/convert-date-to-julian-format)

### [Convert date to Julian format](https://exceljet.net/formulas/convert-date-to-julian-format)

This formula builds the final result in 2 parts, joined by concatenation with the ampersand (...

Related functions
-----------------

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Convert date to Julian format](https://exceljet.net/formulas/convert-date-to-julian-format)
    

### Functions

*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    

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