# Sequence of times - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sequence-of-times

---

[Skip to main content](https://exceljet.net/formulas/sequence-of-times#main-content)

[](https://exceljet.net/formulas/sequence-of-times#)

*   [Previous](https://exceljet.net/formulas/sequence-of-months)
    
*   [Next](https://exceljet.net/formulas/sequence-of-weekends)
    

[Date series](https://exceljet.net/formulas#Date-series)

Sequence of times
=================

by Dave Bruns · Updated 15 Jul 2023

Related functions 
------------------

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[TIME](https://exceljet.net/functions/time-function)

![Excel formula: Sequence of times](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sequence%20of%20time.png "Excel formula: Sequence of times")

Summary
-------

To generate a sequence of times, you can use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
, in combination with functions like [TIME](https://exceljet.net/functions/time-function)
, [HOUR](https://exceljet.net/functions/hour-function)
, [MINUTE](https://exceljet.net/functions/minute-function)
, and [SECOND](https://exceljet.net/functions/second-function)
. Or you can use SEQUENCE with raw numeric values that represent time. In the example shown, the formula in D5 is:

    =TIME(SEQUENCE(12,1,HOUR(B5),1),0,0)
    

which generates a series of 12 times, beginning at 7:00 AM, the date in B5.

Generic formula
---------------

    =TIME(SEQUENCE(n,1,HOUR(start),1),0,0)

Explanation 
------------

The SEQUENCE function is a dynamic array function that can generate multiple results. When used by itself on the worksheet, SEQUENCE outputs an array of results that "[spill](https://exceljet.net/glossary/spill)
" onto the worksheet in a "[spill range](https://exceljet.net/glossary/spill-range)
".

In the example shown, we want to generate 12 times, one hour apart, starting at 7:00 AM (the value in B5). To do this, we use the TIME function, which can create a valid Excel time with hours, minutes, and seconds given as decimal values.

To create the numbers used for hours with SEQUENCE, we have:

    SEQUENCE(12,1,HOUR(B5))
    

The HOUR function is used to convert the time in B5 to a decimal value for hours (7). So the function resolves to:

    SEQUENCE(12,1,7)
    

which generates an [array](https://exceljet.net/glossary/array)
 of numbers like this:

    {7;8;9;10;11;12;13;14;15;16;17;18}
    

This array is returned to the TIME function as the _hour_ argument:

    =TIME({7;8;9;10;11;12;13;14;15;16;17;18},1),0,0)
    

The TIME function returns 12 times to a spill range beginning in cell D5.

### With raw numbers

The example above used the TIME function for convenience, but it is also possible to work with numeric values directly. Since [Excel time is recorded as fractions of a day](https://exceljet.net/glossary/excel-time)
, the formula above can be written like this:

    =SEQUENCE(12,1,B5,1/24)
    

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: Sequence of months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_months.png "Excel formula: Sequence of months")](https://exceljet.net/formulas/sequence-of-months)

### [Sequence of months](https://exceljet.net/formulas/sequence-of-months)

The goal is to generate a series of dates by month based on a given start date. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE function inside the EDATE function like this: =EDATE(B5,SEQUENCE(12,1,0)) The result is a series of 12 dates, incremented by...

[![Excel formula: Sequence of years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence%20of%20years.png "Excel formula: Sequence of years")](https://exceljet.net/formulas/sequence-of-years)

### [Sequence of years](https://exceljet.net/formulas/sequence-of-years)

The goal is to generate a series of dates one year apart. In the current version of Excel, the easiest way to do this is with the SEQUENCE function together with the DATE, YEAR, MONTH, and DAY functions. In older versions of Excel, you can use the same date functions and a more manual approach...

[![Excel formula: Sequence of days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_days.png "Excel formula: Sequence of days")](https://exceljet.net/formulas/sequence-of-days)

### [Sequence of days](https://exceljet.net/formulas/sequence-of-days)

The goal is to generate a series of sequential dates with a formula. In the current version of Excel, the easiest method is to use the SEQUENCE function. SEQUENCE can return all dates at the same time into a range on the worksheet. In older versions of Excel without the SEQUENCE function, you can...

Related functions
-----------------

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel TIME function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_time.png "Excel TIME function")](https://exceljet.net/functions/time-function)

### [TIME Function](https://exceljet.net/functions/time-function)

The Excel TIME function is a built-in function that allows you to create a time with individual hour, minute, and second components. The TIME function is useful when you want to assemble a proper time inside another formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sequence of months](https://exceljet.net/formulas/sequence-of-months)
    
*   [Sequence of years](https://exceljet.net/formulas/sequence-of-years)
    
*   [Sequence of days](https://exceljet.net/formulas/sequence-of-days)
    

### Functions

*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [TIME Function](https://exceljet.net/functions/time-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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