# Count cells not between two numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-not-between-two-numbers

---

[Skip to main content](https://exceljet.net/formulas/count-cells-not-between-two-numbers#main-content)

[](https://exceljet.net/formulas/count-cells-not-between-two-numbers#)

*   [Previous](https://exceljet.net/formulas/count-cells-less-than)
    
*   [Next](https://exceljet.net/formulas/count-cells-not-equal-to)
    

[Count](https://exceljet.net/formulas#Count)

Count cells not between two numbers
===================================

by Dave Bruns · Updated 17 Aug 2022

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6469/download?token=hAFXcEmA)
 (18.66 KB)

![Excel formula: Count cells not between two numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Count%20cells%20not%20between%20two%20numbers.png "Excel formula: Count cells not between two numbers")

Summary
-------

To count cell values that are not between two numbers, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the example shown, the formula in cell K5, copied down, is:

    =COUNTIF(C5:G5,"<"&I5)+COUNTIF(C5:G5,">"&J5)
    

At each new row, this formula returns a count of values _not_ between the low and high values in columns I and J.

Generic formula
---------------

    =COUNTIF(range,"<"&low)+COUNTIF(range,">"&high)

Explanation 
------------

The goal of this example is to count the number of values recorded over 5 days that do not fall between two numbers, a low value, and a high value. In other words, to count values that are "out of range". Note that each row, labeled A-G, has its own low and high limit, in columns I and J.

You might at first think to use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 with two criteria. However, because COUNTIFS joins criteria with AND logic, it can't be used with two criteria in this scenario. The logic of less than low AND greater than high will always fail, and the result will always be zero. Instead, we need OR logic.

One straightforward solution is to use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 twice like this:

    =COUNTIF(C5:G5,"<"&I5)+COUNTIF(C5:G5,">"&J5)
    

The first COUNTIF counts values _below_ the value in I5, and the second COUNTIF counts values _above_ the value in J5. When added together these two results correctly handle the required logic: less than I5 OR greater than J5. Notice the greater than (">") and less than ("<") [operators](https://exceljet.net/glossary/logical-operators)
 are [concatenated](https://exceljet.net/glossary/concatenation)
 to cell references with an [ampersand (&) operator](https://exceljet.net/glossary/math-operators)
, a quirk of [RACON functions](https://exceljet.net/articles/excels-racon-functions)
.

### With SUMPRODUCT

A more elegant solution is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 with two logical expressions:

    =SUMPRODUCT((C5:G5<I5)+(C5:G5>J5))
    

Notice we don't need to use concatenation with cell references as with the COUNTIF function above; standard expressions work fine.

This is an example of using [boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
 with addition (+), which creates OR logic. When these expressions are evaluated, we have two [arrays](https://exceljet.net/glossary/array)
 of TRUE and FALSE values like this:

    =SUMPRODUCT({FALSE,FALSE,FALSE,FALSE,TRUE}+{FALSE,FALSE,TRUE,FALSE,FALSE})
    

The math operation automatically coerces the TRUE and FALSE values to 1s and 0s. The result can be visualized like this:

    =SUMPRODUCT({0,0,0,0,1}+{0,0,1,0,0})
    

This results in a single array containing two 1s:

    =SUMPRODUCT({0,0,1,0,1})
    

With only one array to process, SUMPRODUCT sums the items in the array and returns a final result of 2.

### Conditional formatting

To easily see which values aren't between two values, you can use [a conditional formatting rule with a formula](https://exceljet.net/conditional-formatting-formulas)
.

![Conditional formatting to highlight out of range values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/Count%20cells%20not%20between%20two%20numbers%20cropped%20cf.png?itok=pCC95V2g "Conditional formatting to highlight out of range values")

The formula used to highlight the out-of-range values above is:

    =OR(C5<$I5,C5>$J5)
    

More details [here](https://exceljet.net/formulas/highlight-values-not-between-x-and-y)
.

Related formulas
----------------

[![Excel formula: Count cells between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20two%20numbers_0.png "Excel formula: Count cells between two numbers")](https://exceljet.net/formulas/count-cells-between-two-numbers)

### [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)

In this example, the goal is to count numbers that fall within specific ranges. The lower value comes from the "Start" column, and the upper value comes from the "End" column. For each range, we want to include both the lower value and the upper value. For convenience, the numbers being counted are...

[![Excel formula: Count cells between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20dates_0.png "Excel formula: Count cells between dates")](https://exceljet.net/formulas/count-cells-between-dates)

### [Count cells between dates](https://exceljet.net/formulas/count-cells-between-dates)

In this example, the goal is to count the number of cells in column D that contain dates that are between two variable dates in G4 and G5. This problem can be solved with the COUNTIFS function or the SUMPRODUCT function, as explained below. For convenience, the worksheet contains two named ranges...

[![Excel formula: Highlight values not between X and Y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20NOT%20between.png "Excel formula: Highlight values not between X and Y")](https://exceljet.net/formulas/highlight-values-not-between-x-and-y)

### [Highlight values not between X and Y](https://exceljet.net/formulas/highlight-values-not-between-x-and-y)

When you use a formula to apply conditional formatting, the formula is evaluated for each cell in the range, relative to the active cell in the selection at the time the rule is created. So, in this case, if you apply the rule to B4:G11, with B4 as the active cell, the rule is evaluated for each of...

[![Excel formula: Count matches between two columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20matches%20between%20two%20columns.png "Excel formula: Count matches between two columns")](https://exceljet.net/formulas/count-matches-between-two-columns)

### [Count matches between two columns](https://exceljet.net/formulas/count-matches-between-two-columns)

In this example, the goal is to compare two columns and return the count of matches in corresponding rows. A good way to solve this problem is to use the SUMPRODUCT function or the SUM function, as explained below. SUMPRODUCT function The SUMPRODUCT function is a versatile function that handles...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

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

*   [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)
    
*   [Count cells between dates](https://exceljet.net/formulas/count-cells-between-dates)
    
*   [Highlight values not between X and Y](https://exceljet.net/formulas/highlight-values-not-between-x-and-y)
    
*   [Count matches between two columns](https://exceljet.net/formulas/count-matches-between-two-columns)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

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