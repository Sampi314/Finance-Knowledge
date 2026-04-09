# Group times into 3 hour buckets - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/group-times-into-3-hour-buckets

---

[Skip to main content](https://exceljet.net/formulas/group-times-into-3-hour-buckets#main-content)

[](https://exceljet.net/formulas/group-times-into-3-hour-buckets#)

*   [Previous](https://exceljet.net/formulas/group-numbers-with-vlookup)
    
*   [Next](https://exceljet.net/formulas/group-times-into-unequal-buckets)
    

[Grouping](https://exceljet.net/formulas#Grouping)

Group times into 3 hour buckets
===============================

by Dave Bruns · Updated 22 Sep 2020

Related functions 
------------------

[FLOOR](https://exceljet.net/functions/floor-function)

![Excel formula: Group times into 3 hour buckets](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/group%20times%20into%203%20hour%20buckets.png "Excel formula: Group times into 3 hour buckets")

Summary
-------

To group times into buckets (i.e. group by 2 hours, group by 3 hours, etc.) you can use the [FLOOR function](https://exceljet.net/functions/floor-function)
. In the example shown, the formula in E5 is:

    =FLOOR(D5,"3:00")
    

Generic formula
---------------

    =FLOOR(time,"3:00")

Explanation 
------------

If you need to group times into buckets (i.e. group by 6 hours, group by 3 hours, etc.) you can do so with a rounding function called FLOOR.

In the example shown, we have a number of transactions, each with a timestamp. Let's say you want to group these transactions into buckets of 3 hours like this:

12:00 AM-3:00 AM  
3:00 AM-6:00 AM  
6:00 AM-9:00 AM  
9:00 AM-12:00 PM

For example, a time of 2:30 AM, needs to go into the 12:00 AM - 3:00 AM bucket. A time of 8:45 AM needs to go into the 6:00 AM-9:00 AM bucket, and so on.

If you think about it, one way to do this is to round each time until it fits into the right bucket. However, unlike normal rounding, where we might round to the _nearest_ multiple, in this case, we want to round _down to the nearest multiple_, starting at midnight.

Because [Excel times are just decimal numbers](https://exceljet.net/glossary/excel-time)
, you can easily do this with the [FLOOR function](https://exceljet.net/functions/floor-function)
, which rounds down to a multiple that you supply (FLOOR calls the argument that represents multiple "significance"). Even better, FLOOR understands how to round time provided in a format like "h:mm" (for example, "3:00", "12:00", etc.).

In the example shown, the formula in E5 is:

    =FLOOR(D5,"3:00")
    

FLOOR knows how to read time, so it interprets 3:00 as its decimal equivalent, 0.125. It then simple rounds down each time to the nearest multiple of 0.125 You can use this same approach to group times into any standard bucket that you like.

If you have times that span one or more days, you can use the MOD function to extract just the time, as explained [here](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
.

### Pivot tables

Pivot tables will  automatically group times into buckets of 1 hour, but they can't automatically group into other time buckets. However, using the approach outlined on this page, you can group time as you like, then run the resulting data through a pivot table to summarize.

Related formulas
----------------

[![Excel formula: Group times into unequal buckets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/group%20times%20into%20unequal%20buckets.png "Excel formula: Group times into unequal buckets")](https://exceljet.net/formulas/group-times-into-unequal-buckets)

### [Group times into unequal buckets](https://exceljet.net/formulas/group-times-into-unequal-buckets)

If you need to group times into buckets that are not the same size (i.e. 12 AM-7 AM, 7 AM-12 PM, etc.) you can use the VLOOKUP function in approximate match mode. The problem There are several ways to group times in Excel. If you just need to group times by the hour, a pivot table is very quick and...

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

[![Excel formula: Round time to nearest 15 minutes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20time%20to%20nearest%2015%20minutes.png "Excel formula: Round time to nearest 15 minutes")](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

### [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

MROUND rounds to nearest values based on a supplied multiple. When you supply "0:15" as the multiple, Excel internal converts 0:15 into 0.0104166666666667, which is the decimal value that represents 15 minutes, and rounds using that value. You can also express 15 minutes in a formula with this...

[![Excel formula: Random times at specific intervals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20times%20at%20specific%20intervals.png "Excel formula: Random times at specific intervals")](https://exceljet.net/formulas/random-times-at-specific-intervals)

### [Random times at specific intervals](https://exceljet.net/formulas/random-times-at-specific-intervals)

The RAND function generates a decimal number between zero and 1. So, you might get output like this from RAND() in three cells: 0.54739314 0.919767722 0.633760119 Dates in Excel are defined as simple numbers, where 1 = 1 day. This means you can simply divide 1 by the decimal value of time to get a...

Related functions
-----------------

[![Excel FLOOR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20floor%20function.png "Excel FLOOR function")](https://exceljet.net/functions/floor-function)

### [FLOOR Function](https://exceljet.net/functions/floor-function)

The Excel FLOOR function rounds a given number down to the nearest specified multiple. FLOOR works like the MROUND function, but FLOOR _always rounds down_.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Group times into unequal buckets](https://exceljet.net/formulas/group-times-into-unequal-buckets)
    
*   [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
    
*   [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)
    
*   [Random times at specific intervals](https://exceljet.net/formulas/random-times-at-specific-intervals)
    

### Functions

*   [FLOOR Function](https://exceljet.net/functions/floor-function)
    

### Articles

*   [Pivot Table Tips](https://exceljet.net/articles/pivot-table-tips)
    

### Links

*   [Three ways to group time in Excel (ExcelCampus)](http://www.excelcampus.com/charts/group-times-in-excel/)
    

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