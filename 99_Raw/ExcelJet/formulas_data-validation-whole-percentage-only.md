# Data validation whole percentage only - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-whole-percentage-only

---

[Skip to main content](https://exceljet.net/formulas/data-validation-whole-percentage-only#main-content)

[](https://exceljet.net/formulas/data-validation-whole-percentage-only#)

*   [Previous](https://exceljet.net/formulas/data-validation-unique-values-only)
    
*   [Next](https://exceljet.net/formulas/data-validation-with-conditional-list)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation whole percentage only
=====================================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[TRUNC](https://exceljet.net/functions/trunc-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: Data validation whole percentage only](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/data%20validation%20whole%20percentage%20only3.png "Excel formula: Data validation whole percentage only")

Summary
-------

To allow only whole number percentages like 5%, 10% and not 5.5%, 10.25%, etc. you can use data validation with a custom formula based on the TRUNC function. In the example shown, the data validation applied to B5:B9 is:

    =TRUNC(C5*100)=(C5*100)
    

Generic formula
---------------

    =TRUNC(A1*100)=(A1*100)

Explanation 
------------

The Excel TRUNC function does no rounding, it just returns a truncated number. It has an optional second argument (num\_digits) to specify precision. When _num\_digits_ is not provided, it defaults to zero. In this formula for data validation, we use TRUNC to get the non-decimal part of a percentage, after we multiply the percentage by 100.

For example, if a user inputs 15%:

    =TRUNC(.15*100)=(.15*100)
    =TRUNC(15)=(15)
    =15=15
    =TRUE
    

If a user enters 15.5%, the formula evaluates like this

    =TRUNC(.155*100)=(.155*100)
    =TRUNC(15.5)=(15.5)
    =15=15.5
    =FALSE
    

This formula doesn't validate anything else, for example, that percentages are less than 100%. Additional conditions can be added with the AND function.

_Notes: Data validation rules are triggered when a user adds or changes a cell value. Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined, in this case, B5._

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

[![Excel formula: Highlight integers only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20integers%20only.png "Excel formula: Highlight integers only")](https://exceljet.net/formulas/highlight-integers-only)

### [Highlight integers only](https://exceljet.net/formulas/highlight-integers-only)

The MOD function returns the remainder after division. With a divisor of 1, MOD will return zero for any whole number. We use this fact to construct a simple formula that tests the result of MOD. When the result is zero (i.e. when the number is an integer) the formula returns TRUE, triggering the...

Related functions
-----------------

[![Excel TRUNC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trunc%20function.png "Excel TRUNC function")](https://exceljet.net/functions/trunc-function)

### [TRUNC Function](https://exceljet.net/functions/trunc-function)

The Excel TRUNC function returns a truncated number based on an (optional) number of digits. For example, TRUNC(4.9) will return 4, and TRUNC(-3.5) will return -3. The TRUNC function does no rounding, it simply truncates as specified.

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

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
    
*   [Highlight integers only](https://exceljet.net/formulas/highlight-integers-only)
    

### Functions

*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

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