# Excel VALUETOTEXT function | Exceljet

**Source:** https://exceljet.net/functions/valuetotext-function

---

[Skip to main content](https://exceljet.net/functions/valuetotext-function#main-content)

[](https://exceljet.net/functions/valuetotext-function#)

*   [Previous](https://exceljet.net/functions/unique-function)
    
*   [Next](https://exceljet.net/functions/vstack-function)
    

Excel 2021

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

VALUETOTEXT Function
====================

by Dave Bruns · Updated 18 Jun 2025

Related functions 
------------------

[ARRAYTOTEXT](https://exceljet.net/functions/arraytotext-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel VALUETOTEXT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20valuetotext%20function.png "Excel VALUETOTEXT function")

Summary
-------

The Excel VALUETOTEXT function converts a value to text. By default, text values pass through unaffected. However, in strict mode, text values are enclosed in double quotes (""). Numeric values are converted to text in all cases, and [number formatting](https://exceljet.net/glossary/number-format)
 is lost.

Purpose 
--------

Converts a value to a text string

Return value 
-------------

Value as a text string

Syntax
------

    =VALUETOTEXT(value,[format])

*   _value_ - The value to convert to text.
*   _format_ - \[optional\] Output format. 0 = concise (default), and 1 = strict.

Using the VALUETOTEXT function 
-------------------------------

The VALUETOTEXT function converts a value to a [text string](https://exceljet.net/glossary/text-value)
. By default, text values pass through unaffected. However, in strict mode, text values are enclosed in double quotes (""). VALUETOTEXT will always remove [number formatting](https://exceljet.net/glossary/number-format)
 applied to numeric values, regardless of _format_.

The VALUETOTEXT function takes two arguments: _value_ and _format_. _Value_ is the value to convert to text. The _format_ argument controls the structure of the output. By default, _format_ is zero and VALUETOTEXT will output a "concise" format text value, essentially the normal format that Excel will use to display any text value. When _format_ is set to 1 (strict format), text values will be enclosed in double quotes ("").

> VALUETOTEXT is related to the [ARRAYTOTEXT function](https://exceljet.net/functions/arraytotext-function)
> , which performs the same kind of text conversion on [arrays](https://exceljet.net/glossary/array)
> .

### With numeric values

With the value 100 in cell A1:

    =VALUETOTEXT(A1) // returns "100"
    =VALUETOTEXT(A1,0) // returns "100"
    =VALUETOTEXT(A1,1) // returns "100"
    

In all cases, 100 is returned as a normal text string, and you will not see double quotes ("") in the output on a worksheet. However, you will see the output aligned left in cells with the [General number format](https://exceljet.net/videos/how-to-apply-general-formatting-in-excel)
 applied, since text values appear aligned left in Excel by default. If any [number formatting](https://exceljet.net/shortcuts/apply-number-format)
 (i.e. currency, percentage, etc.) has been applied to cell A1, it will be lost in the conversion.

### With text values

With the text "apple" in cell A1:

    =VALUETOTEXT(A1) // returns "apple"
    =VALUETOTEXT(A1,0) // returns "apple"
    =VALUETOTEXT(A1,1) // returns ""apple""
    

Notice in the first two examples above, the text "apple" passes through unchanged. In the third example, where _format_ is set to 1 (strict), double quotes are added to the text and will display on the worksheet.

Related functions
-----------------

[![Excel ARRAYTOTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20arraytotext%20function.png "Excel ARRAYTOTEXT function")](https://exceljet.net/functions/arraytotext-function)

### [ARRAYTOTEXT Function](https://exceljet.net/functions/arraytotext-function)

The Excel ARRAYTOTEXT function converts an array or range to a text string. The result can optionally include or omit curly braces.

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [ARRAYTOTEXT Function](https://exceljet.net/functions/arraytotext-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

### Links

*   [Microsoft VALUETOTEXT function documentation](https://support.microsoft.com/en-us/office/valuetotext-function-5fff61a2-301a-4ab2-9ffa-0a5242a08fea)
    

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