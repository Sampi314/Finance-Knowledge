# MAC address format - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/mac-address-format

---

[Skip to main content](https://exceljet.net/formulas/mac-address-format#main-content)

[](https://exceljet.net/formulas/mac-address-format#)

*   [Previous](https://exceljet.net/formulas/join-cells-with-comma)
    
*   [Next](https://exceljet.net/formulas/make-words-plural)
    

[Text](https://exceljet.net/formulas#Text)

MAC address format
==================

by Dave Bruns · Updated 20 Feb 2023

Related functions 
------------------

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[MID](https://exceljet.net/functions/mid-function)

![Excel formula: MAC address format](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/MAC%20address%20format.png "Excel formula: MAC address format")

Summary
-------

To format a MAC address string without delimiters to a MAC address separated by a colon (:) or hyphen (-), you can use a formula based on the [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
, [MID](https://exceljet.net/functions/mid-function)
, and [SEQUENCE](https://exceljet.net/functions/sequence-function)
 functions. In the example shown, the formula in D5, copied down, is:

    =TEXTJOIN(C5,1,MID(B5,SEQUENCE(6,1,1,2),2))
    

The formula returns the formatted strings as seen in column D.

Generic formula
---------------

    =TEXTJOIN(separator,1,MID(A1,SEQUENCE(6,1,1,2),2))

Explanation 
------------

A MAC (Media Access Control) address is a unique identifier assigned to most network adapters. Two common IEEE 802 standards display a MAC address in 6 groups of 2 hexadecimal digits separated by a colon (:) or hyphen (-) like this:

    "01-23-45-67-89-ab"
    "01:23:45:67:89:ab"
    

To format a text string with 12 characters in the same way, you can use a formula like this:

    =TEXTJOIN(C5,1,MID(B5,SEQUENCE(6,1,1,2),2))
    

Working from the inside out, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 is used to generate an array of 6 numbers used as the _start\_num_ argument in the MID function:

    SEQUENCE(6,1,1,2) // returns {1;3;5;7;9;11}
    

These are returned directly to the [MID function](https://exceljet.net/functions/mid-function)
:

    MID(B5,{1;3;5;7;9;11},2)
    

With the text "112233445566" in B5, the MID function returns an array of 6 strings:

    {"11";"22";"33";"44";"55";"66"}
    

This array is returned to the TEXTJOIN function as the _text1_ argument, and with the colon (:) as the delimiter from C5, we have:

    =TEXTJOIN(";",1,{"11";"22";"33";"44";"55";"66"})
    

The TEXTJOIN function concatenates the 6 strings together using a colon, and returns a single string as a final result:

11:22:33:44:55:66

The formula in D6 works exactly the same, except it uses the hyphen in C6 to join the strings:

11-22-33-44-55-66

### Three groups of four

Another standard format is 3 groups of 4 hexadecimal digits, separated with a dot. To create a MAC address in this format, use a formula like this:

    =TEXTJOIN(".",1,MID(B5,SEQUENCE(3,1,1,4),4))
    

SEQUENCE now generates 3 start numbers incremented by 4 characters:

    SEQUENCE(3,1,1,4) // returns {1;5;9}
    

And MID returns 3 strings:

    {"1122";"3344";"5566"}
    

The TEXTJOIN function then concatenates these strings separated with a dot (.) character:

    "1122.3344.5566"
    

Related functions
-----------------

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

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

### Functions

*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    

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