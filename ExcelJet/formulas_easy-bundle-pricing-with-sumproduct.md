# Easy bundle pricing with SUMPRODUCT - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/easy-bundle-pricing-with-sumproduct

---

[Skip to main content](https://exceljet.net/formulas/easy-bundle-pricing-with-sumproduct#main-content)

[](https://exceljet.net/formulas/easy-bundle-pricing-with-sumproduct#)

*   [Previous](https://exceljet.net/formulas/dropdown-sum-with-all-option)
    
*   [Next](https://exceljet.net/formulas/expense-begins-on-specific-month)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Easy bundle pricing with SUMPRODUCT
===================================

by Dave Bruns · Updated 14 Dec 2019

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Easy bundle pricing with SUMPRODUCT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/easy%20bundle%20pricing%20with%20SUMPRODUCT.png "Excel formula: Easy bundle pricing with SUMPRODUCT")

Summary
-------

To calculate product bundle pricing using a simple "x" to include or exclude a product, you can use a formula based on the SUMPRODUCT function. In the example shown, the formula in D11 is:

    =SUMPRODUCT($C$5:$C$9,--(D5:D9="x"))
    

Generic formula
---------------

    =SUMPRODUCT(costs,--(range="x"))

Explanation 
------------

The [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 multiplies ranges or arrays together and returns the sum of products. This sounds boring, but SUMPRODUCT is an elegant and versatile function, which this example illustrates nicely.

In this example, SUMPRODUCT is configured with two [arrays](https://exceljet.net/glossary/array)
. The first array is the range that holds product pricing:

    $C$5:$C$9
    

Note the reference is absolute to prevent changes as the formula is copied to the right. This range evaluates to the following array:

    {99;69;129;119;49}
    

The second array is generated with this expression:

    --(D5:D9="x")
    

The result of D5:D9="x" is an array of TRUE FALSE values like this:

    {TRUE;TRUE;FALSE;FALSE;FALSE}
    

The [double negative](https://exceljet.net/glossary/double-unary)
 (--) converts these TRUE FALSE values to 1s and 0s:

    {1;1;0;0;0}
    

So, inside SUMPRODUCT we have:

    =SUMPRODUCT({99;69;129;119;49},{1;1;0;0;0})
    

The SUMPRODUCT function then multiplies corresponding items in each array together:

    =SUMPRODUCT({99;69;0;0;0})
    

and returns the sum of products, 168 in this case.

Effectively, the second array acts as a filter for the values in the first array. Zeros in array2 cancel out items in array1, and 1s in array2 allow values from array1 to pass through into the final result.

### With a single array

SUMPRODUCT is set up to accept multiple arrays, but you can simplify this formula a bit by providing a single array at the start:

    =SUMPRODUCT($C$5:$C$9*(D5:D9="x"))
    

The math operation (multiplication) automatically coerces the TRUE FALSE values in the second expression to ones and zeros, with no need for a double negative.

Related formulas
----------------

[![Excel formula: Count total characters in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_characters_in_cell.png "Excel formula: Count total characters in a range")](https://exceljet.net/formulas/count-total-characters-in-a-range)

### [Count total characters in a range](https://exceljet.net/formulas/count-total-characters-in-a-range)

SUMPRODUCT accepts the range B3:B6 as an array of four cells. For each cell in the array, LEN calculates the length of the text as a number. The result is an array that contains 4 numbers. SUMPRODUCT then sums the items in this array and returns the total.

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

*   [Count total characters in a range](https://exceljet.net/formulas/count-total-characters-in-a-range)
    

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