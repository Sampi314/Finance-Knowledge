# Data validation require unique number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-require-unique-number

---

[Skip to main content](https://exceljet.net/formulas/data-validation-require-unique-number#main-content)

[](https://exceljet.net/formulas/data-validation-require-unique-number#)

*   [Previous](https://exceljet.net/formulas/data-validation-require-specific-multiple)
    
*   [Next](https://exceljet.net/formulas/data-validation-specific-characters-only)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation require unique number
=====================================

by Dave Bruns · Updated 5 Sep 2018

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Data validation require unique number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/data%20validation%20require%20unique%20number.png "Excel formula: Data validation require unique number")

Summary
-------

To allow only unique numbers in a given range, you can use data validation with a custom formula based on the AND, ISNUMBER, and COUNTIF functions.

In the example shown, the data validation applied to B5:B9 is:

    =AND(ISNUMBER(B5),COUNTIF(ids,B5)<2)
    

where ids is the named range B5:B9.

Generic formula
---------------

    =AND(ISNUMBER(A1),COUNTIF(range,A1)<2)

Explanation 
------------

Data validation rules are triggered when a user adds or changes a cell value.

The AND function takes multiple arguments (logical expressions) and returns TRUE only when all arguments return TRUE. In this case, we need two conditions:

Logical 1 tests if the input is a number using the ISNUMBER function:

    ISNUMBER(B5)
    

The ISNUMBER function returns TRUE when a value is numeric and FALSE if not.

Logical 2 tests checks that the input doesn't already exist in the named range "ids":

    COUNTIF(ids,B5)<2
    

COUNTIF returns a count of the value in B5 inside the named range ids (B5:B9). If the count is less than 2, the logical expression returns TRUE.

If both logical expressions return TRUE, the AND function returns TRUE and validation succeeds:

    =AND(TRUE,TRUE) // validation successful
    

If either logical returns FALSE, data validation fails.

Be aware that numeric input includes dates and times, whole numbers, and decimal values.

_Note: Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined, in this case B5._

> [Data Validation Guide](https://exceljet.net/articles/excel-data-validation-guide)
>  | [Data Validation Formulas](https://exceljet.net/data-validation-formulas)
>  | [Dependent Dropdown Lists](https://exceljet.net/articles/dependent-dropdown-lists)

Related formulas
----------------

[![Excel formula: Data validation unique values only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20unique%20values%20only.png "Excel formula: Data validation unique values only")](https://exceljet.net/formulas/data-validation-unique-values-only)

### [Data validation unique values only](https://exceljet.net/formulas/data-validation-unique-values-only)

Data validation rules are triggered when a user adds or changes a cell value. In this example, we are using a formula that checks that the input doesn't already exist in the named range "emails": COUNTIF(ids,B5)<2 COUNTIF returns a count of the value in C5 inside the named range emails (C5:C9)...

[![Excel formula: Data validation allow numbers only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20number%20only.png "Excel formula: Data validation allow numbers only")](https://exceljet.net/formulas/data-validation-allow-numbers-only)

### [Data validation allow numbers only](https://exceljet.net/formulas/data-validation-allow-numbers-only)

Data validation rules are triggered when a user adds or changes a cell value. The ISNUMBER function returns TRUE when a value is numeric and FALSE if not. As a result, all numeric input will pass validation. Be aware that numeric input includes dates and times, whole numbers, and decimal values...

[![Excel formula: Data validation allow text only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20text%20only.png "Excel formula: Data validation allow text only")](https://exceljet.net/formulas/data-validation-allow-text-only)

### [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)

Data validation rules are triggered when a user adds or changes a cell value. Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined. The ISTEXT function returns TRUE when a value is text and FALSE if not. As a...

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

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

*   [Data validation unique values only](https://exceljet.net/formulas/data-validation-unique-values-only)
    
*   [Data validation allow numbers only](https://exceljet.net/formulas/data-validation-allow-numbers-only)
    
*   [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)
    

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
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