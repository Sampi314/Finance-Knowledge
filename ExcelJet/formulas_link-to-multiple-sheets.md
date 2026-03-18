# Link to multiple sheets - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/link-to-multiple-sheets

---

[Skip to main content](https://exceljet.net/formulas/link-to-multiple-sheets#main-content)

[](https://exceljet.net/formulas/link-to-multiple-sheets#)

*   [Previous](https://exceljet.net/formulas/leave-a-comment-in-a-formula)
    
*   [Next](https://exceljet.net/formulas/list-most-frequently-occurring-numbers)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Link to multiple sheets
=======================

by Dave Bruns · Updated 31 Dec 2019

Related functions 
------------------

[HYPERLINK](https://exceljet.net/functions/hyperlink-function)

[CELL](https://exceljet.net/functions/cell-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Link to multiple sheets](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/link%20to%20multiple%20sheets.png "Excel formula: Link to multiple sheets")

Summary
-------

To build links to multiple sheets in a workbook, you can use the HYPERLINK function. In the example shown, the formula in D5, copied down, is:

    =HYPERLINK("#"&B5&"!"&C5,"Link")
    

This formula generates a working hyperlink to cell A1 in each of the 9 worksheets as shown.

Generic formula
---------------

    =HYPERLINK("#"&sheet&"!"&cell,"linktext")

Explanation 
------------

This formula relies on [concatenation](https://exceljet.net/glossary/concatenation)
 to assemble a valid location for the HYPERLINK function.

In cell D5, the link location argument is created like this:

    "#"&B5&"!"&C5 // returns ""#Sheet1!A1""
    

which returns the string "#Sheet1!A1". The formula then resolves to:

    =HYPERLINK("#Sheet1!A1","Link")
    

Which returns a valid link.

The cell value in column C is entirely arbitrary and can be any cell you like. It could also be hardcoded into the formula as a string like this:

    =HYPERLINK("#"&B5&"!A1","Link")
    

_Note: The hash character (#) at the start of the sheet name is required. For more link syntax examples, see [HYPERLINK](https://exceljet.net/functions/hyperlink-function)
._

Related formulas
----------------

[![Excel formula: Hyperlink to first match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/hyperlink%20to%20first%20match.png "Excel formula: Hyperlink to first match")](https://exceljet.net/formulas/hyperlink-to-first-match)

### [Hyperlink to first match](https://exceljet.net/formulas/hyperlink-to-first-match)

Working from the inside out, we use a standard INDEX and MATCH function to locate the first match of lookup values in column B: INDEX(data,MATCH(B5,data,0)) The MATCH function gets the position of the value in B5 inside the named range data, which for the lookup value "blue" is 3. This result goes...

[![Excel formula: Build hyperlink with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/build%20hyperlink%20with%20VLOOKUP.png "Excel formula: Build hyperlink with VLOOKUP")](https://exceljet.net/formulas/build-hyperlink-with-vlookup)

### [Build hyperlink with VLOOKUP](https://exceljet.net/formulas/build-hyperlink-with-vlookup)

The hyperlink function allows you to create a working link with a formula. It takes two arguments: link\_location and, optionally, friendly\_name . Working from the inside out, VLOOKUP looks up and retrieves a link value from column 2 of the named range "link\_table" (B5:C8). The lookup value comes...

[![Excel formula: Hyperlink to first blank cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Hyperlink%20to%20first%20blank%20cell.png "Excel formula: Hyperlink to first blank cell")](https://exceljet.net/formulas/hyperlink-to-first-blank-cell)

### [Hyperlink to first blank cell](https://exceljet.net/formulas/hyperlink-to-first-blank-cell)

Working from the inside out, we use MATCH to locate the relative position of the last entry in column C: MATCH(9.99E+307,C5:C100) Basically, we are giving MATCH a "big number" it will never find in approximate match mode. In this mode, MATCH will "step back" to the last numeric value. Note: this...

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

*   [Hyperlink to first match](https://exceljet.net/formulas/hyperlink-to-first-match)
    
*   [Build hyperlink with VLOOKUP](https://exceljet.net/formulas/build-hyperlink-with-vlookup)
    
*   [Hyperlink to first blank cell](https://exceljet.net/formulas/hyperlink-to-first-blank-cell)
    

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