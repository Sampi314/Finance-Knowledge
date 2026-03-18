# Sum if greater than - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-greater-than

---

[Skip to main content](https://exceljet.net/formulas/sum-if-greater-than#main-content)

[](https://exceljet.net/formulas/sum-if-greater-than#)

*   [Previous](https://exceljet.net/formulas/sum-if-ends-with)
    
*   [Next](https://exceljet.net/formulas/sum-if-less-than)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if greater than
===================

by Dave Bruns · Updated 15 Jan 2023

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: Sum if greater than](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_greater_than.png "Excel formula: Sum if greater than")

Summary
-------

To sum values greater than a given number, you can use the [SUMIF function](https://exceljet.net/functions/sumif-function)
 or the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. In the example shown, cell G5 contains this formula:

    =SUMIF(D5:D16,">"&F5)
    

With $1,000 in cell F5, this formula returns $7,400, the sum of values in D5:D16 greater than $1,000.

Generic formula
---------------

    =SUMIF(D5:D16,">"&A1)

Explanation 
------------

In this example, the goal is to sum values in the range D5:D16 when they are _greater than_ the value entered in cell F5. This problem can be easily solved with the SUMIF function or the SUMIFS function. The main challenge in this problem is the syntax needed for criteria that uses the value in cell F5, which involves [concatenation](https://exceljet.net/glossary/concatenation)
.

### SUMIF function

The [SUMIF function](https://exceljet.net/functions/sumif-function)
 is designed to sum cells based on a _single_ condition. The generic syntax for SUMIF looks like this:

    =SUMIF(range,criteria,sum_range)

For example, to sum values in D5:D16 that are greater than $1,000, we can use the SUMIF function like this:

    =SUMIF(D5:D16,">1000") // returns 7400

We don't need to enter a _sum\_range_, because D5:D16 contains both the values we want to test and the values we want to sum. When this formula is entered on the worksheet shown, it returns $7,400, the sum of values in D5:D16 that are greater than $1,000.

### Hardcoded value versus cell reference

The formula above is an example of _hardcoding_ a value into a formula, which is generally a bad practice, because it makes the formula less transparent and harder to maintain. A better approach is to expose the value on the worksheet where it can be easily changed, as seen in the worksheet shown. This is the tricky part of the formula because we need to use [concatenation](https://exceljet.net/articles/build-friendly-messages-with-concatenation)
 to join the operator (">") to the cell reference F5. The updated formula looks like this:

    =SUMIF(D5:D16,">"&F5)

Notice the operator is in double quotes (">") and joined to cell F5 with an ampersand (&). When Excel evaluates this formula, it will start with the criteria, first retrieving the value from cell F5, then joining the value to the operator. After evaluating criteria, the formula will look like this:

    =SUMIF(D5:D16,">1000")

Notice this is exactly the same formula we started with above. However, by using a reference to F5 the value used by SUMIF can easily be changed at any time. For more SUMIF examples, [see this page](https://exceljet.net/functions/sumif-function)
. For more on concatenation, [see this page](https://exceljet.net/articles/how-to-concatenate-in-excel)
.

### SUMIFS function

This formula can also be solved with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
, which is designed to sum cells in a [range](https://exceljet.net/glossary/range)
 with _multiple_ criteria. The syntax for SUMIFS is similar, but the order of the [arguments](https://exceljet.net/glossary/function-argument)
 is different. With a single condition, the generic syntax for SUMIFS looks like this:

    =SUMIFS(sum_range,range1,criteria1) // 1 condition

Unlike the SUMIF function, the _sum\_range_ argument comes _first_ and not _last_, and is _not optional_. In general, this is more logical, but it does make the formula a little longer when working with just one condition. The equivalent SUMIFS formula looks like this:

    =SUMIFS(D5:D16,D5:D16,">"&F5)

Notice the _criteria_ in this formula is exactly the same as what we used in SUMIFS above. However, we need to enter the range D5:D16 two times: once for _sum\_range_, and once for _range_. When we enter this formula it returns $7,400, the sum of all values greater than $1,000 in the range D5:D16. For more SUMIFS examples, [see this page](https://exceljet.net/functions/sumifs-function)
.

Related formulas
----------------

[![Excel formula: Sum if less than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_less_than.png "Excel formula: Sum if less than")](https://exceljet.net/formulas/sum-if-less-than)

### [Sum if less than](https://exceljet.net/formulas/sum-if-less-than)

In this example, the goal is to sum values in the range D5:D16 when they are less than the value entered in cell F5. This problem can be easily solved with the SUMIF function or the SUMIFS function. The main challenge in this problem is the syntax needed for cell F5 in the criteria, which involves...

[![Excel formula: Sum if between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20if%20between.png "Excel formula: Sum if between")](https://exceljet.net/formulas/sum-if-between)

### [Sum if between](https://exceljet.net/formulas/sum-if-between)

In this example, the goal is to sum the amounts in the table using the "Start" and "End" values in columns F and G. For convenience, all data is in an Excel Table called data , which means we can use the structured reference data\[Amount\] to refer to amounts. An easy way to solve this problem is to...

[![Excel formula: Sum if begins with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_begins_with.png "Excel formula: Sum if begins with")](https://exceljet.net/formulas/sum-if-begins-with)

### [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)

In this example, the goal is to sum the Price in column C when the Product in column B begins with "sha". To solve this problem, you can use either the SUMIF function or the SUMIFS function with the asterisk (\*) wildcard, as explained below. Wildcards Certain Excel functions like SUMIF and SUMIFS...

[![Excel formula: Sum if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_not_blank.png "Excel formula: Sum if not blank")](https://exceljet.net/formulas/sum-if-not-blank)

### [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)

In this example, the goal is to sum the Amounts in C5:C16 when the Lead in D5:D16 is not blank (i.e., not empty). A good way to solve this problem is to use the SUMIFS function . However, you can also use the SUMPRODUCT function or the FILTER function , as explained below. Because SUMPRODUCT and...

[![Excel formula: Sum if cells are not equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_not_equal_to.png "Excel formula: Sum if cells are not equal to")](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

### [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when corresponding cells in the range C5:C15 are not equal to "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only one criteria...

[![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")](https://exceljet.net/formulas/sum-if-x-or-y)

### [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an Excel Table named data . This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the SUMIFS function . However, when...

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumif-function)

### [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)

In this video we'll look at how to use the SUMIF function to sum cells that meet a single criteria. Let's take a look. The SUMIF function sums cells that satisfy a single condition that you supply. It takes three arguments: range, criteria, and sum range. Note that sum range is optional. If you don...

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

*   [Sum if less than](https://exceljet.net/formulas/sum-if-less-than)
    
*   [Sum if between](https://exceljet.net/formulas/sum-if-between)
    
*   [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    
*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

### Videos

*   [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)
    
*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    

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