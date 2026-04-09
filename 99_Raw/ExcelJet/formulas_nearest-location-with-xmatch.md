# Nearest location with XMATCH - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/nearest-location-with-xmatch

---

[Skip to main content](https://exceljet.net/formulas/nearest-location-with-xmatch#main-content)

[](https://exceljet.net/formulas/nearest-location-with-xmatch#)

*   [Previous](https://exceljet.net/formulas/multiple-matches-into-separate-rows)
    
*   [Next](https://exceljet.net/formulas/next-largest-match-with-the-match-function)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Nearest location with XMATCH
============================

by Dave Bruns · Updated 21 Feb 2020

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

![Excel formula: Nearest location with XMATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/nearest%20location%20with%20XMATCH.png "Excel formula: Nearest location with XMATCH")

Summary
-------

To locate the nearest location by distance you can use a formula based on the XMATCH function with INDEX function. In the example shown, the formula in cell E5 is:

    =INDEX(location,XMATCH(0,distance,1))
    

where **location** (B5:B12) and **distance** (C5:C12) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =INDEX(location,XMATCH(0,distance,1))

Explanation 
------------

At the core, this formula is a basic [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
. However, instead of using the older [MATCH function](https://exceljet.net/functions/match-function)
, we are using [XMATCH function](https://exceljet.net/functions/xmatch-function)
, which provides a more powerful match mode setting:

    =INDEX(location,XMATCH(0,distance,1))
    

Working from the inside out, we are using the XMATCH function to find the position of the nearest location:

    XMATCH(0,distance,1) // find row nearest zero
    

We do that by setting lookup value to zero (0), lookup array to the **distance** (C5:C12), and match mode to 1.

A match mode value of 1 tells XMATCH to find an exact match or _next largest value_. Since lookup value is provided as zero (0), XMATCH will find the first distance greater than zero. A nice benefit of XMATCH – what sets it apart from MATCH – is it doesn't the lookup array to be sorted. Regardless of order, MATCH will return the first exact match or next largest value.

In the example, XMATCH returns 5, since the smallest distance is 7 (location G), which appears fifth in the list. The formula resolves to:

    =INDEX(location,5) // returns "G"
    

and INDEX returns the fifth item from the [named range](https://exceljet.net/glossary/named-range)
 **location** (B5:B12), which is "G".

_Note: in the even of a tie, XMATCH will return the first match for tied values._

### Get distance

The formula to return the actual distance of the nearest location is almost the same. Instead of giving INDEX the location names, we give INDEX the distances. The formula in F5 is:

    =INDEX(distance,XMATCH(0,distance,1)) // returns distance
    

XMATCH returns the same result as above (5), and INDEX returns 7.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    

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