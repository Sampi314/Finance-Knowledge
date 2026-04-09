# Distinct values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/distinct-values

---

[Skip to main content](https://exceljet.net/formulas/distinct-values#main-content)

[](https://exceljet.net/formulas/distinct-values#)

*   [Previous](https://exceljet.net/formulas/detailed-let-function-example)
    
*   [Next](https://exceljet.net/formulas/dynamic-summary-count)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Distinct values
===============

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

![Excel formula: Distinct values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/distinct%20values.png "Excel formula: Distinct values")

Summary
-------

To extract a list of distinct values from a set of data (i.e. values that appear just once), you can use the [UNIQUE function](https://exceljet.net/functions/unique-function)
. In the example shown, the formula in D5 is:

    =UNIQUE(B5:B16,FALSE,TRUE)
    

which outputs the 2 distinct values in the data, "purple", and "gray".

Generic formula
---------------

    =UNIQUE(data,FALSE,TRUE)

Explanation 
------------

This example uses the [UNIQUE function](https://exceljet.net/functions/unique-function)
. With default settings, UNIQUE will output a list of unique values, i.e. values that appear one or more times in the source data. However, UNIQUE has an optional third argument, called _occurs\_once_ that, when set to TRUE, will cause UNIQUE to return only values that appear once in the data.

In the example shown, UNIQUE's arguments are configured like this:

*   _array_ \- B5:B16
*   _by\_col_ - FALSE
*   _occurs\_once_ \- TRUE

Because _occurs\_once_ is set to TRUE, UNIQUE outputs the 2 values in the data that appear just once: "purple", and "gray".

Notice the _by\_col_ argument is optional and defaults to FALSE, so it can be omitted:

    =UNIQUE(data,,TRUE)
    

TRUE and FALSE can also be replaced with 1 and zero like this:

    =UNIQUE(data,0,1)
    

### Dynamic source range

UNIQUE won't automatically change the source range if data is added or deleted. To give UNIQUE a dynamic range that will automatically resize as needed, you can use an [Excel Table](https://exceljet.net/articles/excel-tables)
, or create a [dynamic named range](https://exceljet.net/glossary/dynamic-named-range)
 with a formula.

> UNIQUE is a new function available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: Unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values.png "Excel formula: Unique values")](https://exceljet.net/formulas/unique-values)

### [Unique values](https://exceljet.net/formulas/unique-values)

This example uses the UNIQUE function, which is fully automatic. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. UNIQUE is a dynamic function. If any data in B5:B16 changes, the output from UNIQUE will update immediately...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Unique values](https://exceljet.net/formulas/unique-values)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    

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