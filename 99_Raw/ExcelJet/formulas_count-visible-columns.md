# Count visible columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-visible-columns

---

[Skip to main content](https://exceljet.net/formulas/count-visible-columns#main-content)

[](https://exceljet.net/formulas/count-visible-columns#)

*   [Previous](https://exceljet.net/formulas/count-cells-in-range)
    
*   [Next](https://exceljet.net/formulas/countifs-with-variable-range)
    

[Range](https://exceljet.net/formulas#Range)

Count visible columns
=====================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[CELL](https://exceljet.net/functions/cell-function)

[N](https://exceljet.net/functions/n-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Count visible columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20visible%20columns.png "Excel formula: Count visible columns")

Summary
-------

To count visible columns in a range, you can use a helper formula based on the CELL function with IF, then tally results with the SUM function. In the example shown, the formula in I4 is:

    =SUM(key)
    

where "key" is the [named range](https://exceljet.net/glossary/named-range)
 B4:F4, and all cells contain this formula, copied across:

    =N(CELL("width",B4)>0)
    

To see the count change, you _must force calculation with F9_, or perform another worksheet change that triggers recalculation. Below is the same worksheet with all columns visible:

![Count visible columns - all columns unhidden](https://exceljet.net/sites/default/files/images/formulas/inline/count%20visible%20columns%20all%20columns%20visisble.png "Count visible columns - all columns unhidden")

_Note: I ran into the core idea for this formula on the [excellent wmfexcel.com site](https://wmfexcel.com/2015/08/29/a-trick-to-sum-visible-columns-only-without-vba/)
._

Generic formula
---------------

    =N(CELL("width",A1)>0)

Explanation 
------------

There is no direct way to detect a hidden column with a formula in Excel. You might think of using the [SUBTOTAL function](https://exceljet.net/functions/subtotal-function)
, but SUBTOTAL only works with vertical ranges. As a result, the approach described in this example is a workaround based on a helper formula that must be entered in a range that includes all columns in the scope of interest. In this example, this range is the named range "key".

In the example shown, columns C and E are hidden. The helper formula, entered in B4 and copied across B4:F4, is based on the [CELL function](https://exceljet.net/functions/cell-function)
:

    =CELL("width",B4)>0
    

The CELL function will only return a width for a cell in a visible column. When a column is hidden, the same formula will return zero. By checking if the result is greater than zero, we get a TRUE or FALSE result. The N function is used to coerce TRUE to 1 and FALSE to zero, so the final result is 1 when a column is visible, and 0 when a column is hidden. Nice.

To count visible columns, we use the [SUM function](https://exceljet.net/videos/how-to-use-the-sum-function)
 formula in I4:

    =SUM(key)
    

where "key" is the named range B4:F4.

### Count hidden columns

To count hidden columns, the formula in I5 is:

    =COLUMNS(key)-SUM(key)
    

The [COLUMNS function](https://exceljet.net/functions/columns-function)
 returns the total columns in the range (5) and the SUM function returns the sum of visible columns (3), so the final result is 2:

    =COLUMNS(key)-SUM(key)
    =5-3
    =2
    

### With other operations

Once you have the "column key" in place, you can use it with other operations. For example, you could SUM values in visible columns by using SUM like this:

    =SUM(key*B6:F6)
    

Although each cell in B6:F6 contains the number 25, SUM will return 75 when column C and E are hidden, as shown in the example.

_Note: CELL function is a [volatile function](https://exceljet.net/glossary/volatile-function)
. Volatile functions normally recalculate with every worksheet change, so they can cause performance problems. Unfortunately, CELL does not fire when a column is hidden or made visible again. This means you will not see correct results until the worksheet recalculates, either with a normal change, or by pressing F9._

Related formulas
----------------

[![Excel formula: Count visible rows in a filtered list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20visible%20rows%20in%20a%20filtered%20list.png "Excel formula: Count visible rows in a filtered list")](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list)

### [Count visible rows in a filtered list](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list)

In this example, the goal is to count rows that are visible and ignore rows that are hidden. This is a job for the SUBTOTAL function . SUBTOTAL can perform a variety of calculations like COUNT, SUM, MAX, MIN, and more. What makes SUBTOTAL interesting and useful is that it automatically ignores...

[![Excel formula: Sum visible rows in a filtered list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_visible_rows_in_a_filtered_list.png "Excel formula: Sum visible rows in a filtered list")](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)

### [Sum visible rows in a filtered list](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)

In this example, the goal is to sum values in rows that are visible and ignore values in rows that are hidden. The range F7:F19 contains 13 values total, 4 of which are hidden by the filter applied to column C. This is a good job for the SUBTOTAL function , which can distinguish between visible and...

Related functions
-----------------

[![Excel CELL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20cell%20function.png "Excel CELL function")](https://exceljet.net/functions/cell-function)

### [CELL Function](https://exceljet.net/functions/cell-function)

The Excel CELL function returns information about a cell in a worksheet. The type of information to be returned is specified as _info\_type_. CELL can get things like address and filename, as well as detailed info about the formatting used in the cell. See below for a full list of...

[![Excel N function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20n%20function.png "Excel N function")](https://exceljet.net/functions/n-function)

### [N Function](https://exceljet.net/functions/n-function)

The Excel N function returns a number when given a value. The N function can be used to convert TRUE and FALSE to 1 and 0 respectively. When given a text value, the N function returns zero.

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count visible rows in a filtered list](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list)
    
*   [Sum visible rows in a filtered list](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)
    

### Functions

*   [CELL Function](https://exceljet.net/functions/cell-function)
    
*   [N Function](https://exceljet.net/functions/n-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

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