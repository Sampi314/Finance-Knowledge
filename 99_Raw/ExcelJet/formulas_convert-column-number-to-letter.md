# Convert column number to letter - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-column-number-to-letter

---

[Skip to main content](https://exceljet.net/formulas/convert-column-number-to-letter#main-content)

[](https://exceljet.net/formulas/convert-column-number-to-letter#)

*   [Previous](https://exceljet.net/formulas/convert-column-letter-to-number)
    
*   [Next](https://exceljet.net/formulas/convert-expense-time-units)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Convert column number to letter
===============================

by Dave Bruns · Updated 17 Oct 2023

Related functions 
------------------

[ADDRESS](https://exceljet.net/functions/address-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

![Excel formula: Convert column number to letter](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20column%20number%20to%20letter_0.png "Excel formula: Convert column number to letter")

Summary
-------

To convert a column number to an Excel column letter (e.g. A, B, C, etc.) you can use a formula based on the [ADDRESS](https://exceljet.net/functions/address-function)
 and [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
 functions. In the example shown, the formula in C5, copied down, is:

    =SUBSTITUTE(ADDRESS(1,B5,4),"1","")
    

The result is the column reference as one or more letters, returned as a text string.

Generic formula
---------------

    =SUBSTITUTE(ADDRESS(1,number,4),"1","")

Explanation 
------------

In this example, the goal is to convert an ordinary number into a column reference expressed in letters. For example, the number 1 should return "A", the number 2 should return "B", the number 26 should return "Z", etc. The challenge is that Excel can handle over 16,000 columns, so the number of letter combinations is large. One way to solve this problem is to construct a valid address with the number and extract just the column from the address. This is the approach explained below. For reference, the formula in C5 is:

    =SUBSTITUTE(ADDRESS(1,B5,4),"1","")
    

### ADDRESS function

Working from the inside out, the first step is to construct an address that contains the correct column reference. We can do this with the [ADDRESS function](https://exceljet.net/functions/address-function)
, which will return the address for a cell based on a given row and column number. For example:

    =ADDRESS(1,1) // returns "$A$1"
    =ADDRESS(1,2) // returns "$B$1"
    =ADDRESS(1,26) // returns "$Z$1"
    

By providing 4 for the optional _abs\_num_ [argument](https://exceljet.net/glossary/function-argument)
, we can get a relative reference:

    =ADDRESS(1,1,4) // returns "A1"
    =ADDRESS(1,2,4) // returns "B1"
    =ADDRESS(1,26,4) // returns "Z1"
    

Note the result from ADDRESS is always a [text string](https://exceljet.net/glossary/text-value)
. We don't particularly care about the row number, we only care about the column number, so we use 1 for _row\_num_ in all cases. In the worksheet shown, we get the column number from column B and use 1 for the row number like this:

    ADDRESS(1,B5,4)
    

As the formula is copied down, ADDRESS creates a valid address using each number in column B. The maximum number of columns in an Excel worksheet is 16,384, so the final column in a worksheet is "XFD".

### SUBSTITUTE function

Now that we have an address with the column reference we want, we simply need to remove the row number. One way to do this is with the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
. For example, assuming we have an address like "A1", we can use SUBSTITUTE like this:

    =SUBSTITUTE("A1","1","") // returns "A"
    

We are telling SUBSTITUTE to look for "1" and replace it with an [empty string](https://exceljet.net/glossary/empty-string)
 (""). We can confidently do this in all cases because we've hardcoded the row number as 1 inside the ADDRESS function. The final formula in C5 is:

    =SUBSTITUTE(ADDRESS(1,B5,4),"1","")
    

In brief, ADDRESS creates the cell reference and returns the result to SUBSTITUTE, which removes the "1".

### TEXTBEFORE function

A cleaner way to extract the column reference from the address is to use the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
 like this:

    =TEXTBEFORE(ADDRESS(1,B5,4),"1")
    

Here, we treat "1" as a delimiter and ask TEXTBEFORE for all text before the delimiter. The result from this formula is the same as above, but the configuration is a bit simpler.

Related formulas
----------------

[![Excel formula: Convert column letter to number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20column%20letter%20to%20number.png "Excel formula: Convert column letter to number")](https://exceljet.net/formulas/convert-column-letter-to-number)

### [Convert column letter to number](https://exceljet.net/formulas/convert-column-letter-to-number)

The first step is to construct a standard "A1" style reference using the column letter, by adding a "1" with concatenation: B5...

Related functions
-----------------

[![Excel ADDRESS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20address%20function.png "Excel ADDRESS function")](https://exceljet.net/functions/address-function)

### [ADDRESS Function](https://exceljet.net/functions/address-function)

The Excel ADDRESS function returns the address for a cell based on a given row and column number. For example, =ADDRESS(1,1) returns $A$1. ADDRESS can return an address in relative, mixed, or absolute format, and can be used to construct a cell reference inside a formula.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Convert column letter to number](https://exceljet.net/formulas/convert-column-letter-to-number)
    

### Functions

*   [ADDRESS Function](https://exceljet.net/functions/address-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    

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