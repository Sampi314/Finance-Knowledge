# Count day of week between dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-day-of-week-between-dates

---

[Skip to main content](https://exceljet.net/formulas/count-day-of-week-between-dates#main-content)

[](https://exceljet.net/formulas/count-day-of-week-between-dates#)

*   [Previous](https://exceljet.net/formulas/count-dates-in-current-month)
    
*   [Next](https://exceljet.net/formulas/count-holidays-between-two-dates)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Count day of week between dates
===============================

by Dave Bruns · Updated 21 Feb 2020

Related functions 
------------------

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[ROW](https://exceljet.net/functions/row-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

![Excel formula: Count day of week between dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20day%20of%20week%20between%20dates.png "Excel formula: Count day of week between dates")

Summary
-------

To count weekdays (Mondays, Fridays, Sundays, etc.) between two dates you can use an array formula that uses several functions: SUMPRODUCT, WEEKDAY, ROW, and INDIRECT. In the example shown, the formula in cell E6 is

    =SUMPRODUCT(--(WEEKDAY(ROW(INDIRECT(B6&":"&C6)))=D6))
    

In the generic version of the formula, **start** = start date, **end** = end date, and **dow** = day of week.

Generic formula
---------------

    =SUMPRODUCT(--(WEEKDAY(ROW(INDIRECT(start&":"&end)))=dow))

Explanation 
------------

At the core, this formula uses the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
 to test a number of dates to see if they land on a given day of week (dow) and the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to tally up the total.

When given a date, WEEKDAY simply returns a number between 1 and 7 that corresponds to a particular day of the week. With default settings, 1 = Sunday and 7 = Saturday. So, 2 = Monday, 6 = Friday, and so on.

The trick to this formula is understanding that [dates in Excel are just serial numbers](https://exceljet.net/glossary/excel-date)
 that begin on Jan 1, 1900. For example, January 1, 2016 is the serial number 42370, and January 8 is 42377. Dates in Excel only look like dates when a date number format is applied.

So, the question becomes - how can you construct an [array](https://exceljet.net/glossary/array)
 of dates that you can feed into the WEEKDAY function to find out corresponding days of week?

The answer is to use [ROW](https://exceljet.net/functions/row-function)
 with [INDIRECT](https://exceljet.net/functions/indirect-function)
 functions like so:

    ROW(INDIRECT(date1&":"&date2))
    

INDIRECT allows the concatenated dates "42370:42377" to be interpreted as row numbers. Then the ROW function returns an array like this:

    {42370;42371;42372;42373;42374;42375;42376;42377}
    

The WEEKDAY function evaluates these numbers _as dates_ and returns this array:

    {6;7;1;2;3;4;5;6}
    

which is tested against the given day of week (6 in this case, from D6). Once the results of the test are converted to 1s and 0s with the double hyphen, this array is processed by SUMPRODUCT:

    {1;0;0;0;0;0;0;1}
    

Which returns 2.

### With SEQUENCE

With the new [SEQUENCE function](https://exceljet.net/functions/sequence-function)
, this formula can simplified somewhat like this:

    =SUMPRODUCT(--(WEEKDAY(SEQUENCE(end-start+1,1,start,1))=dow))
    

In this version, we use SEQUENCE to generate the array of dates directly, with no need for INDIRECT or ROW.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: Count dates by day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20dates%20by%20day%20of%20week.png "Excel formula: Count dates by day of week")](https://exceljet.net/formulas/count-dates-by-day-of-week)

### [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)

You might wonder why we aren't using COUNTIF or COUNTIFS . These functions seem like the obvious solution. However, without adding a helper column that contains a weekday value, there is no way to create criteria for COUNTIF to count weekdays in a range of dates. Instead, we use the versatile...

[![Excel formula: Sum by weekday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20weekday.png "Excel formula: Sum by weekday")](https://exceljet.net/formulas/sum-by-weekday)

### [Sum by weekday](https://exceljet.net/formulas/sum-by-weekday)

In this example, the goal is to sum amounts by weekday. In other words, we want to sum amounts by Monday, Tuesday, Wednesday, and so on. Column B contains valid Excel dates formatted with a custom number format explained below. For convenience, all source data is in an Excel Table named data . The...

Related functions
-----------------

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

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
    
*   [Sum by weekday](https://exceljet.net/formulas/sum-by-weekday)
    

### Functions

*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    

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