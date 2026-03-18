# How to fix the #REF! error - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/how-to-fix-the-ref-error

---

[Skip to main content](https://exceljet.net/formulas/how-to-fix-the-ref-error#main-content)

[](https://exceljet.net/formulas/how-to-fix-the-ref-error#)

*   [Previous](https://exceljet.net/formulas/how-to-fix-the-num-error)
    
*   [Next](https://exceljet.net/formulas/how-to-fix-the-spill-error)
    

[Errors](https://exceljet.net/formulas#Errors)

How to fix the #REF! error
==========================

by Dave Bruns · Updated 5 May 2021

Related functions 
------------------

[ISREF](https://exceljet.net/functions/isref-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

![Excel formula: How to fix the #REF! error](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/how%20to%20fix%20the%20REF%20error.png "Excel formula: How to fix the #REF! error")

Summary
-------

The #REF! error occurs when a reference is invalid. In many cases, this is because sheets, rows, or columns have been removed, or because a formula with [relative references](https://exceljet.net/glossary/relative-reference)
 has been copied to a new location where references are invalid. Fixing a #REF error is a matter of editing a formula to use valid references again. See below for more examples and information.

Explanation 
------------

### About the #REF! error

The #REF! error occurs when a reference is invalid. In many cases, this is because sheets, rows, or columns have been removed, or because a formula with [relative references](https://exceljet.net/glossary/relative-reference)
 has been copied to a new location where references are invalid. In the example shown, the formula in C10 returns a #REF! error when copied to cell E5:

    =SUM(C5:C9) // original C10
    =SUM(#REF) // when copied to E5
    

### Preventing #REF errors

The best way to prevent #REF! errors is to prevent then from occurring in the first place.  Before you delete columns, rows, or sheets be sure they aren't referenced by formulas in the workbook. If you are copying and pasting a formula to a new location, you may want to convert some cell references to an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 to prevent changes during the copy operation.

If you cause a #REF! error, it's best to fix immediately. For example, if you delete a column, and #REF! errors appear, undo that action (you can use the shortcut Control + Z). When you undo, the #REF! errors will disappear. Then edit the formula(s) to exclude the column you want to delete, moving data if needed. Finally, delete the column and confirm there are no #REF! errors.

### Clearing multiple #REF! errors

To quickly remove many #REF errors from a worksheet, you can use Find and Replace. Use the [shortcut](https://exceljet.net/shortcuts)
 Control + H to open the Find and Replace dialog.  Enter #REF! in the find input area, and leave the replace input area blank:

![Clear REF errors with find and replace](https://exceljet.net/sites/default/files/images/formulas/inline/clear%20REF%20errors%20with%20find%20and%20place.png "Clear REF errors with find and replace")

You can then make case-by-case changes with Find next + Replace, or use Replace All to replace all #REF errors in one step.

### Fixing #REF errors

#REF errors are somewhat tricky to fix because the original cell reference is gone forever. If you know what the reference should be, you can simply fix it manually. Just edit the formula and replace #REF! with a valid reference. If you don't know what the cell reference should be, you may have to study the worksheet in more detail before you can repair the formula.

_Note: you can't undo the deletion of a sheet in Excel. If you delete a worksheet tab, and see #REF errors, your best option is probably to close the file and re-open the last saved version. For this reason, always save a workbook (or save a copy) before deleting one or more sheets._

### #REF! errors with VLOOKUP

You may see a #REF! error with the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
, when a column is specified incorrectly. In the screen below, VLOOKUP returns #REF! because there is no column 3 in the table range, which is B3:C7:

![Example of #REF! error with VLOOKUP](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/fix%20REF%20error%20with%20VLOOKUP.png?itok=remPfSBP "Example of #REF! error with VLOOKUP")

When the column index is set to the correct value of 2 the #REF! error is resolved and VLOOKUP works properly:

![Example of #REF! error resolved with VLOOKUP](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/fix%20REF%20error%20with%20VLOOKUP%20fixed.png?itok=MgC4YpMb "Example of #REF! error resolved with VLOOKUP")

Note: you may also see a #REF error with the [INDEX function](https://exceljet.net/functions/index-function)
 when a row or column reference is not valid.

### Trapping the #REF! error with IFERROR

In most cases, it doesn't make sense to trap the #REF! error in a formula, because #REF! indicates a low-level problem. However, one situation where IFERROR may make sense to catch a #REF error is when you are building references [dynamically with the INDIRECT function](https://exceljet.net/formulas/dynamic-worksheet-reference)
.

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

[![Excel ISREF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isref%20function.png "Excel ISREF function")](https://exceljet.net/functions/isref-function)

### [ISREF Function](https://exceljet.net/functions/isref-function)

The Excel ISREF returns TRUE when a cell contains a reference and FALSE if not. You can use the ISREF function to check for a reference in a formula.

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)

### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)

In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...

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

*   [ISREF Function](https://exceljet.net/functions/isref-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    

### Videos

*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    

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