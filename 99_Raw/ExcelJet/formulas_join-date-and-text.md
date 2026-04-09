# Join date and text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/join-date-and-text

---

[Skip to main content](https://exceljet.net/formulas/join-date-and-text#main-content)

[](https://exceljet.net/formulas/join-date-and-text#)

*   [Previous](https://exceljet.net/formulas/if-monday-roll-back-to-friday)
    
*   [Next](https://exceljet.net/formulas/last-n-days)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Join date and text
==================

by Dave Bruns · Updated 13 Sep 2024

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8311/download?token=n6-ucyOC)
 (17.89 KB)

![Excel formula: Join date and text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/join_date_and_text.png "Excel formula: Join date and text")

Summary
-------

To join a date with text, you can use concatenation with the [TEXT function](https://exceljet.net/functions/text-function)
 to control the date format. In the example shown, the formula in D5 is:

    ="The date is "&TEXT(B5,"dddd, mmmm d, yyyy")
    

The result is the text string "The date is Friday, December 31, 1999". As the formula is copied down the table, it calculates a similar result for all dates in column B.

Generic formula
---------------

    ="text"&TEXT(A1,format)

Explanation 
------------

In this example, the goal is to join a text string to a formatted date. The challenge is that numbers lose their formatting in Excel when they are concatenated in a formula. For example, if we have the date 31-Dec-1999 in cell B5, and we join B5 to a text string and don't control the date format with a formula like this:

    ="The date is "&B5

The date will revert to its raw [serial number](https://exceljet.net/glossary/excel-date)
 format and the result will show the date as a serial number like this:

    "The date is 36525".

This happens because the date December 31, 1999, is stored as the number 36525 by Excel. When date formatting is applied to a cell on the worksheet, the number is displayed as a date. However, when a cell value is concatenated to another value in a formula, it reverts to the raw number.

### Using the TEXT function to control number formatting

The [TEXT Function](https://exceljet.net/functions/text-function)
 is designed to apply a number format inside a formula. The generic syntax looks like this:

    TEXT(value,format_text)

Here, _value_ is the number to format, and _format\_text_ is a special [number format](https://exceljet.net/glossary/number-format)
 code to display the number in the desired format. For example, with the date December 31, 1999, in cell B5, we can use the TEXT function to display the month and year like this:

    TEXT(B5,"mmmm yyyy") // returns "December 1999"

### Concatenating with TEXT

[Concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
 is the process of joining values to form text strings. Since the TEXT function always returns text, it works perfectly for concatenating formatted numbers to text strings. In this example, the generic formula looks like this, where cell B5 contains a date:

    ="The date is"&B5
    

As mentioned, if we don't control the formatting for the date, the result will be a number. To maintain the date formatting, we just need to replace the cell reference with the TEXT function and provide a suitable date format. In the worksheet shown, the formula in cell E4 looks like this:

    ="The date is "&TEXT(B5,"dddd, mmmm d, yyyy")
    

The result is the text string "The date is Friday, December 31, 1999".

### Other date formats

You are not limited to formatting a date in the "long" format shown above. Excel's date formatting codes are flexible so you can format the same date in many different ways. The screen below shows how the same date in cell D2 can be formatted in eleven different ways by adjusting the date format codes in column B:

![Formatting the same date with different date format codes](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/join_date_and_text_date_formatting_options.png "Formatting the same date with different date format codes")

The formula in D5 looks like this:

    ="The date is "&TEXT($D$2,B5)

Inside the TEXT function, the _value_ is provided as $D$2, locked as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 so that it won't change as the formula is copied down, and _format\_text_ is supplied as cell B5 which contains the format codes to apply. As the formula is copied down, the reference to B5 changes while the reference to D2 does not. The final result is the same date displayed in eleven different ways.\*

_\* The results on rows 10 and 11 are the same in the example because there is no abbreviation for May. Change the date in D2 to another month to see different results._

### Helpful resources

The following links provide more examples of the concepts explained above:

*   [Excel's custom number formats](https://exceljet.net/articles/custom-number-formats)
     - a detailed overview on number formatting in Excel.
*   [How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
     - what concatenation is and how to use it.
*   [How to use number formatting in Excel](https://exceljet.net/videos/how-to-use-number-formatting-in-excel)
     - brief video.
*   [How to create a custom date format](https://exceljet.net/videos/how-to-create-a-custom-date-format)
     - brief video.

Related formulas
----------------

[![Excel formula: Extract date from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract_date_from_text_string.png "Excel formula: Extract date from text string")](https://exceljet.net/formulas/extract-date-from-text-string)

### [Extract date from text string](https://exceljet.net/formulas/extract-date-from-text-string)

In this example, the goal is to extract a date in a format like mm/dd/yy from a text string with a formula. The position of the date is not known, so the date must be located as a first step. This article explains two ways to solve this challenge: A "classic" formula based on the SEARCH function...

[![Excel formula: Get day name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20day%20name%20from%20date.png "Excel formula: Get day name from date")](https://exceljet.net/formulas/get-day-name-from-date)

### [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)

In this example, the goal is to get the day name (i.e. Monday, Tuesday, Wednesday, etc.) from a given date. There are several ways to go about this in Excel, depending on your needs. This article explains three approaches: Display date with a custom number format Convert date to day name with TEXT...

[![Excel formula: Get month name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20month%20name%20from%20date_0.png "Excel formula: Get month name from date")](https://exceljet.net/formulas/get-month-name-from-date)

### [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)

In this example, the goal is to get and display the month name from any given date. There are several ways to go about this in Excel, depending on whether you want to extract the month name as text, or just display a valid Excel using the month name. To extract the month name from a date as text ,...

[![Excel formula: Convert date to text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20text.png "Excel formula: Convert date to text")](https://exceljet.net/formulas/convert-date-to-text)

### [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)

Dates and times in Excel are stored as serial numbers and converted to human-readable values on the fly using number formats. When you enter a date in Excel, you can apply a number format to display that date as you like. Similarly, the TEXT function allows you to convert a date or time into text...

[![Excel formula: Join cells with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join%20cells%20with%20comma_0.png "Excel formula: Join cells with comma")](https://exceljet.net/formulas/join-cells-with-comma)

### [Join cells with comma](https://exceljet.net/formulas/join-cells-with-comma)

Working from the inside out, the formula first joins the values the 5 cells to the left using the concatenation operator (...

Related functions
-----------------

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20number%20number%20formatting-play.png)](https://exceljet.net/videos/how-to-use-number-formatting-in-excel)

### [How to use number formatting in Excel](https://exceljet.net/videos/how-to-use-number-formatting-in-excel)

In this lesson, we'll look at the Number format called "Number." The Number format provides three options: the ability to set a fixed number of decimal places, an option to use commas to separate thousandths, and several ways to display negative numbers. Let's take a look. To start off, let's copy...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_use_date_formatting-thumb.png)](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)

### [How to use date formatting in Excel](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)

In this lesson we'll take a look at the Date format. The Date format is flexible and can display the same date in many different ways. Let's take a look. Here we have a set of dates in column B of our table. Let's start off by copying these dates to all columns. Let's look first at the Short Date...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_create_a_custom_number_format-thumb_0.png)](https://exceljet.net/videos/how-to-create-a-custom-number-format-in-excel)

### [How to create a custom number format in Excel](https://exceljet.net/videos/how-to-create-a-custom-number-format-in-excel)

Excel allows you to create custom formats for dates, times, text, and numbers. In this lesson we'll create a simple custom format for positive and negative numbers based on an existing format. Let's take a look. The easiest way to create a custom format in Excel is to first apply a format that is...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract date from text string](https://exceljet.net/formulas/extract-date-from-text-string)
    
*   [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)
    
*   [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)
    
*   [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)
    
*   [Join cells with comma](https://exceljet.net/formulas/join-cells-with-comma)
    

### Functions

*   [TEXT Function](https://exceljet.net/functions/text-function)
    

### Videos

*   [How to use number formatting in Excel](https://exceljet.net/videos/how-to-use-number-formatting-in-excel)
    
*   [How to use date formatting in Excel](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)
    
*   [How to create a custom number format in Excel](https://exceljet.net/videos/how-to-create-a-custom-number-format-in-excel)
    

### Articles

*   [How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
    

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