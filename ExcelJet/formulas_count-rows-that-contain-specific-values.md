# Count rows that contain specific values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-rows-that-contain-specific-values

---

[Skip to main content](https://exceljet.net/formulas/count-rows-that-contain-specific-values#main-content)

[](https://exceljet.net/formulas/count-rows-that-contain-specific-values#)

*   [Previous](https://exceljet.net/formulas/count-paired-items-in-listed-combinations)
    
*   [Next](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)
    

[Count](https://exceljet.net/formulas#Count)

Count rows that contain specific values
=======================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[MMULT](https://exceljet.net/functions/mmult-function)

[COLUMN](https://exceljet.net/functions/column-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[BYROW](https://exceljet.net/functions/byrow-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7119/download?token=NkEpDybS)
 (15.72 KB)

![Excel formula: Count rows that contain specific values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20rows%20that%20contain%20specific%20values.png "Excel formula: Count rows that contain specific values")

Summary
-------

To count rows that contain specific values, you can use a formula based on the [MMULT](https://exceljet.net/functions/mmult-function)
, [TRANSPOSE](https://exceljet.net/functions/transpose-function)
, [COLUMN](https://exceljet.net/functions/column-function)
, and [SUM](https://exceljet.net/functions/sum-function)
 functions. In the example shown, the formula in G6 is:

    =SUM(--(MMULT(--(data=G4),TRANSPOSE(COLUMN(data)^0))>0))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B4:D15. The result is 5, the number of rows that contain the number 19.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control shift enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
. See below for a formula that performs the same task with the newer [BYROW function](https://exceljet.net/functions/byrow-function)
._

Generic formula
---------------

    =SUM(--(MMULT(--(criteria),TRANSPOSE(COLUMN(data)))>0))

Explanation 
------------

In this example, the goal is to count the number of rows in the data that contain the value in cell G4, which is 19. The main challenge in this problem is that the value might appear in any column, and might appear more than once in the same row. If we wanted to simply count the total number of times a value appeared in a range, we could use the [COUNTIF function](https://exceljet.net/functions/countif-function)
. But we need a more advanced formula to count rows that may contain multiple instances of the value. The explanation below reviews two options: one based on the [MMULT function](https://exceljet.net/formulas/count-rows-that-contain-specific-values#MMULT_option)
, and one based on the newer [BYROW function](https://exceljet.net/formulas/count-rows-that-contain-specific-values#BYROW_option)
.

### Background study

*   [The double negative in Excel formulas](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
    
*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    
*   [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
    

### MMULT option

One option for solving this problem is the [MMULT function](https://exceljet.net/functions/mmult-function)
. The MMULT function returns the matrix product of two arrays, sometimes called the "dot product". The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. The MMULT function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _array1_ and _array2_, both of which are required. The column count of _array1_ must equal the row count of _array2_. In the example shown, the formula in G6 is:

    =SUM(--(MMULT(--(data=G4),TRANSPOSE(COLUMN(data)^0))>0))
    

Working from the inside out, the logical criteria used in this formula is:

    --(data=G4)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B4:D15. This expression generates a TRUE or FALSE result for every value in data, and the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) coerces the TRUE FALSE values to 1s and 0s, respectively. The result is an [array](https://exceljet.net/glossary/array)
 of 1s and 0s like this:

    {1,0,1;0,0,0;1,0,0;0,0,0;0,0,0;0,0,0;0,0,0;0,1,1;0,0,0;0,0,0;1,0,0;0,1,0}
    

Like the original data, this array is 12 rows by 3 columns (12 x 3) and is delivered directly to the MMULT function as _array1_. _Array2_ is derived with this snippet:

    TRANSPOSE(COLUMN(data)^0)
    

Which returns an array of three 1s like this:

    {1;1;1}
    

This is the tricky and fun part of this formula. The [COLUMN function](https://exceljet.net/functions/column-function)
 is used for convenience as a way to generate a numeric array of the right size. To perform matrix multiplication with MMULT, the column count in _array1_ (3) must equal the row count in _array2_ (3). COLUMN returns the 3-column array {2,3,4} which, when raised to the power of zero, becomes {1,1,1}. Next, the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 transposes the 1 x 3 array into a 3 x 1 array:

    TRANSPOSE({1,1,1}) // returns {1;1;1}
    

With both arrays in place, the MMULT function runs and returns an array with 12 rows and 1 column, {2;0;1;0;0;0;0;2;0;0;1;1}. This array contains the count per row of cells that contain 19, and we can use this data to solve the problem. Each non-zero number represents a row that contains the number 19, so we can convert non-zero values to 1s and sum up the result:

    =SUM(--({2;0;1;0;0;0;0;2;0;0;1;1}>0))
    

We check for non-zero entries with >0 and again coerce TRUE FALSE to 1 and 0 with a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to get a final array inside SUM:

    =SUM({1;0;1;0;0;0;0;1;0;0;1;1})
    

In this array, 1 represents a row that contains 19 and a 0 represents a row that does not contain 19. The SUM function returns a final result of 5, the count of all rows that contain the number 19.

### BYROW option

The [BYROW function](https://exceljet.net/functions/byrow-function)
 applies a [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to each row in a given array and returns one result per row as a single [array](https://exceljet.net/glossary/array)
. The purpose of BYROW is to process data in an array or range in a "by row" fashion. For example, if BYROW is given an array with 12 rows, BYCOL will return an array with 12 results. In this example, we can use BYROW like this:

    =SUM(BYROW(data,LAMBDA(row,--(SUM(--(row=G4))>0))))
    

![Using BYROW to count rows that contain a specific value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20rows%20that%20contain%20specific%20values%20byrow.png?itok=MsaiZ9x3 "Using BYROW to count rows that contain a specific value")

The BYROW function iterates through the named range **data** (B4:D15) one row at a time. At each row, BYCOL evaluates and stores the result of the supplied LAMBDA function:

    LAMBDA(row,--(SUM(--(row=G4))>0))
    

The logic here checks for values in _row_ that are equal to G4, which results in an array of TRUE and FALSE values. The TRUE and FALSE values are coerced to 1s and 0s with the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--), and the SUM function sums the result. Next, we check if the total from SUM is >0, and coerce that result to a 1 or 0. After BYROW runs, we have an array with one result per row, either a 1 or 0:

    {1;0;1;0;0;0;0;1;0;0;1;1} // result from BYROW
    

The formula can now be simplified as follows:

    =SUM({1;0;1;0;0;0;0;1;0;0;1;1}) // returns 5
    

In the last step, the SUM function sums the items in the array and returns a final result of 5.

### Literal contains

To check for specific substrings (i.e. check to see if cells _contain_ a specific text value) you can adjust the logic in the formulas above to use the [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [SEARCH](https://exceljet.net/functions/search-function)
 functions. For example, to check if a value _contains_ "apple" you can use:

    =ISNUMBER(SEARCH("apple",data))
    

This expression would replace data=G4 logic above like this:

    =SUM(--(MMULT(--(ISNUMBER(SEARCH(G4,data))),TRANSPOSE(COLUMN(data)^0))>0))
    

See [this example](https://exceljet.net/formulas/cell-contains-specific-text)
 for more information on using ISNUMBER with SEARCH.

Related formulas
----------------

[![Excel formula: Count columns that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20columns%20that%20contain%20specific%20values.png "Excel formula: Count columns that contain specific values")](https://exceljet.net/formulas/count-columns-that-contain-specific-values)

### [Count columns that contain specific values](https://exceljet.net/formulas/count-columns-that-contain-specific-values)

In this example, the goal is to count the number of columns in the data that contain 19 (the value in cell I4). The main challenge in this problem is that the value might appear in any row, and more than once in the same column. If we wanted to simply count the total number of times a value...

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

[![Excel formula: Get row totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20row%20totals.png "Excel formula: Get row totals")](https://exceljet.net/formulas/get-row-totals)

### [Get row totals](https://exceljet.net/formulas/get-row-totals)

In this example, the goal is to return an array with nine subtotals, one for each of the colors named in column B. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We can'...

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

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

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

*   [Count columns that contain specific values](https://exceljet.net/formulas/count-columns-that-contain-specific-values)
    
*   [Count rows with at least n matching values](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)
    
*   [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)
    
*   [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)
    
*   [Count if row meets multiple criteria](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)
    
*   [Get row totals](https://exceljet.net/formulas/get-row-totals)
    

### Functions

*   [MMULT Function](https://exceljet.net/functions/mmult-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    
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