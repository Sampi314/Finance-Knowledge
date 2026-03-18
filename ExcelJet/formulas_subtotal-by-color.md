# Subtotal by color - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/subtotal-by-color

---

[Skip to main content](https://exceljet.net/formulas/subtotal-by-color#main-content)

[](https://exceljet.net/formulas/subtotal-by-color#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-contain-formulas)
    
*   [Next](https://exceljet.net/formulas/subtotal-by-invoice-number)
    

[Sum](https://exceljet.net/formulas#Sum)

Subtotal by color
=================

by Dave Bruns · Updated 23 Oct 2025

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Subtotal by color](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/subtotal%20by%20color_0.png "Excel formula: Subtotal by color")

Summary
-------

To subtotal values by cell color you can use a few different approaches. In the example shown above, the formula in G5 to count amounts that are highlighted in green is:

    =COUNTIF(amount,F5)
    

where **color** (D5:D16) and **amount** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
. This is an indirect approach that works because the logic that has been used to apply color is easily reproducible inside the COUNTIF function. See below for a more direct approach.

Explanation 
------------

In this example, the goal is to subtotal (count and sum) values based on cell color. This is a tricky problem, because there is no Excel function that will let you count cells by color directly. There are several different approaches, as explained below.

### Standard formula logic

If color is being applied based on specific rules (either with conditional formatting or manually) you may be able to use standard logic that follows the same rules to count and sum by color. This is an indirect way to solve this problem because the formula is not actually checking cell color but is instead applying logic that mirrors the rules that were used to apply the color. However, it is a simple and clean way to solve the problem in compatible scenarios.

In the screen below, the green and yellow color is applied with two separate conditional formatting rules. When a value in column C is less than 1000, _yellow_ formatting is applied. When a value is greater than 1200, _green_ formatting is applied. The formulas in G5:G6, and H5:H6 use this same criteria to count and sum the data. The formula in cell G5 is:

    =COUNTIF(amount,F5)
    =COUNTIF(C5:C16,"<1000") // returns 2
    

The formula in H5 is:

    =SUMIF(amount,F5)
    =SUMIF(C5:C16,"<1000") // returns 1915
    

This approach only works in cases where cell color is being applied with rules that can be applied in a formula. It won't handle cases where color is applied to cells randomly, or in a way that can't be mimicked in a formula. For that situation, see the GET.CELL option below.

### GET.CELL function

In cases where cell color has been applied _manually_ (i.e. not with conditional formatting), you can use an obscure function called GET.CELL to retrieve cell color as a numeric code, then use this code to calculate the subtotals you need, as seen in the worksheet below:

![Subtotals by color with the GET.CELL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/subtotal%20by%20color%20with%20GETCELL.png?itok=Puo0Oy5Z "Subtotals by color with the GET.CELL function")

GET.CELL can't be used in a formula directly, you must first [create a named range](https://exceljet.net/articles/named-ranges)
 that uses GET.CELL to get the color of the cell directly to the left. To do this, place the cursor in cell B1, then create a new named range called "CellColor" that refers to cell A1 like this:

    =GET.CELL(38,A1)
    

![Creating a named range called CellColor](https://exceljet.net/sites/default/files/images/formulas/inline/Creating%20a%20named%20range%20called%20CellColor.png "Creating a named range called CellColor")

> Another option to define a cell "one column to the left in the same row" is to use an R1C1-style reference with the [INDIRECT function](https://exceljet.net/functions/indirect-function)
>  like this: `=GET.CELL(38,INDIRECT("RC[-1]",FALSE))`There is very little good documentation on GET.CELL, but I did find this [interesting 20+ year old link](https://www.mrexcel.com/board/threads/info-only-get-cell-arguments.20611/)
>  on MrExcel.com that provides a list of available arguments.

Because we are using [relative references](https://exceljet.net/glossary/relative-reference)
, this essentially means: get the color code of the cell directly to the left. Once you have defined the named range, you can use it in a column directly to the right of the cell you want color information for. In the worksheet shown below, CellColor is used in cell D5 like this:

    =CellColor
    

![Using CellColor on the worksheet](https://exceljet.net/sites/default/files/images/formulas/inline/calling%20CellColor%20on%20the%20worksheet.png "Using CellColor on the worksheet")

In cases where the cell to the left _does not_ have a fill color, the result is zero (0). In cases where a fill color has been applied, CellColor will return a unique numeric code for that particular color. In the example shown, light green is 35 and light yellow is 19. In cell G5, the formula is:

    =COUNTIF(color,19) // returns 2
    

where **color** is the [named range](https://exceljet.net/glossary/named-range)
 D5:D16. Notice we are hardcoding 19 into the formula to count cells that have a light yellow fill. In cell G6, we count the colors that are 35 (light green):

    =COUNTIF(color,35) // returns 3
    

The formulas in cells H5 and H6 use [SUMIF](https://exceljet.net/functions/sumif-function)
 to sum amounts based on the same color codes:

    =SUMIF(color,19,amount) // returns 1915
    =SUMIF(color,35,amount) // returns 3900
    

where **color** (D5:D16) and **amount** (C5:C16) are named ranges.

_Note: the GET.CELL function is an old macro-based function. You will need to save your worksheet with macros enabled (i.e. with the extension .xlsm) to use it._

### With a filter and SUBTOTAL

Another way to solve this problem is to use Excel's "Filter by Color" feature with the [SUBTOTAL function](https://exceljet.net/functions/subtotal-function)
. To take this approach, first [enable a filter](https://exceljet.net/shortcuts/toggle-autofilter)
 on the data you are working with like this:

![Filter enabled above data](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/subtotal%20by%20color%20filter%20setup.png?itok=ySPazehR "Filter enabled above data")

Next, either above or below the data, enter the SUBTOTAL function configured to target visible cells. In the screen below, the formulas to count and sum visible cells are:

    =SUBTOTAL(102,amount) // count visible
    =SUBTOTAL(109,amount) // sum visible
    

where **amount** is the [named range](https://exceljet.net/glossary/named-range)
 C5:C16. The _function\_num_ 102 directs SUBTOTAL to [count visible cells](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list)
, and the number 109 tells SUBTOTAL to [sum visible cells](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)
. Finally, select a target color in the Filter by Color menu:

![Use the Filter by color menu to filter by color](https://exceljet.net/sites/default/files/images/formulas/inline/subtotal%20by%20color%20with%20filter%20by%20color%20menu.png "Use the Filter by color menu to filter by color")

Filtering by color will exclude rows that do not match the target color and the SUBTOTAL formulas entered previously will show results that apply only to the color selected:

![Final results after filtering by color](https://exceljet.net/sites/default/files/images/formulas/inline/subtotal%20by%20color%20filter%20final%20results.png "Final results after filtering by color")

To show results for another color, just change the target color in the Filter by Color menu.

_Note: Another way to solve this problem is to create a custom function with VBA._ [_Sumit Bansal has a good summary of this approach here_](https://trumpexcel.com/count-colored-cells-in-excel/)
_._

Related formulas
----------------

[![Excel formula: Sum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_multiple_criteria.png "Excel formula: Sum if multiple criteria")](https://exceljet.net/formulas/sum-if-multiple-criteria)

### [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)

In this example, the goal is to sum the values in F5:F16 when the Color in C5:C16 is "Red" and the State in D5:D16 is "TX". This is an example of a conditional sum with multiple criteria and the SUMIFS function is the easiest way to solve this problem. SUMIFS function The SUMIFS function sums cells...

[![Excel formula: Subtotal invoices by age](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Subtotal%20invoices%20by%20age.png "Excel formula: Subtotal invoices by age")](https://exceljet.net/formulas/subtotal-invoices-by-age)

### [Subtotal invoices by age](https://exceljet.net/formulas/subtotal-invoices-by-age)

In this example, the goal is to subtotal invoices by age, where age represents the number of days since the invoice was issued. This problem can be solved with the SUMIFS function and the COUNTIFS function, as explained below. For convenience, age (E5:E16) and amount (D5:D16) are named ranges ...

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumif-function)

### [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)

In this video we'll look at how to use the SUMIF function to sum cells that meet a single criteria. Let's take a look. The SUMIF function sums cells that satisfy a single condition that you supply. It takes three arguments: range, criteria, and sum range. Note that sum range is optional. If you don...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)
    
*   [Subtotal invoices by age](https://exceljet.net/formulas/subtotal-invoices-by-age)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Videos

*   [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)
    
*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    

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