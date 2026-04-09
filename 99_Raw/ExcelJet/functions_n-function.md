# Excel N function | Exceljet

**Source:** https://exceljet.net/functions/n-function

---

[Skip to main content](https://exceljet.net/functions/n-function#main-content)

[](https://exceljet.net/functions/n-function#)

*   [Previous](https://exceljet.net/functions/istext-function)
    
*   [Next](https://exceljet.net/functions/na-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

N Function
==========

by Dave Bruns · Updated 3 Nov 2023

Related functions 
------------------

[T](https://exceljet.net/functions/t-function)

![Excel N function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20n%20function.png "Excel N function")

Summary
-------

The Excel N function returns a number when given a value. The N function can be used to convert TRUE and FALSE to 1 and 0 respectively. When given a text value, the N function returns zero.

Purpose 
--------

Convert a value to a number

Return value 
-------------

A number or error code

Syntax
------

    =N(value)

*   _value_ - The value to convert to a number.

Using the N function 
---------------------

Use the N function to convert value to a number. The N function takes one [argument](https://exceljet.net/glossary/function-argument)
, _value_, which can be a cell reference, a formula result, or a hardcoded value. Values are converted as shown below. The logical values TRUE and FALSE are converted to 1 and 0, and text values are converted to zero. Numeric values and errors are unaffected.

| Input value | Return value |
| --- | --- |
| Any number | Same number |
| A recognized date | A date in Excel [serial number format](https://exceljet.net/glossary/excel-date) |
| TRUE | 1   |
| FALSE | 0   |
| Error (#VALUE, #N/A, #NUM!, etc.) | Same error code |
| Other values | 0   |

The N function is provided for compatibility with other spreadsheet programs. In most cases, using the N function is unnecessary, because Excel automatically converts values when needed. However, the N function is a simple way to convert TRUE and FALSE to their numeric equivalents, 1 and 0, as mentioned below.

### Examples

The N function converts text values to zero:

    =N("apple") // returns 0
    

Numeric values and errors are not affected:

    =N(100) // returns 100
    =N(5/0) // returns #DIV/0!
    

The N function converts TRUE to 1 and FALSE to zero:

    =N(TRUE) // returns 1
    =N(FALSE) // returns 0
    =N(3>1) // returns 1
    =N(3<1) // returns 0
    

There are several ways to perform this conversion in Excel, which is useful in more advanced formulas. For example, the formula below will return a [count of cells in a range that contain more than 100 characters](https://exceljet.net/formulas/count-cells-over-n-characters)
:

    =SUMPRODUCT(N(LEN(range)>100))
    

[This article](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 explains other ways to convert TRUE and FALSE to 1 and 0.

### Notes

1.  The N function removes text values. The [T function](https://exceljet.net/functions/t-function)
     removes numeric values.

N function examples
-------------------

[![Excel formula: Sum text values like numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20text%20values%20like%20numbers.png "Excel formula: Sum text values like numbers")](https://exceljet.net/formulas/sum-text-values-like-numbers)

### [Sum text values like numbers](https://exceljet.net/formulas/sum-text-values-like-numbers)

The heart of this formula is a basic INDEX and MATCH formula, used to translate text values into numbers as defined in a lookup table. For example, to translate "EX" to the corresponding number, we would use: =INDEX(value,MATCH("EX",code,0)) which would return 4. The twist in this problem however...

[![Excel formula: Count cells over n characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20over%20n%20characters.png "Excel formula: Count cells over n characters")](https://exceljet.net/formulas/count-cells-over-n-characters)

### [Count cells over n characters](https://exceljet.net/formulas/count-cells-over-n-characters)

In this example, the goal is to count the number of cells in a range that are over a certain number of characters in length, where the number ( n ) is provided as a variable in cell F4. This problem can be solved with the SUMPRODUCT and LEN functions like this: =SUMPRODUCT(N(LEN(B5:B15)>F4)) //...

[![Excel formula: Leave a comment in a formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Leave%20a%20comment%20in%20a%20formula.png "Excel formula: Leave a comment in a formula")](https://exceljet.net/formulas/leave-a-comment-in-a-formula)

### [Leave a comment in a formula](https://exceljet.net/formulas/leave-a-comment-in-a-formula)

This is a tricky use of N() that allows you to use it as a way to leave in-cell comments. It only works for formulas that return numeric results. The N function takes a value and returns a number. When given a text value, the N function returns zero. In this case, the primary formula the SUM...

[![Excel formula: Count dates in current month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20dates%20in%20current%20month.png "Excel formula: Count dates in current month")](https://exceljet.net/formulas/count-dates-in-current-month)

### [Count dates in current month](https://exceljet.net/formulas/count-dates-in-current-month)

At the core, this formula uses the COUNTIFS function to count dates that are greater than or equal to the first day of the current month, and less than the first day of the next month. The EOMONTH function is used to create both dates based on the current date, which is supplied by the TODAY...

[![Excel formula: Count visible columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20visible%20columns.png "Excel formula: Count visible columns")](https://exceljet.net/formulas/count-visible-columns)

### [Count visible columns](https://exceljet.net/formulas/count-visible-columns)

There is no direct way to detect a hidden column with a formula in Excel. You might think of using the SUBTOTAL function , but SUBTOTAL only works with vertical ranges. As a result, the approach described in this example is a workaround based on a helper formula that must be entered in a range that...

[![Excel formula: Return array with INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/return%20array%20with%20INDEX%20function.png "Excel formula: Return array with INDEX function")](https://exceljet.net/formulas/return-array-with-index-function)

### [Return array with INDEX function](https://exceljet.net/formulas/return-array-with-index-function)

It is surprisingly tricky to get INDEX to return more than one value to another function. To illustrate, the following formula can be used to return the first three items in the named range "data", when entered as a multi-cell array formula. {=INDEX(data,{1,2,3})} The results can be seen in the...

Related functions
-----------------

[![Excel T function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20t%20function.png "Excel T function")](https://exceljet.net/functions/t-function)

### [T Function](https://exceljet.net/functions/t-function)

The Excel T function returns text when given a text value and an empty string ("") for numbers, dates, and the logical values TRUE and FALSE. You can use the T function to remove values that are not text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Leave a comment in a formula](https://exceljet.net/formulas/leave-a-comment-in-a-formula)
    
*   [Count dates in current month](https://exceljet.net/formulas/count-dates-in-current-month)
    
*   [Count visible columns](https://exceljet.net/formulas/count-visible-columns)
    
*   [Return array with INDEX function](https://exceljet.net/formulas/return-array-with-index-function)
    
*   [Sum text values like numbers](https://exceljet.net/formulas/sum-text-values-like-numbers)
    
*   [Count cells over n characters](https://exceljet.net/formulas/count-cells-over-n-characters)
    

### Functions

*   [T Function](https://exceljet.net/functions/t-function)
    

### Links

*   [Microsoft N function documentation](https://support.office.com/en-us/article/n-function-a624cad1-3635-4208-b54a-29733d1278c9)
    

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