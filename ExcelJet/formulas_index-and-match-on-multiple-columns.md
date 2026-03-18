# Index and match on multiple columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/index-and-match-on-multiple-columns

---

[Skip to main content](https://exceljet.net/formulas/index-and-match-on-multiple-columns#main-content)

[](https://exceljet.net/formulas/index-and-match-on-multiple-columns#)

*   [Previous](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [Next](https://exceljet.net/formulas/index-and-match-two-column-lookup)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Index and match on multiple columns
===================================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[MMULT](https://exceljet.net/functions/mmult-function)

[COLUMN](https://exceljet.net/functions/column-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[INDEX](https://exceljet.net/functions/index-function)

![Excel formula: Index and match on multiple columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/index%20and%20match%20on%20multiple%20columns.png "Excel formula: Index and match on multiple columns")

Summary
-------

To lookup a value by matching across multiple columns, you can use an [array formula](https://exceljet.net/glossary/array-formula)
 based on several functions, including [MMULT](https://exceljet.net/functions/mmult-function)
, [TRANSPOSE](https://exceljet.net/functions/transpose-function)
, [COLUMN](https://exceljet.net/functions/column-function)
, and [INDEX](https://exceljet.net/functions/index-function)
. In the example shown, the formula in H4 is:

    {=INDEX(groups,MATCH(1,MMULT(--(names=G4),TRANSPOSE(COLUMN(names)^0)),0))}
    

where "names" is the [named range](https://exceljet.net/glossary/named-range)
 C4:E7, and "groups" is the named range B4:B7. The formula returns the group that each name belongs to.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control shift enter._

Generic formula
---------------

    {=INDEX(rng1,MATCH(1,MMULT(--(rng2=criteria),TRANSPOSE(COLUMN(rng2)^0)),0))}

Explanation 
------------

Working from the inside out, the logical criteria used in this formula is this expression:

    --(names=G4)
    

where **names** is the [named range](https://exceljet.net/glossary/named-range)
 C4:E7. This generates a TRUE / FALSE result for every value in the data, and the [double negative](https://exceljet.net/glossary/double-unary)
 coerces the TRUE and FALSE values to 1 and 0 to yield an array like this:

    {0,0,0;1,0,0;0,0,0;0,0,0}
    

This array is 4 rows by 3 columns, matching the structure of "names". A second array is created with this expression:

    TRANSPOSE(COLUMN(names)^0))
    

The [COLUMN function](https://exceljet.net/functions/column-function)
 is used to create a numeric array with 3 columns and 1 row, and [TRANSPOSE](https://exceljet.net/functions/transpose-function)
 converts this array to 1 column and 3 rows. Raising the result to the power of zero simply converts all numbers in the array to 1. The [MMULT function](https://exceljet.net/functions/mmult-function)
 is then used to perform matrix multiplication:

    MMULT({0,0,0;1,0,0;0,0,0;0,0,0},{1;1;1})
    

and the result goes into the [MATCH function](https://exceljet.net/functions/match-function)
 as the _array_ argument, with 1 as the lookup value:

    MATCH(1,{0;1;0;0},0)
    

The MATCH function returns the position of the first match, which corresponds to the first matching row meeting supplied criteria. This is fed into [INDEX](https://exceljet.net/functions/index-function)
 as the row number, with the named range "groups" as the array:

    =INDEX(groups,2)
    

Finally, INDEX returns "Bear", the group Adam belongs to.

### Literal "contains" criteria

To check for specific text values instead of an exact match, you can use the [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [SEARCH](https://exceljet.net/functions/search-function)
 functions together. For example, to match cells that contain "apple" you can use:

    =ISNUMBER(SEARCH("apple",data))
    

This formula is explained [here](https://exceljet.net/formulas/cell-contains-specific-text)
.

Related formulas
----------------

[![Excel formula: Count rows with at least n matching values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20with%20at%20least%20n%20matching%20values3.png "Excel formula: Count rows with at least n matching values")](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)

### [Count rows with at least n matching values](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)

Working from the inside out, the logical criteria used in this formula is: (data)<70 where data is the named range C5:I14. This generates a TRUE / FALSE result for every value in data , and the double negative coerces the TRUE FALSE values to 1 and 0 to yield an array like this: {0,0,0,1,0,1,0;0...

[![Excel formula: Count rows with multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20with%20multiple%20OR%20criteria.png "Excel formula: Count rows with multiple OR criteria")](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)

### [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)

In this example, the goal is to count rows using OR logic based on the criteria shown in column F. For example, in cell G5 we want to count rows where Color is "Blue" OR Pet is "Dog". This can be done with Boolean logic and the SUMPRODUCT function , as explained below. Notes This formula uses an...

[![Excel formula: Count if row meets internal criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20if%20row%20meets%20internal%20criteria.png "Excel formula: Count if row meets internal criteria")](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)

### [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)

In this example the goal is to count products (rows) where sales have increased and sales have decreased, where previous sales are in column C (Previous) and current sales are in column D (Current). In this case, we can't use COUNTIFS directly, because COUNTIFS is a range-based function and it won'...

[![Excel formula: Count if row meets multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20if%20row%20meets%20multiple%20criteria.png "Excel formula: Count if row meets multiple criteria")](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)

### [Count if row meets multiple criteria](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)

In this example, the goal is to count orders (rows) where the state is Texas ("TX"), the amount is greater than $100, and the month is March. In this case, we can't use COUNTIFS , because COUNTIFS is a range-based function and it won't accept a calculation for a range argument, which we need to...

Related functions
-----------------

[![Excel MMULT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mmult%20function.png "Excel MMULT function")](https://exceljet.net/functions/mmult-function)

### [MMULT Function](https://exceljet.net/functions/mmult-function)

The Excel MMULT function returns the matrix product of two arrays. The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. 

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count rows with at least n matching values](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)
    
*   [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)
    
*   [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)
    
*   [Count if row meets multiple criteria](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)
    

### Functions

*   [MMULT Function](https://exceljet.net/functions/mmult-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

### Links

*   [Stackoverflow answer by XOR LX](https://stackoverflow.com/questions/43277252/excel-count-occurences-of-value-in-rows-of-a-range/43278905#43278905)
    

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