# Dynamic named range with OFFSET - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-named-range-with-offset

---

[Skip to main content](https://exceljet.net/formulas/dynamic-named-range-with-offset#main-content)

[](https://exceljet.net/formulas/dynamic-named-range-with-offset#)

*   [Previous](https://exceljet.net/formulas/dynamic-named-range-with-index)
    
*   [Next](https://exceljet.net/formulas/dynamic-range-between-two-matches)
    

[Range](https://exceljet.net/formulas#Range)

Dynamic named range with OFFSET
===============================

by Dave Bruns · Updated 6 Feb 2025

Related functions 
------------------

[OFFSET](https://exceljet.net/functions/offset-function)

[COUNTA](https://exceljet.net/functions/counta-function)

[TRIMRANGE](https://exceljet.net/functions/trimrange-function)

![Excel formula: Dynamic named range with OFFSET](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/dynamic%20named%20range%20with%20offset.png "Excel formula: Dynamic named range with OFFSET")

Summary
-------

One way to create a dynamic [named range](https://exceljet.net/articles/named-ranges)
 with a formula is to use the OFFSET function together with the COUNTA function. In the example shown, the formula below is used to create a dynamic named to encompass the data in B5:G10:

    =OFFSET(B5,0,0,COUNTA($B$5:$B$100),COUNTA($B$4:$Z$4))

> Note: this formula is meant to define a [named range](https://exceljet.net/articles/named-ranges)
>  that can be used in other formulas. This range will be dynamic and expand and shrink with the data. An alternative to a formula-based dynamic named range is to use an [Excel Table](https://exceljet.net/articles/excel-tables)
> . If you are using Excel 365 another option is to use the [TRIMRANGE function](https://exceljet.net/functions/trimrange-function)
> , which is designed to create dynamic ranges.

_Note: OFFSET is a_ [_volatile function_](https://exceljet.net/glossary/volatile-function)
 _that can cause performance problems when used on large datasets or in more complicated workbooks. If you have trouble, consider building a dynamic named range with the INDEX function instead._

Generic formula
---------------

    =OFFSET(origin,0,0,COUNTA(range),COUNTA(range))

Explanation 
------------

Dynamic ranges are also known as expanding ranges because they automatically expand and contract to accommodate new or deleted data. You can see a [video demo of this approach here](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-offset)
. This formula uses the OFFSET function to generate a range that expands and contracts by adjusting height and width based on a count of non-empty cells:

    =OFFSET(B5,0,0,COUNTA($B$5:$B$100),COUNTA($B$4:$Z$4))
    

The first argument in OFFSET represents the first cell in the data (the origin), which in this case is cell B5. The next two arguments are offsets for rows and columns and are supplied as zero.

The last two arguments represent height and width. Height and width are generated on the fly by using COUNTA, which makes the resulting reference dynamic.

For height, we use the COUNTA function to count non-empty values in the range B5:B100. This assumes no blank values in the data, and no values beyond B100. COUNTA returns 6.

For width, we use the COUNTA function to count non-empty values in the range B5:Z5. This assumes no header cells, and no headers beyond Z5. COUNTA returns 6.

At this point, the formula looks like this:

    =OFFSET(B5,0,0,6,6)
    

With this information, OFFSET returns a reference to B5:G10, which corresponds to a range 6 rows height by 6 columns across.

_Note: The ranges used for height and width should be adjusted to match the worksheet layout._

### Variation with full column/row references

You can also use full column and row references for height and width like so:

    =OFFSET($B$5,0,0,COUNTA($B:$B)-2,COUNTA($4:$4))
    

Note that height is being adjusted with -2 to take into account header and title values in cells B4 and B2. The advantage of this approach is the simplicity of the ranges inside COUNTA. The disadvantage comes from the huge size full columns and rows — care must be taken to prevent errant values outside the range, as they can easily throw off the count.

### Determining the last row

There are several ways to determine the last row (last relative position) in a set of data, depending on the structure and content of the data in the worksheet:

*   [Last row in mixed data with blanks](https://exceljet.net/formulas/last-row-in-mixed-data-with-blanks)
    
*   [Last row in mixed data with no blanks](https://exceljet.net/formulas/last-row-in-mixed-data-with-no-blanks)
    
*   [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)
    
*   [Last row in numeric data](https://exceljet.net/formulas/last-row-in-numeric-data)
    

Related formulas
----------------

[![Excel formula: Dynamic named range with INDEX](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20named%20range%20with%20index1.png "Excel formula: Dynamic named range with INDEX")](https://exceljet.net/formulas/dynamic-named-range-with-index)

### [Dynamic named range with INDEX](https://exceljet.net/formulas/dynamic-named-range-with-index)

This page shows an example of a dynamic named range created with the INDEX function together with the COUNTA function. Dynamic named ranges automatically expand and contract when data is added or removed. They are an alternative to using an Excel Table , which also resizes as data is added or...

Related functions
-----------------

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel TRIMRANGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_trimrange_function.png "Excel TRIMRANGE function")](https://exceljet.net/functions/trimrange-function)

### [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)

The Excel TRIMRANGE function removes empty rows and columns from the outer edges of a range of data. The result is a "trimmed" range that only includes data from the used portion of the range. Because it is a formula, TRIMRANGE will update the range dynamically when data is added or removed...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20dynamic%20named%20range%20with%20OFFSET-thumb.png)](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-offset)

### [How to create a dynamic named range with OFFSET](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-offset)

In this video we're going to look at how to create a dynamic named range using the OFFSET function . To create a dynamic named range that refers to this data using the OFFSET function, first identify the first cell of the data in the upper left. In this case, that's cell B6. To create a named range...

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
    

### Functions

*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)
    

### Videos

*   [How to create a dynamic named range with OFFSET](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-offset)
    

### Articles

*   [Named Ranges in Excel](https://exceljet.net/articles/named-ranges)
    

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