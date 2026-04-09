# Convert text to date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-text-to-date

---

[Skip to main content](https://exceljet.net/formulas/convert-text-to-date#main-content)

[](https://exceljet.net/formulas/convert-text-to-date#)

*   [Previous](https://exceljet.net/formulas/convert-text-timestamp-into-time)
    
*   [Next](https://exceljet.net/formulas/convert-time-to-money)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert text to date
====================

by Dave Bruns · Updated 16 Apr 2024

Related functions 
------------------

[DATE](https://exceljet.net/functions/date-function)

[LEFT](https://exceljet.net/functions/left-function)

[MID](https://exceljet.net/functions/mid-function)

[RIGHT](https://exceljet.net/functions/right-function)

![Excel formula: Convert text to date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20text%20to%20date.png "Excel formula: Convert text to date")

Summary
-------

To convert text in an unrecognized date format to a proper Excel date, you can parse the text and assemble a proper date with a formula based on several functions: DATE, LEFT, MID, and RIGHT. In the example shown, the formula in C6 is:

    =DATE(LEFT(B6,4),MID(B6,5,2),RIGHT(B6,2))
    

This formula extract the year, month, and day values separately, and uses the DATE function to assemble them into the date October 24, 2000.

> Note: before you use a formula, see below for other ways to convert text to dates.

### Background

When you're working with data from another system, you might run into a situation where dates are not properly recognized by Excel, which instead treats the dates like text. For example, you might have text values like this:

|     |     |
| --- | --- |
| Text | Date represented |
| 20001024 | October 24, 2000 |
| 20050701 | July 1, 2005 |
| 19980424 | April 24, 1998 |
| 28.02.2014 | February 28, 2014 |

When Excel has evaluated a date value as text, one option is to use a formula to parse the text into its components (year, month, day) and use these to make a date with the DATE function. As noted above, I recommend you first try the solutions below (adding zero and using text to columns) before you use a formula. Both workarounds are faster and require less effort.

Generic formula
---------------

    =DATE(LEFT(text,4),MID(text,5,2),RIGHT(text,2))

Explanation 
------------

The [DATE function](https://exceljet.net/functions/date-function)
 creates a valid date using three arguments: year, month, and day:

    =DATE(year,month,day)
    

In cell C6, we use the LEFT, MID, and RIGHT functions to extract each of these components from a text string, and feed the results into the DATE function:

    =DATE(LEFT(B6,4),MID(B6,5,2),RIGHT(B6,2))
    

The [LEFT function](https://exceljet.net/functions/left-function)
 extracts the leftmost 4 characters for year, the [MID function](https://exceljet.net/functions/mid-function)
 extracts characters in positions 5-6 for month, and the [RIGHT function](https://exceljet.net/functions/right-function)
 extracts the rightmost 2 characters as day. Each result is returned directly to the DATE function. The final result is a proper Excel date that can be formatted any way you like.

This approach can be customized as needed. For example, the unrecognized date format in row 8 is dd.mm.yyyy and the formula in C8 is:

    =DATE(RIGHT(B8,4),MID(B8,4,2),LEFT(B8,2))
    

### Long form text

Sometimes you may have dates in a longer form like "Apr 11 2020 08:43:13" that Excel does not recognize properly. In this case, you may be able to adjust the string in a way that allows Excel to correctly recognize the date with the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
. The formula below replaces the second instance of a space (" ") with a comma and space (", "):

    =SUBSTITUTE(A2," ",", ",2)+0 // add comma after month
    

Once we add the comma after the month name, Excel will understand the date, but it still needs a little "kick". That's why we add zero at the end. The math operation causes Excel to try and convert the string to a number. When successful, this will result in a valid Excel date. Note you may need to apply date [number formatting](https://exceljet.net/articles/custom-number-formats)
 to display the date correctly.

### Without formulas

Before you use a formula to manually parse and construct a date from text, try one of the fixes below. The first option uses a math operation to "nudge" Excel a bit and force it to try and evaluate the text as a number. Because [Excel dates are in fact numbers](https://exceljet.net/glossary/excel-date)
, this can often do the trick. You may need to apply a date format if the operations succeeds.

### Add zero to fix dates

Sometimes, you'll encounter dates in a text format that Excel should recognize. In this case, you might be able to force Excel to convert the text values into dates by adding zero to the value. When you add zero, Excel will try to coerce text values to numbers. Since dates are just numbers, this trick is a great way to convert dates in text format that Excel really should understand.

To convert dates in place by adding zero, try [Paste Special](https://exceljet.net/videos/how-to-do-in-place-changes-with-paste-special)
:

1.  Enter zero (0) in an unused cell and copy to the clipboard
2.  Select the problematic dates
3.  Paste Special > Values > Add
4.  Apply a date format (if needed)

You can also add zero in a formula like this:

    =A1+0
    

where A1 contains an unrecognized date.

### Text to columns to fix dates

Another way to get Excel to recognize dates is to use the [Text to Columns](https://exceljet.net/glossary/text-to-columns)
 Feature:

Select the column of dates, then try Data > Text to columns > Fixed > Finish

If Excel recognizes the dates, it will fix them all in one step.

Related formulas
----------------

[![Excel formula: Convert date to text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20text.png "Excel formula: Convert date to text")](https://exceljet.net/formulas/convert-date-to-text)

### [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)

Dates and times in Excel are stored as serial numbers and converted to human-readable values on the fly using number formats. When you enter a date in Excel, you can apply a number format to display that date as you like. Similarly, the TEXT function allows you to convert a date or time into text...

[![Excel formula: Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20date%20ddmmyy%20to%20mmddyy.png "Excel formula: Convert text date dd/mm/yy to mm/dd/yy")](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)

### [Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)

The core of this formula is the DATE function, which is used to assemble a proper Excel date value. The DATE function requires valid year, month, and day values, so these are parsed out of the original text string as follows: 1. The year value is extracted with the RIGHT function: RIGHT(B5,2)+2000...

Related functions
-----------------

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)
    
*   [Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)
    

### Functions

*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    

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