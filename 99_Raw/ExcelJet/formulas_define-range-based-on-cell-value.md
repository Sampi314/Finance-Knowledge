# Define range based on cell value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/define-range-based-on-cell-value

---

[Skip to main content](https://exceljet.net/formulas/define-range-based-on-cell-value#main-content)

[](https://exceljet.net/formulas/define-range-based-on-cell-value#)

*   [Previous](https://exceljet.net/formulas/countifs-with-variable-range)
    
*   [Next](https://exceljet.net/formulas/dynamic-named-range-with-index)
    

[Range](https://exceljet.net/formulas#Range)

Define range based on cell value
================================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[OFFSET](https://exceljet.net/functions/offset-function)

![Excel formula: Define range based on cell value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Define%20range%20based%20on%20cell%20value.png "Excel formula: Define range based on cell value")

Summary
-------

To define a range based on a value in another cell, you can use the [INDEX function](https://exceljet.net/functions/index-function)
. In the example shown, the formula in J7 is:

    =SUM(C5:INDEX(data,J5,J6))
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 C5:G9.

Generic formula
---------------

    =SUM(firstcell:INDEX(data,rows,cols))

Explanation 
------------

This formula relies on a specific behavior of INDEX — although it seems that INDEX returns the _value_ at a particular location, it actually returns a _reference_ to the location. In most formulas, you wouldn't notice the difference – Excel simply evaluates the reference and returns the value. This formula uses this feature to construct a dynamic range based on worksheet input.

Inside the sum function, the first reference is simply the first cell in the range that covers all possible cells:

    =SUM(C5:
    

To get the last cell, we use INDEX. Here, we give INDEX the [named range](https://exceljet.net/glossary/named-range)
 "data", which is the maximum possible range of values, and also the values from J5 (rows) and J6 (columns). INDEX doesn't return a range, it only returns a single cell at that location, E9 in the example:

    INDEX(data,J5,J6) // returns E9
    

The original formula is reduced to:

    =SUM(C5:E9)
    

which returns 300, the sum of all values in C5:E9.

The formula in J8 is almost the same but uses [AVERAGE](https://exceljet.net/functions/average-function)
 instead of [SUM](https://exceljet.net/functions/sum-function)
 to calculate an average. When a user changes values in J5 or J6 the range is updated, and new results are returned.

### Alternative with OFFSET

You can build a similar formula with the [OFFSET function](https://exceljet.net/functions/offset-function)
, shown below:

    =SUM(OFFSET(C5,0,0,J5,J6)) // sum
    =AVERAGE(OFFSET(C5,0,0,J5,J6)) // average
    

OFFSET is designed to return a range, so the formulas are perhaps simpler to understand. However, OFFSET is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and can cause performance problems when used in larger, more complex worksheets.

Related formulas
----------------

[![Excel formula: Dynamic named range with INDEX](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20named%20range%20with%20index1.png "Excel formula: Dynamic named range with INDEX")](https://exceljet.net/formulas/dynamic-named-range-with-index)

### [Dynamic named range with INDEX](https://exceljet.net/formulas/dynamic-named-range-with-index)

This page shows an example of a dynamic named range created with the INDEX function together with the COUNTA function. Dynamic named ranges automatically expand and contract when data is added or removed. They are an alternative to using an Excel Table , which also resizes as data is added or...

[![Excel formula: Dynamic named range with OFFSET](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20named%20range%20with%20offset.png "Excel formula: Dynamic named range with OFFSET")](https://exceljet.net/formulas/dynamic-named-range-with-offset)

### [Dynamic named range with OFFSET](https://exceljet.net/formulas/dynamic-named-range-with-offset)

Dynamic ranges are also known as expanding ranges because they automatically expand and contract to accommodate new or deleted data. You can see a video demo of this approach here . This formula uses the OFFSET function to generate a range that expands and contracts by adjusting height and width...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

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

*   [Dynamic named range with INDEX](https://exceljet.net/formulas/dynamic-named-range-with-index)
    
*   [Dynamic named range with OFFSET](https://exceljet.net/formulas/dynamic-named-range-with-offset)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
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