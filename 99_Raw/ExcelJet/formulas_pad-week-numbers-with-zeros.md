# Pad week numbers with zeros - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/pad-week-numbers-with-zeros

---

[Skip to main content](https://exceljet.net/formulas/pad-week-numbers-with-zeros#main-content)

[](https://exceljet.net/formulas/pad-week-numbers-with-zeros#)

*   [Previous](https://exceljet.net/formulas/next-working-day)
    
*   [Next](https://exceljet.net/formulas/parse-time-string-to-time)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Pad week numbers with zeros
===========================

by Dave Bruns · Updated 23 Feb 2016

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

[WEEKNUM](https://exceljet.net/functions/weeknum-function)

![Excel formula: Pad week numbers with zeros](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/pad%20week%20numbers%20with%20zeros.png "Excel formula: Pad week numbers with zeros")

Summary
-------

To pad week numbers (or any number) with zeros using a formula, you can use the TEXT function.

In the example show, D5 contains this formula:

    =TEXT(WEEKNUM(B5,21),"00")
    

Which returns the string "07".

Generic formula
---------------

    =TEXT(WEEKNUM(date,type),"00")

Explanation 
------------

The TEXT function can apply number formats of any kind, including currency, date, percentage, etc. By applying a number format like "00", "000", "0000", you can "pad" numbers with as many zeros as you like. Zeros will only be added where needed.

### Number format only

The TEXT function converts numbers to text as a normal step in applying the number format.

If you are concatenating (joining) the result to another text string, this is fine, but if you just want to apply visual padding to a free-standing number set of numbers, you can apply a custom number format without using a formula.

Related formulas
----------------

[![Excel formula: Get week number from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20week%20number%20from%20date.png "Excel formula: Get week number from date")](https://exceljet.net/formulas/get-week-number-from-date)

### [Get week number from date](https://exceljet.net/formulas/get-week-number-from-date)

The WEEKNUM function takes a date and returns a week number (1-54) that corresponds to the week of year. The WEEKNUM function starts counting with the week that contains January 1. WEEKNUM takes two arguments: a date , and (optionally) return\_type , which controls the scheme used to calculate the...

Related functions
-----------------

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel WEEKNUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weeknum%20function.png "Excel WEEKNUM function")](https://exceljet.net/functions/weeknum-function)

### [WEEKNUM Function](https://exceljet.net/functions/weeknum-function)

The Excel WEEKNUM function takes a date and returns a week number (1-54) that corresponds to the week of year. The WEEKNUM function starts counting on the week that contains January 1. By default, weeks begin on Sunday, but this can be changed.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get week number from date](https://exceljet.net/formulas/get-week-number-from-date)
    

### Functions

*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [WEEKNUM Function](https://exceljet.net/functions/weeknum-function)
    

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