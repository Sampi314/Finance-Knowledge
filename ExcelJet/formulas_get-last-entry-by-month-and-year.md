# Get last entry by month and year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-last-entry-by-month-and-year

---

[Skip to main content](https://exceljet.net/formulas/get-last-entry-by-month-and-year#main-content)

[](https://exceljet.net/formulas/get-last-entry-by-month-and-year#)

*   [Previous](https://exceljet.net/formulas/get-first-entry-by-month-and-year)
    
*   [Next](https://exceljet.net/formulas/get-pivot-table-grand-total)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Get last entry by month and year
================================

by Dave Bruns · Updated 11 Oct 2017

Related functions 
------------------

[LOOKUP](https://exceljet.net/functions/lookup-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Get last entry by month and year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20last%20entry%20by%20month%20and%20year.png "Excel formula: Get last entry by month and year")

Summary
-------

To lookup the last entry in a table by month and year, you can use the LOOKUP function with the TEXT function. In the example shown, the formula in F5 is:

    =LOOKUP(2,1/(TEXT($B$5:$B$13,"mmyy")=TEXT(E5,"mmyy")),$C$5:$C$13)
    

where B5:B13 and E5:E7 contain valid dates, and C5:C13 contains amounts.

Generic formula
---------------

    =LOOKUP(2,1/(TEXT(dates,"mmyy")=TEXT(A1,"mmyy")),values)

Explanation 
------------

_Note: the lookup\_value of 2 is deliberately larger than any values in the lookup\_vector, following the [concept of bignum](https://exceljet.net/glossary/bignum)
._

Working from the inside out, the expression:

    (TEXT($B$5:$B$13,"mmyy")=TEXT(E5,"mmyy"))
    

generates strings like "0117" using the values in column B and E, which are then compared to each other. The result is an array like this:

    {TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

where TRUE represents dates in the same month and year. The number 1 is then divided by this array. The result is an array of either 1's or divide by zero errors (#DIV/0!):

    {1;1;1;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!}
    

which goes into LOOKUP as the lookup array. LOOKUP assumes data is sorted in ascending order and always does an approximate match. When the lookup value of 2 can't be found, LOOKUP will match the previous value, so lookup will match the last 1 in the array.

Finally, LOOKUP returns the corresponding value in result\_vector, which contains the amounts in C5:C13.

Related formulas
----------------

[![Excel formula: Get first entry by month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_first_entry_by_month_and_year.png "Excel formula: Get first entry by month and year")](https://exceljet.net/formulas/get-first-entry-by-month-and-year)

### [Get first entry by month and year](https://exceljet.net/formulas/get-first-entry-by-month-and-year)

Note: the values in E5:E8 are actual dates, formatted with the custom number format "mmm". Working from the inside out, the expression: MATCH(TRUE,TEXT(date,"mmyy")=TEXT(E5,"mmyy") uses the TEXT function to generate an array of strings in the format "mmyy": {"0117";"0117";"0117";"0217";"0217";"0217...

[![Excel formula: Get value of last non-empty cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_value_of_last_non-empty_cell.png "Excel formula: Get value of last non-empty cell")](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

### [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

In this example, the goal is to get the last value in column B, even when data may contain empty cells. A secondary goal is to get the corresponding value in column C. This is useful for analyzing datasets where the most recent or last entry is significant. In the current version of Excel, a good...

[![Excel formula: Get date associated with last entry](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20date%20associated%20with%20last%20entry.png "Excel formula: Get date associated with last entry")](https://exceljet.net/formulas/get-date-associated-with-last-entry)

### [Get date associated with last entry](https://exceljet.net/formulas/get-date-associated-with-last-entry)

Working from the inside out, the expression C5:G5<>"" returns an array of true and false values: {FALSE,TRUE,FALSE,FALSE,FALSE} The number 1 is divided by this array, which creates a new array composed of either 1's or #DIV/0! errors: {#DIV/0!,1,#DIV/0!,#DIV/0!,#DIV/0!} This array is used as...

[![Excel formula: Get first non-blank value in a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_non-blank_value_in_a_list.png "Excel formula: Get first non-blank value in a list")](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

### [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

The gist of this problem is that we want to get the first non-blank cell, but we don't have a direct way to do that in Excel. The easiest way to solve this problem is with the XLOOKUP function. XLOOKUP function The XLOOKUP function is a modern upgrade to the VLOOKUP function. XLOOKUP is very...

[![Excel formula: Lookup latest price](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Lookup%20latest%20price.png "Excel formula: Lookup latest price")](https://exceljet.net/formulas/lookup-latest-price)

### [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)

The LOOKUP function assumes data is sorted, and always does an approximate match. If the lookup value is greater than all values in the lookup array, default behavior is to "fall back" to the previous value. This formula exploits this behavior by creating an array that contains only 1s and errors,...

[![Excel formula: Last row in numeric data](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Last%20row%20in%20numeric%20data.png "Excel formula: Last row in numeric data")](https://exceljet.net/formulas/last-row-in-numeric-data)

### [Last row in numeric data](https://exceljet.net/formulas/last-row-in-numeric-data)

When building advanced formulas that use dynamic ranges, it's often necessary to figure out the last location of data in a list. Depending on the data, this could be the last row with data, the last column with data, or the intersection of both. Note: we want the last \*relative position\* inside a...

[![Excel formula: Last row in text data](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Last%20row%20in%20text%20data.png "Excel formula: Last row in text data")](https://exceljet.net/formulas/last-row-in-text-data)

### [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)

This formula uses the MATCH function in approximate match mode to locate the last text value in a range. Approximate match enabled by setting by the 3rd argument in MATCH to 1, or omitting this argument, which defaults to 1. The lookup value is a so-called "big text" (sometimes abbreviated "bigtext...

Related functions
-----------------

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

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

*   [Get first entry by month and year](https://exceljet.net/formulas/get-first-entry-by-month-and-year)
    
*   [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
    
*   [Get date associated with last entry](https://exceljet.net/formulas/get-date-associated-with-last-entry)
    
*   [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)
    
*   [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)
    
*   [Last row in numeric data](https://exceljet.net/formulas/last-row-in-numeric-data)
    
*   [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)
    

### Functions

*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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