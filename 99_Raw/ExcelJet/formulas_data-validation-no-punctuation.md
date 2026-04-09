# Data validation no punctuation - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-no-punctuation

---

[Skip to main content](https://exceljet.net/formulas/data-validation-no-punctuation#main-content)

[](https://exceljet.net/formulas/data-validation-no-punctuation#)

*   [Previous](https://exceljet.net/formulas/data-validation-must-not-exist-in-list)
    
*   [Next](https://exceljet.net/formulas/data-validation-only-dates-between)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation no punctuation
==============================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[FIND](https://exceljet.net/functions/find-function)

[COUNT](https://exceljet.net/functions/count-function)

![Excel formula: Data validation no punctuation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/data%20validation%20no%20punctuation.png "Excel formula: Data validation no punctuation")

Summary
-------

To use data validation to restrict punctuation, you can use a named range and a formula based on the FIND and COUNT functions. In the example shown, the data validation applied to C5:C10 is:

    =COUNT(FIND(xlist,B5))=0
    

where **xlist** is the named range D5:D11.

Generic formula
---------------

    =COUNT(FIND(xlist,A1))=0

Explanation 
------------

Data validation rules are triggered when a user adds or changes a cell value. When a custom formula returns TRUE, validation passes and the input is accepted. When a formula returns FALSE, validation fails and the input is rejected with a popup message.

In this case, we have previously defined the [named range](https://exceljet.net/glossary/named-range)
 "xlist" as D5:D11. This range holds characters that are not allowed.

The formula we are using for data validation is:

    =COUNT(FIND(xlist,B5))=0
    

Working from the inside out FIND function is configured with xlist for "find text", and cell B5 as the text to search. Because we are giving FIND an [array](https://exceljet.net/glossary/array)
 with multiple values, FIND returns an array of results, one for each character in the named range "xlist". For cell B5, the result from FIND looks like this:

    {#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!}
    

Each #VALUE error represents one character not found. If we try to enter, say, "demolition@", which includes a restricted character, FIND returns:

    {#VALUE!;11;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!}
    

Note the second value in the array is now 11.

Next, the COUNT function returns the count of all numbers in the array. When the array contains no numbers (i.e. no restricted characters) COUNT returns zero, the expression returns TRUE, and data validation succeeds. However, When the array contains no numbers (i.e. there is at least one restricted character found) COUNT returns a number, the expression returns FALSE, and data validation fails.

The characters that appear in the named range **xlist** can be customized fit requirements.

_Note: Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined, in this case, B5._

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

[![Excel formula: Data validation whole percentage only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20whole%20percentage%20only3.png "Excel formula: Data validation whole percentage only")](https://exceljet.net/formulas/data-validation-whole-percentage-only)

### [Data validation whole percentage only](https://exceljet.net/formulas/data-validation-whole-percentage-only)

The Excel TRUNC function does no rounding, it just returns a truncated number. It has an optional second argument (num\_digits) to specify precision. When num\_digits is not provided, it defaults to zero. In this formula for data validation, we use TRUNC to get the non-decimal part of a percentage,...

Related functions
-----------------

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

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
    
*   [Data validation whole percentage only](https://exceljet.net/formulas/data-validation-whole-percentage-only)
    

### Functions

*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    

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