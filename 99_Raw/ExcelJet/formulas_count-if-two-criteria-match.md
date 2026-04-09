# Count if two criteria match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-if-two-criteria-match

---

[Skip to main content](https://exceljet.net/formulas/count-if-two-criteria-match#main-content)

[](https://exceljet.net/formulas/count-if-two-criteria-match#)

*   [Previous](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/count-items-in-list)
    

[Count](https://exceljet.net/formulas#Count)

Count if two criteria match
===========================

by Dave Bruns · Updated 21 Aug 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count if two criteria match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Count%20if%20two%20criteria%20match.png "Excel formula: Count if two criteria match")

Summary
-------

To count rows where two (or more) criteria match, you can use a formula based on the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. In the example shown, the formula in cell G5 is:

    =COUNTIFS(B5:B15,"blue",C5:C15,">15")
    

The result is 3, since there are three rows with a color of "blue" and quantity greater than 15.

Generic formula
---------------

    =COUNTIFS(range1,"blue",range2,">15")

Explanation 
------------

In this example, the goal is to count orders where the color is "blue" and the quantity is greater than 15. All data is in the [range](https://exceljet.net/glossary/range)
 B5:B15. There are two primary ways to solve this problem, one with the COUNTIFS function, the other with the SUMPRODUCT function. Both approaches are explained below.

### COUNTIFS function

The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 returns the count of cells that meet one or more criteria. COUNTIFS can be used with criteria based on dates, numbers, text, and other conditions. COUNTIFS supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching.

In this example, we want to count orders where the color is "blue" in column B and the quantity is greater than 15 in column C. The COUNTIFS function takes multiple criteria in pairs — each pair contains one range and the associated criteria for that range. To start off, we can write a formula like this to count orders where the color is "blue":

    =COUNTIFS(B5:B15,"blue") // returns 5
    

COUNTIFS returns 5 since there are five cells in B5:B15 equal to "blue". Notice we have single range/criteria pair at this point. To add a condition to check for a quantity greater than (>) 15, we add another range/criteria pair like this:

    =COUNTIFS(B5:B15,"blue",C5:C15,">15") // returns 3
    

This is the formula used in cell G5 in the example. COUNTIFS returns 3, since there are three rows in the data where the color in B5:B15 is "blue" and the quantity in C5:C15 is greater than 15. To generate a count, all conditions must match. To add more conditions, add more range/criteria pairs. For reference, the formula in G6 is:

    =COUNTIFS(B5:B15,"red",C5:C15,">15") // returns 1
    

This time, COUNTIFS returns 1, since there is just one "red" order over 15.

### SUMPRODUCT alternative

You can also use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to count rows that match multiple conditions. the equivalent formula is:

    =SUMPRODUCT((B5:B15="blue")*(C5:C15>15)) // returns 3
    

This is an example of using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 in a formula. The first expression tests for "blue":

    B5:B15="blue"
    

Because there are 11 cells in B5:B15, the expression returns 11 TRUE and FALSE values in an [array](https://exceljet.net/glossary/array)
 like this:

    {FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE}
    

The second expression tests for a quantity greater than 15:

    C5:C15>15
    

Because there are again 11 cells in C5:C15, this expression returns an array like this:

    {FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE}
    

The math operation of multiplying these two arrays together [converts](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 the TRUE and FALSE values to 1s and 0s:

    =SUMPRODUCT({0;1;0;1;0;1;0;0;1;0;1}*{0;0;1;1;1;1;0;0;1;1;0})
    

After multiplication, we have a single array like this:

    =SUMPRODUCT({0;0;0;1;0;1;0;0;1;0;0})
    

With just one array to process, SUMPRODUCT returns the sum, 3, as a final result.

SUMPRODUCT is more powerful and flexible than COUNTIFS, which is in a [group of eight functions require ranges](https://exceljet.net/articles/excels-racon-functions)
. For more details, see [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)
.

### Pivot table alternative

To summarize different combinations in a larger data set, consider a [Pivot Table](https://exceljet.net/articles/excel-pivot-tables)
. Pivot tables are a fast and flexible reporting tool that can summarize data in many different ways. For a direct comparison of SUMIF and Pivot tables, see [this video](https://exceljet.net/videos/why-pivot-tables)
.

Related formulas
----------------

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Count cells between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20two%20numbers_0.png "Excel formula: Count cells between two numbers")](https://exceljet.net/formulas/count-cells-between-two-numbers)

### [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)

In this example, the goal is to count numbers that fall within specific ranges. The lower value comes from the "Start" column, and the upper value comes from the "End" column. For each range, we want to include both the lower value and the upper value. For convenience, the numbers being counted are...

[![Excel formula: COUNTIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/COUNTIFS%20with%20multiple%20criteria%20and%20OR%20logic.png "Excel formula: COUNTIFS with multiple criteria and OR logic")](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

### [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

In this example, the goal is to use the COUNTIFS function to count data with "OR logic". The challenge is the COUNTIFS function applies AND logic by default. COUNTIFS function The COUNTIFS function returns the count of cells that meet one or more criteria, and supports logical operators (>,...

[![Excel formula: Two-way summary count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Two-way%20summary%20count.png "Excel formula: Two-way summary count")](https://exceljet.net/formulas/two-way-summary-count)

### [Two-way summary count](https://exceljet.net/formulas/two-way-summary-count)

In this example, the goal is to count the people shown in the table by both Department (Dept) and Group as shown in the worksheet. A simple way to do this is with the COUNTIFS function. COUNTIFS function The COUNTIFS function is designed to count things based on more than one condition. Conditions...

[![Excel formula: Count if row meets internal criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20if%20row%20meets%20internal%20criteria.png "Excel formula: Count if row meets internal criteria")](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)

### [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)

In this example the goal is to count products (rows) where sales have increased and sales have decreased, where previous sales are in column C (Previous) and current sales are in column D (Current). In this case, we can't use COUNTIFS directly, because COUNTIFS is a range-based function and it won'...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Why%20pivot%20table-Thumb.png)](https://exceljet.net/videos/why-pivot-tables)

### [Why pivot tables?](https://exceljet.net/videos/why-pivot-tables)

Hi, Dave here from Exceljet So, today we're going to tackle the question Why Pivot Tables? And this question comes up a lot when people first run into Pivot Tables, because they're wondering...why should they care? And you're trying to explain that pivot tables are really fast, that you can...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)
    
*   [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)
    
*   [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
    
*   [Two-way summary count](https://exceljet.net/formulas/two-way-summary-count)
    
*   [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Videos

*   [Why pivot tables?](https://exceljet.net/videos/why-pivot-tables)
    

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