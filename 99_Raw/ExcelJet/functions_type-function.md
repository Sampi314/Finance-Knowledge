# Excel TYPE function | Exceljet

**Source:** https://exceljet.net/functions/type-function

---

[Skip to main content](https://exceljet.net/functions/type-function#main-content)

[](https://exceljet.net/functions/type-function#)

*   [Previous](https://exceljet.net/functions/t-function)
    
*   [Next](https://exceljet.net/functions/abs-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

TYPE Function
=============

by Dave Bruns · Updated 16 May 2023

Related functions 
------------------

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[ISTEXT](https://exceljet.net/functions/istext-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[ISFORMULA](https://exceljet.net/functions/isformula-function)

[ISREF](https://exceljet.net/functions/isref-function)

[ISLOGICAL](https://exceljet.net/functions/islogical-function)

![Excel TYPE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20type%20function.png "Excel TYPE function")

Summary
-------

The Excel TYPE function returns a numeric code representing "type" in 5 categories: number = 1, text = 2, logical = 4, error = 16, and array = 64. Use TYPE when the operation of a formula depends on the type of value in a particular cell.

Purpose 
--------

Get the type of value in a cell

Return value 
-------------

A numeric code representing type

Syntax
------

    =TYPE(value)

*   _value_ - The value to check the type of.

Using the TYPE function 
------------------------

The TYPE function returns a numeric code representing "type" in 5 categories: number = 1, text = 2, logical = 4, error = 16, and array = 64. The TYPE function takes one argument, _value_, which can be a reference, a formula, or a hardcoded value. The table below shows the possible type codes returned from TYPE and the meaning of each:

| Type code | Meaning |
| --- | --- |
| 1   | Number |
| 2   | Text |
| 4   | Logical value |
| 16  | Error value |
| 64  | [Array](https://exceljet.net/glossary/array) |
| 128 | Compound data |

### Examples

The TYPE function returns a numeric code:

    =TYPE(100) // returns 1 for numbers
    =TYPE("apple") // returns 2 for text
    =TYPE(TRUE) // returns 4 for logicals
    

 TYPE returns 16 for errors:

    =TYPE(3/0) // returns 16
    =TYPE(NA()) // returns 16
    

If TYPE is given an [array constant](https://exceljet.net/glossary/array-constant)
, or a [range](https://exceljet.net/glossary/range)
, the result is 64:

    =TYPE({1;2;3}) // returns 64
    =TYPE(A1:C1 // returns 64
    

 TYPE returns 128 for compound data, like LAMBDA functions:

    =TYPE(LAMBDA(x,x*x)) // returns 128
    

### Notes

*   You can't use TYPE to test for a formula, because TYPE evaluates the result.
*   [Excel dates](https://exceljet.net/glossary/excel-date)
     and [times](https://exceljet.net/glossary/excel-time)
     are numeric values, and therefore return 1.

Related functions
-----------------

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel ISTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20istext%20function.png "Excel ISTEXT function")](https://exceljet.net/functions/istext-function)

### [ISTEXT Function](https://exceljet.net/functions/istext-function)

The Excel ISTEXT function returns TRUE when a cell contains a [text value](https://exceljet.net/glossary/text-value)
, and FALSE if the cell contains any other value. You can use the ISTEXT function to check if a cell contains a text value, or a numeric value entered as text.

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

[![Excel ISFORMULA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isformula%20function.png "Excel ISFORMULA function")](https://exceljet.net/functions/isformula-function)

### [ISFORMULA Function](https://exceljet.net/functions/isformula-function)

The Excel ISFORMULA function returns TRUE if a cell contains a formula, and FALSE if not. When a cell contains a formula ISFORMULA will return TRUE regardless of the formula's output or error conditions.

[![Excel ISREF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isref%20function.png "Excel ISREF function")](https://exceljet.net/functions/isref-function)

### [ISREF Function](https://exceljet.net/functions/isref-function)

The Excel ISREF returns TRUE when a cell contains a reference and FALSE if not. You can use the ISREF function to check for a reference in a formula.

[![Excel ISLOGICAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20islogical%20function.png "Excel ISLOGICAL function")](https://exceljet.net/functions/islogical-function)

### [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)

The Excel ISLOGICAL function returns TRUE when a cell contains the logical values TRUE or FALSE, and returns FALSE for cells that contain any other value, including empty cells. 

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [ISTEXT Function](https://exceljet.net/functions/istext-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [ISFORMULA Function](https://exceljet.net/functions/isformula-function)
    
*   [ISREF Function](https://exceljet.net/functions/isref-function)
    
*   [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)
    

### Links

*   [Microsoft TYPE function documentation](https://support.office.com/en-us/article/type-function-45b4e688-4bc3-48b3-a105-ffa892995899)
    

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