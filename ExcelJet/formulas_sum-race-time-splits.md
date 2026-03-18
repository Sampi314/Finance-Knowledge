# Sum race time splits - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-race-time-splits

---

[Skip to main content](https://exceljet.net/formulas/sum-race-time-splits#main-content)

[](https://exceljet.net/formulas/sum-race-time-splits#)

*   [Previous](https://exceljet.net/formulas/sum-by-fiscal-year)
    
*   [Next](https://exceljet.net/formulas/sum-time)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Sum race time splits
====================

by Dave Bruns · Updated 6 Mar 2024

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Sum race time splits](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Sum%20race%20time%20splits.png "Excel formula: Sum race time splits")

Summary
-------

To sum race time splits that are some combination of hours, minutes, and seconds, you can use the [SUM function](https://exceljet.net/functions/sum-function)
. The formula in cell H5, copied down, is:

    =SUM(C5:G5)
    

Generic formula
---------------

    =SUM(times)

Explanation 
------------

[Excel times are fractional numbers](https://exceljet.net/glossary/excel-time)
. This means you can add times together with the [SUM function](https://exceljet.net/functions/sum-function)
 to get total durations. However, you must take care to enter times with the right syntax and use a suitable time format to display results, as explained below.

### Enter times in the correct format

You must be sure that times are correctly entered in hh:mm:ss format. For example, to enter a time of 9 minutes, 3 seconds, type: 0:09:03. Excel will show the time in the formula bar as 12:09:03 AM, but will record the time properly as a decimal value.

Internally, Excel tracks times as decimal numbers, where 1 hour = 1/24, 1 minute = 1/(24\*60), and 1 second = 1/(24\*60\*60). How Excel displays time depends on what number format is applied.

### Use a suitable time format

When working with times, you must use a time format suitable to the problem. This usually means you will need to apply a [custom number format](https://exceljet.net/articles/custom-number-formats)
 to certain cells before you enter the time. This number format will control two things: (1) the format you must use to enter the time, and (2) the way the time is displayed. To apply a custom time format, follow these steps:

1.  Select the cells to format.
2.  Use Control + 1 (Command + 1 on a Mac) to open the Format cells dialog.
3.  Select the "Number" tab.
4.  Select "Custom" from the list to the left.
5.  Enter the desired time format and click OK to apply.

![Custom time format for hours, minutes, and seconds](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/custom%20time%20format.png?itok=NrXiD25A "Custom time format for hours, minutes, and seconds")

These are the number formats used in the example shown:

    mm:ss // split times
    h:mm:ss // total time
    

If total times may exceed 24 hours, use enclose the "h" in square brackets like "\[h\]":

    [h]:mm:ss
    

The square brackets tell Excel not to "reset" durations greater than 24 hours back to zero. Without the brackets, a time like 30:00:00 (30 hours) will _display_ as 6:00:00 because Excel will reset the time to zero at 24 hours.

### Tracking time with more precision

In the example above, we are tracking time down to a second, but there are cases where you will need to record time to a hundredth of a second or even a thousandth of a second (a millisecond). In that case, you will need to adjust the custom time format before entering the times. To enter time down to a hundredth of a second, use a custom time format like this:

    mm:ss.00
    

To enter time down to a thousandth of a second (i.e. a millisecond), use a custom time format like this:

    mm:ss.000
    

You will need to enter the seconds with a decimal value when a value is present. You can add h or \[h\] if needed to handle hours.

Related functions
-----------------

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SUM Function](https://exceljet.net/functions/sum-function)
    

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