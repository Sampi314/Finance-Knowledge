# Excel ISNA function | Exceljet

**Source:** https://exceljet.net/functions/isna-function

---

[Skip to main content](https://exceljet.net/functions/isna-function#main-content)

[](https://exceljet.net/functions/isna-function#)

*   [Previous](https://exceljet.net/functions/islogical-function)
    
*   [Next](https://exceljet.net/functions/isnontext-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

ISNA Function
=============

by Dave Bruns · Updated 7 Sep 2021

Related functions 
------------------

[ISERROR](https://exceljet.net/functions/iserror-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

[ISERR](https://exceljet.net/functions/iserr-function)

[ISEVEN](https://exceljet.net/functions/iseven-function)

[ISFORMULA](https://exceljet.net/functions/isformula-function)

[ISLOGICAL](https://exceljet.net/functions/islogical-function)

[ISNONTEXT](https://exceljet.net/functions/isnontext-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[ISODD](https://exceljet.net/functions/isodd-function)

[ISREF](https://exceljet.net/functions/isref-function)

[ISTEXT](https://exceljet.net/functions/istext-function)

![Excel ISNA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20isna%20function.png "Excel ISNA function")

Summary
-------

The Excel ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs.

Purpose 
--------

Test for the #N/A error

Return value 
-------------

A logical value (TRUE or FALSE)

Syntax
------

    =ISNA(value)

*   _value_ - The value to check if #N/A.

Using the ISNA function 
------------------------

The ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. The ISNA function takes one argument, _value_, which is typically a cell reference.

### Examples

If A1 contains the #N/A error, ISNA returns TRUE:

    =ISNA(A1) // returns TRUE
    

ISNA returns FALSE for other values and errors:

    =ISNA(100) // returns FALSE
    =ISNA(5/0) // returns FALSE
    

You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs. For example, to display a message if A1 contains #N/A and the value of A1 if not:

    =IF(ISNA(A1),"message",A1)
    

The [IFNA function](https://exceljet.net/functions/ifna-function)
 is a more efficient way to trap the #N/A error. See [VLOOKUP without NA error](https://exceljet.net/formulas/vlookup-without-na-error)
 for an example.

### Return #N/A

To explicitly return the #N/A error in a formula, you can use the [NA function](https://exceljet.net/functions/ifna-function)
:

    =NA() // returns #N/A error
    

The following will return true:

    =ISNA(NA()) // returns TRUE
    

### Count #N/A errors

To count cells in a range that contain #N/A errors, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 like this:

    =SUMPRODUCT(--ISNA(range))
    

The [double negative](https://exceljet.net/glossary/double-unary)
 coerces the TRUE and FALSE results from ISNA into 1s and 0s and SUMPRODUCT sums the result.

### Notes

*   The [IFNA function](https://exceljet.net/functions/ifna-function)
     is a more efficient way to trap and handle the #N/A error.

ISNA function examples
----------------------

[![Excel formula: Count cells not equal to many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to%20many.png "Excel formula: Count cells not equal to many things")](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)

### [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)

First, a little context. Normally, if you have just a couple things you don't want to count, you can use COUNTIFS like this: =COUNTIFS(range,"<>apple",range,"<>orange") But this doesn't scale very well if you have a list of many things, because you'll have to add an additional range/...

[![Excel formula: Range contains a value not in another range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/range%20contains%20a%20value%20not%20in%20another%20range.png "Excel formula: Range contains a value not in another range")](https://exceljet.net/formulas/range-contains-a-value-not-in-another-range)

### [Range contains a value not in another range](https://exceljet.net/formulas/range-contains-a-value-not-in-another-range)

Normally, the MATCH function receives a single lookup value, and returns a single match if any. In this case, however, we are giving MATCH an array for lookup value, so it will return an array of results, one per element in the lookup array. MATCH is configured for "exact match". If a match isn't...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

[![Excel formula: Count missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_missing_values.png "Excel formula: Count missing values")](https://exceljet.net/formulas/count-missing-values)

### [Count missing values](https://exceljet.net/formulas/count-missing-values)

In this example, the goal is to count the number of names in the range B5:B16 (Invited) that are missing from the range D5:D12 (Attended). This problem can be solved with the COUNTIF function or the MATCH function, as explained below. Both approaches work well. The advantage of the MATCH approach...

[![Excel formula: Count not equal to multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20not%20equal%20to%20multiple%20criteria.png "Excel formula: Count not equal to multiple criteria")](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)

### [Count not equal to multiple criteria](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)

In this example, the goal is to count rows in a set of data using multiple criteria and "not equals to" logic. Specifically, we want to count males that are not in group A or B. All data is in an Excel Table named data in the range B5:D15. This problem can be solved with the COUNTIFS function or...

Related functions
-----------------

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

[![Excel ISERR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserr%20function.png "Excel ISERR function")](https://exceljet.net/functions/iserr-function)

### [ISERR Function](https://exceljet.net/functions/iserr-function)

The Excel ISERR function returns TRUE for any error type except the #N/A error. You can use the ISERR function together with the IF function to test for an error and display a custom message, or perform a different calculation if found.

[![Excel ISEVEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iseven%20function.png "Excel ISEVEN function")](https://exceljet.net/functions/iseven-function)

### [ISEVEN Function](https://exceljet.net/functions/iseven-function)

The Excel ISEVEN function returns TRUE when a value is an even number, and FALSE when a value is an odd number. ISEVEN will return the #VALUE error if a value is not numeric.

[![Excel ISFORMULA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isformula%20function.png "Excel ISFORMULA function")](https://exceljet.net/functions/isformula-function)

### [ISFORMULA Function](https://exceljet.net/functions/isformula-function)

The Excel ISFORMULA function returns TRUE if a cell contains a formula, and FALSE if not. When a cell contains a formula ISFORMULA will return TRUE regardless of the formula's output or error conditions.

[![Excel ISLOGICAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20islogical%20function.png "Excel ISLOGICAL function")](https://exceljet.net/functions/islogical-function)

### [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)

The Excel ISLOGICAL function returns TRUE when a cell contains the logical values TRUE or FALSE, and returns FALSE for cells that contain any other value, including empty cells. 

[![Excel ISNONTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnontext%20function.png "Excel ISNONTEXT function")](https://exceljet.net/functions/isnontext-function)

### [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)

The Excel ISNONTEXT function returns TRUE when a cell contains any value except text. This includes numbers, dates, times, errors, and formulas that do not return text. ISNONTEXT also returns TRUE when a cell is empty.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel ISODD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isodd%20function.png "Excel ISODD function")](https://exceljet.net/functions/isodd-function)

### [ISODD Function](https://exceljet.net/functions/isodd-function)

The Excel ISODD function returns TRUE when a value is an odd number, and FALSE when a value is an even number. ISODD will return the #VALUE error if a value is not numeric.

[![Excel ISREF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isref%20function.png "Excel ISREF function")](https://exceljet.net/functions/isref-function)

### [ISREF Function](https://exceljet.net/functions/isref-function)

The Excel ISREF returns TRUE when a cell contains a reference and FALSE if not. You can use the ISREF function to check for a reference in a formula.

[![Excel ISTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20istext%20function.png "Excel ISTEXT function")](https://exceljet.net/functions/istext-function)

### [ISTEXT Function](https://exceljet.net/functions/istext-function)

The Excel ISTEXT function returns TRUE when a cell contains a [text value](https://exceljet.net/glossary/text-value)
, and FALSE if the cell contains any other value. You can use the ISTEXT function to check if a cell contains a text value, or a numeric value entered as text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    
*   [Count missing values](https://exceljet.net/formulas/count-missing-values)
    
*   [Count not equal to multiple criteria](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)
    
*   [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)
    
*   [Range contains a value not in another range](https://exceljet.net/formulas/range-contains-a-value-not-in-another-range)
    

### Functions

*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [ISERR Function](https://exceljet.net/functions/iserr-function)
    
*   [ISEVEN Function](https://exceljet.net/functions/iseven-function)
    
*   [ISFORMULA Function](https://exceljet.net/functions/isformula-function)
    
*   [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)
    
*   [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [ISODD Function](https://exceljet.net/functions/isodd-function)
    
*   [ISREF Function](https://exceljet.net/functions/isref-function)
    
*   [ISTEXT Function](https://exceljet.net/functions/istext-function)
    

### Links

*   [Microsoft ISNA function documentation](https://support.office.com/en-us/article/is-functions-0f2d7971-6019-40a0-a171-f2d869135665)
    

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