# Sum columns based on adjacent criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria

---

[Skip to main content](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria#main-content)

[](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria#)

*   [Previous](https://exceljet.net/formulas/sum-by-year)
    
*   [Next](https://exceljet.net/formulas/sum-entire-column)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum columns based on adjacent criteria
======================================

by Dave Bruns · Updated 12 Nov 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Sum columns based on adjacent criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20columns%20based%20on%20adjacent%20criteria.png "Excel formula: Sum columns based on adjacent criteria")

Summary
-------

To sum values in columns based on criteria in an adjacent column, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in K5 is:

    =SUMPRODUCT(--($B5:$H5=J$4),$C5:$I5)
    

As the formula is copied across and down, it returns a sum of values associated with "A" and "B" in the table to the left.

Generic formula
---------------

    =SUMPRODUCT(--(range1=criteria),range2)

Explanation 
------------

In this example, the goal is to sum the values in columns C, E, G, and I conditionally using the text values in columns B, D, F, and H for criteria. This problem can be solved with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
, which is designed to multiply [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and return the sum of products. The formula in K5 is:

    =SUMPRODUCT(--($B5:$H5=K$4),$C5:$I5)
    

Working from the inside out, SUMPRODUCT is configured with two arguments, _array1_ and _array2_. The first array, _array1,_ is set up to act as a "filter" to allow only values that meet criteria:

    --($B5:$H5=K$4)
    

_Note: both references above are [mixed references](https://exceljet.net/videos/how-to-create-a-mixed-reference)
. $B5:$H5 has the columns locked, so that the formula can be copied across. K$4 has the row locked so that the formula can be copied down._

All values in the range B5:H5 are compared to the value in K4. The result is an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values like this:

    {TRUE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE}
    

In this array, each TRUE value corresponds to the value "A" in B5:H5, and FALSE values correspond to other values. The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is used to convert the TRUE and FALSE values to 1s and 0s and the result looks like this:

    {1,0,0,0,1,0,0}
    

We can now simplify the formula like this:

    =SUMPRODUCT({1,0,0,0,1,0,0},$C5:$I5)
    

The second array, input as $C5:$I5, evaluates to:

    {2,"B",5,"A",2,"B",1}
    

We can now simplify the formula to:

    =SUMPRODUCT({1,0,0,0,1,0,0},{2,"B",5,"A",2,"B",1})
    

Next, SUMPRODUCT multiplies the two arrays together. Only the values in the second array that correspond to 1s in the first array survive this operation. Since SUMPRODUCT is programmed to ignore the errors that result from multiplying text values, the final array looks like this:

    {2,0,0,0,2,0,0}
    

SUMPRODUCT then sums the array and returns a final result of 4.

    =SUMPRODUCT({2,0,0,0,2,0,0}) // returns 4
    

This represents the numbers that correspond to "A'" in row 5. As the formula is copied down and across, we get a sum for "A" and "B" in each row.

Related formulas
----------------

[![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")](https://exceljet.net/formulas/sum-every-nth-column)

### [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)

In this example, the goal is to sum every nth value by column in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value by column, if n =3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and n is entered into...

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

*   [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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