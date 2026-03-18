# Excel ABS function | Exceljet

**Source:** https://exceljet.net/functions/abs-function

---

[Skip to main content](https://exceljet.net/functions/abs-function#main-content)

[](https://exceljet.net/functions/abs-function#)

*   [Previous](https://exceljet.net/functions/type-function)
    
*   [Next](https://exceljet.net/functions/aggregate-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

ABS Function
============

by Dave Bruns · Updated 1 Aug 2021

![Excel ABS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20abs%20function.png "Excel ABS function")

Summary
-------

The Excel ABS function returns the absolute value of a number. ABS converts negative numbers to positive numbers, and positive numbers are unaffected.

Purpose 
--------

Find the absolute value of a number

Return value 
-------------

A positive number.

Syntax
------

    =ABS(number)

*   _number_ - The number to get the absolute value of.

Using the ABS function 
-----------------------

The ABS function returns the absolute value of a number. You can think about absolute value as a number's distance from zero on a number line. ABS converts negative numbers to positive numbers. Positive numbers and zero (0) are unaffected.

The ABS function takes just one [argument](https://exceljet.net/glossary/function-argument)
, _number_, which must be a numeric value. If _number_ is not numeric, ABS returns a #VALUE! error.

### Basic example

Negative numbers become positive, while positive numbers and zero (0) are unaffected:

    =ABS(-3) // returns 3
    =ABS(5) // returns 5
    =ABS(0) // returns 0
    

### Absolute Variance

Calculating the variance between two numbers is a common problem. For example, with a _forecast_ value in A1 and an _actual_ value in B1, you might calculate variance like this:

    =B1-A1 // negative or positive result
    

When B1 is greater than A1, variance is a positive number. However, when A1 is greater than B1, the result will be negative. To ensure the result is a positive number, you can use ABS like this:

    =ABS(B1-A1)  // ensure positive result
    

See a [detailed example here](https://exceljet.net/formulas/calculate-percent-variance)
.

### Counting absolute variances with conditions

The ABS function can be used together with the SUMPRODUCT function to count absolute variances that meet specific conditions. For example, to count absolute variances greater than 100, you can use a formula like this:

    =SUMPRODUCT(--(ABS(variances)>100))
    

[This formula is explained in more detail here](https://exceljet.net/formulas/count-or-sum-variance)
.

### Square root of negative number

The [SQRT function](https://exceljet.net/functions/sqrt-function)
 calculates the square root of a number.  If you give SQRT a negative number, it will return a #NUM! error:

    =SQRT(-4) // returns #NUM!
    

To handle a negative number like a positive number, you can use the ABS function like this:

    =SQRT(ABS(A1))
    

### Calculating tolerance

To calculate whether a value is within tolerance or not, you can use a formula like this:

    =IF(ABS(actual-expected)<=tolerance,"OK","Fail")
    

See a [detailed explanation here](https://exceljet.net/formulas/value-is-within-tolerance)
.

ABS function examples
---------------------

[![Excel formula: Count values out of tolerance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20values%20out%20of%20tolerance.png "Excel formula: Count values out of tolerance")](https://exceljet.net/formulas/count-values-out-of-tolerance)

### [Count values out of tolerance](https://exceljet.net/formulas/count-values-out-of-tolerance)

This formula counts how many values are not in range of a fixed tolerance. The variation of each value is calculated with this: ABS(data-target) Because the named range "data" contains 10 values, subtracting the target value in F4 will created an array with 10 results: {0.001;-0.002;-0.01;0.003;0...

[![Excel formula: Difference is within specific percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/difference%20is%20within%20specific%20percentage.png "Excel formula: Difference is within specific percentage")](https://exceljet.net/formulas/difference-is-within-specific-percentage)

### [Difference is within specific percentage](https://exceljet.net/formulas/difference-is-within-specific-percentage)

In this example, the goal to calculate the difference as a percentage between two values then check the result to see if its within a given target percentage. The values come from the Expected and Actual columns in the worksheet. The challenge is that the difference might be negative or positive,...

[![Excel formula: Find closest match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_closest_match_0.png "Excel formula: Find closest match")](https://exceljet.net/formulas/find-closest-match)

### [Find closest match](https://exceljet.net/formulas/find-closest-match)

In this example, the goal is to find the closest match to a target value entered in cell E5. Although it may not look like it, this is essentially a look-up problem. The easiest way to solve this problem is with the XLOOKUP function . However in older versions of Excel without the XLOOKUP function...

[![Excel formula: Square root of number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/square%20root.png "Excel formula: Square root of number")](https://exceljet.net/formulas/square-root-of-number)

### [Square root of number](https://exceljet.net/formulas/square-root-of-number)

The SQRT function is fully automatic and will return the square root of any positive number. For example, to get the square root of 25, you can use: =SQRT(25) // returns 5 To get the square root of 16: =SQRT(16) // returns 4 To get the square root of a number in cell A1: =SQRT(A1) // square root of...

[![Excel formula: Round number to n significant figures](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round_number_to_n_significant_figures.png "Excel formula: Round number to n significant figures")](https://exceljet.net/formulas/round-number-to-n-significant-figures)

### [Round number to n significant figures](https://exceljet.net/formulas/round-number-to-n-significant-figures)

In this example, the goal is to round a number to a given number of significant figures while preserving trailing zeros when needed. This is a tricky problem because Excel's rounding functions return numbers, and numbers don't preserve trailing zeros. This article uses "significant figures" and "...

[![Excel formula: Calculate percent variance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20percent%20variance.png "Excel formula: Calculate percent variance")](https://exceljet.net/formulas/calculate-percent-variance)

### [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)

In this example, the goal is to calculate the variance between a Forecast (column C) and Actual (column D) as a percentage. For example, with a Forecast value of 100,000 and an Actual value of 112,000, we want to return a variance of 12%. The concept of variance requires a baseline value and a "new...

[![Excel formula: Filter values within tolerance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20values%20within%20tolerance.png "Excel formula: Filter values within tolerance")](https://exceljet.net/formulas/filter-values-within-tolerance)

### [Filter values within tolerance](https://exceljet.net/formulas/filter-values-within-tolerance)

In this example, the goal is to list values in a given group that are within a given tolerance. The group is set in cell G4, and the target value is entered in cell G5. The allowed tolerance is entered in cell G6. The data comes from an Excel Table called data in the range B5:D16. The solution is...

[![Excel formula: Change negative numbers to positive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/change%20negative%20numbers%20to%20positive.png "Excel formula: Change negative numbers to positive")](https://exceljet.net/formulas/change-negative-numbers-to-positive)

### [Change negative numbers to positive](https://exceljet.net/formulas/change-negative-numbers-to-positive)

The ABS function is fully automatic. All you need to do is supply a number and ABS will return the absolute value. Convert negative numbers in place If you only need to convert negative numbers once, you can convert in-place with Paste Special : Add -1 to a cell and copy to the clipboard Select the...

[![Excel formula: Convert inches to feet and inches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Convert%20inches%20to%20feet%20and%20inches.png "Excel formula: Convert inches to feet and inches")](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)

### [Convert inches to feet and inches](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)

In this example, the goal is to create a formula that converts a numeric value in inches to a format that displays inches and feet, as seen in the table below: Input Output 9 0' 9" 12 1' 0" 30 2' 6" 75 6' 3" The math for this problem is fairly simple, but the problem is more complex because we need...

[![Excel formula: Lookup number plus or minus N](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20number%20plus%20or%20minus%20n.png "Excel formula: Lookup number plus or minus N")](https://exceljet.net/formulas/lookup-number-plus-or-minus-n)

### [Lookup number plus or minus N](https://exceljet.net/formulas/lookup-number-plus-or-minus-n)

In this example, the goal is to look up a number with a certain amount of allowed tolerance, defined as n . In other words, with a given lookup number we are trying to find a number in a set of data that is ± n . In the worksheet shown, the number to find is in cell G4 and the number used for n is...

[![Excel formula: Count or sum variance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20or%20sum%20variance.png "Excel formula: Count or sum variance")](https://exceljet.net/formulas/count-or-sum-variance)

### [Count or sum variance](https://exceljet.net/formulas/count-or-sum-variance)

In this example, the goal is to sum or count a set of variances in different ways. Variances are listed in D5:D15, which is also the named range variance . The first formula in F5 simply sums all variances with the SUM function . =SUM(variance) // returns -175 Sum absolute variances The formula in...

[![Excel formula: Rank with ordinal suffix](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20with%20ordinal%20suffix.png "Excel formula: Rank with ordinal suffix")](https://exceljet.net/formulas/rank-with-ordinal-suffix)

### [Rank with ordinal suffix](https://exceljet.net/formulas/rank-with-ordinal-suffix)

Ordinal numbers represent position or rank in a sequential order. They are normally written using a number + letter suffix: 1st, 2nd, 3rd, etc. To get an ordinal suffix for a small set of numbers, you can use the CHOOSE function like this: =CHOOSE(B5,"st","nd","rd","th","th","th","th","th","th","th...

[![Excel formula: Value is within tolerance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value%20is%20within%20tolerance.png "Excel formula: Value is within tolerance")](https://exceljet.net/formulas/value-is-within-tolerance)

### [Value is within tolerance](https://exceljet.net/formulas/value-is-within-tolerance)

In this example the goal is to check if values in column B are within a tolerance of .005. If a value is within tolerance, the formula should return "OK". If the value is out of tolerance, the formula should return "Fail". The expected value is listed in column C, and the allowed tolerance is...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)
    
*   [Convert inches to feet and inches](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)
    
*   [Count values out of tolerance](https://exceljet.net/formulas/count-values-out-of-tolerance)
    
*   [Lookup number plus or minus N](https://exceljet.net/formulas/lookup-number-plus-or-minus-n)
    
*   [Count or sum variance](https://exceljet.net/formulas/count-or-sum-variance)
    
*   [Change negative numbers to positive](https://exceljet.net/formulas/change-negative-numbers-to-positive)
    
*   [Find closest match](https://exceljet.net/formulas/find-closest-match)
    
*   [Rank with ordinal suffix](https://exceljet.net/formulas/rank-with-ordinal-suffix)
    
*   [Difference is within specific percentage](https://exceljet.net/formulas/difference-is-within-specific-percentage)
    
*   [Value is within tolerance](https://exceljet.net/formulas/value-is-within-tolerance)
    

### Links

*   [Microsoft ABS function documentation](https://support.office.com/en-us/article/abs-function-3420200f-5628-4e8c-99da-c99d7c87713c)
    

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