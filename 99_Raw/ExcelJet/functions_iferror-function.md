# Excel IFERROR function | Exceljet

**Source:** https://exceljet.net/functions/iferror-function

---

[Skip to main content](https://exceljet.net/functions/iferror-function#main-content)

[](https://exceljet.net/functions/iferror-function#)

*   [Previous](https://exceljet.net/functions/if-function)
    
*   [Next](https://exceljet.net/functions/ifna-function)
    

Excel 2007

[Logical](https://exceljet.net/functions#Logical)

IFERROR Function
================

by Dave Bruns · Updated 29 Jan 2024

Related functions 
------------------

[ISERROR](https://exceljet.net/functions/iserror-function)

[IFNA](https://exceljet.net/functions/ifna-function)

![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")

Summary
-------

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

Purpose 
--------

Trap and handle errors

Return value 
-------------

The value you specify for error conditions.

Syntax
------

    =IFERROR(value,value_if_error)

*   _value_ - The value, reference, or formula to check for an error.
*   _value\_if\_error_ - The value to return if an error is found.

Using the IFERROR function 
---------------------------

The IFERROR function returns a _custom result_ when a formula returns an error and a _normal result_ when a formula calculates without an error. The typical syntax for the IFERROR function looks like this:

    =IFERROR(formula,custom)

In the example above, "formula" represents a formula that might return an error, and "custom" represents the value that should be returned if the formula returns an error. This makes IFERROR an elegant way to trap and manage errors in one step. Before the introduction of IFERROR, it was necessary to use more complicated nested IF statements together with the older [ISERROR function](https://exceljet.net/functions/iserror-function)
.

You can use the IFERROR function to trap and handle [errors](https://exceljet.net/articles/excel-formula-errors)
 produced by other formulas or functions. IFERROR checks for the following errors: #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL!.

### Example 1 - Trap #DIV/0! errors

In the example shown, the formula in E5 copied down is:

    =IFERROR(C5/D5,0)
    

This formula catches the #DIV/0! error that occurs when the quantity field is empty or zero, and replaces it with zero. You are free to change the zero (0) to suit your needs. For example, to display nothing, you could use an [empty string](https://exceljet.net/glossary/empty-string)
 ("") instead of zero:

    =IFERROR(C5/D5,"")
    

This version of the formula will trap the #DIV/0! error and return an empty string, which looks like an blank cell.

### Example 2 - request input before calculating

Sometimes you may want to suppress a calculation until the worksheet receives specific input. For example, if A1 contains 10, B1 is blank, and C1 contains the formula =A1/B1, the following formula will return a #DIV/0 error if B1 is empty:

    =IFERROR(A1/B1) // returns #DIV! if B1 is empty
    

The formula below has been modified to use the IFERROR function to trap the #DIV/0! error and remap it to the message "Please enter a value in B1".

    =IFERROR(A1/B1,"Please enter a value in B1")
    

As long as B1 is empty, C1 will display the message "Please enter a value in B1" if B1. When a number is entered in B1, the formula will return the result of A1/B1.

### Example 3 - Sum and ignore errors

A common problem in Excel is that errors in data will corrupt the results of other formulas. For example, in the worksheet shown below, the goal is to sum values in the range D5:D15. However, because the range D5:D15 contains #N/A errors, the SUM function will return #N/A:

    =SUM(D5:D15) // returns #N/A

![Using IFERROR to sum and ignore errors](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sum_and_ignore_errors_with_IFERROR.png "Using IFERROR to sum and ignore errors")

To ignore the #N/A errors and sum the remaining values, we can adjust the formula to use the IFERROR function like this:

    =SUM(IFERROR(D5:D15,0)) // returns 152.50

Essentially, we use IFERROR to map the errors to zero and then sum the result. For more details and alternatives, see [Sum and ignore errors](https://exceljet.net/formulas/sum-and-ignore-errors)
.

### Example 3 - VLOOKUP #N/A

When VLOOKUP cannot find a lookup value, it returns an #N/A error.  You can use the IFERROR function to catch the #N/A error VLOOKUP throws when a lookup value isn't found like this:

    =IFERROR(VLOOKUP(value,data,column,0),"Not found")
    

In this example, the IFERROR function evaluates the result returned by VLOOKUP. If no error is present, the result is returned normally. However, if VLOOKUP returns an #N/A error, IFERROR catches the error and returns "Not Found". 

### IFERROR or IFNA?

The [IFERROR function](https://exceljet.net/functions/iferror-function)
 is useful, but it is a rather blunt instrument that will trap all kinds of errors. For example, if a function is misspelled in a formula, Excel will return the #NAME? error and IFERROR will catch that error too, and return an alternate result. This can cause IFERROR to hide an important problem. In most cases, it makes more sense to use the [IFNA function](https://exceljet.net/functions/ifna-function)
 with VLOOKUP instead of IFERROR.

    =IFNA(VLOOKUP(value,data,column,0),"Not found")
    

Unlike IFERROR, IFNA only traps the #N/A error.

### Other error functions

Excel provides several error-related functions, each with a different behavior:

*   The [ISERR function](https://exceljet.net/functions/iserr-function)
     returns TRUE for any error type except the #N/A error.
*   The [ISERROR function](https://exceljet.net/functions/iserror-function)
     returns TRUE for any error.
*   The [ISNA function](https://exceljet.net/functions/isna-function)
     returns TRUE for #N/A errors only.
*   The [ERROR.TYPE function](https://exceljet.net/functions/errortype-function)
     returns the numeric code for a given error.
*   The [IFERROR function](https://exceljet.net/functions/iferror-function)
     traps errors and provides an alternative result.
*   The [IFNA function](https://exceljet.net/functions/ifna-function)
     traps #N/A errors and provides an alternative result.

### Notes

*   If _value_ is empty, it is evaluated as an empty string ("") and not an error.
*   If _value\_if\_error_ is supplied as an empty string (""), no message is displayed when an error is detected.
*   In Excel 2013+, you can use the [IFNA function](https://exceljet.net/functions/ifna-function)
     to trap and handle #N/A errors specifically.

IFERROR function examples
-------------------------

[![Excel formula: Multiple matches into separate rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple_matches_into_separate_rows.png "Excel formula: Multiple matches into separate rows")](https://exceljet.net/formulas/multiple-matches-into-separate-rows)

### [Multiple matches into separate rows](https://exceljet.net/formulas/multiple-matches-into-separate-rows)

In this example, the goal is to get all names in a given group into separate rows grouped by column, as seen in the worksheet above. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns where each column holds the names that belong to a...

[![Excel formula: Show formula text with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/show%20formula%20text%20with%20formula.png "Excel formula: Show formula text with formula")](https://exceljet.net/formulas/show-formula-text-with-formula)

### [Show formula text with formula](https://exceljet.net/formulas/show-formula-text-with-formula)

The FORMULATEXT is fully automatic. When given the reference of a cell that contains a formula, it will return the entire formula as text. In the example as shown, the formula: =FORMULATEXT(C5) returns the text "=IF(B5>=70,"Pass","Fail")". Dealing with errors The FORMULATEXT function will return...

[![Excel formula: How to fix the #CALC! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20calc%20error.png "Excel formula: How to fix the #CALC! error")](https://exceljet.net/formulas/how-to-fix-the-calc-error)

### [How to fix the #CALC! error](https://exceljet.net/formulas/how-to-fix-the-calc-error)

With the introduction of Dynamic Arrays in Excel formulas , there is more emphasis on arrays . The #CALC! error occurs when a formula runs into a calculation error with an array. The #CALC! error is a "new" error in Excel, introduced with dynamic arrays. It will not appear in older versions of...

[![Excel formula: XLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_without_NA_error.png "Excel formula: XLOOKUP without #N/A error")](https://exceljet.net/formulas/xlookup-without-na-error)

### [XLOOKUP without #N/A error](https://exceljet.net/formulas/xlookup-without-na-error)

In this example, we have a simple worksheet that uses the XLOOKUP function to lookup the name of a U.S. state when a valid two-letter code is provided as a lookup value. The goal is to remove the #N/A error that XLOOKUP returns when it can't find a result. Although you could use the IFNA or IFERROR...

[![Excel formula: How to fix the #REF! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20REF%20error.png "Excel formula: How to fix the #REF! error")](https://exceljet.net/formulas/how-to-fix-the-ref-error)

### [How to fix the #REF! error](https://exceljet.net/formulas/how-to-fix-the-ref-error)

About the #REF! error The #REF! error occurs when a reference is invalid. In many cases, this is because sheets, rows, or columns have been removed, or because a formula with relative references has been copied to a new location where references are invalid. In the example shown, the formula in C10...

[![Excel formula: Multiple chained VLOOKUPs](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/chained%20lookups%20with%20VLOOKUP.png "Excel formula: Multiple chained VLOOKUPs")](https://exceljet.net/formulas/multiple-chained-vlookups)

### [Multiple chained VLOOKUPs](https://exceljet.net/formulas/multiple-chained-vlookups)

The IFERROR function is designed to trap errors and perform an alternate action when an error is detected. The VLOOKUP function will throw an #N/A error when a value isn't found. By nesting multiple VLOOKUPs inside the IFERROR function, the formula allows for sequential lookups. If the first...

[![Excel formula: VLOOKUP with numbers and text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20numbers%20and%20text.png "Excel formula: VLOOKUP with numbers and text")](https://exceljet.net/formulas/vlookup-with-numbers-and-text)

### [VLOOKUP with numbers and text](https://exceljet.net/formulas/vlookup-with-numbers-and-text)

In this example, the goal is to configure VLOOKUP to perform a lookup in a table where the first column contains numbers entered as text, and the lookup value is a true number. This mismatch between numbers and text will cause VLOOKUP to return an #N/A error. Typically, the lookup column in the...

[![Excel formula: How to fix the #SPILL! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20SPILL%20error.png "Excel formula: How to fix the #SPILL! error")](https://exceljet.net/formulas/how-to-fix-the-spill-error)

### [How to fix the #SPILL! error](https://exceljet.net/formulas/how-to-fix-the-spill-error)

About spilling and the #SPILL! error With the introduction of Dynamic Arrays in Excel , formulas that return multiple values " spill " these values directly onto the worksheet. The rectangle that encloses the values is called the " spill range ". When data changes, the spill range will expand or...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

[![Excel formula: Count cells that contain errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20errors.png "Excel formula: Count cells that contain errors")](https://exceljet.net/formulas/count-cells-that-contain-errors)

### [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)

In this example, the goal is to count errors in the range B5:B15, which is named data for convenience. The article below explains several different approaches, depending on your needs. For background, this article: Excel Formula Errors . COUNTIF function One way to count individual errors is with...

[![Excel formula: How to fix the #NUM! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/How%20to%20fix%20the%20NUM%20error.png "Excel formula: How to fix the #NUM! error")](https://exceljet.net/formulas/how-to-fix-the-num-error)

### [How to fix the #NUM! error](https://exceljet.net/formulas/how-to-fix-the-num-error)

The #NUM! error occurs in Excel formulas when a calculation can't be performed. For example, if you try to calculate the square root of a negative number, you'll see the #NUM! error. The examples below show formulas that return the #NUM error. In general, the fixing the #NUM! error is a matter of...

[![Excel formula: How to fix the #DIV/0! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20DIV%20error.png "Excel formula: How to fix the #DIV/0! error")](https://exceljet.net/formulas/how-to-fix-the-div0-error)

### [How to fix the #DIV/0! error](https://exceljet.net/formulas/how-to-fix-the-div0-error)

About the #DIV/0! error The #DIV/0! error appears when a formula attempts to divide by zero, or a value equivalent to zero. Like other errors, the #DIV/0! is useful, because it tells you there is something missing or unexpected in a spreadsheet. You may see #DIV/0! errors when data is being entered...

[![Excel formula: Get middle name from full name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_middle_name_from_name_0.png "Excel formula: Get middle name from full name")](https://exceljet.net/formulas/get-middle-name-from-full-name)

### [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)

In this example, the goal is to return the middle name from a full name in "First Middle Last" format. In the current version of Excel this is a fairly simple problem using the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, a similar formula is significantly more complicated, based...

[![Excel formula: How to fix the #VALUE! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/How%20to%20fix%20the%20VALUE%20error.png "Excel formula: How to fix the #VALUE! error")](https://exceljet.net/formulas/how-to-fix-the-value-error)

### [How to fix the #VALUE! error](https://exceljet.net/formulas/how-to-fix-the-value-error)

The #VALUE! error appears when a value is not the expected type. This can occur when cells are left blank, when a function expecting a number receives text value, or when dates are evaluated as text by Excel. Fixing a #VALUE! error is usually just a matter of entering the right kind of value. The #...

[![Excel formula: TEXTSPLIT get numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/TEXTSPLIT_get_numbers.png "Excel formula: TEXTSPLIT get numeric values")](https://exceljet.net/formulas/textsplit-get-numeric-values)

### [TEXTSPLIT get numeric values](https://exceljet.net/formulas/textsplit-get-numeric-values)

In this example, we have comma-separated text in column B. The goal is to split the text in column B into columns D through G while at the same time converting the numbers to true numeric values. The challenge is that TEXTSPLIT always returns text, so we need a way to convert the numbers while...

IFERROR function videos
-----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/TEXTSPLIT_with_numbers_Play.png)](https://exceljet.net/videos/textsplit-with-numbers)

### [TEXTSPLIT with numbers](https://exceljet.net/videos/textsplit-with-numbers)

In this video, we'll take a look at how to handle numbers with the TEXTSPLIT function. One result of using the TEXTSPLIT function is that all output is text, and this can cause problems if you need numeric values. Let me illustrate with an example. In this worksheet, we have some comma-separated...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20to%20do%20when%20VLOOKUP%20returns%20NA-thumb.png)](https://exceljet.net/videos/what-to-do-when-vlookup-returns-na)

### [What to do when VLOOKUP returns NA](https://exceljet.net/videos/what-to-do-when-vlookup-returns-na)

When you start using VLOOKUP , you'll often run into situations where VLOOKUP can't find a match and displays an error. In this video we'll look how to avoid and handle that situation. Here we have a VLOOKUP example we've looked at previously which uses VLOOKUP to retrieve employee information...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20trap%20errors%20in%20formulas-thumb.png)](https://exceljet.net/videos/how-to-trap-errors-in-formulas)

### [How to trap errors in formulas](https://exceljet.net/videos/how-to-trap-errors-in-formulas)

In this video, we'll look at a few ways to trap errors. Trapping errors can make your spreadsheets more professional by making them less cluttered and more friendly to use. In this first worksheet, we have a simple table that shows test scores for 5 sections. The total questions in each section are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Formulas%20to%20query%20a%20table-Thumb.png)](https://exceljet.net/videos/formulas-to-query-a-table)

### [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)

In this video, we'll look at some formulas you can use to query a table. Because tables support structured references, you can learn a lot about a table with basic formulas. On this sheet, Table1 contains employee data. Let's run through some examples. To start off, you can use the ROWS function to...

Related functions
-----------------

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

[![Excel IFNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ifna_function.png "Excel IFNA function")](https://exceljet.net/functions/ifna-function)

### [IFNA Function](https://exceljet.net/functions/ifna-function)

The Excel IFNA function is a simple way to handle #N/A errors specifically without catching other errors. The IFNA function allows you to specify a custom value or message to display instead of the #N/A error. If no error #N/A error occurs the formula returns a normal result....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)
    
*   [How to fix the #NUM! error](https://exceljet.net/formulas/how-to-fix-the-num-error)
    
*   [Average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)
    
*   [Multiple matches into separate rows](https://exceljet.net/formulas/multiple-matches-into-separate-rows)
    
*   [How to fix the #NAME? error](https://exceljet.net/formulas/how-to-fix-the-name-error)
    
*   [XLOOKUP without #N/A error](https://exceljet.net/formulas/xlookup-without-na-error)
    
*   [How to fix the #N/A error](https://exceljet.net/formulas/how-to-fix-the-na-error)
    
*   [Show formula text with formula](https://exceljet.net/formulas/show-formula-text-with-formula)
    
*   [TEXTSPLIT get numeric values](https://exceljet.net/formulas/textsplit-get-numeric-values)
    
*   [How to fix the #CALC! error](https://exceljet.net/formulas/how-to-fix-the-calc-error)
    

### Videos

*   [How to trap errors in formulas](https://exceljet.net/videos/how-to-trap-errors-in-formulas)
    
*   [What to do when VLOOKUP returns NA](https://exceljet.net/videos/what-to-do-when-vlookup-returns-na)
    
*   [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)
    
*   [TEXTSPLIT with numbers](https://exceljet.net/videos/textsplit-with-numbers)
    

### Functions

*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [IFNA Function](https://exceljet.net/functions/ifna-function)
    

### Links

*   [Microsoft IFERROR function documentation](https://support.office.com/en-us/article/iferror-function-c526fd07-caeb-47b8-8bb6-63f3e417f611)
    

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