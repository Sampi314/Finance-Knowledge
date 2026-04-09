# XLOOKUP match any column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-match-any-column

---

[Skip to main content](https://exceljet.net/formulas/xlookup-match-any-column#main-content)

[](https://exceljet.net/formulas/xlookup-match-any-column#)

*   [Previous](https://exceljet.net/formulas/unique-with-non-adjacent-columns)
    
*   [Next](https://exceljet.net/formulas/cap-percentage-between-0-and-100)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

XLOOKUP match any column
========================

by Dave Bruns · Updated 22 Jun 2022

Related functions 
------------------

[MMULT](https://exceljet.net/functions/mmult-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

![Excel formula: XLOOKUP match any column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/xlookup%20match%20any%20column.png "Excel formula: XLOOKUP match any column")

Summary
-------

To perform a lookup by matching a value in any one of several columns, you can use a formula based on the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 together with the [MMULT function](https://exceljet.net/functions/mmult-function)
. In the example shown, the formula in K6 is:

    =XLOOKUP(1,MMULT(--(codes=K5),SEQUENCE(COLUMNS(codes),1,1,0)),group)
    

where **codes** (C5:H15) and **group** (B5:B15) are [named ranges](https://exceljet.net/glossary/named-range)
. The result for the lookup code "BDBC" is "Epsilon. This lookup can also be done in older versions of Excel with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, as explained below.

Explanation 
------------

In this example, we have a table that contains 6 columns of codes, and each row of codes belongs to a group in column B. The goal is to lookup any code in C5:H15, and return the name of the group the code belongs to. The challenge is that the code may be in any one of the six columns, and potentially more columns in larger sets of data. The formula in K6 is:

    =XLOOKUP(1,MMULT(--(codes=K5),SEQUENCE(COLUMNS(codes),1,1,0)),group)
    

where **codes** (C5:H15) and **group** (B5:B15) are [named ranges](https://exceljet.net/glossary/named-range)
.

At a high level, this formula uses the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 to perform the lookup, with the number 1 as the lookup value, and the named range **group** as the return array. The tricky part of the formula is the lookup array, which is created with the [MMULT function](https://exceljet.net/functions/mmult-function)
 like this:

    MMULT(--(codes=K5),SEQUENCE(COLUMNS(codes),1,1,0))
    

The MMULT function performs matrix multiplication, which is a handy way to reduce results from many columns to a single column of results. MMULT takes two arrays, _array1_ and _array2_, and requires that the number of columns in _array1_ be the same as the number of rows in _array2_. The resulting matrix (which is an [array](https://exceljet.net/glossary/array)
) will have same number of rows as the first matrix, and the same number of columns as the second matrix.

The first array is simply the logical test of all codes in the named range C5:I13 against the code we are looking for in K5:

    =MMULT(--(codes=K5)
    

The [double negative](https://exceljet.net/glossary/double-unary)
 forces TRUE and FALSE values to 1s and 0s. The result is an array of 11 rows by 6 columns. Notice the lone 1 in row 5 is the only matching code:

    {0,0,0,0,0,0;
    0,0,0,0,0,0;
    0,0,0,0,0,0;
    0,0,0,0,0,0;
    0,0,1,0,0,0;
    0,0,0,0,0,0;
    0,0,0,0,0,0;
    0,0,0,0,0,0;
    0,0,0,0,0,0;
    0,0,0,0,0,0;
    0,0,0,0,0,0}
    

The first array has 6 columns, so the second array must contain 6 rows. The [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 provides an easy way to construct this array, with some help from the [COLUMNS function](https://exceljet.net/functions/columns-function)
:

    SEQUENCE(COLUMNS(codes),1,1,0)
    

COLUMNS returns 6 to SEQUENCE for as the _rows_ argument. The _columns_ argument is 1, _start_ is 1, and the _step_ value is zero. The result is an array with 6 rows and 1 column, filled only with 1:

    {1;1;1;1;1;1}
    

The MMULT function then calculates the matrix product of the two arrays and returns an array with 11 rows and 1 column:

    {0;0;0;0;1;0;0;0;0;0;0}
    

Notice row 5, which contains the code "BDBC" is 1, while all other rows are zero. This array is returned to XLOOKUP as the _lookup\_array_:

    =XLOOKUP(1,{0;0;0;0;1;0;0;0;0;0;0},group)
    

and XLOOKUP matches the 1 and returns the 5th item in group, "Epsilon"

### Get matching column

The formula above can be adjusted to return the position or heading of the matching column. To get the matching column number from the range C4:H4, you can use a formula like this:

    =XLOOKUP(1,MMULT(SEQUENCE(1,ROWS(codes),1,0),--(codes=K5)),C4:H4)
    

The structure of this formula is similar to the formula above. The _lookup\_value_ is 1, and the _lookup\_array_ is created with MMULT here:

    MMULT(SEQUENCE(1,ROWS(codes),1,0),--(codes=K5))
    

Notice in this case we are using the [ROWS function](https://exceljet.net/functions/rows-function)
 in the first argument to MMULT, and SEQUENCE is configured to create columns. The result from SEQUENCE is an array with 11 columns like this:

    {1,1,1,1,1,1,1,1,1,1,1}
    

The second array in MMULT is created with the same code we used above:

    --(codes=K5)
    

After MMULT runs, it returns the following array directly to the XLOOKUP function as the _lookup\_array_:

    {0,0,1,0,0,0}
    

Notice the 1 corresponds to column 3 in **codes**. We can now simplify the formula as follows:

    =XLOOKUP(1,{0,0,1,0,0,0},C4:H4)
    

XLOOKUP locates the 1 in the array, and returns the third value in the range C4:H4, which is 3. Note that the range C4:H4 could be a [named range](https://exceljet.net/glossary/named-range)
, and can contain values of any kind.

### Without XLOOKUP and SEQUENCE

In versions of Excel without XLOOKUP and SEQUENCE, this problem can be solved with a formula based on [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
:

    {=INDEX(group,MATCH(1,MMULT(--(codes=K5),TRANSPOSE(COLUMN(codes)^0)),0))}
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

The MMULT function is configured to return the same result as above, but the syntax used to create _array2_ is different:

    TRANSPOSE(COLUMN(codes)^0))
    

The [COLUMN function](https://exceljet.net/functions/column-function)
 returns 6 numbers in a horizontal array:

    COLUMN(data) // returns {3,4,5,6,7,8}
    

And these numbers are then raised to a power of zero with the exponent operator (^):

    COLUMN(data)^0) // returns {1,1,1,1,1,1}
    

Raising any number to the power of zero (0) results in 1, so the result is the same 1 x 6 array filled only with 1s.

Finally, [TRANSPOSE](https://exceljet.net/functions/transpose-function)
 flips the array to a 1 x 6 array to a 6 x 1 array:

    TRANSPOSE({1,1,1,1,1,1} // returns {1;1;1;1;1;1}
    

and the result is handed off to the MMULT function as _array2_, as before.

The first array in MMULT is created in the same way as in the original formula, with the same result. So the final result from MMULT is the same:

    {0;0;0;0;1;0;0;0;0;0;0}
    

Substituting this array into the formula, we have a "standard" INDEX and MATCH formula:

    =INDEX(group,MATCH(1,{0;0;0;0;1;0;0;0;0;0;0},0))
    

The [MATCH function](https://exceljet.net/functions/match-function)
 returns 5, the position of the single 1 in the array:

    =INDEX(group,5) // returns "Epsilon"
    

And [INDEX](https://exceljet.net/functions/index-function)
 returns the 5th item in the named range **group** (B5:B15), "Epsilon", as the final result.

Related formulas
----------------

[![Excel formula: Get column totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20column%20totals.png "Excel formula: Get column totals")](https://exceljet.net/formulas/get-column-totals)

### [Get column totals](https://exceljet.net/formulas/get-column-totals)

In this example, the goal is to return an array with 7 subtotals, one for each day of the week, as seen in columns C:I. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We...

[![Excel formula: Get row totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20row%20totals.png "Excel formula: Get row totals")](https://exceljet.net/formulas/get-row-totals)

### [Get row totals](https://exceljet.net/formulas/get-row-totals)

In this example, the goal is to return an array with nine subtotals, one for each of the colors named in column B. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We can'...

[![Excel formula: Get location of value in 2D array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_location_of_value_in_2D_array.png "Excel formula: Get location of value in 2D array")](https://exceljet.net/formulas/get-location-of-value-in-2d-array)

### [Get location of value in 2D array](https://exceljet.net/formulas/get-location-of-value-in-2d-array)

In this example, the goal is to return a list of the locations for a specific value in a 2D array of values (i.e., a table). The target value is entered in cell N5, and the table being tested is in the range C4:L16. The coordinates are supplied from row 4 and column B, as seen in the worksheet. In...

Related functions
-----------------

[![Excel MMULT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mmult%20function.png "Excel MMULT function")](https://exceljet.net/functions/mmult-function)

### [MMULT Function](https://exceljet.net/functions/mmult-function)

The Excel MMULT function returns the matrix product of two arrays. The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. 

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get column totals](https://exceljet.net/formulas/get-column-totals)
    
*   [Get row totals](https://exceljet.net/formulas/get-row-totals)
    
*   [Get location of value in 2D array](https://exceljet.net/formulas/get-location-of-value-in-2d-array)
    

### Functions

*   [MMULT Function](https://exceljet.net/functions/mmult-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    

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