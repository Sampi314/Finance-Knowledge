# Row is blank - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/row-is-blank

---

[Skip to main content](https://exceljet.net/formulas/row-is-blank#main-content)

[](https://exceljet.net/formulas/row-is-blank#)

*   [Previous](https://exceljet.net/formulas/range-contains-specific-date)
    
*   [Next](https://exceljet.net/formulas/total-columns-in-range)
    

[Range](https://exceljet.net/formulas#Range)

Row is blank
============

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[BYROW](https://exceljet.net/functions/byrow-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

![Excel formula: Row is blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/row_is_blank.png "Excel formula: Row is blank")

Summary
-------

To determine if all cells in a row are blank (i.e. empty), you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in cell J5 is:

    =SUMPRODUCT(--(C5:H5<>""))=0

As the formula is copied down, it returns TRUE if all cells in a row are empty and FALSE if any cell contains a value. In newer versions of Excel, you can also use the [BYROW function](https://exceljet.net/functions/byrow-function)
, as explained below.

Generic formula
---------------

    =SUMPRODUCT(--(range<>""))=0

Explanation 
------------

The goal is to use a formula to check if all cells in a row are blank or empty and return TRUE or FALSE. One way to solve this problem is with the SUMPRODUCT function, as seen in the worksheet above. Another approach is to use the newer BYROW function. Both methods are described below.

### SUMPRODUCT function

The SUMPRODUCT function is a Swiss Army Knife function that appears in all kinds of formulas [because it can handle many array operations natively](https://exceljet.net/articles/why-sumproduct)
 in older versions of Excel. In this case, the formula we are using in cell J5 is:

    =SUMPRODUCT(--(C5:H5<>""))=0

Working from the inside out, the expression below is used to check for data in row 5 like this:

    C5:H5<>""

The <> [operator](https://exceljet.net/glossary/logical-operators)
 means "not equal to", so <>"" means "not empty". Notice we are excluding column B, which contains times. Because there are six cells in the range C5:H5, the expression returns six results in an array like this:

    =SUMPRODUCT(--({FALSE,FALSE,TRUE,FALSE,TRUE,TRUE}))=0

In this array, FALSE corresponds to cells that _are not empty_ and TRUE corresponds to cells that _are empty_. Next, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) operation to convert TRUE values to 1 and FALSE values to 0. The result looks like this:

    =SUMPRODUCT({0,0,1,0,1,1})=0

SUMPRODUCT then sums the values in the array and returns 3:

    =3=0 // returns FALSE

The final result in J5 is FALSE since 3 is not equal to zero. This formula will return TRUE only when all cells in a given row are empty. For example, in row 7, which is empty, the formula evaluates like this:

    =SUMPRODUCT(--(C7:H7<>""))=0
    =SUMPRODUCT(--({FALSE,FALSE,FALSE,FALSE,FALSE,FALSE}))=0
    =SUMPRODUCT({0,0,0,0,0,0})=0
    =TRUE

See [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
 for more information about the logic used in SUMPRODUCT.

### BYROW function

In newer versions of Excel, you can use the [BYROW function](https://exceljet.net/functions/byrow-function)
 to test all rows in a range in one step. The purpose of BYROW is to process data in an array or range in a "by row" fashion. BYROW applies a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to each row in a range or array and returns one result per row as a single [array](https://exceljet.net/glossary/array)
. You can see the result in the worksheet below:

![Testing for blank rows with the BYROW function](https://exceljet.net/sites/default/files/images/formulas/inline/row_is_blank_with_byrow_function.png "Testing for blank rows with the BYROW function")

The formula used in cell J5 is:

    =BYROW(C5:H16,LAMBDA(row,SUM(--(row<>""))=0))

The BYROW function delivers the range C5:H16 one row at a time to the LAMBDA function, which uses the [SUM function](https://exceljet.net/functions/sum-function)
 and the same [Boolean logic](https://exceljet.net/videos/boolean-operations-in-array-formulas)
 explained above to count non-blank cells. The result from SUM is then compared to zero to force a TRUE or FALSE result. After processing the entire range, BYROW delivers all results in a single array:

    {FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE}

Notice the array contains 12 results because the original range contains 12 rows. These results spill into the range J5:J16. Other than convenience, the advantage of using BYROW like this is that the results can be used in other functions. For example, you can use BYROW inside the [FILTER function](https://exceljet.net/functions/filter-function)
 to remove blank rows.

Related formulas
----------------

[![Excel formula: All cells in range are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all_cells_in_range_are_blank.png "Excel formula: All cells in range are blank")](https://exceljet.net/formulas/all-cells-in-range-are-blank)

### [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)

When working with Excel, there are times when you need to determine if a range of cells is empty. This can be useful in various scenarios, such as data validation, error checking, or report preparation. In this article, we'll explore a couple of formulas that can help you check if all cells in a...

[![Excel formula: Get row totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20row%20totals.png "Excel formula: Get row totals")](https://exceljet.net/formulas/get-row-totals)

### [Get row totals](https://exceljet.net/formulas/get-row-totals)

In this example, the goal is to return an array with nine subtotals, one for each of the colors named in column B. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We can'...

[![Excel formula: Count rows that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20that%20contain%20specific%20values.png "Excel formula: Count rows that contain specific values")](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

### [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

In this example, the goal is to count the number of rows in the data that contain the value in cell G4, which is 19. The main challenge in this problem is that the value might appear in any column, and might appear more than once in the same row. If we wanted to simply count the total number of...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

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

*   [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)
    
*   [Get row totals](https://exceljet.net/formulas/get-row-totals)
    
*   [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    

### Training

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