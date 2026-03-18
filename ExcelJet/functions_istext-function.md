# Excel ISTEXT function | Exceljet

**Source:** https://exceljet.net/functions/istext-function

---

[Skip to main content](https://exceljet.net/functions/istext-function#main-content)

[](https://exceljet.net/functions/istext-function#)

*   [Previous](https://exceljet.net/functions/isref-function)
    
*   [Next](https://exceljet.net/functions/n-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

ISTEXT Function
===============

by Dave Bruns · Updated 7 Sep 2021

Related functions 
------------------

[ISNONTEXT](https://exceljet.net/functions/isnontext-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

[ISERR](https://exceljet.net/functions/iserr-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[ISEVEN](https://exceljet.net/functions/iseven-function)

[ISLOGICAL](https://exceljet.net/functions/islogical-function)

[ISFORMULA](https://exceljet.net/functions/isformula-function)

[ISNA](https://exceljet.net/functions/isna-function)

[ISNONTEXT](https://exceljet.net/functions/isnontext-function)

[ISODD](https://exceljet.net/functions/isodd-function)

[ISREF](https://exceljet.net/functions/isref-function)

![Excel ISTEXT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20istext%20function.png "Excel ISTEXT function")

Summary
-------

The Excel ISTEXT function returns TRUE when a cell contains a [text value](https://exceljet.net/glossary/text-value)
, and FALSE if the cell contains any other value. You can use the ISTEXT function to check if a cell contains a text value, or a numeric value entered as text.

Purpose 
--------

Test for a text value

Return value 
-------------

A logical value (TRUE or FALSE)

Syntax
------

    =ISTEXT(value)

*   _value_ - The value to check.

Using the ISTEXT function 
--------------------------

The ISTEXT function returns TRUE when a cell contains a [text value](https://exceljet.net/glossary/text-value)
, and FALSE if the cell contains any other value, or is empty. You can use the ISTEXT function to check if a cell contains a text value, or a numeric value entered as text.

The ISTEXT function takes one [argument](https://exceljet.net/glossary/function-argument)
, _value_, which can be a cell reference, a formula, or a hardcoded value. Typically, value is entered as a cell reference like A1. When _value_ is text, the ISTEXT function will return TRUE. If value is any other value, ISTEXT will return FALSE.

### Examples

The ISTEXT function returns TRUE if _value_ is text:

    =ISTEXT("apple") // returns TRUE
    =ISTEXT(100) // returns FALSE
    

If cell A1 contains the number 100, ISTEXT returns FALSE:

    =ISTEXT(A1) // returns FALSE
    

If a cell contains a formula, ISTEXT checks the result of the formula:

    =ISTEXT(10 &" apples") // returns TRUE
    =ISTEXT(2+2) // returns FALSE
    =ISTEXT(A1&B1) // returns TRUE
    

Note: the ampersand (&) is the [concatenation](https://exceljet.net/glossary/concatenation)
 [operator](https://exceljet.net/glossary/math-operators)
 in Excel. When values are concatenated, the result is text.

### Count text values

To count cells in a range that contain text, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 like this:

    =SUMPRODUCT(--ISTEXT(range))
    

The [double negative](https://exceljet.net/glossary/double-unary)
 coerces the TRUE and FALSE results from ISTEXT into 1s and 0s and SUMPRODUCT sums the result.

### Notes

*   Dates and times are [numbers](https://exceljet.net/glossary/excel-date)
    , not text.
*   The [ISNONTEXT function](https://exceljet.net/functions/isnontext-function)
     tests for non-text values.

ISTEXT function examples
------------------------

[![Excel formula: Convert text to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert_text_to_numbers.png "Excel formula: Convert text to numbers")](https://exceljet.net/formulas/convert-text-to-numbers)

### [Convert text to numbers](https://exceljet.net/formulas/convert-text-to-numbers)

In this example, the goal is to convert the text values seen in column B to the numeric values seen in column D. There are several ways to fix this problem in Excel, but this article focuses on a formula-based approach to convert text values to numbers. It also explains how to convert values in...

[![Excel formula: Get first text value in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_first_text_value_in_a_range.png "Excel formula: Get first text value in a range")](https://exceljet.net/formulas/get-first-text-value-in-a-range)

### [Get first text value in a range](https://exceljet.net/formulas/get-first-text-value-in-a-range)

The general goal is to return the first text value in a range. Specifically, we have dates in column B and some city names in column C. We want a formula to find the first city listed in the range C5:C16. Because some cells in C5:C16 are empty, and some contain zeros, we need to ignore these cells...

[![Excel formula: Count cells that contain text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20text.png "Excel formula: Count cells that contain text")](https://exceljet.net/formulas/count-cells-that-contain-text)

### [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)

In this example, the goal is to count cells in a range that contain text values. This could be hard-coded text like "apple" or "red", numbers entered as text, or formulas that return text values. Empty cells and cells that contain numeric values or errors should not be included in the count. This...

[![Excel formula: VLOOKUP with numbers and text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20numbers%20and%20text.png "Excel formula: VLOOKUP with numbers and text")](https://exceljet.net/formulas/vlookup-with-numbers-and-text)

### [VLOOKUP with numbers and text](https://exceljet.net/formulas/vlookup-with-numbers-and-text)

In this example, the goal is to configure VLOOKUP to perform a lookup in a table where the first column contains numbers entered as text, and the lookup value is a true number. This mismatch between numbers and text will cause VLOOKUP to return an #N/A error. Typically, the lookup column in the...

[![Excel formula: Get first text value in a row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_text_value_in_a_row.png "Excel formula: Get first text value in a row")](https://exceljet.net/formulas/get-first-text-value-in-a-row)

### [Get first text value in a row](https://exceljet.net/formulas/get-first-text-value-in-a-row)

The goal is to return the first text value in each row, ignoring both blank cells and cells that contain numbers. This problem can be solved using the HLOOKUP function. In newer versions of Excel, you can use the XLOOKUP function, which is a more modern lookup function that can look up values in...

[![Excel formula: Data validation allow text only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20text%20only.png "Excel formula: Data validation allow text only")](https://exceljet.net/formulas/data-validation-allow-text-only)

### [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)

Data validation rules are triggered when a user adds or changes a cell value. Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined. The ISTEXT function returns TRUE when a value is text and FALSE if not. As a...

ISTEXT function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/what%20is%20text%20in%20Excel-thumb.png)](https://exceljet.net/videos/what-is-text-in-excel)

### [What is text in Excel](https://exceljet.net/videos/what-is-text-in-excel)

In this video we're going to take a quick look at the question: "what is text in Excel?" Whenever you enter data in an Excel worksheet, Excel checks the data type you've entered and classifies it according to four basic data types: Numbers Dates and times Boolean values Text Excel figures out the...

Related functions
-----------------

[![Excel ISNONTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnontext%20function.png "Excel ISNONTEXT function")](https://exceljet.net/functions/isnontext-function)

### [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)

The Excel ISNONTEXT function returns TRUE when a cell contains any value except text. This includes numbers, dates, times, errors, and formulas that do not return text. ISNONTEXT also returns TRUE when a cell is empty.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

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

[![Excel ISLOGICAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20islogical%20function.png "Excel ISLOGICAL function")](https://exceljet.net/functions/islogical-function)

### [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)

The Excel ISLOGICAL function returns TRUE when a cell contains the logical values TRUE or FALSE, and returns FALSE for cells that contain any other value, including empty cells. 

[![Excel ISFORMULA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isformula%20function.png "Excel ISFORMULA function")](https://exceljet.net/functions/isformula-function)

### [ISFORMULA Function](https://exceljet.net/functions/isformula-function)

The Excel ISFORMULA function returns TRUE if a cell contains a formula, and FALSE if not. When a cell contains a formula ISFORMULA will return TRUE regardless of the formula's output or error conditions.

[![Excel ISNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isna%20function.png "Excel ISNA function")](https://exceljet.net/functions/isna-function)

### [ISNA Function](https://exceljet.net/functions/isna-function)

The Excel ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs.

[![Excel ISNONTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnontext%20function.png "Excel ISNONTEXT function")](https://exceljet.net/functions/isnontext-function)

### [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)

The Excel ISNONTEXT function returns TRUE when a cell contains any value except text. This includes numbers, dates, times, errors, and formulas that do not return text. ISNONTEXT also returns TRUE when a cell is empty.

[![Excel ISODD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isodd%20function.png "Excel ISODD function")](https://exceljet.net/functions/isodd-function)

### [ISODD Function](https://exceljet.net/functions/isodd-function)

The Excel ISODD function returns TRUE when a value is an odd number, and FALSE when a value is an even number. ISODD will return the #VALUE error if a value is not numeric.

[![Excel ISREF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isref%20function.png "Excel ISREF function")](https://exceljet.net/functions/isref-function)

### [ISREF Function](https://exceljet.net/functions/isref-function)

The Excel ISREF returns TRUE when a cell contains a reference and FALSE if not. You can use the ISREF function to check for a reference in a formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)
    
*   [VLOOKUP with numbers and text](https://exceljet.net/formulas/vlookup-with-numbers-and-text)
    
*   [Get first text value in a row](https://exceljet.net/formulas/get-first-text-value-in-a-row)
    
*   [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)
    
*   [Convert text to numbers](https://exceljet.net/formulas/convert-text-to-numbers)
    
*   [Get first text value in a range](https://exceljet.net/formulas/get-first-text-value-in-a-range)
    

### Videos

*   [What is text in Excel](https://exceljet.net/videos/what-is-text-in-excel)
    

### Functions

*   [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [ISERR Function](https://exceljet.net/functions/iserr-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [ISEVEN Function](https://exceljet.net/functions/iseven-function)
    
*   [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)
    
*   [ISFORMULA Function](https://exceljet.net/functions/isformula-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    
*   [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)
    
*   [ISODD Function](https://exceljet.net/functions/isodd-function)
    
*   [ISREF Function](https://exceljet.net/functions/isref-function)
    

### Links

*   [Microsoft ISTEXT function documentation](https://support.office.com/en-us/article/is-functions-0f2d7971-6019-40a0-a171-f2d869135665)
    

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