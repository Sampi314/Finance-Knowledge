# Maximum value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/maximum-value

---

[Skip to main content](https://exceljet.net/formulas/maximum-value#main-content)

[](https://exceljet.net/formulas/maximum-value#)

*   [Previous](https://exceljet.net/formulas/maximum-if-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/maximum-value-if)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Maximum value
=============

by Dave Bruns · Updated 19 Mar 2023

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[MAXIFS](https://exceljet.net/functions/maxifs-function)

[LARGE](https://exceljet.net/functions/large-function)

![Excel formula: Maximum value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/maximum_value.png "Excel formula: Maximum value")

Summary
-------

To get the maximum value in a set of data, you can use the [MAX function](https://exceljet.net/functions/max-function)
. In the example shown, the formula in cell I5 is:

    =MAX(C5:G5)
    

As the formula is copied down, it returns the top quiz score for each person listed in column B. 

Generic formula
---------------

    =MAX(range)

Explanation 
------------

In this example, the goal is to get the maximum quiz score (i.e. the best quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MAX function or the LARGE function, as explained below.

### MAX function

The [MAX function](https://exceljet.net/functions/max-function)
 accepts one or more [arguments](https://exceljet.net/glossary/function-argument)
, which can be a mix of constants, cell references, and [ranges](https://exceljet.net/glossary/range)
. MAX will return the maximum value in the data provided. Text values and empty cells are ignored.

In this example, each student has five test scores in the same row, and the goal is to get the maximum score for each student. Because the quiz scores are all together, the data is supplied to MAX as a single range. The formula in I5 is:

    =MAX(C5:G5)
    

As the formula is copied down the table, MAX returns the highest score for each student. MAX is fully automatic. If data changes, MAX will automatically recalculate. Note that the MAX function will automatically ignore empty cells, but it will return an error if the data contains an error. To calculate a maximum value while ignoring errors, [see this example](https://exceljet.net/formulas/max-value-ignore-all-errors)
.

### LARGE function

The [LARGE function](https://exceljet.net/functions/large-function)
 can also be used to return the maximum value in a set of data. The generic syntax for LARGE looks like this:

    =LARGE(range,n)
    

where **n** is a number like 1, 2, 3, etc. For example, you can retrieve the first, second, and third largest values like this:

    =LARGE(range,1) // first largest
    =LARGE(range,2) // second largest
    =LARGE(range,3) // third largest

In this example, you could use LARGE to get the best quiz score for each person like this:

    =LARGE(C5:G5,1)

The LARGE function is especially useful when you want to get other nth largest values, [as seen in this example](https://exceljet.net/formulas/nth-largest-value)
.

### Notes

*   To get a max value with one or more criteria, see the [MAXIFS function](https://exceljet.net/functions/maxifs-function)
    . You can also use the FILTER function with the MAX function, as [explained here](https://exceljet.net/formulas/maximum-value-if)
    .
*   To get the nth largest value in a set of data (i.e. 1st largest, 2nd largest, 3rd largest, etc.), see the [LARGE function](https://exceljet.net/functions/large-function)
    .

Related formulas
----------------

[![Excel formula: Maximum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value_if.png "Excel formula: Maximum value if")](https://exceljet.net/formulas/maximum-value-if)

### [Maximum value if](https://exceljet.net/formulas/maximum-value-if)

In this example, the goal is to get the maximum value for each group in the data as shown. The easiest way to solve this problem is with the MAXIFS function. However, there are actually several options. If you need more flexibility (i.e. you need to work with arrays and not ranges), you can use the...

[![Excel formula: Minimum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value.png "Excel formula: Minimum value")](https://exceljet.net/formulas/minimum-value)

### [Minimum value](https://exceljet.net/formulas/minimum-value)

In this example, the goal is to get the minimum quiz score (i.e. the lowest quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MIN function or the SMALL function, as explained below. MIN function The MIN function...

[![Excel formula: Minimum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value_if_0.png "Excel formula: Minimum value if")](https://exceljet.net/formulas/minimum-value-if)

### [Minimum value if](https://exceljet.net/formulas/minimum-value-if)

In this example, the goal is to get the minimum value for each group in the data as shown. The easiest way to solve this problem is with the MINIFS function. However, there are actually several options. If you need more flexibility (you need to work with arrays instead of ranges), you can use the...

[![Excel formula: Minimum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_if_multiple_criteria.png "Excel formula: Minimum if multiple criteria")](https://exceljet.net/formulas/minimum-if-multiple-criteria)

### [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)

In this example, the goal is to get the minimum value for a given group above a specific temperature. In other words, we want the min value after applying multiple criteria. The easiest way to solve this problem is with the MINIFS function. However, if you need more flexibility (for example, you...

[![Excel formula: Maximum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_if_multiple_criteria.png "Excel formula: Maximum if multiple criteria")](https://exceljet.net/formulas/maximum-if-multiple-criteria)

### [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)

In this example, the goal is to get the maximum value for a given group below a specific temperature. In other words, we want the max value after applying multiple criteria. The easiest way to solve this problem is with the MAXIFS function. However, if you need more flexibility (i.e., you need to...

[![Excel formula: Get next scheduled event](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20next%20scheduled%20event.png "Excel formula: Get next scheduled event")](https://exceljet.net/formulas/get-next-scheduled-event)

### [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)

The first part of the solution uses the MIN and TODAY functions to find the "next date" based on the date today. This is done by filtering the dates through the IF function: IF((date>=TODAY()),date) The logical test generates an array of TRUE / FALSE values, where TRUE corresponds to dates greater...

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MAXIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxifs%20function.png "Excel MAXIFS function")](https://exceljet.net/functions/maxifs-function)

### [MAXIFS Function](https://exceljet.net/functions/maxifs-function)

The Excel MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MAXIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and...

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Maximum value if](https://exceljet.net/formulas/maximum-value-if)
    
*   [Minimum value](https://exceljet.net/formulas/minimum-value)
    
*   [Minimum value if](https://exceljet.net/formulas/minimum-value-if)
    
*   [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)
    
*   [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)
    
*   [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MAXIFS Function](https://exceljet.net/functions/maxifs-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    

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