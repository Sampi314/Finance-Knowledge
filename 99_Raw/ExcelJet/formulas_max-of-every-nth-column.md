# Max of every nth column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/max-of-every-nth-column

---

[Skip to main content](https://exceljet.net/formulas/max-of-every-nth-column#main-content)

[](https://exceljet.net/formulas/max-of-every-nth-column#)

*   [Previous](https://exceljet.net/formulas/max-by-month)
    
*   [Next](https://exceljet.net/formulas/max-value-ignore-all-errors)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Max of every nth column
=======================

by Dave Bruns · Updated 10 Mar 2023

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[FILTER](https://exceljet.net/functions/filter-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

[COLUMN](https://exceljet.net/functions/column-function)

[MOD](https://exceljet.net/functions/mod-function)

![Excel formula: Max of every nth column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/max_of_every_nth_column.png "Excel formula: Max of every nth column")

Summary
-------

To get the max of every nth column, you can use a formula based on [MAX](https://exceljet.net/functions/max-function)
, [FILTER](https://exceljet.net/functions/filter-function)
, [MOD](https://exceljet.net/functions/mod-function)
, [SEQUENCE](https://exceljet.net/functions/sequence-function)
, and [COLUMNS](https://exceljet.net/functions/columns-function)
. In the example shown, the formula in O5 is:

    =MAX(FILTER(B5:M5,MOD(SEQUENCE(,COLUMNS(B5:M5)),n)=0))

where **n** is the [named range](https://exceljet.net/glossary/named-range)
 **M2**. With 3 in cell **M2**, the formula returns 17, the maximum value of the 3rd, 6th, 9th, and 12th values in B5:M5. If **n** is changed to another value, the formula will recalculate. See below for alternatives and a formula that will work in older versions of Excel.

Generic formula
---------------

    =MAX(FILTER(data,MOD(SEQUENCE(,COLUMNS(data)),n)=0))

Explanation 
------------

In this example, the goal is to calculate the maximum value of every "nth" column in a row of data, where **n** is a variable entered in the named range **M2**. This problem can be solved in several ways, as explained below. The explanation below also includes a formula that will work in older versions of Excel, before [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 were introduced.

### FILTER + MOD + SEQUENCE

A classic solution to "nth" problems is to use the [MOD function](https://exceljet.net/functions/mod-function)
 to check a numeric array for a remainder of zero after dividing by **n**. This is the approach in the worksheet shown, there the formula in cell O5, copied down, is:

    =MAX(FILTER(B5:M5,MOD(SEQUENCE(,COLUMNS(B5:M5)),n)=0))

At a high level, the FILTER function is configured to retrieve only the nth values of interest using logic created with MOD and SEQUENCE. The result from FILTER is returned to MAX, which returns the maximum value as a final result. Working from the inside out, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 is configured to generate a numeric array like this:

    SEQUENCE(,COLUMNS(B5:M5))

Because there are 12 columns in the range B5:M5, SEQUENCE returns an 1 x 12 [array](https://exceljet.net/glossary/array)
 like this:

    {1,2,3,4,5,6,7,8,9,10,11,12}

This array is returned to the MOD function as the _number_ argument, with **n** provided as the divisor. The result from MOD is then compared to zero:

    MOD({1,2,3,4,5,6,7,8,9,10,11,12},n)=0

With the number 3 in cell **M2** for **n**, MOD returns an array like this:

    {1,2,0,1,2,0,1,2,0,1,2,0}=0

Note that every 3rd value is zero. When this array is compared to zero, the result is an array of TRUE and FALSE values like this:

    {FALSE,FALSE,TRUE,FALSE,FALSE,TRUE,FALSE,FALSE,TRUE,FALSE,FALSE,TRUE}

Notice that every 3rd value is now TRUE. This array is returned directly to the FILTER function as the _include_ argument. With _array_ given as B5:M5, FILTER returns every 3rd value in B5:M5 directly to MAX like this:

    =MAX({17,1,8,10})

The MAX function then returns 17 as a final result.

### CHOOSECOLS + SEQUENCE

An alternative approach is to use the [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
 with the SEQUENCE function like this:

    =MAX(CHOOSECOLS(B5:M5,SEQUENCE(,COLUMNS(B5:M5)/n,n,n)))

This formula calculates the numeric indices of target nth values directly, then requests just those values with the CHOOSECOLS function. The SEQUENCE function is configured to return the numeric indexes of every nth value like this:

    SEQUENCE(,COLUMNS(B5:M5)/n,n,n)))

The _rows_ argument is left empty. The _columns_ argument is calculated by dividing the number of columns by **n**. Both _start_ and _step_ are assigned the value **n**. With 12 columns in B5:M5, and the number 3 for **n**, this simplifies to:

    SEQUENCE(,4,3,3))

The result is a numeric array of "target nth values" like this:

    {3,6,9,12}

This array is returned directly to the CHOOSECOLS function as the second argument:

    =MAX(CHOOSECOLS(B5:M5,{3,6,9,12}))

The CHOOSECOLS function then returns the values at these locations in an array to MAX:

    =MAX({17,1,8,10})

The MAX function returns 17 as before.

### All in one formulas

If desired, you can adapt the formulas above to single, all-in-one formulas based on the [BYROW function](https://exceljet.net/functions/byrow-function)
 like this:

    =BYROW(B5:M16,LAMBDA(r,MAX(FILTER(r,MOD(SEQUENCE(,COLUMNS(r)),n)=0))))
    =BYROW(B5:M16,LAMBDA(r,MAX(CHOOSECOLS(r,SEQUENCE(,COLUMNS(r)/n,n,n)))))

The first formula uses the SEQUENCE and MOD approach, the second formula uses the SEQUENCE and CHOOSECOLS approach. Both formulas will return the max values for nth columns for all rows at once.

### Legacy Excel

In older versions of Excel without [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 like FILTER and SEQUENCE, you can use an [array formula](https://exceljet.net/articles/what-is-an-array-formula)
 like this:

    {=MAX(IF(MOD(COLUMN(B5:M5)-COLUMN(B5)+1,n)=0,B5:M5))}

_This is an array formula and must be entered with control + shift + enter in older versions of Excel._

At a high level, this formula uses the [IF Function](https://exceljet.net/functions/if-function)
 together with the MOD and COLUMN functions to "cancel out" values _not_ in nth columns, then runs MAX on the result. The key is this snippet:

    MOD(COLUMN(B5:M5)-COLUMN(B5)+1,n)

The [COLUMN function](https://exceljet.net/functions/column-function)
 is used to get a set of "relative" column numbers as explained in detail [here](https://exceljet.net/formulas/get-relative-column-numbers-in-range)
. The result is a numeric [array](https://exceljet.net/glossary/array)
 that starts with the number 1:

    {1,2,3,4,5,6,7,8,9,10,11,12}

This array goes into the [MOD function](https://exceljet.net/functions/mod-function)
 as the _number_ argument:

    MOD({1,2,3,4,5,6,7,8,9,10,11,12},n)=0

where **n** is the value to use for "nth". The MOD function returns the remainder for each column number divided by **n**. When **n** = 3, MOD will return an array like this:

    {1,2,0,1,2,0,1,2,0,1,2,0}

Note that zeros appear for columns 3, 6, 9 and 12, corresponding to every 3rd column. This array is compared to zero with the logical expression =0 to force a TRUE when the remainder is zero and a FALSE when not. These values go into the IF function as the logical test. The IF function then "filters" results so only values in the original range in nth columns make it into the final array. Other values become FALSE. The result is delivered to the MAX function:

    =MAX({FALSE,FALSE,17,FALSE,FALSE,1,FALSE,FALSE,8,FALSE,FALSE,10})

The [MAX function](https://exceljet.net/functions/max-function)
 automatically ignores FALSE values and returns 17 as a final result.

### Max of every other column

To get the maximum value in every other column, you can make a small adjustment to the formula when needed. To get the maximum value in even columns, use the original formula with 2 as **n**:

    =MAX(FILTER(data,MOD(SEQUENCE(,COLUMNS(data)),2)=0))

To get the maximum number in odd columns use 2 for **n** and compare the result to 1:

    =MAX(FILTER(data,MOD(SEQUENCE(,COLUMNS(data)),2)=1))

In older versions of Excel, you can use these generic formulas:

    {=MAX(IF(MOD(COLUMN(A1:Z1)-COLUMN(A1)+1,2)=0,rng))} // even columns
    {=MAX(IF(MOD(COLUMN(A1:Z1)-COLUMN(A1)+1,2)=1,rng))} // odd columns
    

_These are array formulas and must be entered with control + shift + enter in older versions of Excel._

Related formulas
----------------

[![Excel formula: Get relative column numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20column%20numbers%20in%20range.png "Excel formula: Get relative column numbers in range")](https://exceljet.net/formulas/get-relative-column-numbers-in-range)

### [Get relative column numbers in range](https://exceljet.net/formulas/get-relative-column-numbers-in-range)

The first COLUMN function generates an array of 7 numbers like this: {2,3,4,5,6,7,8} The second COLUMN function generates an array with just one item like this: {2} which is then subtracted from the first array to yield: {0,1,2,3,4,5,6} Finally, 1 is added to get: {1,2,3,4,5,6,7} With a named range...

[![Excel formula: Sum columns based on adjacent criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20columns%20based%20on%20adjacent%20criteria.png "Excel formula: Sum columns based on adjacent criteria")](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)

### [Sum columns based on adjacent criteria](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)

In this example, the goal is to sum the values in columns C, E, G, and I conditionally using the text values in columns B, D, F, and H for criteria. This problem can be solved with the SUMPRODUCT function , which is designed to multiply ranges or arrays together and return the sum of products. The...

[![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")](https://exceljet.net/formulas/sum-every-nth-column)

### [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)

In this example, the goal is to sum every nth value by column in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value by column, if n =3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and n is entered into...

[![Excel formula: Copy value from every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20column.png "Excel formula: Copy value from every nth column")](https://exceljet.net/formulas/copy-value-from-every-nth-column)

### [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)

In Excel, you can't easily create formulas that skip columns following a certain pattern, because the references in the formula will automatically change to maintain the relationship between the original source cell and the new target cell. However, with a little work, it's possible to construct...

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get relative column numbers in range](https://exceljet.net/formulas/get-relative-column-numbers-in-range)
    
*   [Sum columns based on adjacent criteria](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)
    
*   [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
    
*   [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    
*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    

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