# Pad text to equal length - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/pad-text-to-equal-length

---

[Skip to main content](https://exceljet.net/formulas/pad-text-to-equal-length#main-content)

[](https://exceljet.net/formulas/pad-text-to-equal-length#)

*   [Previous](https://exceljet.net/formulas/number-to-words)
    
*   [Next](https://exceljet.net/formulas/remove-characters-from-right)
    

[Text](https://exceljet.net/formulas#Text)

Pad text to equal length
========================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[REPT](https://exceljet.net/functions/rept-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: Pad text to equal length](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/pad%20text%20to%20equal%20length.png "Excel formula: Pad text to equal length")

Summary
-------

To pad text to an equal length using another character, you can use a formula based on the [REPT](https://exceljet.net/functions/rept-function)
 and [LEN](https://exceljet.net/functions/len-function)
 functions. In the example shown, a formula is used to append a variable number of asterisks (\*) to values in column B so that the final result is always 12 characters in length. The formula in C5 is:

    =B5&REPT("*",12-LEN(B5))
    

Generic formula
---------------

    =A1&REPT("*",count-LEN(A1))

Explanation 
------------

This formula concatenates the original value in column B to a string of asterisks (\*) assembled with the REPT function so that the final result is always 12 characters:

    REPT("*",12-LEN(B5))
    

Inside the REPT function, the text to repeat is provided as a single asterisk ("\*"). The number of asterisks needed for each value is determined with the LEN function in this bit of code here:

    12-LEN(B5)
    

We start with 12, then subtract the length of the text in column B. In cell B5, "Sebastian" is 9 characters, so the result is 3. The formula is evaluated like this:

    ="Sebastian"&REPT("*",12-LEN(B5))
    ="Sebastian"&REPT("*",12-9)
    ="Sebastian"&REPT("*",3)
    ="Sebastian"&"***"
    ="Sebastian***"
    

The results in column C are formatted with a monospaced font (Courier New) to clearly show all strings are the same length.

Related formulas
----------------

[![Excel formula: Conditional message with REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20message%20with%20REPT.png "Excel formula: Conditional message with REPT function")](https://exceljet.net/formulas/conditional-message-with-rept-function)

### [Conditional message with REPT function](https://exceljet.net/formulas/conditional-message-with-rept-function)

This formula uses boolean logic to output a conditional message. If the value in column C is less than 100, the formula returns "low". If not, the formula returns an empty string (""). Boolean logic is a technique of handling TRUE and FALSE values like 1 and 0. In cell C5, the formula is evaluated...

Related functions
-----------------

[![Excel REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rept%20function.png "Excel REPT function")](https://exceljet.net/functions/rept-function)

### [REPT Function](https://exceljet.net/functions/rept-function)

The Excel REPT function repeats characters a given number of times. For example, =REPT("x",5) returns "xxxxx".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Conditional message with REPT function](https://exceljet.net/formulas/conditional-message-with-rept-function)
    

### Functions

*   [REPT Function](https://exceljet.net/functions/rept-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

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