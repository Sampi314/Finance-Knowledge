# Excel WRAPROWS function | Exceljet

**Source:** https://exceljet.net/functions/wraprows-function

---

[Skip to main content](https://exceljet.net/functions/wraprows-function#main-content)

[](https://exceljet.net/functions/wraprows-function#)

*   [Previous](https://exceljet.net/functions/wrapcols-function)
    
*   [Next](https://exceljet.net/functions/xlookup-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

WRAPROWS Function
=================

by Dave Bruns · Updated 14 Apr 2025

Related functions 
------------------

[WRAPCOLS](https://exceljet.net/functions/wrapcols-function)

[TOROW](https://exceljet.net/functions/torow-function)

[TOCOL](https://exceljet.net/functions/tocol-function)

![Excel WRAPROWS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20wraprows%20function.png "Excel WRAPROWS function")

Summary
-------

The Excel WRAPROWS function converts a one-dimensional array into a two-dimensional array by wrapping values into separate rows. The length of each row is given as the _wrap\_count_ argument: when the count is reached, WRAPROWS starts a new row.

Purpose 
--------

Wrap array into rows

Return value 
-------------

Array wrapped by row

Syntax
------

    =WRAPROWS(vector,wrap_count,[pad_with])

*   _vector_ - The array or range to wrap.
*   _wrap\_count_ - Max values in each row.
*   _pad\_with_ - \[optional\] Value to use for unfilled places.

Using the WRAPROWS function 
----------------------------

The WRAPROWS function converts a one-dimensional array into a two-dimensional array by wrapping values into separate rows. The length of each row is provided as the _wrap\_count_ argument: when the count is reached, WRAPROWS starts a new row.

The WRAPROWS function takes three arguments: _vector_, _wrap\_count_, and _pad\_with_. _Vector_ and _wrap\_count_ are both required. _Vector_ must be a one-dimensional [array](https://exceljet.net/glossary/array)
 or [range](https://exceljet.net/glossary/range)
. _Wrap\_count_ is a number that represents the length of each row. The final argument, _pad\_with_, is an optional value to use if there are unfilled places in the last row. If no value is supplied, WRAPROWS will return an #N/A error after all values in _vector_ have been used, and there are still unfilled places in the resulting array. You can override this behavior by providing a custom value for the _pad\_with_ argument.

### Basic usage

WRAPROWS outputs values "by row", working left to right, top to bottom. When _wrap\_count_ has been reached, WRAPROWS starts a new row. In the worksheet below, the goal is to wrap the range C2:J2 into 2 rows that each contain 4 values. The formula in B5 is:

    =WRAPROWS(C2:J2,4)
    

![WRAPCOLS function - basic usage](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/WRAPROWS%20function%20-%20basic%20usage.png?itok=8oNCwLkV "WRAPCOLS function - basic usage")

Notice WRAPROWS outputs values "by row", moving left to right, and each row contains 4 values.

### Wrap count

_Wrap\_count_ represents the maximum number of values in each row. Once the count has been reached, WRAPROWS starts a new row. In the screen below, you can see how this works. The formula in D3 uses a _wrap\_count_ of 4:

    =WRAPROWS(B3:B14,4)
    

The formula in D9 uses a _wrap\_count_ of 3:

    =WRAPROWS(B3:B14,3)
    

![WRAPROWS function - wrap count behavior](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/WRAPROWS%20function%20-%20wrap%20count%20behavior.png?itok=db5FBx8y "WRAPROWS function - wrap count behavior")

Notice values are output from left to right, and top to bottom.

### Padding

If no value is supplied for _pad\_with,_ WRAPROWS will return an #N/A error after all values in the source array have been accounted for. You will see these errors appear in the last row when the size of the source array is not evenly divisible by the _wrap\_count_. You can override this behavior by providing a custom value for the _pad\_with_ argument. The formula in D3 shows default behavior. No value for _pad\_with_ has been provided:

    =WRAPROWS(B3:B12,4)
    

The input range contains only 10 cells, which is not evenly divisible by 4. As a result, the last 2 cells return #N/A. To override this behavior, provide a value for _pad\_with_. The formula in D10 supplies "x" for _pad\_with:_

    =WRAPROWS(B3:B12,4,"x")
    

![WRAPROWS function - padding example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/WRAPROWS%20function%20-%20padding%20example.png?itok=wfDHMDXa "WRAPROWS function - padding example")

Notice the  #N/A errors have been replaced by "x" in the resulting array.

### Notes

*   WRAPROWS will return a #VALUE! error if _vector_ is not a one-dimensional array or range.
*   _Wrap\_count_ indicates the length of each row, not the number of rows.

Related functions
-----------------

[![Excel WRAPCOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20wrapcols%20function.png "Excel WRAPCOLS function")](https://exceljet.net/functions/wrapcols-function)

### [WRAPCOLS Function](https://exceljet.net/functions/wrapcols-function)

The Excel WRAPCOLS function converts a one-dimensional array into a two-dimensional array by wrapping values into separate columns. The length of each column is given as the _wrap\_count_ argument: when the count is reached, WRAPCOLS starts a new column....

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

*   [WRAPCOLS Function](https://exceljet.net/functions/wrapcols-function)
    
*   [TOROW Function](https://exceljet.net/functions/torow-function)
    
*   [TOCOL Function](https://exceljet.net/functions/tocol-function)
    

### Links

*   [Microsoft WRAPROWS function documentation](https://support.microsoft.com/en-us/office/wraprows-function-796825f3-975a-4cee-9c84-1bbddf60ade0)
    

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