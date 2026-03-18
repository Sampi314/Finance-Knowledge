# Count visible rows with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-visible-rows-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/count-visible-rows-with-criteria#main-content)

[](https://exceljet.net/formulas/count-visible-rows-with-criteria#)

*   [Previous](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list)
    
*   [Next](https://exceljet.net/formulas/countif-with-non-contiguous-range)
    

[Count](https://exceljet.net/formulas#Count)

Count visible rows with criteria
================================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[SUBTOTAL](https://exceljet.net/functions/subtotal-function)

[OFFSET](https://exceljet.net/functions/offset-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[INDEX](https://exceljet.net/functions/index-function)

![Excel formula: Count visible rows with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Count%20visible%20rows%20with%20criteria.png "Excel formula: Count visible rows with criteria")

Summary
-------

To count visible rows with criteria, you can use a rather complex formula based on three main functions: [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
, [SUBTOTAL](https://exceljet.net/functions/subtotal-function)
, and [OFFSET](https://exceljet.net/functions/offset-function)
. In the example shown, the formula in H7 is:

    =SUMPRODUCT((data=H4)*(SUBTOTAL(103,OFFSET(INDEX(data,1),ROW(data)-MIN(ROW(data)),0))))
    

Where **data** is the [named range](https://exceljet.net/glossary/named-range)
 C5:C16. The result is 4 since there are four visible rows where the Region is "West".

Generic formula
---------------

    =SUMPRODUCT((criteria)*(SUBTOTAL(103,OFFSET(range,rows,0,1))))

Explanation 
------------

In this example, the goal is to count visible rows where Region="West". Row 13 meets this criteria, but has been hidden. The [SUBTOTAL function](https://exceljet.net/functions/subtotal-function)
 can easily generate [sums](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)
 and [counts](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list)
 for visible rows. However, SUBTOTAL is not able to apply criteria like the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 without help. Conversely, COUNTIFS can easily apply criteria but is not able to distinguish between rows that are visible and rows that are hidden. One solution is to use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 to apply criteria, then use the SUBTOTAL function together with the OFFSET function to check visibility, and then tally up results with the SUMPRODUCT function. The details of this approach are described below.

### Overview

At the core, this formula works by setting up two [arrays](https://exceljet.net/glossary/array)
 inside SUMPRODUCT. The first array applies [criteria](https://exceljet.net/articles/how-to-use-formula-criteria)
, and the second array handles visibility:

    =SUMPRODUCT(criteria*visibility)
    

The formula in H7 takes this approach:

    =SUMPRODUCT((data=H4)*(SUBTOTAL(103,OFFSET(INDEX(data,1),ROW(data)-MIN(ROW(data)),0))))
    

### Criteria

The criteria are applied with this part of the formula:

    =(data=H4)
    

Because there are 12 values in **data** (C5:C16) this expression generates an [array](https://exceljet.net/glossary/array)
 with 12 TRUE and FALSE results like this:

    {FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE}
    

The TRUE values in this array indicate cells in **data** that contain "West". When this array is multiplied by the array returned by the SUBTOTAL function (described in detail below) the math operation coerces the TRUE and FALSE values to 1s and 0s, which creates this final array of results:

    {0;1;0;1;0;1;0;0;1;0;0;1}
    

This array is used to apply the criteria Region="West" in one of the last steps below.

### Visibility

To check visibility, we use an expression like this:

    (SUBTOTAL(103,OFFSET(INDEX(data,1),ROW(data)-MIN(ROW(data)),0)))
    

At a high level, we are using the [SUBTOTAL function](https://exceljet.net/functions/subtotal-function)
 with _function\_num_ set to 103, which causes SUBTOTAL to _count_ visible cells, ignoring cells that are hidden with a filter, or hidden manually. The reason the expression is complex is that we need an [_array_](https://exceljet.net/glossary/array)
 of results, not a single result. This means we need to feed cells into SUBTOTAL one at a time using the [OFFSET function](https://exceljet.net/functions/offset-function)
. To do this, we have configured OFFSET to create the references needed for _ref1_ inside SUBTOTAL like this:

    OFFSET(INDEX(data,1),ROW(data)-MIN(ROW(data)),0)
    

Working from the inside out, _reference_ is provided to OFFSET with the [INDEX function](https://exceljet.net/functions/index-function)
 like this:

    INDEX(data,1) // first cell in data
    

We are simply asking INDEX for the first cell in the [named range](https://exceljet.net/glossary/named-range)
 **data**, and INDEX (under the hood) returns C5 as a result:

    OFFSET(C5,ROW(data)-MIN(ROW(data)),0)
    

The _rows_ argument inside of OFFSET is created like this:

    =ROW(data)-MIN(ROW(data))
    ={5;6;7;8;9;10;11;12;13;14;15;16}-5
    ={0;1;2;3;4;5;6;7;8;9;10;11}
    

Essentially, we are using [this construction](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
 to create a zero-based index of offsets to give to the OFFSET function:

    OFFSET(C5,{0;1;2;3;4;5;6;7;8;9;10;11},0)
    

Using these 12 row offsets, the OFFSET function returns an array of 12 cell references like this:

    {C5;C6;C7;C8;C9;C10;C11;C12;C13;C14;C15;C16}
    

This array of references is returned to the SUBTOTAL function as the _ref1_ argument:

    (SUBTOTAL(103,{C5;C6;C7;C8;C9;C10;C11;C12;C13;C14;C15;C16}))
    

With _function\_num_ set to 103, SUBTOTAL returns the count of visible cells in each reference. Because each reference is provided separately, we get back an array with 12 counts like this:

    {1;1;1;1;1;1;1;1;0;1;1;1}
    

Since we are feeding the references to SUBTOTAL one at a time, the only possible values are 1 and 0, which is exactly what we need when we multiply this array by the array we created for the criteria below. To recap, the complexity above is needed to get to _12 results_ instead of the _single_ result SUBTOTAL would give us if we provided a simple range.

### Adding up results

Finally, we are ready to add up the results. For this, we use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. Both arrays explained above are delivered to SUMPRODUCT like this:

    =SUMPRODUCT({0;1;0;1;0;1;0;0;1;0;0;1}*{1;1;1;1;1;1;1;1;0;1;1;1})
    

After the two arrays are multiplied, we have:

    =SUMPRODUCT({0;1;0;1;0;1;0;0;0;0;0;1}) // returns 4
    

In the final step, SUMPRODUCT sums the array and returns 4 as a final result.

### Multiple criteria

You can extend the formula to handle multiple criteria like this:

    =SUMPRODUCT((criteria1)*(criteria2)*(SUBTOTAL(103,OFFSET(ref,rows,0,1))))
    

### Summing results

To return a sum of visible values (instead of a count), you can adapt the formula to include a range of cells to sum like this:

    =SUMPRODUCT(criteria*visibility*sumrange)
    

The sum range is the range that contains values you want to sum. The criteria and visibility arrays work the same as explained above, excluding cells that are not visible. If you need partial matching, you can construct an expression using ISNUMBER + SEARCH, [as explained here](https://exceljet.net/formulas/cell-contains-specific-text)
, to create the criteria array.

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

[![Excel SUBTOTAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20subtotal%20function.png "Excel SUBTOTAL function")](https://exceljet.net/functions/subtotal-function)

### [SUBTOTAL Function](https://exceljet.net/functions/subtotal-function)

The Excel SUBTOTAL function is designed to run a given calculation on a range of cells while ignoring cells that should not be included. SUBTOTAL can return a SUM, AVERAGE, COUNT, MAX, and others (see complete list below), and SUBTOTAL function can either include or exclude values in hidden...

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

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

*   [SUBTOTAL Function](https://exceljet.net/functions/subtotal-function)
    
*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

### Links

*   [MrExcel discussion, with Mike Girvin and Aladin Akyurek](http://www.mrexcel.com/forum/excel-questions/56984-countif-visible-cells-filter-mode.html)
    
*   [Mike Girvin's Magic Trick 1010](https://www.youtube.com/watch?v=1W2Y-29TzGw)
    

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