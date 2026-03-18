# Basic outline numbering - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/basic-outline-numbering

---

[Skip to main content](https://exceljet.net/formulas/basic-outline-numbering#main-content)

[](https://exceljet.net/formulas/basic-outline-numbering#)

*   [Previous](https://exceljet.net/formulas/basic-numeric-sort-formula)
    
*   [Next](https://exceljet.net/formulas/basic-text-sort-formula)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Basic outline numbering
=======================

by Dave Bruns · Updated 4 Dec 2018

Related functions 
------------------

[COUNTA](https://exceljet.net/functions/counta-function)

[MID](https://exceljet.net/functions/mid-function)

[FIND](https://exceljet.net/functions/find-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: Basic outline numbering](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/basic%20outline%20numbering.png "Excel formula: Basic outline numbering")

Summary
-------

To generate basic outline numbering you can use a formula based several Excel functions, including COUNTA, IF, MID, FIND, and LEN. In the example shown, the formula in D5 is:

    =COUNTA($B$5:B5)&"."&IF(B5<>"",1,MID(D4,FIND(".",D4)+1,LEN(D4))+1)
    

_Note: this formula will only handle a 2-level outline._

Explanation 
------------

At the core, this formula builds a level 1 and level 2 number and [concatenates](https://exceljet.net/glossary/concatenation)
 the two numbers together with a period (".") as a separator. The result is a value like "1.1". The "level 1" number is generated with COUNTA like this:

    =COUNTA($B$5:B5)
    

Note the range is an [expanding reference](https://exceljet.net/glossary/expanding-reference)
, so it will expand as it is copied down the column.

The "level 2" number is generated with this code:

    IF(B5<>"",1,MID(D4,FIND(".",D4)+1,LEN(D4))+1)
    

Here, the IF function is used to check the contents of B5. If B5 is not blank, it means we have a new level 1 heading and IF returns 1. In other words, every time we have a new level 1 entry, we restart level 2 numbering at 1.

If the B5 \*is\* blank we need to increment the level 2 number using the value in the cell above. This is a bit tricky, because the outline number is a text string, not a number. That means we need to extract the value with a text function before we can increment. To do this, we use the MID function to extract all text to the right of the period ("."), which we locate with the FIND function:

    MID(D4,FIND(".",D4)+1,LEN(D4))+1
    

The LEN function is used as a simple way to guarantee all characters after the period are extracted. Notice we then add 1 directly to the result, which is still text. This math operation causes Excel to coerce the text to a number, so the result is an incremented number. Finally, the level 1 and level 2 numbers are concatenated together with a period (".") as a separator.

Related formulas
----------------

[![Excel formula: Automatic row numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/automatic_row_numbers.png "Excel formula: Automatic row numbers")](https://exceljet.net/formulas/automatic-row-numbers)

### [Automatic row numbers](https://exceljet.net/formulas/automatic-row-numbers)

In this example, the goal is to create automatic row numbers starting in cell B5 that match the data entered in column C. When new data is added to the list, the row numbers should increase as required. If items are deleted, the row numbers should respond accordingly. This has traditionally been a...

Related functions
-----------------

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

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

*   [Automatic row numbers](https://exceljet.net/formulas/automatic-row-numbers)
    

### Functions

*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
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