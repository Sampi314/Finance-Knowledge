# XMATCH reverse search - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xmatch-reverse-search

---

[Skip to main content](https://exceljet.net/formulas/xmatch-reverse-search#main-content)

[](https://exceljet.net/formulas/xmatch-reverse-search#)

*   [Previous](https://exceljet.net/formulas/xlookup-without-na-error)
    
*   [Next](https://exceljet.net/formulas/xmatch-with-multiple-criteria)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XMATCH reverse search
=====================

by Dave Bruns · Updated 21 Feb 2020

Related functions 
------------------

[XMATCH](https://exceljet.net/functions/xmatch-function)

[INDEX](https://exceljet.net/functions/index-function)

![Excel formula: XMATCH reverse search](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XMATCH%20reverse%20search.png "Excel formula: XMATCH reverse search")

Summary
-------

To perform a "reverse search" (i.e. search last to first), you can use the XMATCH function. In the example shown, the formula in cell G5, copied down, is:

    =XMATCH(F5,names,0,-1)
    

where **names** (B5:B15) is a [named range](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =XMATCH(A1,range,0,-1)

Explanation 
------------

The XMATCH function offers new features not available with the MATCH function. One of these is the ability to perform a "reverse search", by setting the optional search mode argument. The default value for search mode is 1, which specifies a normal "first to last" search. In this mode, XMATCH will match the lookup value against the lookup array, beginning at the first value.

    =XMATCH(F5,names,0,1) // start with first name
    

Setting search mode to -1 species a "last to first" search. In this mode, XMATCH will match the lookup value against the lookup array, starting with the last value, and moving toward the first:

    =XMATCH(F5,names,0,-1) // start with last name
    

### Retrieve date and amount

XMATCH returns a position. Typically, XMATCH is used with the INDEX function to return a value at that position. In the example show, we can use INDEX and XMATCH together to retrieve the date and sales for each name as follows:

    =INDEX(dates,XMATCH(F5,names,0,-1)) // get date
    =INDEX(sales,XMATCH(F5,names,0,-1)) // get sale
    

where **dates** (C5:C15) and **sales** (D5:D15) are [named ranges](https://exceljet.net/glossary/named-range)
. As before, search mode is set to -1 to force a reverse search.

For more information about using INDEX with MATCH, see [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: Nearest location with XMATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nearest%20location%20with%20XMATCH.png "Excel formula: Nearest location with XMATCH")](https://exceljet.net/formulas/nearest-location-with-xmatch)

### [Nearest location with XMATCH](https://exceljet.net/formulas/nearest-location-with-xmatch)

At the core, this formula is a basic INDEX and MATCH formula . However, instead of using the older MATCH function , we are using XMATCH function , which provides a more powerful match mode setting: =INDEX(location,XMATCH(0,distance,1)) Working from the inside out, we are using the XMATCH function...

Related functions
-----------------

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Nearest location with XMATCH](https://exceljet.net/formulas/nearest-location-with-xmatch)
    

### Functions

*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

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