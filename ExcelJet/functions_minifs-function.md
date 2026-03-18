# Excel MINIFS function | Exceljet

**Source:** https://exceljet.net/functions/minifs-function

---

[Skip to main content](https://exceljet.net/functions/minifs-function#main-content)

[](https://exceljet.net/functions/minifs-function#)

*   [Previous](https://exceljet.net/functions/mina-function)
    
*   [Next](https://exceljet.net/functions/mode-function)
    

Excel 2019

[Statistical](https://exceljet.net/functions#Statistical)

MINIFS Function
===============

by Dave Bruns · Updated 7 Jun 2025

Related functions 
------------------

[MAXIFS](https://exceljet.net/functions/maxifs-function)

[MAX](https://exceljet.net/functions/max-function)

[MIN](https://exceljet.net/functions/min-function)

[SMALL](https://exceljet.net/functions/small-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[AVERAGEIF](https://exceljet.net/functions/averageif-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

![Excel MINIFS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_minifs.png "Excel MINIFS function")

Summary
-------

The Excel MINIFS function returns the smallest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MINIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and text.

Purpose 
--------

Get minimum value with criteria

Return value 
-------------

Minimum value

Syntax
------

    =MINIFS(min_range,range1,criteria1,[range2],[criteria2],...)

*   _min\_range_ - Range of values used to determine minimum.
*   _range1_ - The first range to evaluate.
*   _criteria1_ - The criteria to use on range1.
*   _range2_ - \[optional\] The second range to evaluate.
*   _criteria2_ - \[optional\] The criteria to use on range2.

Using the MINIFS function 
--------------------------

The MINIFS function returns the smallest numeric value in cells that meet multiple conditions, referred to as _criteria_. Each condition is provided with a separate _range_ and _criteria_. To define criteria, MINIFS supports various [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?,~). The syntax used to apply criteria in MINIFS is a bit tricky because it is unusual in Excel. See below for details.

### Key features

*   Can handle up to 126 conditions.
*   Each new condition requires a separate _range_ and _criteria_.
*   To be included in the final result, _all conditions must be TRUE._
*   Returns zero (0) when no cells meet the supplied criteria.
*   Automatically ignores _empty cells_ that meet supplied criteria.
*   Returns a #VALUE! error if _criteria\_range_ is not the same size as _max\_range._

> Unlike most other Excel functions, MINIFS requires an actual range for min/criteria ranges. If you try to use an [array](https://exceljet.net/glossary/array)
> , Excel will not let you enter the formula. 

### Syntax

The syntax for the MINIFS function depends on the criteria being evaluated. Each condition is provided with a separate _range_ and _criteria_. The generic syntax for MINIFS looks like this:

    =MINIFS(min_range,range1,criteria1) // 1 condition
    =MINIFS(min_range,range1,criteria1,range2,criteria2) // 2 conditions

The MINIFS function takes three required [arguments](https://exceljet.net/glossary/function-argument)
: _min\_range_, _range1_, and _criteria1_. With these three arguments, MINIFS returns the minimum number in _min\_range_ where corresponding cells in _range1_ meet the condition set by _criteria1_. Additional conditions are applied using range/criteria pairs. The second condition is defined by _range2_ and _criteria2_, the third condition is _range3_ and _criteria3_, and so on. MINIFS can handle up to 126 range/criteria pairs. 

### Criteria

The MINIFS function supports logical operators (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. Because MINIFS is in a group of [eight functions](https://exceljet.net/articles/excels-racon-functions)
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
 with the ampersand (&) character. When a _criteria_ argument includes a value from another cell, or the result of a formula, logical operators like "<" must be joined with concatenation. This is because Excel needs to evaluate cell references and formulas first to get a value before that value can be joined to an operator.

### Basic example

In the worksheet shown above, the formulas in G5 and G6 are:

    =MINIFS(D5:D16,C5:C16,"F") // returns 72
    =MINIFS(D5:D16,C5:C16,"M") // returns 64
    

In the first formula, MINIFS returns the minimum value in D5:D16 where C5:C16 is equal to "F" (72). In the second formula, MINIFS returns the minimum value in D5:D16 where C5:C16 is equal to "M" (64).

### Two criteria

In the example below, the MINIFS function is used with two criteria, one for Gender and one for Group. Note conditions are added in range/criteria pairs. The range E5:E16 is paired with the condition "B".

![Example of MINIFS function with two criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/minifs%20function%20with%20two%20criteria.png?itok=9dFSlGr4 "Example of MINIFS function with two criteria")

The formulas in H5:I6 are:

    =MINIFS(D5:D16,C5:C16,"F",E5:E16,"A") // returns 72
    =MINIFS(D5:D16,C5:C16,"F",E5:E16,"B") // returns 83
    =MINIFS(D5:D16,C5:C16,"M",E5:E16,"A") // returns 65
    =MINIFS(D5:D16,C5:C16,"M",E5:E16,"B") // returns 64
    

### Other criteria

To return the minimum value in A1:A100 when cells in B1:B100 are greater than 50:

    =MINIFS(A1:A100,B1:B100,">50")
    

To get the minimum value in A1:A100 when cells in B1:B100 are less than or equal to 100, and cells in C1:C100 are greater than zero:

    =MINIFS(A1:A100,B1:B100,"<=100",C1:C100,">0")
    

### Not equal to

To construct "not equal to" criteria, use the "<>" [operator](https://exceljet.net/glossary/logical-operators)
 surrounded by double quotes (""). For example, to return the minimum value in A1:A100 when cells in B1:B100 are not equal to "red":

    =MINIFS(A1:A100,B1:B100,"<>red")
    

### Value from another cell

When using a value from another cell in a condition, the cell reference must be [concatenated](https://exceljet.net/glossary/concatenation)
 to the operator. For example, to return the minimum value in A1:A100 when cells in B1:B100 are greater than the value in C1:

    =MINIFS(A1:A100,B1:B100,">"&C1)
    

Notice the greater than [operator](https://exceljet.net/glossary/logical-operators)
 (>) is enclosed in quotes (""), but the cell reference (C1) is not.

### Wildcards

The [wildcard](https://exceljet.net/glossary/wildcard)
 characters question mark (?), asterisk(\*), or tilde (~) can be used in _criteria_. A question mark (?) matches any one character, and an asterisk (\*) matches zero or more characters. For example, to return the minimum value in A1:A100 when cells in B1:B100 begin with "a":

    =MINIFS(A1:A100,B1:B100,"a*")
    

The tilde (~) is an escape character that allows you to find literal wildcards. For example, to match a literal question mark (?), an asterisk (\*), or a tilde (~), add a tilde in front of the wildcard (i.e. ~?, ~\*, ~~).

### Notes

*   Conditions are applied using range/criteria pairs.
*   MINIFS will return a #VALUE error if any criteria range is not the same size as _min\_range._
*   If no criteria match, MINIFS will return zero (0).
*   MINIFS ignores empty cells that meet criteria.

MINIFS function examples
------------------------

[![Excel formula: First in last out times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first_in_last_out_time.png "Excel formula: First in last out times")](https://exceljet.net/formulas/first-in-last-out-times)

### [First in last out times](https://exceljet.net/formulas/first-in-last-out-times)

In this problem, the goal is to find the first (earliest) time in and the last (latest) time out for a given name. This is essentially a lookup problem and the solution shown in the worksheet is an example of how you can sometimes use minimum and maximum functions to perform lookups. This works...

[![Excel formula: Minimum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value_if_0.png "Excel formula: Minimum value if")](https://exceljet.net/formulas/minimum-value-if)

### [Minimum value if](https://exceljet.net/formulas/minimum-value-if)

In this example, the goal is to get the minimum value for each group in the data as shown. The easiest way to solve this problem is with the MINIFS function. However, there are actually several options. If you need more flexibility (you need to work with arrays instead of ranges), you can use the...

[![Excel formula: Minimum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value.png "Excel formula: Minimum value")](https://exceljet.net/formulas/minimum-value)

### [Minimum value](https://exceljet.net/formulas/minimum-value)

In this example, the goal is to get the minimum quiz score (i.e. the lowest quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MIN function or the SMALL function, as explained below. MIN function The MIN function...

[![Excel formula: Minimum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_if_multiple_criteria.png "Excel formula: Minimum if multiple criteria")](https://exceljet.net/formulas/minimum-if-multiple-criteria)

### [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)

In this example, the goal is to get the minimum value for a given group above a specific temperature. In other words, we want the min value after applying multiple criteria. The easiest way to solve this problem is with the MINIFS function. However, if you need more flexibility (for example, you...

[![Excel formula: Get earliest and latest project dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20earliest%20and%20latest%20project%20dates.png "Excel formula: Get earliest and latest project dates")](https://exceljet.net/formulas/get-earliest-and-latest-project-dates)

### [Get earliest and latest project dates](https://exceljet.net/formulas/get-earliest-and-latest-project-dates)

The MINIFS function returns the smallest numeric value that meets supplied criteria, and the MAXIFS function returns the largest numeric value that meets supplied criteria. Like COUNTIFS and SUMIFS, these functions use range/criteria "pairs" to apply conditions. For both formulas, we need just one...

[![Excel formula: Get next scheduled event](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20next%20scheduled%20event.png "Excel formula: Get next scheduled event")](https://exceljet.net/formulas/get-next-scheduled-event)

### [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)

The first part of the solution uses the MIN and TODAY functions to find the "next date" based on the date today. This is done by filtering the dates through the IF function: IF((date>=TODAY()),date) The logical test generates an array of TRUE / FALSE values, where TRUE corresponds to dates greater...

Related functions
-----------------

[![Excel MAXIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxifs%20function.png "Excel MAXIFS function")](https://exceljet.net/functions/maxifs-function)

### [MAXIFS Function](https://exceljet.net/functions/maxifs-function)

The Excel MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MAXIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and...

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

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

[![Excel AVERAGEIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageif.png "Excel AVERAGEIF function")](https://exceljet.net/functions/averageif-function)

### [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)

The Excel AVERAGEIF function calculates the average of numbers in a range that meet supplied criteria. AVERAGEIF criteria can include logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching.

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Minimum value](https://exceljet.net/formulas/minimum-value)
    
*   [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)
    
*   [Get earliest and latest project dates](https://exceljet.net/formulas/get-earliest-and-latest-project-dates)
    
*   [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)
    
*   [First in last out times](https://exceljet.net/formulas/first-in-last-out-times)
    
*   [Minimum value if](https://exceljet.net/formulas/minimum-value-if)
    

### Functions

*   [MAXIFS Function](https://exceljet.net/functions/maxifs-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)
    
*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

### Links

*   [Microsoft MINIFS function documentation](https://support.office.com/en-us/article/minifs-function-6ca1ddaa-079b-4e74-80cc-72eef32e6599)
    

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