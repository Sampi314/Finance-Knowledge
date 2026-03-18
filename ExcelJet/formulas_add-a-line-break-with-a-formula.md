# Add a line break with a formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/add-a-line-break-with-a-formula

---

[Skip to main content](https://exceljet.net/formulas/add-a-line-break-with-a-formula#main-content)

[](https://exceljet.net/formulas/add-a-line-break-with-a-formula#)

*   [Previous](https://exceljet.net/formulas/abbreviate-names-or-words)
    
*   [Next](https://exceljet.net/formulas/add-line-break-based-on-os)
    

[Text](https://exceljet.net/formulas#Text)

Add a line break with a formula
===============================

by Dave Bruns · Updated 18 Nov 2023

Related functions 
------------------

[CHAR](https://exceljet.net/functions/char-function)

![Excel formula: Add a line break with a formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/add_a_line_break_with_a_formula.png "Excel formula: Add a line break with a formula")

Summary
-------

To add a line break with a formula, you can use the [CHAR function](https://exceljet.net/functions/char-function)
. In the worksheet shown the formula in F5, copied down, is:

    =TEXTJOIN(CHAR(10),1,B5:D5)
    

This formula uses the TEXTJOIN function to add line breaks between three text values. See below for another formula that uses manual concatenation with the ampersand (&) operator.

_Note: To get Excel to respect the line break in a cell, be sure to enable "Wrap text" in the Alignment controls of the Ribbon, or at Format cells > Alignment > Wrap text._

Generic formula
---------------

    =TEXTJOIN(CHAR(10),1,range)

Explanation 
------------

In this example, the goal is to join together three text values separated by line breaks. In Excel, you can use the keyboard shortcut [Alt + Enter](https://exceljet.net/shortcuts/insert-line-break-in-cell)
 to add a line break in a cell that contains text, but the same approach won't work in a formula. The trick is to use the [CHAR function](https://exceljet.net/functions/char-function)
 with the [ASCII code](https://exceljet.net/glossary/ascii)
 10 like this:

    =CHAR(10) // line break

CHAR (10) returns a hidden character that Excel uses as a line break. To use CHAR(10) in a formula you must use [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
.  The article below explains two approaches.

> Note: "Wrap text" [must be enabled](https://exceljet.net/videos/how-to-wrap-text-in-cells-in-excel)
>  for Excel to display the line breaks.

### With TEXTJOIN

One way to join together text values with a line break is to use the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
, which is designed to concatenate values together with a delimiter of your choice. This is the approach seen in the worksheet above, where the formula in cell F5 is:

    =TEXTJOIN(CHAR(10),1,B5:D5)

The inputs to TEXTJOIN are provided as follows:

*   _delimiter_ - given as CHAR(10) which returns a line break character in Excel
*   _ignore\_empty_ - set to 1, to avoid adding extra line breaks when values are empty
*   _text1_ - the range B5:D5, which contains the three text values to join together

As the formula is copied down, it inserts a line break character after Name and Address like this:

Traci Brown¬  
1301 Robinson Court¬  
Saginaw, MI 48607

### Manual concatenation

It is also possible to create the same result with "manual" [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
 using the ampersand (&) [operator](https://exceljet.net/glossary/math-operators)
 like this:

    =B5&CHAR(10)&C5&CHAR(10)&D5

Notice that each cell reference must be joined to the line break manually with an ampersand (&). The result from this formula is exactly the same as the formula above:

Traci Brown¬  
1301 Robinson Court¬  
Saginaw, MI 48607

_Note: make sure you have Wrap Text enabled on cells that contain line breaks._

Related formulas
----------------

[![Excel formula: Count line breaks in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20line%20breaks%20in%20cell.png "Excel formula: Count line breaks in cell")](https://exceljet.net/formulas/count-line-breaks-in-cell)

### [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)

First, the LEN function counts total characters in the cell B5. Next SUBSTITUTE removes all "line returns" from the text in B5 by looking for CHAR(10) which is the character code for the return character in Windows. LEN returns the result inside of a second LEN, which counts characters without...

[![Excel formula: Add line break based on OS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add%20line%20break%20based%20on%20OS.png "Excel formula: Add line break based on OS")](https://exceljet.net/formulas/add-line-break-based-on-os)

### [Add line break based on OS](https://exceljet.net/formulas/add-line-break-based-on-os)

In older versions of Excel (before Excel 2016?), the character used for line breaks is different depending on whether Excel is running on a Mac or Windows computer: On Windows Excel, the line break character is ASCII 10. In older versions of Excel on a Mac, the line break character is ASCII 13...

[![Excel formula: Double quotes inside a formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/double%20quotes%20inside%20a%20formula.png "Excel formula: Double quotes inside a formula")](https://exceljet.net/formulas/double-quotes-inside-a-formula)

### [Double quotes inside a formula](https://exceljet.net/formulas/double-quotes-inside-a-formula)

To include double quotes inside a formula, you can use additional double quotes as escape characters . By escaping a character, you are telling Excel to treat the " character as literal text. You'll also need to include double quotes wherever you would normally in a formula. For example, if cell A1...

[![Excel formula: Replace one delimiter with another](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/replace_one_delimiter_with_another.png "Excel formula: Replace one delimiter with another")](https://exceljet.net/formulas/replace-one-delimiter-with-another)

### [Replace one delimiter with another](https://exceljet.net/formulas/replace-one-delimiter-with-another)

In this example, the goal is to replace the comma-separated values in column B with the line break-separated values seen in column D. In a problem like this, the first step is to identify the delimiter , which is the character (or characters) that separate each value we want to process. In this...

Related functions
-----------------

[![Excel CHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")](https://exceljet.net/functions/char-function)

### [CHAR Function](https://exceljet.net/functions/char-function)

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20concatenate%20with%20line%20breaks-thumb.png)](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)

### [How to concatenate with line breaks](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)

In the real world, you often need to concatenate values in a way that includes line breaks and other punctuation. In this video we'll look at a clever way to make this task easier and less error-prone. A common example of a situation that requires concatenation is assembling a mailing address from...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)
    
*   [Add line break based on OS](https://exceljet.net/formulas/add-line-break-based-on-os)
    
*   [Double quotes inside a formula](https://exceljet.net/formulas/double-quotes-inside-a-formula)
    
*   [Replace one delimiter with another](https://exceljet.net/formulas/replace-one-delimiter-with-another)
    

### Functions

*   [CHAR Function](https://exceljet.net/functions/char-function)
    

### Videos

*   [How to concatenate with line breaks](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)
    

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