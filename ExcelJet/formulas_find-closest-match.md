# Find closest match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/find-closest-match

---

[Skip to main content](https://exceljet.net/formulas/find-closest-match#main-content)

[](https://exceljet.net/formulas/find-closest-match#)

*   [Previous](https://exceljet.net/formulas/case-sensitive-lookup)
    
*   [Next](https://exceljet.net/formulas/find-longest-string)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Find closest match
==================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[ABS](https://exceljet.net/functions/abs-function)

[MIN](https://exceljet.net/functions/min-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7825/download?token=bFgH8rcN)
 (14.85 KB)

![Excel formula: Find closest match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/find_closest_match_0.png "Excel formula: Find closest match")

Summary
-------

To find the closest match in numeric data, you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 or an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
. In the example shown, the formula in F5 is:

    =XLOOKUP(0,ABS(C5:C16-E5),B5:B16,,1)
    

The result is "Tokyo" because the cost of $1195 is closest to the target value in cell E5, $1200.

Generic formula
---------------

    =XLOOKUP(0,ABS(values-A1),results,,1)
    

Explanation 
------------

In this example, the goal is to find the closest match to a target value entered in cell E5. Although it may not look like it, this is essentially a look-up problem. The easiest way to solve this problem is with the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
. However in older versions of Excel without the XLOOKUP function, you can use an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
. Both approaches are explained below.

### XLOOKUP solution

The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 provides an interesting way to solve this problem because one of XLOOKUP's core features is the ability to perform an approximate match on unsorted data. This sounds very abstract, but we can use this feature to look for a difference of zero between a target value and a set of data, and we don't need to worry about where in the data this match might be. The trick is that we need to calculate the actual differences on-the-fly and use the result as our lookup array. Then we look for a difference of zero. This is the approach used in the workbook shown, where the formula in cell F5 is:

    =XLOOKUP(0,ABS(C5:C16-E5),B5:B16,,1)

Notice the _lookup\_value_ is zero (0) and the _return\_array_ is B5:B16, the range that contains the city names. The clever bit is the _lookup\_array_, which is calculated like this:

    ABS(C5:C16-E5)

Working from the inside out, the first operation is to subtract the value in E5 from all costs in C5:C16. Because there are 12 values in C5:C16, this is an [array operation](https://exceljet.net/glossary/array-operation)
, and the result is an [array](https://exceljet.net/glossary/array)
 that contains 12 values like this:

    ABS({295;-601;-411;-751;-301;-50;-651;-561;499;-50;399;-5})

These values represent the _differences_ between 1200 and the values in C5:C16. Notice many values are negative. To normalize these values, we use the [ABS function](https://exceljet.net/functions/abs-function)
, which converts the numbers to absolute values. We use the ABS function here because some of the differences are negative, but we only care about absolute differences when looking for the closest match. The result from ABS looks like this:

    {295;601;411;751;301;50;651;561;499;50;399;5}

This array is returned directly to the XLOOKUP function as the _lookup\_array_:

    =XLOOKUP(0,{295;601;411;751;301;50;651;561;499;50;399;5},B5:B16,,1)

The _if\_not\_found_ argument is left empty. Finally, we get to the _match\_mode_ argument, which is key to the successful operation of the formula. By default, _match\_mode_ is zero, which means "exact match". We don't want an exact match in this problem because we are looking for a _difference of zero_ and in most cases, we won't find a perfect match. Instead, the behavior we want is "exact match or next largest value". To enable this behavior, we use the number 1 for _match\_mode_. ([More details on XLOOKUP here](https://exceljet.net/functions/xlookup-function)
).

With the configuration explained above, and a target value of $1200 in cell E5, the final result is "Tokyo", because the difference between $1200 and $1195 is $5, and 5 is the closest match to zero. The next closest match is Stockholm, with a cost of $1,150 and a difference of $50.

### INDEX and MATCH solution

In older versions of Excel without the XLOOKUP function, you can use an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 based on INDEX and MATCH like this:

    {=INDEX(B5:B16,MATCH(MIN(ABS(C5:C16-E5)),ABS(C5:C16-E5),0))}

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter in Excel 2019 and previous._

At the core, this is an [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula: [MATCH](https://exceljet.net/functions/match-function)
 locates the position of the closest match, feeds the position to [INDEX](https://exceljet.net/functions/index-function)
, and INDEX returns the value at that position in the range B5:B16. The hard work is done with the MATCH function, which is carefully configured to match the "minimum difference" like this:

    MATCH(MIN(ABS(C5:C16-E5)),ABS(C5:C16-E5),0)

Taking things step-by-step, the lookup value in MATCH is calculated with MIN and ABS like this:

    MIN(ABS(C5:C16-E5)
    

First, the value in E5 is subtracted from the values in C5:C16. This is an array operation, and since there are 12 values in the range, the result is an [array](https://exceljet.net/glossary/array)
 with 10 values like this:

    MIN(ABS({295;-601;-411;-751;-301;-50;-651;-561;499;-50;399;-5}))

These numbers represent the difference between each cost in C5:C16 and the cost in cell E5, 1200. Some values are negative because a cost is lower than the number in E5. To convert negative values to positive values, we use the [ABS function](https://exceljet.net/functions/abs-function)
, which returns the following array:

    MIN({295;601;411;751;301;50;651;561;499;50;399;5}) // returns 5

We are looking for the _closest match_, so we use the [MIN function](https://exceljet.net/functions/min-function)
 to find the _smallest difference_, which is 5. This becomes the lookup value inside MATCH. The lookup array is generated in the same way:

    ABS(C5:C16-E5) // generate lookup array
    

The ABS function then returns the same array we saw above:

    {295;601;411;751;301;50;651;561;499;50;399;5}

We now have what we need to find the position of the closest match (smallest difference), and we can rewrite the MATCH portion of the formula like this:

    MATCH(5,{295;601;411;751;301;50;651;561;499;50;399;5},0) // returns 12
    

With 5 as the lookup value, MATCH returns 12, since 5 is in the 12th position in the array:

    =INDEX(B5:B16,12)
    

The [INDEX function](https://exceljet.net/functions/index-function)
 then returns the 12th city in the range, "Tokyo", as a final result.

_Note: if there is a tie, this formula will return the first match._

Related formulas
----------------

[![Excel formula: Lookup number plus or minus N](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20number%20plus%20or%20minus%20n.png "Excel formula: Lookup number plus or minus N")](https://exceljet.net/formulas/lookup-number-plus-or-minus-n)

### [Lookup number plus or minus N](https://exceljet.net/formulas/lookup-number-plus-or-minus-n)

In this example, the goal is to look up a number with a certain amount of allowed tolerance, defined as n . In other words, with a given lookup number we are trying to find a number in a set of data that is ± n . In the worksheet shown, the number to find is in cell G4 and the number used for n is...

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: Maximum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value_if.png "Excel formula: Maximum value if")](https://exceljet.net/formulas/maximum-value-if)

### [Maximum value if](https://exceljet.net/formulas/maximum-value-if)

In this example, the goal is to get the maximum value for each group in the data as shown. The easiest way to solve this problem is with the MAXIFS function. However, there are actually several options. If you need more flexibility (i.e. you need to work with arrays and not ranges), you can use the...

[![Excel formula: Minimum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value_if_0.png "Excel formula: Minimum value if")](https://exceljet.net/formulas/minimum-value-if)

### [Minimum value if](https://exceljet.net/formulas/minimum-value-if)

In this example, the goal is to get the minimum value for each group in the data as shown. The easiest way to solve this problem is with the MINIFS function. However, there are actually several options. If you need more flexibility (you need to work with arrays instead of ranges), you can use the...

[![Excel formula: Lookup value between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20value%20between%20two%20numbers.png "Excel formula: Lookup value between two numbers")](https://exceljet.net/formulas/lookup-value-between-two-numbers)

### [Lookup value between two numbers](https://exceljet.net/formulas/lookup-value-between-two-numbers)

The LOOKUP function does an approximate match lookup in one range, and returns the corresponding value in another. Although the table in this example includes both maximum and minimum values, we only need to use the minimum values. This is because when LOOKUP can't find a match, it will match the...

[![Excel formula: Find closest match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_closest_match_0.png "Excel formula: Find closest match")](https://exceljet.net/formulas/find-closest-match)

### [Find closest match](https://exceljet.net/formulas/find-closest-match)

In this example, the goal is to find the closest match to a target value entered in cell E5. Although it may not look like it, this is essentially a look-up problem. The easiest way to solve this problem is with the XLOOKUP function . However in older versions of Excel without the XLOOKUP function...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20abs%20function.png "Excel ABS function")](https://exceljet.net/functions/abs-function)

### [ABS Function](https://exceljet.net/functions/abs-function)

The Excel ABS function returns the absolute value of a number. ABS converts negative numbers to positive numbers, and positive numbers are unaffected.

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Lookup number plus or minus N](https://exceljet.net/formulas/lookup-number-plus-or-minus-n)
    
*   [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [Maximum value if](https://exceljet.net/formulas/maximum-value-if)
    
*   [Minimum value if](https://exceljet.net/formulas/minimum-value-if)
    
*   [Lookup value between two numbers](https://exceljet.net/formulas/lookup-value-between-two-numbers)
    
*   [Find closest match](https://exceljet.net/formulas/find-closest-match)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ABS Function](https://exceljet.net/functions/abs-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

### Articles

*   [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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