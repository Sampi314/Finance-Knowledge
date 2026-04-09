# Excel ISFORMULA function | Exceljet

**Source:** https://exceljet.net/functions/isformula-function

---

[Skip to main content](https://exceljet.net/functions/isformula-function#main-content)

[](https://exceljet.net/functions/isformula-function#)

*   [Previous](https://exceljet.net/functions/iseven-function)
    
*   [Next](https://exceljet.net/functions/islogical-function)
    

Excel 2013

[Information](https://exceljet.net/functions#Information)

ISFORMULA Function
==================

by Dave Bruns · Updated 6 Sep 2021

Related functions 
------------------

[FORMULATEXT](https://exceljet.net/functions/formulatext-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

[ISERR](https://exceljet.net/functions/iserr-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[ISEVEN](https://exceljet.net/functions/iseven-function)

[ISLOGICAL](https://exceljet.net/functions/islogical-function)

[ISNA](https://exceljet.net/functions/isna-function)

[ISNONTEXT](https://exceljet.net/functions/isnontext-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[ISODD](https://exceljet.net/functions/isodd-function)

[ISREF](https://exceljet.net/functions/isref-function)

[ISTEXT](https://exceljet.net/functions/istext-function)

![Excel ISFORMULA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20isformula%20function.png "Excel ISFORMULA function")

Summary
-------

The Excel ISFORMULA function returns TRUE if a cell contains a formula, and FALSE if not. When a cell contains a formula ISFORMULA will return TRUE regardless of the formula's output or error conditions.

Purpose 
--------

Test if cell contains a formula

Return value 
-------------

TRUE or FALSE

Syntax
------

    =ISFORMULA(reference)

*   _reference_ - Reference to cell or cell range.

Using the ISFORMULA function 
-----------------------------

The ISFORMULA function returns TRUE if a cell contains a formula, and FALSE if not. When a cell contains a formula ISFORMULA will return TRUE regardless of the formula's output or error conditions. The ISFORMULA takes one [argument](https://exceljet.net/glossary/function-argument)
, _reference_, which must be a cell reference.

### Examples

If cell A1 contains the formula =2+2, the ISFORMULA function returns TRUE:

    =ISFORMULA(A1) // returns TRUE
    

If cell A1 contains the text "apple", the ISFORMULA function returns FALSE:

    =ISFORMULA(A1) // returns FALSE
    

### Count formulas

To count cells in a range that contain formulas, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 like this:

    =SUMPRODUCT(--ISFORMULA(range))
    

The [double negative](https://exceljet.net/glossary/double-unary)
 coerces the TRUE and FALSE results from ISFORMULA into 1s and 0s and SUMPRODUCT returns the sum.

### Notes

*   You can _temporarily_ display all formulas in a worksheet with a [keyboard shortcut](https://exceljet.net/shortcuts/toggle-formulas-on-and-off)
    .
*   To extract and display a formula as text, use the [FORMULATEXT function](https://exceljet.net/functions/formulatext-function)
    .

ISFORMULA function examples
---------------------------

[![Excel formula: Show formula text with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/show%20formula%20text%20with%20formula.png "Excel formula: Show formula text with formula")](https://exceljet.net/formulas/show-formula-text-with-formula)

### [Show formula text with formula](https://exceljet.net/formulas/show-formula-text-with-formula)

The FORMULATEXT is fully automatic. When given the reference of a cell that contains a formula, it will return the entire formula as text. In the example as shown, the formula: =FORMULATEXT(C5) returns the text "=IF(B5>=70,"Pass","Fail")". Dealing with errors The FORMULATEXT function will return...

[![Excel formula: Sum formulas only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20formulas%20only.png "Excel formula: Sum formulas only")](https://exceljet.net/formulas/sum-formulas-only)

### [Sum formulas only](https://exceljet.net/formulas/sum-formulas-only)

In this example, the goal is to calculate a sum of the values in a range that are generated with a formula. In other words, we want to sum values in a range while ignoring the values that have been entered manually. In the context of this example, the hardcoded values in C5:C12 represent actual...

[![Excel formula: Count cells that contain formulas](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_cells_that_contain_formulas.png "Excel formula: Count cells that contain formulas")](https://exceljet.net/formulas/count-cells-that-contain-formulas)

### [Count cells that contain formulas](https://exceljet.net/formulas/count-cells-that-contain-formulas)

In this example, the goal is to count the number of cells in a range that contain formulas. This problem can be solved with a formula based on the SUMPRODUCT and ISFORMULA functions, as explained below. Forecast values The values in the range C13:C16 are forecasts created with a formula based on...

Related functions
-----------------

[![Excel FORMULATEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20formulatext%20function.png "Excel FORMULATEXT function")](https://exceljet.net/functions/formulatext-function)

### [FORMULATEXT Function](https://exceljet.net/functions/formulatext-function)

The Excel FORMULATEXT function returns a formula as a text string from a given reference. You can use FORMULATEXT to extract the formula as text from a cell. If you use FORMULATEXT on a cell that doesn't contain a formula, it returns #N/A.

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

*   [Sum formulas only](https://exceljet.net/formulas/sum-formulas-only)
    
*   [Count cells that contain formulas](https://exceljet.net/formulas/count-cells-that-contain-formulas)
    
*   [Show formula text with formula](https://exceljet.net/formulas/show-formula-text-with-formula)
    

### Functions

*   [FORMULATEXT Function](https://exceljet.net/functions/formulatext-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [ISERR Function](https://exceljet.net/functions/iserr-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [ISEVEN Function](https://exceljet.net/functions/iseven-function)
    
*   [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    
*   [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [ISODD Function](https://exceljet.net/functions/isodd-function)
    
*   [ISREF Function](https://exceljet.net/functions/isref-function)
    
*   [ISTEXT Function](https://exceljet.net/functions/istext-function)
    

### Links

*   [Microsoft ISFORMULA function documentation](https://support.office.com/en-us/article/isformula-function-e4d1355f-7121-4ef2-801e-3839bfd6b1e5)
    

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