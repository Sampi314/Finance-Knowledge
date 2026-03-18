# Data validation date in next 30 days - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-date-in-next-30-days

---

[Skip to main content](https://exceljet.net/formulas/data-validation-date-in-next-30-days#main-content)

[](https://exceljet.net/formulas/data-validation-date-in-next-30-days#)

*   [Previous](https://exceljet.net/formulas/data-validation-allow-weekday-only)
    
*   [Next](https://exceljet.net/formulas/data-validation-date-in-specific-year)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation date in next 30 days
====================================

by Dave Bruns · Updated 5 Sep 2018

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[TODAY](https://exceljet.net/functions/today-function)

![Excel formula: Data validation date in next 30 days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Data%20validation%20date%20in%20next%2030%20days.png "Excel formula: Data validation date in next 30 days")

Summary
-------

_Note: Excel has several built-in data validation rules for dates. This page explains how to create a your own validation rule based on a custom formula when you want more control and flexibility._

To allow only a date in the next 30 days, you can use data validation with a custom formula based on the AND, and TODAY functions.

In the example shown, the data validation applied to C5:C7 is:

    =AND(C5>TODAY(),C5<=(TODAY()+30))
    

Generic formula
---------------

    =AND(A1>TODAY(),A1<=(TODAY()+days))

Explanation 
------------

Data validation rules are triggered when a user adds or changes a cell value.

The TODAY function returns today's date (recalculated an on on-going basis). The AND function takes multiple logical expressions and returns TRUE only when all expressions return TRUE. In this case, we need to test two conditions:

The first condition checks that the input is greater than today:

    C5>TODAY()
    

The second condition checks that the input is less than today + 30:

    C5<=(TODAY()+30)
    

(Dates are just serial numbers in Excel, so we can simply add 30).

If both logical expressions return TRUE, the AND function returns TRUE and validation succeeds. If either expressions returns FALSE, data validation fails.

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

[![Excel formula: Count cells between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20two%20numbers_0.png "Excel formula: Count cells between two numbers")](https://exceljet.net/formulas/count-cells-between-two-numbers)

### [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)

In this example, the goal is to count numbers that fall within specific ranges. The lower value comes from the "Start" column, and the upper value comes from the "End" column. For each range, we want to include both the lower value and the upper value. For convenience, the numbers being counted are...

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

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

*   [Data validation allow numbers only](https://exceljet.net/formulas/data-validation-allow-numbers-only)
    
*   [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)
    
*   [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)
    

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
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