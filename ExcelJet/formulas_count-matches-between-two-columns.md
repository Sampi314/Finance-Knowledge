# Count matches between two columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-matches-between-two-columns

---

[Skip to main content](https://exceljet.net/formulas/count-matches-between-two-columns#main-content)

[](https://exceljet.net/formulas/count-matches-between-two-columns#)

*   [Previous](https://exceljet.net/formulas/count-long-numbers)
    
*   [Next](https://exceljet.net/formulas/count-matching-values-in-matching-columns)
    

[Count](https://exceljet.net/formulas#Count)

Count matches between two columns
=================================

by Dave Bruns · Updated 7 Jun 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count matches between two columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20matches%20between%20two%20columns.png "Excel formula: Count matches between two columns")

Summary
-------

To compare two columns and count matches in corresponding rows, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in G6 is:

    =SUMPRODUCT(--(B5:B15=D5:D15))
    

The result is 9 because there are nine values in the range B5:B15 that match values in D5:D15 in corresponding rows.

_Note: this formula counts matches in corresponding rows. To count all matches in two ranges, regardless of row, [see this example](https://exceljet.net/formulas/count-total-matches-in-two-ranges)
._

Generic formula
---------------

    =SUMPRODUCT(--(range1=range2))

Explanation 
------------

In this example, the goal is to compare two columns and return the count of matches in corresponding rows. A good way to solve this problem is to use the SUMPRODUCT function or the SUM function, as explained below.

### SUMPRODUCT function

The [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 is a versatile function that [handles array operations natively](https://exceljet.net/articles/why-sumproduct)
 without any special array syntax. Its behavior is simple: it multiplies, then sums the product of arrays. Working from the inside out, we compare the range B5:B15 to D5:D15 like this:

    B5:B15=D5:D15
    

Because there are 11 values in the first range, the result is an array with 11 TRUE and FALSE values like this:

    {TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;TRUE}
    

In this array, the TRUE values correspond to cells in B5:B15 that match corresponding cells in D5:D15. In this state, SUMPRODUCT will actually return zero because TRUE and FALSE values are not counted as numbers in Excel by default. To get SUMPRODUCT to treat TRUE as 1 and FALSE as zero, we need to "coerce" them into numbers. The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is a simple way to do that:

    --(B5:B15=D5:D15)
    

This results in an array containing only 1s and 0s, which is returned directly to the SUMPRODUCT function:

    =SUMPRODUCT({1;1;1;1;0;1;1;1;1;0;1}) // returns 9
    

With no other arrays to multiply, SUMPRODUCT simply sums the values and returns 9.

### Count non-matching rows

To count non-matching values, you can reverse the logic and use the not equal to [operator](https://exceljet.net/glossary/logical-operators)
 (<>). The formula in G7 is:

    =SUMPRODUCT(--(B5:B15<>D5:D15))
    

This formula returns 2, since there are two non-matching cells.

### SUM function

Traditionally, the SUMPRODUCT function has been used instead of the SUM function in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, because SUMPRODUCT can handle [array operations](https://exceljet.net/glossary/array-operation)
 without Control + Shift + Enter. In Excel 365 and Excel 2021, [the formula engine handles array formulas natively](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, so you can use the SUM function instead without special treatment:

    =SUM(--(B5:B15=D5:D15)) // count matches
    =SUM(--(B5:B15<>D5:D15)) // count non-matches
    

For more details, [see this article](https://exceljet.net/articles/why-sumproduct)
.

Related formulas
----------------

[![Excel formula: Count if two criteria match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20if%20two%20criteria%20match.png "Excel formula: Count if two criteria match")](https://exceljet.net/formulas/count-if-two-criteria-match)

### [Count if two criteria match](https://exceljet.net/formulas/count-if-two-criteria-match)

In this example, the goal is to count orders where the color is "blue" and the quantity is greater than 15. All data is in the range B5:B15. There are two primary ways to solve this problem, one with the COUNTIFS function, the other with the SUMPRODUCT function. Both approaches are explained below...

[![Excel formula: Count sold and remaining](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20sold%20and%20remaining.png "Excel formula: Count sold and remaining")](https://exceljet.net/formulas/count-sold-and-remaining)

### [Count sold and remaining](https://exceljet.net/formulas/count-sold-and-remaining)

In this example, the goal is to count the number of items sold and remaining, based on the data visible in columns B and C. The ID column holds unique ids, and the Sold column is used to record a sale. An "x" in the Sold column indicates the item has been sold. As is typical in Excel, there are...

[![Excel formula: Count total matches in two ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20total%20matches%20in%20two%20ranges.png "Excel formula: Count total matches in two ranges")](https://exceljet.net/formulas/count-total-matches-in-two-ranges)

### [Count total matches in two ranges](https://exceljet.net/formulas/count-total-matches-in-two-ranges)

In this example, the goal is to count the number of exact matches in two ranges, ignoring the sort order or location of the values in each range. This problem can be solved with the COUNTIF function or with the MATCH function. Each approach is explained below. Note: Both formulas below use the...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count if two criteria match](https://exceljet.net/formulas/count-if-two-criteria-match)
    
*   [Count sold and remaining](https://exceljet.net/formulas/count-sold-and-remaining)
    
*   [Count total matches in two ranges](https://exceljet.net/formulas/count-total-matches-in-two-ranges)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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