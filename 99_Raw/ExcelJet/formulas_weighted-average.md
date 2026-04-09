# Weighted average - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/weighted-average

---

[Skip to main content](https://exceljet.net/formulas/weighted-average#main-content)

[](https://exceljet.net/formulas/weighted-average#)

*   [Previous](https://exceljet.net/formulas/must-pass-4-out-of-6-subjects)
    
*   [Next](https://exceljet.net/formulas/basic-filter-example)
    

[Average](https://exceljet.net/formulas#Average)

Weighted average
================

by Dave Bruns · Updated 24 Jan 2023

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[SUM](https://exceljet.net/functions/sum-function)

[AVERAGE](https://exceljet.net/functions/average-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6264/download?token=FbMVTZDm)
 (16.65 KB)

![Excel formula: Weighted average](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/weighted_average.png "Excel formula: Weighted average")

Summary
-------

To calculated a weighted average, you can use a formula based on the [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 function and the [SUM function](https://exceljet.net/videos/how-to-use-the-sum-function)
. In the example shown, the formula in G5, copied down, is:

    =SUMPRODUCT(weights,C5:E5)/SUM(weights)
    

where **weights** is the [named range](https://exceljet.net/glossary/named-range)
 I5:K5. As the formula is copied down, it returns the weighted average seen in column G.

Generic formula
---------------

    =SUMPRODUCT(weights,values)/SUM(weights)

Explanation 
------------

In this example, the goal is to calculate a _weighted average_ of scores for each name in the table using the weights that appear in the named range **weights** (I5:K5) and the scores in columns C through E. A weighted average (also called a _weighted mean_) is an average where some values are more important than others. In other words, some values have more "weight". We can calculate a weighted average by multiplying the values to average by their corresponding weights, then dividing the sum of results by the sum of weights. In Excel, this can be represented with the generic formula below, where weights and values are cell ranges:

    =SUMPRODUCT(weights,values)/SUM(weights)
    

The core of this formula is the SUMPRODUCT function. In a nutshell, SUMPRODUCT multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds really boring, but SUMPRODUCT is an incredibly versatile function that shows up in all kinds of useful formulas. See [this page](https://exceljet.net/functions/sumproduct-function)
 for an overview.

### Worksheet example

In the worksheet shown, scores for 3 tests appear in columns C through E, and weights appear in the [named range](https://exceljet.net/glossary/named-range)
 **weights** (I5:K5). The formula in cell G5 is:

    =SUMPRODUCT(weights,C5:E5)/SUM(weights)
    

Looking first at the left side, we use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to multiply weights by corresponding scores and sum the result:

    =SUMPRODUCT(weights,C5:E5) // returns  88.25
    

SUMPRODUCT multiplies _corresponding_ elements of the two arrays together, then returns the sum of the product. We can visualize this operation in cell G5 like this:

    =SUMPRODUCT({0.25,0.25,0.5},{90,83,90})
    =SUMPRODUCT({22.5,20.75,45})
    =88.25
    

The result is then divided by the sum of the weights:

    =88.25/SUM(weights)
    =88.25/SUM({0.25,0.25,0.5})
    =88.25/1
    =88.25
    

_Note: when calculating a weighted average, it is common to assign weights that add up to the number 1. As you can see above, when the weights do add up to 1, the denominator becomes 1 and has no effect in the formula. However, it is not required that weights add up to 1, and the general form of the formula used above is meant to handle either case. See below for an example where weights do not add up to 1._

As the formula is copied down column G, the named range **weights** I5:K5 does not change, since it behaves like an [absolute reference](https://exceljet.net/glossary/absolute-reference)
. However, the scores in C5:E5, which are [relative reference](https://exceljet.net/glossary/relative-reference)
, change with each new row. The result is a weighted average for each name in the list as shown. For easy reference, the average in column F is calculated normally with the [AVERAGE function](https://exceljet.net/functions/average-function)
:

    =AVERAGE(C5:E5)
    

### Weights that do not sum to 1

In the example above, the weights are configured to add up to 1, so the divisor is 1, and the final result is the value returned by SUMPRODUCT. However, a nice feature of the formula is that the weights don't need to add up to 1. For example, we could use a weight of 1 for the first two tests and a weight of 2 for the final (since the final is twice as important) and the weighted average will be the same:

![Excel weighted average with custom weights](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/weighted%20average%20custom%20weights.png?itok=hUyK49Tn "Excel weighted average with custom weights")

In cell G5, the formula is solved like this:

    =SUMPRODUCT(weights,C5:E5)/SUM(weights)
    =SUMPRODUCT({1,1,2},{90,83,90})/SUM(1,1,2)
    =SUMPRODUCT({90,83,180})/SUM(1,1,2)
    =353/4
    =88.25
    

_Note: the values in curly braces {} above are [arrays](https://exceljet.net/glossary/array)
, which map directly to ranges in Excel._

### Transposing weights

The SUMPRODUCT function requires that array dimensions be compatible to run correctly. For example, if the data is in a [horizontal array](https://exceljet.net/videos/what-is-an-array)
, the weights should also be in a horizontal array. If dimensions are _not_ compatible, SUMPRODUCT will return a #VALUE error. To prevent this problem, you may need to transpose the weights to match the data. In the example below, the weights are the same as the original example above, but they are listed in a _vertical_ range:

![Excel weighted average with TRANSPOSE](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/weighted%20average%20with%20transpose.png?itok=LcuVwOaJ "Excel weighted average with TRANSPOSE")

In this case, to calculate a weighted average with the same formula, we need to "flip" the weights into a horizontal array with the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 like this:

    =SUMPRODUCT(TRANSPOSE(weights),C5:E5)/SUM(weights)
    

After TRANSPOSE runs, the vertical array:

    =TRANSPOSE({0.25;0.25;0.5}) // vertical array
    

becomes a horizontal array like this:

    ={0.25,0.25,0.5} // horizontal array
    

Note the semicolons are now commas, which indicate a horizontal array. From this point, the formula is solved the same way as explained earlier.

Video: [What is an array?](https://exceljet.net/videos/what-is-an-array)

Related formulas
----------------

[![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")](https://exceljet.net/formulas/average-top-3-scores)

### [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the...

[![Excel formula: Basic average example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic_average_example.png "Excel formula: Basic average example")](https://exceljet.net/formulas/basic-average-example)

### [Basic average example](https://exceljet.net/formulas/basic-average-example)

In this example, the goal is to calculate a quiz score average for each person listed in column D using the four scores in columns C, D, E, and F. The standard way to solve this problem in Excel is to use the AVERAGE function . AVERAGE function The AVERAGE function calculates the average (...

[![Excel formula: Average numbers ignore zero](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_numbers_ignore_zero.png "Excel formula: Average numbers ignore zero")](https://exceljet.net/formulas/average-numbers-ignore-zero)

### [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)

In this example, the goal is to calculate an average of the quiz scores in columns C, D, E, and F for each person. However, the result needs to ignore any zeros that appear in the data. This formula can be easily solved with the AVERAGEIF function or the AVERAGEIFS function . It can also be solved...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20an%20average%20value-thumb.png)](https://exceljet.net/videos/how-to-calculate-an-average-value)

### [How to calculate an average value](https://exceljet.net/videos/how-to-calculate-an-average-value)

In this video we'll look at how to calculate an average value. Let's take a look. In this worksheet we have a list of 16 properties, each with a price and other information. Let's calculate an average price. First, I'll create a named range for the prices. This makes the formulas easier to read and...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20is%20an%20array%20formula%3F-play.png)](https://exceljet.net/videos/what-is-an-array-formula)

### [What is an array formula?](https://exceljet.net/videos/what-is-an-array-formula)

In this video, we'll answer the question: What is an array formula? In the world of Excel formulas, the term "array formula" is probably responsible for more confusion than just about any other concept. This is because the definition of an array formula has become mixed up with the requirement to...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    
*   [Basic average example](https://exceljet.net/formulas/basic-average-example)
    
*   [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    

### Videos

*   [How to calculate an average value](https://exceljet.net/videos/how-to-calculate-an-average-value)
    
*   [What is an array formula?](https://exceljet.net/videos/what-is-an-array-formula)
    

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