# Rank with ordinal suffix - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/rank-with-ordinal-suffix

---

[Skip to main content](https://exceljet.net/formulas/rank-with-ordinal-suffix#main-content)

[](https://exceljet.net/formulas/rank-with-ordinal-suffix#)

*   [Previous](https://exceljet.net/formulas/rank-values-by-month)
    
*   [Next](https://exceljet.net/formulas/rank-without-ties)
    

[Rank](https://exceljet.net/formulas#Rank)

Rank with ordinal suffix
========================

by Dave Bruns · Updated 7 Jul 2018

Related functions 
------------------

[CHOOSE](https://exceljet.net/functions/choose-function)

[ABS](https://exceljet.net/functions/abs-function)

[MOD](https://exceljet.net/functions/mod-function)

![Excel formula: Rank with ordinal suffix](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/rank%20with%20ordinal%20suffix.png "Excel formula: Rank with ordinal suffix")

Summary
-------

To add an ordinal suffix to a number (i.e. 1st, 2nd, 3rd, etc.) you can use a formula based on the CHOOSE function to assign the suffix.

In the example shown, the formula in C5 is:

    =CHOOSE(B5,"st","nd","rd","th","th","th","th","th","th","th")
    

Generic formula
---------------

    =CHOOSE(number,"st","nd","rd","th","th","th","th","th","th","th")

Explanation 
------------

Ordinal numbers represent position or rank in a sequential order. They are normally written using a number + letter suffix: 1st, 2nd, 3rd, etc.

To get an ordinal suffix for a small set of numbers, you can use the CHOOSE function like this:

    =CHOOSE(B5,"st","nd","rd","th","th","th","th","th","th","th")
    

Here CHOOSE simply picks up a number from column B and uses that number as an index to retrieve the right suffix.

### A universal formula

With a larger range of numbers it's not practical to keep adding values to CHOOSE. In that case, you can switch to a more complicated formula that uses the MOD function:

    =IF(AND(MOD(ABS(A1),100)>10,MOD(ABS(A1),100)<14),"th",
    CHOOSE(MOD(ABS(A1),10)+1,"th","st","nd","rd","th","th","th","th","th","th"))
    

This formula first uses MOD with AND to "trap" the case of numbers like 11, 12, 13, 111, 112, 113, etc that have a non-standard suffix with is always "th". All other numbers use the 10 suffix values inside CHOOSE.

The ABS function is used to handle negative numbers as well as positive numbers.

### Concatenate suffix to number

You can concatenate (join) the suffix directly using either formula above. For example to add an ordinal suffix to a number 1-10 in A1:

    =A1&CHOOSE(A1,"st","nd","rd","th","th","th","th","th","th","th")
    

But be aware that doing so will change the number into a text value.

Related formulas
----------------

[![Excel formula: Rank function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20function%20example1.png "Excel formula: Rank function example")](https://exceljet.net/formulas/rank-function-example)

### [Rank function example](https://exceljet.net/formulas/rank-function-example)

You can use the RANK function to rank numeric values. RANK has two modes of operation: ranking values where the largest value is #1 (order = 0), and ranking values where the lowest value is #1 (order = 1). In this case, we are ranking test scores, so the highest value should rank #1, so we omit the...

[![Excel formula: Rank race results](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20race%20results2.png "Excel formula: Rank race results")](https://exceljet.net/formulas/rank-race-results)

### [Rank race results](https://exceljet.net/formulas/rank-race-results)

You can use the RANK function to rank numeric values. RANK has two modes of operation: ranking values so that the largest value is ranked #1 (order = 0), and ranking values so that the smallest value is #1 (order = 1). In this case, we are ranking race times. The lowest/fastest value should rank #1...

Related functions
-----------------

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

[![Excel ABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20abs%20function.png "Excel ABS function")](https://exceljet.net/functions/abs-function)

### [ABS Function](https://exceljet.net/functions/abs-function)

The Excel ABS function returns the absolute value of a number. ABS converts negative numbers to positive numbers, and positive numbers are unaffected.

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Rank function example](https://exceljet.net/formulas/rank-function-example)
    
*   [Rank race results](https://exceljet.net/formulas/rank-race-results)
    

### Functions

*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    
*   [ABS Function](https://exceljet.net/functions/abs-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    

### Links

*   [Ordinal suffixes in Excel (Chip Pearson)](http://www.cpearson.com/excel/Ordinal.aspx)
    

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