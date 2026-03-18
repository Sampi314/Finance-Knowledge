# Data validation must not exist in list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-must-not-exist-in-list

---

[Skip to main content](https://exceljet.net/formulas/data-validation-must-not-exist-in-list#main-content)

[](https://exceljet.net/formulas/data-validation-must-not-exist-in-list#)

*   [Previous](https://exceljet.net/formulas/data-validation-must-not-contain)
    
*   [Next](https://exceljet.net/formulas/data-validation-no-punctuation)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation must not exist in list
======================================

by Dave Bruns · Updated 19 Nov 2018

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Data validation must not exist in list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/data%20validation%20must%20not%20exist%20in%20list.png "Excel formula: Data validation must not exist in list")

Summary
-------

_Note: Excel has a built-in data validation rules for dropdown lists. This page explains how to create a custom validation rule when you want to \*prevent\* a user from entering a value in a list._

To allow only values that do not exist in a list, you can use data validation with a custom formula based on the COUNTIF function. In the example shown, the data validation applied to B5:B9 is:

    =COUNTIF(list,B5)=0
    

where "list" is the [named range](https://exceljet.net/glossary/named-range)
 D5:D7.

Generic formula
---------------

    =COUNTIF(list,A1)=0

Explanation 
------------

Data validation rules are triggered when a user adds or changes a cell value.

In this case, the COUNTIF function is part of an expression that returns TRUE when a value _does not exist_ in a defined list. The COUNTIF function simply counts occurrences of the value in the list. As long as the count is zero, the entry will pass validation. If the count is not zero (i.e. the user entered a value from the list) validation will fail.

_Note: Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined, in this case B5._

> [Data Validation Guide](https://exceljet.net/articles/excel-data-validation-guide)
>  | [Data Validation Formulas](https://exceljet.net/data-validation-formulas)
>  | [Dependent Dropdown Lists](https://exceljet.net/articles/dependent-dropdown-lists)

Related formulas
----------------

[![Excel formula: Data validation exists in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20value%20exists%20in%20list.png "Excel formula: Data validation exists in list")](https://exceljet.net/formulas/data-validation-exists-in-list)

### [Data validation exists in list](https://exceljet.net/formulas/data-validation-exists-in-list)

Data validation rules are triggered when a user adds or changes a cell value. In this case, the COUNTIF function is part of an expression that returns TRUE when a value exists in a specified range or list, and FALSE if not. The COUNTIF function simply counts occurrences of the value in the list...

[![Excel formula: Data validation allow text only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20text%20only.png "Excel formula: Data validation allow text only")](https://exceljet.net/formulas/data-validation-allow-text-only)

### [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)

Data validation rules are triggered when a user adds or changes a cell value. Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined. The ISTEXT function returns TRUE when a value is text and FALSE if not. As a...

[![Excel formula: Data validation only dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20only%20dates%20between.png "Excel formula: Data validation only dates between")](https://exceljet.net/formulas/data-validation-only-dates-between)

### [Data validation only dates between](https://exceljet.net/formulas/data-validation-only-dates-between)

Data validation rules are triggered when a user adds or changes a cell value. The AND function takes multiple arguments (logicals) and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because we want to allow...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Data validation exists in list](https://exceljet.net/formulas/data-validation-exists-in-list)
    
*   [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)
    
*   [Data validation only dates between](https://exceljet.net/formulas/data-validation-only-dates-between)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Articles

*   [Excel Data Validation Guide](https://exceljet.net/articles/excel-data-validation-guide)
    

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