# Get first entry by month and year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-first-entry-by-month-and-year

---

[Skip to main content](https://exceljet.net/formulas/get-first-entry-by-month-and-year#main-content)

[](https://exceljet.net/formulas/get-first-entry-by-month-and-year#)

*   [Previous](https://exceljet.net/formulas/get-date-associated-with-last-entry)
    
*   [Next](https://exceljet.net/formulas/get-last-entry-by-month-and-year)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Get first entry by month and year
=================================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Get first entry by month and year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get_first_entry_by_month_and_year.png "Excel formula: Get first entry by month and year")

Summary
-------

To look up the first entry in a table by month and year, you can use a formula based on the [INDEX](https://exceljet.net/functions/index-function)
, [MATCH](https://exceljet.net/functions/xmatch-function)
, and [TEXT](https://exceljet.net/functions/text-function)
 functions. In the example shown, the formula in F5 is:

    =INDEX(entry,MATCH(TRUE,TEXT(date,"mmyy")=TEXT(E5,"mmyy"),0))
    

where "entry" is the [named range](https://exceljet.net/glossary/named-range)
 C5:C16, "date" is the named range B5:B16, and cell E5 contains a valid date formatted with the custom format "mmm".

_This is an array formula, and must be entered with control + shift + enter in Excel 2019 and earlier._

Generic formula
---------------

    =INDEX(entry,MATCH(TRUE,TEXT(date,"mmyy")=TEXT(A1,"mmyy"),0))

Explanation 
------------

> Note: the values in E5:E8 are actual dates, formatted with the [custom number format](https://exceljet.net/articles/custom-number-formats)
>  "mmm".

Working from the inside out, the expression:

    MATCH(TRUE,TEXT(date,"mmyy")=TEXT(E5,"mmyy")
    

uses the TEXT function to generate an array of strings in the format "mmyy":

    {"0117";"0117";"0117";"0217";"0217";"0217";"0317";"0317";"0317"}

which are compared to a single string based on the value in E5, "0117". The result is an array of TRUE / FALSE values:

    {TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}

This array is fed into the MATCH function as the _lookup\_array_, with a _lookup\_value_ of TRUE, and a _match\_type_ of zero for exact match. In exact match mode, the MATCH function returns the position of the first TRUE in the array, which is 1 in the formula in F5. This position goes into INDEX as the row number, with an array based on the named range "entry":

    =INDEX(entry,1)
    

Finally, INDEX returns the item inside **entry** as a final result.

Note: if an entry isn't found for a given month and year, this formula will return #N/A.

### Get the first entry based on today's date

To get the first entry for a given month and year based on today's date, you can adapt the formula to use the TODAY function instead of the value in E5:

    {=INDEX(entry,MATCH(TRUE,TEXT(date,"mmyy")=TEXT(TODAY(),"mmyy"),0))}
    

Related formulas
----------------

[![Excel formula: Get last entry by month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20last%20entry%20by%20month%20and%20year.png "Excel formula: Get last entry by month and year")](https://exceljet.net/formulas/get-last-entry-by-month-and-year)

### [Get last entry by month and year](https://exceljet.net/formulas/get-last-entry-by-month-and-year)

Note: the lookup\_value of 2 is deliberately larger than any values in the lookup\_vector, following the concept of bignum . Working from the inside out, the expression: (TEXT($B$5:$B$13,"mmyy")=TEXT(E5,"mmyy")) generates strings like "0117" using the values in column B and E, which are then compared...

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

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

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

*   [Get last entry by month and year](https://exceljet.net/formulas/get-last-entry-by-month-and-year)
    
*   [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
    
*   [Get date associated with last entry](https://exceljet.net/formulas/get-date-associated-with-last-entry)
    
*   [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)
    
*   [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)
    
*   [Last row in numeric data](https://exceljet.net/formulas/last-row-in-numeric-data)
    
*   [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
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