# Excel TEXT function | Exceljet

**Source:** https://exceljet.net/functions/text-function

---

[Skip to main content](https://exceljet.net/functions/text-function#main-content)

[](https://exceljet.net/functions/text-function#)

*   [Previous](https://exceljet.net/functions/substitute-function)
    
*   [Next](https://exceljet.net/functions/textjoin-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

TEXT Function
=============

by Dave Bruns · Updated 11 Nov 2024

Related functions 
------------------

[DOLLAR](https://exceljet.net/functions/dollar-function)

[FIXED](https://exceljet.net/functions/fixed-function)

![Excel TEXT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")

Summary
-------

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

Purpose 
--------

Convert a number to text with a number format

Return value 
-------------

A number formatted as text in the given format.

Syntax
------

    =TEXT(value,format_text)

*   _value_ - The number to convert.
*   _format\_text_ - The number format to use.

Using the TEXT function 
------------------------

The TEXT function in Excel is a tool for formatting numbers, dates, and times as text. The purpose of the TEXT function is to convert a number to text using a specified format code. TEXT is most often used to control the formatting of a number embedded into a text string. However, TEXT is also a clever way to test dates in more advanced formulas (see [below](https://exceljet.net/functions/text-function#using-text-in-other-formulas)
 for an example).

### Table of Contents

*   [Syntax and example](https://exceljet.net/functions/text-function#syntax-and-example)
    
*   [Why do we need the TEXT function?](https://exceljet.net/functions/text-function#why-do-we-need-the-text-function)
    
*   [TEXT with dates](https://exceljet.net/functions/text-function#text-with-dates)
    
*   [TEXT with times](https://exceljet.net/functions/text-function#text-with-times)
    
*   [TEXT with percentages](https://exceljet.net/functions/text-function#text-with-percentages)
    
*   [Using TEXT in other formulas](https://exceljet.net/functions/text-function#using-text-in-other-formulas)
    
*   [Notes](https://exceljet.net/functions/text-function#notes)
    

### Syntax and example

The TEXT function takes two arguments, _value_ and _format\_text_.

*   _Value_ is the number to be formatted as text and should be a numeric value. Most often, this is a cell reference like A1. Note that the _value_ must be a number for TEXT to do anything. If the _value_ is already text, no formatting will be applied.
*   _Format\_text_ is a text string that contains the format codes to apply to _value_. Note that _format\_text_ must be enclosed in double quotes (""), and must contain valid number format codes.

Assume cell A1 contains the number 1500.35, and your goal is to display the number as "$1,500.35". You can do that by providing the number format "$#,##0.00" with TEXT like this:

    =TEXT(A1,"$#,##0.00") // returns "$150.35"

The codes provided in format\_codes can be adjusted to display decimal numbers, percentages, dates, times, and more.

> Excel provides a huge number of codes that can be used to format numbers, including dates, times, currency, percentages, and more. For a detailed overview with many examples, see [Excel Custom Number Formats](https://exceljet.net/articles/custom-number-formats)
> .

### Why do we need the TEXT function?

Why do we need the TEXT function? Can't we just apply Excel's built-in number formatting to format numbers in a worksheet? Yes. In general, you should always try to use regular number formatting first because it preserves the numeric value underneath. Keeping the number allows it to be used in standard numeric calculations.

The TEXT function, by contrast, actually _converts_ a number to text. The result is _text_, so numbers returned by TEXT _can't be used in numeric calculations_. However, there are still many situations where TEXT is quite helpful. The most common example is when you need to embed a number inside a text string. For example, assume we have the date 20-Oct-2024 in cell A1 and want to display a message like "The date is October 20, 2024". If we simply [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the text to cell A1 like this:

    ="The date is "&A1 // returns "The date is 45585"

We end up with: "The date is 45585". Why? This happens because the date formatting applied to cell A1 is not part of the number, which is 45585 in Excel's [date system](https://exceljet.net/glossary/excel-date)
. The formatting is not available during concatenation. To include a _formatted date_ in a text string, we need to use the TEXT function to control formatting like this:

    ="The date is "&TEXT(A1,"mmmm d, yyyy")

This formula returns the date in a readable format like "The date is October 20, 2024".

> The TEXT function is especially useful when concatenating numbers and text. If you are new to the concept of concatenation, see [How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
> .

### TEXT with dates

With the date October 21, 2024, in cell A1, the TEXT function can be used like this:

    =TEXT(A1,"dd-mmm-yy") // returns"24-Oct-2024"
    =TEXT(A1,"mmmm d") // returns "October 21"
    

In the worksheet below, you can see how the TEXT function can be used to apply a variety of date formats to the date in cell B5:

![TEXT function date example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/text_function_date_example.png "TEXT function date example")

The formulas used in column D are below. The result is shown after the "//" marker.

    ="The year is "&TEXT($B$5,"yyyy") // "The year is 2024"
    ="The month is "&TEXT($B$5,"mmmm") // "The month is October"
    ="The month is "&TEXT($B$5,"mmm") // "The month is Oct"
    ="The month is "&TEXT($B$5,"mm") // "The month is 10"
    ="The day is "&TEXT($B$5,"dddd") // "The day is Monday"
    ="The day is "&TEXT($B$5,"ddd") // "The day is Mon"
    ="The day is "&TEXT($B$5,"dd") // "The day is 21"
    ="The day is "&TEXT($B$5,"ddd, mmm d") // "The day is Mon, Oct 21"
    

### TEXT with times

TEXT can format times as well as dates. For example, with the time 3:15 PM in cell A1, the TEXT function can print the time in a 24-hour format like this:

    ="The time is "&TEXT(A1,"hh:mm") // returns "The time is 15:00"
    

In the worksheet below, TEXT is configured to display the time in cell B5 in various ways:

![TEXT function time example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/text_function_time_example.png "TEXT function time example")

The formulas used in column D are below. The result is shown after the "//" marker.

    ="The hour is "&TEXT($B$5,"h AM/PM") // "The hour is 3 PM"
    ="The hour is "&TEXT($B$5,"hh") // "The hour is 15"
    ="The minutes are "&RIGHT(TEXT($B$5,"hhmm"),2) // "The minutes are 15"
    ="The AM/PM is "&TEXT($B$5,"AM/PM") // "The AM/PM is PM"
    ="The time is "&TEXT($B$5,"hhmm") // "The time is 1515"
    ="The time is "&TEXT($B$5,"hh:mm") // "The time is 15:15"
    ="The time is "&TEXT($B$5,"h:mm AM/PM") // "The time is 3:15 PM"
    

Note that the formula in D7 is not like the others. Because the code "mm" conflicts with the date formatting codes for "month" when used alone, we use the format code "hhmm". Then we use the [RIGHT function](https://exceljet.net/functions/right-function)
 to extract just the two characters to the right, which are minutes.

### TEXT with percentages

With the number 0.537 in cell A1, TEXT can be used to apply percentage formatting like this:

    =TEXT(A1,"0.0%") // returns "53.7%"
    =TEXT(A1,"0%") // returns "54%"
    

In the worksheet below, we use the TEXT function together with the [IFS function](https://exceljet.net/functions/ifs-function)
 to report the gain or loss as a percentage in column F. The formula in F5, copied down, looks like this:

    =IFS(D5>0,"Up "&TEXT(D5,"0.0%"),D5<0,"Down "&TEXT(D5,"0.0%"),D5=0,"Unchanged")

![TEXT function percentage example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/text_function_percentage_example.png "TEXT function percentage example")

The IFS function is used to control the flow of the formula by testing for three conditions. If the change is greater than zero, IFS returns:

    "Up "&TEXT(D5,"0.0%")

If the change is less than zero, IFS returns:

    "Down "&TEXT(D5,"0.0%")

Finally, if the change equals zero, IFS returns the message "Unchanged":

    "Unchanged"

The result in column F is that each row has a custom message that depends on whether the change is positive, negative, or zero.

### Using TEXT in other formulas

The TEXT function is surprisingly versatile and turns up in many other advanced formulas because it is so good an extracting useful information from a number. For example, in the worksheet below, the goal is to mark dates that occur in the same month and year with an "x". The TEXT provides an elegant way to do this in a simple formula.

![Example of the TEXT function in another formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/text_function_in_other_formulas_example.png "Example of the TEXT function in another formula")

For a detailed explanation of how this formula works, [see this page](https://exceljet.net/formulas/date-is-same-month-and-year)
. Here is a related example of the TEXT function [used to sort birthdays](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)
 while ignoring the year, useful when you want to see a list of birthdays in the coming year.

### Notes

*   The TEXT function always returns text.
*   _Value_ must be a numeric value.
*   _Format\_text_ must appear in double quotation marks.
*   The TEXT function can be used with [custom number formats](https://exceljet.net/articles/custom-number-formats)
    
*   TEXT always returns _text_. To keep the number, use [standard number formatting](https://exceljet.net/videos/how-to-use-number-formatting-in-excel)
    .

TEXT function examples
----------------------

[![Excel formula: Partial match with numbers and wildcard](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/partial%20match%20with%20numbers%20and%20wildcard.png "Excel formula: Partial match with numbers and wildcard")](https://exceljet.net/formulas/partial-match-with-numbers-and-wildcard)

### [Partial match with numbers and wildcard](https://exceljet.net/formulas/partial-match-with-numbers-and-wildcard)

Excel supports the wildcard characters "\*" and "?", and these wildcards can be used to perform partial (substring) matches in various lookup formulas. However, if you use wildcards with a number, you'll convert the numeric value to a text value. In other words, "\*"&99&"\*" = "\*99\*" (a text...

[![Excel formula: Get days, hours, and minutes between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20hours%20and%20minutes%20between%20dates2.png "Excel formula: Get days, hours, and minutes between dates")](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

### [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

Most of the work in this formula is done by the TEXT function, which applies a custom number format for hours and minutes to a value created by subtracting the start date from the end date. TEXT(C5-B5,"h"" hrs ""m"" mins """) This is an example of embedding text into a custom number format, and...

[![Excel formula: Average call time per month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_call_time_per_month.png "Excel formula: Average call time per month")](https://exceljet.net/formulas/average-call-time-per-month)

### [Average call time per month](https://exceljet.net/formulas/average-call-time-per-month)

In this example, the goal is to calculate the average call time (duration in minutes) for each month listed in column G using the dates in column B and the durations in column E. The article below explains two approaches. The first formula is based on the AVERAGEIFS function , which is designed to...

[![Excel formula: Happy birthday message](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/happy%20birthday%20message.png "Excel formula: Happy birthday message")](https://exceljet.net/formulas/happy-birthday-message)

### [Happy birthday message](https://exceljet.net/formulas/happy-birthday-message)

In this example, the goal is to display a Happy Birthday message when a birthday in a given cell matches the current date. The core of the problem is to compare the given birthday to the current date while ignoring the year. There are two main ways to approach the problem. The first way is to use...

[![Excel formula: Get last entry by month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20last%20entry%20by%20month%20and%20year.png "Excel formula: Get last entry by month and year")](https://exceljet.net/formulas/get-last-entry-by-month-and-year)

### [Get last entry by month and year](https://exceljet.net/formulas/get-last-entry-by-month-and-year)

Note: the lookup\_value of 2 is deliberately larger than any values in the lookup\_vector, following the concept of bignum . Working from the inside out, the expression: (TEXT($B$5:$B$13,"mmyy")=TEXT(E5,"mmyy")) generates strings like "0117" using the values in column B and E, which are then compared...

[![Excel formula: Max value on given weekday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_value_on_given_weekday.png "Excel formula: Max value on given weekday")](https://exceljet.net/formulas/max-value-on-given-weekday)

### [Max value on given weekday](https://exceljet.net/formulas/max-value-on-given-weekday)

In this example, the goal is to calculate the maximum value that occurs in a set of data on a given weekday (i.e. Monday, Tuesday, Wednesday, Thursday, Friday). In the current version of Excel, the simplest approach is to use the FILTER function. In older versions of Excel, you can use a...

[![Excel formula: Join date and text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_date_and_text.png "Excel formula: Join date and text")](https://exceljet.net/formulas/join-date-and-text)

### [Join date and text](https://exceljet.net/formulas/join-date-and-text)

In this example, the goal is to join a text string to a formatted date. The challenge is that numbers lose their formatting in Excel when they are concatenated in a formula. For example, if we have the date 31-Dec-1999 in cell B5, and we join B5 to a text string and don't control the date format...

[![Excel formula: Convert date to Julian format](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20Julian%20format.png "Excel formula: Convert date to Julian format")](https://exceljet.net/formulas/convert-date-to-julian-format)

### [Convert date to Julian format](https://exceljet.net/formulas/convert-date-to-julian-format)

This formula builds the final result in 2 parts, joined by concatenation with the ampersand (...

[![Excel formula: Get next day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_next_day_of_week.png "Excel formula: Get next day of week")](https://exceljet.net/formulas/get-next-day-of-week)

### [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)

In this example, the goal is to get the next specified weekday, starting on a given start date. So for example, with a valid start date in column B, we want to be able to ask for the next Monday, the next Tuesday, the next Wednesday, and so on. This article describes two different ways of solving...

[![Excel formula: Max by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_by_month.png "Excel formula: Max by month")](https://exceljet.net/formulas/max-by-month)

### [Max by month](https://exceljet.net/formulas/max-by-month)

In this example, the goal is to get the maximum value in the data for each month listed in column E. The easiest way to do this is with the MAXIFS function, which is designed to return a maximum value based on one or more criteria. In older versions of Excel without the MAXIFS function, you can use...

[![Excel formula: Last updated date stamp](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/date%20last%20updated.png "Excel formula: Last updated date stamp")](https://exceljet.net/formulas/last-updated-date-stamp)

### [Last updated date stamp](https://exceljet.net/formulas/last-updated-date-stamp)

The TEXT function can apply number formatting to numbers just like Excel's built-in cell formats for dates, currency, fractions, and so on. However, unlike Excel's cell formatting, the TEXT function works inside a formula and returns a result that is text. You can use TEXT to format numbers that...

[![Excel formula: Sort birthdays by month and day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sort%20birthdays%20by%20month%20and%20day.png "Excel formula: Sort birthdays by month and day")](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)

### [Sort birthdays by month and day](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)

In this example, the goal is to sort a list of names and birthdays by month and year. The complication is that the birthdays also include a birth year, so if we try to sort the raw data by birthdays, we'll end up with a list of birthdays sorted first by year. We will actually see the oldest people...

[![Excel formula: Add leading zeros to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add%20leading%20zeros%20to%20numbers.png "Excel formula: Add leading zeros to numbers")](https://exceljet.net/formulas/add-leading-zeros-to-numbers)

### [Add leading zeros to numbers](https://exceljet.net/formulas/add-leading-zeros-to-numbers)

In this example, the goal is to add leading zeros to a given number so that the total number of characters displayed is 5. Sometimes this is referred to as "padding" a number with zeros, because the number of zeros needed is variable. If the original number contains 2 digits, 3 zeros are added. If...

[![Excel formula: Get day name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20day%20name%20from%20date.png "Excel formula: Get day name from date")](https://exceljet.net/formulas/get-day-name-from-date)

### [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)

In this example, the goal is to get the day name (i.e. Monday, Tuesday, Wednesday, etc.) from a given date. There are several ways to go about this in Excel, depending on your needs. This article explains three approaches: Display date with a custom number format Convert date to day name with TEXT...

[![Excel formula: Get month name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20month%20name%20from%20date_0.png "Excel formula: Get month name from date")](https://exceljet.net/formulas/get-month-name-from-date)

### [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)

In this example, the goal is to get and display the month name from any given date. There are several ways to go about this in Excel, depending on whether you want to extract the month name as text, or just display a valid Excel using the month name. To extract the month name from a date as text ,...

TEXT function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20test%20a%20conditional%20formatting%20formula-thumb.png)](https://exceljet.net/videos/how-to-test-a-conditional-formatting-formula)

### [How to test a conditional formatting formula](https://exceljet.net/videos/how-to-test-a-conditional-formatting-formula)

In this video, we'll look at an easy way to test a conditional formatting formula before you create the rule. When you use a formula to apply conditional formatting, it can be tricky to set the formula up correctly. The dialog used to create and edit the formula doesn't provide all the nice...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20join%20text%20with%20numbers-thumb_0.png)](https://exceljet.net/videos/how-to-join-text-with-numbers)

### [How to join text with numbers](https://exceljet.net/videos/how-to-join-text-with-numbers)

In this video we'll look at how to convert numbers to text using a function called TEXT. This is useful when you want to convert a number to text, or when you want to join a number with text using a specific number format. Let's take a look. The TEXT function has just one purpose—to convert a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20the%20number%20of%20days%20between%20dates-thumb.png)](https://exceljet.net/videos/how-to-calculate-the-number-of-days-between-dates)

### [How to calculate the number of days between dates](https://exceljet.net/videos/how-to-calculate-the-number-of-days-between-dates)

In this video we'll look at how to calculate the number of days between dates. To get started, let's first set up some dates, so we have a visual representation to refer to. In C5, I'll add a start date. Then, I'll add and copy a formula below that simply adds "1" to each date above. The result is...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20concatenation%20to%20clarify%20assumptions-thumb.png)](https://exceljet.net/videos/how-to-use-concatenation-to-clarify-assumptions)

### [How to use concatenation to clarify assumptions](https://exceljet.net/videos/how-to-use-concatenation-to-clarify-assumptions)

One of the most basic and useful features in Excel is the ability to concatenate values with text. CONCATENATE is just a fancy word for "join." In this video we'll look at a simple way to use concatenation with the TEXT formula to highlight assumptions in a break-even model. This model calculates...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20combine%20functions%20in%20a%20formula-thumb.png)](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)

### [How to combine functions in a formula](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)

In this video I'm going to show you how you can use multiple Excel functions to split, manipulate, and rejoin values inside a single formula. Here we have some sample data and, in column B, we have text values with a number at the end. What we want to do is increment these numbers using the value...

Related functions
-----------------

[![Excel DOLLAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20dollar%20function.png "Excel DOLLAR function")](https://exceljet.net/functions/dollar-function)

### [DOLLAR Function](https://exceljet.net/functions/dollar-function)

The Excel DOLLAR function converts a number to text using the Currency number format. The TEXT function can do the same thing, and is much more versatile.

[![Excel FIXED function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20fixed%20function.png "Excel FIXED function")](https://exceljet.net/functions/fixed-function)

### [FIXED Function](https://exceljet.net/functions/fixed-function)

The Excel FIXED function converts a number to text with fixed number of decimals, rounding as needed with the given number of decimals. The FIXED function can be useful when concatenating a formatted number text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)
    
*   [Max value on given weekday](https://exceljet.net/formulas/max-value-on-given-weekday)
    
*   [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)
    
*   [Create date range from two dates](https://exceljet.net/formulas/create-date-range-from-two-dates)
    
*   [Pad week numbers with zeros](https://exceljet.net/formulas/pad-week-numbers-with-zeros)
    
*   [Partial match with numbers and wildcard](https://exceljet.net/formulas/partial-match-with-numbers-and-wildcard)
    
*   [Convert numbers to text](https://exceljet.net/formulas/convert-numbers-to-text)
    
*   [List nth weekdays of the month](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)
    
*   [Get last entry by month and year](https://exceljet.net/formulas/get-last-entry-by-month-and-year)
    
*   [Pad a number with zeros](https://exceljet.net/formulas/pad-a-number-with-zeros)
    

### Videos

*   [How to calculate the number of days between dates](https://exceljet.net/videos/how-to-calculate-the-number-of-days-between-dates)
    
*   [How to join text with numbers](https://exceljet.net/videos/how-to-join-text-with-numbers)
    
*   [How to use concatenation to clarify assumptions](https://exceljet.net/videos/how-to-use-concatenation-to-clarify-assumptions)
    
*   [How to test a conditional formatting formula](https://exceljet.net/videos/how-to-test-a-conditional-formatting-formula)
    
*   [How to combine functions in a formula](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)
    

### Functions

*   [DOLLAR Function](https://exceljet.net/functions/dollar-function)
    
*   [FIXED Function](https://exceljet.net/functions/fixed-function)
    

### Articles

*   [Excel custom number formats](https://exceljet.net/articles/custom-number-formats)
    

### Links

*   [Microsoft TEXT function documentation](https://support.office.com/en-us/article/text-function-20d5ac4d-7b94-49fd-bb38-93d29371225c)
    

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