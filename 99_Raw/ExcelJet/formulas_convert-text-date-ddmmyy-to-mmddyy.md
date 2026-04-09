# Convert text date dd/mm/yy to mm/dd/yy - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy

---

[Skip to main content](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy#main-content)

[](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy#)

*   [Previous](https://exceljet.net/formulas/convert-excel-time-to-unix-time)
    
*   [Next](https://exceljet.net/formulas/convert-text-timestamp-into-time)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert text date dd/mm/yy to mm/dd/yy
======================================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[DATE](https://exceljet.net/functions/date-function)

[LEFT](https://exceljet.net/functions/left-function)

[MID](https://exceljet.net/functions/mid-function)

[RIGHT](https://exceljet.net/functions/right-function)

[TRIM](https://exceljet.net/functions/trim-function)

![Excel formula: Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20text%20date%20ddmmyy%20to%20mmddyy.png "Excel formula: Convert text date dd/mm/yy to mm/dd/yy")

Summary
-------

To convert dates in text format dd/mm/yy to a true date in mm/dd/yy format, you can use uses a formula based on the DATE function. In the example shown, the formula in C5 is:

    =DATE(RIGHT(B5,2)+2000,MID(B5,4,2),LEFT(B5,2))
    

Which converts the text value in B5 "29/02/16" into a proper Excel date.

Generic formula
---------------

    =DATE(RIGHT(A1,2)+2000,MID(A1,4,2),LEFT(A1,2))

Explanation 
------------

The core of this formula is the DATE function, which is used to assemble a proper Excel date value. The DATE function requires valid year, month, and day values, so these are parsed out of the original text string as follows:

1\. The year value is extracted with the RIGHT function:

    RIGHT(B5,2)+2000
    

RIGHT gets the right-most 2 characters from the original value. The number 2000 is added to the result to create a valid year. This number goes into DATE as the year argument.

2\. The month value is extracted with:

    MID(B5,4,2)
    

MID retrieves characters 4-5. The result goes into DATE as the month argument.

3\. The day value is extracted with:

    LEFT(B5,2)
    

LEFT grabs the final 2 characters of the original text value, which goes into DATE as the day argument.

4\. The three values extracted above go into DATE like this:

    =DATE(2016,"02","29")
    

Although month and day are supplied as text, the DATE function automatically converts to numbers and returns a valid date.

_Note: the year value 2016 was automatically converted to a number when 2000 was added._

### Dealing with extra space

If the original text value contains extra leading or trailing space characters, you can add the TRIM function to remove:

    =DATE(RIGHT(TRIM(A1),2)+2000,MID(TRIM(A1),4,2),LEFT(TRIM(A1),2))
    

Related formulas
----------------

[![Excel formula: Convert date to text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20text.png "Excel formula: Convert date to text")](https://exceljet.net/formulas/convert-date-to-text)

### [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)

Dates and times in Excel are stored as serial numbers and converted to human-readable values on the fly using number formats. When you enter a date in Excel, you can apply a number format to display that date as you like. Similarly, the TEXT function allows you to convert a date or time into text...

[![Excel formula: Convert text to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20to%20date.png "Excel formula: Convert text to date")](https://exceljet.net/formulas/convert-text-to-date)

### [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)

The DATE function creates a valid date using three arguments: year, month, and day: =DATE(year,month,day) In cell C6, we use the LEFT, MID, and RIGHT functions to extract each of these components from a text string, and feed the results into the DATE function: =DATE(LEFT(B6,4),MID(B6,5,2),RIGHT(B6,...

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

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

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
    

### Functions

*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [TRIM Function](https://exceljet.net/functions/trim-function)
    

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