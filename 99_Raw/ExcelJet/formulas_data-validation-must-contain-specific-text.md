# Data validation must contain specific text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-must-contain-specific-text

---

[Skip to main content](https://exceljet.net/formulas/data-validation-must-contain-specific-text#main-content)

[](https://exceljet.net/formulas/data-validation-must-contain-specific-text#)

*   [Previous](https://exceljet.net/formulas/data-validation-must-begin-with)
    
*   [Next](https://exceljet.net/formulas/data-validation-must-not-contain)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation must contain specific text
==========================================

by Dave Bruns · Updated 18 Sep 2018

Related functions 
------------------

[FIND](https://exceljet.net/functions/find-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: Data validation must contain specific text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/data%20validation%20contains%20specific%20text.png "Excel formula: Data validation must contain specific text")

Summary
-------

To allow only values that contain a specific text string, you can use data validation with a custom formula based on the FIND and ISNUMBER functions. In the example shown, the data validation applied to C5:C9 is:

    =ISNUMBER(FIND("XST",C5))
    

Generic formula
---------------

    =ISNUMBER(FIND("txt",A1))

Explanation 
------------

Data validation rules are triggered when a user adds or changes a cell value.

In this formula, the FIND function is configured to search for the text "XST" in cell C5. If found, FIND will return a numeric position (i.e. 2, 4, 5, etc.) to represent the starting point of the text in the cell. If the text is not found, FIND will return an error. For example, for cell C5, FIND will return 5, since "XST" starts at character 5.

The result returned by the FIND function is then evaluated by the ISNUMBER function. For any numeric result returned by FIND, ISNUMBER will return TRUE and validation will succeed. When text isn't found, FIND will return an error, ISNUMBER will return FALSE, and the input will fail validation.

### Must not contain

To validate input only when a cell does not contain specific text, you can replace the ISNUMBER function with ISERROR like this:

    =ISERROR(FIND("XST",C5))
    

This formula will return TRUE when "XST" is _not found_, and data validation will succeed.

_Note: Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined, in this case C5._

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

[![Excel formula: Data validation must not contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data_validation_must_not_contain.png "Excel formula: Data validation must not contain")](https://exceljet.net/formulas/data-validation-must-not-contain)

### [Data validation must not contain](https://exceljet.net/formulas/data-validation-must-not-contain)

In this example, the goal is to construct a data validation rule that will prevent any one of a list of values from being entered. Data validation rules are triggered when a user adds or changes a cell value. One option is to use a formula to validate user input, which is the approach taken in the...

Related functions
-----------------

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

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
    
*   [Data validation must not contain](https://exceljet.net/formulas/data-validation-must-not-contain)
    

### Functions

*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

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