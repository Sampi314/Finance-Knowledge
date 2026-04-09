# Range contains specific date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/range-contains-specific-date

---

[Skip to main content](https://exceljet.net/formulas/range-contains-specific-date#main-content)

[](https://exceljet.net/formulas/range-contains-specific-date#)

*   [Previous](https://exceljet.net/formulas/range-contains-numbers)
    
*   [Next](https://exceljet.net/formulas/row-is-blank)
    

[Range](https://exceljet.net/formulas#Range)

Range contains specific date
============================

by Dave Bruns · Updated 21 Apr 2020

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[DATE](https://exceljet.net/functions/date-function)

[TODAY](https://exceljet.net/functions/today-function)

![Excel formula: Range contains specific date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/range%20contains%20specific%20date2.png "Excel formula: Range contains specific date")

Summary
-------

To test if a range contains a specific date, you can use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. In the example shown, the formula in F5, copied down, is:

    =COUNTIFS(dates,E5)>0
    

where **dates** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16

Generic formula
---------------

    =COUNTIFS(range,date)>0

Explanation 
------------

First, it's important to note first that [Excel dates are simply large serial numbers](https://exceljet.net/glossary/excel-date)
. When we check for a date with a formula, we are looking for a specific large number, _not text_.

This formula is a basic example of using the COUNTIFS function with just one condition. The named range **dates** is supplied as the first argument, and the date in column E is supplied as the second argument for the condition:

    =COUNTIFS(dates,E5)
    

With the date 13-Jun-2020 in cell E5, the COUNTIFS function returns 1, so the formula then simplifies to:

    =1>0
    

which returns TRUE.

By checking if the result from COUNTIFS is greater than zero, we also handle cases where the count is greater than 1 (i.e. the date we are looking for appears more than once), as in cell E7. Any positive result will cause the formula to return TRUE. When COUNTIFS returns a count of zero, the formula will return FALSE.

### With a hardcoded date

The best way to hardcode a date into this formula is to use the DATE function like this:

    =COUNTIFS(dates,DATE(2020,6,13))>0
    

The [DATE function](https://exceljet.net/functions/date-function)
 ensures that the correct date is passed into COUNTIFS, without requiring Excel to interpret a date in text format.

### Check for today's date

To check for today's date, use the [TODAY function](https://exceljet.net/functions/today-function)
 like this:

    =COUNTIFS(dates,TODAY())>0
    

_Note: the TODAY function will continually update as time passes._

### With IF

You can [nest](https://exceljet.net/glossary/nesting)
 this formula inside the [IF function](https://exceljet.net/functions/if-function)
 as the logical test. For example, to return a final result of "Yes" or "No", you can use IF like this:

    =IF(COUNTIFS(dates,E5),"Yes","No")
    

Related formulas
----------------

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

[![Excel formula: Range contains one of many values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20one%20of%20many%20values.png "Excel formula: Range contains one of many values")](https://exceljet.net/formulas/range-contains-one-of-many-values)

### [Range contains one of many values](https://exceljet.net/formulas/range-contains-one-of-many-values)

Each item in rng is compared to each item in values and the result is an array of TRUE or FALSE values. The double negative will force the TRUE and FALSE values to 1 and 0 respectively. Since SUMPRODUCT receives just one array, it simply adds up the items in the array and returns the result...

[![Excel formula: Range contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20specific%20text.png "Excel formula: Range contains specific text")](https://exceljet.net/formulas/range-contains-specific-text)

### [Range contains specific text](https://exceljet.net/formulas/range-contains-specific-text)

The COUNTIF function counts cells that meet supplied criteria, and returns a count of occurrences found. If no cells meet criteria, COUNTIF returns zero. The asterisk (\*) is a wildcard for one or more characters. By concatenating asterisks before and after the value in D5, the formula will count...

[![Excel formula: Range contains one of many substrings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20one%20of%20many%20substrings.png "Excel formula: Range contains one of many substrings")](https://exceljet.net/formulas/range-contains-one-of-many-substrings)

### [Range contains one of many substrings](https://exceljet.net/formulas/range-contains-one-of-many-substrings)

All the hard work is done by the COUNTIF function, which is configured to count the values in the named range "substrings" that appear the named range "rng" with like this: COUNTIF(rng,"\*"&substrings&"\*")) By wrapping substrings in the asterisks, Excel evaluates the formula like this: =...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

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

*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    
*   [Range contains one of many values](https://exceljet.net/formulas/range-contains-one-of-many-values)
    
*   [Range contains specific text](https://exceljet.net/formulas/range-contains-specific-text)
    
*   [Range contains one of many substrings](https://exceljet.net/formulas/range-contains-one-of-many-substrings)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    

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