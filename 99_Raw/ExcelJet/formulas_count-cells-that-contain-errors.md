# Count cells that contain errors - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-contain-errors

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-contain-errors#main-content)

[](https://exceljet.net/formulas/count-cells-that-contain-errors#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-contain-n-characters)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that contain errors
===============================

by Dave Bruns · Updated 6 Dec 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[ISERR](https://exceljet.net/functions/iserr-function)

[ERROR.TYPE](https://exceljet.net/functions/errortype-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7376/download?token=Kdyl8P7J)
 (14.68 KB)

![Excel formula: Count cells that contain errors](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20contain%20errors.png "Excel formula: Count cells that contain errors")

Summary
-------

To count cells that contain errors, you can use the [ISERROR](https://exceljet.net/functions/iserror-function)
 [](https://exceljet.net/functions/iserr-function)
[function](https://exceljet.net/functions/iserror-function)
, wrapped in the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, cell E6 contains this formula:

    =SUMPRODUCT(--ISERROR(data))
    

Where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15.

Generic formula
---------------

    =SUMPRODUCT(--ISERROR(range))

Explanation 
------------

In this example, the goal is to count errors in the range B5:B15, which is [named](https://exceljet.net/glossary/named-range)
 **data** for convenience. The article below explains several different approaches, depending on your needs. For background, this article: [Excel Formula Errors](https://exceljet.net/articles/excel-formula-errors)
.

### COUNTIF function

One way to count individual errors is with the [COUNTIF function](https://exceljet.net/functions/countif-function)
 like this:

    =COUNTIF(data,"#N/A") // returns 1
    =COUNTIF(data,"#VALUE!") // returns 1
    =COUNTIF(data,"#DIV/0!") // returns 0
    

This is an odd syntax since technically errors are not [text values](https://exceljet.net/glossary/text-value)
. But COUNTIF is in a group of [eight functions that have some quirks](https://exceljet.net/articles/excels-racon-functions)
, and this is one of them. During calculation, COUNTIF is able to resolve the text into the given error and return a count of that error. One limitation of this approach is that there is no simple way to count [all error types](https://exceljet.net/articles/excel-formula-errors)
 with a single formula. You might think we can use COUNTIF like this:

    =COUNTIF(ISERROR(data),TRUE) // fails
    

The idea here is that the [ISERROR function](https://exceljet.net/functions/iserror-function)
 will return TRUE or FALSE, and COUNTIF will count the TRUE results. However, if you try to enter this formula, Excel won't let you. This is a case where COUNTIF won't work because it won't allow an "[array operation](https://exceljet.net/glossary/array-operation)
" in place of a normal range. One solution is to use SUMPRODUCT with ISERROR, as explained below.

### SUMPRODUCT function

A better way to count errors in a range is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 with the ISERROR function and [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. The SUMPRODUCT function accepts one or more arrays, multiplies the arrays together, and returns the "sum of products" as a final result. If only one array is supplied, SUMPRODUCT simply returns the sum of items in the array. In the example shown, the formula in E6 is:

    =SUMPRODUCT(--ISERROR(data))
    

Working from the inside out, the [ISERROR function](https://exceljet.net/functions/iserror-function)
 returns TRUE when a cell contains an error, and FALSE if not. Because there are eleven cells in the range B5:B15, ISERROR evaluates each cell and returns 11 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE}
    

Next, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to convert the TRUE and FALSE values to 1s and 0s. The resulting array inside the SUMPRODUCT function looks like this:

    =SUMPRODUCT({0;0;0;1;0;0;0;1;0;0;0})
    

Finally, SUMPRODUCT sums the items in this array and returns the total, which is 2 in this case.

### ISERR option

The ISERROR function counts _all_ errors. If for some reason you want to count all errors _except_ #N/A, you can use the [ISERR function](https://exceljet.net/functions/iserr-function)
 instead:

    =SUMPRODUCT(--ISERR(data)) // returns 1
    

Since one of the errors shown in the example is #N/A, this formula returns 1 instead of 2.

### Count by error code

Each Excel formula error is associated with a numeric error code ([complete list here](https://exceljet.net/articles/excel-formula-errors)
). You can retrieve this code with the [ERROR.TYPE function](https://exceljet.net/functions/errortype-function)
. To count errors by numeric code, you can use ERROR.TYPE instead of ISERROR. For example to count #VALUE! errors, which have a numeric code of 3, you can use a formula like this:

    =SUMPRODUCT(--(IFERROR(ERROR.TYPE(data),0)=3))
    

In an ironic twist, we need the [IFERROR function](https://exceljet.net/functions/iferror-function)
 to help us here. The ERROR.TYPE function will return a numeric code for any formula error. However, if a cell does not contain an error, ERROR.TYPE itself returns an #N/A error, which will bubble to the top and cause the entire formula to return #N/A. We use IFERROR to map the #N/A errors to zero so that we can compare the results from ERROR.TYPE to 3 without trouble. This part of the formula evaluates like this:

    =IFERROR(ERROR.TYPE(data),0)=3)
    =IFERROR({#N/A;#N/A;#N/A;3;#N/A;#N/A;#N/A;7;#N/A;#N/A;#N/A},0)=3)
    ={0;0;0;3;0;0;0;7;0;0;0}=3
    ={FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

Notice in the second step above, we see error code 3 and error code 7. This indicates the #VALUE! and #N/A error in **data** (B5:B15). After IFERROR runs, the #N/A errors are gone and replaced with zeros, as you can see in the third step. This lets us check for error code 3 without trouble. From there, we use a double negative to convert the TRUE and FALSE values to 1s and 0s and the resulting array is returned directly to SUMPRODUCT:

    =SUMPRODUCT({0;0;0;1;0;0;0;0;0;0;0}) // returns 1
    

The final result is 1, since there is one error in **data** with an error code of 3.

_Note: In Excel 365 and Excel 2021 you can use the [SUM function](https://exceljet.net/functions/sum-function)
 instead of SUMPRODUCT in all formulas above if_ _you prefer, with some caveats. [This article provides a complete](https://exceljet.net/articles/why-sumproduct)
 explanation._

Related formulas
----------------

[![Excel formula: Count cells that do not contain errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain%20errors.png "Excel formula: Count cells that do not contain errors")](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)

### [Count cells that do not contain errors](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)

In this example, the goal is to count the number of cells in a range that do not contain errors. The best way to solve this problem is to use the SUMPRODUCT function together with the ISERROR function. You can also use the COUNTIF function or COUNTIFS function to exclude specific errors. Both...

[![Excel formula: Average and ignore errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average%20and%20ignore%20errors2.png "Excel formula: Average and ignore errors")](https://exceljet.net/formulas/average-and-ignore-errors)

### [Average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)

In this example, the goal is to average a list of values that may contain errors. The values to average are in the named range data (B5:B15). Normally, you can use the AVERAGE function to calculate an average. However, if the data contains errors, AVERAGE will return an error. You can see this in...

[![Excel formula: Match first error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/match%20first%20error.png "Excel formula: Match first error")](https://exceljet.net/formulas/match-first-error)

### [Match first error](https://exceljet.net/formulas/match-first-error)

Working from the inside out, the ISERROR function returns TRUE when a value is a recognized error, and FALSE if not. When given a range of cells (an array of cells) ISERROR function will return an array of TRUE/FALSE results. In the example, this resulting array looks like this: {FALSE;FALSE;FALSE;...

[![Excel formula: How to fix the #N/A error ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20NA%20error.png "Excel formula: How to fix the #N/A error ")](https://exceljet.net/formulas/how-to-fix-the-na-error)

### [How to fix the #N/A error](https://exceljet.net/formulas/how-to-fix-the-na-error)

About the #N/A error The #N/A error appears when something can't be found or identified. It is often a useful error, because it tells you something important is missing – a product not yet available, an employee name misspelled, a color option that doesn't exist, etc. However, #N/A errors can also...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

[![Excel ISERR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserr%20function.png "Excel ISERR function")](https://exceljet.net/functions/iserr-function)

### [ISERR Function](https://exceljet.net/functions/iserr-function)

The Excel ISERR function returns TRUE for any error type except the #N/A error. You can use the ISERR function together with the IF function to test for an error and display a custom message, or perform a different calculation if found.

[![Excel ERROR.TYPE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20error.type%20function.png "Excel ERROR.TYPE function")](https://exceljet.net/functions/errortype-function)

### [ERROR.TYPE Function](https://exceljet.net/functions/errortype-function)

The Excel ERROR.TYPE function returns a number that corresponds to a specific error value. You can use ERROR.TYPE to test for specific kinds of errors. If no error exists, ERROR.TYPE returns #N/A. See below for a key to the error codes returned by ERROR.TYPE. ...

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

*   [Count cells that do not contain errors](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)
    
*   [Average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)
    
*   [Match first error](https://exceljet.net/formulas/match-first-error)
    
*   [How to fix the #N/A error](https://exceljet.net/formulas/how-to-fix-the-na-error)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [ISERR Function](https://exceljet.net/functions/iserr-function)
    
*   [ERROR.TYPE Function](https://exceljet.net/functions/errortype-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    

### Articles

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