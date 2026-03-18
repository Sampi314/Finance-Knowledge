# INDEX and MATCH with variable columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/index-and-match-with-variable-columns

---

[Skip to main content](https://exceljet.net/formulas/index-and-match-with-variable-columns#main-content)

[](https://exceljet.net/formulas/index-and-match-with-variable-columns#)

*   [Previous](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/index-with-variable-array)
    

[Lookup](https://exceljet.net/formulas#Lookup)

INDEX and MATCH with variable columns
=====================================

by Dave Bruns · Updated 21 Feb 2025

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

![Excel formula: INDEX and MATCH with variable columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/INDEX_and_MATCH_with_variable_columns.png "Excel formula: INDEX and MATCH with variable columns")

Summary
-------

To create an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
 that returns a variable number of columns from the source data, you can use the second instance of MATCH to find the numeric index of the desired columns. In the example shown, the formula in cell J5 is:

    =INDEX(C5:G16,XMATCH(I5,B5:B16),XMATCH(J4:L4,C4:G4))

With "Red", "Blue", and "Green" in the range J4:L4, the formula returns 7, 9, and 8. The values for Red, Green, and Blue on April 6. If the values in J4:L4 are changed to other valid column names, the formula adjusts correspondingly.

_Note: See below for a solution based on the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
._

Generic formula
---------------

    =INDEX(data,XMATCH(A1,array),XMATCH(array,array))

Explanation 
------------

In this example, the goal is to demonstrate how an INDEX and (X)MATCH formula can be set up so that the columns returned are variable. This approach illustrates one benefit of the 2-step process used by INDEX and MATCH: Because INDEX expects a numeric index for row and column numbers, it is easy to manipulate these values before they are returned to INDEX. If you are new to INDEX and MATCH, see the overview here [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

### Two-way INDEX and MATCH

Essentially, this formula employs the [two-way INDEX and MATCH approach](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
. The INDEX function is provided with the data to return, and the MATCH function is used twice: once to get the correct row number, and once to get the correct column number(s). The generic syntax looks like this:

    =INDEX(data,XMATCH(),XMATCH())

The first MATCH retrieves a row number, and the second MATCH retrieves the column number.

_Note: we are using XMATCH in this example because the configuration is slightly easier (XMATCH defaults to exact match), but the original MATCH function will work fine as well._

In the worksheet shown, the specific formula used in cell J5 is as follows:

    =INDEX(C5:G16,XMATCH(I5,B5:B16),XMATCH(J4:L4,C4:G4))

Working from the inside out, the first [XMATCH function](https://exceljet.net/functions/xmatch-function)
 returns a row number:

    XMATCH(I5,B5:B16) // returns 6

Because April 6 is the sixth value in the range B5:B16, the first XMATCH function returns 6. The second XMATCH function is used to find the required columns like this:

    XMATCH(J4:L4,C4:G4) // returns {1,3,5}

This is the clever bit. Notice the _lookup\_value_ is the _range_ J4:L4, which contains "Red", "Blue", and "Green", and the _lookup\_array_ is the desired columns in C4:G4. Since we are asking XMATCH to find 3 values, it returns an [array](https://exceljet.net/glossary/array)
 with 3 results:

    {1,3,5}

The numbers in this array are the numeric positions of the "Red", "Blue", and "Green" in the range C4:G4. After both MATCH formulas run, we have the following inside INDEX:

    =INDEX(C5:G16,6,{1,3,5}) // returns {7,9,8}

The [INDEX function](https://exceljet.net/functions/index-function)
 then returns the values for April 6 (row 6 in the data) for the "Red", "Blue", and "Green" columns only, and the values [spill](https://exceljet.net/glossary/spill)
 into the range J5:L5. 

_Note: in a modern version of Excel that supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, this formula will just work. In an older version of Excel, you will need to use the [MATCH function](https://exceljet.net/functions/match-function)
 instead of XMATCH and enter the formula as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
._

### XLOOKUP

How can this problem be solved using [XLOOKUP](https://exceljet.net/functions/xlookup-function)
? One approach is to use the XMATCH function together with the [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
 to alter the original data like this:

    =XLOOKUP(I5,B5:B16,CHOOSECOLS(C5:G16,XMATCH(J4:L4,C4:G4)))

Here, the lookup value is the date in cell I5 as before, and the lookup array is the range B5:B16. The _return\_array_ is created on the fly with XMATCH and CHOOSECOLS. XMATCH returns the array {1,3,5} as explained above, and the result from MATCH is returned to CHOOSECOLS as the _col\_num1_ argument and C5:G16 as the _array_. CHOOSECOLS then returns columns 1, 3, and 5 to XLOOKUP as the _return\_array_.

### XLOOKUP vs INDEX and MATCH

This problem illustrates a key difference between XLOOKUP and INDEX and MATCH: because INDEX and MATCH formulas use a _numeric index_ for both rows and columns, it is easy to modify these values before they are used in the INDEX function. XLOOKUP on the other hand deals with _ranges_. To make column ranges dynamic, you sometimes need to use another function like CHOOSECOLS. Both XLOOKUP and INDEX and MATCH offer flexibility and functionality for manipulating and retrieving data, but your choice between them will depend on the specific needs of your project.

> For an in-depth comparison, see [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)

Related formulas
----------------

[![Excel formula: Two-way lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20lookup%20with%20INDEX%20and%20MATCH.png "Excel formula: Two-way lookup with INDEX and MATCH")](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

### [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

In this example, the goal is to perform a two-way lookup, sometimes called a matrix lookup . This means we need to create a match on both rows and columns and return the value at the intersection of this two-way match The core of this formula is INDEX, which is simply retrieving a value from C6:G10...

[![Excel formula: Step-based lookup example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/step-based_lookup_example.png "Excel formula: Step-based lookup example")](https://exceljet.net/formulas/step-based-lookup-example)

### [Step-based lookup example](https://exceljet.net/formulas/step-based-lookup-example)

This worksheet demonstrates a clever way to look up prices that change based on a selected tier. Imagine a pricing system where the cost of a product depends on both the product color and a tier (e.g., "Bronze," "Silver," or "Gold"). The challenge is to pull the correct price based on both inputs...

[![Excel formula: INDEX and MATCH two-column lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_two-column_lookup.png "Excel formula: INDEX and MATCH two-column lookup")](https://exceljet.net/formulas/index-and-match-two-column-lookup)

### [INDEX and MATCH two-column lookup](https://exceljet.net/formulas/index-and-match-two-column-lookup)

In this example, the goal is to look up Width and Length based on inputs for Code (K6) and Size (K7). While finding the correct row based on the Code value is straightforward, the problem of how to best retrieve both columns of data (Width and Length) is more challenging. One good way to solve this...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    
*   [Step-based lookup example](https://exceljet.net/formulas/step-based-lookup-example)
    
*   [INDEX and MATCH two-column lookup](https://exceljet.net/formulas/index-and-match-two-column-lookup)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    
*   [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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