# Highlight numbers that include symbols - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-numbers-that-include-symbols

---

[Skip to main content](https://exceljet.net/formulas/highlight-numbers-that-include-symbols#main-content)

[](https://exceljet.net/formulas/highlight-numbers-that-include-symbols#)

*   [Previous](https://exceljet.net/formulas/highlight-multiples-of-specific-value)
    
*   [Next](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight numbers that include symbols
======================================

by Dave Bruns · Updated 12 Jun 2020

Related functions 
------------------

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[MID](https://exceljet.net/functions/mid-function)

![Excel formula: Highlight numbers that include symbols](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Conditional%20formatting%20numbers%20with%20symbols%20arrows.png "Excel formula: Highlight numbers that include symbols")

Summary
-------

To highlight numbers less than a certain value, including numbers entered as text like "<9", "<10", etc., you can use conditional formatting with a formula strips the symbols as needed and handles the result as a number. In the example shown, "input" is a [named range](https://exceljet.net/glossary/named-range)
 for cell G2.

Generic formula
---------------

    =IF(ISNUMBER(B4),B4<input,IF(LEFT(B4)="<",(MID(B4,2,LEN(B4))+0)<input))

Explanation 
------------

The formula first uses the ISNUMBER function to test if the value is a number, and applies a simple logical if so:

    =IF(ISNUMBER(B4)
    

For any number less than the value in "input", the formula will return TRUE and the conditional formatting will be applied.

However, if the value is not a number, the formula then checks if the first character is a less than symbol (<) using the LEFT function:

    IF(LEFT(B4)="<"
    

If so, the MID function is used to extract everything after the symbol:

    MID(B4,2,LEN(B4)
    

Technically, the LEN function returns a number 1 greater than we need, since it includes the "<" symbol as well. If this bothers you, feel free to subtract 1.

The result of MID is always text so the formula adds zero to force a Excel to convert the text to a number. This number is then compared to the value from "input".

Related formulas
----------------

[![Excel formula: Highlight values greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/%20Highlight%20values%20greater%20than%20or%20less%20than.png "Excel formula: Highlight values greater than")](https://exceljet.net/formulas/highlight-values-greater-than)

### [Highlight values greater than](https://exceljet.net/formulas/highlight-values-greater-than)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. So, in this case the formula =B4>100 is evaluated for each of the 40 cells in B4:G11. Because B4 is entered as a relative address, the...

[![Excel formula: Highlight values between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20between.png "Excel formula: Highlight values between")](https://exceljet.net/formulas/highlight-values-between)

### [Highlight values between](https://exceljet.net/formulas/highlight-values-between)

When you use a formula to apply conditional formatting, the formula is evaluated for each cell in the range, relative to the active cell in the selection at the time the rule is created. So, in this case, if you apply the rule to B4:G11, with B4 as the active cell, the rule is evaluated for each of...

Related functions
-----------------

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Highlight values greater than](https://exceljet.net/formulas/highlight-values-greater-than)
    
*   [Highlight values between](https://exceljet.net/formulas/highlight-values-between)
    

### Functions

*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    

### Articles

*   [Cool things you can do with conditional formatting](https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting)
    
*   [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
    

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