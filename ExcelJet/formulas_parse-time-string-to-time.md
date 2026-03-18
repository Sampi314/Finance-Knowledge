# Parse time string to time - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/parse-time-string-to-time

---

[Skip to main content](https://exceljet.net/formulas/parse-time-string-to-time#main-content)

[](https://exceljet.net/formulas/parse-time-string-to-time#)

*   [Previous](https://exceljet.net/formulas/pad-week-numbers-with-zeros)
    
*   [Next](https://exceljet.net/formulas/previous-working-day)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Parse time string to time
=========================

by Dave Bruns · Updated 2 Aug 2022

Related functions 
------------------

[TIME](https://exceljet.net/functions/time-function)

[RIGHT](https://exceljet.net/functions/right-function)

[LEFT](https://exceljet.net/functions/left-function)

[MID](https://exceljet.net/functions/mid-function)

![Excel formula: Parse time string to time](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/parse%20time%20string%20to%20time.png "Excel formula: Parse time string to time")

Summary
-------

To parse a text string that represents a time into a [proper Excel time](https://exceljet.net/glossary/excel-time)
, you can use a formula based on the [RIGHT](https://exceljet.net/functions/right-function)
, [LEFT](https://exceljet.net/functions/left-function)
, [MID](https://exceljet.net/functions/mid-function)
, and [TIME](https://exceljet.net/functions/time-function)
 functions. In the example shown, the formula in F5 is:

    =TIME(LEFT(E5,2),MID(E5,3,2),RIGHT(E5,2))
    

Which parses a 6-character time string in hhmmss format into a [valid Excel time](https://exceljet.net/glossary/excel-time)
.

_Note: the examples above use different [time format codes](https://exceljet.net/videos/how-to-create-a-custom-time-format)
 as indicated in the screenshot._

### Context

Excel expects times in Excel to be entered with the hour and minute separated by a colon. If you are entering a time with seconds, you'll need to add another colon to separate minutes and seconds, as seen in the table below:

| Desired time | Entry format |
| --- | --- |
| 2.5 hours | 2:30 |
| 30 minutes | 0:30 |
| 10 minutes, 15 seconds | 0:10:15 |
| 45 seconds | 0:00:45 |

The example on this page shows one way to skip the colons and enter a simple 4-digit or 6-digit text string that represents a time, then parse the text into a proper Excel time with a formula in a [helper column](https://exceljet.net/glossary/helper-column)
.

This is a good example of [nesting one function inside another](https://exceljet.net/glossary/nesting)
 in the same formula.

Generic formula
---------------

    =TIME(LEFT(A1,2),MID(A1,3,2),RIGHT(A1,2))

Explanation 
------------

In this example, the goal is to parse a [text string](https://exceljet.net/glossary/text-value)
 into a proper [Excel time](https://exceljet.net/glossary/excel-time)
.

First, note that the cells in F5:F13 are [formatted as Text](https://exceljet.net/videos/how-to-use-text-formatting-in-excel)
 _prior to entry_. This allows the times to contain leading zeros like "083000". Alternately, you can enter these time strings with a single quote at the start (') to force Excel to respect them as text.

Next, the time string contains 6 characters in the following format:

    hhmmss // as text
    

This means the formula needs to pick up 2 characters each for hour, minute, and second. Working from the inside out, this task is performed with the LEFT, MID, and RIGHT functions:

    LEFT(E5,2) // get hh
    MID(E5,3,2) // get mm
    RIGHT(E5,2) // get ss
    

Each of the functions returns a result directly to the TIME function. In E9, we have:

    041055
    

So the result inside TIME looks like this:

    =TIME("04","10","55")
    

The TIME function then quietly handles the text-to-number conversion and returns a valid time:

    04:10:55
    

Representing 4 hours, 10 minutes, and 55 seconds.

### With a 4-character time string

The formula in C5 is meant to handle only a 4 character time string (hours and minutes), so the structure is a bit simpler. We simply hardcode the value for seconds into the TIME function as zero:

    =TIME(LEFT(B5,2),MID(B5,3,2),0)
    

Related formulas
----------------

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

[![Excel formula: Convert decimal hours to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20hours%20to%20excel%20time.png "Excel formula: Convert decimal hours to Excel time")](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

### [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Value Time 1 1/24 0.04167 1:00 3 3/24 0.125 3:00 6 6/24 0.25 6:00 4 4/24 0.167 4:00 8 8/24 0.333 8:00 12 12/24 0.5 12:00 18 18/24 0.75 18:00 21 21/24 0...

Related functions
-----------------

[![Excel TIME function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_time.png "Excel TIME function")](https://exceljet.net/functions/time-function)

### [TIME Function](https://exceljet.net/functions/time-function)

The Excel TIME function is a built-in function that allows you to create a time with individual hour, minute, and second components. The TIME function is useful when you want to assemble a proper time inside another formula.

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
    
*   [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)
    

### Functions

*   [TIME Function](https://exceljet.net/functions/time-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    

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