# XLOOKUP without #N/A error - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-without-na-error

---

[Skip to main content](https://exceljet.net/formulas/xlookup-without-na-error#main-content)

[](https://exceljet.net/formulas/xlookup-without-na-error#)

*   [Previous](https://exceljet.net/formulas/xlookup-with-regex-match)
    
*   [Next](https://exceljet.net/formulas/xmatch-reverse-search)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP without #N/A error
==========================

by Dave Bruns · Updated 16 Mar 2023

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

[IFNA](https://exceljet.net/functions/ifna-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7754/download?token=cOxobA50)
 (15.62 KB)

![Excel formula: XLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP_without_NA_error.png "Excel formula: XLOOKUP without #N/A error")

Summary
-------

To hide the #N/A error that the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 returns when it can't find a result, you can add a value for the _not\_found_ argument. In the example shown, the formula in cell F5 is:

    =XLOOKUP(E5,data[Code],data[State],"Not found")

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:C55. The result is "Not Found" because "XX" does not exist in the Code column.

Generic formula
---------------

    =XLOOKUP(A1,range1,range2,"Not found")

Explanation 
------------

In this example, we have a simple worksheet that uses the XLOOKUP function to lookup the name of a U.S. state when a valid two-letter code is provided as a lookup value. The goal is to remove the #N/A error that XLOOKUP returns when it can't find a result. Although you could use the IFNA or IFERROR function to trap the error and provide an alternative result, the easiest solution is to add a value for the _not\_found_ [argument](https://exceljet.net/glossary/function-argument)
, as explained below.

### XLOOKUP function

XLOOKUP is a modern replacement for the VLOOKUP function. It is a flexible and versatile function that can be used in a wide variety of situations. In this case, we want to lookup an abbreviation entered in cell E5 and return the correct State name in cell F5, where all data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data**. We can do this with a formula like this:

    XLOOKUP(E5,data[Code],data[State])

Note the _lookup\_array_ and _return\_array_ are both entered as [structured references](https://exceljet.net/videos/introduction-to-structured-references)
, which is the name Excel uses for references that refer to parts of an Excel Table. By default, XLOOKUP performs an _exact match_, so when a valid 2-letter code is entered in cell E5, XLOOKUP will return the corresponding State. For example, if "CO" is entered in cell E5, XLOOKUP will return "Colorado":

    XLOOKUP("CO",data[Code],data[State]) // returns "Colorado"

If an invalid code is entered in cell E5, XLOOKUP will return an #N/A error:

    XLOOKUP("XX",data[Code],data[State]) // returns #N/A

_By the way, this is a good example of how XLOOKUP can easily solve problems that are difficult with VLOOKUP. Because the lookup Code is to the right of State, VLOOKUP can't be used without a more advanced approach. [See this example for details](https://exceljet.net/formulas/left-lookup-with-vlookup)
._

To extend this formula to provide a custom result when a value is not found, all we need to do is add a value for the _not\_found_ argument. In this case, we want to return "Not found", so that is the value we use:

    =XLOOKUP(E5,data[Code],data[State],"Not found")

Notice we need to enclose "Not found" in double quotes because it is a [text value](https://exceljet.net/glossary/text-value)
. To return nothing when XLOOKUP can't find a value, you can provide an [empty string](https://exceljet.net/glossary/empty-string)
 ("") like this:

    =XLOOKUP(E5,data[Code],data[State],"")

The result from this formula will look like a blank cell when the lookup Code is not found.

### XLOOKUP with another formula

The example above displays a custom text message when XLOOKUP returns the #N/A error. However, the alternative value is not limited to text. For example, to have XLOOKUP return zero instead of #N/A, you can use a generic formula like this

    =XLOOKUP(A1,range1,range2,0)

In fact, you can provide another formula as well:

    =XLOOKUP(A1,range1,range2,formula)

This can be any normal Excel formula, even another XLOOKUP formula that refers to a different set of data. For example, if the first XLOOKUP fails, the second XLOOKUP can try the same lookup in a different table. In this way, you can chain together multiple XLOOKUP formulas.

### XLOOKUP with IFNA

XLOOKUP will work fine with other error-trapping formulas like the IFNA function:

    =IFNA(XLOOKUP(),alternative)

The [IFNA function](https://exceljet.net/functions/ifna-function)
 is a simple way to trap and handle #N/A errors specifically without catching other errors. In the worksheet shown above, you could use IFNA with XLOOKUP like this:

    =IFNA(XLOOKUP(E5,data[Code],data[State]),"Not found")

Notice the "Not found" result is now moved out of XLOOKUP into the IFNA function. I can't think of a good reason why you would need to use XLOOKUP with the IFNA function, but it should work just fine. The formula above is not wrong, it is just more complex than necessary.

### XLOOKUP with IFERROR

You can also trap #N/A errors returned by XLOOKUP with the [IFERROR function](https://exceljet.net/functions/iferror-function)
 like this:

    =IFERROR(XLOOKUP(E5,data[Code],data[State]),"Not found")

The IFERROR function is a more general function that will catch _any error_. This is a different formula from the IFNA formula above, and different from providing a value for the _not\_found_ argument. This formula will trap _any error_ returned by XLOOKUP, including  #REF!, #NAME, etc. This means there is a risk you might accidentally hide another legitimate error and return a message that is not actually correct. Unless you have a good reason to want this result, I would avoid XLOOKUP with IFERROR.

Related formulas
----------------

[![Excel formula: XLOOKUP basic exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20basic%20exact%20match_0.png "Excel formula: XLOOKUP basic exact match")](https://exceljet.net/formulas/xlookup-basic-exact-match)

### [XLOOKUP basic exact match](https://exceljet.net/formulas/xlookup-basic-exact-match)

In the example shown, cell G4 contains the lookup value, "Berlin". XLOOKUP is configured to find this value in the table, and return the population. The formula in G5 is: =XLOOKUP(G4,B5:B18,D5:D18) // get population The lookup\_value comes from cell G4 The lookup\_array is the range B5:B18, which...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

[![Excel formula: How to fix the #N/A error ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20NA%20error.png "Excel formula: How to fix the #N/A error ")](https://exceljet.net/formulas/how-to-fix-the-na-error)

### [How to fix the #N/A error](https://exceljet.net/formulas/how-to-fix-the-na-error)

About the #N/A error The #N/A error appears when something can't be found or identified. It is often a useful error, because it tells you something important is missing – a product not yet available, an employee name misspelled, a color option that doesn't exist, etc. However, #N/A errors can also...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

[![Excel IFNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ifna_function.png "Excel IFNA function")](https://exceljet.net/functions/ifna-function)

### [IFNA Function](https://exceljet.net/functions/ifna-function)

The Excel IFNA function is a simple way to handle #N/A errors specifically without catching other errors. The IFNA function allows you to specify a custom value or message to display instead of the #N/A error. If no error #N/A error occurs the formula returns a normal result....

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

*   [XLOOKUP basic exact match](https://exceljet.net/formulas/xlookup-basic-exact-match)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    
*   [How to fix the #N/A error](https://exceljet.net/formulas/how-to-fix-the-na-error)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    
*   [IFNA Function](https://exceljet.net/functions/ifna-function)
    

### Videos

*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    
*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    
*   [Excel Formula Errors](https://exceljet.net/articles/excel-formula-errors)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
*   [Excel Tables](https://exceljet.net/training/excel-tables)
    

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