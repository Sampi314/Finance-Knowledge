# Data validation don't exceed total - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-dont-exceed-total

---

[Skip to main content](https://exceljet.net/formulas/data-validation-dont-exceed-total#main-content)

[](https://exceljet.net/formulas/data-validation-dont-exceed-total#)

*   [Previous](https://exceljet.net/formulas/data-validation-date-in-specific-year)
    
*   [Next](https://exceljet.net/formulas/data-validation-exists-in-list)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation don't exceed total
==================================

by Dave Bruns · Updated 5 Sep 2018

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Data validation don't exceed total](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/data%20validation%20dont%20exceed%20total.png "Excel formula: Data validation don't exceed total")

Summary
-------

To allow only values that don't exceed a set sum, you can use data validation with a custom formula based on the SUM function. In the example shown, the data validation applied to B5:B9 is:

    =SUM($C$6:$C$9)<=1000
    

Generic formula
---------------

    =SUM(range)<=1000

Explanation 
------------

Data validation rules are triggered when a user adds or changes a cell value.

In this case, we need a formula that returns FALSE as long as entries in C6:C9 sum to a total equal to or below 1000. We use the SUM function to sum a fixed range and then simply compare the result to 1000 using less than or equal to. Note the range C6:C9 is entered as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 to prevent the reference from changing automatically for each cell that data validation is applied to.

Each time a number is entered, the validation is triggered. As long as the sum remains less than 1000, validation succeeds. If any entry causes the sum C6:C9 to exceed 1000, validation fails.

_Note: Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined, in this case B5._

> [Data Validation Guide](https://exceljet.net/articles/excel-data-validation-guide)
>  | [Data Validation Formulas](https://exceljet.net/data-validation-formulas)
>  | [Dependent Dropdown Lists](https://exceljet.net/articles/dependent-dropdown-lists)

Related formulas
----------------

[![Excel formula: Data validation allow numbers only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20number%20only.png "Excel formula: Data validation allow numbers only")](https://exceljet.net/formulas/data-validation-allow-numbers-only)

### [Data validation allow numbers only](https://exceljet.net/formulas/data-validation-allow-numbers-only)

Data validation rules are triggered when a user adds or changes a cell value. The ISNUMBER function returns TRUE when a value is numeric and FALSE if not. As a result, all numeric input will pass validation. Be aware that numeric input includes dates and times, whole numbers, and decimal values...

[![Excel formula: Data validation allow text only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20text%20only.png "Excel formula: Data validation allow text only")](https://exceljet.net/formulas/data-validation-allow-text-only)

### [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)

Data validation rules are triggered when a user adds or changes a cell value. Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined. The ISTEXT function returns TRUE when a value is text and FALSE if not. As a...

[![Excel formula: Data validation require unique number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20require%20unique%20number.png "Excel formula: Data validation require unique number")](https://exceljet.net/formulas/data-validation-require-unique-number)

### [Data validation require unique number](https://exceljet.net/formulas/data-validation-require-unique-number)

Data validation rules are triggered when a user adds or changes a cell value. The AND function takes multiple arguments (logical expressions) and returns TRUE only when all arguments return TRUE. In this case, we need two conditions: Logical 1 tests if the input is a number using the ISNUMBER...

Related functions
-----------------

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Data validation allow numbers only](https://exceljet.net/formulas/data-validation-allow-numbers-only)
    
*   [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)
    
*   [Data validation require unique number](https://exceljet.net/formulas/data-validation-require-unique-number)
    

### Functions

*   [SUM Function](https://exceljet.net/functions/sum-function)
    

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