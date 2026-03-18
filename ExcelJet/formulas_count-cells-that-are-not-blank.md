# Count cells that are not blank - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-are-not-blank

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-are-not-blank#main-content)

[](https://exceljet.net/formulas/count-cells-that-are-not-blank#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-are-blank)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-begin-with)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that are not blank
==============================

by Dave Bruns · Updated 25 Sep 2023

Related functions 
------------------

[COUNTA](https://exceljet.net/functions/counta-function)

[COUNTBLANK](https://exceljet.net/functions/countblank-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count cells that are not blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20are%20not%20blank.png "Excel formula: Count cells that are not blank")

Summary
-------

To count cells that are not blank, you can use the [COUNTA function](https://exceljet.net/functions/counta-function)
. In the example shown, F6 contains this formula:

    =COUNTA(C5:C16)
    

The result is 9, since nine cells in the [range](https://exceljet.net/glossary/range)
 C5:C16 contain values.

Generic formula
---------------

    =COUNTA(range)

Explanation 
------------

In this example, the goal is to count cells in a [range](https://exceljet.net/glossary/range)
 that are not blank (i.e. not empty). There are several ways to go about this task, depending on your needs. The article below explains different approaches.

### COUNTA function

While the [COUNT function](https://exceljet.net/functions/count-function)
 only counts numbers, the [COUNTA function](https://exceljet.net/functions/counta-function)
 counts both numbers and text. This means you can use COUNTA as a simple way to count cells that are not blank. In the example shown, the formula in F6 uses COUNTA like this:

    =COUNTA(C5:C16) // returns 9
    

Since there are nine cells in the range C5:C16 that contain values, COUNTA returns 9. COUNTA is fully automatic, so there is nothing to configure.

### COUNTIFS function

You can also use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 to count cells that are not blank like this:

    =COUNTIFS(C5:C16,"<>") // returns 9
    

The "<>" [operator](https://exceljet.net/glossary/logical-operators)
 means "not equal to" in Excel, so this formula literally means _count cells not equal to nothing_. Because [COUNTIFS can handle multiple criteria](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)
, we can easily extend this formula to count cells that are not empty in Group "A" like this:

    =COUNTIFS(B5:B16,"A",C5:C16,"<>") // returns 4
    

The first _range/criteria_ pair selects cells that are in Group A only. The second _range/criteria_ pair selects cells that are not empty. The result from COUNTIFS is 4, since there are 4 cells in Group A that are not empty. You can swap the order of the _range/criteria_ pairs with the same result.

See also: [50 examples of formula criteria](https://exceljet.net/articles/how-to-use-formula-criteria)
.

### Counting empty strings ("")

One problem with COUNTA and COUNTIFS is that they will also count [empty strings](https://exceljet.net/glossary/empty-string)
 ("") returned by formulas as _not blank_, even though these cells are intended to be blank. For example, if A1 contains 21, this formula in B1 will return an empty string:

    =IF(A1>30,"Overdue","")

However, COUNTA and COUNTIFS will still count B1 as _not empty_. If you run into this problem, you can use the SUMPRODUCT function to count cells that are not blank like this:

    =SUMPRODUCT(--(C5:C16<>""))
    

![Using SUMPRODUCT to count cells that are not blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20cells%20that%20are%20not%20blank%20sumproduct.png?itok=g-FXr_m3 "Using SUMPRODUCT to count cells that are not blank")

The expression C5:C16<>"" returns an [array](https://exceljet.net/glossary/array)
 that contains 12 TRUE and FALSE values, and the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) converts the TRUE and FALSE values to 1s and 0s:

    =SUMPRODUCT({1;1;0;1;1;0;1;1;1;0;1;1}) // returns 9
    

The result is 9 as before. But this formula will ignore empty strings ("") returned by formulas.

You can easily adjust the logic used in SUMPRODUCT with other functions as needed. For example, the variant below uses the [LEN function](https://exceljet.net/functions/len-function)
 to count cells that have a length greater than zero:

    =SUMPRODUCT(--(LEN(C5:C16)>0)) // returns 9
    

You can extend the formula to count cells that are not blank in Group A like this:

    =SUMPRODUCT((LEN(C5:C16)>0)*(B5:B16="A"))
    

This is an example of using [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
 in a formula. The double negative is no longer needed in this case because the math operation of multiplying the two arrays together automatically converts the TRUE and FALSE values to 1s and 0s:

    =SUMPRODUCT({1;1;0;1;1;0;0;0;0;0;0;0}) // returns 4
    

The final result is 4, since there are four cells in Group A that are not blank in C5:C16.

_Note: in Excel 2021+, you can use the SUM function instead of SUMPRODUCT in the formula above with the same result. You can read more about this topic here: [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)
_

Related formulas
----------------

[![Excel formula: Count cells that contain numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20numbers.png "Excel formula: Count cells that contain numbers")](https://exceljet.net/formulas/count-cells-that-contain-numbers)

### [Count cells that contain numbers](https://exceljet.net/formulas/count-cells-that-contain-numbers)

In this example, the goal is to count the number of cells in a range that contain numbers. This problem can be solved with the COUNT function or the SUMPRODUCT function. Both methods are explained below. COUNT function The COUNT function counts the number of cells in a range that contain numeric...

[![Excel formula: Count cells that contain text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20text.png "Excel formula: Count cells that contain text")](https://exceljet.net/formulas/count-cells-that-contain-text)

### [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)

In this example, the goal is to count cells in a range that contain text values. This could be hard-coded text like "apple" or "red", numbers entered as text, or formulas that return text values. Empty cells and cells that contain numeric values or errors should not be included in the count. This...

[![Excel formula: Count cells that are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20are%20blank_0.png "Excel formula: Count cells that are blank")](https://exceljet.net/formulas/count-cells-that-are-blank)

### [Count cells that are blank](https://exceljet.net/formulas/count-cells-that-are-blank)

In this example, the goal is to count cells in a range that are blank. Counting blank cells in Excel can be tricky because cells can look blank even when they are not actually empty. The article below explains three different approaches. COUNTBLANK function The simplest way to count empty cells in...

Related functions
-----------------

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel COUNTBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20countblank%20function.png "Excel COUNTBLANK function")](https://exceljet.net/functions/countblank-function)

### [COUNTBLANK Function](https://exceljet.net/functions/countblank-function)

The Excel COUNTBLANK function returns a count of empty cells in a [range](https://exceljet.net/glossary/range)
. Cells that contain text, numbers, errors, spaces, etc. are _not_ counted. Formulas that return empty strings ("") _are_ counted as blank.

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

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

*   [Count cells that contain numbers](https://exceljet.net/formulas/count-cells-that-contain-numbers)
    
*   [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)
    
*   [Count cells that are blank](https://exceljet.net/formulas/count-cells-that-are-blank)
    

### Functions

*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [COUNTBLANK Function](https://exceljet.net/functions/countblank-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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