# Sum every n rows - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-every-n-rows

---

[Skip to main content](https://exceljet.net/formulas/sum-every-n-rows#main-content)

[](https://exceljet.net/formulas/sum-every-n-rows#)

*   [Previous](https://exceljet.net/formulas/sum-entire-row)
    
*   [Next](https://exceljet.net/formulas/sum-every-nth-column)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum every n rows
================

by Dave Bruns · Updated 14 Mar 2025

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

[OFFSET](https://exceljet.net/functions/offset-function)

![Excel formula: Sum every n rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20every%20n%20rows.png "Excel formula: Sum every n rows")

Summary
-------

To sum every n rows, you can use a formula based on the [OFFSET function](https://exceljet.net/functions/offset-function)
 and the [SUM function](https://exceljet.net/functions/sum-function)
. In the example shown, the formula in F4 is:

    =SUM(OFFSET($C$5,(ROW()-4)*5,0,5,1))
    

where n=5 because each week contains 5 rows of data. As the formula is copied down, it returns the sum of every 5 values in the range C5:C19.

Generic formula
---------------

    =SUM(OFFSET(A1,(ROW()-offset)*n,0,n,1))

Explanation 
------------

In this example, the goal is to calculate a weekly total using the data as shown. Notice each week corresponds to 5 rows of data (Monday-Friday) so we will need to sum values in every 5 rows. To build a range that corresponds to the correct 5 rows for each week, we use the OFFSET function. To sum the values returned by OFFSET, we use the SUM function. The complete formula in cell F4, copied down, is:

    =SUM(OFFSET($C$5,(ROW()-4)*5,0,5,1))
    

### Calculating ranges

The [OFFSET function](https://exceljet.net/functions/offset-function)
 returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, and (5) a width in columns. In the example shown, we use OFFSET inside of SUM like this:

    OFFSET($C$5,(ROW()-4)*5,0,5,1)
    

The starting _reference_ is C5 since this is the first value in the data. Notice we use an absolute reference because we don't want this reference to change later when we copy the formula down. The next argument, _rows_, is the crux of the problem because this is where we need logic that will figure out the correct starting row for each week.

To calculate the right starting point, we use the [ROW function](https://exceljet.net/functions/row-function)
. ROW returns the row number for a given reference or, if no reference is provided, the row number of the cell containing the formula. Because the formula sits in cell F4, ROW() will return 4. We use this fact to create the logic we need. We first subtract 4 as an "offset" because we want to create a zero-based index for reasons made clear below. Then, we multiply the result by 5. This is how this snippet will evaluate in cells F4, F5, and F6:

    F4=(ROW()-4)*5 // returns 0
    F5=(ROW()-4)*5 // returns 5
    F6=(ROW()-4)*5 // returns 10
    

To finish off the arguments for OFFSET, we provide _cols_ as zero, because we want to stay in the same column. We provide _height_ as 5 because we want a range that contains 5 rows. Finally, we provide _width_ as 1, because we want a range that contains 1 column. After the row logic runs, this is how OFFSET works F4, F5, and F6:

    F4=OFFSET($C$5,0,0,5,1) // returns C5:C9
    F5=OFFSET($C$5,5,0,5,1) // returns C10:C14
    F6=OFFSET($C$5,10,0,5,1) // returns C15:C19
    

### Summing ranges

The final step in the problem is just to sum the ranges provided by OFFSET. This is done with the [SUM function](https://exceljet.net/functions/sum-function)
. After OFFSET is evaluated, the resulting range is delivered directly to the SUM function, which sums the values in the range and returns a final result. As the formula is copied down into F4:F6, we get the final totals per week:

    SUM(C5:C9) // returns 220
    SUM(C10:C14) // returns 202
    SUM(C15:C19) // returns 285
    

To recap, OFFSET returns a calculation of the correct range for each week using the row logic explained above. The SUM function sums the ranges returned by OFFSET.

Related formulas
----------------

[![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")](https://exceljet.net/formulas/sum-every-nth-column)

### [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)

In this example, the goal is to sum every nth value by column in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value by column, if n =3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and n is entered into...

[![Excel formula: Copy value from every nth row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20row_0.png "Excel formula: Copy value from every nth row")](https://exceljet.net/formulas/copy-value-from-every-nth-row)

### [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)

In this example, the goal is to copy every nth value from column B, where n is a variable that can be changed as needed. In Excel, it's difficult to create formulas that skip rows following a certain pattern, because the references in the formula will automatically change as the formula is copied...

[![Excel formula: Copy value from every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20column.png "Excel formula: Copy value from every nth column")](https://exceljet.net/formulas/copy-value-from-every-nth-column)

### [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)

In Excel, you can't easily create formulas that skip columns following a certain pattern, because the references in the formula will automatically change to maintain the relationship between the original source cell and the new target cell. However, with a little work, it's possible to construct...

Related functions
-----------------

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
    
*   [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)
    
*   [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)
    

### Functions

*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    

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