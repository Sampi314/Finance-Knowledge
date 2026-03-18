# Excel ISREF function | Exceljet

**Source:** https://exceljet.net/functions/isref-function

---

[Skip to main content](https://exceljet.net/functions/isref-function#main-content)

[](https://exceljet.net/functions/isref-function#)

*   [Previous](https://exceljet.net/functions/isodd-function)
    
*   [Next](https://exceljet.net/functions/istext-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

ISREF Function
==============

by Dave Bruns · Updated 8 Sep 2021

Related functions 
------------------

[ISBLANK](https://exceljet.net/functions/isblank-function)

[ISERR](https://exceljet.net/functions/iserr-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[ISEVEN](https://exceljet.net/functions/iseven-function)

[ISFORMULA](https://exceljet.net/functions/isformula-function)

[ISLOGICAL](https://exceljet.net/functions/islogical-function)

[ISNA](https://exceljet.net/functions/isna-function)

[ISNONTEXT](https://exceljet.net/functions/isnontext-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[ISODD](https://exceljet.net/functions/isodd-function)

[ISTEXT](https://exceljet.net/functions/istext-function)

![Excel ISREF function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20isref%20function.png "Excel ISREF function")

Summary
-------

The Excel ISREF returns TRUE when a cell contains a reference and FALSE if not. You can use the ISREF function to check for a reference in a formula.

Purpose 
--------

Test for a reference

Return value 
-------------

A logical value (TRUE or FALSE)

Syntax
------

    =ISREF(value)

*   _value_ - The value to check.

Using the ISREF function 
-------------------------

The ISREF function returns TRUE to test for a reference in a formula. The ISREF function takes one [argument](https://exceljet.net/glossary/function-argument)
, _value_, to test. If _value_ is a valid cell reference, [range](https://exceljet.net/glossary/range)
, or [named range](https://exceljet.net/glossary/named-range)
, ISREF returns TRUE. If _value_ is not a reference, ISREF returns FALSE. ISREF does not evaluate the _contents_ of a reference, just the reference itself.

### Examples

ISREF returns TRUE when value is a reference and FALSE if not:

    =ISREF(A1) // returns TRUE
    =ISREF(A1:C1) // returns TRUE
    =ISREF(Sheet1!A1) // returns TRUE
    =ISREF("apple") // returns FALSE
    =ISREF(100) // returns FALSE
    =ISREF(ZZZ1) // returns FALSE
    

Some functions, like INDEX and OFFSET, can return a reference. As long as the reference is valid, ISREF returns TRUE:

    =ISREF(INDEX(A:A,10)) // returns TRUE
    =ISREF(OFFSET(A1,1,1)) // returns TRUE
    

To evaluate a reference as [text](https://exceljet.net/glossary/text-value)
 (i.e. "A1"), use the INDIRECT function:

    =ISREF(INDIRECT("A1")) // returns TRUE
    =ISREF(INDIRECT("ZZZ1")) // returns FALSE
    

### Notes

*   Use the [INDIRECT function](https://exceljet.net/functions/indirect-function)
     with ISREF to evaluate a reference as text.

ISREF function examples
-----------------------

[![Excel formula: How to fix the #REF! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20REF%20error.png "Excel formula: How to fix the #REF! error")](https://exceljet.net/formulas/how-to-fix-the-ref-error)

### [How to fix the #REF! error](https://exceljet.net/formulas/how-to-fix-the-ref-error)

About the #REF! error The #REF! error occurs when a reference is invalid. In many cases, this is because sheets, rows, or columns have been removed, or because a formula with relative references has been copied to a new location where references are invalid. In the example shown, the formula in C10...

[![Excel formula: Worksheet name exists](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/worksheet%20name%20exists.png "Excel formula: Worksheet name exists")](https://exceljet.net/formulas/worksheet-name-exists)

### [Worksheet name exists](https://exceljet.net/formulas/worksheet-name-exists)

The ISREF function returns TRUE for a valid worksheet reference and FALSE is not. In this case, we want to find out of a particular sheet exists in a workbook, so we construct a full reference by concatenating the sheet names in column B with an exclamation mark and "A1": B5...

[![Excel formula: Count errors in all sheets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_errors_in_all_sheets.png "Excel formula: Count errors in all sheets")](https://exceljet.net/formulas/count-errors-in-all-sheets)

### [Count errors in all sheets](https://exceljet.net/formulas/count-errors-in-all-sheets)

In this example, the goal is to count errors in a workbook by sheet, where the sheet names have been previously entered in a column as shown. This is a tricky problem in Excel for a couple of reasons. First, there is no direct way to generate a list of sheets in a workbook with a formula. Second,...

Related functions
-----------------

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

[![Excel ISERR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserr%20function.png "Excel ISERR function")](https://exceljet.net/functions/iserr-function)

### [ISERR Function](https://exceljet.net/functions/iserr-function)

The Excel ISERR function returns TRUE for any error type except the #N/A error. You can use the ISERR function together with the IF function to test for an error and display a custom message, or perform a different calculation if found.

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

[![Excel ISEVEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iseven%20function.png "Excel ISEVEN function")](https://exceljet.net/functions/iseven-function)

### [ISEVEN Function](https://exceljet.net/functions/iseven-function)

The Excel ISEVEN function returns TRUE when a value is an even number, and FALSE when a value is an odd number. ISEVEN will return the #VALUE error if a value is not numeric.

[![Excel ISFORMULA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isformula%20function.png "Excel ISFORMULA function")](https://exceljet.net/functions/isformula-function)

### [ISFORMULA Function](https://exceljet.net/functions/isformula-function)

The Excel ISFORMULA function returns TRUE if a cell contains a formula, and FALSE if not. When a cell contains a formula ISFORMULA will return TRUE regardless of the formula's output or error conditions.

[![Excel ISLOGICAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20islogical%20function.png "Excel ISLOGICAL function")](https://exceljet.net/functions/islogical-function)

### [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)

The Excel ISLOGICAL function returns TRUE when a cell contains the logical values TRUE or FALSE, and returns FALSE for cells that contain any other value, including empty cells. 

[![Excel ISNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isna%20function.png "Excel ISNA function")](https://exceljet.net/functions/isna-function)

### [ISNA Function](https://exceljet.net/functions/isna-function)

The Excel ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs.

[![Excel ISNONTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnontext%20function.png "Excel ISNONTEXT function")](https://exceljet.net/functions/isnontext-function)

### [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)

The Excel ISNONTEXT function returns TRUE when a cell contains any value except text. This includes numbers, dates, times, errors, and formulas that do not return text. ISNONTEXT also returns TRUE when a cell is empty.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel ISODD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isodd%20function.png "Excel ISODD function")](https://exceljet.net/functions/isodd-function)

### [ISODD Function](https://exceljet.net/functions/isodd-function)

The Excel ISODD function returns TRUE when a value is an odd number, and FALSE when a value is an even number. ISODD will return the #VALUE error if a value is not numeric.

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

*   [Worksheet name exists](https://exceljet.net/formulas/worksheet-name-exists)
    
*   [Count errors in all sheets](https://exceljet.net/formulas/count-errors-in-all-sheets)
    
*   [How to fix the #REF! error](https://exceljet.net/formulas/how-to-fix-the-ref-error)
    

### Functions

*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [ISERR Function](https://exceljet.net/functions/iserr-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [ISEVEN Function](https://exceljet.net/functions/iseven-function)
    
*   [ISFORMULA Function](https://exceljet.net/functions/isformula-function)
    
*   [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    
*   [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [ISODD Function](https://exceljet.net/functions/isodd-function)
    
*   [ISTEXT Function](https://exceljet.net/functions/istext-function)
    

### Links

*   [Microsoft ISREF function documentation](https://support.office.com/en-us/article/is-functions-0f2d7971-6019-40a0-a171-f2d869135665)
    

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