# All cells in range are blank - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/all-cells-in-range-are-blank

---

[Skip to main content](https://exceljet.net/formulas/all-cells-in-range-are-blank#main-content)

[](https://exceljet.net/formulas/all-cells-in-range-are-blank#)

*   [Previous](https://exceljet.net/formulas/address-of-last-cell-in-range)
    
*   [Next](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)
    

[Range](https://exceljet.net/formulas#Range)

All cells in range are blank
============================

by Dave Bruns · Updated 2 Oct 2023

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: All cells in range are blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/all_cells_in_range_are_blank.png "Excel formula: All cells in range are blank")

Summary
-------

To test if all cells in a range are empty, you can use a formula based on the [COUNTA](https://exceljet.net/functions/counta-function)
 or [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 functions. In the example shown, the formula in I5 is:

    =COUNTA(C5:G5)=0
    

As the formula is copied down, it returns TRUE when all cells between columns C and G are empty, and FALSE if not.

_Note: COUNTA will count both numbers and text values in a cell. It will also count formulas that return an empty string (""), which will cause problems if you want to treat such cells as empty. See below for an alternative formula._

Generic formula
---------------

    =COUNTA(range)=0

Explanation 
------------

When working with Excel, there are times when you need to determine if a range of cells is empty. This can be useful in various scenarios, such as data validation, error checking, or report preparation. In this article, we'll explore a couple of formulas that can help you check if all cells in a given range are empty. The first and simplest formula is based on the COUNTA function, which will count numbers and text values in cells. The second formula is based on the SUMPRODUCT with the LEN function. This option is useful when you need to treat formulas that return empty strings ("") as empty.

> **Blank vs. Empty Cells** - In Excel, there is a distinction between blank and empty cells. A cell can visually appear blank but might contain a formula that returns an empty string (""). Such cells are technically not empty, as they contain a formula. If you need to treat formulas that return "" as empty, see the SUMPRODUCT option below.

### COUNTA option

The simplest way to test if a range is empty is to use the COUNTA function. The [COUNTA function](https://exceljet.net/functions/counta-function)
 is designed to count the number of cells in a range that are not empty. It considers any cell with content, including text, numbers, errors, and formulas, as _non-empty_. In the worksheet shown, we use COUNTA to test if all cells in a range are empty with a formula like this in cell I5:

    =COUNTA(C5:G5)=0

If the count is zero, the formula will return TRUE. If the count is any other number, the formula will return FALSE. In other words, the result will be TRUE _only when all cells in C5:G5 are empty_.

The screen below shows how you can apply the formula above inside the [IF function](https://exceljet.net/functions/if-function)
. The idea here is clearly mark rows where all 5 cells are blank. The formula in cell I5 is:

    =IF(COUNTA(C5:G5)=0,"*","")

![Combining the formula with the IF function](https://exceljet.net/sites/default/files/images/formulas/inline/all_cells_in_range_are_blank_applied.png "Combining the formula with the IF function")

_Note: COUNTA counts the number of cells in a range that are not empty. However, it won't work correctly for cells that contain formulas resulting in empty strings (""). Such cells will be considered non-empty by the COUNTA function even though they visually appear blank. If you need to treat formulas that return "" as empty, see the SUMPRODUCT options below._

### SUMPRODUCT option

Another way to test for an empty range is to use the SUMPRODUCT with LEN  like this:

    =SUMPRODUCT(LEN(range))=0

The [LEN function](https://exceljet.net/functions/len-function)
 calculates the length of the content in each cell in a given and returns the length as a number. The [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 then returns the sum of all lengths. If the combined length is zero, the formula will return TRUE. Otherwise, the formula will return FALSE.

This is a more robust solution to the empty vs. blank dilemma. If a cell is truly empty, its length will be zero, and LEN will return zero. If a cell contains a formula that results in an empty string, it is technically not empty, but LEN will still return zero since an empty string ("") has no length. In other words, LEN will treat formulas that return ="" the same as truly empty cells. In cell I5, the formula evaluates like this:

    =SUMPRODUCT(LEN(C5:G5))=0
    =SUMPRODUCT({2,2,2,0,2})=0
    =8=0
    =FALSE

In cell I10, the formula evaluates like this:

    =SUMPRODUCT(LEN(C10:G10))=0
    =SUMPRODUCT({0,0,0,0,0})=0
    =0=0
    =TRUE

**Alternative Formula**: Another approach using SUMPRODUCT is to directly check if the cells are not equal to an empty string:

    =SUMPRODUCT(--(range<>""))=0

This formula is a bit more literal because it uses the "not equals to" [operator](https://exceljet.net/glossary/logical-operators)
 (<>). The expression <>"" means "no equal to nothing" or, more concisely, "not empty". In cell I5, the formula evaluates like this:

    =SUMPRODUCT(--(C5:G5<>""))=0
    =SUMPRODUCT(--({TRUE,TRUE,TRUE,FALSE,TRUE}))=0
    =SUMPRODUCT({1,1,1,0,1})=0
    =4=0
    =FALSE

Notice in the second line above the expression _C5:G5<>""_ returns an [array](https://exceljet.net/glossary/array)
 of five values, one for each cell in the range, where TRUE means _not empty_, and FALSE means _empty_. The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is then used to convert the TRUE and FALSE values to 1s and 0s and SUMPRODUCT returns a sum. Only when the sum is zero will the formula return TRUE, as in cell I10, where the formula evaluates like this:

    =SUMPRODUCT(--(C10:G10<>""))=0
    =SUMPRODUCT(--({FALSE,FALSE,FALSE,FALSE,FALSE}))=0
    =SUMPRODUCT({0,0,0,0,0})=0
    =0=0
    =TRUE

### Conclusion

There are different ways in Excel to check if all cells in a range are empty, but it's important to understand the difference between blank and empty cells. If you are checking a range that does not contain formulas, the COUNTA function will work fine. If however, you are checking a range that does contain formulas, the SUMPRODUCT options above are more robust.

Related formulas
----------------

[![Excel formula: Row is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/row_is_blank.png "Excel formula: Row is blank")](https://exceljet.net/formulas/row-is-blank)

### [Row is blank](https://exceljet.net/formulas/row-is-blank)

The goal is to use a formula to check if all cells in a row are blank or empty and return TRUE or FALSE. One way to solve this problem is with the SUMPRODUCT function, as seen in the worksheet above. Another approach is to use the newer BYROW function. Both methods are described below. SUMPRODUCT...

[![Excel formula: All values in a range are at least](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/All%20values%20in%20a%20range%20are%20at%20least.png "Excel formula: All values in a range are at least")](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)

### [All values in a range are at least](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)

At the core, this formula uses the COUNTIF function to count any cells that fall below a given value, which is hardcoded as 65 in the formula: COUNTIF(B5:F5,"<65") In this part of the formula, COUNTIF will return a positive number if any cell in the range is less than 65, and zero if not. In the...

[![Excel formula: Count cells that are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20are%20blank_0.png "Excel formula: Count cells that are blank")](https://exceljet.net/formulas/count-cells-that-are-blank)

### [Count cells that are blank](https://exceljet.net/formulas/count-cells-that-are-blank)

In this example, the goal is to count cells in a range that are blank. Counting blank cells in Excel can be tricky because cells can look blank even when they are not actually empty. The article below explains three different approaches. COUNTBLANK function The simplest way to count empty cells in...

[![Excel formula: Highlight rows with blank cells](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20rows%20with%20blank%20cells.png "Excel formula: Highlight rows with blank cells")](https://exceljet.net/formulas/highlight-rows-with-blank-cells)

### [Highlight rows with blank cells](https://exceljet.net/formulas/highlight-rows-with-blank-cells)

Conditional formatting is applied to all cells in the active selection at the time a rule is created. In this case, the column references are locked to prevent columns from changing as the formula is evaluated, but the row references are relative so that row numbers are free to change. The result...

[![Excel formula: Highlight blank cells](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight_blank_cells.png "Excel formula: Highlight blank cells")](https://exceljet.net/formulas/highlight-blank-cells)

### [Highlight blank cells](https://exceljet.net/formulas/highlight-blank-cells)

In this example, the goal is to highlight empty cells in the range C5:J16 with conditional formatting. This is a quick and easy way to locate missing values in a data set. To apply a conditional formatting rule to highlight empty cells, follow these steps: Select the range that contains empty cells...

[![Excel formula: Only calculate if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20not%20blank%20then%20calculate2.png "Excel formula: Only calculate if not blank")](https://exceljet.net/formulas/only-calculate-if-not-blank)

### [Only calculate if not blank](https://exceljet.net/formulas/only-calculate-if-not-blank)

The goal is to verify the input of all required values before calculating a result. In the worksheet shown, the SUM function is used as an example only. You can use the same approach with any formula to prevent calculation until all required values are available. The logic can be adjusted in many...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Row is blank](https://exceljet.net/formulas/row-is-blank)
    
*   [All values in a range are at least](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)
    
*   [Count cells that are blank](https://exceljet.net/formulas/count-cells-that-are-blank)
    
*   [Highlight rows with blank cells](https://exceljet.net/formulas/highlight-rows-with-blank-cells)
    
*   [Highlight blank cells](https://exceljet.net/formulas/highlight-blank-cells)
    
*   [Only calculate if not blank](https://exceljet.net/formulas/only-calculate-if-not-blank)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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