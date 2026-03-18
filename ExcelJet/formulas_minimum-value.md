# Minimum value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/minimum-value

---

[Skip to main content](https://exceljet.net/formulas/minimum-value#main-content)

[](https://exceljet.net/formulas/minimum-value#)

*   [Previous](https://exceljet.net/formulas/minimum-if-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/minimum-value-if)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Minimum value
=============

by Dave Bruns · Updated 20 Mar 2023

Related functions 
------------------

[MIN](https://exceljet.net/functions/min-function)

[MINIFS](https://exceljet.net/functions/minifs-function)

[SMALL](https://exceljet.net/functions/small-function)

![Excel formula: Minimum value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/minimum_value.png "Excel formula: Minimum value")

Summary
-------

To get the minimum value in a set of data, you can use the [MIN function](https://exceljet.net/functions/min-function)
. In the example shown, the formula in cell I5 is:

    =MIN(C5:G5)
    

As the formula is copied down, it returns the lowest quiz score for each person listed in column B. 

Generic formula
---------------

    =MIN(range)

Explanation 
------------

In this example, the goal is to get the minimum quiz score (i.e. the lowest quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MIN function or the SMALL function, as explained below.

### MIN function

The [MIN function](https://exceljet.net/functions/min-function)
 accepts one or more [arguments](https://exceljet.net/glossary/function-argument)
, which can be a mix of constants, cell references, and [ranges](https://exceljet.net/glossary/range)
. MIN will return the minimum value in the data provided. Text values and empty cells are ignored.

In this example, each student has five test scores in the same row, and the goal is to get the minimum score for each student. Because the quiz scores are all together, the data is supplied to MIN as a single range. The formula in I5 is:

    =MIN(C5:G5)
    

As the formula is copied down the table, MIN returns the lowest score for each student. MIN is fully automatic. If data changes, MIN will automatically recalculate. Note that the MIN function will ignore empty cells, but it will return an error if the data contains an error. To calculate a minimum value while ignoring errors you can adapt the formula approach [explained here](https://exceljet.net/formulas/max-value-ignore-all-errors)
.

### SMALL function

The [SMALL function](https://exceljet.net/functions/small-function)
 can also be used to return the minimum value in a set of data. The generic syntax for SMALL looks like this:

    =SMALL(range,n)
    

where **n** is a number like 1, 2, 3, etc. For example, you can retrieve the first, second, and third smallest values like this:

    =SMALL(range,1) // first smallest
    =SMALL(range,2) // second smallest
    =SMALL(range,3) // third smallest

In this example, you could use SMALL to get the minimum quiz score for each person like this:

    =SMALL(C5:G5,1)

The SMALL function is especially useful when you want to get other nth smallest values, [as seen in this example](https://exceljet.net/formulas/nth-smallest-value)
.

### Notes

*   To get a minimum value with one or more criteria, see the [MINIFS function](https://exceljet.net/functions/minifs-function)
    . You can also use the FILTER function with the MIN function, as [explained here](https://exceljet.net/formulas/minimum-value-if)
    .
*   To get the nth smallest value in a set of data (i.e. 1st smallest, 2nd smallest, 3rd smallest, etc.), see the [SMALL function](https://exceljet.net/functions/small-function)
    .

Related formulas
----------------

[![Excel formula: Minimum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value_if_0.png "Excel formula: Minimum value if")](https://exceljet.net/formulas/minimum-value-if)

### [Minimum value if](https://exceljet.net/formulas/minimum-value-if)

In this example, the goal is to get the minimum value for each group in the data as shown. The easiest way to solve this problem is with the MINIFS function. However, there are actually several options. If you need more flexibility (you need to work with arrays instead of ranges), you can use the...

[![Excel formula: Maximum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value.png "Excel formula: Maximum value")](https://exceljet.net/formulas/maximum-value)

### [Maximum value](https://exceljet.net/formulas/maximum-value)

In this example, the goal is to get the maximum quiz score (i.e. the best quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MAX function or the LARGE function, as explained below. MAX function The MAX function accepts...

[![Excel formula: Maximum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value_if.png "Excel formula: Maximum value if")](https://exceljet.net/formulas/maximum-value-if)

### [Maximum value if](https://exceljet.net/formulas/maximum-value-if)

In this example, the goal is to get the maximum value for each group in the data as shown. The easiest way to solve this problem is with the MAXIFS function. However, there are actually several options. If you need more flexibility (i.e. you need to work with arrays and not ranges), you can use the...

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

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MINIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_minifs.png "Excel MINIFS function")](https://exceljet.net/functions/minifs-function)

### [MINIFS Function](https://exceljet.net/functions/minifs-function)

The Excel MINIFS function returns the smallest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MINIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers,...

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20maximum%20and%20minimum%20values-thumb.png)](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

### [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

In this video we'll look at how to calculate minimum and maximum values in Excel. Let's take a look. Here we have a list of properties, that includes an address, a price, and a variety of other information. Let's calculate the maximum and minimum values in this list. First, I'm going to create a...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Minimum value if](https://exceljet.net/formulas/minimum-value-if)
    
*   [Maximum value](https://exceljet.net/formulas/maximum-value)
    
*   [Maximum value if](https://exceljet.net/formulas/maximum-value-if)
    
*   [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)
    
*   [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)
    
*   [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)
    

### Functions

*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [MINIFS Function](https://exceljet.net/functions/minifs-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    

### Videos

*   [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)
    

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