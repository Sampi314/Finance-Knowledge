# Data validation require specific multiple - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-require-specific-multiple

---

[Skip to main content](https://exceljet.net/formulas/data-validation-require-specific-multiple#main-content)

[](https://exceljet.net/formulas/data-validation-require-specific-multiple#)

*   [Previous](https://exceljet.net/formulas/data-validation-only-dates-between)
    
*   [Next](https://exceljet.net/formulas/data-validation-require-unique-number)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation require specific multiple
=========================================

by Dave Bruns · Updated 16 Aug 2023

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

![Excel formula: Data validation require specific multiple](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/data%20validation%20number%20multiple%20100.png "Excel formula: Data validation require specific multiple")

Summary
-------

To require that numbers be a specific multiple of another number, you can use data validation with a custom formula based on the [MOD function](https://exceljet.net/functions/mod-function)
. In the example shown, the data validation applied to C5:C10 is based on this formula:

    =MOD(C5,100)=0
    

This validation rule requires that the number entered in cell C5 be a specific multiple of 100.

Generic formula
---------------

    =MOD(A1,multiple)=0

Explanation 
------------

In this example, the goal is to create a data validation rule that will only accept numbers that are a specific multiple of another number. In the worksheet shown, the multiple is 100. Data validation rules are triggered when a user adds or changes a cell value. When a custom formula returns TRUE, validation passes and the input is accepted. When the formula returns FALSE, validation fails and the input is rejected. This means we need to create a formula that will return TRUE when input is a multiple of 100 and FALSE when input is not a multiple of 100. We can do this with the MOD function.

### MOD function

The [MOD function](https://exceljet.net/functions/mod-function)
 returns the remainder of two numbers after division. For example, with a number of 10 and a divisor of 3, MOD will return 1, the remainder after dividing 10 by 3:

    =MOD(10,3) // returns 1

In the worksheet shown, we want to validate that entered in column C numbers are a multiple of 100. The formula used to validate input looks like this:

    =MOD(C5,100)=0
    

The value in C5 is 500. The MOD function divides 500 by 100 and gets 5, with a remainder of zero. Since 0 = 0, the rule returns TRUE and the data validation passes:

    =MOD(500,100)=0
    =0=0
    =TRUE
    

If a user enters, 550, the remainder is 50, and validation fails:

    =MOD(C5,100)=0
    =MOD(550,100)=0
    =50=0
    =FALSE
    

The formula returns FALSE and data validation fails.

_Note: Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined, in this case, C5._

### Fractional values

Although the example above deals with whole numbers, you can use the same approach to validate fractional values as well. For example, to require that the value entered in cell A1 be a multiple of 0.25, you can use a data validation rule with a formula like this:

    =MOD(A1,0.25)=0
    

Effectively, this means the input to A1 must end in 0, 0.25, 0.50, or 0.75.

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

[![Excel formula: Highlight every other row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20every%20other%20row.png "Excel formula: Highlight every other row")](https://exceljet.net/formulas/highlight-every-other-row)

### [Highlight every other row](https://exceljet.net/formulas/highlight-every-other-row)

When you use a formula to apply conditional formatting, the formula is evaluated for every cell in the selection. In this case, there are no addresses in the formula, so, for every cell in the data, the ROW and ISEVEN functions are run. ROW returns the row number of the cell, and ISEVEN returns...

Related functions
-----------------

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20zebra%20stripes%20with%20conditional%20formatting-thumb.png)](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

### [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

In this video, we'll look at how to use conditional formatting to shade every other row in a table. This is sometimes called "zebra striping". In this spreadsheet, we have a table of employees with a small amount of formatting. To get shading on every other row, we could just convert this table to...

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
    
*   [Highlight every other row](https://exceljet.net/formulas/highlight-every-other-row)
    

### Functions

*   [MOD Function](https://exceljet.net/functions/mod-function)
    

### Videos

*   [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)
    

### Articles

*   [Excel Data Validation Guide](https://exceljet.net/articles/excel-data-validation-guide)
    
*   [How to use the MOD function to repeat values](https://exceljet.net/articles/how-to-use-the-mod-function-to-repeat-values)
    

### Training

*   [Conditional Formatting](https://exceljet.net/training/conditional-formatting)
    

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