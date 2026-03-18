# Convert date to Julian format - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-date-to-julian-format

---

[Skip to main content](https://exceljet.net/formulas/convert-date-to-julian-format#main-content)

[](https://exceljet.net/formulas/convert-date-to-julian-format#)

*   [Previous](https://exceljet.net/formulas/convert-date-string-to-date-time)
    
*   [Next](https://exceljet.net/formulas/convert-date-to-month-and-year)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert date to Julian format
=============================

by Dave Bruns · Updated 9 Aug 2016

Related functions 
------------------

[DATE](https://exceljet.net/functions/date-function)

[YEAR](https://exceljet.net/functions/year-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Convert date to Julian format](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20date%20to%20Julian%20format.png "Excel formula: Convert date to Julian format")

Summary
-------

If you need to convert a date to a Julian date format in Excel, you can do so by building a formula that uses the TEXT, YEAR, and DATE functions.

### Background

"Julian date format" refers to a format where the year value of a date is combined with the "ordinal day for that year" (i.e. 14th day, 100th day, etc.) to form a date stamp.

There are several variations. A date in this format may include a 4-digit year (yyyy) or a two-digit year (yy) and the day number may or may not be padded with zeros to always use 3 digits. For example, for the date January 21, 2017, you might see:

    1721 // YYD
    201721 //YYYYD
    2017021 // YYYYDDD
    

### Solution

For a two-digit year + a day number without padding use:

    =TEXT(B5,"yy")&B5-DATE(YEAR(B5),1,0)
    

For a two-digit year + a day number padded with zeros to 3 places:

    =TEXT(B5,"yy")&TEXT(B5-DATE(YEAR(B5),1,0),"000")
    

For a four-digit year + a day number padded with zeros to 3 places:

    =YEAR(B5)&TEXT(B5-DATE(YEAR(B5),1,0),"000")
    

Generic formula
---------------

    =YEAR(date)&TEXT(date-DATE(YEAR(date),1,0),"000")

Explanation 
------------

This formula builds the final result in 2 parts, joined by concatenation with the ampersand (&) operator.

On the left of the ampersand, we generate the year value. To extract a 2-digit year, we can use the TEXT function, which can apply a number format inside a formula:

    TEXT(B5,"yy")
    

To extract a full year, use the YEAR function:

    YEAR(B5)
    

On the right side of the ampersand we need to figure out the day of year. We do this by subtracting the last day of the previous year from the date we are working with. Because dates are just serial numbers, this will give us the "nth" day of year.

To get the last day of year of the previous year, we use the DATE function. When you give DATE a year and month value, and a zero for day, you get the last day of the previous month. So:

    B5-DATE(YEAR(B5),1,0)
    

gives us the last day of the previous year, which is December 31, 2015 in the example.

Now we need to pad the day value with zeros. Again, we can use the TEXT function:

    TEXT(B5-DATE(YEAR(B5),1,0),"000")
    

### Reverse Julian date

If you need to convert a Julian date back to a regular date, you can use a formula that parses Julian date and runs it through the date function with a month of 1 and day equal to the "nth" day. For example, this would create a date from a yyyyddd Julian date like 1999143.

    =DATE(LEFT(A1,4),1,RIGHT(A1,3)) // for yyyyddd
    

If you just have a day number (e.g. 100, 153, etc.), you can hard-code the year and insert the day this:

    =DATE(2016,1,A1)
    

Where A1 contains the day number. This works because the DATE function knows how to adjust for values that are out of range.

Related formulas
----------------

[![Excel formula: Convert date to text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20text.png "Excel formula: Convert date to text")](https://exceljet.net/formulas/convert-date-to-text)

### [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)

Dates and times in Excel are stored as serial numbers and converted to human-readable values on the fly using number formats. When you enter a date in Excel, you can apply a number format to display that date as you like. Similarly, the TEXT function allows you to convert a date or time into text...

[![Excel formula: Convert date to month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20month%20and%20year.png "Excel formula: Convert date to month and year")](https://exceljet.net/formulas/convert-date-to-month-and-year)

### [Convert date to month and year](https://exceljet.net/formulas/convert-date-to-month-and-year)

The TEXT function applies the number format you specify to a numeric value, and returns a result as text. In this case, the number format provided is "yyyymm", which joins a 4-digit year with a 2-digit month value. Display only option If you only want to display a date with the year and month, you...

[![Excel formula: Get nth day of year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20nth%20day%20of%20year.png "Excel formula: Get nth day of year")](https://exceljet.net/formulas/get-nth-day-of-year)

### [Get nth day of year](https://exceljet.net/formulas/get-nth-day-of-year)

This formula takes advantage of the fact that dates are just sequential numbers in Excel. It determines the last day of the previous year and subtracts that value from the original date with this formula: =B5-DATE(YEAR(B5),1,0) The result is nth day of the year, based on the date in cell B5. Notice...

[![Excel formula: Get date from day number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20date%20from%20day%20number.png "Excel formula: Get date from day number")](https://exceljet.net/formulas/get-date-from-day-number)

### [Get date from day number](https://exceljet.net/formulas/get-date-from-day-number)

The DATE function builds dates from separate year, month, and day values. One of its tricks is the ability to roll forward to correct dates when given days and months that are "out of range". For example, DATE returns April 9, 2016, with the following arguments: =DATE(2016,1,100) There is no 100th...

Related functions
-----------------

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

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
    
*   [Convert date to month and year](https://exceljet.net/formulas/convert-date-to-month-and-year)
    
*   [Get nth day of year](https://exceljet.net/formulas/get-nth-day-of-year)
    
*   [Get date from day number](https://exceljet.net/formulas/get-date-from-day-number)
    

### Functions

*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

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