# VLOOKUP if blank return blank - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-if-blank-return-blank

---

[Skip to main content](https://exceljet.net/formulas/vlookup-if-blank-return-blank#main-content)

[](https://exceljet.net/formulas/vlookup-if-blank-return-blank#)

*   [Previous](https://exceljet.net/formulas/vlookup-from-another-workbook)
    
*   [Next](https://exceljet.net/formulas/vlookup-override-output)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP if blank return blank
=============================

by Dave Bruns · Updated 10 Mar 2022

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: VLOOKUP if blank return blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP%20if%20blank%20return%20blank.png "Excel formula: VLOOKUP if blank return blank")

Summary
-------

To check for empty cells in VLOOKUP results, you can combine the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 with the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the formula in G5, copied down, is:

    =IF(VLOOKUP(E5,data,2,0)="","",VLOOKUP(E5,data,2,0))
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 B5:C11.

Generic formula
---------------

    =IF(VLOOKUP(A1,data,col,0)="","",VLOOKUP(A1,data,col,0))

Explanation 
------------

In this example, the goal is create a VLOOKUP formula that will return an empty cell when the lookup result is an empty cell.

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. You can use the [IFNA function](https://exceljet.net/functions/ifna-function)
 or [IFERROR function](https://exceljet.net/functions/iferror-function)
 to trap this error. However, when the _result in a lookup table is an empty cell_, no error is thrown, VLOOKUP simply returns a zero.

This can cause problems when the lookup table contains actual zero values, because it suggests that blank cells in the lookup table also contain zeros, when they in fact are empty. To work around this problem you can test the result of VLOOKUP explicitly with the [IF function](https://exceljet.net/functions/if-function)
, then return a custom result if you find an empty string.

### With IF function

To test the result of VLOOKUP directly, we use the IF function like this:

    =IF(VLOOKUP(E5,data,2,0)="",""
    

Translated: _if the result from VLOOKUP is an [empty string](https://exceljet.net/glossary/empty-string)
 (""), return an empty string._

If the result from VLOOKUP is not an empty string, run VLOOKUP again and return a normal result:

    VLOOKUP(E5,data,2,0)
    

In both cases, the fourth argument for VLOOKUP is set to zero to force an exact match.

_Note: you can use the [same general approach](https://exceljet.net/formulas/xlookup-return-blank-if-blank)
 with the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
._

### With LEN or ISNUMBER

Depending on your needs, you can expand the idea above to run more specific tests. For example, to test for cells that literally have zero characters (i.e. a length of zero), you can use the [LEN function](https://exceljet.net/functions/len-function)
 like this:

    =IF(LEN(VLOOKUP(E5,data,2,0))=0,"",VLOOKUP(E5,data,2,0))
    

To test for numeric results only, you can use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
, and reorder the logic like this:

    =IF(ISNUMBER(VLOOKUP(E5,data,2,0)),VLOOKUP(E5,data,2,0),"")
    

Translated: _if the result from VLOOKUP is a number, return a normal lookup. If not, return an empty string ("")._

Related formulas
----------------

[![Excel formula: VLOOKUP with numbers and text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20numbers%20and%20text.png "Excel formula: VLOOKUP with numbers and text")](https://exceljet.net/formulas/vlookup-with-numbers-and-text)

### [VLOOKUP with numbers and text](https://exceljet.net/formulas/vlookup-with-numbers-and-text)

In this example, the goal is to configure VLOOKUP to perform a lookup in a table where the first column contains numbers entered as text, and the lookup value is a true number. This mismatch between numbers and text will cause VLOOKUP to return an #N/A error. Typically, the lookup column in the...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

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
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    
*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    

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