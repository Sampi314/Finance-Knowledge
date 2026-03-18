# Last row in mixed data with blanks - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/last-row-in-mixed-data-with-blanks

---

[Skip to main content](https://exceljet.net/formulas/last-row-in-mixed-data-with-blanks#main-content)

[](https://exceljet.net/formulas/last-row-in-mixed-data-with-blanks#)

*   [Previous](https://exceljet.net/formulas/last-n-rows)
    
*   [Next](https://exceljet.net/formulas/last-row-in-mixed-data-with-no-blanks)
    

[Range](https://exceljet.net/formulas#Range)

Last row in mixed data with blanks
==================================

by Dave Bruns · Updated 31 Oct 2023

Related functions 
------------------

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Last row in mixed data with blanks](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/last%20row%20in%20mixed%20data%20with%20blanks.png "Excel formula: Last row in mixed data with blanks")

Summary
-------

To get the last relative position (i.e. last row, last column) for mixed data that may contain empty cells, you can use the MATCH function as described below. In the example shown, the formula in E5 is:

    {=MATCH(2,1/(B4:B10<>""))}
    

_Note: this is an array formula and must be entered with Control+Shift+Enter._

Generic formula
---------------

    {=MATCH(2,1/(range<>""))}

Explanation 
------------

When constructing more advanced formulas, it's often necessary to figure out the last location of data in a list. Depending on the data, this could be the last row with data, the last column with data, or the intersection of both. We want the last \*relative position\* _inside a given range_ not the row number on the worksheet:

![Illustration of last relative position (last row, last column)](https://exceljet.net/sites/default/files/images/formulas/inline/relative%20position%20in%20range.png "Illustration of last relative position (last row, last column)")

This formula uses the MATCH function configured to find the position of the last non-empty cell in a range. Working from the inside out, the lookup array inside MATCH is constructed like this:

    =1/(B4:B10<>""))
    =1/{TRUE;FALSE;TRUE;FALSE;TRUE;TRUE;FALSE}
    ={1;#DIV/0!;1;#DIV/0!;1;1;#DIV/0!}
    

_Note: all values in the array are either 1 or the #DIV/0! error._

MATCH is then set to match the value 2 in "approximate match mode", by omitting the 3rd argument is omitted.

Because the lookup value of 2 will never be found, MATCH will always find the last 1 in the lookup array, which corresponds to the last non-empty cell.

This approach will work with any kind of data, including numbers, text, dates, etc. It also works with null text strings that are returned by formulas like this:

    =IF(A1<100,"")
    

### Dynamic range

You can use this formula to create a dynamic range with other functions like INDEX and OFFSET. See the links below for examples:

*   [Dynamic range with INDEX and COUNTA](https://exceljet.net/formulas/dynamic-named-range-with-index)
    
*   [Dynamic range with OFFSET and COUNTA](https://exceljet.net/formulas/dynamic-named-range-with-offset)
    

_Inspiration for this article came from [Mike Girvin's](https://www.youtube.com/user/excelisfun)
 excellent book [Control + Shift + Enter](http://www.amazon.com/gp/product/1615470077/?tag=exceljet-20)
, where Mike does a great job explaining the concept of "last relative position"._

Related formulas
----------------

[![Excel formula: Last row in mixed data with no blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Last%20row%20in%20mixed%20data%20no%20blanks.png "Excel formula: Last row in mixed data with no blanks")](https://exceljet.net/formulas/last-row-in-mixed-data-with-no-blanks)

### [Last row in mixed data with no blanks](https://exceljet.net/formulas/last-row-in-mixed-data-with-no-blanks)

This formula uses the COUNTA function to count values in a range. COUNTA counts both numbers and text to so works well with mixed data. The range B4:B8 contains 5 values, so COUNTA returns 5. The number 5 corresponds to the last row (last relative position) of data in the range B4:B100. Note: This...

[![Excel formula: Last row in numeric data](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Last%20row%20in%20numeric%20data.png "Excel formula: Last row in numeric data")](https://exceljet.net/formulas/last-row-in-numeric-data)

### [Last row in numeric data](https://exceljet.net/formulas/last-row-in-numeric-data)

When building advanced formulas that use dynamic ranges, it's often necessary to figure out the last location of data in a list. Depending on the data, this could be the last row with data, the last column with data, or the intersection of both. Note: we want the last \*relative position\* inside a...

[![Excel formula: Last row in text data](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Last%20row%20in%20text%20data.png "Excel formula: Last row in text data")](https://exceljet.net/formulas/last-row-in-text-data)

### [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)

This formula uses the MATCH function in approximate match mode to locate the last text value in a range. Approximate match enabled by setting by the 3rd argument in MATCH to 1, or omitting this argument, which defaults to 1. The lookup value is a so-called "big text" (sometimes abbreviated "bigtext...

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
    
*   [Last row in numeric data](https://exceljet.net/formulas/last-row-in-numeric-data)
    
*   [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)
    
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