# Hyperlink to first blank cell - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/hyperlink-to-first-blank-cell

---

[Skip to main content](https://exceljet.net/formulas/hyperlink-to-first-blank-cell#main-content)

[](https://exceljet.net/formulas/hyperlink-to-first-blank-cell#)

*   [Previous](https://exceljet.net/formulas/get-pivot-table-subtotal-grouped-date)
    
*   [Next](https://exceljet.net/formulas/hyperlink-to-first-match)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Hyperlink to first blank cell
=============================

by Dave Bruns · Updated 9 Sep 2024

Related functions 
------------------

[HYPERLINK](https://exceljet.net/functions/hyperlink-function)

[CELL](https://exceljet.net/functions/cell-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Hyperlink to first blank cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Hyperlink%20to%20first%20blank%20cell.png "Excel formula: Hyperlink to first blank cell")

Summary
-------

To create hyperlinks to the first match in a lookup, you can use a formula based on the HYPERLINK function, with help from CELL and INDEX and MATCH. In the example shown, the formula in C5 is:

    =HYPERLINK("#"&CELL("address",INDEX(C5:C100,MATCH(9.99E+307,C5:C100)+1)),"First blank")
    

This formula generates a working hyperlink to the first blank cell in column C.

Generic formula
---------------

    =HYPERLINK("#"&CELL("address",INDEX(range,MATCH(bignum,range)+1)),"First blank")

Explanation 
------------

Working from the inside out, we use MATCH to locate the relative position of the last entry in column C:

    MATCH(9.99E+307,C5:C100)
    

Basically, we are giving MATCH a "big number" it will never find in approximate match mode. In this mode, MATCH will "step back" to the last numeric value.

_Note: this works in this case because all values in C are numeric, and there are no blanks. For other situations (text values, etc.), see other "last row" formulas mentioned below. You will need to adjust the MATCH part of the formula to suit your needs._

Next, we use INDEX to get the address of the "entry after the last entry" like this:

    INDEX(C5:C100,6))
    

For the array, we give INDEX C5:C100, which represents the range we care about. For row number, we give INDEX the result returned by MATCH + 1. In this example, this simplifies to:

    INDEX(C5:C100,6)
    

This appears to return the value at C10, but in fact, INDEX returns an address ($C$10), which we extract with the CELL function and concatenate to the "#" character:

    =HYPERLINK("#"&CELL($C$10)
    

In the end, this is what goes into the HYPERLINK function:

    =HYPERLINK("#$C$10","First blank")
    

The HYPERLINK function then constructs a clickable link to cell C10 on the same sheet, with "First blank" as the link text.

Related formulas
----------------

[![Excel formula: Hyperlink to first match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/hyperlink%20to%20first%20match.png "Excel formula: Hyperlink to first match")](https://exceljet.net/formulas/hyperlink-to-first-match)

### [Hyperlink to first match](https://exceljet.net/formulas/hyperlink-to-first-match)

Working from the inside out, we use a standard INDEX and MATCH function to locate the first match of lookup values in column B: INDEX(data,MATCH(B5,data,0)) The MATCH function gets the position of the value in B5 inside the named range data, which for the lookup value "blue" is 3. This result goes...

[![Excel formula: Build hyperlink with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/build%20hyperlink%20with%20VLOOKUP.png "Excel formula: Build hyperlink with VLOOKUP")](https://exceljet.net/formulas/build-hyperlink-with-vlookup)

### [Build hyperlink with VLOOKUP](https://exceljet.net/formulas/build-hyperlink-with-vlookup)

The hyperlink function allows you to create a working link with a formula. It takes two arguments: link\_location and, optionally, friendly\_name . Working from the inside out, VLOOKUP looks up and retrieves a link value from column 2 of the named range "link\_table" (B5:C8). The lookup value comes...

[![Excel formula: Last row in numeric data](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Last%20row%20in%20numeric%20data.png "Excel formula: Last row in numeric data")](https://exceljet.net/formulas/last-row-in-numeric-data)

### [Last row in numeric data](https://exceljet.net/formulas/last-row-in-numeric-data)

When building advanced formulas that use dynamic ranges, it's often necessary to figure out the last location of data in a list. Depending on the data, this could be the last row with data, the last column with data, or the intersection of both. Note: we want the last \*relative position\* inside a...

[![Excel formula: Last row in text data](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Last%20row%20in%20text%20data.png "Excel formula: Last row in text data")](https://exceljet.net/formulas/last-row-in-text-data)

### [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)

This formula uses the MATCH function in approximate match mode to locate the last text value in a range. Approximate match enabled by setting by the 3rd argument in MATCH to 1, or omitting this argument, which defaults to 1. The lookup value is a so-called "big text" (sometimes abbreviated "bigtext...

[![Excel formula: Last row in mixed data with blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20row%20in%20mixed%20data%20with%20blanks.png "Excel formula: Last row in mixed data with blanks")](https://exceljet.net/formulas/last-row-in-mixed-data-with-blanks)

### [Last row in mixed data with blanks](https://exceljet.net/formulas/last-row-in-mixed-data-with-blanks)

When constructing more advanced formulas, it's often necessary to figure out the last location of data in a list. Depending on the data, this could be the last row with data, the last column with data, or the intersection of both. We want the last \*relative position\* inside a given range not the...

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
    
*   [Last row in numeric data](https://exceljet.net/formulas/last-row-in-numeric-data)
    
*   [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)
    
*   [Last row in mixed data with blanks](https://exceljet.net/formulas/last-row-in-mixed-data-with-blanks)
    

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