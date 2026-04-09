# Sum lookup values using SUMIF - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-lookup-values-using-sumif

---

[Skip to main content](https://exceljet.net/formulas/sum-lookup-values-using-sumif#main-content)

[](https://exceljet.net/formulas/sum-lookup-values-using-sumif#)

*   [Previous](https://exceljet.net/formulas/step-based-lookup-example)
    
*   [Next](https://exceljet.net/formulas/sum-range-with-index)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Sum lookup values using SUMIF
=============================

by Dave Bruns · Updated 22 May 2016

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Sum lookup values using SUMIF](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20lookup%20values%20using%20SUMIF.png "Excel formula: Sum lookup values using SUMIF")

Summary
-------

To sum values retrieved by a lookup operation, you can use SUMPRODUCT with the SUMIF function.

In the example shown, the formula in H5 is:

    =SUMPRODUCT(SUMIF(codes,C5:G5,values))
    

Where codes is the named range J4:J5 and values is the named range K4:K5.

### Context

Sometimes you may want to sum multiple values retrieved by a lookup operation. In this example, we want to sum holiday time taken each week based on a code system, where F = a full day, and H = a half day. If a day is blank, no time was taken.

The challenge is to find a formula that both looks up and sums the values associated with F and H.

Generic formula
---------------

    =SUMPRODUCT(SUMIF(codes,lookups,values))

Explanation 
------------

The core of this formula is SUMIF, which is used to lookup the correct values for F and H. Using SUMIF to lookup values is a more advanced technique that works well when the values are _numeric_, and there are _no duplicates_ in the "lookup table".

The trick in this case is that the criteria for SUMIF is not a single value, but rather an array of values in the range C5:G5:

    =SUMPRODUCT(SUMIF(codes,C5:G5,values))
    

Because we are giving SUMIF more than one criteria, SUMIF will return more than one result. In the example shown, the result of SUMIF is the following array:

{1,0.5,0,0,0}

Note that we correctly get 1 for each "F" and 0.5 for each "H"., and blank values in the week generate zero.

Finally, we use SUMPRODUCT to add up the values in the array returned by SUMIF. Because there is only a single array, SUMPRODUCT simply returns the sum of all values.

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

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

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
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