# Excel AVERAGEIFS function | Exceljet

**Source:** https://exceljet.net/functions/averageifs-function

---

[Skip to main content](https://exceljet.net/functions/averageifs-function#main-content)

[](https://exceljet.net/functions/averageifs-function#)

*   [Previous](https://exceljet.net/functions/averageif-function)
    
*   [Next](https://exceljet.net/functions/binom.dist-function)
    

Excel 2007

[Statistical](https://exceljet.net/functions#Statistical)

AVERAGEIFS Function
===================

by Dave Bruns · Updated 8 Jun 2025

Related functions 
------------------

[AVERAGEIF](https://exceljet.net/functions/averageif-function)

[AVERAGE](https://exceljet.net/functions/average-function)

[AVERAGEA](https://exceljet.net/functions/averagea-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[MINIFS](https://exceljet.net/functions/minifs-function)

[MAXIFS](https://exceljet.net/functions/maxifs-function)

![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")

Summary
-------

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Purpose 
--------

Average cells that match multiple criteria

Return value 
-------------

The average of the cells that meet all criteria

Syntax
------

    =AVERAGEIFS(avg_rng,range1,criteria1,[range2],[criteria2],...)

*   _avg\_rng_ - The range to average.
*   _range1_ - The first range to evaluate.
*   _criteria1_ - The criteria to use on range1.
*   _range2_ - \[optional\] The second range to evaluate.
*   _criteria2_ - \[optional\] The criteria to use on range2.

Using the AVERAGEIFS function 
------------------------------

The AVERAGEIFS function calculates the average of cells in a range that meet multiple conditions, referred to as _criteria_. Each condition is provided with a separate _range_ and _criteria_. To define criteria, AVERAGEIFS supports various [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?,~). The AVERAGEIFS function is widely used in Excel and can be used to average cells based on dates, text values, and numbers. However, the syntax used to apply conditions is a bit tricky because it is unusual in Excel. See below for details.

### Key Features

*   Calculates averages based on _multiple conditions_
*   Supports logical operators (>, <, >=, <=, <>, =) and wildcards (\*, ?, ~) for flexible matching
*   _Automatically excludes_ empty cells from the average calculation (even when criteria match)
*   Only cells that meet _all conditions_ are included in the final average (uses AND logic).
*   Returns #DIV/0! error if no cells meet the specified criteria.
*   Works in Excel 2007 and all later versions.

> Unlike most other Excel functions, AVERAGEIFS requires actual ranges for _average\_range_ and all _criteria\_range_ arguments. If you try to use an [array](https://exceljet.net/glossary/array)
> , Excel will not let you enter the formula.

### Syntax

The syntax for the AVERAGEIFS function depends on the criteria being evaluated. Each separate condition will require a _range_ and _criteria_. The generic syntax for AVERAGEIFS looks like this:

    =AVERAGEIFS(avg_range,range1,criteria1) // 1 condition
    =AVERAGEIFS(avg_range,range1,criteria1,range2,criteria2) // 2 conditions

The first [argument](https://exceljet.net/glossary/function-argument)
, _avg\_range_, is the range of cells to average, which should contain numeric values. The second argument, _range1_, is the range to which the first condition should be applied. The third argument, _criteria1_, contains the condition that should be applied to _range1_, along with any [logical operators](https://exceljet.net/glossary/logical-operators)
. Additional conditions are applied by providing additional _range/criteria_ arguments. 

### Applying criteria

The AVERAGEIFS function supports logical operators (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. Because AVERAGEIFS is in a group of [eight functions](https://exceljet.net/articles/excels-racon-functions)
 that split logical criteria into two parts, the syntax is a bit tricky. Each condition requires a separate _range_ and _criteria_, and operators need to be enclosed in double quotes (""). The table below shows some common examples:

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
 with the ampersand (&) character. When a criteria argument includes a value from another cell, or the result of a formula, logical operators like "<" must be joined with concatenation. This is because Excel needs to evaluate cell references and formulas first to get a value, before that value can be joined with an operator.

### Examples

In the example shown, the formulas in H5:H7 are:

    =AVERAGEIFS(C5:C15,C5:C15,">0")
    =AVERAGEIFS(C5:C15,C5:C15,">0",C5:C15,"<500000")
    =AVERAGEIFS(C5:C15,D5:D15,">=2",E5:E15,">1")
    

These formulas return the average price of properties where:

1.  prices are greater than zero
2.  prices are greater than zero and less than $500,000
3.  properties have at least 2 bedrooms and more than 1 bathroom

### Double quotes ("") in criteria

In general, text values in criteria are enclosed in double quotes (""), and numbers are not. However, when a [logical operator](https://exceljet.net/glossary/logical-operators)
 is included with a number, both the number and the operator must be enclosed in quotes. Note the difference in the two examples below. Because the second formula uses the "greater than or equal to" operator (>=), the operator and number are both enclosed in double quotes.

    =AVERAGEIFS(C5:C15,D5:D15,2) // 2 bedrooms
    =AVERAGEIFS(C5:C15,D5:D15,">=2") // 2+ bedrooms
    

Double quotes are also used for text values. For example, to average values in B1:B10 when values in A1:A10 equal "red", you can use a formula like this:

    =AVERAGEIFS(B1:B10,A1:A10,"red")
    

### Multiple criteria

Enter criteria in pairs \[range, criteria\]. For example, to average values in A1:A10, where B1:B10 = "A", _and_ C1:C10 > 5, use:

    =AVERAGEIFS(A1:A10,B1:B10,"A",C1:C10,">5")
    

### Value from another cell

A value from another cell can be included in _criteria_ using [concatenation](https://exceljet.net/glossary/concatenation)
. In the example below, AVERAGEIFS will return the average of numbers in A1:A10 that are less than the value in cell B1. Notice the less than [operator](https://exceljet.net/glossary/logical-operators)
 (which is text) is enclosed in quotes.

    =AVERAGEIFS(A1:A10,A1:A10,"<"&B1) // average values less than  B1
    

### Wildcards

The [wildcard](https://exceljet.net/glossary/wildcard)
 characters question mark (?), asterisk(\*), or tilde (~) can be used in criteria. A question mark (?) matches any one character and an asterisk (\*) matches zero or more characters of any kind.  For example, to average values in B1:B10 when values in A1:A10 _contain_ the text "red", you can use a formula like this:

    =AVERAGEIFS(B1:B10,A1:A10,"*red*")
    

The tilde (~) is an escape character to match literal wildcards. For example, to match a literal question mark (?), an asterisk (\*), or tilde (~), add a tilde in front of the wildcard (i.e. ~?, ~\*, ~~).

_Note: the order of arguments is different between AVERAGEIFS and_ [_AVERAGEIF_](https://exceljet.net/functions/averageif-function)
_. The range to average is always the first argument in AVERAGEIFS._

### Notes

*   All ranges must be the same size, or AVERAGEIFS will return a #VALUE! error.
*   Only values that meet all conditions will be included in the final result.
*   AVERAGEIFS will not include empty cells in the average, even when criteria match.
*   TRUE and FALSE values are ignored when calculating an average.
*   AVERAGEIFS will return a #DIV/0! error if no cells meet criteria.
*   AVERAGEIFS requires a [range](https://exceljet.net/glossary/range)
    , you can't substitute an [array](https://exceljet.net/glossary/array)
    .
*   Logical operators and text values should be enclosed in double quotes ("").
*   AVERAGEIFS supports [wildcards](https://exceljet.net/glossary/wildcard)
     but is not case-sensitive.

AVERAGEIFS function examples
----------------------------

[![Excel formula: Dynamic two-way sum](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20sum.png "Excel formula: Dynamic two-way sum")](https://exceljet.net/formulas/dynamic-two-way-sum)

### [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)

In this example, the goal is to create a formula that performs a dynamic two-way sum of all City and Size combinations in the range B5:D17 . The solution shown requires four basic steps: Create an Excel Table called data List unique cities with the UNIQUE function List unique sizes with the UNIQUE...

[![Excel formula: Dynamic two-way average](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20average.png "Excel formula: Dynamic two-way average")](https://exceljet.net/formulas/dynamic-two-way-average)

### [Dynamic two-way average](https://exceljet.net/formulas/dynamic-two-way-average)

In this example, the goal is to create a formula that performs a dynamic two-way average of all age and gender combinations in the range B5:D16 . The solution shown requires four general steps: Create an Excel Table called data List unique age groups with UNIQUE function List unique genders with...

[![Excel formula: Average call time per month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_call_time_per_month.png "Excel formula: Average call time per month")](https://exceljet.net/formulas/average-call-time-per-month)

### [Average call time per month](https://exceljet.net/formulas/average-call-time-per-month)

In this example, the goal is to calculate the average call time (duration in minutes) for each month listed in column G using the dates in column B and the durations in column E. The article below explains two approaches. The first formula is based on the AVERAGEIFS function , which is designed to...

[![Excel formula: Average numbers ignore zero](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_numbers_ignore_zero.png "Excel formula: Average numbers ignore zero")](https://exceljet.net/formulas/average-numbers-ignore-zero)

### [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)

In this example, the goal is to calculate an average of the quiz scores in columns C, D, E, and F for each person. However, the result needs to ignore any zeros that appear in the data. This formula can be easily solved with the AVERAGEIF function or the AVERAGEIFS function . It can also be solved...

[![Excel formula: Basic average example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic_average_example.png "Excel formula: Basic average example")](https://exceljet.net/formulas/basic-average-example)

### [Basic average example](https://exceljet.net/formulas/basic-average-example)

In this example, the goal is to calculate a quiz score average for each person listed in column D using the four scores in columns C, D, E, and F. The standard way to solve this problem in Excel is to use the AVERAGE function . AVERAGE function The AVERAGE function calculates the average (...

[![Excel formula: Average salary by department](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_salary_by_department.png "Excel formula: Average salary by department")](https://exceljet.net/formulas/average-salary-by-department)

### [Average salary by department](https://exceljet.net/formulas/average-salary-by-department)

In this example, the goal is to create a formula that calculates an average salary by department, where data is an Excel Table in the range B5:D16. The solution shown requires three general steps: Create an Excel Table called data List unique departments with the UNIQUE function Calculate averages...

[![Excel formula: Average by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_by_month.png "Excel formula: Average by month")](https://exceljet.net/formulas/average-by-month)

### [Average by month](https://exceljet.net/formulas/average-by-month)

In this example, the goal is to calculate a monthly average for the amounts shown in column C using the dates in column B. The article below explains two approaches. One approach is based on the AVERAGEIFS function , which is designed to calculate averages using multiple criteria. The second...

[![Excel formula: Average if with filter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Average_if_with_filter.png "Excel formula: Average if with filter")](https://exceljet.net/formulas/average-if-with-filter)

### [Average if with filter](https://exceljet.net/formulas/average-if-with-filter)

In this example, the goal is to calculate an average for any given group ("A", "B", or "C") across all three months of data in the range C5:E16. For convenience only, data (C5:E16) and group (B5:B16) are named ranges . In the article below, we look at several approaches to this problem: Why the...

[![Excel formula: Average by group](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_by_group.png "Excel formula: Average by group")](https://exceljet.net/formulas/average-by-group)

### [Average by group](https://exceljet.net/formulas/average-by-group)

In this example, the goal is to create a formula that calculates an average by group, using the group names in column C. The solution shown requires three general steps: Create an Excel Table called data List unique groups with the UNIQUE function Calculate averages with the AVERAGEIFS function...

[![Excel formula: Average if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_if_not_blank.png "Excel formula: Average if not blank")](https://exceljet.net/formulas/average-if-not-blank)

### [Average if not blank](https://exceljet.net/formulas/average-if-not-blank)

In this example, the goal is to average the Prices in C5:C16 when the Group in D5:D16 is not blank (i.e. not empty). The traditional way to solve this problem is to use the AVERAGEIFS function . However, you can also use the FILTER function with the AVERAGE function , as explained below. Because...

[![Excel formula: Average with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_with_multiple_criteria.png "Excel formula: Average with multiple criteria")](https://exceljet.net/formulas/average-with-multiple-criteria)

### [Average with multiple criteria](https://exceljet.net/formulas/average-with-multiple-criteria)

In this example, the goal is to calculate an average for each group and region in the data as shown in the worksheet. For convenience, data is an Excel Table in the range B5:D16. This problem can be easily solved with the AVERAGEIFS function . Like the COUNTIFS function and SUMIFS function , the...

Related functions
-----------------

[![Excel AVERAGEIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageif.png "Excel AVERAGEIF function")](https://exceljet.net/functions/averageif-function)

### [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)

The Excel AVERAGEIF function calculates the average of numbers in a range that meet supplied criteria. AVERAGEIF criteria can include logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching.

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

*   [Basic average example](https://exceljet.net/formulas/basic-average-example)
    
*   [Average if with filter](https://exceljet.net/formulas/average-if-with-filter)
    
*   [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)
    
*   [Average by group](https://exceljet.net/formulas/average-by-group)
    
*   [Average by month](https://exceljet.net/formulas/average-by-month)
    
*   [Dynamic two-way average](https://exceljet.net/formulas/dynamic-two-way-average)
    
*   [Average if not blank](https://exceljet.net/formulas/average-if-not-blank)
    
*   [Average with multiple criteria](https://exceljet.net/formulas/average-with-multiple-criteria)
    
*   [Average call time per month](https://exceljet.net/formulas/average-call-time-per-month)
    
*   [Average salary by department](https://exceljet.net/formulas/average-salary-by-department)
    

### Functions

*   [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)
    
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

*   [Microsoft AVERAGEIFS function documentation](https://support.office.com/en-us/article/averageifs-function-48910c45-1fc0-4389-a028-f7c5c3001690)
    

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