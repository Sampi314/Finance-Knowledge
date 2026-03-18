# Excel ISEVEN function | Exceljet

**Source:** https://exceljet.net/functions/iseven-function

---

[Skip to main content](https://exceljet.net/functions/iseven-function#main-content)

[](https://exceljet.net/functions/iseven-function#)

*   [Previous](https://exceljet.net/functions/iserror-function)
    
*   [Next](https://exceljet.net/functions/isformula-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

ISEVEN Function
===============

by Dave Bruns · Updated 6 Sep 2021

Related functions 
------------------

[ISODD](https://exceljet.net/functions/isodd-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

[ISERR](https://exceljet.net/functions/iserr-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[ISFORMULA](https://exceljet.net/functions/isformula-function)

[ISLOGICAL](https://exceljet.net/functions/islogical-function)

[ISNA](https://exceljet.net/functions/isna-function)

[ISNONTEXT](https://exceljet.net/functions/isnontext-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[ISREF](https://exceljet.net/functions/isref-function)

[ISTEXT](https://exceljet.net/functions/istext-function)

![Excel ISEVEN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20iseven%20function.png "Excel ISEVEN function")

Summary
-------

The Excel ISEVEN function returns TRUE when a value is an even number, and FALSE when a value is an odd number. ISEVEN will return the #VALUE error if a value is not numeric.

Purpose 
--------

Test if a value is even

Return value 
-------------

A logical value (TRUE or FALSE)

Syntax
------

    =ISEVEN(value)

*   _value_ - The numeric value to check.

Using the ISEVEN function 
--------------------------

The ISEVEN function tests for even numbers. ISEVEN takes one [argument](https://exceljet.net/glossary/function-argument)
, _value_, which should be a numeric value or a cell reference. When _value_ is an even number, ISEVEN returns TRUE. When _value_ is an odd number, ISEVEN returns FALSE. If _value_ is not numeric, ISEVEN will return the #VALUE error. Only the integer portion of _value_ is evaluated, decimal values are truncated.

### Examples

The ISEVEN function returns TRUE or FALSE:

    =ISEVEN(4) // returns TRUE
    =ISEVEN(3) // returns FALSE
    =ISEVEN(0) // returns TRUE
    

If cell A1 contains 11, the formula below returns FALSE:

    =ISEVEN(A1) //returns FALSE
    

Only the integer portion of _value_ is tested. If _value_ is a decimal number, the decimal portion is truncated:

    =ISEVEN(4.1) // returns TRUE
    =ISEVEN(0.33) // returns TRUE
    =ISEVEN(7.4) // returns FALSE
    

### Notes

*   If _value_ is not numeric, ISEVEN will return the #VALUE error.
*   Only the integer portion of _value_ is tested, decimal values are truncated.
*   Use the [ISODD function](https://exceljet.net/functions/isodd-function)
     to test for odd numbers.

ISEVEN function examples
------------------------

[![Excel formula: Count cells that contain odd numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20odd%20numbers.png "Excel formula: Count cells that contain odd numbers")](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)

### [Count cells that contain odd numbers](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)

In this example, the goal is to count odd numbers in the range B5:B15, which is named data . This can be done with the SUMPRODUCT function together with the ISODD function. Instead of ISODD, the MOD function can also be used. Both approaches are explained below. SUMPRODUCT with ISODD The SUMPRODUCT...

[![Excel formula: Highlight every other row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20every%20other%20row.png "Excel formula: Highlight every other row")](https://exceljet.net/formulas/highlight-every-other-row)

### [Highlight every other row](https://exceljet.net/formulas/highlight-every-other-row)

When you use a formula to apply conditional formatting, the formula is evaluated for every cell in the selection. In this case, there are no addresses in the formula, so, for every cell in the data, the ROW and ISEVEN functions are run. ROW returns the row number of the cell, and ISEVEN returns...

[![Excel formula: Shade alternating groups of n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Shade%20alternating%20groups%20of%20n%20rows.png "Excel formula: Shade alternating groups of n rows")](https://exceljet.net/formulas/shade-alternating-groups-of-n-rows)

### [Shade alternating groups of n rows](https://exceljet.net/formulas/shade-alternating-groups-of-n-rows)

Working from the inside out, we first "normalize" row numbers to begin with 1 using the ROW function and an offset: ROW()-offset In this case, the first row of data is in row 5, so we use an offset of 4: ROW()-4 // 1 in row 5 ROW()-4 // 2 in row 6 ROW()-4 // 3 in row 7 etc. The result goes into the...

ISEVEN function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20zebra%20stripes%20with%20conditional%20formatting-thumb.png)](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

### [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

In this video, we'll look at how to use conditional formatting to shade every other row in a table. This is sometimes called "zebra striping". In this spreadsheet, we have a table of employees with a small amount of formatting. To get shading on every other row, we could just convert this table to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Shade%20groups%20of%20rows%20with%20conditional%20formatting-thumb.png)](https://exceljet.net/videos/shade-groups-of-rows-with-conditional-formatting)

### [Shade groups of rows with conditional formatting](https://exceljet.net/videos/shade-groups-of-rows-with-conditional-formatting)

In this video, we'll look at how to use conditional formatting to shade alternating groups of rows. For example, you can use this approach to shade groups of 3 rows, groups of 4 rows, and so on. This can be a nice way to make certain tables easier to read. Here we have a table with 3 rows of data...

Related functions
-----------------

[![Excel ISODD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isodd%20function.png "Excel ISODD function")](https://exceljet.net/functions/isodd-function)

### [ISODD Function](https://exceljet.net/functions/isodd-function)

The Excel ISODD function returns TRUE when a value is an odd number, and FALSE when a value is an even number. ISODD will return the #VALUE error if a value is not numeric.

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

[![Excel ISERR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserr%20function.png "Excel ISERR function")](https://exceljet.net/functions/iserr-function)

### [ISERR Function](https://exceljet.net/functions/iserr-function)

The Excel ISERR function returns TRUE for any error type except the #N/A error. You can use the ISERR function together with the IF function to test for an error and display a custom message, or perform a different calculation if found.

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

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

*   [Highlight every other row](https://exceljet.net/formulas/highlight-every-other-row)
    
*   [Shade alternating groups of n rows](https://exceljet.net/formulas/shade-alternating-groups-of-n-rows)
    
*   [Count cells that contain odd numbers](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)
    
*   [Shade groups of rows with conditional formatting](https://exceljet.net/videos/shade-groups-of-rows-with-conditional-formatting)
    

### Functions

*   [ISODD Function](https://exceljet.net/functions/isodd-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [ISERR Function](https://exceljet.net/functions/iserr-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [ISFORMULA Function](https://exceljet.net/functions/isformula-function)
    
*   [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    
*   [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [ISREF Function](https://exceljet.net/functions/isref-function)
    
*   [ISTEXT Function](https://exceljet.net/functions/istext-function)
    

### Links

*   [Microsoft ISEVEN function documentation](https://support.office.com/en-us/article/iseven-function-aa15929a-d77b-4fbb-92f4-2f479af55356)
    

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