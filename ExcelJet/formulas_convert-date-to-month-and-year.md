# Convert date to month and year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-date-to-month-and-year

---

[Skip to main content](https://exceljet.net/formulas/convert-date-to-month-and-year#main-content)

[](https://exceljet.net/formulas/convert-date-to-month-and-year#)

*   [Previous](https://exceljet.net/formulas/convert-date-to-julian-format)
    
*   [Next](https://exceljet.net/formulas/convert-date-to-text)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert date to month and year
==============================

by Dave Bruns · Updated 20 Jun 2016

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Convert date to month and year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20date%20to%20month%20and%20year.png "Excel formula: Convert date to month and year")

Summary
-------

To convert a normal Excel date into yyyymm format (e.g. 9/1/2017 > 201709), you can use the TEXT function.

In the example shown, the formula in C6 is:

    =TEXT(B6,"yyyymm")
    

Generic formula
---------------

    =TEXT(date,"yyyymm")

Explanation 
------------

The TEXT function applies the number format you specify to a numeric value, and returns a result as text.

In this case, the number format provided is "yyyymm", which joins a 4-digit year with a 2-digit month value.

### Display only option

If you only want to _display_ a date with the year and month, you can simply apply the custom number format "yyyymm" to the date(s). This will cause Excel to display the year and month together, but will not change the underlying date.

Related formulas
----------------

[![Excel formula: Convert date to Julian format](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20Julian%20format.png "Excel formula: Convert date to Julian format")](https://exceljet.net/formulas/convert-date-to-julian-format)

### [Convert date to Julian format](https://exceljet.net/formulas/convert-date-to-julian-format)

This formula builds the final result in 2 parts, joined by concatenation with the ampersand (...

[![Excel formula: Convert date to text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20text.png "Excel formula: Convert date to text")](https://exceljet.net/formulas/convert-date-to-text)

### [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)

Dates and times in Excel are stored as serial numbers and converted to human-readable values on the fly using number formats. When you enter a date in Excel, you can apply a number format to display that date as you like. Similarly, the TEXT function allows you to convert a date or time into text...

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

*   [Convert date to Julian format](https://exceljet.net/formulas/convert-date-to-julian-format)
    
*   [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)
    

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