# Running count of occurrence in list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/running-count-of-occurrence-in-list

---

[Skip to main content](https://exceljet.net/formulas/running-count-of-occurrence-in-list#main-content)

[](https://exceljet.net/formulas/running-count-of-occurrence-in-list#)

*   [Previous](https://exceljet.net/formulas/histogram-with-frequency)
    
*   [Next](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    

[Count](https://exceljet.net/formulas#Count)

Running count of occurrence in list
===================================

by Dave Bruns · Updated 1 May 2024

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[IF](https://exceljet.net/functions/if-function)

[LET](https://exceljet.net/functions/let-function)

[SCAN](https://exceljet.net/functions/scan-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7406/download?token=rL_RS2E9)
 (14.99 KB)

![Excel formula: Running count of occurrence in list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/running%20count%20of%20occurrence%20in%20list.png "Excel formula: Running count of occurrence in list")

Summary
-------

To create a running count for a specific value that appears in a range of cells, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 with an [expanding range](https://exceljet.net/glossary/expanding-reference)
. In the example shown, the formula in C5 is:

    =IF(B5=value,COUNTIF($B$5:B5,value),"")
    

where **value** is the [named range](https://exceljet.net/glossary/named-range)
 E5. The result is a running count of the 4 cells that contain "blue", since E5 contains "blue".

Generic formula
---------------

    =IF(A1=value,COUNTIF($A$1:A1,value),"")

Explanation 
------------

In this example, the goal is to create a running count for a specific value that appears in column B. The value to count is entered in cell E5, which is the [named range](https://exceljet.net/glossary/named-range)
 **value**. The core of the solution explained below is the [COUNTIF function](https://exceljet.net/functions/countif-function)
, with help from the [IF function](https://exceljet.net/functions/if-function)
 to suppress a count for other values.

### Basic count

Normally, the [COUNTIF function](https://exceljet.net/functions/countif-function)
 is given a _range_ and _criteria_ like this:

    COUNTIF(B5:B16,"blue") // returns 4
    

Since the range B5:B16 contains 4 cells that contain "blue", COUNTIF returns 4. The formula above works well when you want to _single_ count for one value in a range. However, to get a _running count_, we'll need to adapt the formula to use an _expanding range_.

### Running count with expanding range

An expanding range is a range with one side that is [absolute](https://exceljet.net/glossary/absolute-reference)
, and one side that is [relative](https://exceljet.net/glossary/relative-reference)
. In this case, we lock the first reference to B5, and leave the second reference relative like this:

    $B$5:B5 // expanding range
    

Notice that the left side of the range is locked ($B$5) and the right side is relative (B5). This is a special kind of "[mixed reference](https://exceljet.net/glossary/mixed-reference)
", since it contains both absolute and relative addresses. Because the first reference, $B$5, is locked, it doesn't change. However the second reference, B5, changes when the formula is copied. The result is an [expanding range](https://exceljet.net/glossary/expanding-reference)
. Dropping the expanding range back into the COUNTIF function, we have this formula:

    =COUNTIF($B$5:B5,"blue") // returns 1
    

As the formula is copied down column 1, the range "expands" at each row. You can see the result of the formula above in the screen below:

![Basic example of running count of "blue" values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/running%20count%20of%20occurrence%20in%20list%20simple%20example.png?itok=Xr2OoCMo "Basic example of running count of "blue" values")

Notice we get a count on _every_ row. However, the count only increments when another "blue" value is encountered.

### Removing extra counts

Because we only want to create a running count for one specific value, the next step is to remove the counts that appear next to other values. To do this, we nest the COUNTIF function inside the [IF function](https://exceljet.net/functions/if-function)
 like this:

    =IF(B5=value,COUNTIF($B$5:B5,value),"")
    

This is the formula entered in cell C5 of the example shown. Notice we have now swapped the hardcoded value "blue" with the named range **value** (E5). The named range is simply for convenience. It automatically acts like an absolute reference, and it makes the formula easier to read and write.

At each row, the logical test inside of IF tests the value in column B to see if it is equal to the named range **value** (E5), which contains "blue". If so, the COUNTIF formula explained above is executed, and returns the current running count for "blue". If the value in column B is not equal to "blue", the IF function returns an [empty string](https://exceljet.net/glossary/empty-string)
 (""). This effectively removes the count for all other values. The final result is a running count for cells that contain "blue".

### Other values

In the attached worksheet, the named range value (E5) is set up to provide a dropdown menu with [data validation](https://exceljet.net/glossary/data-validation)
. If we select a different value, the running count formula immediately returns a new set of running counts. The screen below shows the result of selecting "Green" in E5:

![Result of selecting a different value to count](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/running%20count%20of%20occurrence%20in%20list%20other%20value.png?itok=25jDGORU "Result of selecting a different value to count")

### SCAN solution

The [SCAN function](https://exceljet.net/functions/scan-function)
 is designed for problems like running totals and running sums. However, it is not obvious how to use SCAN in this case because it isn't clear how to suppress the running count on non-matching rows. If we set the accumulator to an empty string (""), SCAN will return errors when we increment the accumulator on matching rows. One interesting solution is to run a logical test first, then feed the result into SCAN like this:

    =LET(
    hits,B5:B16=value,
    counts,SCAN(0,hits,LAMBDA(a,v,a+v)),
    IF(hits,counts,"")
    )

In this formula, we use the [LET function](https://exceljet.net/functions/let-function)
 to define a variable called "hits" which is assigned a value based on the following expression:

    B5:B16=value

With _value_ equal to "Blue", this expression generates an array of 12 TRUE and FALSE values like this:

    {TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;FALSE}

We then define another variable called "counts", and assign a value by scanning _hits_ like this:

    SCAN(0,hits,LAMBDA(a,v,a+v))

The result is that SCAN generates a running count using the TRUE values in hits. The math operation of a+v causes Excel to convert the TRUE value to 1, which increments a by 1. FALSE values evaluate as zero and do not affect the count. The resulting array looks like this:

    {1;1;1;1;2;2;2;2;3;4;4;4}

The last step is to run counts through the [IF function](https://exceljet.net/functions/if-function)
 like this:

    IF(hits,counts,"")

Here, the IF function acts like a filter. The numbers in _counts_ associated with TRUE in hits pass through unaffected. The numbers associated with FALSE are replaced with empty strings. The array returned by IF looks like this:

    {1;"";"";"";2;"";"";"";3;4;"";""}

The final result is the same as with the original formula above.

### Running count for every value

To create a running count of every value that appears in column B, you can use a generic version of the formula like this:

    =COUNTIF($B$5:B5,B5)
    

As this formula is copied down the table, it returns the running count for every value in column B.

### Excel Tables

In an [Excel Table](https://exceljet.net/glossary/excel-table)
, formulas that use standard expanding references can become corrupted when rows are added or removed. You can work around this problem by using a [structured reference](https://exceljet.net/glossary/structured-reference)
 to create an expanding range like this:

    --(INDEX([Value],1):[@Value]=[@Value])
    

When entered in cell C5, this formula will return a running count for every value in every row. To return a running count for just one value as in the original example above, nest the formula inside IF like this:

    =IF(B5=value,SUM(--(INDEX([Value],1):[@Value]=[@Value])),"")
    

For more information, [see the example here](https://exceljet.net/formulas/running-total-in-table)
.

Related formulas
----------------

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

[![Excel formula: Calculate running total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate%20running%20total.png "Excel formula: Calculate running total")](https://exceljet.net/formulas/calculate-running-total)

### [Calculate running total](https://exceljet.net/formulas/calculate-running-total)

In this example, the goal is to calculate a running total in column D of the worksheet as shown. A running total, or cumulative sum, is a set of partial sums that changes as more data is collected. Each calculation represents the sum of values up to that point. In this example, each calculation...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel SCAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")](https://exceljet.net/functions/scan-function)

### [SCAN Function](https://exceljet.net/functions/scan-function)

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Calculate running total](https://exceljet.net/formulas/calculate-running-total)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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