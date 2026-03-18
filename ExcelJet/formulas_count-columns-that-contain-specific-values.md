# Count columns that contain specific values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-columns-that-contain-specific-values

---

[Skip to main content](https://exceljet.net/formulas/count-columns-that-contain-specific-values#main-content)

[](https://exceljet.net/formulas/count-columns-that-contain-specific-values#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-end-with)
    
*   [Next](https://exceljet.net/formulas/count-dates-by-day-of-week)
    

[Count](https://exceljet.net/formulas#Count)

Count columns that contain specific values
==========================================

by Dave Bruns · Updated 24 Mar 2022

Related functions 
------------------

[MMULT](https://exceljet.net/functions/mmult-function)

[COLUMN](https://exceljet.net/functions/column-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[BYCOL](https://exceljet.net/functions/bycol-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

![Excel formula: Count columns that contain specific values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20columns%20that%20contain%20specific%20values.png "Excel formula: Count columns that contain specific values")

Summary
-------

To count rows that contain specific values, you can use a formula based on the [MMULT](https://exceljet.net/functions/mmult-function)
, [TRANSPOSE](https://exceljet.net/functions/transpose-function)
, [ROW](https://exceljet.net/functions/row-function)
, and [SUM](https://exceljet.net/functions/sum-function)
 functions. In the example shown, the formula in I6 is:

    =SUM(--(MMULT(TRANSPOSE(ROW(data)^0),--(data=I4))>0))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B4:F15. The result is 4, the number of columns that contain the number 19.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control shift enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
. See below for a formula that performs the same task with the newer [BYCOL function](https://exceljet.net/functions/bycol-function)
._

Generic formula
---------------

    =SUM(--(MMULT(TRANSPOSE(ROW(data)^0),--(criteria))>0))

Explanation 
------------

In this example, the goal is to count the number of columns in the data that contain 19 (the value in cell I4). The main challenge in this problem is that the value might appear in any row, and more than once in the same column. If we wanted to simply count the total number of times a value appeared in a range, we could use the [COUNTIF function](https://exceljet.net/functions/countif-function)
. But we need a more advanced formula to count columns that may contain multiple instances of a specific value. The explanation below discusses two options: one based on the [MMULT function](https://exceljet.net/formulas/count-columns-that-contain-specific-values#MMULT_option)
, and one based on the newer [BYCOL function](https://exceljet.net/formulas/count-columns-that-contain-specific-values#BYCOL_option)
.

### MMULT option

One option for solving this problem is the [MMULT function](https://exceljet.net/functions/mmult-function)
. The MMULT function returns the matrix product of two arrays, sometimes called the "dot product". The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. The MMULT function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _array1_ and _array2_, both of which are required. The column count in _array1_ must equal the row count in _array2_. In the example shown, the formula in I6 is:

    =SUM(--(MMULT(TRANSPOSE(ROW(data)^0),--(data=I4))>0))
    

Working from the inside out, the logical criteria used in this formula is:

    --(data=I4)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B4:F15. This expression generates a TRUE or FALSE result for every value in data, and the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) coerces the TRUE and FALSE values to 1s and 0s, respectively. The result is an [array](https://exceljet.net/glossary/array)
 of 1s and 0s like this:

    {0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;1,0,0,1,0;0,1,0,1,0;0,0,0,1,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,1;0,0,0,0,0}
    

Like the original data, this array is 12 rows by 5 columns (12 x 5) and is delivered directly to the MMULT function as _array2_. _Array1_ is derived with this snippet:

    TRANSPOSE(ROW(data)^0)
    

This is the tricky part of the formula. The [ROW function](https://exceljet.net/functions/row-function)
 is used to generate a numeric array of the right size. To perform matrix multiplication with MMULT, the column count in _array1_ (12) must equal the row count in _array2_ (12). ROW returns a 12-row array, which is raised to the power of zero, and converted with the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 into a 12-column array:

    =TRANSPOSE(ROW(data)^0)
    =TRANSPOSE({4;5;6;7;8;9;10;11;12;13;14;15}^0)
    =TRANSPOSE({1;1;1;1;1;1;1;1;1;1;1;1})
    ={1,1,1,1,1,1,1,1,1,1,1,1}
    

With both arrays in place, the MMULT function runs and returns an array with 1 row and 5 columns, {1,1,0,3,1}. This is the data we can use to solve the problem. Each non-zero number represents a column that contains the number 19. We can now simplify the formula to:

    =SUM(--({1,1,0,3,1}>0))
    

We check for non-zero entries with >0 and again coerce TRUE FALSE to 1 and 0 with a double negative (--) to get a final array inside SUM:

    =SUM({1,1,0,1,1})
    

In this array, 1 represents a column that contains 19 and 0 represents a column that does not contain 19. The SUM function returns a final result of 4, the count of all columns that contain the number 19.

### BYCOL option

The [BYCOL function](https://exceljet.net/functions/bycol-function)
 applies a [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to each column in a given array and returns one result per column in a single [array](https://exceljet.net/glossary/array)
. The purpose of BYCOL is to process data in an array or range in a "by column" fashion. For example, if BYCOL is given an array with 5 columns, BYCOL will return an array with 5 results. In this example, we can use BYCOL like this:

    =SUM(BYCOL(data,LAMBDA(col,--(SUM(--(col=I4))>0))))
    

![Using BYCOL to count columns that contain a specific value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20columns%20that%20contain%20specific%20values%20bycol.png?itok=Si_1YfWh "Using BYCOL to count columns that contain a specific value")

The BYCOL function iterates through the named range **data** (B4:D15) one column at a time. At each column, BYCOL evaluates and stores the result of the supplied LAMBDA function:

    LAMBDA(col,--(SUM(--(col=I4))>0))
    

Working from the inside out, the logic here checks for values in _col_ that are equal to I4, which results in an array of TRUE and FALSE values. The TRUE and FALSE values are coerced to 1s and 0s with the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--), and the [SUM function](https://exceljet.net/functions/sum-function)
 sums the result. Next, we check if the result from SUM is > 0 and coerce that result to a 1 or 0 with another double negative. After BYCOL runs, we have an array with one result per column, either a 1 or 0:

    {1,1,0,1,1} // result from BYCOL
    

The formula can now be simplified as follows:

    =SUM({1,1,0,1,1}) // returns 4
    

In the last step, the SUM function sums the items in the array and returns a final result of 4.

### Literal contains

If you need to check for specific text values, in other words, literally check to see if cells contain certain text values, you can change the logic in the formula on this page to use the ISNUMBER and SEARCH function. For example, to count cells/rows that contain "apple" you can use:

    =ISNUMBER(SEARCH("apple",data))
    

Details on how this formula works [here](https://exceljet.net/formulas/cell-contains-specific-text)
.

Related formulas
----------------

[![Excel formula: Count rows that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20that%20contain%20specific%20values.png "Excel formula: Count rows that contain specific values")](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

### [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

In this example, the goal is to count the number of rows in the data that contain the value in cell G4, which is 19. The main challenge in this problem is that the value might appear in any column, and might appear more than once in the same row. If we wanted to simply count the total number of...

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

[![Excel BYCOL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20bycol%20function.png "Excel BYCOL function")](https://exceljet.net/functions/bycol-function)

### [BYCOL Function](https://exceljet.net/functions/bycol-function)

The Excel BYCOL function applies a function to each column in a given array and returns one result per column. BYCOL can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)
    
*   [Count rows with at least n matching values](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)
    
*   [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)
    
*   [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)
    
*   [Count if row meets multiple criteria](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)
    

### Functions

*   [MMULT Function](https://exceljet.net/functions/mmult-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    
*   [BYCOL Function](https://exceljet.net/functions/bycol-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    

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