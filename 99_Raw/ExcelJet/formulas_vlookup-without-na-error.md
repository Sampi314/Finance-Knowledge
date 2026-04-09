# VLOOKUP without #N/A error - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-without-na-error

---

[Skip to main content](https://exceljet.net/formulas/vlookup-without-na-error#main-content)

[](https://exceljet.net/formulas/vlookup-without-na-error#)

*   [Previous](https://exceljet.net/formulas/vlookup-with-variable-table-array)
    
*   [Next](https://exceljet.net/formulas/xlookup-approximate-match-with-multiple-criteria)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP without #N/A error
==========================

by Dave Bruns · Updated 2 May 2025

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

[IFNA](https://exceljet.net/functions/ifna-function)

[ISNA](https://exceljet.net/functions/isna-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7755/download?token=bJWcKeVA)
 (15.64 KB)

![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")

Summary
-------

To hide the #N/A error that [VLOOKUP](https://exceljet.net/functions/vlookup-function)
 returns when it can't find a lookup value, you can use the [IFNA function](https://exceljet.net/functions/ifna-function)
 to catch the error and return any value you like. In the example shown, the formula in cell F5 is:

    =IFNA(VLOOKUP(E5,data,2,FALSE),"Not found")

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:C55. The result is "Not Found" because "XX" does not exist in the Code column. When a valid 2-letter code is entered in cell E5, VLOOKUP will function normally. For example, if "GA" is entered in cell E5, VLOOKUP will return "Georgia":

Generic formula
---------------

    =IFNA(VLOOKUP(value,table,column,FALSE),"message")

Explanation 
------------

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used in the same way. Both options are explained below.

### VLOOKUP function

The VLOOKUP function performs a lookup operation on vertical data. The generic syntax for VLOOKUP looks like this:

    VLOOKUP(A1,table,column,FALSE)

Where _A1_ contains a value to lookup, _table_ is the data, _column_ is a number, and _FALSE_ specifies exact match, which is required in this example. In the workbook shown, we want to enter an abbreviation in cell E5 and get the correct State name in cell F5, where all data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data**. To do this, we can use VLOOKUP in a formula like this:

    VLOOKUP(E5,data,2,FALSE)

When a valid 2-letter code is entered in cell E5, VLOOKUP will return the corresponding State. For example, if "CA" is entered in cell E5, VLOOKUP will return "California":

    ​VLOOKUP("CA",data,2,FALSE) // returns "California"

If an invalid code is entered in cell E5, VLOOKUP will return an #N/A error:

    ​VLOOKUP("XX",data,2,FALSE) // returns #N/A

The screen below shows how this error looks on the worksheet:

![Untrapped #N/A error with VLOOKUP](https://exceljet.net/sites/default/files/images/formulas/inline/VLOOKUP_without_NA_untrapped_error.png "Untrapped #N/A error with VLOOKUP")

The #N/A error technically means "not available". However, you may want to return a more friendly result. You can do this by combining VLOOKUP with the IFNA function.

### VLOOKUP with IFNA

The [IFNA function](https://exceljet.net/functions/ifna-function)
 is a simple way to trap and handle #N/A errors without catching other errors. When used with a formula, the generic syntax looks like this:

    =IFNA(formula,alternative)

Here, the _formula_ might return a #N/A error; the _alternative_ is the value or formula to return in that case. To trap the #N/A error in this example, we wrap the IFNA function around the original VLOOKUP function and provide an alternate value. For example, to return "Not found" when VLOOKUP returns #N/A, we can use a formula like this:

    =IFNA(VLOOKUP(E5,data,2,FALSE),"Not found")

Now, when VLOOKUP returns the #N/A error, IFNA takes over and returns "Not found":

    =IFNA(VLOOKUP("XX",data,2,FALSE),"Not found") // returns "Not found"

To return a different message, just change the second [argument](https://exceljet.net/glossary/function-argument)
 in IFNA:

    =IFNA(VLOOKUP("XX",data,2,FALSE),"Invalid code") // returns "Invalid code"

If you would prefer to return nothing, you can provide an [empty string](https://exceljet.net/glossary/empty-string)
 ("") instead, like this:

    =IFNA(VLOOKUP("XX",data,2,FALSE),"") // returns ""

The result from this formula will look like an empty cell when the lookup Code is not found.

### VLOOKUP with IFERROR

You can also trap #N/A errors returned by VLOOKUP with the [IFERROR function](https://exceljet.net/functions/iferror-function)
 like this:

    =IFERROR(VLOOKUP(E5,data,2,FALSE),"Not found")

IFERROR works just like the IFNA function — it catches an #N/A error returned by VLOOKUP and returns an alternative result. The difference is that IFERROR will catch _other errors_ as well.

> The #N/A error is Excel's way of telling you a value was not found. With the more general IFERROR function, there is a risk that you might catch other unrelated errors and return a confusing result. For example, if you have a typo in a function name, Excel will return a #NAME! error. Or, if rows/columns are deleted in a worksheet, a formula may return a #REF! error. While IFNA will let these errors come through (so you see them), IFERROR will catch these errors, too, which can hide the underlying problem. For these reasons, I recommend you use the IFNA function when the purpose is to trap #N/A errors only.

### Older versions of Excel

In earlier versions of Excel that lack the IFNA function, you will need to repeat the VLOOKUP inside an IF function that catches an error with the [ISNA function](https://exceljet.net/functions/isna-function)
. For example:

    =IF(ISNA(VLOOKUP(A1,table,2,FALSE)),"Not found",VLOOKUP(A1,table,2,FALSE))
    

Related formulas
----------------

[![Excel formula: VLOOKUP with numbers and text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20numbers%20and%20text.png "Excel formula: VLOOKUP with numbers and text")](https://exceljet.net/formulas/vlookup-with-numbers-and-text)

### [VLOOKUP with numbers and text](https://exceljet.net/formulas/vlookup-with-numbers-and-text)

In this example, the goal is to configure VLOOKUP to perform a lookup in a table where the first column contains numbers entered as text, and the lookup value is a true number. This mismatch between numbers and text will cause VLOOKUP to return an #N/A error. Typically, the lookup column in the...

[![Excel formula: VLOOKUP if blank return blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20if%20blank%20return%20blank.png "Excel formula: VLOOKUP if blank return blank")](https://exceljet.net/formulas/vlookup-if-blank-return-blank)

### [VLOOKUP if blank return blank](https://exceljet.net/formulas/vlookup-if-blank-return-blank)

In this example, the goal is create a VLOOKUP formula that will return an empty cell when the lookup result is an empty cell. When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. You can use the IFNA function or IFERROR function to trap this error. However, when the result...

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: How to fix the #N/A error ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20NA%20error.png "Excel formula: How to fix the #N/A error ")](https://exceljet.net/formulas/how-to-fix-the-na-error)

### [How to fix the #N/A error](https://exceljet.net/formulas/how-to-fix-the-na-error)

About the #N/A error The #N/A error appears when something can't be found or identified. It is often a useful error, because it tells you something important is missing – a product not yet available, an employee name misspelled, a color option that doesn't exist, etc. However, #N/A errors can also...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

[![Excel IFNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ifna_function.png "Excel IFNA function")](https://exceljet.net/functions/ifna-function)

### [IFNA Function](https://exceljet.net/functions/ifna-function)

The Excel IFNA function is a simple way to handle #N/A errors specifically without catching other errors. The IFNA function allows you to specify a custom value or message to display instead of the #N/A error. If no error #N/A error occurs the formula returns a normal result....

[![Excel ISNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isna%20function.png "Excel ISNA function")](https://exceljet.net/functions/isna-function)

### [ISNA Function](https://exceljet.net/functions/isna-function)

The Excel ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)

### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)

In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP with numbers and text](https://exceljet.net/formulas/vlookup-with-numbers-and-text)
    
*   [VLOOKUP if blank return blank](https://exceljet.net/formulas/vlookup-if-blank-return-blank)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [How to fix the #N/A error](https://exceljet.net/formulas/how-to-fix-the-na-error)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    
*   [IFNA Function](https://exceljet.net/functions/ifna-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    

### Videos

*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    
*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    
*   [Excel Formula Errors](https://exceljet.net/articles/excel-formula-errors)
    

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