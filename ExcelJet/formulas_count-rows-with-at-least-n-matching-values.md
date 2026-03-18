# Count rows with at least n matching values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values

---

[Skip to main content](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values#main-content)

[](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values#)

*   [Previous](https://exceljet.net/formulas/count-rows-that-contain-specific-values)
    
*   [Next](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)
    

[Count](https://exceljet.net/formulas#Count)

Count rows with at least n matching values
==========================================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[MMULT](https://exceljet.net/functions/mmult-function)

[COLUMN](https://exceljet.net/functions/column-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

![Excel formula: Count rows with at least n matching values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20rows%20with%20at%20least%20n%20matching%20values3.png "Excel formula: Count rows with at least n matching values")

Summary
-------

To count rows that contain specific values, you can use an [array formula](https://exceljet.net/glossary/array-formula)
 based on the MMULT, TRANSPOSE, COLUMN, and SUM functions. In the example shown, the formula in K6 is:

    {=SUM(--(MMULT(--((data)<70),TRANSPOSE(COLUMN(data)^0))>=2))}
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 C5:I14.

_Note this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control shift enter._

Generic formula
---------------

    {=SUM(--(MMULT(--(criteria),TRANSPOSE(COLUMN(data)^0))>=N))}

Explanation 
------------

Working from the inside out, the logical criteria used in this formula is:

    (data)<70
    

where **data** is the named range C5:I14. This generates a TRUE / FALSE result for every value in **data**, and the double negative coerces the TRUE FALSE values to 1 and 0 to yield an array like this:

    {0,0,0,1,0,1,0;0,0,0,0,0,0,0;0,0,0,0,0,0,0;0,1,1,0,0,1,0;0,0,0,0,0,0,0;0,0,0,0,0,0,0;0,0,0,0,0,0,0;0,1,0,0,0,0,0;0,0,0,0,0,0,0;0,0,0,0,0,0,0}
    

Like the original data, this array is 10 rows by 7 columns (10 x 7) and goes into the MMULT function as _array1_. The next argument, _array2_ is created with:

    TRANSPOSE(COLUMN(data)^0))
    

Here, the COLUMN function is used as a way to generate a numeric array of the right size, since matrix multiplication requires the column count in _array1_ (7) to equal the row count in _array2._

The COLUMN function returns the 7-column array {3,4,5,6,7,8,9}. By raising this array to a power of zero, we end up with a 7 x 1 array like {1,1,1,1,1,1,1}, which TRANSPOSE changes to a 1 x 7 array like {1;1;1;1;1;1;1}.

MMULT then runs and returns a 10 x 1 array result {2;0;0;3;0;0;0;1;0;0}, which is processed with the logical expression >=2, resulting in an array of TRUE FALSE values:

    {TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

We again coerce TRUE FALSE to 1 and 0 with a double negative to get a final array inside SUM:

    =SUM({1;0;0;1;0;0;0;0;0;0})
    

Which correctly returns 2, the number of names with at least 2 scores below 70.

Related formulas
----------------

[![Excel formula: Count rows with multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20with%20multiple%20OR%20criteria.png "Excel formula: Count rows with multiple OR criteria")](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)

### [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)

In this example, the goal is to count rows using OR logic based on the criteria shown in column F. For example, in cell G5 we want to count rows where Color is "Blue" OR Pet is "Dog". This can be done with Boolean logic and the SUMPRODUCT function , as explained below. Notes This formula uses an...

[![Excel formula: Count if row meets internal criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20if%20row%20meets%20internal%20criteria.png "Excel formula: Count if row meets internal criteria")](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)

### [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)

In this example the goal is to count products (rows) where sales have increased and sales have decreased, where previous sales are in column C (Previous) and current sales are in column D (Current). In this case, we can't use COUNTIFS directly, because COUNTIFS is a range-based function and it won'...

[![Excel formula: Count if row meets multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20if%20row%20meets%20multiple%20criteria.png "Excel formula: Count if row meets multiple criteria")](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)

### [Count if row meets multiple criteria](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)

In this example, the goal is to count orders (rows) where the state is Texas ("TX"), the amount is greater than $100, and the month is March. In this case, we can't use COUNTIFS , because COUNTIFS is a range-based function and it won't accept a calculation for a range argument, which we need to...

[![Excel formula: Count rows that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20that%20contain%20specific%20values.png "Excel formula: Count rows that contain specific values")](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

### [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

In this example, the goal is to count the number of rows in the data that contain the value in cell G4, which is 19. The main challenge in this problem is that the value might appear in any column, and might appear more than once in the same row. If we wanted to simply count the total number of...

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

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)
    
*   [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)
    
*   [Count if row meets multiple criteria](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)
    
*   [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)
    

### Functions

*   [MMULT Function](https://exceljet.net/functions/mmult-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    

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