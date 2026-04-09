# Last row in numeric data - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/last-row-in-numeric-data

---

[Skip to main content](https://exceljet.net/formulas/last-row-in-numeric-data#main-content)

[](https://exceljet.net/formulas/last-row-in-numeric-data#)

*   [Previous](https://exceljet.net/formulas/last-row-in-mixed-data-with-no-blanks)
    
*   [Next](https://exceljet.net/formulas/last-row-in-text-data)
    

[Range](https://exceljet.net/formulas#Range)

Last row in numeric data
========================

by Dave Bruns · Updated 31 Oct 2023

Related functions 
------------------

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Last row in numeric data](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Last%20row%20in%20numeric%20data.png "Excel formula: Last row in numeric data")

Summary
-------

To get the last relative position (i.e. last row, last column) for numeric data (with or without empty cells), you can use the MATCH function with a so-called "[big number](https://exceljet.net/glossary/bignum)
". In the example shown, the formula in E5 is:

    =MATCH(9.99E+307,B4:B9)
    

Generic formula
---------------

    =MATCH(bignum,range)

Explanation 
------------

When building advanced formulas that use dynamic ranges, it's often necessary to figure out the last location of data in a list. Depending on the data, this could be the last row with data, the last column with data, or the intersection of both. Note: we want the last \*relative position\* _inside a given range_, not the row number on the worksheet. The screen below shows the idea:

![Illustration of last relative position (last row, last column)](https://exceljet.net/sites/default/files/images/formulas/inline/relative%20position%20in%20range.png "Illustration of last relative position (last row, last column)")

This formula uses the MATCH function in approximate match mode to locate the last numeric value in a range. Approximate match enabled by setting by the 3rd argument in MATCH to 1, or omitting this argument, which defaults to 1.

The lookup value is a so-called "big number" (sometimes abbreviated "bignum") which is intentionally larger than any value that will appear in the range.

The result is that MATCH will "step back" to the last numeric value in the range, and return that position.

_Note: this approach works fine with empty cells in the range, but is not reliable with mixed data that includes both numbers and text._

### About bignum

The biggest number Excel can handle is 9.99999999999999E+307.

When using MATCH this way, you can use any large number that is guaranteed to be larger than any value in the range, for example:

    =MATCH(1E+06,range) // 1 million
    =MATCH(1E+09,range) // 1 billion
    =MATCH(1E+12,range) // 1 trillion
    

The advantage to using 9.99E+307 or similar, is that it's (1) a huge number and (2) recognizable as a placeholder for a "big number". You'll see it used in various advanced Excel formulas.

### Dynamic range

You can use this formula to create a dynamic range with other functions like INDEX and OFFSET. See links below for examples and explanation:

*   [Dynamic range with INDEX and COUNTA](https://exceljet.net/formulas/dynamic-named-range-with-index)
    
*   [Dynamic range with OFFSET and COUNTA](https://exceljet.net/formulas/dynamic-named-range-with-offset)
    

_Inspiration for this article came from [Mike Girvin's](https://www.youtube.com/user/excelisfun)
 excellent book [Control + Shift + Enter](http://www.amazon.com/gp/product/1615470077/?tag=exceljet-20)
, where Mike explains the concept of "last relative position"._

Related formulas
----------------

[![Excel formula: Last row in mixed data with no blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Last%20row%20in%20mixed%20data%20no%20blanks.png "Excel formula: Last row in mixed data with no blanks")](https://exceljet.net/formulas/last-row-in-mixed-data-with-no-blanks)

### [Last row in mixed data with no blanks](https://exceljet.net/formulas/last-row-in-mixed-data-with-no-blanks)

This formula uses the COUNTA function to count values in a range. COUNTA counts both numbers and text to so works well with mixed data. The range B4:B8 contains 5 values, so COUNTA returns 5. The number 5 corresponds to the last row (last relative position) of data in the range B4:B100. Note: This...

[![Excel formula: Last row in mixed data with blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20row%20in%20mixed%20data%20with%20blanks.png "Excel formula: Last row in mixed data with blanks")](https://exceljet.net/formulas/last-row-in-mixed-data-with-blanks)

### [Last row in mixed data with blanks](https://exceljet.net/formulas/last-row-in-mixed-data-with-blanks)

When constructing more advanced formulas, it's often necessary to figure out the last location of data in a list. Depending on the data, this could be the last row with data, the last column with data, or the intersection of both. We want the last \*relative position\* inside a given range not the...

[![Excel formula: Dynamic named range with OFFSET](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20named%20range%20with%20offset.png "Excel formula: Dynamic named range with OFFSET")](https://exceljet.net/formulas/dynamic-named-range-with-offset)

### [Dynamic named range with OFFSET](https://exceljet.net/formulas/dynamic-named-range-with-offset)

Dynamic ranges are also known as expanding ranges because they automatically expand and contract to accommodate new or deleted data. You can see a video demo of this approach here . This formula uses the OFFSET function to generate a range that expands and contracts by adjusting height and width...

[![Excel formula: Dynamic named range with INDEX](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20named%20range%20with%20index1.png "Excel formula: Dynamic named range with INDEX")](https://exceljet.net/formulas/dynamic-named-range-with-index)

### [Dynamic named range with INDEX](https://exceljet.net/formulas/dynamic-named-range-with-index)

This page shows an example of a dynamic named range created with the INDEX function together with the COUNTA function. Dynamic named ranges automatically expand and contract when data is added or removed. They are an alternative to using an Excel Table , which also resizes as data is added or...

Related functions
-----------------

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Last row in mixed data with no blanks](https://exceljet.net/formulas/last-row-in-mixed-data-with-no-blanks)
    
*   [Last row in mixed data with blanks](https://exceljet.net/formulas/last-row-in-mixed-data-with-blanks)
    
*   [Dynamic named range with OFFSET](https://exceljet.net/formulas/dynamic-named-range-with-offset)
    
*   [Dynamic named range with INDEX](https://exceljet.net/formulas/dynamic-named-range-with-index)
    

### Functions

*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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