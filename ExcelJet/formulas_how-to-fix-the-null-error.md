# How to fix the #NULL! error - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/how-to-fix-the-null-error

---

[Skip to main content](https://exceljet.net/formulas/how-to-fix-the-null-error#main-content)

[](https://exceljet.net/formulas/how-to-fix-the-null-error#)

*   [Previous](https://exceljet.net/formulas/how-to-fix-the-name-error)
    
*   [Next](https://exceljet.net/formulas/how-to-fix-the-num-error)
    

[Errors](https://exceljet.net/formulas#Errors)

How to fix the #NULL! error
===========================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[IFERROR](https://exceljet.net/functions/iferror-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[ERROR.TYPE](https://exceljet.net/functions/errortype-function)

![Excel formula: How to fix the #NULL! error](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/How%20to%20fix%20the%20NULL%20error.png "Excel formula: How to fix the #NULL! error")

Summary
-------

The #NULL! error is quite rare in Excel, and is usually the result of a typo where a space character is used instead of a comma (,) or colon (:) between two cell references. This error may seem baffling to the average user, but in most cases replacing the space with a comma or colon will fix the problem. See below for more information.

Explanation 
------------

The #NULL! error is quite rare in Excel, and is usually the result of a typo where a space character is used instead of a comma (,) or colon (:) between two cell references. Technically, the space character is the "range intersect" operator and the #NULL! error is reporting that the two ranges do not intersect. This is baffling to the average user but in most cases replacing the space with a comma or colon as needed will fix the problem.

### Example 1 - space instead of colon

In the screen below, the formula in C9 returns the #NULL error:

    =SUM(C3 C7) // returns #NULL!
    

![#NULL! error example - space instead of colon](https://exceljet.net/sites/default/files/images/formulas/inline/NULL%20error%20example%20space%20instead%20of%20colon.png "#NULL! error example - space instead of colon")

In this case, the input was meant to be the range C3:C7, but the colon did not get typed. Once the colon is added, the error is fixed:

    =SUM(C3:C7) // returns 1205
    

![#NULL! error example - space instead of colon FIXED](https://exceljet.net/sites/default/files/images/formulas/inline/NULL%20error%20example%20space%20instead%20of%20colon%20fixed.png "#NULL! error example - space instead of colon FIXED")

### Example 2 - space instead of comma

In the example below, the formula in C5 returns the #NULL error:

    =SUM(C2,F2 I2) // returns #NULL!
    

![#NULL! error example - space instead of comma](https://exceljet.net/sites/default/files/images/formulas/inline/NULL%20error%20example%20space%20instead%20of%20comma.png "#NULL! error example - space instead of comma")

Here, a space was typed instead of a comma between F2 and I2.  Once the colon is added, the error is fixed:

    =SUM(C2,F2,I2) // returns 1205
    

![#NULL! error example - space instead of comma FIXED](https://exceljet.net/sites/default/files/images/formulas/inline/NULL%20error%20example%20space%20instead%20of%20comma%20fixed.png "#NULL! error example - space instead of comma FIXED")

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