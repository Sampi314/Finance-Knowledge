# Two-way lookup with INDEX and MATCH - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/two-way-lookup-with-index-and-match

---

[Skip to main content](https://exceljet.net/formulas/two-way-lookup-with-index-and-match#main-content)

[](https://exceljet.net/formulas/two-way-lookup-with-index-and-match#)

*   [Previous](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/vlookup-by-date)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Two-way lookup with INDEX and MATCH
===================================

by Dave Bruns · Updated 4 Apr 2023

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Two-way lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/two-way%20lookup%20with%20INDEX%20and%20MATCH.png "Excel formula: Two-way lookup with INDEX and MATCH")

Summary
-------

To lookup in value in a table using both rows and columns, you can build a formula that does a two-way lookup with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
. In the example shown, the formula in J8 is:

    =INDEX(C6:G10,MATCH(J6,B6:B10,1),MATCH(J7,C5:G5,1))
    

_Note: this formula is set to "approximate match", so row values and column values must be sorted._

Generic formula
---------------

    =INDEX(data,MATCH(val,rows,1),MATCH(val,columns,1))

Explanation 
------------

In this example, the goal is to perform a two-way lookup, sometimes called a _matrix lookup_. This means we need to create a match on both rows and columns and return the value at the intersection of this two-way match

The core of this formula is INDEX, which is simply retrieving a value from C6:G10 (the "data") based on a row number and a column number.

    =INDEX(C6:G10,row,column)
    

To get the row and column numbers, we use the MATCH function configured for an approximate match by setting the _match\_type_ argument to 1:

    MATCH(J6,B6:B10,1) // get row number
    MATCH(J7,C5:G5,1) // get column number
    

In the example, MATCH will return 2 when the width is 290, and 3 when the height is 300.

In the end, the formula reduces to:

    =INDEX(C6:G10, 2, 3)
    = 1800
    

Related formulas
----------------

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: INDEX and MATCH descending order](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20and%20MATCH%20descending%20order.png "Excel formula: INDEX and MATCH descending order")](https://exceljet.net/formulas/index-and-match-descending-order)

### [INDEX and MATCH descending order](https://exceljet.net/formulas/index-and-match-descending-order)

This formula uses -1 for match type to allow an approximate match on values sorted in descending order. The MATCH part of the formula looks like this: MATCH(F4,B5:B9,-1) Using the lookup value in cell F4, MATCH finds the first value in B5:B9 that is greater than or equal to the lookup value. If an...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20do%20a%20two-way%20lookup%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

### [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

In this video we'll look at how to set up a classic two-way lookup using INDEX and MATCH . Here we have a list of salespeople with monthly sales figures. What we want to do is add a formula in Q6 that looks up and retrieves a sales number based on the name and month above. To do this, we'll use the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Two-way%20lookup%20with%20INDEX%20and%20MATCH%20approximate-Thumb.png)](https://exceljet.net/videos/two-way-lookup-with-index-and-match-approximate)

### [Two-way lookup with INDEX and MATCH approximate](https://exceljet.net/videos/two-way-lookup-with-index-and-match-approximate)

In this video we'll look at how to build a two-way lookup with INDEX and MATCH using an approximate match. Here we have a simple cost calculator which looks up cost based on a material's width and height. The match needs to be approximate. For example, if the width is 250, and the height is 325,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [INDEX and MATCH descending order](https://exceljet.net/formulas/index-and-match-descending-order)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)
    
*   [Two-way lookup with INDEX and MATCH approximate](https://exceljet.net/videos/two-way-lookup-with-index-and-match-approximate)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

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