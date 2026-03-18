# Excel MODE function | Exceljet

**Source:** https://exceljet.net/functions/mode-function

---

[Skip to main content](https://exceljet.net/functions/mode-function#main-content)

[](https://exceljet.net/functions/mode-function#)

*   [Previous](https://exceljet.net/functions/minifs-function)
    
*   [Next](https://exceljet.net/functions/mode.mult-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

MODE Function
=============

by Dave Bruns · Updated 24 Nov 2021

Related functions 
------------------

[AVERAGE](https://exceljet.net/functions/average-function)

[MEDIAN](https://exceljet.net/functions/median-function)

[MODE.SNGL](https://exceljet.net/functions/mode.sngl-function)

[MODE.MULT](https://exceljet.net/functions/mode.mult-function)

![Excel MODE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20mode%20function.png "Excel MODE function")

Summary
-------

The Excel MODE function returns the most frequently occurring number in a numeric data set. For example, =MODE(1,2,4,4,5,5,5,6) returns 5.

Purpose 
--------

Get most frequently occurring number

Return value 
-------------

A number representing the mode.

Syntax
------

    =MODE(number1,[number2],...)

*   _number1_ - A number or cell reference that refers to numeric values.
*   _number2_ - \[optional\] A number or cell reference that refers to numeric values.

Using the MODE function 
------------------------

The MODE function returns the most frequently occurring number in a set of numeric data. If supplied data does not contain any duplicate numbers, the MODE function returns a #N/A error.

The MODE function takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form _number1_, _number2_, _number3_, etc. Arguments can be a hardcoded constant, a cell reference, or a range, in any combination. MODE ignores empty cells, text values, and the logical values TRUE and FALSE. The MODE function will accept up to 255 separate arguments. 

### Examples

MODE returns the most frequently occurring number in supplied data. For example,

    =MODE(1,2,4,4,5,5,5,6) // returns 5
    =MODE(7,8,9,7,9) // returns 7
    

If there are no duplicate numbers, the MODE function returns the #N/A error:

    =MODE(7,9,6,5,3,1,0) // returns #N/A
    

In the example shown, the formula in L5, copied down, is:

    =MODE(B5:J5)
    

_Note: the MODE function is now classified as a "[compatibility function](https://exceljet.net/glossary/compatibility-function)
". Microsoft recommends that [MODE.SNGL](https://exceljet.net/functions/mode.sngl-function)
 or [MODE.MULT](https://exceljet.net/functions/mode.mult-function)
 be used instead._

### Notes

*   If supplied data does not contain duplicate numbers, MODE returns #N/A
*   MODE ignores empty cells, the logical values TRUE and FALSE, and [text](https://exceljet.net/glossary/text-value)
    .
*   Arguments can be numbers, names, [arrays](https://exceljet.net/glossary/array)
    , or references.

MODE function examples
----------------------

[![Excel formula: Conditional mode with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20mode%20with%20criteria.png "Excel formula: Conditional mode with criteria")](https://exceljet.net/formulas/conditional-mode-with-criteria)

### [Conditional mode with criteria](https://exceljet.net/formulas/conditional-mode-with-criteria)

The MODE function has no built-in way to apply criteria. Given a range, it will return the most frequently occurring number in that range. To apply criteria, we use the IF function inside MODE to filter values in a range. In this example, the IF function filters values by group with an expression...

[![Excel formula: Most frequently occurring number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequently%20occurring%20number.png "Excel formula: Most frequently occurring number")](https://exceljet.net/formulas/most-frequently-occurring-number)

### [Most frequently occurring number](https://exceljet.net/formulas/most-frequently-occurring-number)

The MODE function is fully automatic and will return the most frequently occurring number in a set of numbers. For example: =MODE(1,2,4,4,5,5,5,6) // returns 5 In the example shown, we give MODE the range B4:K4, so the formula is solved like this: =MODE(B4:K4) =MODE({1,2,2,1,1,2,2,2,1,1}) =2

[![Excel formula: Most frequently occurring text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequent%20text2.png "Excel formula: Most frequently occurring text")](https://exceljet.net/formulas/most-frequently-occurring-text)

### [Most frequently occurring text](https://exceljet.net/formulas/most-frequently-occurring-text)

Working from the inside out, the MATCH function matches the range against itself. That is, we give the MATCH function the same range for lookup value and lookup array (B5:F5). Because the lookup value contains more than one value (an array), MATCH returns an array of results, where each number...

[![Excel formula: List most frequently occurring numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20most%20frequently%20occuring%20numbers.png "Excel formula: List most frequently occurring numbers")](https://exceljet.net/formulas/list-most-frequently-occurring-numbers)

### [List most frequently occurring numbers](https://exceljet.net/formulas/list-most-frequently-occurring-numbers)

The core of this formula is the MODE function, which returns the most frequently occurring number in a range or array. The rest of the formula just constructs a filtered array for MODE to use in each row. The expanding range $D$4:D4 works to exclude numbers already output in $D$4:D4. Working from...

[![Excel formula: Most frequent text with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequent%20text%20with%20criteria.png "Excel formula: Most frequent text with criteria")](https://exceljet.net/formulas/most-frequent-text-with-criteria)

### [Most frequent text with criteria](https://exceljet.net/formulas/most-frequent-text-with-criteria)

In this example, the goal is to return the most frequently occurring text based on one or more supplied criteria. Working from the inside out, we use the MATCH function to match the text range against itself, by giving MATCH the same range for lookup value and lookup array, with zero for match type...

Related functions
-----------------

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel MEDIAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20median%20function.png "Excel MEDIAN function")](https://exceljet.net/functions/median-function)

### [MEDIAN Function](https://exceljet.net/functions/median-function)

The Excel MEDIAN function returns the median (middle number) in the supplied set of data. For example, =MEDIAN(1,2,3,4,5) returns 3.

[![Excel MODE.SNGL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mode.sngl%20function.png "Excel MODE.SNGL function")](https://exceljet.net/functions/mode.sngl-function)

### [MODE.SNGL Function](https://exceljet.net/functions/mode.sngl-function)

The Excel MODE.SNGL function returns the most frequently occurring number in a numeric data set. For example, =MODE.SNGL(1,2,4,4,5,5,5,6) returns 5.

[![Excel MODE.MULT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mode.mult%20function.png "Excel MODE.MULT function")](https://exceljet.net/functions/mode.mult-function)

### [MODE.MULT Function](https://exceljet.net/functions/mode.mult-function)

The Excel MODE.MULT function returns an array of the most frequently occurring numbers in a numeric data set. For example, =MODE.MULT(1,2,3,3,4,5,5) returns {3;5}, because there are two modes, 3 and 5.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Most frequently occurring text](https://exceljet.net/formulas/most-frequently-occurring-text)
    
*   [List most frequently occurring numbers](https://exceljet.net/formulas/list-most-frequently-occurring-numbers)
    
*   [Most frequent text with criteria](https://exceljet.net/formulas/most-frequent-text-with-criteria)
    
*   [Conditional mode with criteria](https://exceljet.net/formulas/conditional-mode-with-criteria)
    
*   [Most frequently occurring number](https://exceljet.net/formulas/most-frequently-occurring-number)
    

### Functions

*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [MEDIAN Function](https://exceljet.net/functions/median-function)
    
*   [MODE.SNGL Function](https://exceljet.net/functions/mode.sngl-function)
    
*   [MODE.MULT Function](https://exceljet.net/functions/mode.mult-function)
    

### Links

*   [Microsoft MODE function documentation](https://support.office.com/en-us/article/mode-function-e45192ce-9122-4980-82ed-4bdc34973120)
    

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