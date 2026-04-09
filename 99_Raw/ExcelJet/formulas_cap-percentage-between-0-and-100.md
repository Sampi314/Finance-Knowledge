# Cap percentage between 0 and 100 - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cap-percentage-between-0-and-100

---

[Skip to main content](https://exceljet.net/formulas/cap-percentage-between-0-and-100#main-content)

[](https://exceljet.net/formulas/cap-percentage-between-0-and-100#)

*   [Previous](https://exceljet.net/formulas/xlookup-match-any-column)
    
*   [Next](https://exceljet.net/formulas/find-lowest-n-values)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Cap percentage between 0 and 100
================================

by Dave Bruns · Updated 20 Nov 2020

Related functions 
------------------

[MIN](https://exceljet.net/functions/min-function)

[MAX](https://exceljet.net/functions/max-function)

[MEDIAN](https://exceljet.net/functions/median-function)

[IF](https://exceljet.net/functions/if-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6352/download?token=HNVDj_8s)
 (13.72 KB)

![Excel formula: Cap percentage between 0 and 100](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cap%20percentage%20between%200%20and%20100.png "Excel formula: Cap percentage between 0 and 100")

Summary
-------

To limit a percentage value so that it falls between 0% and 100% you can use a formula based on the [MIN](https://exceljet.net/functions/min-function)
 and [MAX](https://exceljet.net/functions/max-function)
 functions. In the example shown, the formula in C5, copied down, is:

    =MAX(0,MIN(B5,1))
    

The result is that negative values are forced to zero, values over 1 are capped at 1, and values between 0 and 1 are unaffected.

_Note: all values formatted with percentage [number format](https://exceljet.net/articles/custom-number-formats)
._

Generic formula
---------------

    =MAX(0,MIN(A1,1))

Explanation 
------------

In order to understand this problem, make sure you understand how [percentage number formatting works](https://exceljet.net/videos/how-to-use-percentage-formatting-in-excel)
. In a nutshell, percentages are decimal values: 0.1 is 10%, 0.2 is 20%, and so on. The number 1, when formatted as a percentage, is 100%. [More on number formats here](https://exceljet.net/articles/custom-number-formats)
.

The goal of this example is to limit incoming percentage values so that they fall within an upper and lower threshold. Negative values and values over 100% are not allowed, so the final result must be a number between zero and 1 (0-100%), inclusive.

Although the [IF function](https://exceljet.net/functions/if-function)
 can be used to solve this problem (see below), the result will be somewhat longer and redundant. Instead, the example shown uses a combination of the MIN and MAX functions in a very compact formula:

    =MAX(0,MIN(B5,1))
    

This is an example of [nesting](https://exceljet.net/glossary/nesting)
 – the MIN function is nested inside the MAX function. Nesting is a key building block for more advanced formulas.

Working from the inside out, the [MIN function](https://exceljet.net/functions/min-function)
 is used to cap incoming values to 1 like this:

    MIN(B5,1) // get smaller value
    

Translation: return the smaller of B5 and 1. For any value over 1, the value in B5 is returned. In the example, B5 contains -5% (-0.05), so MIN returns -0.05. This result is returned directly to the [MAX function](https://exceljet.net/functions/max-function)
:

    =MAX(0,-0.05) // get larger value
    

Here, we see the formula do its work. Because zero is larger (greater) than -0.05, MAX returns zero as a final result. The original value is discarded.

### IF function

As mentioned above, the [IF function](https://exceljet.net/functions/if-function)
 can also be used to solve this problem. To do this, we need two separate IF functions. One IF forces negative values to zero:

    IF(B5<0,0,B5) // cap at zero
    

The second IF caps larger values at 1:

    =IF(B5>1,1,B5) // cap at 1
    

When we nest the first IF inside the second, we have the final formula:

    =IF(B5>1,1,IF(B5<0,0,B5))
    

This is an example of a [nested IF](https://exceljet.net/articles/nested-ifs)
. It returns exactly the same result as the MIN and MAX formula above, but is slightly more complex and redundant. Notice, for example, the reference to B5 occurs three separate times.

The bottom line – when you need to make a choice based on smaller or larger values, the MIN and MAX functions can be a clever and elegant way to keep a formula simple.

### MEDIAN Function

OK, now that we've talked about nesting, and talked about the elegance of MIN with MAX,  I should mention that it is possible to solve this problem without any nesting at all with the [MEDIAN function](https://exceljet.net/functions/median-function)
. The generic version of the formula looks like this:

    =MEDIAN(0,1,A1)
    

This works because MEDIAN function returns the median (middle number) in a group of numbers. When a value is negative, zero becomes the middle number. When a number is greater than 1, 1 becomes the middle number. Clever!

However, note MEDIAN only returns the middle number when the total number of values is _odd_. If the number of values is _even_, MEDIAN returns the _average_ of the two numbers in the middle. As a consequence, if the target cell (A1) is _empty_, MEDIAN will return the average of 1 and zero, which is 0.5, or 50% when formatted as a percentage.

Related formulas
----------------

[![Excel formula: Cap percentage at specific amount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cap%20percentage%20at%20specific%20amount.png "Excel formula: Cap percentage at specific amount")](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

### [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

This formula uses the MIN function to make a decision that might otherwise be handled with the IF function . Although MIN is usually used to return the minimum value in a data set with many numbers, it also works fine for the "lesser of the two" situations. Inside MIN, the value in C6 is multiplied...

[![Excel formula: Cap percentage at 100](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cap%20percentage%20at%20100.png "Excel formula: Cap percentage at 100")](https://exceljet.net/formulas/cap-percentage-at-100)

### [Cap percentage at 100](https://exceljet.net/formulas/cap-percentage-at-100)

This formula uses the MIN function as an alternative to the IF function . Although MIN is frequently used to find the minimum value in a larger set of numbers, it also works fine with just two values. Inside MIN, the first value is hardcoded as 1, the equivalent of 100% when formatted as a...

[![Excel formula: Convert negative numbers to zero](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20negative%20numbers%20to%20zero.png "Excel formula: Convert negative numbers to zero")](https://exceljet.net/formulas/convert-negative-numbers-to-zero)

### [Convert negative numbers to zero](https://exceljet.net/formulas/convert-negative-numbers-to-zero)

In this example, the goal is to convert negative numbers in column B to zero and leave positive numbers unchanged. Essentially, we want to force negative numbers to zero. With the MAX function The MAX function provides an elegant solution: =MAX(B5,0) This formula takes advantage of the fact that...

[![Excel formula: Get total from percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20total%20from%20percent_0.png "Excel formula: Get total from percentage")](https://exceljet.net/formulas/get-total-from-percentage)

### [Get total from percentage](https://exceljet.net/formulas/get-total-from-percentage)

In this example, the goal is to work out the total of all expenses using a known percent of total of any one expense . If we know groceries are $200 and we know groceries represent 10.3% of total expenses, we want to calculate the total of all expenses ($1945). In other words, $200 is 10.3% of what...

[![Excel formula: Get amount with percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20amount%20with%20percent_0.png "Excel formula: Get amount with percentage")](https://exceljet.net/formulas/get-amount-with-percentage)

### [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)

In this example, the goal is to convert the percentages shown in column C to amounts, where the total of all amounts is given as $1945. In other words, if we know Rent is 36.0%, and the total of all expenses is $1945, we want to calculate that Rent is $700. With "x" as the number we want to find,...

[![Excel formula: Get percentage of total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20of%20total_0.png "Excel formula: Get percentage of total")](https://exceljet.net/formulas/get-percentage-of-total)

### [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)

In this example, the goal is to work out the "percent of total" for each expense shown in the worksheet. In other words, given that we know the total is $1945, and we know Rent is $700, we want to determine that Rent is 36% of the total. The total already exists in the named range total (C15) which...

Related functions
-----------------

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MEDIAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20median%20function.png "Excel MEDIAN function")](https://exceljet.net/functions/median-function)

### [MEDIAN Function](https://exceljet.net/functions/median-function)

The Excel MEDIAN function returns the median (middle number) in the supplied set of data. For example, =MEDIAN(1,2,3,4,5) returns 3.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)
    
*   [Cap percentage at 100](https://exceljet.net/formulas/cap-percentage-at-100)
    
*   [Convert negative numbers to zero](https://exceljet.net/formulas/convert-negative-numbers-to-zero)
    
*   [Get total from percentage](https://exceljet.net/formulas/get-total-from-percentage)
    
*   [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)
    
*   [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)
    

### Functions

*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MEDIAN Function](https://exceljet.net/functions/median-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Articles

*   [Replace ugly IFs with MAX or MIN](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
    
*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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