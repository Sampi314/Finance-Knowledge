# How to fix the #SPILL! error - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/how-to-fix-the-spill-error

---

[Skip to main content](https://exceljet.net/formulas/how-to-fix-the-spill-error#main-content)

[](https://exceljet.net/formulas/how-to-fix-the-spill-error#)

*   [Previous](https://exceljet.net/formulas/how-to-fix-the-ref-error)
    
*   [Next](https://exceljet.net/formulas/how-to-fix-the-value-error)
    

[Errors](https://exceljet.net/formulas#Errors)

How to fix the #SPILL! error
============================

by Dave Bruns · Updated 29 Nov 2021

Related functions 
------------------

[IFERROR](https://exceljet.net/functions/iferror-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[ERROR.TYPE](https://exceljet.net/functions/errortype-function)

![Excel formula: How to fix the #SPILL! error](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/how%20to%20fix%20the%20SPILL%20error.png "Excel formula: How to fix the #SPILL! error")

Summary
-------

Most often, a #SPILL! error occurs when a [spill range](https://exceljet.net/glossary/spill-range)
 is blocked by something on the worksheet, and the solution is to clear the spill range of any obstructing data. However, a #SPILL! error can have other causes as well. Read below for details.

Explanation 
------------

### About spilling and the #SPILL! error

With the introduction of [Dynamic Arrays in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, formulas that return multiple values "[spill](https://exceljet.net/glossary/spill)
" these values directly onto the worksheet. The rectangle that encloses the values is called the "[spill range](https://exceljet.net/glossary/spill-range)
".  When data changes, the spill range will expand or contract as needed. You might see new values added, or existing values disappear. 

Video: [Spilling and the spill range](https://exceljet.net/videos/spilling-and-the-spill-range)

### Spill behavior is native

It's important to understand that spill behavior is [_automatic and native_](https://exceljet.net/videos/dynamic-arrays-are-native)
. In [Dynamic Excel](https://exceljet.net/glossary/dynamic-excel)
 (Excel 365/2021) _any formula_, even a simple formula without functions, can spill results. Although there are ways to stop a formula from returning multiple results, spilling itself can't be disabled with a global setting. Similarly,  there is no option in Excel to "disable #SPILL errors. To fix a #SPILL error, you'll have to investigate and resolve the root cause of the problem.

### Spill error information

A #SPILL error often occurs when a spill range is blocked by something on the worksheet. Sometimes this is expected. For example, you have entered a formula, expecting it to spill, but existing data in the worksheet is in the way. The solution is just to clear the spill range of any obstructing data. Less often, a #SPILL error has another cause. You can click the spill error indicator to see more information about the cause of the error:

![SPILL error indicator provides more information](https://exceljet.net/sites/default/files/images/formulas/inline/spill%20error%20indicator%20shows%20more%20information.png "SPILL error indicator provides more information")

Read below for more information about #SPILL! errors and the specific fixes.

### 1\. Spill range blocked

This is the simplest case to resolve. The formula _should_ return multiple values, but instead it returns #SPILL! because there is already something in the spill range. In the screen below, the "x" is blocking the spill range:

![#SPILL error example 1 - before fix](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/SPILL%20error%20example%201%20-%20before.png?itok=IDx4KXxF "#SPILL error example 1 - before fix")

To fix the error, select any cell in the spill range so you can see its boundaries. Then make sure all cells in the spill range are empty.  Once the "x" is removed, the UNIQUE function spills results normally:

![#SPILL error example 1 - after fix](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/SPILL%20error%20example%201%20-%20after.png?itok=l2JBl4M7 "#SPILL error example 1 - after fix")

Cells in the spill range must be _empty_, so be alert to cells with invisible characters, like spaces.

### 2\. Excel Tables do not support dynamic arrays

Dynamic array formulas are not compatible with [Excel tables](https://exceljet.net/articles/excel-tables)
. If you try to add a dynamic array formula to an Excel Table, the formula will return a #SPILL! error in all rows. The solution in this case is to (1) use an alternative formula or (2) remove the Excel Table by converting it to a normal range with the Convert to Range button on the Table Design tab of the Ribbon: Table Design > Convert to Range

Video: [How to remove an Excel Table](https://exceljet.net/videos/how-to-remove-an-excel-table)
.

### 3\. Spill range is unknown

Some functions are [volatile](https://exceljet.net/glossary/volatile-function)
 and can't be used with dynamic array functions because the result would be "unknown" and dynamic formulas do not currently support arrays of unknown length. For example, the following formula will return a #SPILL! error:

    =SEQUENCE(RANDBETWEEN(1,100))
    

This happens because [RANDBETWEEN](https://exceljet.net/functions/randbetween-function)
 is volatile and the array returned by [SEQUENCE](https://exceljet.net/functions/sequence-function)
 would therefore have an unknown length. The only solution is to avoid dynamic array formulas that create arrays or ranges of an unknown length.

### 4\. Spill range too big

It is possible to write a formula that creates a spill range that extends off the edge of the worksheet. For example, the following formula uses the [full column reference](https://exceljet.net/glossary/full-column-reference)
 A:A:

    =A:A+1
    

If this formula is entered in any row except row 1, it will return a #SPILL! error with a "Spill range is too big" message. This happens because the resulting spill range includes 1,048,576 rows (the limit in Excel) and will run off the bottom of the worksheet. Similarly, the formula below tries to use SEQUENCE to create an array with 17,000 columns:

    =SEQUENCE(1,17000)
    

Because an Excel worksheet contains only 16,384 columns, this formula also returns a #SPILL! error. The solution is to avoid references and formulas that may create spill ranges that do not fit on the worksheet.

### 5\. Implicit intersection (@)

Before [Dynamic Arrays](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, Excel silently applied a behavior called "[implicit intersection](https://exceljet.net/glossary/implicit-intersection)
" to ensure that certain formulas with the potential to return multiple results only returned a single result. In non-dynamic array Excel, these formulas return a normal-looking result with no error. However, in certain cases the same formula entered in [Dynamic Excel](https://exceljet.net/glossary/dynamic-excel)
 may create a #SPILL error. For example, in the screen below, cell D5 contains this formula, copied down:

    =$B$5:$B$10+3
    

![#SPILL error example 2 - before fix](https://exceljet.net/sites/default/files/images/formulas/inline/SPILL%20error%20example%202%20-%20before.png "#SPILL error example 2 - before fix")

This formula would not throw an error in Excel 2016 because implicit intersection would prevent the formula from returning multiple results. However, in Dynamic Excel, the same formula _automatically_ returns multiple results that crash into each other, since the formula is copied down in D5:D10. One solution is to use the @ character to _enable_ implicit intersection like this:

    = @$B$5:$B$10+3
    

With this change, each formula returns a single result again and the #SPILL error disappears.

![#SPILL error example 2 - after fix](https://exceljet.net/sites/default/files/images/formulas/inline/SPILL%20error%20example%202%20-%20after.png "#SPILL error example 2 - after fix")

_Note: this also explains why you might suddenly see the "@" character appear in formulas created in older versions of Excel. This is done to maintain compatibility. Since formulas in older versions of Excel can't spill into multiple cells, the @ is added to ensure the same behavior when the formula is opened in a version of Excel that supports dynamic arrays._

A better way to fix the #SPILL error above is to use a native dynamic array formula in cell D5:

    =B5:B10+3
    

In Dynamic Excel, this _single formula_ will spill results into the range D5:D10, as seen in the screen below:

![#SPILL error example 3 - after fix](https://exceljet.net/sites/default/files/images/formulas/inline/SPILL%20error%20example%203%20-%20after.png "#SPILL error example 3 - after fix")

Note there is no need to use an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 since one formula creates all six results.

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

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Spilling%20and%20the%20spill%20range-Play.png)](https://exceljet.net/videos/spilling-and-the-spill-range)

### [Spilling and the spill range](https://exceljet.net/videos/spilling-and-the-spill-range)

In this video, we’ll look at a core idea in dynamic array behavior, the spill range . When a dynamic array formula outputs multiple values, it is said to “spill” these values onto the worksheet. For example, if I use the UNIQUE function on this list of colors, UNIQUE spills 3 values - red, blue,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Dynamic%20arrays%20are%20native-PLay.png)](https://exceljet.net/videos/dynamic-arrays-are-native)

### [Dynamic arrays are native](https://exceljet.net/videos/dynamic-arrays-are-native)

In this video we'll look at how dynamic array behavior is native and deeply integrated in Excel. Although new dynamic array functions will get a lot of attention, it's important to understand that dynamic array behavior is native and deeply integrated. All formulas will now run on a new calculation...

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
    
*   [How to fix the #CALC! error](https://exceljet.net/formulas/how-to-fix-the-calc-error)
    

### Functions

*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [ERROR.TYPE Function](https://exceljet.net/functions/errortype-function)
    

### Videos

*   [Spilling and the spill range](https://exceljet.net/videos/spilling-and-the-spill-range)
    
*   [Dynamic arrays are native](https://exceljet.net/videos/dynamic-arrays-are-native)
    

### Articles

*   [Excel Formula Errors](https://exceljet.net/articles/excel-formula-errors)
    
*   [Excel formulas and functions](https://exceljet.net/articles/excel-formulas-and-functions)
    
*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [29 ways to save time with Excel formulas](https://exceljet.net/articles/29-ways-to-save-time-with-excel-formulas)
    
*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    

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