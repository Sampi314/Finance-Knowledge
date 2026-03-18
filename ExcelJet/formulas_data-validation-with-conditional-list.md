# Data validation with conditional list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-with-conditional-list

---

[Skip to main content](https://exceljet.net/formulas/data-validation-with-conditional-list#main-content)

[](https://exceljet.net/formulas/data-validation-with-conditional-list#)

*   [Previous](https://exceljet.net/formulas/data-validation-whole-percentage-only)
    
*   [Next](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation with conditional list
=====================================

by Dave Bruns · Updated 4 May 2024

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Data validation with conditional list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/data_validation_with_conditional_list.png "Excel formula: Data validation with conditional list")

Summary
-------

To allow a user to switch between two or more lists, you can use the IF function to test for a value and conditionally return a list of values based on the result. In the example shown, the data validation applied to C4 is:

    =IF(C4="See full list",long_list,short_list)
    

This allows a user to select a city from a short list of options by default, but also provides an easy way to view and select a city from a longer list of cities.

_Note: I ran into [this formula and approach](http://chandoo.org/wp/2008/11/25/advanced-data-validation-techniques-in-excel-spreadcheats/)
 on the excellent Chandoo site._

Generic formula
---------------

    =IF(A1="See full list",long_list,short_list)

Explanation 
------------

Data validation rules are triggered when a user adds or changes a cell value. This formula takes advantage of this behavior to provide a clever way for the user to switch between a short list of cities and a longer list of cities. In the worksheet shown, the data validation applied to C4 looks like this:

    =IF(C4="See full list",long_list,short_list)
    

![Data validation with conditional list set up](https://exceljet.net/sites/default/files/images/formulas/inline/data_validation_with_conditional_list_setup.png "Data validation with conditional list set up")

The IF function is configured to test the value in cell C4. When C4 contains the text "See full list", IF returns the named range long\_list. When C4 is empty or contains any other value IF returns the named range short\_list.

### Behavior

The user starts with the values in E6:E13 as seen below:

![Data validation with default short list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/data_validation_with_conditional_list_default_short_list.png "Data validation with default short list")

When the user selects "See full list", they can select from the longer list of cities in G6:G35:

![Data validation with optional long list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/data_validation_with_conditional_list_optional_long_list.png "Data validation with optional long list")

The named ranges used in the formula are not required, but they make the formula easier to read. If you are new to named ranges, [this page provides a good overview](https://exceljet.net/articles/named-ranges)
.

### Dependent dropdown lists

Expanding on the example above, you can create multiple dependent dropdown lists. For example, a user selects an item type of "fruit", so they next see a list of fruits to select. If they first select "vegetable" they then see a list of vegetables. Click the image below for instructions and examples:

[![dependent dropdown list example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/dependent%20dropdown%20list%20with%20custom%20formula%20and%20INDIRECT.png?itok=RoZuVJMg "dependent dropdown list example")](https://exceljet.net/articles/dependent-dropdown-lists)

> [Data Validation Guide](https://exceljet.net/articles/excel-data-validation-guide)
>  | [Data Validation Formulas](https://exceljet.net/data-validation-formulas)
>  | [Dependent Dropdown Lists](https://exceljet.net/articles/dependent-dropdown-lists)

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    

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