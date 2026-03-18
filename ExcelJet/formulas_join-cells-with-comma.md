# Join cells with comma - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/join-cells-with-comma

---

[Skip to main content](https://exceljet.net/formulas/join-cells-with-comma#main-content)

[](https://exceljet.net/formulas/join-cells-with-comma#)

*   [Previous](https://exceljet.net/formulas/get-unicode-sequence-from-text)
    
*   [Next](https://exceljet.net/formulas/mac-address-format)
    

[Text](https://exceljet.net/formulas#Text)

Join cells with comma
=====================

by Dave Bruns · Updated 15 May 2021

Related functions 
------------------

[TRIM](https://exceljet.net/functions/trim-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

![Excel formula: Join cells with comma](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/join%20cells%20with%20comma_0.png "Excel formula: Join cells with comma")

Summary
-------

To join multiple cell values with a comma, you can use a formula based on the [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
 and [TRIM](https://exceljet.net/functions/trim-function)
 functions. You can use this same approach to concatenate values in cells with any delimiter you like. In the example shown, the formula in G5 is:

    =SUBSTITUTE(TRIM(B5&" "&C5&" "&D5&" "&E5&" "&F5)," ",", ")
    

_Note: the new [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 is a better way to solve this problem. [See below](https://exceljet.net/formulas/join-cells-with-comma#textjoin)
 for more information._

Generic formula
---------------

    =SUBSTITUTE(TRIM(A1&" "&B1&" "&C1&" "&D1&" "&E1)," ",", ")

Explanation 
------------

Working from the inside out, the formula first joins the values the 5 cells to the left using the concatenation operator (&) and a single space between each value:

    B5&" "&C5&" "&D5&" "&E5&" "&F5
    

This part of the formula is annoyingly manual. To speed things up, copy **&" "&** to the clipboard before you start. Then follow this pattern:

\[click\] \[paste\] \[click\] \[paste\] \[click\] \[paste\]

until you get to the last cell reference. It actually goes pretty fast.

The result of this concatenation (before TRIM and SUBSTITUTE run) is a string like this:

    "figs  apples  "
    

Next, the [TRIM function](https://exceljet.net/functions/trim-function)
 is used to "normalize" all spacing. TRIM automatically strips space at the start and end of a given string, and leaves just one space between all words inside the string. This takes care of extra spaces causes by empty cells.

    "figs apples"
    

Finally, the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 is used to replace each space (" ") with a comma and space (", "), returning text like this:

    "figs, apples"
    

### Joining cells with other delimiters

To join cells with another delimiter (separator), just adapt the "new\_text" argument inside SUBSTITUTE. For example, to join cells with a forward slash, use:

    =SUBSTITUTE(TRIM(B7&" "&C7&" "&D7&" "&E7&" "&F7)," ","/")
    

The output will look like this:

    limes/apricots/apricots/limes/figs
    

### TEXTJOIN Function

The [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 is a new function available in [Excel 365](https://exceljet.net/glossary/excel-365)
 and Excel 2019. TEXTJOIN allows you to concatenate a range of cells with a delimiter, and will can also be set to ignore empty cells. To use TEXTJOIN with the example above, the formula is:

    =TEXTJOIN(", ",TRUE,B5:F5)
    

Related formulas
----------------

[![Excel formula: Join first and last name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_first_and_last_names.png "Excel formula: Join first and last name")](https://exceljet.net/formulas/join-first-and-last-name)

### [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)

In this example, the goal is to join different parts of a name (first, middle, last) into a full name. This is an example of concatenation . To concatenate means to join one text value to another with a formula, or in a more general programming language. In a current version of Excel, the simplest...

[![Excel formula: Join date and text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_date_and_text.png "Excel formula: Join date and text")](https://exceljet.net/formulas/join-date-and-text)

### [Join date and text](https://exceljet.net/formulas/join-date-and-text)

In this example, the goal is to join a text string to a formatted date. The challenge is that numbers lose their formatting in Excel when they are concatenated in a formula. For example, if we have the date 31-Dec-1999 in cell B5, and we join B5 to a text string and don't control the date format...

[![Excel formula: Last updated date stamp](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/date%20last%20updated.png "Excel formula: Last updated date stamp")](https://exceljet.net/formulas/last-updated-date-stamp)

### [Last updated date stamp](https://exceljet.net/formulas/last-updated-date-stamp)

The TEXT function can apply number formatting to numbers just like Excel's built-in cell formats for dates, currency, fractions, and so on. However, unlike Excel's cell formatting, the TEXT function works inside a formula and returns a result that is text. You can use TEXT to format numbers that...

[![Excel formula: Add a line break with a formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_a_line_break_with_a_formula.png "Excel formula: Add a line break with a formula")](https://exceljet.net/formulas/add-a-line-break-with-a-formula)

### [Add a line break with a formula](https://exceljet.net/formulas/add-a-line-break-with-a-formula)

In this example, the goal is to join together three text values separated by line breaks. In Excel, you can use the keyboard shortcut Alt + Enter to add a line break in a cell that contains text, but the same approach won't work in a formula. The trick is to use the CHAR function with the ASCII...

Related functions
-----------------

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20concatenate%20with%20line%20breaks-thumb.png)](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)

### [How to concatenate with line breaks](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)

In the real world, you often need to concatenate values in a way that includes line breaks and other punctuation. In this video we'll look at a clever way to make this task easier and less error-prone. A common example of a situation that requires concatenation is assembling a mailing address from...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20concatenation%20to%20clarify%20assumptions-thumb.png)](https://exceljet.net/videos/how-to-use-concatenation-to-clarify-assumptions)

### [How to use concatenation to clarify assumptions](https://exceljet.net/videos/how-to-use-concatenation-to-clarify-assumptions)

One of the most basic and useful features in Excel is the ability to concatenate values with text. CONCATENATE is just a fancy word for "join." In this video we'll look at a simple way to use concatenation with the TEXT formula to highlight assumptions in a break-even model. This model calculates...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20change%20case%20with%20UPPER%2C%20LOWER%20and%20PROPER-thumb.png)](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

### [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

When you're working with text in Excel, you'll frequently need to change case. In this video we'll look at three functions that allow you to easily change case of text in Excel: UPPER, LOWER, and PROPER. In this worksheet, we have two columns that contain names. Column B contains last names in...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)
    
*   [Join date and text](https://exceljet.net/formulas/join-date-and-text)
    
*   [Last updated date stamp](https://exceljet.net/formulas/last-updated-date-stamp)
    
*   [Add a line break with a formula](https://exceljet.net/formulas/add-a-line-break-with-a-formula)
    

### Functions

*   [TRIM Function](https://exceljet.net/functions/trim-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    

### Videos

*   [How to concatenate with line breaks](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)
    
*   [How to use concatenation to clarify assumptions](https://exceljet.net/videos/how-to-use-concatenation-to-clarify-assumptions)
    
*   [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)
    

### Links

*   [Macro to concatenate range by Jon Acampora of ExcelCampus](https://www.excelcampus.com/keyboard-shortcuts/concatenate-range-of-cells/)
    

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