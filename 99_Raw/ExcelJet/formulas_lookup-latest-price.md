# Lookup latest price - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lookup-latest-price

---

[Skip to main content](https://exceljet.net/formulas/lookup-latest-price#main-content)

[](https://exceljet.net/formulas/lookup-latest-price#)

*   [Previous](https://exceljet.net/formulas/lookup-last-file-version)
    
*   [Next](https://exceljet.net/formulas/lookup-lowest-monday-tide)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Lookup latest price
===================

by Dave Bruns · Updated 26 May 2020

Related functions 
------------------

[LOOKUP](https://exceljet.net/functions/lookup-function)

![Excel formula: Lookup latest price](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Lookup%20latest%20price.png "Excel formula: Lookup latest price")

Summary
-------

To lookup the latest price for a product in a list, sorted so latest items appear last, you can use a formula based on the [LOOKUP function](https://exceljet.net/functions/lookup-function)
. In the example show, the formula in G7 is:

    =LOOKUP(2,1/(item=F7),price)
    

where **item** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B12, **price** is the named range D5:D12, and data is sorted ascending by date.

Generic formula
---------------

    =LOOKUP(2,1/(item="hat"),price)

Explanation 
------------

The LOOKUP function assumes data is sorted, and always does an approximate match. If the lookup value is greater than all values in the lookup array, default behavior is to "fall back" to the previous value. This formula exploits this behavior by creating an array that contains only 1s and errors, then deliberately looking for the value 2, which will never be found.

First, this expression is evaluated:

    item=F7
    

When F7 contains "sandals" the result is an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values like this:

    {FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE}
    

This array is provided as the divisor to 1:

    1/{FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE}
    

The math operation automatically coerces the TRUE and FALSE values to 1s and 0s, so the result is another array like this:

    {#DIV/0!;1;#DIV/0!;1;#DIV/0!;#DIV/0!;1;#DIV/0!}
    

returned directly to the LOOKUP function as the lookup vector argument.

Notice the array contains only two unique values: the divide by zero error (#DIV/0!) and the number 1.

LOOKUP searches the array for the value 2, ignoring the error values. Not finding 2, it falls back to the last 1, at position 7 in the lookup vector. LOOKUP then returns the 7th item in the result vector (the named range "price"), the value 15.

To read more about the concept of intentionally looking for a value that won't ever appear, read about [BigNum](https://exceljet.net/glossary/bignum)
.

Related formulas
----------------

[![Excel formula: Get date associated with last entry](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20date%20associated%20with%20last%20entry.png "Excel formula: Get date associated with last entry")](https://exceljet.net/formulas/get-date-associated-with-last-entry)

### [Get date associated with last entry](https://exceljet.net/formulas/get-date-associated-with-last-entry)

Working from the inside out, the expression C5:G5<>"" returns an array of true and false values: {FALSE,TRUE,FALSE,FALSE,FALSE} The number 1 is divided by this array, which creates a new array composed of either 1's or #DIV/0! errors: {#DIV/0!,1,#DIV/0!,#DIV/0!,#DIV/0!} This array is used as...

[![Excel formula: Get value of last non-empty cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_value_of_last_non-empty_cell.png "Excel formula: Get value of last non-empty cell")](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

### [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

In this example, the goal is to get the last value in column B, even when data may contain empty cells. A secondary goal is to get the corresponding value in column C. This is useful for analyzing datasets where the most recent or last entry is significant. In the current version of Excel, a good...

[![Excel formula: Get information about max value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_information_corresponding_to_max_value.png "Excel formula: Get information about max value")](https://exceljet.net/formulas/get-information-about-max-value)

### [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)

An interesting problem in Excel is how to look up information related to the maximum value in a set of data. For example, if you have a dataset of property listings and prices, you might want to find details about the property with the highest price. The best way to solve this problem depends on...

[![Excel formula: XLOOKUP latest by date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20latest%20by%20date.png "Excel formula: XLOOKUP latest by date")](https://exceljet.net/formulas/xlookup-latest-by-date)

### [XLOOKUP latest by date](https://exceljet.net/formulas/xlookup-latest-by-date)

XLOOKUP offers several features that make it exceptionally good for more complicated lookups. In this example, we want the latest price for an item by date . If data were sorted by date in ascending order, this would be very straightforward . However, in this case, data is unsorted . By default,...

Related functions
-----------------

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get date associated with last entry](https://exceljet.net/formulas/get-date-associated-with-last-entry)
    
*   [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
    
*   [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)
    
*   [XLOOKUP latest by date](https://exceljet.net/formulas/xlookup-latest-by-date)
    

### Functions

*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    

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