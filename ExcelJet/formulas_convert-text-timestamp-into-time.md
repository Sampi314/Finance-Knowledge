# Convert text timestamp into time - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-text-timestamp-into-time

---

[Skip to main content](https://exceljet.net/formulas/convert-text-timestamp-into-time#main-content)

[](https://exceljet.net/formulas/convert-text-timestamp-into-time#)

*   [Previous](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)
    
*   [Next](https://exceljet.net/formulas/convert-text-to-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert text timestamp into time
================================

by Dave Bruns · Updated 6 Jan 2019

Related functions 
------------------

[TIME](https://exceljet.net/functions/time-function)

[MID](https://exceljet.net/functions/mid-function)

![Excel formula: Convert text timestamp into time](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Convert%20text%20timestamp%20into%20time.png "Excel formula: Convert text timestamp into time")

Summary
-------

Top convert a timestamp entered as text into a proper Excel time, you can use the MID function to extract components and the TIME function to assemble the time. In the example shown, the formula in F5 is:

    =TIME(MID(B5,1,2),MID(B5,4,2),MID(B5,7,2))
    

Generic formula
---------------

    =TIME(MID(A1,1,2),MID(A1,4,2),MID(A1,7,2))

Explanation 
------------

This formula works for times entered in a particular format as shown below:

    00h01m13s
    00h01m08s
    08h02m59s
    

Note the text string is always 9 characters long, and each component is 2 digits.

The core of this formula is the TIME function, which assembles a valid time using individual hour, minute, and second components. Since these values are all together in a single text string, the MID function is used to extract each component:

    MID(B5,1,2) // extract hour
    MID(B5,4,2) // extract minute
    MID(B5,7,2) // extract second
    

The results are fed directly to the TIME function as arguments. The code below shows how the formula is solved in cell F5:

    =TIME(MID(B5,1,2),MID(B5,4,2),MID(B5,7,2))
    =TIME("00","01","13")
    =12:01:13
    

Notice MID, as a text function, returns text instead of actual numbers. However, the TIME function still works properly, coercing the text values to numbers automatically.

Related formulas
----------------

[![Excel formula: Convert date to text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20text.png "Excel formula: Convert date to text")](https://exceljet.net/formulas/convert-date-to-text)

### [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)

Dates and times in Excel are stored as serial numbers and converted to human-readable values on the fly using number formats. When you enter a date in Excel, you can apply a number format to display that date as you like. Similarly, the TEXT function allows you to convert a date or time into text...

[![Excel formula: Convert text to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20to%20date.png "Excel formula: Convert text to date")](https://exceljet.net/formulas/convert-text-to-date)

### [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)

The DATE function creates a valid date using three arguments: year, month, and day: =DATE(year,month,day) In cell C6, we use the LEFT, MID, and RIGHT functions to extract each of these components from a text string, and feed the results into the DATE function: =DATE(LEFT(B6,4),MID(B6,5,2),RIGHT(B6,...

[![Excel formula: Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20date%20ddmmyy%20to%20mmddyy.png "Excel formula: Convert text date dd/mm/yy to mm/dd/yy")](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)

### [Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)

The core of this formula is the DATE function, which is used to assemble a proper Excel date value. The DATE function requires valid year, month, and day values, so these are parsed out of the original text string as follows: 1. The year value is extracted with the RIGHT function: RIGHT(B5,2)+2000...

Related functions
-----------------

[![Excel TIME function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_time.png "Excel TIME function")](https://exceljet.net/functions/time-function)

### [TIME Function](https://exceljet.net/functions/time-function)

The Excel TIME function is a built-in function that allows you to create a time with individual hour, minute, and second components. The TIME function is useful when you want to assemble a proper time inside another formula.

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

*   [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)
    
*   [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)
    
*   [Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)
    

### Functions

*   [TIME Function](https://exceljet.net/functions/time-function)
    
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