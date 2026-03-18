# Double quotes inside a formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/double-quotes-inside-a-formula

---

[Skip to main content](https://exceljet.net/formulas/double-quotes-inside-a-formula#main-content)

[](https://exceljet.net/formulas/double-quotes-inside-a-formula#)

*   [Previous](https://exceljet.net/formulas/count-total-words-in-a-range)
    
*   [Next](https://exceljet.net/formulas/encode-unicode-sequence-into-text)
    

[Text](https://exceljet.net/formulas#Text)

Double quotes inside a formula
==============================

by Dave Bruns · Updated 5 Apr 2020

Related functions 
------------------

[CHAR](https://exceljet.net/functions/char-function)

![Excel formula: Double quotes inside a formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/double%20quotes%20inside%20a%20formula.png "Excel formula: Double quotes inside a formula")

Summary
-------

To include double quotes inside a formula, you can use additional double quotes. In the example shown, the formula in C5 is:

     ="The movie """ &B5 &""" is good."
    

Generic formula
---------------

    =""""&A1&""""

Explanation 
------------

To include double quotes inside a formula, you can use additional double quotes as _escape characters_. By escaping a character, you are telling Excel to treat the " character as literal text. You'll also need to include double quotes wherever you would normally in a formula.

For example, if cell A1 contains the text: The Graduate and you want wrap that text inside double quotes (""), you can use this formula:

    =""""&A1&""""
    

Because the text on either side of A1 consists of only of a double quote, you need """" . The outer quotes (1 & 4) tell Excel this is text, the 2nd quote tells Excel to escape the next character, and the 3rd quote is displayed.

If you want to add the movie to other text to create, you can concatenate the movie title inside double quotes with a formula like this:

    ="The 1960's movie """ &A1&""" is famous"
    

The result: _The 1960's movie "The Graduate" is famous_

Working with extra double quotes can get confusing fast, so another way to do the same thing is to use the [CHAR function](https://exceljet.net/functions/char-function)
 with the number 34:

    ="The 1960's movie "&CHAR(34)&A1&CHAR(34)&" is famous"
    

In this case, CHAR(34) returns the double quote character (") which is included in the result as literal text.

CHAR is handy for adding other text that is hard to work with in a formula as well. You can use CHAR(10) to insert a line break character into a formula on Windows. On a Mac, use CHAR(13):

    =CHAR(10) // win line break
    =CHAR(13) // mac line break
    

Related formulas
----------------

[![Excel formula: Add a line break with a formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_a_line_break_with_a_formula.png "Excel formula: Add a line break with a formula")](https://exceljet.net/formulas/add-a-line-break-with-a-formula)

### [Add a line break with a formula](https://exceljet.net/formulas/add-a-line-break-with-a-formula)

In this example, the goal is to join together three text values separated by line breaks. In Excel, you can use the keyboard shortcut Alt + Enter to add a line break in a cell that contains text, but the same approach won't work in a formula. The trick is to use the CHAR function with the ASCII...

Related functions
-----------------

[![Excel CHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")](https://exceljet.net/functions/char-function)

### [CHAR Function](https://exceljet.net/functions/char-function)

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Add a line break with a formula](https://exceljet.net/formulas/add-a-line-break-with-a-formula)
    

### Functions

*   [CHAR Function](https://exceljet.net/functions/char-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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