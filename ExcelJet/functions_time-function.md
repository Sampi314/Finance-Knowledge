# Excel TIME function | Exceljet

**Source:** https://exceljet.net/functions/time-function

---

[Skip to main content](https://exceljet.net/functions/time-function#main-content)

[](https://exceljet.net/functions/time-function#)

*   [Previous](https://exceljet.net/functions/second-function)
    
*   [Next](https://exceljet.net/functions/timevalue-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

TIME Function
=============

by Dave Bruns · Updated 2 May 2024

Related functions 
------------------

[DATE](https://exceljet.net/functions/date-function)

![Excel TIME function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_time.png "Excel TIME function")

Summary
-------

The Excel TIME function is a built-in function that allows you to create a time with individual hour, minute, and second components. The TIME function is useful when you want to assemble a proper time inside another formula.

Purpose 
--------

Create a valid time with hours, minutes, and seconds

Return value 
-------------

A decimal number representing time in Excel.

Syntax
------

    =TIME(hour,minute,second)

*   _hour_ - Number of hours.
*   _minute_ - Number of minutes.
*   _second_ - Number of seconds.

Using the TIME function 
------------------------

The TIME function creates a valid Excel time using the given values for _hour_, _minute_, and _second_. Like all Excel time, the result is a [number that represents a fractional day](https://exceljet.net/glossary/excel-time)
. The TIME function will only return time values up to one full day, between 0 (zero) to 0.99999999, or 0:00:00 to 23:59:59.  To see results formatted as time, apply a time-based [number format](https://exceljet.net/glossary/number-format)
. 

The main benefit of the TIME function is the convenience of entering a time with separate values for hours, minutes, and seconds. It is analogous to the [DATE function](https://exceljet.net/functions/date-function)
, which creates dates with separate values for year, month, and day.

### Basic example

    =TIME(3,0,0) // 3 hours
    =TIME(0,3,0) // 3 minutes
    =TIME(0,0,3) // 3 seconds
    =TIME(8,30,0) // 8.5 hours
    

### Time formatting

The TIME function returns a valid time as a number, but the way Excel displays the result depends on [number formatting](https://exceljet.net/glossary/number-format)
. Excel can display that result as time with AM/PM suffix, a 24-hour time like 17:30:00, or as a regular number. You can see how these formats compare in the screen below, where the number formatting applied to columns F, G, and H is as follows:

    h:mm AM/PM
    h:mm:ss
    0.0

![Output from TIME formatted in different ways](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/time_function_number_format_comparison.png "Output from TIME formatted in different ways")

> Number formatting affects the _display_ of time only, _not the underlying value_.

### Larger units

The TIME function can interpret units in larger increments. For example, both of the formulas below return 2 hours:

    =TIME(0,120,0) // 2 hours
    =TIME(0,0,7200) // 2 hours
    

However, TIME will not handle numeric inputs larger than 32,767. For example, even though there are 86,400 seconds in a day, the following formula (which represents 12 hours) will fail with a #NUM! error:

    =TIME(0,0,43200) // returns #NUM! 
    

### Time over 24 hours

It's important to understand that TIME only returns results _up to 24 hours_. When the total time exceeds 24 hours, the TIME function will "reset" to zero.

    =TIME(12,0,0) // returns 0.5 (12 hours)
    =TIME(18,0,0) // returns 0.75 (18 hours)
    =TIME(24,0,0) // returns 0 (0 hours)
    =TIME(36,0,0) // returns 0.5 (12 hours)
    =TIME(48,0,0) // returns 0 (0 hours)
    

Notice TIME returns 0 for 24 hours and 48 hours above. In this way, the behavior of the TIME function is similar to a 24-hour clock that resets at midnight. To create time durations greater than 24 hours, you can use a manual formula to convert [hours](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)
, [minutes](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)
, and [seconds](https://exceljet.net/formulas/convert-decimal-seconds-to-excel-time)
 to Excel time like this:

    =(hours/24)+(minutes/1440)+(seconds/86400)
    

The result from the formula above is the same as with the TIME function for time durations up to 24 hours. For time durations _over_ 24 hours, this formula will continue to work correctly while the TIME function will reset to zero at each 24-hour interval. For example, for a time duration of 72 hours, TIME returns zero:

    =TIME(72,0,0) // returns 0
    

However, the alternate formula above will correctly return 3 days:

    =(hours/24)+(minutes/1440)+(seconds/86400)
    =(72/24)+(0/1440)+(0/86400)
    =(3)+(0)+(0)
    =3

When formatted with the [custom number format](https://exceljet.net/articles/custom-number-formats)
 \[h\]:mm:ss. Excel will display 72:00:00.

> This formula is also useful for creating time that includes [fractional seconds](https://exceljet.net/formulas/time-in-hundredths-of-a-second)
> .

### Negative inputs

Although the TIME function will return an error if the final result is negative, you _can_ supply units as negative numbers so long as the result is positive. For example:

    =TIME(12,-3,0) // returns 09:00:00
    =TIME(24,-1,0) // returns 23:59:00
    =TIME(3,-120,0) // returns 01:00:00
    

### TIME function limitations

There are two limitations to the TIME that you should be aware of. First, TIME will only accept whole numbers for hours, minutes, and seconds. If you supply decimal values, the decimal portion of the number will be discarded. For example, both formulas below return 12 hours even though the second formula provides 12.5 for hours:

    =TIME(12,0,0) returns 12 hours
    =TIME(12.5,0,0) returns 12 hours
    

Second, TIME only supports positive time. If you provide inputs that would create a negative time, TIME will return a #NUM! error:

    =TIME(-6,0,0) // returns #NUM! 
    

### Notes

*   When the total time reaches 24 hours, the TIME function will "reset" to zero. 
*   The largest number that TIME will allow for hour, minute, or second is 32,767. Larger values will return a #NUM! error.
*   If hours, minutes, or seconds are provided as a negative number, TIME will return a #NUM! error.

TIME function examples
----------------------

[![Excel formula: Parse time string to time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/parse%20time%20string%20to%20time.png "Excel formula: Parse time string to time")](https://exceljet.net/formulas/parse-time-string-to-time)

### [Parse time string to time](https://exceljet.net/formulas/parse-time-string-to-time)

In this example, the goal is to parse a text string into a proper Excel time . First, note that the cells in F5:F13 are formatted as Text prior to entry . This allows the times to contain leading zeros like "083000". Alternately, you can enter these time strings with a single quote at the start...

[![Excel formula: Sequence of times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence%20of%20time.png "Excel formula: Sequence of times")](https://exceljet.net/formulas/sequence-of-times)

### [Sequence of times](https://exceljet.net/formulas/sequence-of-times)

The SEQUENCE function is a dynamic array function that can generate multiple results. When used by itself on the worksheet, SEQUENCE outputs an array of results that " spill " onto the worksheet in a " spill range ". In the example shown, we want to generate 12 times, one hour apart, starting at 7:...

[![Excel formula: Count times in a specific range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20times%20in%20a%20specific%20range.png "Excel formula: Count times in a specific range")](https://exceljet.net/formulas/count-times-in-a-specific-range)

### [Count times in a specific range](https://exceljet.net/formulas/count-times-in-a-specific-range)

The COUNTIFS function takes one or more criteria, entered as range/criteria pairs. In this example, the first range/criteria pair is: B5:B11,">="&E5 Matching any time greater than or equal to the time E5 (5:00). The second range/criteria pair is: B5:B11,"<"&E6 Matching any time less...

[![Excel formula: Add decimal minutes to time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_decimal_minutes_to_time.png "Excel formula: Add decimal minutes to time")](https://exceljet.net/formulas/add-decimal-minutes-to-time)

### [Add decimal minutes to time](https://exceljet.net/formulas/add-decimal-minutes-to-time)

In this example, the goal is to add minutes in decimal format (i.e., 1, 5, 10, etc.) to an existing Excel time. The complication is that Excel stores time as fractional values. The number 0.0104167 makes sense when you consider that 15 minutes is 1/96th of a day, and a day in Excel equals 1. But it...

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

[![Excel formula: Convert UTC timestamp to Excel datetime](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert-utc-timestamp-to-excel-datetime.png "Excel formula: Convert UTC timestamp to Excel datetime")](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime)

### [Convert UTC timestamp to Excel datetime](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime)

UTC timestamps like 2026-01-18T08:00:00Z are a common standard for representing dates and times, but Excel won't correctly recognize this format without some help. If you try to apply date formatting to a UTC timestamp, nothing happens. In this example, the goal is to convert UTC timestamps to...

[![Excel formula: Add decimal hours to time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_decimal_hours_to_time.png "Excel formula: Add decimal hours to time")](https://exceljet.net/formulas/add-decimal-hours-to-time)

### [Add decimal hours to time](https://exceljet.net/formulas/add-decimal-hours-to-time)

In this example, the goal is to add hours in decimal format (i.e. 1, 2, 3, etc.) to an existing Excel time. The complication is that Excel stores time as fractional values. The number 0.25 makes sense when you consider that 6 hours is one-quarter of a day, and a day in Excel equals 1. But it isn't...

[![Excel formula: Time duration with days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/time%20duration%20with%20days.png "Excel formula: Time duration with days")](https://exceljet.net/formulas/time-duration-with-days)

### [Time duration with days](https://exceljet.net/formulas/time-duration-with-days)

In the example shown, the goal is to enter a valid time based on days, hours, and minutes, then display the result as total hours. The key is to understand that time in Excel is just a number. 1 day = 24 hours , and 1 hour = 0.0412 (1/24). That means 12 hours = 0.5, 6 hours = 0.25, and so on...

[![Excel formula: Time in hundredths of a second](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/time_in_hundredths_of_a_second.png "Excel formula: Time in hundredths of a second")](https://exceljet.net/formulas/time-in-hundredths-of-a-second)

### [Time in hundredths of a second](https://exceljet.net/formulas/time-in-hundredths-of-a-second)

In the worksheet shown, we have race results for an 800m race. The goal is to display time in minutes, seconds, and hundredths of a second (centiseconds). Dealing with times that include fractional seconds can be tricky in Excel. The default time format will only show whole seconds and it is not...

[![Excel formula: Convert text timestamp into time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Convert%20text%20timestamp%20into%20time.png "Excel formula: Convert text timestamp into time")](https://exceljet.net/formulas/convert-text-timestamp-into-time)

### [Convert text timestamp into time](https://exceljet.net/formulas/convert-text-timestamp-into-time)

This formula works for times entered in a particular format as shown below: 00h01m13s 00h01m08s 08h02m59s Note the text string is always 9 characters long, and each component is 2 digits. The core of this formula is the TIME function, which assembles a valid time using individual hour, minute, and...

[![Excel formula: Sum time over 30 minutes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20time%20over%2030%20minutes.png "Excel formula: Sum time over 30 minutes")](https://exceljet.net/formulas/sum-time-over-30-minutes)

### [Sum time over 30 minutes](https://exceljet.net/formulas/sum-time-over-30-minutes)

This formula uses the SUMPRODUCT function to sum the result of two expressions that yield arrays. The goal is to sum only time greater than 30 minutes, the "surplus" or "extra" time. The first expression subtracts 30 minutes from every time in the named range "times": times-TIME(0,30,0) This...

TIME function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20work%20with%20times-thumb.png)](https://exceljet.net/videos/how-to-work-with-times)

### [How to work with times](https://exceljet.net/videos/how-to-work-with-times)

Excel contains functions that will let you extract the hour, minute, and second values from a time, and a function called TIME that will let you put them back together again. Let's take a look. Here we have a set of random times in column B. First, I'll add a formula to column C to pick up the time...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20date%20and%20time%20series%20with%20formulas-thumb.png)](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)

### [How to create date and time series with formulas](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)

Although you can use Excel's AutoFill feature to fill in a series of dates and times, you can also do the same thing with formulas. The advantage of using a formula is that you can easily change the starting value and generate a new series. Let's take a look. Often you'll need to generate a series...

Related functions
-----------------

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

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
    
*   [Time duration with days](https://exceljet.net/formulas/time-duration-with-days)
    
*   [Parse time string to time](https://exceljet.net/formulas/parse-time-string-to-time)
    
*   [Time in hundredths of a second](https://exceljet.net/formulas/time-in-hundredths-of-a-second)
    
*   [Add decimal hours to time](https://exceljet.net/formulas/add-decimal-hours-to-time)
    
*   [Sequence of times](https://exceljet.net/formulas/sequence-of-times)
    
*   [Convert text timestamp into time](https://exceljet.net/formulas/convert-text-timestamp-into-time)
    
*   [Sum time over 30 minutes](https://exceljet.net/formulas/sum-time-over-30-minutes)
    
*   [Count times in a specific range](https://exceljet.net/formulas/count-times-in-a-specific-range)
    
*   [Convert UTC timestamp to Excel datetime](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime)
    

### Videos

*   [How to create date and time series with formulas](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)
    
*   [How to work with times](https://exceljet.net/videos/how-to-work-with-times)
    

### Functions

*   [DATE Function](https://exceljet.net/functions/date-function)
    

### Links

*   [Microsoft TIME function documentation](https://support.office.com/en-us/article/time-function-9a5aff99-8f7d-4611-845e-747d0b8d5457)
    

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