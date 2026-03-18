# Excel MAXIFS function | Exceljet

**Source:** https://exceljet.net/functions/maxifs-function

---

[Skip to main content](https://exceljet.net/functions/maxifs-function#main-content)

[](https://exceljet.net/functions/maxifs-function#)

*   [Previous](https://exceljet.net/functions/maxa-function)
    
*   [Next](https://exceljet.net/functions/median-function)
    

Excel 2019

[Statistical](https://exceljet.net/functions#Statistical)

MAXIFS Function
===============

by Dave Bruns · Updated 7 Jun 2025

Related functions 
------------------

[MINIFS](https://exceljet.net/functions/minifs-function)

[MIN](https://exceljet.net/functions/min-function)

[MAX](https://exceljet.net/functions/max-function)

[LARGE](https://exceljet.net/functions/large-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[AVERAGEIF](https://exceljet.net/functions/averageif-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

![Excel MAXIFS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20maxifs%20function.png "Excel MAXIFS function")

Summary
-------

The Excel MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MAXIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and text.

Purpose 
--------

Get maximum value with criteria

Return value 
-------------

Maximum value

Syntax
------

    =MAXIFS(max_range,range1,criteria1,[range2],[criteria2],...)

*   _max\_range_ - Range of values used to determine maximum.
*   _range1_ - The first range to evaluate.
*   _criteria1_ - The criteria to use on range1.
*   _range2_ - \[optional\] The second range to evaluate.
*   _criteria2_ - \[optional\] The criteria to use on range2.

Using the MAXIFS function 
--------------------------

The MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as _criteria_. Each condition is provided with a separate _range_ and _criteria_. To define criteria, MAXIFS supports various [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?,~). The syntax used to apply criteria in MAXIFS is a bit tricky because it is unusual in Excel. See below for details.

### Key features

*   Can handle up to 126 conditions.
*   Each new condition requires a separate _range_ and _criteria_.
*   To be included in the final result, _all conditions must be TRUE._
*   Returns zero (0) when no cells meet the supplied criteria.
*   Automatically ignores _empty cells_ that meet supplied criteria.
*   Returns a #VALUE! error if _criteria\_range_ is not the same size as _max\_range._

> Unlike most other Excel functions, MAXIFS requires an actual range for max/criteria ranges. If you try to use an [array](https://exceljet.net/glossary/array)
> , Excel will not let you enter the formula. 

### Syntax

The syntax for the MAXIFS function depends on the criteria being evaluated. Each condition is provided with a separate _range_ and _criteria_. The generic syntax for MAXIFS looks like this:

    =MAXIFS(max_range,range1,criteria1) // 1 condition
    =MAXIFS(max_range,range1,criteria1,range2,criteria2) // 2 conditions

The MAXIFS function takes three required [arguments](https://exceljet.net/glossary/function-argument)
: _max\_range_, _range1_, and _criteria1_. With these three arguments, MAXIFS returns the maximum number in _max\_range_ where corresponding cells in _range1_ meet the condition set by _criteria1_. Additional conditions are applied using range/criteria pairs. The second condition is defined by _range2_ and _criteria2_, the third condition is _range3_ and _criteria3_, and so on. MAXIFS can handle up to 126 range/criteria pairs. 

### Criteria

The MAXIFS function supports logical operators (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. Because MAXIFS is in a group of [eight functions](https://exceljet.net/articles/excels-racon-functions)
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

### Basic Example

In the worksheet shown above, the formulas in G5 and G6 are:

    =MAXIFS(D5:D16,C5:C16,"F") // returns 93
    =MAXIFS(D5:D16,C5:C16,"M") // returns 83
    

In the first formula, MAXIFS returns the maximum value in D5:D16 where C5:C16 is equal to "F" (93). In the second formula, MAXIFS returns the maximum value in D5:D16 where C5:C16 is equal to "M" (83).

### Two criteria

In the example below, the MAXIFS function is used with two criteria, one for Gender and one for Group. Note conditions are added in range/criteria pairs. The range E5:E16 is paired with the condition "B".

![Example of MAXIFS function with two criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet%20maxifs%20with%20two%20criteria.png?itok=u7qFRlPs "Example of MAXIFS function with two criteria")

The formulas in H5:I6 are:

    H5=MAXIFS(D5:D16,C5:C16,"F",E5:E16,"A") // returns 93
    I5=MAXIFS(D5:D16,C5:C16,"F",E5:E16,"B") // returns 85
    H6=MAXIFS(D5:D16,C5:C16,"M",E5:E16,"A") // returns 83
    I6=MAXIFS(D5:D16,C5:C16,"M",E5:E16,"B") // returns 79
    

### Other criteria

To return the maximum value in A1:A100 when cells in B1:B100 are greater than 50:

    =MAXIFS(A1:A100,B1:B100,">50")
    

To get the maximum value in A1:A100 when cells in B1:B100 are less than or equal to 100, and cells in C1:C100 are greater than zero:

    =MAXIFS(A1:A100,B1:B100,"<=100",C1:C100,">0")
    

### Not equal to

To construct "not equal to" criteria, use the "<>" [operator](https://exceljet.net/glossary/logical-operators)
 surrounded by double quotes (""). For example, to return the maximum value in A1:A100 when cells in B1:B100 are not equal to "red":

    =MAXIFS(A1:A100,B1:B100,"<>red")
    

### Value from another cell

When using a value from another cell in a condition, the cell reference must be [concatenated](https://exceljet.net/glossary/concatenation)
 to the operator. For example, to return the maximum value in A1:A100 when cells in B1:B100 are greater than the value in C1:

    =MAXIFS(A1:A100,B1:B100,">"&C1)
    

Notice the greater than [operator](https://exceljet.net/glossary/logical-operators)
 (>) is enclosed in quotes (""), but the cell reference (C1) is not.

### Wildcards

The [wildcard](https://exceljet.net/glossary/wildcard)
 characters question mark (?), asterisk(\*), or tilde (~) can be used in _criteria_. A question mark (?) matches any one character, and an asterisk (\*) matches zero or more characters. For example, to return the maximum value in A1:A100 when cells in B1:B100 begin with "a":

    =MAXIFS(A1:A100,B1:B100,"a*")
    

The tilde (~) is an escape character to allow you to find literal wildcards. For example, to match a literal question mark (?), asterisk(\*), or tilde (~), add a tilde in front of the wildcard (i.e. ~?, ~\*, ~~).

### Notes

*   Conditions are applied using range/criteria pairs.
*   MAXIFS will return a #VALUE error if any criteria range is not the same size as _max\_range._
*   If no criteria match, MAXIFS will return zero (0).
*   MAXIFS ignores empty cells that meet criteria.

MAXIFS function examples
------------------------

[![Excel formula: Get earliest and latest project dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20earliest%20and%20latest%20project%20dates.png "Excel formula: Get earliest and latest project dates")](https://exceljet.net/formulas/get-earliest-and-latest-project-dates)

### [Get earliest and latest project dates](https://exceljet.net/formulas/get-earliest-and-latest-project-dates)

The MINIFS function returns the smallest numeric value that meets supplied criteria, and the MAXIFS function returns the largest numeric value that meets supplied criteria. Like COUNTIFS and SUMIFS, these functions use range/criteria "pairs" to apply conditions. For both formulas, we need just one...

[![Excel formula: Max by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_by_month.png "Excel formula: Max by month")](https://exceljet.net/formulas/max-by-month)

### [Max by month](https://exceljet.net/formulas/max-by-month)

In this example, the goal is to get the maximum value in the data for each month listed in column E. The easiest way to do this is with the MAXIFS function, which is designed to return a maximum value based on one or more criteria. In older versions of Excel without the MAXIFS function, you can use...

[![Excel formula: Maximum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_if_multiple_criteria.png "Excel formula: Maximum if multiple criteria")](https://exceljet.net/formulas/maximum-if-multiple-criteria)

### [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)

In this example, the goal is to get the maximum value for a given group below a specific temperature. In other words, we want the max value after applying multiple criteria. The easiest way to solve this problem is with the MAXIFS function. However, if you need more flexibility (i.e., you need to...

[![Excel formula: Maximum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value.png "Excel formula: Maximum value")](https://exceljet.net/formulas/maximum-value)

### [Maximum value](https://exceljet.net/formulas/maximum-value)

In this example, the goal is to get the maximum quiz score (i.e. the best quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MAX function or the LARGE function, as explained below. MAX function The MAX function accepts...

[![Excel formula: Max if criteria match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max%20if%20criteria%20match.png "Excel formula: Max if criteria match")](https://exceljet.net/formulas/max-if-criteria-match)

### [Max if criteria match](https://exceljet.net/formulas/max-if-criteria-match)

The example shown contains almost 10,000 rows of data. The data represents temperature readings taken every 2 minutes over a period of days. For any given date (provided in cell H7), we want to get the maximum temperature on that date. Inside the IF function , logical test is entered as B5:B9391=H7...

[![Excel formula: Maximum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value_if.png "Excel formula: Maximum value if")](https://exceljet.net/formulas/maximum-value-if)

### [Maximum value if](https://exceljet.net/formulas/maximum-value-if)

In this example, the goal is to get the maximum value for each group in the data as shown. The easiest way to solve this problem is with the MAXIFS function. However, there are actually several options. If you need more flexibility (i.e. you need to work with arrays and not ranges), you can use the...

[![Excel formula: Max value ignore all errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_value_ignore_all_errors.png "Excel formula: Max value ignore all errors")](https://exceljet.net/formulas/max-value-ignore-all-errors)

### [Max value ignore all errors](https://exceljet.net/formulas/max-value-ignore-all-errors)

In this example, the goal is to return the maximum value in a set of data while ignoring any errors that might exist. This problem can be solved with the AGGREGATE function or with the MAXIFS function, as explained below. MAX with errors The standard way to retrieve the maximum value in a range of...

[![Excel formula: First in last out times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first_in_last_out_time.png "Excel formula: First in last out times")](https://exceljet.net/formulas/first-in-last-out-times)

### [First in last out times](https://exceljet.net/formulas/first-in-last-out-times)

In this problem, the goal is to find the first (earliest) time in and the last (latest) time out for a given name. This is essentially a lookup problem and the solution shown in the worksheet is an example of how you can sometimes use minimum and maximum functions to perform lookups. This works...

Related functions
-----------------

[![Excel MINIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_minifs.png "Excel MINIFS function")](https://exceljet.net/functions/minifs-function)

### [MINIFS Function](https://exceljet.net/functions/minifs-function)

The Excel MINIFS function returns the smallest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MINIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers,...

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

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

*   [Max if criteria match](https://exceljet.net/formulas/max-if-criteria-match)
    
*   [Get earliest and latest project dates](https://exceljet.net/formulas/get-earliest-and-latest-project-dates)
    
*   [Maximum value if](https://exceljet.net/formulas/maximum-value-if)
    
*   [Max by month](https://exceljet.net/formulas/max-by-month)
    
*   [Max value ignore all errors](https://exceljet.net/formulas/max-value-ignore-all-errors)
    
*   [First in last out times](https://exceljet.net/formulas/first-in-last-out-times)
    
*   [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)
    
*   [Maximum value](https://exceljet.net/formulas/maximum-value)
    

### Functions

*   [MINIFS Function](https://exceljet.net/functions/minifs-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)
    
*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

### Links

*   [Microsoft MAXIFS function documentation](https://support.office.com/en-us/article/maxifs-function-dfd611e6-da2c-488a-919b-9b6376b28883)
    

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