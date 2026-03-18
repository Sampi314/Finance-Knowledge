# Convert numbers to text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-numbers-to-text

---

[Skip to main content](https://exceljet.net/formulas/convert-numbers-to-text#main-content)

[](https://exceljet.net/formulas/convert-numbers-to-text#)

*   [Previous](https://exceljet.net/formulas/conditional-message-with-rept-function)
    
*   [Next](https://exceljet.net/formulas/convert-text-to-numbers)
    

[Text](https://exceljet.net/formulas#Text)

Convert numbers to text
=======================

by Dave Bruns · Updated 4 Oct 2023

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Convert numbers to text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20numbers%20to%20text.png "Excel formula: Convert numbers to text")

Summary
-------

To convert numbers into text values, you can use the [TEXT function](https://exceljet.net/functions/text-function)
. In the example shown, the formula in C5 is:

    =TEXT(B5,"0")
    

The result is the number 1021 formatted as text "1021". All numbers in column D are formatted as text with the formulas seen in column F.

Generic formula
---------------

    =TEXT(A1,"0")

Explanation 
------------

Normally, you want to maintain numeric values in Excel, because they can be used in formulas that perform numeric calculations. However, there are situations where converting numbers to text makes sense. One example is when you want to [concatenate](https://exceljet.net/glossary/concatenation)
 (join) a formatted number to text. For example, "Sales last year increased by over 15%", where the number .15 has been formatted with a percent symbol. Without the TEXT function, the number formatting will be stripped. Another example is when you want to perform a [lookup on numbers using wildcards](https://exceljet.net/formulas/partial-match-with-numbers-and-wildcard)
, which can't be done with numeric values.

### Convert with formatting

The [TEXT function](https://exceljet.net/functions/text-function)
 can be used to convert numbers to text using a given [number format](https://exceljet.net/glossary/number-format)
. In the example shown, the TEXT function is used to convert each number in column B to a text value using the formula and number shown in column F. The TEXT function accepts a number as the _value_ argument, the [number format](https://exceljet.net/glossary/number-format)
 to use as the _format\_text_ argument. The number format can include codes for dates, times, numbers, currency, percentage, and so on, as well as [custom number formats](https://exceljet.net/articles/custom-number-formats)
. Notice the output from the TEXT function is a text value, which is left-aligned by default in Excel.

### Convert without formatting

To convert a number in A1 to a text value without number formatting, you can [concatenate](https://exceljet.net/glossary/concatenation)
 the number to an [empty string](https://exceljet.net/glossary/empty-string)
 ("") like this:

    =A1&"" // convert A1 to text
    

With the number 100 in cell A1, the result is "100".

Related formulas
----------------

[![Excel formula: Convert text to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert_text_to_numbers.png "Excel formula: Convert text to numbers")](https://exceljet.net/formulas/convert-text-to-numbers)

### [Convert text to numbers](https://exceljet.net/formulas/convert-text-to-numbers)

In this example, the goal is to convert the text values seen in column B to the numeric values seen in column D. There are several ways to fix this problem in Excel, but this article focuses on a formula-based approach to convert text values to numbers. It also explains how to convert values in...

[![Excel formula: Get month name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20month%20name%20from%20date_0.png "Excel formula: Get month name from date")](https://exceljet.net/formulas/get-month-name-from-date)

### [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)

In this example, the goal is to get and display the month name from any given date. There are several ways to go about this in Excel, depending on whether you want to extract the month name as text, or just display a valid Excel using the month name. To extract the month name from a date as text ,...

[![Excel formula: Convert date to Julian format](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20Julian%20format.png "Excel formula: Convert date to Julian format")](https://exceljet.net/formulas/convert-date-to-julian-format)

### [Convert date to Julian format](https://exceljet.net/formulas/convert-date-to-julian-format)

This formula builds the final result in 2 parts, joined by concatenation with the ampersand (...

[![Excel formula: Pad week numbers with zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/pad%20week%20numbers%20with%20zeros.png "Excel formula: Pad week numbers with zeros")](https://exceljet.net/formulas/pad-week-numbers-with-zeros)

### [Pad week numbers with zeros](https://exceljet.net/formulas/pad-week-numbers-with-zeros)

The TEXT function can apply number formats of any kind, including currency, date, percentage, etc. By applying a number format like "00", "000", "0000", you can "pad" numbers with as many zeros as you like. Zeros will only be added where needed. Number format only The TEXT function converts numbers...

Related functions
-----------------

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

### Formulas

*   [Convert text to numbers](https://exceljet.net/formulas/convert-text-to-numbers)
    
*   [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)
    
*   [Convert date to Julian format](https://exceljet.net/formulas/convert-date-to-julian-format)
    
*   [Pad week numbers with zeros](https://exceljet.net/formulas/pad-week-numbers-with-zeros)
    

### Functions

*   [TEXT Function](https://exceljet.net/functions/text-function)
    

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