# Remove blank rows - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-blank-rows

---

[Skip to main content](https://exceljet.net/formulas/remove-blank-rows#main-content)

[](https://exceljet.net/formulas/remove-blank-rows#)

*   [Previous](https://exceljet.net/formulas/random-sort)
    
*   [Next](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Remove blank rows
=================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[BYROW](https://exceljet.net/functions/byrow-function)

![Excel formula: Remove blank rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove_blank_rows.png "Excel formula: Remove blank rows")

Summary
-------

To remove blank/empty rows from a range, you can use a formula based on the [FILTER function](https://exceljet.net/functions/filter-function)
 and the [BYROW function](https://exceljet.net/functions/byrow-function)
. In the worksheet shown, the formula in cell G5 is:

    =FILTER(B5:E16,BYROW(B5:E16,LAMBDA(row,SUM(--(row<>""))>0)))

When the formula is entered in cell G5, the FILTER function uses the result from the BYROW function to return only non-empty rows from the range B5:E16.

Generic formula
---------------

    =FILTER(data,BYROW(data,LAMBDA(row,SUM(--(row<>""))<>0)))

Explanation 
------------

In this example, the goal is to remove empty rows from a range with a formula. One approach is to use the BYROW function to identify all non-empty rows in the range and pass this result into the FILTER function as the _include_ argument. This is the approach used in the worksheet shown, where the formula in cell G5 is:

    =FILTER(B5:E16,BYROW(B5:E16,LAMBDA(row,SUM(--(row<>""))>0)))

Working from the inside out, the [BYROW function](https://exceljet.net/functions/byrow-function)
 is used to check for non-blank rows like this:

    BYROW(B5:E16,LAMBDA(row,SUM(--(row<>""))>0))

The purpose of BYROW is to process data in an array or range in a "by row" fashion. At each row, BYROW applies a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
 that contains the calculation needed to achieve the desired result. In this case, we want to identify non-blank rows. In other words, we want to check for rows that contain content in any cell. This is done in the following snippet:

    LAMBDA(row,SUM(--(row<>""))>0)

The BYROW function delivers the range B5:E16 row-by-row to the LAMBDA above as the _row_ argument. The LAMBDA then runs this calculation on each row:

    SUM(--(row<>""))>0

The <> operator means "not equal to", so <>"" means "not empty". The result is an array of TRUE and FALSE values. In row 5, the result is an array like this:

    =SUM(--({TRUE,TRUE,TRUE,TRUE}))>0

Next, the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) above converts TRUE to 1 and FALSE to 0:

    =SUM({1,1,1,1})>0 // returns TRUE

The [SUM function](https://exceljet.net/functions/sum-function)
 then returns 4, and the expression returns TRUE since 4 is greater than 0. Each row is processed in the same way, and BYROW returns all results in a single array like this:

    {TRUE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE}

Notice the array contains 12 results because the original range contains 12 rows. In this array, TRUE indicates non-empty rows and FALSE indicates empty rows. The array is returned directly to the FILTER function as the _include_ argument:

    =FILTER(B5:E16,{TRUE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE})

FILTER returns the 9 rows that correspond to TRUE as a final result.

### Simple option

The formula above is more complex because it tests every cell in a row to make sure it is empty. If you only need to test a single column to determine if a row is blank you can use a simpler formula like this:

    FILTER(range,CHOOSECOLS(range,1)<>"")

In this formula, we use the FILTER formula as before. However, for the _include_ argument we use the [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
 instead of BYROW:

    CHOOSECOLS(range,1)<>"" // column 1 only

CHOOSECOLS runs first and extracts just the first column from the range. Then we simply test each cell in the column with <>"". Because each cell corresponds to a row, the result is a single array of TRUE and FALSE values that are used to filter the range. Adapting this formula to the example above, we have:

    =FILTER(B5:E16,CHOOSECOLS(B5:E16,1)<>"")

After CHOOSECOLS is evaluated, we have the following:

    =FILTER(B5:E16,{TRUE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE})

The final result is the same as the FILTER + BYROW formula above. Note however that we are only testing column 1, so rows that contain data in other columns will be discarded.

### More details

*   To simply identify blank and non-blank rows, see: [Row is blank](https://exceljet.net/formulas/row-is-blank)
    .
*   For more on the Boolean logic used above, see [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    .

Related formulas
----------------

[![Excel formula: Row is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/row_is_blank.png "Excel formula: Row is blank")](https://exceljet.net/formulas/row-is-blank)

### [Row is blank](https://exceljet.net/formulas/row-is-blank)

The goal is to use a formula to check if all cells in a row are blank or empty and return TRUE or FALSE. One way to solve this problem is with the SUMPRODUCT function, as seen in the worksheet above. Another approach is to use the newer BYROW function. Both methods are described below. SUMPRODUCT...

[![Excel formula: Filter exclude blank values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20exclude%20blank%20values.png "Excel formula: Filter exclude blank values")](https://exceljet.net/formulas/filter-exclude-blank-values)

### [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)

The FILTER function is designed to extract data that matches one or more criteria. In this case, we want to apply criteria that requires all three columns in the source data (Name, Group, and Room) to have data. In other words, if a row is missing any of these values, we want to exclude that row...

[![Excel formula: Count rows that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20that%20contain%20specific%20values.png "Excel formula: Count rows that contain specific values")](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

### [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

In this example, the goal is to count the number of rows in the data that contain the value in cell G4, which is 19. The main challenge in this problem is that the value might appear in any column, and might appear more than once in the same row. If we wanted to simply count the total number of...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Row is blank](https://exceljet.net/formulas/row-is-blank)
    
*   [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)
    
*   [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

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