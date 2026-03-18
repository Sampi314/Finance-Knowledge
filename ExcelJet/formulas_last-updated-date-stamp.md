# Last updated date stamp - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/last-updated-date-stamp

---

[Skip to main content](https://exceljet.net/formulas/last-updated-date-stamp#main-content)

[](https://exceljet.net/formulas/last-updated-date-stamp#)

*   [Previous](https://exceljet.net/formulas/last-n-weeks)
    
*   [Next](https://exceljet.net/formulas/list-holidays-between-two-dates)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Last updated date stamp
=======================

by Dave Bruns · Updated 1 Oct 2019

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

[TODAY](https://exceljet.net/functions/today-function)

![Excel formula: Last updated date stamp](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/date%20last%20updated.png "Excel formula: Last updated date stamp")

Summary
-------

To add a date stamp in a workbook to indicate a "date last updated", you can use the TEXT function. In the example shown, the formula in C5 is:

    ="Last update: "& TEXT(B5, "ddd, mmmm d, yyyy")
    

Generic formula
---------------

    ="Last update: "& TEXT(A1, "ddd, mmmm d, yyyy")

Explanation 
------------

The [TEXT function](https://exceljet.net/functions/text-function)
 can apply [number formatting](https://exceljet.net/articles/custom-number-formats)
 to numbers just like Excel's built-in cell formats for dates, currency, fractions, and so on. However, unlike Excel's cell formatting, the TEXT function works inside a formula and returns a result that is text.

You can use TEXT to format numbers that appear inside other text strings. In this case, we concatenate the text "Last update" with the result provided by the TEXT function, which picks up a date from column B and formats it using the supplied number format.

You can embed the date in any format you like, using the codes that represent date formats (dd, mm ,yyyy, etc.)

### With a named range

One convenient way to manage a "last updated" message in a large workbook is to use a [named range](https://exceljet.net/articles/named-ranges)
 to hold the date last updated, then refer to that named range in formulas elsewhere to display a last update message.

For example, you can name a cell something like "last\_update", and use that cell to enter the date last updated. Once you've defined the named range, you can use the formula below anywhere you like to display the same message:

    ="Updated: "& TEXT(last_update, "ddd, mmmm d, yyyy")
    

Whenever you change the date value in the named range, all formulas will update instantly, and all date stamps will stay in sync.

### With current date

To embed the current date in a string, you can use the [TODAY function](https://exceljet.net/functions/today-function)
 like this:

    ="Current date: "& TEXT(TODAY(), "ddd, mmmm d, yyyy")
    

Related formulas
----------------

[![Excel formula: Convert date to text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20text.png "Excel formula: Convert date to text")](https://exceljet.net/formulas/convert-date-to-text)

### [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)

Dates and times in Excel are stored as serial numbers and converted to human-readable values on the fly using number formats. When you enter a date in Excel, you can apply a number format to display that date as you like. Similarly, the TEXT function allows you to convert a date or time into text...

[![Excel formula: Convert numbers to text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20numbers%20to%20text.png "Excel formula: Convert numbers to text")](https://exceljet.net/formulas/convert-numbers-to-text)

### [Convert numbers to text](https://exceljet.net/formulas/convert-numbers-to-text)

Normally, you want to maintain numeric values in Excel, because they can be used in formulas that perform numeric calculations. However, there are situations where converting numbers to text makes sense. One example is when you want to concatenate (join) a formatted number to text. For example, "...

Related functions
-----------------

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)
    
*   [Convert numbers to text](https://exceljet.net/formulas/convert-numbers-to-text)
    

### Functions

*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    

### Articles

*   [Excel custom number formats](https://exceljet.net/articles/custom-number-formats)
    

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