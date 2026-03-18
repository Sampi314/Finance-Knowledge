# Sum if not blank - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-not-blank

---

[Skip to main content](https://exceljet.net/formulas/sum-if-not-blank#main-content)

[](https://exceljet.net/formulas/sum-if-not-blank#)

*   [Previous](https://exceljet.net/formulas/sum-if-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/sum-if-one-of-many-things)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if not blank
================

by Dave Bruns · Updated 28 Apr 2025

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[FILTER](https://exceljet.net/functions/filter-function)

[SUM](https://exceljet.net/functions/sum-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7660/download?token=gKJEHOZJ)
 (14.95 KB)

![Excel formula: Sum if not blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_not_blank.png "Excel formula: Sum if not blank")

Summary
-------

To sum values when corresponding cells are _not blank_, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. In the example shown, the formula in cell G5 is:

    =SUMIFS(C5:C16,D5:D16,"<>")
    

The result is 61,600, the sum of amounts in C5:C16 when corresponding cells in D5:D16 are _not blank_.

Generic formula
---------------

    =SUMIFS(sum_range,range,"<>")

Explanation 
------------

In this example, the goal is to sum the Amounts in C5:C16 when the Lead in D5:D16 is not blank (i.e., not empty). A good way to solve this problem is to use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. However, you can also use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 or the [FILTER function](https://exceljet.net/functions/filter-function)
, as explained below. Because SUMPRODUCT and FILTER can work with ranges _and_ [arrays](https://exceljet.net/glossary/array)
, they are more flexible.

### Background study

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

### SUMIFS Function

The SUMIFS function sums cells in a [range](https://exceljet.net/glossary/range)
 that meet one or more conditions, referred to as _criteria_. To apply criteria, the SUMIFS function supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. The generic syntax for SUMIFS with one condition looks like this:

    =SUMIFS(sum_range,range1,criteria1) // 1 condition

In this case, we need to test for only one condition, which is that the cells in D5:D16 are _not blank_. We start off with the _sum\_range_, which contains the amounts in C5:C16:

    =SUMIFS(C5:C16,

Next, we add the _range_ that we need to test, which in D5:D16:

    =SUMIFS(C5:C16,D5:D16,

Finally, we add the _criteria_, which is not equal to [operator](https://exceljet.net/glossary/logical-operators)
 (<>), which must be enclosed in double quotes (""):

    =SUMIFS(C5:C16,D5:D16,"<>")

The result is 61,600, the sum of amounts in C5:C16 when corresponding cells in D5:D16 are _not blank_. The main challenge with SUMIFS is the [quirky syntax](https://exceljet.net/articles/excels-racon-functions)
. For criteria, we simply use the "not equal to" operator, "<>". We don't provide a value, and it's implied that this means "not equal to nothing", i.e., "not blank". To read more about how to use the SUMIFS function with logical operators and wildcards, [see this page](https://exceljet.net/functions/sumifs-function)
.

### SUMPRODUCT function

Another way to solve this problem is with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and a formula like this:

    =SUMPRODUCT((D5:D16<>"")*C5:C16)

This is an example of using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 in Excel. The expression on the left checks if the cells in D5:D16 are not empty:

    (D5:D16<>"")

Because there are 12 cells in D5:D16, the expression returns an [array](https://exceljet.net/glossary/array)
 of 12 TRUE and FALSE values:

    {TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;FALSE;TRUE;TRUE;FALSE}

Note the TRUE values correspond to cells in D5:D16 that are _not blank_. Next, the math operation of multiplying this array by the range numeric values in C5:C16 automatically converts the TRUE and FALSE values to an array of 1s and 0s. Inside SUMPRODUCT, we can visualize the operation like this:

    =SUMPRODUCT({1;0;1;1;1;1;0;1;0;1;1;0}*C5:C16)

In this form, you can see how the logic works. When the Boolean array is multiplied by C5:C16, it acts like a filter that only allows values associated with 1s to pass through; other values are "zeroed out". After multiplication, we have one array:

    =SUMPRODUCT({10600;0;12000;7500;6000;4000;0;7000;0;2500;12000;0})

With only one array to process, SUMPRODUCT sums the array and returns 61,600 as a final result. One advantage of SUMPRODUCT is that it can handle [array operations](https://exceljet.net/glossary/array-operation)
 natively. This can be handy when you want to adjust a formula to use more specific logic that is not supported by SUMIFS. For more information, see [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)

### FILTER function

In the latest version of Excel, another approach is to use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [SUM function](https://exceljet.net/functions/sum-function)
 in a formula like this:

    =SUM(FILTER(C5:C16,D5:D16<>"",0))

In this formula, we are literally removing values we don't want to sum. The FILTER function is configured to return only values in C5:C16 when cells in D5:D16 are _not empty_. The result inside SUM looks like this:

    =SUM({10600;12000;7500;6000;4000;7000;2500;12000})

The final result is 61,600. Like SUMPRODUCT, FILTER is a more flexible function that can apply criteria in ways that SUMIFS can't. For more on the FILTER function, [see this page](https://exceljet.net/functions/filter-function)
.

### Sum if blank

The formulas above can be easily adjusted to sum amounts when corresponding cells in D5:D16 _are blank_. In the worksheet shown, the formula in cell G6 is:

    =SUMIFS(C5:C16,D5:D16,"")

The result is 32,700, the sum of amounts in C5:C16 when corresponding cells in D5:D16 _are blank_. The equivalent SUMPRODUCT and FILTER formulas are as follows:

    =SUMPRODUCT((D5:D16="")*C5:C16)
    =SUM(FILTER(C5:C16,D5:D16="",0))

These formulas also return 32,700.

Related formulas
----------------

[![Excel formula: Sum if cells are equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_equal_to.png "Excel formula: Sum if cells are equal to")](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

### [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when cells in the range C5:C15 contain "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only a single condition. SUMIFS on the other...

[![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")](https://exceljet.net/formulas/sum-if-x-or-y)

### [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an Excel Table named data . This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the SUMIFS function . However, when...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20algebra%20in%20Excel-Play.png)](https://exceljet.net/videos/boolean-algebra-in-excel)

### [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

In this video, we’ll look at how boolean algebra is used for AND and OR logic in formulas. In Boolean algebra, there are only two possible results for a math operation: 1 or 0, which, as we know, correspond to the logical values TRUE and FALSE. AND logic corresponds to multiplication . Anything...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

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