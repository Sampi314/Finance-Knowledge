# Get cell content at given row and column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-cell-content-at-given-row-and-column

---

[Skip to main content](https://exceljet.net/formulas/get-cell-content-at-given-row-and-column#main-content)

[](https://exceljet.net/formulas/get-cell-content-at-given-row-and-column#)

*   [Previous](https://exceljet.net/formulas/get-all-matches-cell-contains)
    
*   [Next](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get cell content at given row and column
========================================

by Dave Bruns · Updated 1 May 2023

Related functions 
------------------

[ADDRESS](https://exceljet.net/functions/address-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

[INDEX](https://exceljet.net/functions/index-function)

![Excel formula: Get cell content at given row and column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_cell_content_at_given_row_and_column.png "Excel formula: Get cell content at given row and column")

Summary
-------

To retrieve the cell value at a specific row and column number, you can use the [ADDRESS function](https://exceljet.net/functions/address-function)
 together with the [INDIRECT function](https://exceljet.net/functions/indirect-function)
. In the example shown, the formula in G6 is:

    =INDIRECT(ADDRESS(G4,G5))
    

The result is "Mango", the value in cell C9, at row 9 and column 3 of the worksheet. Although this is one way to get the value of a cell at a known location, it is not an optimal approach. Read more below.

Generic formula
---------------

    =INDIRECT(ADDRESS(row,col))

Explanation 
------------

The goal is to retrieve the value of a cell at a given row and column location, which are entered in cells G5 and G4, respectively. There are several ways to go about this, depending on your needs. See below for options.

### ADDRESS and INDIRECT

In the example worksheet, the ADDRESS function is combined with the INDIRECT function to solve this problem with the following formula:

    =INDIRECT(ADDRESS(G4,G5))
    

The [ADDRESS function](https://exceljet.net/functions/address-function)
 returns the address for a cell based on a given row and column number like this:

    =ADDRESS(1,1) // returns $A$1
    =ADDRESS(1,2) // returns $B$1
    =ADDRESS(2,1) // returns $A$2
    =ADDRESS(2,2) // returns $B$2

_Note: ADDRESS can return references in different formats, [see](https://exceljet.net/functions/address-function)
 here for details._

In the example shown, the ADDRESS function returns the value "$C$9" inside INDIRECT:

    =INDIRECT(ADDRESS(9,3))
    =INDIRECT("$C$9")
    

The [INDIRECT function](https://exceljet.net/functions/indirect-function)
 converts a text value into a valid reference. INDIRECT converts the text "$C$9" into the cell _reference_ $C$9 and returns "Mango" as the final result:

    =INDIRECT("$C$9")
    =$C$9
    ="Mango"

While this formula works, there is a better way to retrieve the cell value at a known location in Excel.

_Note: INDIRECT is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and can cause performance problems in more complicated worksheets._

### INDEX function

The [INDEX function](https://exceljet.net/functions/index-function)
 is well-known in Excel because it is part of [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, a common way to perform lookup operations in Excel. But INDEX can also be used by itself to retrieve values at known coordinates. To solve this problem, we can give the INDEX function a range that begins at A1, and includes the cells that need to be referenced like this:

    =INDEX(A1:E100,9,3) // returns "Mango"
    

As before, the result is "Mango" and this is a much better example of how to retrieve a value in Excel. Replacing the hardcoded row and column numbers above with worksheet references we have:

    =INDEX(A1:E100,G4,G5)
    

This formula returns the same result seen in the screenshot. If row or column numbers change, the INDEX function returns a new result. Note that the size of the range we give INDEX is arbitrary, but it must start at A1 and include the data you wish to reference.

_Note: In most cases, INDEX is not used by itself in a formula because the row and column numbers are often unknown. Instead, INDEX is combined with the [MATCH function](https://exceljet.net/functions/match-function)
, which calculates the required row and column positions. Read more [here](https://exceljet.net/articles/index-and-match)
._

Related formulas
----------------

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

Related functions
-----------------

[![Excel ADDRESS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20address%20function.png "Excel ADDRESS function")](https://exceljet.net/functions/address-function)

### [ADDRESS Function](https://exceljet.net/functions/address-function)

The Excel ADDRESS function returns the address for a cell based on a given row and column number. For example, =ADDRESS(1,1) returns $A$1. ADDRESS can return an address in relative, mixed, or absolute format, and can be used to construct a cell reference inside a formula.

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

### [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

In this video we're going to combine INDEX and MATCH together to look things up. Here we have the city population data we looked at before. We used the INDEX function to retrieve information about a city with a hard-coded position value. When we supply a number, INDEX retrieves information for the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    

### Functions

*   [ADDRESS Function](https://exceljet.net/functions/address-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

### Videos

*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

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