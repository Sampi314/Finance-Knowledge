# Data validation must begin with - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-must-begin-with

---

[Skip to main content](https://exceljet.net/formulas/data-validation-must-begin-with#main-content)

[](https://exceljet.net/formulas/data-validation-must-begin-with#)

*   [Previous](https://exceljet.net/formulas/data-validation-exists-in-list)
    
*   [Next](https://exceljet.net/formulas/data-validation-must-contain-specific-text)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation must begin with
===============================

by Dave Bruns · Updated 5 Sep 2018

Related functions 
------------------

[EXACT](https://exceljet.net/functions/exact-function)

[LEFT](https://exceljet.net/functions/left-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Data validation must begin with](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/data%20validation%20must%20begin%20with.png "Excel formula: Data validation must begin with")

Summary
-------

To allow only values that begin with certain text, you can use data validation with a custom formula based on the EXACT and LEFT functions.

In the example shown, the data validation applied to C5:C9 is:

    =EXACT(LEFT(C5,3),"MX-")
    

Generic formula
---------------

    =EXACT(LEFT(A1,3),"XX-")

Explanation 
------------

Data validation rules are triggered when a user adds or changes a cell value.

In this formula, the LEFT function is used to extract the first 3 characters of the input in C5.

Next, the EXACT function is used to compare the extracted text to the text hard-coded into the formula, "MX-". EXACT performs a case-sensitive comparison. If the two text strings match exactly, EXACT returns TRUE and validation will pass. If the match fails, EXACT will return FALSE, and input will fail validation.

### Non case-sensitive test with COUNTIF

If you don't need a case-sensitive test, you can use a simpler formula based on the COUNTIF function with a wildcard:

    =COUNTIF(C5,"MX-*")
    

The asterisk (\*) is a wildcard that matches one or more characters.

_Note: Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined, in this case C5._

> [Data Validation Guide](https://exceljet.net/articles/excel-data-validation-guide)
>  | [Data Validation Formulas](https://exceljet.net/data-validation-formulas)
>  | [Dependent Dropdown Lists](https://exceljet.net/articles/dependent-dropdown-lists)

Related formulas
----------------

[![Excel formula: Data validation must contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20contains%20specific%20text.png "Excel formula: Data validation must contain specific text")](https://exceljet.net/formulas/data-validation-must-contain-specific-text)

### [Data validation must contain specific text](https://exceljet.net/formulas/data-validation-must-contain-specific-text)

Data validation rules are triggered when a user adds or changes a cell value. In this formula, the FIND function is configured to search for the text "XST" in cell C5. If found, FIND will return a numeric position (i.e. 2, 4, 5, etc.) to represent the starting point of the text in the cell. If the...

[![Excel formula: Data validation allow numbers only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20number%20only.png "Excel formula: Data validation allow numbers only")](https://exceljet.net/formulas/data-validation-allow-numbers-only)

### [Data validation allow numbers only](https://exceljet.net/formulas/data-validation-allow-numbers-only)

Data validation rules are triggered when a user adds or changes a cell value. The ISNUMBER function returns TRUE when a value is numeric and FALSE if not. As a result, all numeric input will pass validation. Be aware that numeric input includes dates and times, whole numbers, and decimal values...

[![Excel formula: Data validation allow text only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20text%20only.png "Excel formula: Data validation allow text only")](https://exceljet.net/formulas/data-validation-allow-text-only)

### [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)

Data validation rules are triggered when a user adds or changes a cell value. Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined. The ISTEXT function returns TRUE when a value is text and FALSE if not. As a...

Related functions
-----------------

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

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

*   [Data validation must contain specific text](https://exceljet.net/formulas/data-validation-must-contain-specific-text)
    
*   [Data validation allow numbers only](https://exceljet.net/formulas/data-validation-allow-numbers-only)
    
*   [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)
    

### Functions

*   [EXACT Function](https://exceljet.net/functions/exact-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
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