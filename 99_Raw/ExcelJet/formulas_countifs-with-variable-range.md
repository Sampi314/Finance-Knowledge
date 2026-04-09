# COUNTIFS with variable range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/countifs-with-variable-range

---

[Skip to main content](https://exceljet.net/formulas/countifs-with-variable-range#main-content)

[](https://exceljet.net/formulas/countifs-with-variable-range#)

*   [Previous](https://exceljet.net/formulas/count-visible-columns)
    
*   [Next](https://exceljet.net/formulas/define-range-based-on-cell-value)
    

[Range](https://exceljet.net/formulas#Range)

COUNTIFS with variable range
============================

by Dave Bruns · Updated 2 Aug 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[OFFSET](https://exceljet.net/functions/offset-function)

[ADDRESS](https://exceljet.net/functions/address-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

[ROW](https://exceljet.net/functions/row-function)

![Excel formula: COUNTIFS with variable range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/countifs%20with%20a%20variable%20range.png "Excel formula: COUNTIFS with variable range")

Summary
-------

To configure [COUNTIFS](https://exceljet.net/functions/countifs-function)
 (or [COUNTIF](https://exceljet.net/functions/countif-function)
) with a variable range, you can use the [OFFSET function](https://exceljet.net/functions/offset-function)
. In the example shown, the formula in B11 is:

    =COUNTIFS(OFFSET(B$5,0,0,ROW()-ROW(B$5)-1,1),"<>")
    

This formula counts non-blank cells in a range that begins at B5 and ends 2 rows above the cell where the formula lives. The same formula is copied and pasted 2 rows below the last entry in the data as shown.

Explanation 
------------

In the example shown, the formula in B11 is:

    =COUNTIFS(OFFSET(B$5,0,0,ROW()-ROW(B$5)-1,1),"<>")
    

Working from the inside out, the work of setting up a variable range is done by the OFFSET function here:

    OFFSET(B$5,0,0,ROW()-ROW(B$5)-1,1) // variable range
    

OFFSET has five arguments and is configured like this:

*   _reference_ = B$5, begin at cell B5, row locked
*   _rows_ = 0, offset zero rows from starting cell
*   _cols_ = 0, offset zero columns starting cell
*   _height_ = ROW()-ROW(B$5)-1 = 5 rows high
*   _width_ = 1 column wide

To work out the height of the range in rows, we use the [ROW function](https://exceljet.net/functions/row-function)
 like this:

    ROW()-ROW(B$5)-1 // work out height
    

Since ROW() returns the row number of the "current" cell (i.e. the cell the formula lives in), we can simplify like this:

    =ROW()-ROW(B$5)-1
    =11-5-1
    =5
    

With the above configuration, OFFSET returns the range B5:B9 directly to COUNTIFS:

    =COUNTIFS(B5:B9,"<>") // returns 4
    

Notice the reference to B$5 in the above formula is a [mixed reference](https://exceljet.net/glossary/mixed-reference)
, with the column relative and the row locked. This allows the formula to be copied to another column and still work. For example, once copied to C12, the formula is:

    =COUNTIFS(OFFSET(C$5,0,0,ROW()-ROW(C$5)-1,1),"<>")
    

_Note: OFFSET is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and can cause performance problems in large or complex worksheets._

### With INDIRECT and ADDRESS

Another approach is to use a formula based on the [INDIRECT](https://exceljet.net/functions/indirect-function)
 and [ADDRESS](https://exceljet.net/functions/address-function)
 functions. In this case, we assemble a range as text, then use INDIRECT to evaluate the text as a reference. The formula in B11 would be:

    =COUNTIFS(INDIRECT(ADDRESS(5,COLUMN())&":"&ADDRESS(ROW()-2,COLUMN())),"<>")
    

The ADDRESS function is used to construct a range like this:

    ADDRESS(5,COLUMN())&":"&ADDRESS(ROW()-2,COLUMN())
    

In the first instance of ADDRESS, we supply _row\_number_ as the hardcoded value 5, and provide the _column\_number_ with the [COLUMN function](https://exceljet.net/functions/column-function)
:

    =ADDRESS(5,COLUMN()) // returns "$B$5"
    

In the second instance, we supply the "current" _row\_number_ minus 2, and the current _column_ with the COLUMN function:

    =ADDRESS(ROW()-2,COLUMN()) // returns "$B$9"
    

After [concatenating](https://exceljet.net/glossary/concatenation)
 these two values together, we have:

    "$B$5:$B$9" // as text
    

Note this is a _text string_. To convert to a valid reference, we need to use INDIRECT:

    =INDIRECT("$B$5:$B$9") // returns $B$5:$B$9 as valid range
    

Finally, the formula in B11 becomes:

    =COUNTIFS($B$5:$B$9,"<>") // returns 4
    

_Note: INDIRECT is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and can cause performance problems in large or complex worksheets._

Related formulas
----------------

[![Excel formula: Average last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_n_rows.png "Excel formula: Average last n rows")](https://exceljet.net/formulas/average-last-n-rows)

### [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)

In the worksheet shown, we have a list of values in column C. The goal is to dynamically average the last n values using the numbers in cell E5 for n . Since the list may grow over time, the key requirement is to average amounts by position. For convenience only, the values to average are in the...

[![Excel formula: Address of last cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20last%20cell%20in%20range.png "Excel formula: Address of last cell in range")](https://exceljet.net/formulas/address-of-last-cell-in-range)

### [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)

The ADDRESS function creates a reference based on a given a row and column number. In this case, we want to get the last row and the last column used by the named range data (B5:D14). To get the last row used, we use the ROW function together with the MAX function like this: MAX(ROW(data)) Because...

[![Excel formula: Dynamic named range with OFFSET](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20named%20range%20with%20offset.png "Excel formula: Dynamic named range with OFFSET")](https://exceljet.net/formulas/dynamic-named-range-with-offset)

### [Dynamic named range with OFFSET](https://exceljet.net/formulas/dynamic-named-range-with-offset)

Dynamic ranges are also known as expanding ranges because they automatically expand and contract to accommodate new or deleted data. You can see a video demo of this approach here . This formula uses the OFFSET function to generate a range that expands and contracts by adjusting height and width...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

[![Excel ADDRESS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20address%20function.png "Excel ADDRESS function")](https://exceljet.net/functions/address-function)

### [ADDRESS Function](https://exceljet.net/functions/address-function)

The Excel ADDRESS function returns the address for a cell based on a given row and column number. For example, =ADDRESS(1,1) returns $A$1. ADDRESS can return an address in relative, mixed, or absolute format, and can be used to construct a cell reference inside a formula.

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIFS%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countifs-function)

### [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)

In this video, we'll look at how to use the COUNTIFS function to count cells that meet multiple criteria. Let's take a look. In this first set of tables, we have two named ranges , "number" and "color." In column G, I'll enter a formula that satisfies the conditions in column E. The COUNTIFS...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)
    
*   [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)
    
*   [Dynamic named range with OFFSET](https://exceljet.net/formulas/dynamic-named-range-with-offset)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    
*   [ADDRESS Function](https://exceljet.net/functions/address-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    

### Videos

*   [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)
    

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