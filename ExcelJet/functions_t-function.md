# Excel T function | Exceljet

**Source:** https://exceljet.net/functions/t-function

---

[Skip to main content](https://exceljet.net/functions/t-function#main-content)

[](https://exceljet.net/functions/t-function#)

*   [Previous](https://exceljet.net/functions/sheets-function)
    
*   [Next](https://exceljet.net/functions/type-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

T Function
==========

by Dave Bruns · Updated 9 Sep 2021

Related functions 
------------------

[N](https://exceljet.net/functions/n-function)

![Excel T function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20t%20function.png "Excel T function")

Summary
-------

The Excel T function returns text when given a text value and an empty string ("") for numbers, dates, and the logical values TRUE and FALSE. You can use the T function to remove values that are not text.

Purpose 
--------

Filter text values only

Return value 
-------------

Value as text when text

Syntax
------

    =T(value)

*   _value_ - The value to return as text.

Using the T function 
---------------------

The Excel T function converts numbers, dates, and the logical values TRUE and FALSE into [empty strings](https://exceljet.net/glossary/empty-string)
.  Text values and errors are not converted and pass through unaffected. You can use the T function to remove values that are not text.

The T function takes one argument, _value_, which can be a cell reference, a formula result, or a hardcoded value.

### Examples

The T function returns text when given a text value and an empty string ("") for numbers, dates, and the logical values TRUE and FALSE. For example:

    =T("apple") // returns "apple"
    =T("NASA") // returns "NASA"
    =T(100) // returns ""
    =T(FALSE) // returns ""
    

In most cases, the T function is unnecessary, because Excel automatically converts values when needed. The T function is provided for compatibility with other spreadsheet programs.

Errors are not affected by the T function:

    =T(3/0) // returns #DIV/0!
    =T("#N/A") // returns #N/A
    

### Notes

1.  The T function removes numeric values. The [N function](https://exceljet.net/functions/n-function)
     removes text values.

T function examples
-------------------

[![Excel formula: List sheet names with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/List_sheet_names_with_formula_0.png "Excel formula: List sheet names with formula")](https://exceljet.net/formulas/list-sheet-names-with-formula)

### [List sheet names with formula](https://exceljet.net/formulas/list-sheet-names-with-formula)

In this example, the goal is to generate a list of the sheet names in an Excel workbook with a formula. Unfortunately, there is no simple way to do this with a formula in Excel. However, it can be done with a two-step approach: Define a name called "sheetnames" with an old macro command and the...

[![Excel formula: Translate letters to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/translate%20letters%20to%20numbers.png "Excel formula: Translate letters to numbers")](https://exceljet.net/formulas/translate-letters-to-numbers)

### [Translate letters to numbers](https://exceljet.net/formulas/translate-letters-to-numbers)

At the core, this formula uses an array operation to generate an array of letters from the input text, translates each letter individually to a number, then joins all numbers together again and returns the output as a string. To parse the input string into an array or letters, we use MID, ROW, LEN...

Related functions
-----------------

[![Excel N function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20n%20function.png "Excel N function")](https://exceljet.net/functions/n-function)

### [N Function](https://exceljet.net/functions/n-function)

The Excel N function returns a number when given a value. The N function can be used to convert TRUE and FALSE to 1 and 0 respectively. When given a text value, the N function returns zero.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Translate letters to numbers](https://exceljet.net/formulas/translate-letters-to-numbers)
    
*   [List sheet names with formula](https://exceljet.net/formulas/list-sheet-names-with-formula)
    

### Functions

*   [N Function](https://exceljet.net/functions/n-function)
    

### Links

*   [Microsoft T function documentation](https://support.office.com/en-us/article/t-function-fb83aeec-45e7-4924-af95-53e073541228)
    

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