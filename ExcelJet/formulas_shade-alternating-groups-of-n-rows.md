# Shade alternating groups of n rows - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/shade-alternating-groups-of-n-rows

---

[Skip to main content](https://exceljet.net/formulas/shade-alternating-groups-of-n-rows#main-content)

[](https://exceljet.net/formulas/shade-alternating-groups-of-n-rows#)

*   [Previous](https://exceljet.net/formulas/highlight-values-not-between-x-and-y)
    
*   [Next](https://exceljet.net/formulas/data-validation-allow-numbers-only)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Shade alternating groups of n rows
==================================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[ROW](https://exceljet.net/functions/row-function)

[CEILING](https://exceljet.net/functions/ceiling-function)

[ISEVEN](https://exceljet.net/functions/iseven-function)

[ISODD](https://exceljet.net/functions/isodd-function)

![Excel formula: Shade alternating groups of n rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Shade%20alternating%20groups%20of%20n%20rows.png "Excel formula: Shade alternating groups of n rows")

Summary
-------

To highlight rows in groups of "n" (i.e. shade every 3 rows, every 5 rows, etc.) you can apply conditional formatting with a formula based on the [ROW](https://exceljet.net/functions/row-function)
, [CEILING](https://exceljet.net/functions/ceiling-function)
 and [ISEVEN](https://exceljet.net/functions/iseven-function)
 functions. In the example shown, the formula used to highlight every 3 rows in the table is:

    =ISEVEN(CEILING(ROW()-4,3)/3)
    

Where 3 is n (the number of rows to group) and 4 is an offset to normalize the first row to 1, as explained below.

Generic formula
---------------

    =ISEVEN(CEILING(ROW()-offset,n)/n)

Explanation 
------------

Working from the inside out, we first "normalize" row numbers to begin with 1 using the ROW function and an offset:

    ROW()-offset
    

In this case, the first row of data is in row 5, so we use an offset of 4:

    ROW()-4 // 1 in row 5
    ROW()-4 // 2 in row 6
    ROW()-4 // 3 in row 7
    etc.
    

The result goes into the CEILING function, which rounds incoming values up to a given multiple of n. Essentially, the CEILING function counts by a given multiple of n:

![Counting rows by multiples of n](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20rows%20by%20multiples%20of%20n.png?itok=Kaugcym1 "Counting rows by multiples of n")

This count is then divided by n to count by groups of n, starting with 1:

![Counting rows in groups of n](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/counting%20by%20groups%20of%20n.png?itok=IWYc6WsR "Counting rows in groups of n")

Finally, the ISEVEN function is used to force a TRUE result for all even row groups, which triggers the conditional formatting.

Odd row groups return FALSE so no conditional formatting is applied.

### Shade first group

To shade rows starting with the first group of n rows, instead of the second, replace ISEVEN with ISODD:

    =ISODD(CEILING(ROW()-offset,n)/n)
    

Related formulas
----------------

[![Excel formula: Highlight every other row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20every%20other%20row.png "Excel formula: Highlight every other row")](https://exceljet.net/formulas/highlight-every-other-row)

### [Highlight every other row](https://exceljet.net/formulas/highlight-every-other-row)

When you use a formula to apply conditional formatting, the formula is evaluated for every cell in the selection. In this case, there are no addresses in the formula, so, for every cell in the data, the ROW and ISEVEN functions are run. ROW returns the row number of the cell, and ISEVEN returns...

[![Excel formula: Highlight entire rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20entire%20rows.png "Excel formula: Highlight entire rows")](https://exceljet.net/formulas/highlight-entire-rows)

### [Highlight entire rows](https://exceljet.net/formulas/highlight-entire-rows)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the address of the active cell (B5) is used for the row (5) and entered as a mixed address , with column D locked and the row...

Related functions
-----------------

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

[![Excel ISEVEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iseven%20function.png "Excel ISEVEN function")](https://exceljet.net/functions/iseven-function)

### [ISEVEN Function](https://exceljet.net/functions/iseven-function)

The Excel ISEVEN function returns TRUE when a value is an even number, and FALSE when a value is an odd number. ISEVEN will return the #VALUE error if a value is not numeric.

[![Excel ISODD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isodd%20function.png "Excel ISODD function")](https://exceljet.net/functions/isodd-function)

### [ISODD Function](https://exceljet.net/functions/isodd-function)

The Excel ISODD function returns TRUE when a value is an odd number, and FALSE when a value is an even number. ISODD will return the #VALUE error if a value is not numeric.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20zebra%20stripes%20with%20conditional%20formatting-thumb.png)](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

### [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

In this video, we'll look at how to use conditional formatting to shade every other row in a table. This is sometimes called "zebra striping". In this spreadsheet, we have a table of employees with a small amount of formatting. To get shading on every other row, we could just convert this table to...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Highlight every other row](https://exceljet.net/formulas/highlight-every-other-row)
    
*   [Highlight entire rows](https://exceljet.net/formulas/highlight-entire-rows)
    

### Functions

*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    
*   [ISEVEN Function](https://exceljet.net/functions/iseven-function)
    
*   [ISODD Function](https://exceljet.net/functions/isodd-function)
    

### Videos

*   [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)
    

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