# How to fix the #N/A error  - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/how-to-fix-the-na-error

---

[Skip to main content](https://exceljet.net/formulas/how-to-fix-the-na-error#main-content)

[](https://exceljet.net/formulas/how-to-fix-the-na-error#)

*   [Previous](https://exceljet.net/formulas/how-to-fix-the-div0-error)
    
*   [Next](https://exceljet.net/formulas/how-to-fix-the-name-error)
    

[Errors](https://exceljet.net/formulas#Errors)

How to fix the #N/A error
=========================

by Dave Bruns · Updated 5 May 2021

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: How to fix the #N/A error ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/how%20to%20fix%20the%20NA%20error.png "Excel formula: How to fix the #N/A error ")

Summary
-------

The #N/A error usually appears when something can't be found or identified. However,  #N/A errors can also be caused by extra space characters, misspellings, or an incomplete lookup table. The functions mostly commonly affected by the #N/A error are classic lookup functions, including [VLOOKUP](https://exceljet.net/functions/vlookup-function)
, [HLOOKUP](https://exceljet.net/functions/hlookup-function)
, [LOOKUP](https://exceljet.net/functions/lookup-function)
, and [MATCH](https://exceljet.net/functions/match-function)
. See below for more information and steps to resolve.

Generic formula
---------------

    =IFERROR(FORMULA(),"message")

Explanation 
------------

### About the #N/A error

The #N/A error appears when something can't be found or identified. It is often a useful error, because it tells you something important is missing – a product not yet available, an employee name misspelled, a color option that doesn't exist, etc.

However,  #N/A errors can also be caused by extra space characters, misspellings, or an incomplete lookup table. The functions mostly commonly affected by the #N/A error are classic lookup functions, including [VLOOKUP](https://exceljet.net/functions/vlookup-function)
, [HLOOKUP](https://exceljet.net/functions/hlookup-function)
, [LOOKUP](https://exceljet.net/functions/lookup-function)
, and [MATCH](https://exceljet.net/functions/match-function)
.

The best way to prevent #N/A errors is to make sure lookup values and lookup tables are correct and complete. If you see an unexpected #N/A error, check the following first:

1.  The lookup value is spelled correctly and does not contain extra space characters.
2.  Values in the lookup table are spelled correctly and do not contain extra space.
3.  The lookup table is contains all required values.
4.  The lookup range provided to the function is complete (i.e. does not "clip" data).
5.  Lookup value type = lookup table type (i.e. both are text, both are numbers, etc.)
6.  Matching (approximate vs. exact) is set correctly.

Note: if you get an incorrect result, when you _should see a #N/A error_, make sure you have [exact matching configured correctly](https://exceljet.net/articles/danger-beware-vlookup-defaults)
. Approximate match mode will happily return all kinds of results that are totally incorrect :)

### Trapping the #N/A error with IFERROR

One option for trapping the #N/A error is the IFERROR function. IFERROR can gracefully catch any error and return an alternative result .

In the example shown, the #N/A error appears in cell F5 because "ice cream" does not exist in the lookup table, which is the named range "data" (B5:C9).

    =VLOOKUP(E5,data,2,0) // "ice cream" is not found
    

To handle this error, the [IFERROR function](https://exceljet.net/functions/iferror-function)
 is wrapped around the VLOOKUP formula like this:

    =IFERROR(VLOOKUP(E7,data,2,0),"Not found")
    

If the VLOOKUP function returns an error, the IFERROR function "catches" that error and returns "Not found".

### Trapping the #N/A error with IFNA

The [IFNA function](https://exceljet.net/functions/ifna-function)
 can also trap and handle #N/A errors specifically. The usage syntax is the same as with IFERROR:

    =IFERROR(VLOOKUP(A1,table,column,0),"Not found")
    =IFNA(VLOOKUP(A1,table,column,0),"Not found")
    

The advantage of the IFNA function is that it is more surgical, targeting just #N/A errors. The IFERROR function, on the other hand, will catch any error. For example, even if you spell VLOOKUP incorrectly, IFERROR will return "Not found".

### No message

If you don't want to display any message when you trap an #N/A error (i.e. you want to display a blank cell), you can use an [empty string](https://exceljet.net/glossary/empty-string)
 ("") like this:

    =IFERROR(VLOOKUP(E7,data,2,0),"")
    

### INDEX and MATCH

The MATCH function also returns #N/A when a value is not found. If you are using INDEX and MATCH together, you can trap the #N/A error in the same way. Based on the example above, the formula in F5 would be:

    =IFERROR(INDEX(C5:C9,MATCH(E5,B5:B9,0)),"Not found")
    

Read more about [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

### Forcing the #N/A error

If you want to force the #N/A error on a worksheet, you can use the [NA function](https://exceljet.net/functions/na-function)
. For example, display #N/A in a cell when A1 equals zero, you can use a formula like this:

    =IF(A1=0, NA())
    

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

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

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

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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