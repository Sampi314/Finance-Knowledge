# Data validation allow weekday only - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-allow-weekday-only

---

[Skip to main content](https://exceljet.net/formulas/data-validation-allow-weekday-only#main-content)

[](https://exceljet.net/formulas/data-validation-allow-weekday-only#)

*   [Previous](https://exceljet.net/formulas/data-validation-allow-uppercase-only)
    
*   [Next](https://exceljet.net/formulas/data-validation-date-in-next-30-days)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation allow weekday only
==================================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[YEAR](https://exceljet.net/functions/year-function)

[TODAY](https://exceljet.net/functions/today-function)

![Excel formula: Data validation allow weekday only](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/data%20validation%20allow%20weekday%20only.png "Excel formula: Data validation allow weekday only")

Summary
-------

_Note: Excel has several built-in data validation rules for dates. This page explains how to create your own validation rule based on a custom formula if you need more control or flexibility._

To allow a user to enter only dates that are weekdays (i.e. Monday, Tuesday, Wednesday, etc.) you can use data validation with a custom formula based on the WEEKDAY function.

In the example shown, the data validation applied to C5:C7 is:

    =WEEKDAY(C5,2)<6
    

Generic formula
---------------

    =WEEKDAY(A1,2)<6

Explanation 
------------

Data validation rules are triggered when a user adds or changes a cell value.

This custom validation formula uses the WEEKDAY function to get a numeric value, 1-7, corresponding to a week beginning Monday (1) and ending Sunday (7). To get a number for a Monday-based week, the _return\_type_ argument for WEEKDAY is provided as 2.

The WEEKDAY result is then compared to 6. Any value less than 6 is a weekday, so the expression returns TRUE and validation succeeds. If the weekday number is not less than 6, validation fails because the date is a Saturday or Sunday.

### Date is weekend

To allow only dates that occur on a weekend (Saturday or Sunday), you can use a similar formula:

    =WEEKDAY(C5,2)>5
    

_Note: Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined, in this case, C5._

> [Data Validation Guide](https://exceljet.net/articles/excel-data-validation-guide)
>  | [Data Validation Formulas](https://exceljet.net/data-validation-formulas)
>  | [Dependent Dropdown Lists](https://exceljet.net/articles/dependent-dropdown-lists)

Related formulas
----------------

[![Excel formula: Data validation only dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20only%20dates%20between.png "Excel formula: Data validation only dates between")](https://exceljet.net/formulas/data-validation-only-dates-between)

### [Data validation only dates between](https://exceljet.net/formulas/data-validation-only-dates-between)

Data validation rules are triggered when a user adds or changes a cell value. The AND function takes multiple arguments (logicals) and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because we want to allow...

[![Excel formula: Data validation date in next 30 days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Data%20validation%20date%20in%20next%2030%20days.png "Excel formula: Data validation date in next 30 days")](https://exceljet.net/formulas/data-validation-date-in-next-30-days)

### [Data validation date in next 30 days](https://exceljet.net/formulas/data-validation-date-in-next-30-days)

Data validation rules are triggered when a user adds or changes a cell value. The TODAY function returns today's date (recalculated an on on-going basis). The AND function takes multiple logical expressions and returns TRUE only when all expressions return TRUE. In this case, we need to test two...

[![Excel formula: Data validation date in specific year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20date%20in%20specific%20year.png "Excel formula: Data validation date in specific year")](https://exceljet.net/formulas/data-validation-date-in-specific-year)

### [Data validation date in specific year](https://exceljet.net/formulas/data-validation-date-in-specific-year)

Data validation rules are triggered when a user adds or changes a cell value. This custom validation formula simply checks the year of any date against a hard-coded year value using the YEAR function. When a user enters a value, the YEAR function extracts and compares the year to 2016: =YEAR(C5)=...

[![Excel formula: Data validation allow numbers only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20number%20only.png "Excel formula: Data validation allow numbers only")](https://exceljet.net/formulas/data-validation-allow-numbers-only)

### [Data validation allow numbers only](https://exceljet.net/formulas/data-validation-allow-numbers-only)

Data validation rules are triggered when a user adds or changes a cell value. The ISNUMBER function returns TRUE when a value is numeric and FALSE if not. As a result, all numeric input will pass validation. Be aware that numeric input includes dates and times, whole numbers, and decimal values...

[![Excel formula: Data validation allow text only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20text%20only.png "Excel formula: Data validation allow text only")](https://exceljet.net/formulas/data-validation-allow-text-only)

### [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)

Data validation rules are triggered when a user adds or changes a cell value. Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined. The ISTEXT function returns TRUE when a value is text and FALSE if not. As a...

Related functions
-----------------

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

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

*   [Data validation only dates between](https://exceljet.net/formulas/data-validation-only-dates-between)
    
*   [Data validation date in next 30 days](https://exceljet.net/formulas/data-validation-date-in-next-30-days)
    
*   [Data validation date in specific year](https://exceljet.net/formulas/data-validation-date-in-specific-year)
    
*   [Data validation allow numbers only](https://exceljet.net/formulas/data-validation-allow-numbers-only)
    
*   [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)
    

### Functions

*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    

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