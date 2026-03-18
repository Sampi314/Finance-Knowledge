# Sum by weekday - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-by-weekday

---

[Skip to main content](https://exceljet.net/formulas/sum-by-weekday#main-content)

[](https://exceljet.net/formulas/sum-by-weekday#)

*   [Previous](https://exceljet.net/formulas/sum-by-week-number)
    
*   [Next](https://exceljet.net/formulas/sum-by-year)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum by weekday
==============

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[TEXT](https://exceljet.net/functions/text-function)

[WEEKDAY](https://exceljet.net/functions/weekday-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7489/download?token=Z_h_TPW8)
 (15.73 KB)

![Excel formula: Sum by weekday](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20by%20weekday.png "Excel formula: Sum by weekday")

Summary
-------

To sum values by day of week, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 together with the [TEXT function](https://exceljet.net/functions/text-function)
. In the example shown, the formula in F5 is:

    =SUMPRODUCT((TEXT(data[Date],"ddd")=E5)*(data[Amount]))
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:C16. As the formula is copied down, the formula returns a sum for each day of the week in column E.

Generic formula
---------------

    =SUMPRODUCT((TEXT(dates,"ddd")=A1)*(amounts))

Explanation 
------------

In this example, the goal is to sum amounts by weekday. In other words, we want to sum amounts by Monday, Tuesday, Wednesday, and so on. Column B contains valid [Excel dates](https://exceljet.net/glossary/excel-date)
 formatted with a custom number format explained below. For convenience, all source data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data**. The values in E5:E11 are hardcoded [text values](https://exceljet.net/glossary/text-value)
. A nice way to solve this problem is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 together with the [TEXT function](https://exceljet.net/functions/text-function)
. The SUMIFS function is not a good fit here for reasons explained below.

### Why not SUMIFS?

You might wonder why we aren't using the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 to solve this problem? The reason is that [SUMIFS is in a group of eight functions](https://exceljet.net/articles/excels-racon-functions)
 that _requires_ a [range](https://exceljet.net/glossary/range)
 for the _criteria\_range_ argument; it is not possible to provide an [array](https://exceljet.net/glossary/array)
 instead. This means we can't extract a day of week value from the date in column B and feed that into SUMIFS as a _range_ argument, unless we add a [helper column](https://exceljet.net/glossary/helper-column)
 to the source data.

### Custom number format

The dates in column B are formatted with a custom [number format](https://exceljet.net/glossary/number-format)
 to show an abbreviated day of week at the start:

    ddd dd-mmm-yy
    

This formatting is not required by the formula, but adding the day of week makes it easier to check results. You can read more about Excel's custom number formats [here](https://exceljet.net/articles/custom-number-formats)
.

### SUMPRODUCT with TEXT

In the worksheet shown, the solution is based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 together with the TEXT function. The formula in cell F5 is:

    =SUMPRODUCT((TEXT(data[Date],"ddd")=E5)*(data[Amount]))
    

Working from the inside out, the [TEXT function](https://exceljet.net/functions/text-function)
 is used to extract a 3-letter abbreviation for each day of the week like this:

    TEXT(data[Date],"ddd")
    

Because **data\[Date\]** contains 12 dates, the TEXT function returns 12 values in an [array](https://exceljet.net/glossary/array)
 like this:

    {"Thu";"Sat";"Wed";"Mon";"Tue";"Tue";"Thu";"Tue";"Sun";"Fri";"Wed";"Mon"}
    

This array is compared against the value in cell E5 ("Mon") which results in an array of 12 TRUE and FALSE values:

    {FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE}
    

In this array, TRUE represents dates that are Monday, and FALSE represents dates that are other days of the week. In the next step, the array above is multiplied by **data\[Amount\]**, which contains numeric values. This math operation coerces the TRUE and FALSE values to 1s and 0s, so we can visualize the operation like this:

    ={0;0;0;1;0;0;0;0;0;0;0;1}*(data[Amount])
    ={0;0;0;275;0;0;0;0;0;0;0;150}
    

Essentially, the array from the TEXT function acts like a filter: only amounts that correspond to 1 survive the operation, the rest of the amounts are "zeroed out". All of this happens inside the SUMPRODUCT function, which receives the final array:

    =SUMPRODUCT({0;0;0;275;0;0;0;0;0;0;0;150}) // returns 425
    

With just one array to process, the SUMPRODUCT function sums the array and returns the final result, 425. As the formula is copied down the column, we get a subtotal for each day listed in E5:E11.

_Note: the reason we use the SUMPRODUCT function in this formula and not the [SUM function](https://exceljet.net/functions/sum-function)
 is that [SUMPRODUCT will work in all versions of Excel](https://exceljet.net/articles/why-sumproduct)
 without special handling. In the [current version of Excel](https://exceljet.net/glossary/dynamic-excel)
, the SUM function will also work as a replacement for SUMPRODUCT. In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, the SUM function must be entered as an [array formula](https://exceljet.net/glossary/array-formula)
 with control + shift + enter._ 

### SUMPRODUCT with WEEKDAY

Another way to approach this problem is to use the SUMPRODUCT function with the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
 like this:

    =SUMPRODUCT((WEEKDAY(dates)=day_num)*values)
    

The WEEKDAY function returns a numeric value for each day of the week. The challenge with this approach is that it's more cryptic: you have to know what number corresponds to each day of the week. [This page](https://exceljet.net/functions/weekday-function)
 provides details on how WEEKDAY operates.

Related formulas
----------------

[![Excel formula: Count dates by day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20dates%20by%20day%20of%20week.png "Excel formula: Count dates by day of week")](https://exceljet.net/formulas/count-dates-by-day-of-week)

### [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)

You might wonder why we aren't using COUNTIF or COUNTIFS . These functions seem like the obvious solution. However, without adding a helper column that contains a weekday value, there is no way to create criteria for COUNTIF to count weekdays in a range of dates. Instead, we use the versatile...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    

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