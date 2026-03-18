# Time in hundredths of a second - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/time-in-hundredths-of-a-second

---

[Skip to main content](https://exceljet.net/formulas/time-in-hundredths-of-a-second#main-content)

[](https://exceljet.net/formulas/time-in-hundredths-of-a-second#)

*   [Previous](https://exceljet.net/formulas/time-duration-with-days)
    
*   [Next](https://exceljet.net/formulas/time-since-start-in-day-ranges)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Time in hundredths of a second
==============================

by Dave Bruns · Updated 11 Jul 2024

Related functions 
------------------

[TIME](https://exceljet.net/functions/time-function)

[SECOND](https://exceljet.net/functions/second-function)

[TIMEVALUE](https://exceljet.net/functions/timevalue-function)

[MOD](https://exceljet.net/functions/mod-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8293/download?token=EZ5QvapZ)
 (26.03 KB)

![Excel formula: Time in hundredths of a second](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/time_in_hundredths_of_a_second.png "Excel formula: Time in hundredths of a second")

Summary
-------

To display times in tenths, hundredths, or thousandths of a second, apply an appropriate number format. In the example shown, the number format applied to cells in the range C4:C16 is:

    mm:ss.00

The result is that the times in column C include minutes, seconds, and hundredths of a second (centiseconds).

Explanation 
------------

In the worksheet shown, we have race results for an 800m race. The goal is to display time in minutes, seconds, and hundredths of a second (centiseconds). Dealing with times that include fractional seconds can be tricky in Excel. The default time format will only show whole seconds and it is not obvious how to display seconds in smaller units. The first step is to apply a custom number format that specifically includes placeholders for tenths, hundredths, or thousandths of a second as needed. However, several quirks in Excel make working with fractional seconds more difficult than you would expect. This article explains these quirks and provides tips and formulas to make the process easier.

> Time values in Excel are fractions of 1, as explained [on this page](https://exceljet.net/glossary/excel-time)
> .

### Number formats for time with seconds

The first step in working with seconds in smaller increments is to apply a suitable number format. The following custom number formats will display tenths, hundredths, or thousandths of a second as noted:

    mm:ss.0 // tenths of a second (deciseconds)
    mm:ss.00 // hundredths of a second (centiseconds)
    mm:ss.000 // thousandths of a second (milliseconds)

If the time also includes hours, add a placeholder for hours like this:

    [h]:mm:ss.0 // tenths of a second (deciseconds)
    [h]:mm:ss.00 // hundredths of a second (centiseconds)
    [h]:mm:ss.000 // thousandths of a second (milliseconds)

The square bracket syntax "\[h\]" tells Excel to treat the time as a duration that may exceed 24 hours. Without the brackets, times with durations greater than 24 hours will appear to reset to zero every 24 hours. Note when you add a placeholder for hours, you must enter time starting with hours. For example, enter "1:05:31.25" for "1 hour, 5 minutes, and 31.25 seconds" and "0:07:45.10" for "0 hours, 7 minutes and 45.10 seconds". In short, you must enter time according to specified placeholders.

> Excel's number formats are a deep topic. See [Excel Custom Number Formats](https://exceljet.net/articles/custom-number-formats)
>  for more information.

### How to apply a custom time format

To enter and display time that includes a decimal value for seconds in Excel, you must first apply a custom format. The fastest way to do this is to use the Format Cells dialog box like this:

1.  Select the range of cells that will contain time values.
2.  Open Format cells with the [keyboard shortcut](https://exceljet.net/shortcuts)
     Control + 1
3.  Go to the "Number" tab, then select "Custom."
4.  In the "Type" field, enter mm:ss.00 for minutes, seconds, and hundredths of a second.
5.  Click the OK button to apply the format.

![Custom number format for time in hundredths of a second](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/custom_number_format_for_time_in_hundredths_of_a_second.png "Custom number format for time in hundredths of a second")

After the custom format is applied, you must enter the time in the format specified. For example, enter "01:45.73" for "1 minute, 45.73 seconds".

Video: [How to use time formatting in Excel](https://exceljet.net/videos/how-to-use-time-formatting-in-excel)

### Editing time in Excel

One of the frustrations of using a custom time format in Excel is that the format is not honored when editing an existing value. For example, you may have a time value like "01:50.82" in a cell but when you edit the cell, Excel will stubbornly present the time as "12:01:51 AM", ignoring the custom time format:

![Excel ignores custom time format when editing](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/excel_ignores_custom_time_format_when_editing.png "Excel ignores custom time format when editing")

While you can still see and edit whole minutes and seconds, fractional seconds are no longer visible. Often, it is easiest to enter the complete time again. In cases where you need to edit time more easily, one option is to set up a helper column that contains the time as a text value, then convert the text to a proper time with the [TIMEVALUE function](https://exceljet.net/functions/timevalue-function)
 as seen below:

![Editing hundredths of a second with a helper column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/editing_hundredths_of_a_second_with_a_helper_column.png "Editing hundredths of a second with a helper column")

The advantage of this approach is the text in column C is easy to edit without re-entering the time. If you are entering the times by hand, one frustration is that Excel _really likes to convert text into numbers_, which defeats the idea of entering text. If you have trouble entering times as text, prepend the text with a single quote (') like this:

    '01:50.82 // time as text value

The single quote will force Excel to treat the value as text, and the single quote will not display on the worksheet.

### Extracting fractional seconds from a time

When you have times in Excel that contain hundredths of a second, how can you extract seconds including any fractional part? This is a puzzling problem. Although Excel offers the [SECOND function](https://exceljet.net/functions/second-function)
 to extract seconds from a time, SECOND will _round fractional seconds to the nearest whole number_. For example, with the worksheet above, if we feed Mason's time in C5 and Henry's time in C6 into the SECOND function, we get back 51 and 54:

    =SECOND(C5) // returns 51.0
    =SECOND(C6) // returns 54.0

That means we can't use SECOND to extract seconds that contain a decimal value without losing precision. The solution is to use a manual formula to extract seconds like this:

    =MOD(C5*1440,1)*60

This formula works to extract fractional seconds from a time in three steps. The first step is to multiply by 1440. Excel stores dates and times as serial numbers where one day is 1.0. Since there are 1440 minutes in a day (24 hours x 60 minutes), multiplying the time by 1440 converts the time into minutes as a decimal value. With the time in C5 of 01:50.82 (stored as the decimal value 0.001282639 by Excel), we get 1.847:

    =MOD(1.847,1)*60

The next step is to use the MOD function to get fractional seconds. MOD is a shortcut here. Since we already have decimal minutes from the previous step, providing 1 as the divisor is a simple way to [remove the integer portion](https://exceljet.net/formulas/get-decimal-part-of-a-number)
 of the number (whole minutes) and return only the decimal part, 0.847:

    =MOD(1.847,1)*60
    =0.847*60

The third and final step is to multiply by 60 to convert decimal minutes to decimal seconds. Multiplying 0.847 x 60 results in 50.82 seconds:

    =0.847*60
    =50.82

This matches the value for seconds seen in cell C5. The worksheet below shows the result from all times in column C.

![Extracting fractional seconds from time in Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/extracting_fractional_seconds_from_time_in_excel.png "Extracting fractional seconds from time in Excel")

The formulas used to extract hours, minutes, and seconds are as follows:

    =HOUR(C5) // extract hours
    =MINUTE(C5) // extract minutes
    =MOD(C5*1440,1)*60 // extract fractional seconds

All three results are formatted as numbers, not times.

### A formula to create a time with fractional seconds

How do you create a time with fractional seconds with a formula? The first thing to know is that Excel's [TIME function](https://exceljet.net/functions/time-function)
 doesn't handle decimal values for hours, minutes, or seconds. You can see this behavior in the formulas below:

    =TIME(3,0,0) // returns 3 hours
    =TIME(3.5,0,0) // returns 3 hours

Although _hours_ is 3 in the first formula and 3.5 in the second, both formulas return the same result. TIME simply removes the decimal part (0.5) during calculation. Likewise, if we try to provide 30.5 for _seconds_, the decimal portion is discarded. Both formulas below return exactly 30 seconds:

    =TIME(0,0,30) // returns 30 seconds
    =TIME(0,0,30.5) // returns 30 seconds

Consequently, to create a time that includes decimal values for hours, minutes, or seconds, we can't use the TIME function. One solution is to use a purely math-based formula like this:

    =(hours/24)+(minutes/1440)+(seconds/86400)

You can hardcode decimal values for hours, minutes, and seconds directly into this formula, or plug in values from cell references on a worksheet. You can see how this formula works in the worksheet below, where the formula in F5, copied down, is:

    =(B5/24)+(C5/1440)+(D5/86400)

![A formula to create time with fractional seconds](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/formula_for_creating_a_time_with_fractional_seconds.png "A formula to create time with fractional seconds")

The final result is a list of original times above, complete with fractional seconds.

Related formulas
----------------

[![Excel formula: Convert Excel time to decimal hours](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20excel%20time%20to%20decimal%20hours.png "Excel formula: Convert Excel time to decimal hours")](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)

### [Convert Excel time to decimal hours](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)

In the Excel time system, one 24-hour day is equal to 1. This means times and hours are fractional values of 1, as shown in the table below: Hours Time Fraction Value 1 1:00 AM 1/24 0.04167 3 3:00 AM 3/24 0.125 6 6:00 AM 6/24 0.25 4 4:00 AM 4/24 0.167 8 8:00 AM 8/24 0.333 12 12:00 PM 12/24 0.5 18 6...

[![Excel formula: Convert decimal minutes to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20minutes%20to%20excel%20time.png "Excel formula: Convert decimal minutes to Excel time")](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)

### [Convert decimal minutes to Excel time](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Minutes Value Time 1 1/24 60 0.04167 1:00 3 3/24 180 0.125 3:00 6 6/24 360 0.25 6:00 4 4/24 240 0.167 4:00 8 8/24 480 0.333 8:00 12 12/24 720 0.5 12:00 18...

[![Excel formula: Convert decimal seconds to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20seconds%20to%20excel%20time.png "Excel formula: Convert decimal seconds to Excel time")](https://exceljet.net/formulas/convert-decimal-seconds-to-excel-time)

### [Convert decimal seconds to Excel time](https://exceljet.net/formulas/convert-decimal-seconds-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Minutes Seconds Value Time 1 1/24 60 3600 0.04167 1:00 3 3/24 180 10800 0.125 3:00 6 6/24 360 21600 0.25 6:00 12 12/24 720 43200 0.5 12:00 18 18/24 1080...

Related functions
-----------------

[![Excel TIME function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_time.png "Excel TIME function")](https://exceljet.net/functions/time-function)

### [TIME Function](https://exceljet.net/functions/time-function)

The Excel TIME function is a built-in function that allows you to create a time with individual hour, minute, and second components. The TIME function is useful when you want to assemble a proper time inside another formula.

[![Excel SECOND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_second_function.png "Excel SECOND function")](https://exceljet.net/functions/second-function)

### [SECOND Function](https://exceljet.net/functions/second-function)

The Excel SECOND function extracts the seconds component of a time as a number between 0-59. For example, when given the time 9:10:15 AM, SECOND will return 15. You can use the SECOND function to extract seconds into another cell.

[![Excel TIMEVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20timevalue%20function.png "Excel TIMEVALUE function")](https://exceljet.net/functions/timevalue-function)

### [TIMEVALUE Function](https://exceljet.net/functions/timevalue-function)

The Excel TIMEVALUE function converts a time represented as text into a proper Excel time. For example, the formula =TIMEVALUE("9:00 AM") returns 0.375, the numeric representation of 9:00 AM in Excel's time system. Numeric time values are more useful than text since they can be directly...

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Convert Excel time to decimal hours](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)
    
*   [Convert decimal minutes to Excel time](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)
    
*   [Convert decimal seconds to Excel time](https://exceljet.net/formulas/convert-decimal-seconds-to-excel-time)
    

### Functions

*   [TIME Function](https://exceljet.net/functions/time-function)
    
*   [SECOND Function](https://exceljet.net/functions/second-function)
    
*   [TIMEVALUE Function](https://exceljet.net/functions/timevalue-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    

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