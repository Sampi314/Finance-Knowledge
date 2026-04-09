# Excel NA function | Exceljet

**Source:** https://exceljet.net/functions/na-function

---

[Skip to main content](https://exceljet.net/functions/na-function#main-content)

[](https://exceljet.net/functions/na-function#)

*   [Previous](https://exceljet.net/functions/n-function)
    
*   [Next](https://exceljet.net/functions/sheet-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

NA Function
===========

by Dave Bruns · Updated 8 Sep 2021

Related functions 
------------------

[ISNA](https://exceljet.net/functions/isna-function)

[IFNA](https://exceljet.net/functions/ifna-function)

[ISERR](https://exceljet.net/functions/iserr-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

![Excel NA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20na%20function.png "Excel NA function")

Summary
-------

The Excel NA function returns the #N/A error. #N/A means "not available" or "no value available". You can use the NA function to display the #N/A error when information is missing.

Purpose 
--------

Create an #N/A error

Return value 
-------------

The #N/A error

Syntax
------

    =NA()

Using the NA function 
----------------------

The NA function returns the #N/A error. #N/A means "not available" or "no value available". You can use the NA function to display the #N/A error when information is missing. Note that if you use the NA function this way, other formulas that depend on cells that contain the #N/A error will also display #N/A, unless you specifically trap and manage the error. The NA function takes no arguments.

### Examples

The NA function returns the #N/A error:

    =NA() // returns #N/A
    

You can use the NA function in other formulas. For example, in the formula below, the IF function is configured to test if cell A1 is empty. If so, IF returns NA(), which returns the #N/A error. If A1 is not empty, IF returns A1\*B1: 

    =IF(A1="",NA(),A1*B1) // #N/A if A1 is empty
    

You can use the NA function to indicate missing information. In the worksheet shown above, cells C9 and C13 contain the NA function:

    =NA()
    

This indicates that cost is not available. In cell D5, the formula copied down is:

    =B5*C5 // qty * cost
    

In cells D9 and D13, the formula returns #N/A because C9 and C13 contain errors. In cell D15 the [SUMIF function](https://exceljet.net/functions/sumif-function)
 is used to sum values in column D while ignoring the #N/A error:

    =SUMIF(D5:D13,"<>#N/A") // ignore #N/A
    

If the [SUM function](https://exceljet.net/functions/sum-function)
 was used instead, it would return #N/A:

    =SUM(D5:D13) // would return #N/A
    

### Notes

*   When other formulas refer to cells that contain #N/A, they also return #N/A.
*   NA takes no arguments, but you must provide empty parentheses.
*   You can also enter the value #N/A directly into a cell as text.

NA function examples
--------------------

[![Excel formula: Get nth day of week in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get-nth-day-of-week-in-month_0.png "Excel formula: Get nth day of week in month")](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

### [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

This example demonstrates how to calculate the nth occurrence of a specific day of the week within a month. For instance, you might need to find the 2nd Tuesday, the 4th Wednesday, or the 1st Friday of any given month. The worksheet is structured with the starting date in column B, the target day...

[![Excel formula: VLOOKUP faster VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_faster_VLOOKUP.png "Excel formula: VLOOKUP faster VLOOKUP")](https://exceljet.net/formulas/vlookup-faster-vlookup)

### [VLOOKUP faster VLOOKUP](https://exceljet.net/formulas/vlookup-faster-vlookup)

In this example, VLOOKUP is configured to look up 1000 invoice numbers in a table that contains 1 million invoices. The catch is that not all of the 1000 invoice numbers exist in the source data. In fact, most of the invoice numbers do not appear in column B . This means we need to configure...

Related functions
-----------------

[![Excel ISNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isna%20function.png "Excel ISNA function")](https://exceljet.net/functions/isna-function)

### [ISNA Function](https://exceljet.net/functions/isna-function)

The Excel ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs.

[![Excel IFNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ifna_function.png "Excel IFNA function")](https://exceljet.net/functions/ifna-function)

### [IFNA Function](https://exceljet.net/functions/ifna-function)

The Excel IFNA function is a simple way to handle #N/A errors specifically without catching other errors. The IFNA function allows you to specify a custom value or message to display instead of the #N/A error. If no error #N/A error occurs the formula returns a normal result....

[![Excel ISERR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserr%20function.png "Excel ISERR function")](https://exceljet.net/functions/iserr-function)

### [ISERR Function](https://exceljet.net/functions/iserr-function)

The Excel ISERR function returns TRUE for any error type except the #N/A error. You can use the ISERR function together with the IF function to test for an error and display a custom message, or perform a different calculation if found.

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP faster VLOOKUP](https://exceljet.net/formulas/vlookup-faster-vlookup)
    
*   [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)
    

### Functions

*   [ISNA Function](https://exceljet.net/functions/isna-function)
    
*   [IFNA Function](https://exceljet.net/functions/ifna-function)
    
*   [ISERR Function](https://exceljet.net/functions/iserr-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    

### Links

*   [Microsoft NA function documentation](https://support.office.com/en-us/article/na-function-5469c2d1-a90c-4fb5-9bbc-64bd9bb6b47c)
    

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