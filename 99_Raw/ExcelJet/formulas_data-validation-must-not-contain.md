# Data validation must not contain - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-must-not-contain

---

[Skip to main content](https://exceljet.net/formulas/data-validation-must-not-contain#main-content)

[](https://exceljet.net/formulas/data-validation-must-not-contain#)

*   [Previous](https://exceljet.net/formulas/data-validation-must-contain-specific-text)
    
*   [Next](https://exceljet.net/formulas/data-validation-must-not-exist-in-list)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation must not contain
================================

by Dave Bruns · Updated 19 May 2024

Related functions 
------------------

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SEARCH](https://exceljet.net/functions/search-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Data validation must not contain](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/data_validation_must_not_contain.png "Excel formula: Data validation must not contain")

Summary
-------

To disallow input that contains one of many things, you can use a custom data validation rule based on the [SEARCH function](https://exceljet.net/functions/search-function)
. In the example shown, the data validation applied to B5:B11 is:

    =SUMPRODUCT(--ISNUMBER(SEARCH(list,B5)))=0
    

Generic formula
---------------

    =SUMPRODUCT(--ISNUMBER(SEARCH(list,A1)))=0

Explanation 
------------

In this example, the goal is to construct a data validation rule that will prevent any one of a list of values from being entered. Data validation rules are triggered when a user adds or changes a cell value. One option is to use a formula to validate user input, which is the approach taken in the example shown, where the formula used to enforce the rule looks like this:

    =SUMPRODUCT(--ISNUMBER(SEARCH(list,B5)))=0
    

This formula uses the [SEARCH function](https://exceljet.net/functions/search-function)
 to test user input for each value in the [named range](https://exceljet.net/glossary/named-range)
 "list", which is the range D5:D10. The search logic is "contains" by default because of how SEARCH works. When a value from the "list" is found, either as a complete value or a substring, SEARCH returns the position of the match as a number. If not found, SEARCH returns an error. Since there are no invalid entries in cell B5, SEARCH returns an array of errors like this:

    {#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!}

The five errors tell us that no invalid entries were found. To test for invalid entries inside the formula, we use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
, which returns TRUE when a value is a number and FALSE for anything else. After ISNUMBER evaluates the results from SEARCH we have an array of TRUE and FALSE values. At this point, our formula looks like this:

    =SUMPRODUCT(--{FALSE;FALSE;FALSE;FALSE;FALSE})=0

Next, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to convert the TRUE and FALSE values to 1s and 0s, which yields this:

    =SUMPRODUCT({0;0;0;0;0})=0

Finally, the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 sums up the items in the array and the result is tested against zero. As long as all items are zero, SUMPRODUCT returns zero and validation succeeds. If SUMPRODUCT returns a positive number, an invalid value has been found. The formula returns FALSE and validation fails.

_Note: Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined, in this case, B5._

> [Data Validation Guide](https://exceljet.net/articles/excel-data-validation-guide)
>  | [Data Validation Formulas](https://exceljet.net/data-validation-formulas)
>  | [Dependent Dropdown Lists](https://exceljet.net/articles/dependent-dropdown-lists)

Related formulas
----------------

[![Excel formula: Data validation allow text only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20text%20only.png "Excel formula: Data validation allow text only")](https://exceljet.net/formulas/data-validation-allow-text-only)

### [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)

Data validation rules are triggered when a user adds or changes a cell value. Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined. The ISTEXT function returns TRUE when a value is text and FALSE if not. As a...

[![Excel formula: Data validation only dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20only%20dates%20between.png "Excel formula: Data validation only dates between")](https://exceljet.net/formulas/data-validation-only-dates-between)

### [Data validation only dates between](https://exceljet.net/formulas/data-validation-only-dates-between)

Data validation rules are triggered when a user adds or changes a cell value. The AND function takes multiple arguments (logicals) and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because we want to allow...

[![Excel formula: Data validation must not exist in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20must%20not%20exist%20in%20list.png "Excel formula: Data validation must not exist in list")](https://exceljet.net/formulas/data-validation-must-not-exist-in-list)

### [Data validation must not exist in list](https://exceljet.net/formulas/data-validation-must-not-exist-in-list)

Data validation rules are triggered when a user adds or changes a cell value. In this case, the COUNTIF function is part of an expression that returns TRUE when a value does not exist in a defined list. The COUNTIF function simply counts occurrences of the value in the list. As long as the count is...

[![Excel formula: Data validation must contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20contains%20specific%20text.png "Excel formula: Data validation must contain specific text")](https://exceljet.net/formulas/data-validation-must-contain-specific-text)

### [Data validation must contain specific text](https://exceljet.net/formulas/data-validation-must-contain-specific-text)

Data validation rules are triggered when a user adds or changes a cell value. In this formula, the FIND function is configured to search for the text "XST" in cell C5. If found, FIND will return a numeric position (i.e. 2, 4, 5, etc.) to represent the starting point of the text in the cell. If the...

Related functions
-----------------

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)
    
*   [Data validation only dates between](https://exceljet.net/formulas/data-validation-only-dates-between)
    
*   [Data validation must not exist in list](https://exceljet.net/formulas/data-validation-must-not-exist-in-list)
    
*   [Data validation must contain specific text](https://exceljet.net/formulas/data-validation-must-contain-specific-text)
    

### Functions

*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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