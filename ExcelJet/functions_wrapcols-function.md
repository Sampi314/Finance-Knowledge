# Excel WRAPCOLS function | Exceljet

**Source:** https://exceljet.net/functions/wrapcols-function

---

[Skip to main content](https://exceljet.net/functions/wrapcols-function#main-content)

[](https://exceljet.net/functions/wrapcols-function#)

*   [Previous](https://exceljet.net/functions/vstack-function)
    
*   [Next](https://exceljet.net/functions/wraprows-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

WRAPCOLS Function
=================

by Dave Bruns · Updated 9 Apr 2025

Related functions 
------------------

[WRAPROWS](https://exceljet.net/functions/wraprows-function)

[TOROW](https://exceljet.net/functions/torow-function)

[TOCOL](https://exceljet.net/functions/tocol-function)

![Excel WRAPCOLS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20wrapcols%20function.png "Excel WRAPCOLS function")

Summary
-------

The Excel WRAPCOLS function converts a one-dimensional array into a two-dimensional array by wrapping values into separate columns. The length of each column is given as the _wrap\_count_ argument: when the count is reached, WRAPCOLS starts a new column.

Purpose 
--------

Wrap array into columns

Return value 
-------------

Array wrapped by column

Syntax
------

    =WRAPCOLS(vector,wrap_count,[pad_with])

*   _vector_ - The array or range to wrap.
*   _wrap\_count_ - Max values in each column.
*   _pad\_with_ - \[optional\] Value to use for unfilled places.

Using the WRAPCOLS function 
----------------------------

The WRAPCOLS function converts a one-dimensional array into a two-dimensional array by wrapping values into separate columns. The length of each column is given as the _wrap\_count_ argument: when the count is reached, WRAPCOLS starts a new column.

The WRAPCOLS function takes three arguments: _vector_, _wrap\_count_, and _pad\_with_. Vector and _wrap\_count_ are both required. _Vector_ must be a one-dimensional array or range. _Wrap\_count_ is a number that represents the length of each column. The final argument, _pad\_with_, is an optional value to use if there are empty spots in the last column. If no value is supplied for _pad\_with,_ WRAPCOLS will return an #N/A error after all values in _vector_ have been used. You can override this behavior by providing a custom value for the _pad\_with_ argument.

### Basic usage

WRAPCOLS outputs values "by column", working top to bottom, left to right. When _wrap\_count_ has been reached, WRAPCOLS starts a new column. In the worksheet below, the goal is to wrap the range C2:J2 into columns that each contain 4 values. The formula in B5 is:

    =WRAPCOLS(C2:J2,4)
    

![WRAPCOLS function - basic usage](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/WRAPCOLS%20-%20basic%20usage.png?itok=4dNuM6Jv "WRAPCOLS function - basic usage")

Notice WRAPCOLS outputs values by column, top to bottom, and each column contains 4 rows.

### Wrap count

_Wrap\_count_ represents the maximum number of values in each column. Once the count has been reached, WRAPCOLS starts a new column. In the screen below, you can see how this works. The formula in D3 uses a _wrap\_count_ of 3:

    =WRAPCOLS(B3:B14,4)
    

The formula in D10 uses a _wrap\_count_ of 4:

    =WRAPCOLS(B3:B14,3)
    

![WRAPCOLS - wrap count behavior](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/WRAPCOLS%20-%20wrap%20count%20examples.png?itok=t2An9ERP "WRAPCOLS - wrap count behavior")

Notice values are output top to bottom.

### Padding

If no value is supplied for _pad\_with,_ WRAPCOLS will return an #N/A error after all values in the source array have been accounted for. You will see these errors appear in the last column when the total number of items in the source array is not evenly divisible by the _wrap\_count_. You can override this behavior by providing a custom value for the _pad\_with_ argument. The formula in D3 shows default behavior. No value for _pad\_with_ has been provided:

    =WRAPCOLS(B3:B12,4)
    

The input range contains only 10 cells, which is not evenly divisible by a _wrap\_count_ of 4. As a result, the last 2 cells return #N/A. The formula in D10 supplied "x" for _pad\_with:_

    =WRAPCOLS(B3:B12,4,"x")
    

![WRAPCOLS - padding example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/WRAPCOLS%20-%20padding%20example.png?itok=Hzh6nuiq "WRAPCOLS - padding example")

Notice the  #N/A errors have been replaced by "x" in the resulting array.

### Notes

*   WRAPCOLS will return a #VALUE! error if vector is not a one-dimensional array or range.
*   _Wrap\_count_ indicates the size of each column not the number of columns.

Related functions
-----------------

[![Excel WRAPROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20wraprows%20function.png "Excel WRAPROWS function")](https://exceljet.net/functions/wraprows-function)

### [WRAPROWS Function](https://exceljet.net/functions/wraprows-function)

The Excel WRAPROWS function converts a one-dimensional array into a two-dimensional array by wrapping values into separate rows. The length of each row is given as the _wrap\_count_ argument: when the count is reached, WRAPROWS starts a new row....

[![Excel TOROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20torow%20function.png "Excel TOROW function")](https://exceljet.net/functions/torow-function)

### [TOROW Function](https://exceljet.net/functions/torow-function)

The Excel TOROW function transforms an array into a single row. By default, TOROW will scan values by row, but TOROW can also scan values by column.

[![Excel TOCOL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20tocol%20function.png "Excel TOCOL function")](https://exceljet.net/functions/tocol-function)

### [TOCOL Function](https://exceljet.net/functions/tocol-function)

The Excel TOCOL function transforms an array into a single column. By default, TOCOL will scan values by row, but TOCOL can also scan values by column.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [WRAPROWS Function](https://exceljet.net/functions/wraprows-function)
    
*   [TOROW Function](https://exceljet.net/functions/torow-function)
    
*   [TOCOL Function](https://exceljet.net/functions/tocol-function)
    

### Links

*   [Microsoft WRAPCOLS function documentation](https://support.microsoft.com/en-us/office/wrapcols-function-d038b05a-57b7-4ee0-be94-ded0792511e2)
    

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