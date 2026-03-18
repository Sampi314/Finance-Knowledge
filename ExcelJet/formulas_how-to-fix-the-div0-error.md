# How to fix the #DIV/0! error - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/how-to-fix-the-div0-error

---

[Skip to main content](https://exceljet.net/formulas/how-to-fix-the-div0-error#main-content)

[](https://exceljet.net/formulas/how-to-fix-the-div0-error#)

*   [Previous](https://exceljet.net/formulas/how-to-fix-the-calc-error)
    
*   [Next](https://exceljet.net/formulas/how-to-fix-the-na-error)
    

[Errors](https://exceljet.net/formulas#Errors)

How to fix the #DIV/0! error
============================

by Dave Bruns · Updated 19 Mar 2025

Related functions 
------------------

[IFERROR](https://exceljet.net/functions/iferror-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[ERROR.TYPE](https://exceljet.net/functions/errortype-function)

![Excel formula: How to fix the #DIV/0! error](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/how%20to%20fix%20the%20DIV%20error.png "Excel formula: How to fix the #DIV/0! error")

Summary
-------

The #DIV/0! error appears when a formula attempts to divide by zero or a value equivalent to zero.  Although a #DIV/0! error is caused by an attempt to divide by zero, it may also appear in other formulas that _reference_ cells that display the #DIV/0! error. In the example shown, if any cell in A1:A5 contains a #DIV/0! error, the SUM formula below will _also_ display #DIV/0!:

    =SUM(A1:A5)

Generic formula
---------------

    =IF(A2="","",A1/A2)

Explanation 
------------

### About the #DIV/0! error

The #DIV/0! error appears when a formula attempts to divide by zero, or a value equivalent to zero. Like other errors, the #DIV/0! is useful, because it tells you there is something missing or unexpected in a spreadsheet. You may see #DIV/0! errors when data is being entered, but is not yet complete. For example, a cell in the worksheet is blank because data is not yet available.

Although a #DIV/0! error is caused by an attempt to divide by zero, it may also appear in other formulas that _reference_ cells that display the #DIV/0! error. For example, if any cell in A1:A5 contains a #DIV/0! error, the SUM formula below will display #DIV/0!:

    =SUM(A1:A5)
    

The best way to prevent #DIV/0! errors is to make sure data is complete. If you see an unexpected #DIV/0! error, check the following:

1.  All cells used by a formula contain valid information
2.  There are no blank cells used to divide other values
3.  The cells referenced by a formula do not already display a #DIV/0! error

Note: if you try to divide a number by a text value, you will see a #VALUE error not #DIV/0!.

### #DIV/0! error and blank cells

Blank cells are a common cause of #DIV/0! errors. For example, in the screen below, we are calculating quantity per hour in column D with this formula, copied down:

    =B3/C3
    

![#DIV/0! error example - blank cell](https://exceljet.net/sites/default/files/images/formulas/inline/DIV%20error%20example%20-%20blank%20cell.png "#DIV/0! error example - blank cell")

Because C3 is blank, Excel evaluates the value of C3 as zero, and the formula returns #DIV/0!.

### #DIV/0! with average functions

Excel has three functions for calculating averages: [AVERAGE](https://exceljet.net/functions/average-function)
, [AVERAGEIF](https://exceljet.net/functions/averageif-function)
, and [AVERAGEIFS](https://exceljet.net/functions/averageifs-function)
. All three functions can return a #DIV/0! error when the count of "matching" values is zero. This is because the general formula for calculating averages is =sum/count, and count can sometimes be zero.

For example, if you try to average a range of cells containing only text values, the AVERAGE function will return #DIV/0! because the count of numeric values to average is zero:

![#DIV/0! error example with AVERAGE function](https://exceljet.net/sites/default/files/images/formulas/inline/DIV%20error%20example%20-%20average%20function.png "#DIV/0! error example with AVERAGE function")

Similarly, if you use the AVERAGEIF or AVERAGEIFS function with logical criteria that do not match any data, these functions will return #DIV/0! because the count of matching records is zero. For example, in the screen below, we are using the AVERAGEIFS function to calculate an average quantity for each color with this formula:

    =AVERAGEIFS(quantity,color,E3)
    

![#DIV/0! error example with AVERAGEIFS function](https://exceljet.net/sites/default/files/images/formulas/inline/DIV%20error%20example%20-%20averageifs.png "#DIV/0! error example with AVERAGEIFS function")

where "color" (B3:B8) and "quantity" (C3:C8) are [named ranges](https://exceljet.net/glossary/named-range)
.

Because there is no color "blue" in the data (i.e. the count of "blue" records is zero), AVERAGEIFS returns #DIV/0!.

This can be confusing when you are "certain" there are matching records. The best way to troubleshoot is to set up a small sample of _hand-entered data_ to validate the criteria you are using. If you are applying [multiple criteria with AVERAGEIFS](https://exceljet.net/formulas/average-with-multiple-criteria)
, work step by step and only add one criteria at a time.

Once you get the example working with criteria as expected, move to real data. [More information on formula criteria here](https://exceljet.net/articles/how-to-use-formula-criteria)
.

### Trapping the #DIV/0! error with IF

A simple way to trap the #DIV/0! is to check required values with the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the #DIV/0! error appears in cell D6 because cell C6 is blank:

    =B6/C6 // #DIV/0! because C6 is blank
    

To check that C6 has a value and abort the calculation if no value is available, you can use IF like this:

    =IF(C6="","",B6/C6) // display nothing if C6 is blank
    

You can extend this idea further and check that both B6 and C6 have values using the OR function:

    =IF(OR(B6="",C6=""),"",B6/C6)
    

See also: [IF cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)
.

### Trapping the #DIV/0! error with IFERROR

Another option for trapping the #DIV/0! error is the [IFERROR function](https://exceljet.net/functions/iferror-function)
. IFERROR will catch any error and return an alternative result. To trap the #DIV/0! error, wrap the IFERROR function around the formula in D6 like this:

    =IFERROR(B6/C6,"") // displays nothing when C6 is empty
    

### Add a message

If you want to display a message when you trap a #DIV/0! error, just wrap the message in quotes. For example, to display the message "Please enter hours", you can use:

    =IFERROR(B6/C6,"Please enter hours")
    

This message will be displayed instead of #DIV/0! while C6 remains blank.

Related formulas
----------------

[![Excel formula: How to fix the #N/A error ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20NA%20error.png "Excel formula: How to fix the #N/A error ")](https://exceljet.net/formulas/how-to-fix-the-na-error)

### [How to fix the #N/A error](https://exceljet.net/formulas/how-to-fix-the-na-error)

About the #N/A error The #N/A error appears when something can't be found or identified. It is often a useful error, because it tells you something important is missing – a product not yet available, an employee name misspelled, a color option that doesn't exist, etc. However, #N/A errors can also...

[![Excel formula: How to fix the #DIV/0! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20DIV%20error.png "Excel formula: How to fix the #DIV/0! error")](https://exceljet.net/formulas/how-to-fix-the-div0-error)

### [How to fix the #DIV/0! error](https://exceljet.net/formulas/how-to-fix-the-div0-error)

About the #DIV/0! error The #DIV/0! error appears when a formula attempts to divide by zero, or a value equivalent to zero. Like other errors, the #DIV/0! is useful, because it tells you there is something missing or unexpected in a spreadsheet. You may see #DIV/0! errors when data is being entered...

[![Excel formula: How to fix the #REF! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20REF%20error.png "Excel formula: How to fix the #REF! error")](https://exceljet.net/formulas/how-to-fix-the-ref-error)

### [How to fix the #REF! error](https://exceljet.net/formulas/how-to-fix-the-ref-error)

About the #REF! error The #REF! error occurs when a reference is invalid. In many cases, this is because sheets, rows, or columns have been removed, or because a formula with relative references has been copied to a new location where references are invalid. In the example shown, the formula in C10...

[![Excel formula: How to fix the #NAME? error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/How%20to%20fix%20the%20NAME%20error.png "Excel formula: How to fix the #NAME? error")](https://exceljet.net/formulas/how-to-fix-the-name-error)

### [How to fix the #NAME? error](https://exceljet.net/formulas/how-to-fix-the-name-error)

The #NAME? error occurs when Excel can't recognize something. Frequently, the #NAME? occurs when a function name is misspelled, but there are other causes, as explained below. Fixing a #NAME? error is usually just a matter of correcting spelling or a syntax problem. The examples below show...

[![Excel formula: How to fix the #VALUE! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/How%20to%20fix%20the%20VALUE%20error.png "Excel formula: How to fix the #VALUE! error")](https://exceljet.net/formulas/how-to-fix-the-value-error)

### [How to fix the #VALUE! error](https://exceljet.net/formulas/how-to-fix-the-value-error)

The #VALUE! error appears when a value is not the expected type. This can occur when cells are left blank, when a function expecting a number receives text value, or when dates are evaluated as text by Excel. Fixing a #VALUE! error is usually just a matter of entering the right kind of value. The #...

[![Excel formula: How to fix the #NUM! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/How%20to%20fix%20the%20NUM%20error.png "Excel formula: How to fix the #NUM! error")](https://exceljet.net/formulas/how-to-fix-the-num-error)

### [How to fix the #NUM! error](https://exceljet.net/formulas/how-to-fix-the-num-error)

The #NUM! error occurs in Excel formulas when a calculation can't be performed. For example, if you try to calculate the square root of a negative number, you'll see the #NUM! error. The examples below show formulas that return the #NUM error. In general, the fixing the #NUM! error is a matter of...

[![Excel formula: How to fix the #NULL! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/How%20to%20fix%20the%20NULL%20error.png "Excel formula: How to fix the #NULL! error")](https://exceljet.net/formulas/how-to-fix-the-null-error)

### [How to fix the #NULL! error](https://exceljet.net/formulas/how-to-fix-the-null-error)

The #NULL! error is quite rare in Excel, and is usually the result of a typo where a space character is used instead of a comma (,) or colon (:) between two cell references. Technically, the space character is the "range intersect" operator and the #NULL! error is reporting that the two ranges do...

[![Excel formula: How to fix the #### (hashtag) error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/How%20to%20fix%20the%20%23%23%23%20error.png "Excel formula: How to fix the #### (hashtag) error")](https://exceljet.net/formulas/how-to-fix-the-hashtag-error)

### [How to fix the #### (hashtag) error](https://exceljet.net/formulas/how-to-fix-the-hashtag-error)

The "hashtag" error, a string of hash or pound characters like ####### is not technically an error, but it looks like one. In most cases, it indicates the column width is too narrow to display the value as formatted. You might run into this odd looking result in several situations: You apply number...

[![Excel formula: How to fix the #SPILL! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20SPILL%20error.png "Excel formula: How to fix the #SPILL! error")](https://exceljet.net/formulas/how-to-fix-the-spill-error)

### [How to fix the #SPILL! error](https://exceljet.net/formulas/how-to-fix-the-spill-error)

About spilling and the #SPILL! error With the introduction of Dynamic Arrays in Excel , formulas that return multiple values " spill " these values directly onto the worksheet. The rectangle that encloses the values is called the " spill range ". When data changes, the spill range will expand or...

[![Excel formula: How to fix the #CALC! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20calc%20error.png "Excel formula: How to fix the #CALC! error")](https://exceljet.net/formulas/how-to-fix-the-calc-error)

### [How to fix the #CALC! error](https://exceljet.net/formulas/how-to-fix-the-calc-error)

With the introduction of Dynamic Arrays in Excel formulas , there is more emphasis on arrays . The #CALC! error occurs when a formula runs into a calculation error with an array. The #CALC! error is a "new" error in Excel, introduced with dynamic arrays. It will not appear in older versions of...

Related functions
-----------------

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

[![Excel ERROR.TYPE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20error.type%20function.png "Excel ERROR.TYPE function")](https://exceljet.net/functions/errortype-function)

### [ERROR.TYPE Function](https://exceljet.net/functions/errortype-function)

The Excel ERROR.TYPE function returns a number that corresponds to a specific error value. You can use ERROR.TYPE to test for specific kinds of errors. If no error exists, ERROR.TYPE returns #N/A. See below for a key to the error codes returned by ERROR.TYPE. ...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)

### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)

In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20trace%20a%20formula%20error-thumb.png)](https://exceljet.net/videos/how-to-trace-a-formula-error)

### [How to trace a formula error](https://exceljet.net/videos/how-to-trace-a-formula-error)

In this video we'll look at how to trace a formula error. Here we have a simple sales summary for a team of salespeople over a period of 4 months. You can see that we have monthly totals in the bottom row and totals for each salesperson in the last column. Below the table, we have a sales target...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [How to fix the #N/A error](https://exceljet.net/formulas/how-to-fix-the-na-error)
    
*   [How to fix the #DIV/0! error](https://exceljet.net/formulas/how-to-fix-the-div0-error)
    
*   [How to fix the #REF! error](https://exceljet.net/formulas/how-to-fix-the-ref-error)
    
*   [How to fix the #NAME? error](https://exceljet.net/formulas/how-to-fix-the-name-error)
    
*   [How to fix the #VALUE! error](https://exceljet.net/formulas/how-to-fix-the-value-error)
    
*   [How to fix the #NUM! error](https://exceljet.net/formulas/how-to-fix-the-num-error)
    
*   [How to fix the #NULL! error](https://exceljet.net/formulas/how-to-fix-the-null-error)
    
*   [How to fix the #### (hashtag) error](https://exceljet.net/formulas/how-to-fix-the-hashtag-error)
    
*   [How to fix the #SPILL! error](https://exceljet.net/formulas/how-to-fix-the-spill-error)
    
*   [How to fix the #CALC! error](https://exceljet.net/formulas/how-to-fix-the-calc-error)
    

### Functions

*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [ERROR.TYPE Function](https://exceljet.net/functions/errortype-function)
    

### Videos

*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    
*   [How to trace a formula error](https://exceljet.net/videos/how-to-trace-a-formula-error)
    

### Articles

*   [Excel Formula Errors](https://exceljet.net/articles/excel-formula-errors)
    
*   [Excel formulas and functions](https://exceljet.net/articles/excel-formulas-and-functions)
    
*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [29 ways to save time with Excel formulas](https://exceljet.net/articles/29-ways-to-save-time-with-excel-formulas)
    

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