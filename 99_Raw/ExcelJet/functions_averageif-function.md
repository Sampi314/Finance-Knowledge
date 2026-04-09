# Excel AVERAGEIF function | Exceljet

**Source:** https://exceljet.net/functions/averageif-function

---

[Skip to main content](https://exceljet.net/functions/averageif-function#main-content)

[](https://exceljet.net/functions/averageif-function#)

*   [Previous](https://exceljet.net/functions/averagea-function)
    
*   [Next](https://exceljet.net/functions/averageifs-function)
    

Excel 2007

[Statistical](https://exceljet.net/functions#Statistical)

AVERAGEIF Function
==================

by Dave Bruns · Updated 8 Jun 2025

Related functions 
------------------

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

[AVERAGE](https://exceljet.net/functions/average-function)

[AVERAGEA](https://exceljet.net/functions/averagea-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[MINIFS](https://exceljet.net/functions/minifs-function)

[MAXIFS](https://exceljet.net/functions/maxifs-function)

![Excel AVERAGEIF function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_averageif.png "Excel AVERAGEIF function")

Summary
-------

The Excel AVERAGEIF function calculates the average of numbers in a range that meet supplied criteria. AVERAGEIF criteria can include logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching.

Purpose 
--------

Get the average of numbers that meet criteria.

Return value 
-------------

A number representing the average.

Syntax
------

    =AVERAGEIF(range,criteria,[average_range])

*   _range_ - One or more cells, including numbers or names, arrays, or references.
*   _criteria_ - A number, expression, cell reference, or text.
*   _average\_range_ - \[optional\] The cells to average. When omitted, range is used.

Using the AVERAGEIF function 
-----------------------------

The AVERAGEIF function calculates the average of the numbers in a range that meet supplied criteria. To apply criteria, the AVERAGEIF function supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. AVERAGEIF can be used to average cells based on dates, numbers, and text. Note that AVERAGEIF only handles one condition. To apply multiple conditions, use the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
.

### Key Features

*   Calculates averages based on _one condition only_ (use [AVERAGEIFS](https://exceljet.net/functions/averageifs-function)
     for multiple criteria)
*   Supports logical operators (>, <, >=, <=, <>, =) and wildcards (\*, ?) for flexible matching
*   _Automatically excludes_ empty cells from the average calculation (even when criteria match)
*   Returns #DIV/0! error if no cells meet the specified criteria
*   Works in all versions of Excel

> Unlike most other Excel functions, AVERAGEIF requires an actual range for the _range_ and _average\_range_ arguments. If you try to use an [array](https://exceljet.net/glossary/array)
> , Excel will not let you enter the formula.

### Syntax

The generic syntax for AVERAGEIF looks like this:

    =AVERAGEIF(range,criteria,[average_range])

The AVERAGEIF function takes three [arguments](https://exceljet.net/glossary/function-argument)
: _range_, _criteria_, and _average\_range_. _Range_ is the range of cells to apply a condition to, and c_riteria_ is the condition to apply, along with any logical operators that are needed. _Average\_range_ argument is optional. When _average\_range_ is not provided, AVERAGEIF will average values in the _range_ argument. When _average\_range_ is provided, AVERAGEIF will average values in _average\_range_. 

### Criteria

The AVERAGEIF function supports logical operators (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. Because AVERAGEIF is in a group of [eight functions](https://exceljet.net/articles/excels-racon-functions)
 that split logical criteria into two parts, the syntax is a bit tricky. Range and criteria are provided separately, and operators in _criteria_ need to be enclosed in double quotes (""). The table below shows some common examples:

| Target | Criteria |
| --- | --- |
| Cells greater than 75 | ">75" |
| Cells equal to 100 | 100 or "100" |
| Cells less than or equal to 100 | "<=100" |
| Cells equal to "Red" | "red" |
| Cells not equal to "Red" | "<>red" |
| Cells that are blank "" | ""  |
| Cells that are _not_ blank | "<>" |
| Cells that begin with "X" | "x\*" |
| Cells less than A1 | "<"&A1 |
| Cells less than today | "<"&TODAY() |

Notice the last two examples use [concatenation](https://exceljet.net/glossary/concatenation)
 with the ampersand (&) character. When a _criteria_ argument includes a value from another cell, or the result of a formula, logical operators like "<" must be joined with concatenation. This is because Excel needs to evaluate cell references and formulas first to get a value, before that value can be joined to an operator.

### Examples

In the example shown, the formulas in H5:H8 are as follows:

    =AVERAGEIF(C5:C15,">0") // price greater than $0
    =AVERAGEIF(C5:C15,">200000") // price greater than $200k
    =AVERAGEIF(D5:D15,">=2",C5:C15) // 2+ bedrooms
    =AVERAGEIF(D5:D15,">=3",C5:C15) // 3+ bedrooms
    

### Double quotes ("") in criteria

In general, text values are enclosed in double quotes (""), and numbers are not. However, when a [logical operator](https://exceljet.net/glossary/logical-operators)
 is included with a number, the number and operator must be enclosed in quotes. Note the difference in the two examples below. Because the second formula uses the greater than or equal to operator (>=), the operator and number are both enclosed in double quotes.

    =AVERAGEIF(D5:D15,2,C5:C15) // 2 bedrooms
    =AVERAGEIF(D5:D15,">=2",C5:C15) // 2+ bedrooms
    

Double quotes are also used for text values. For example, to average values in B1:B10 when values in A1:A10 equal "red", you can use a formula like this:

    =AVERAGEIF(A1:A10,"red",B1:B10) // average "red" only
    

### Value from another cell

A value from another cell can be included in criteria using [concatenation](https://exceljet.net/glossary/concatenation)
. In the example below, AVERAGEIF will return the average of numbers in A1:A10 that are less than the value in cell B1. Notice the less-than [operator](https://exceljet.net/glossary/logical-operators)
 (which is text) is enclosed in quotes.

    =AVERAGEIF(A1:A10,"<"&B1) // average values less than  B1
    

### Wildcards

The [wildcard](https://exceljet.net/glossary/wildcard)
 characters question mark (?), asterisk(\*), or tilde (~) can be used in criteria. A question mark (?) matches any one character, and an asterisk (\*) matches zero or more characters of any kind. For example, to average cells in a B1:B10 when cells in A1:A10 contain the text "red" anywhere, you can use a formula like this:

    =AVERAGEIF(A1:A10,"*red*",B1:B10) // contains "red"
    

The tilde (~) is an escape character to allow you to find literal wildcards. For example, to match a literal question mark (?), asterisk(\*), or tilde (~), add a tilde in front of the wildcard (i.e. ~?, ~\*, ~~).

### Average range caution

AVERAGEIF makes certain assumptions about the size of _average\_range_, essentially resizing it when necessary to match the _range_ argument, using the upper left cell in the range as an origin. In some cases, this behavior can create a result that _seems reasonable_ but is in fact _incorrect_. For an example of this problem, [see this article](https://exceljet.net/formulas/average-if-with-filter)
.

### Notes

*   TRUE and FALSE values ignored when calculating an average.
*   Empty cells are ignored when calculating an average.
*   AVERAGEIF returns #DIV/0! if no cells in _range_ meet criteria.
*   AVERAGEIF requires _actual ranges_ - cannot use [arrays](https://exceljet.net/glossary/array)
     for range arguments.
*   _Average\_range_ does not have to be the same size as _range_. The top left cell in _average\_range_ is used as the starting point, and cells that correspond to cells in _range_ are averaged.
*   AVERAGEIF supports [wildcards](https://exceljet.net/glossary/wildcard)
     but is not case-sensitive.

AVERAGEIF function examples
---------------------------

[![Excel formula: Average and ignore errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average%20and%20ignore%20errors2.png "Excel formula: Average and ignore errors")](https://exceljet.net/formulas/average-and-ignore-errors)

### [Average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)

In this example, the goal is to average a list of values that may contain errors. The values to average are in the named range data (B5:B15). Normally, you can use the AVERAGE function to calculate an average. However, if the data contains errors, AVERAGE will return an error. You can see this in...

[![Excel formula: Average numbers ignore zero](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_numbers_ignore_zero.png "Excel formula: Average numbers ignore zero")](https://exceljet.net/formulas/average-numbers-ignore-zero)

### [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)

In this example, the goal is to calculate an average of the quiz scores in columns C, D, E, and F for each person. However, the result needs to ignore any zeros that appear in the data. This formula can be easily solved with the AVERAGEIF function or the AVERAGEIFS function . It can also be solved...

AVERAGEIF function videos
-------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20AVERAGEIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-averageif-function)

### [How to use the AVERAGEIF function](https://exceljet.net/videos/how-to-use-the-averageif-function)

In this video, we'll look at how to use the AVERAGEIF function to calculate an average from numbers that meet a single criteria. Here we have a list of 16 properties with prices and other information. Let's calculate some averages based on the conditions listed in column K. The AVERAGEIF function...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)

### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)

In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...

Related functions
-----------------

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel AVERAGEA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20averagea%20function.png "Excel AVERAGEA function")](https://exceljet.net/functions/averagea-function)

### [AVERAGEA Function](https://exceljet.net/functions/averagea-function)

The Excel AVERAGEA function returns the average of a set of supplied values. Unlike AVERAGE, AVERAGEA will also evaluate the logical values TRUE and FALSE, and numbers represented as text, whereas AVERAGE ignores these values during calculation

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel MINIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_minifs.png "Excel MINIFS function")](https://exceljet.net/functions/minifs-function)

### [MINIFS Function](https://exceljet.net/functions/minifs-function)

The Excel MINIFS function returns the smallest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MINIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers,...

[![Excel MAXIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxifs%20function.png "Excel MAXIFS function")](https://exceljet.net/functions/maxifs-function)

### [MAXIFS Function](https://exceljet.net/functions/maxifs-function)

The Excel MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MAXIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)
    
*   [Average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)
    

### Videos

*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    
*   [How to use the AVERAGEIF function](https://exceljet.net/videos/how-to-use-the-averageif-function)
    

### Functions

*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [AVERAGEA Function](https://exceljet.net/functions/averagea-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [MINIFS Function](https://exceljet.net/functions/minifs-function)
    
*   [MAXIFS Function](https://exceljet.net/functions/maxifs-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

### Links

*   [Microsoft AVERAGEIF function documentation](https://support.office.com/en-us/article/averageif-function-faec8e2e-0dec-4308-af69-f5576d8ac642)
    

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