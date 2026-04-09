# Alternatives to Dynamic Array Functions | Exceljet

**Source:** https://exceljet.net/articles/alternatives-to-dynamic-array-functions

---

[Skip to main content](https://exceljet.net/articles/alternatives-to-dynamic-array-functions#main-content)

[](https://exceljet.net/articles/alternatives-to-dynamic-array-functions#)

*   [Previous](https://exceljet.net/articles/tracking-covid-19-with-excel)
    
*   [Next](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    

Alternatives to Dynamic Array Functions
=======================================

by Dave Bruns · Updated 17 Oct 2023

![Alternatives to Dynamic Array Functions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/dynamic_array_function_alternatives.jpeg)

Summary
-------

Dynamic Excel offers 6 brand new functions that solve hard problems in Excel like sorting, filtering, and working with unique values. For those not using Office 365, this page provides some alternative formulas that work in older versions of Excel.

[Dynamic Arrays](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 are one of the biggest changes ever to Excel's formula engine. With [6 brand new functions](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
 that directly leverage dynamic arrays, they solve hard problems in Excel that have vexed even power users for decades. However, Dynamic Arrays are only available in [Office 365](https://www.office.com/)
, they are not available in Excel 2016 or 2019, and won't work in any older version.

For those not using Office 365, this page provides some alternative formulas that work in older versions of Excel. It's important to understand however, that none of the alternatives will [spill](https://exceljet.net/glossary/spill)
 multiple results onto the worksheet into a [spill range](https://exceljet.net/glossary/spill-range)
 like a native dynamic array formula. This behavior is limited to the Office 365 version of Excel.

Remember also that [Pivot Tables](https://exceljet.net/articles/excel-pivot-tables)
 can be used to solve many of these same challenges.

### New dynamic functions

For reference, the 6 new dynamic array functions are listed in the table below. Click a function name for an overview and examples of usage.

| Function | Purpose |
| --- | --- |
| [FILTER](https://exceljet.net/functions/filter-function) | Filter data and return matching records |
| --- | --- |
| [RANDARRAY](https://exceljet.net/functions/randarray-function) | Generate an array of random numbers |
| --- | --- |
| [SEQUENCE](https://exceljet.net/functions/sequence-function) | Generate an array of sequential numbers |
| --- | --- |
| [SORT](https://exceljet.net/functions/sort-function) | Sort range by column |
| --- | --- |
| [SORTBY](https://exceljet.net/functions/sortby-function) | Sort range by another range or array |
| --- | --- |
| [UNIQUE](https://exceljet.net/functions/unique-function) | Extract unique values from a list or range |
| --- | --- |

ALTERNATIVES
------------

This section contains alternative formulas that perform some of the same tasks as the functions in the table above. In almost all cases, the formulas are more complex and clunky than an equivalent dynamic array formula. At the same time, these formulas should work in almost any version of Excel.

_Note: several of these formulas are traditional array formulas and need to be entered with control + shift + enter. If you are working with them in Dynamic Excel, you don't need to use control + shift + enter, Excel will handle the array operations automatically._

### Sorting

[Dynamic Excel](https://exceljet.net/glossary/dynamic-excel)
 provides two new functions to handle sorting with formulas: [SORT](https://exceljet.net/functions/sort-function)
 and [SORTBY](https://exceljet.net/functions/sortby-function)
. These functions make it easy to sort data by one or more columns, and even sort data by a custom list. However, if you are using an older version of Excel, you still have some options for sorting with a formula:

*   [Basic numeric sort formula](https://exceljet.net/formulas/basic-numeric-sort-formula)
    
*   [Basic text sort formula](https://exceljet.net/formulas/basic-text-sort-formula)
    
*   [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)
    
*   [Random sort formula](https://exceljet.net/formulas/random-sort-formula)
    

### Filtering and extracting

Filtering and extracting data with formulas in Excel has always been a challenging problem. Dynamic Excel provides a special function, just for this purpose: the [FILTER function](https://exceljet.net/functions/filter-function)
. if you are using an older version of Excel, there are various ways to approach the problem.

*   [Extract all matches with helper column](https://exceljet.net/formulas/index-and-match-all-matches)
    
*   [Extract all partial matches](https://exceljet.net/formulas/index-and-match-all-partial-matches)
    
*   [Extract multiple matches into separate columns](https://exceljet.net/formulas/multiple-matches-into-separate-columns)
    
*   [Extract multiple matches into separate rows](https://exceljet.net/formulas/multiple-matches-into-separate-rows)
    

### Unique values

Dynamic Excel provides a dedicated function for working with unique values: the [UNIQUE function](https://exceljet.net/functions/unique-function)
. In other versions of Excel, you'll need to cobble together solutions based on several other functions. 

For counting unique values:

*   [Count unique numeric values in a range](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)
    
*   [Count unique numeric values with criteria](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)
    
*   [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)
    
*   [Count unique text values with criteria](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
    
*   [Count unique values in a range with COUNTIF](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)
    

For extracting unique values, and other tasks:

*   [Highlight unique values](https://exceljet.net/formulas/highlight-unique-values)
    
*   [Data validation unique values only](https://exceljet.net/formulas/data-validation-unique-values-only)
    
*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    
*   [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)
    

Remember: [Pivot Tables](https://exceljet.net/pivot-tables)
 also provide good tools for listing and counting unique values.

### Sequential values

One of the new Dynamic Array functions is [SEQUENCE](https://exceljet.net/functions/sequence-function)
, specifically designed to generate numeric sequences.  With controls for the start and step value, and the ability to output results in rows, columns, or both, SEQUENCE is a flexible tool for generating sequential dates, times, and all manner of numbers. If you are using an older version of Excel, there are other ways to create numeric sequences, but they are not as convenient. Commonly, you'll see solutions that use the [ROW function](https://exceljet.net/functions/row-function)
 together with [INDIRECT](https://exceljet.net/functions/indirect-function)
. Here are some examples:

*   [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Count day of week between dates](https://exceljet.net/formulas/count-day-of-week-between-dates)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    

### Random values

The [RANDARRAY function](https://exceljet.net/functions/randarray-function)
 is also new in Dynamic Excel. RANDARRAY can generate random decimal or integer values in columns, rows, or two-dimensional arrays. The beauty of RANDARRAY is that you can ask for more than one random number at the same time. This is a huge benefit when building formulas that need to perform random sorts, or random item selection.

In older versions of Excel, you will typically use either the [RAND function](https://exceljet.net/functions/rand-function)
 (decimal values) or the [RANDBETWEEN function](https://exceljet.net/functions/randbetween-function)
 (integers) to perform the same tasks. 

*   [Random sort formula](https://exceljet.net/formulas/random-sort-formula)
    
*   [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)
    
*   [Random number from a fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)
    

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

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