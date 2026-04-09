# Join tables with INDEX and MATCH - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/join-tables-with-index-and-match

---

[Skip to main content](https://exceljet.net/formulas/join-tables-with-index-and-match#main-content)

[](https://exceljet.net/formulas/join-tables-with-index-and-match#)

*   [Previous](https://exceljet.net/formulas/index-with-variable-array)
    
*   [Next](https://exceljet.net/formulas/left-lookup-with-index-and-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Join tables with INDEX and MATCH
================================

by Dave Bruns · Updated 1 Mar 2019

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Join tables with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/join%20tables%20with%20INDEX%20and%20MATCH%202.png "Excel formula: Join tables with INDEX and MATCH")

Summary
-------

To join or merge tables that have a common id, you can use the INDEX and MATCH functions. In the example shown, the formula in E5 is:

    =INDEX(data,MATCH($C5,ids,0),2)
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 H5:J8 and "ids" is the named range H5:H8.

Generic formula
---------------

    =INDEX(data,MATCH(lookup,ids,0),2)

Explanation 
------------

This formula pulls the customer name and state from the customer table into the order table. The MATCH function is used to locate the right customer and the INDEX function is used to retrieve the data.

### Retrieving customer name

Working from the inside out, the MATCH function is used to get a row number like this:

    MATCH($C5,ids,0)
    

*   The lookup value comes the customer id in C5, which is a mixed reference, with the column locked, so the formula can be easily copied.
*   The lookup array is the named range ids (H5:H8), the first column in the customer table.
*   The match type is set to zero to force an exact match.

The MATCH function returns 2 in this case, which goes into INDEX as the row number:

    =INDEX(data,2,2)
    

With the column number hard-coded as 2 (customer names are in column 2) and the array set to the named range "data" (H5:J8) INDEX returns: Amy Chang.

### Retrieving customer state

The formula to retrieve customer state is almost identical. The only difference is the column number is hard-coded as 3, since state info appears in the 3rd column:

    =INDEX(data,MATCH($C5,ids,0),2) // get name
    =INDEX(data,MATCH($C5,ids,0),3) // get state
    

### Dynamic two-way match

By adding another MATCH function to the formula, you can set up a dynamic two-way match. For example, with the named range "headers" for H4:J4, you can use a formula like this:

    =INDEX(data,MATCH($C5,ids,0),MATCH(E$4,headers,0))
    

Here, a second MATCH function has been added to get the correct column number. MATCH uses the current column header in the first table to locate the correct column number in the second table, and automatically returns this number to INDEX.

Related formulas
----------------

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: Two-way lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20lookup%20with%20INDEX%20and%20MATCH.png "Excel formula: Two-way lookup with INDEX and MATCH")](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

### [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

In this example, the goal is to perform a two-way lookup, sometimes called a matrix lookup . This means we need to create a match on both rows and columns and return the value at the intersection of this two-way match The core of this formula is INDEX, which is simply retrieving a value from C6:G10...

Related functions
-----------------

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

*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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