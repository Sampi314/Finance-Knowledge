# Hyperlink to first match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/hyperlink-to-first-match

---

[Skip to main content](https://exceljet.net/formulas/hyperlink-to-first-match#main-content)

[](https://exceljet.net/formulas/hyperlink-to-first-match#)

*   [Previous](https://exceljet.net/formulas/hyperlink-to-first-blank-cell)
    
*   [Next](https://exceljet.net/formulas/increment-a-calculation-with-row-or-column)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Hyperlink to first match
========================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[HYPERLINK](https://exceljet.net/functions/hyperlink-function)

[CELL](https://exceljet.net/functions/cell-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Hyperlink to first match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/hyperlink%20to%20first%20match.png "Excel formula: Hyperlink to first match")

Summary
-------

To create hyperlinks to the first match in a lookup, you can use a formula based on the HYPERLINK function, with help from CELL, INDEX and MATCH. In the example shown, the formula in C5 is:

    =HYPERLINK("#"&CELL("address",INDEX(data,MATCH(B5,data,0))),B5)
    

This formula generates a working hyperlink to the first match found of the lookup value in the named range "data".

Generic formula
---------------

    =HYPERLINK("#"&CELL("address",INDEX(data,MATCH(val,data,0))),val)

Explanation 
------------

Working from the inside out, we use a standard INDEX and MATCH function to locate the first match of lookup values in column B:

    INDEX(data,MATCH(B5,data,0))
    

The MATCH function gets the position of the value in B5 inside the named range data, which for the lookup value "blue" is 3. This result goes into the INDEX function as row\_num, with "data" as the array:

    INDEX(data,3)
    

This appears to return the value "blue" but in fact the INDEX function returns the address E6. We extract this address using the CELL function, which is concatenated to the "#" character:

    =HYPERLINK("#"&CELL(E6,B5)
    

In this end, this is what goes into the HYPERLINK function:

    =HYPERLINK("#$E$6","blue")
    

The HYPERLINK function then constructs a clickable link to cell E6 on the same sheet, with "blue" as the link text.

Related formulas
----------------

[![Excel formula: Build hyperlink with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/build%20hyperlink%20with%20VLOOKUP.png "Excel formula: Build hyperlink with VLOOKUP")](https://exceljet.net/formulas/build-hyperlink-with-vlookup)

### [Build hyperlink with VLOOKUP](https://exceljet.net/formulas/build-hyperlink-with-vlookup)

The hyperlink function allows you to create a working link with a formula. It takes two arguments: link\_location and, optionally, friendly\_name . Working from the inside out, VLOOKUP looks up and retrieves a link value from column 2 of the named range "link\_table" (B5:C8). The lookup value comes...

Related functions
-----------------

[![Excel HYPERLINK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hyperlink%20function.png "Excel HYPERLINK function")](https://exceljet.net/functions/hyperlink-function)

### [HYPERLINK Function](https://exceljet.net/functions/hyperlink-function)

The Excel HYPERLINK function returns a hyperlink to a given destination. You can use HYPERLINK to create a clickable hyperlink with a formula. The HYPERLINK function can build links to workbook locations, pages on the internet, or files on network servers....

[![Excel CELL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20cell%20function.png "Excel CELL function")](https://exceljet.net/functions/cell-function)

### [CELL Function](https://exceljet.net/functions/cell-function)

The Excel CELL function returns information about a cell in a worksheet. The type of information to be returned is specified as _info\_type_. CELL can get things like address and filename, as well as detailed info about the formatting used in the cell. See below for a full list of...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Build hyperlink with VLOOKUP](https://exceljet.net/formulas/build-hyperlink-with-vlookup)
    

### Functions

*   [HYPERLINK Function](https://exceljet.net/functions/hyperlink-function)
    
*   [CELL Function](https://exceljet.net/functions/cell-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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