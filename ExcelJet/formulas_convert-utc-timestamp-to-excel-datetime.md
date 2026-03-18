# Convert UTC timestamp to Excel datetime - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime

---

[Skip to main content](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime#main-content)

[](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime#)

*   [Previous](https://exceljet.net/formulas/convert-unix-time-stamp-to-excel-date)
    
*   [Next](https://exceljet.net/formulas/count-birthdays-by-month)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert UTC timestamp to Excel datetime
=======================================

by Dave Bruns · Updated 24 Jan 2026

Related functions 
------------------

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[TIME](https://exceljet.net/functions/time-function)

[SUM](https://exceljet.net/functions/sum-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9492/download?token=O5MIWDAi)
 (20.9 KB)

![Excel formula: Convert UTC timestamp to Excel datetime](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert-utc-timestamp-to-excel-datetime.png "Excel formula: Convert UTC timestamp to Excel datetime")

Summary
-------

To convert a UTC timestamp to a value that Excel can recognize as a date and time (a datetime), you can use a formula based on the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
. In the worksheet shown, the formula in cell D5 looks like this:

    =--SUBSTITUTE(SUBSTITUTE(B5,"T"," "),"Z","")
    

The result in cell D5 is a [datetime](https://exceljet.net/glossary/excel-datetime)
 value that Excel recognizes as January 18, 2026, at 8:00 AM. As the formula is copied down, it converts the other UTC timestamps to datetimes. You can display the datetime as you like with a custom number format. In the example shown, the datetime is displayed with the custom format `d-mmm-yy h:mm AM/PM`.

> UTC timestamps are in Coordinated Universal Time (UTC), which is the same as Greenwich Mean Time (GMT). See below for instructions on how to convert UTC timestamps to a different timezone.

Generic formula
---------------

    =--SUBSTITUTE(SUBSTITUTE(A1,"T"," "),"Z","")

Explanation 
------------

UTC timestamps like `2026-01-18T08:00:00Z` are a common standard for representing dates and times, but Excel won't correctly recognize this format without some help. If you try to apply date formatting to a UTC timestamp, nothing happens.

In this example, the goal is to convert UTC timestamps to datetimes that Excel can recognize. In addition, we'll look at how to convert UTC timestamps to datetimes in other time zones.

### Table of contents

*   [What are UTC timestamp?](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime#what-are-utc-timestamps)
    
*   [About Excel datetimes](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime#about-excel-datetimes)
    
*   [Entering datetimes in Excel](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime#entering-datetimes-in-excel)
    
*   [Converting UTC timestamps with SUBSTITUTE](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime#converting-utc-timestamps-with-substitute)
    
*   [Converting UTC timestamps with TEXTSPLIT](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime#converting-utc-timestamps-with-textsplit)
    
*   [Converting UTC timestamps to other time zones](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime#converting-utc-timestamps-to-other-timezones)
    
*   [Summary](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime#summary)
    

### What are UTC timestamps?

UTC timestamps are a standard format for representing dates and times. This format is a text value that conforms to the [ISO 8601 standard](https://en.wikipedia.org/wiki/ISO_8601)
 for representing dates and times. The generic format is `YYYY-MM-DDTHH:MM:SSZ` which looks like this: `2026-01-18T08:00:00Z`. The "T" separates the date from the time, and the "Z" at the end stands for "Zulu time", which is another name for UTC (Coordinated Universal Time), also known as Greenwich Mean Time (GMT).

You'll run into UTC timestamps when you're working with data from APIs, web services, databases, and data exports. They're popular because they're unambiguous – there's no confusion about whether 01/02/2026 means January 2nd or February 1st, and the timezone (GMT) is also known.

The problem with UTC timestamps is that Excel doesn't recognize them as dates. If you paste a UTC timestamp into a cell and try to format it as a date, nothing happens. The same is true if you try a function like MONTH or YEAR. Excel just sees text, not a date.

### About Excel datetimes

In Excel, [dates are large serial numbers](https://exceljet.net/glossary/excel-date)
 starting on January 1, 1900. The date January 1, 1900 is the serial number 1, January 2, 1900 is the serial number 2, and so on. The date January 1, 2026 is represented as the serial number 46023. Because each date is a number, and there are 24 hours in a day, [Excel times are fractions of a day](https://exceljet.net/glossary/excel-time)
. The time 12:00 AM is represented as the decimal value 0. The time 12:00 PM is the decimal value 0.5. The time 6:00 PM is the decimal value 0.75.

Although many users don't realize it, dates with times are stored as a single number in a cell. For example, January 18, 2026 12:00 PM is stored in Excel as the number 46040.5. This is referred to as a "[datetime](https://exceljet.net/glossary/excel-datetime)
" value - a single number that represents both a date and a time. Because the UTC timestamp contains both a date and a time, our goal is to convert the UTC timestamp to a datetime value that Excel can recognize.

> Tip: A good way to check datetimes in Excel is to temporarily format them using the General number format (the [shortcut](https://exceljet.net/shortcuts)
>  is Ctrl + Shift + ~). This will let you see the number that represents the date and time.

### Entering datetimes in Excel

One way to enter a datetime in Excel is to use a formula based on the [DATE](https://exceljet.net/functions/date-function)
 and [TIME](https://exceljet.net/functions/time-function)
 functions. For example, to enter the datetime January 18, 2026 at 12:00 PM, you can use a formula like this:

    =DATE(2026,1,18)+TIME(12,0,0)
    

This formula returns the datetime value January 18, 2026 at 12:00 PM (46040.5). Of course, most users will enter the date and times manually by typing the date and time in a cell. The trick is to enter the date and time separated by a space. For example, to enter January 18, 2026 at 12:00 PM, type `18-Jan-2026 12:00 PM`, and Excel will automatically convert the text to a datetime value. Importantly, you can also enter a datetime in the UTC format by removing the "T" and "Z".

    2026-01-18 12:00:00 // YYYY-MM-DD HH:MM:SS
    

Excel will correctly understand this as a datetime value. To summarize, if we remove the "T" and "Z" from the UTC timestamp, Excel will be able to interpret it as a valid datetime. This is the approach we will take in the following examples.

> Tip: you can also enter a format like `1/18/2026 12:00 PM` or `18/1/2026 12:00 PM` depending on your regional settings. However, this can be confusing and ambiguous and result in incorrect dates. A format like `2026-01-18 12:00 PM` or `2026-01-18 12:00` avoids this confusion.

### Converting UTC timestamps with SUBSTITUTE

Since we want to remove the 'T' and the 'Z' from the UTC timestamp, one solution is to use the [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
 function. The SUBSTITUTE function replaces text in a text string with another text string. To replace the "T" with a space, and to remove the "Z" altogether, we can use SUBSTITUTE like this:

    =SUBSTITUTE(B5,"T"," ") // replace the "T" with a space
    =SUBSTITUTE(B5,"Z","") // remove the "Z"
    

Note in the second formula, we are removing the "Z" altogether by using an [empty string](https://exceljet.net/glossary/empty-string)
 (""). By nesting the two SUBSTITUTE functions together, we can remove both the "T" and the "Z" in a single formula:

    =SUBSTITUTE(SUBSTITUTE(B5,"T"," "),"Z","") // remove both the "T" and the "Z"
    

The inner SUBSTITUTE function replaces the "T" with a space and hands the result to the outer SUBSTITUTE function, which then replaces the "Z" with an empty string. The final result is the text string "2026-01-18 08:00:00" without the "T" and "Z".

You might think we are done at this point, but we aren't quite finished. If you use the formula above, Excel will simply return the text string without recognizing it as a date/time value. The final step is to give Excel a little kick in the butt to make it evaluate the text string as a number. One trick is to use the [double negative](https://exceljet.net/glossary/double-unary)
 operator (--). This is the final formula in cell D5:

    =--SUBSTITUTE(SUBSTITUTE(B5,"T"," "),"Z","")
    

![Converting a UTC timestamp with the SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/convert-utc-timestamp-to-excel-datetime-with-substitute.png "Converting a UTC timestamp with the SUBSTITUTE function")

The double negative (--, also called double unary) is a simple math operation that causes Excel to try to interpret the text string as a _number_. The result is the datetime value January 18, 2026 at 8:00 AM (46040.3333333333). To display that date and time together, we are using the [custom number format](https://exceljet.net/articles/custom-number-formats)
 `d-mmm-yy h:mm AM/PM`.

> Excel's laziness here isn't really surprising. SUBSTITUTE is a text function, and it returns a text string, so Excel leaves it alone. The only thing worse than a lazy Excel is a hyper Excel that converts values without asking.

### Converting UTC timestamps with TEXTSPLIT

Of course, since this is Excel, there is always another way to solve the problem. Another way to convert the UTC timestamp to a datetime value is to use the [TEXTSPLIT](https://exceljet.net/functions/textsplit-function)
 function. TEXTSPLIT splits a text string into an array of values based on a delimiter. One interesting feature of TEXTSPLIT is that the delimiter itself is lost in the process. For example, if we use TEXTSPLIT to split the UTC timestamp with the "T" as the delimiter, we get an [array](https://exceljet.net/glossary/array)
 with two separate values, the date and the time.

    =TEXTSPLIT(B5,"T") // returns {"2026-01-18","08:00:00Z"}
    

Note that the "T" is lost in the process. We can actually go one step further and split the UTC timestamp with the "T" and "Z" as the delimiters in a single formula:

    =TEXTSPLIT(B5,{"T","Z"},,1) // returns {"2026-01-18","08:00:00"}
    

Note that we have provided the delimiters as an [array constant](https://exceljet.net/glossary/array-constant)
 and also set _ignore\_empty_ to 1 (TRUE). We need to set _ignore\_empty_ to TRUE to prevent TEXTSPLIT from returning an array with three values: {"2026-01-18","08:00:00",""}, which comes from the "Z" delimiter.

Okay, so at this point, the formula above will split the UTC timestamp into two values: the date and the time. How can we bring them back together again? Since our goal is to get a single numeric value in the end, it's actually pretty simple. We can simply wrap the formula in the [SUM function](https://exceljet.net/functions/sum-function)
 like this:

    =SUM(--TEXTSPLIT(B5,{"T","Z"},,1))
    

![Converting a UTC timestamp with the TEXSPLIT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/convert-utc-timestamp-to-excel-datetime-with-textsplit.png "Converting a UTC timestamp with the TEXSPLIT function")

Notice we are using the double unary operator (--) trick again to convert the text strings returned by TEXTSPLIT to numbers before adding them together. The result is the datetime value January 18, 2026 at 8:00 AM (46040.3333333333).

Is this formula better than the SUBSTITUTE formula? Well, it's certainly more clever, but it's also more complex. But I think it is also a good learning formula because it brings together many important concepts at once. It also manages the date and time separately, which might be convenient in some situations.

### Converting UTC timestamps to other time zones

In the previous examples, we converted the UTC timestamp to a datetime value in the UTC timezone, also known as Greenwich Mean Time (GMT). But what if you need to convert the UTC timestamp to a datetime value in a different timezone, like the Pacific Standard Time (PST) timezone?

To do this, we need to know the offset between the UTC timezone and the target timezone. For example, the offset between the UTC timezone and the Pacific Standard Time (PST) timezone is -8 hours. This means that when the UTC timestamp is 8:00 AM, the Pacific Standard Time (PST) timestamp is 12:00 AM. The offset is negative because the Pacific Standard Time (PST) timezone is 8 hours behind the UTC timezone.

To convert the UTC timestamp to a datetime value in the Pacific Standard Time (PST) timezone, we can use either formula below:

    =--SUBSTITUTE(SUBSTITUTE(B5,"T"," "),"Z","") - TIME(8,0,0)
    =SUM(--TEXTSPLIT(B5,{"T","Z"},,1)) - TIME(8,0,0)
    

Note that both formulas are based on the examples above. You can see how this works in the screenshot below, where we have converted the UTC timestamp to a datetime value in the Pacific Standard Time (PST) timezone with the TEXTSPLIT option:

![Converting a UTC timestamp to a given timezone](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/convert-utc-timestamp-to-a-given-timezone.png "Converting a UTC timestamp to a given timezone")

The time zone conversion is handled with the [TIME function](https://exceljet.net/functions/time-function)
, which creates a time value of 8 hours. We simply subtract this time value from the result to get the datetime value in the Pacific Standard Time (PST) timezone. To convert to Eastern Standard Time (EST), which is UTC-5, we can simply subtract 5 hours from the result:

    =--SUBSTITUTE(SUBSTITUTE(B5,"T"," "),"Z","") - TIME(5,0,0)
    =SUM(--TEXTSPLIT(B5,{"T","Z"},,1)) - TIME(5,0,0)
    

### Summary

UTC timestamps are a common format for dates and times in data exports, APIs, and other systems. They look like this: "2026-01-18T08:00:00Z". The problem is that Excel doesn't recognize this format as a date. If you try to apply date formatting to a UTC timestamp, nothing happens. Fortunately, if you strip out the "T" and "Z", Excel will recognize what's left as a valid datetime. The SUBSTITUTE approach is simple and works in all versions of Excel:

    =--SUBSTITUTE(SUBSTITUTE(B5,"T"," "),"Z","")
    

The TEXTSPLIT approach is a bit more clever, and a good way to learn about delimiters and array handling:

    =SUM(--TEXTSPLIT(B5,{"T","Z"},,1))
    

Both formulas use the double negative (--) trick to force Excel to evaluate the text as a number. Once you have a proper datetime value, you can format it as you like and adjust for timezone offsets by adding or subtracting hours with the TIME function.

Related formulas
----------------

[![Excel formula: Convert text to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20to%20date.png "Excel formula: Convert text to date")](https://exceljet.net/formulas/convert-text-to-date)

### [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)

The DATE function creates a valid date using three arguments: year, month, and day: =DATE(year,month,day) In cell C6, we use the LEFT, MID, and RIGHT functions to extract each of these components from a text string, and feed the results into the DATE function: =DATE(LEFT(B6,4),MID(B6,5,2),RIGHT(B6,...

[![Excel formula: TEXTSPLIT get numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/TEXTSPLIT_get_numbers.png "Excel formula: TEXTSPLIT get numeric values")](https://exceljet.net/formulas/textsplit-get-numeric-values)

### [TEXTSPLIT get numeric values](https://exceljet.net/formulas/textsplit-get-numeric-values)

In this example, we have comma-separated text in column B. The goal is to split the text in column B into columns D through G while at the same time converting the numbers to true numeric values. The challenge is that TEXTSPLIT always returns text, so we need a way to convert the numbers while...

Related functions
-----------------

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel TIME function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_time.png "Excel TIME function")](https://exceljet.net/functions/time-function)

### [TIME Function](https://exceljet.net/functions/time-function)

The Excel TIME function is a built-in function that allows you to create a time with individual hour, minute, and second components. The TIME function is useful when you want to assemble a proper time inside another formula.

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

### Formulas

*   [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)
    
*   [TEXTSPLIT get numeric values](https://exceljet.net/formulas/textsplit-get-numeric-values)
    

### Functions

*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [TIME Function](https://exceljet.net/functions/time-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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