# SUMIFS with multiple criteria and OR logic - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic

---

[Skip to main content](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic#main-content)

[](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic#)

*   [Previous](https://exceljet.net/formulas/sumifs-with-horizontal-range)
    
*   [Next](https://exceljet.net/formulas/sumproduct-with-if)
    

[Sum](https://exceljet.net/formulas#Sum)

SUMIFS with multiple criteria and OR logic
==========================================

by Dave Bruns · Updated 7 Dec 2025

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: SUMIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/SUMIFS_with_multiple_criteria_and_OR_logic.png "Excel formula: SUMIFS with multiple criteria and OR logic")

Summary
-------

To sum based on multiple criteria using OR logic, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 with an [array constant](https://exceljet.net/glossary/array-constant)
. In the example shown, the formula in H7 is:

    =SUM(SUMIFS(E5:E16,D5:D16,{"complete","pending"}))
    

The result is $200, the total of all orders with a status of "Complete" or "Pending". Note that the SUMIFS function is _not_ case-sensitive.

Generic formula
---------------

    =SUM(SUMIFS(sum_range,criteria_range,{"red","blue"}))

Explanation 
------------

In this example, the goal is to sum the value of orders that have a status of "Complete" or "Pending". This is a slightly tricky problem in Excel because the SUMIFS function is designed for conditional sums based on multiple criteria, but all criteria must be TRUE in order for a value to be included in the sum. In other words, the criteria used in the SUMIFS function are joined with AND logic, not OR logic. In simple scenarios, an easy solution is to use the SUMIFS function with an array constant. 

### SUMIFS function

The SUMIFS function sums the values in a range that meet multiple criteria. It is similar to the SUMIF function, which only allows a single condition, but SUMIFS allows multiple criteria, using AND logic. This can be illustrated with the following formulas:

    =SUMIFS(E5:E16,D5:D16,"complete") // returns 150
    =SUMIFS(E5:E16,D5:D16,"pending") // returns 50
    =SUMIFS(E5:E16,D5:D16,"complete",D5:D16,"pending") // returns 0

Notice the first two formulas correctly return the total of complete and pending orders, but the last formula returns zero because an order cannot be "Complete" and "Pending" at the same time. This is because the SUMIFS function only allows AND logic – _all conditions must be TRUE_ for a value to be included in the sum.

### SUMIFS + SUMIFS

One straightforward solution is to use SUMIFS twice in a formula like this:

    =SUMIFS(E5:E16,D5:D16,"complete")+SUMIFS(E5:E16,D5:D16,"pending")

This formula returns a correct result of $200, but it is redundant and doesn't scale well.

### SUMIFS + array constant

Another option is to supply SUMIFS with an [array constant](https://exceljet.net/glossary/array-constant)
 that holds more than one condition, like this:

    =SUMIFS(E5:E16,D5:D16,{"complete","pending"}) // returns {150,50}

Through a formula behavior called "[lifting](https://exceljet.net/glossary/lifting)
", this will cause SUMIFS to be evaluated twice, once for "complete" and once for "pending", and SUMIFS will return _two_ results in an array like this:

    {150,50}

If you enter the formula above in the latest version of Excel, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you will see both results [spill](https://exceljet.net/glossary/spill)
 into a range that contains two cells. Because we want a _single_ result, we [nest](https://exceljet.net/glossary/nesting)
 the SUMIFS function in the SUM function like this:

    =SUM(SUMIFS(E5:E16,D5:D16,{"complete","pending"}))

This is the formula used in the worksheet shown. The formula evaluates like this:

    =SUM(SUMIFS(E5:E16,D5:D16,{"complete","pending"}))
    =SUM({150,50})
    =200

The SUMIFS function returns two results in an array: 250 and 50. This array is returned to the SUM function, which returns a final result of 200.

### With wildcards

You can use wildcards in the criteria if needed. For example, to sum items that contain "red" or "blue" anywhere in the _criteria\_range_, you can use:

    =SUM(SUMIFS(sum_range,criteria_range,{"*red*","*blue*"}))
    

### Adding more conditions

You can add more conditions to this formula, but you'll need to use a [horizontal array](https://exceljet.net/glossary/array)
 for one set of criteria and a _vertical_ array for the other. So, for example, to sum orders that are "Complete" or "Pending", when the customer is "Andy Garcia" or "Bob Jones", you can use a formula like this:

    =SUM(SUMIFS(E4:E16,D4:D16,{"complete","pending"},C4:C16,{"Bob Jones";"Andy Garcia"}))
    

Note the semicolons in the second [array constant](https://exceljet.net/glossary/array-constant)
 represent a _vertical_ array. This works because Excel "pairs" elements in the two array constants and returns a two-dimensional array of results. To apply additional criteria, you will want to move to a [formula based on SUMPRODUCT](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
.

### Cell references for criteria

You can't use cell references inside an array constant; you must use a proper range. When you switch from array constants to ranges, the formula becomes an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 in older versions of Excel and must be entered with control + shift + enter:

    ={SUM(SUMIFS(range1,range2,range3))}
    

Where _range1_ is the sum range, _range2_ is the criteria range, and _range3_ contains multiple criteria on the worksheet. With two OR criteria, you'll need to use horizontal and vertical arrays as explained above.

> Note: this formula will work fine in modern versions of Excel that support [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  without special handling. In Exceln 2019 or older, you will need to enter the formula as an array formula with Ctrl + Shift + Enter.

Related formulas
----------------

[![Excel formula: COUNTIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/COUNTIFS%20with%20multiple%20criteria%20and%20OR%20logic.png "Excel formula: COUNTIFS with multiple criteria and OR logic")](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

### [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

In this example, the goal is to use the COUNTIFS function to count data with "OR logic". The challenge is the COUNTIFS function applies AND logic by default. COUNTIFS function The COUNTIFS function returns the count of cells that meet one or more criteria, and supports logical operators (>,...

[![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")](https://exceljet.net/formulas/sum-if-x-or-y)

### [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an Excel Table named data . This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the SUMIFS function . However, when...

[![Excel formula: SUMPRODUCT count multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT%20count%20multiple%20OR%20criteria2.png "Excel formula: SUMPRODUCT count multiple OR criteria")](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

### [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

In this example, the goal is to count rows where the value in column one is "A" or "B" and the value in column two is "X", "Y", or "Z". In the worksheet shown, we are using array constants to hold the values of interest, but the article also shows how to use cell references instead. In simple...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    
*   [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    

### Training

*   [Core Excel](https://exceljet.net/training/core-excel)
    

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