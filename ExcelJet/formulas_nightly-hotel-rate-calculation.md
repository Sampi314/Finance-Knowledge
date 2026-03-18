# Nightly hotel rate calculation - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/nightly-hotel-rate-calculation

---

[Skip to main content](https://exceljet.net/formulas/nightly-hotel-rate-calculation#main-content)

[](https://exceljet.net/formulas/nightly-hotel-rate-calculation#)

*   [Previous](https://exceljet.net/formulas/new-customers-per-month)
    
*   [Next](https://exceljet.net/formulas/normalize-size-units-to-gigabytes)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Nightly hotel rate calculation
==============================

by Dave Bruns · Updated 4 Oct 2023

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[FILTER](https://exceljet.net/functions/filter-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/5713/download?token=zX4tYU9W)
 (10.51 KB)

![Excel formula: Nightly hotel rate calculation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/nightly%20hotel%20rate%20calculation.png "Excel formula: Nightly hotel rate calculation")

Summary
-------

To calculate a total for a hotel stay where the nightly rate varies by room type and calendar dates, you can use a formula based on the SUMPRODUCT function. In the example shown, the formula in J8 is:

    =SUMPRODUCT((dates>=J5)*(dates<J6)*(rooms=J4),rates)
    

where **dates** (B5:B15), **rooms** (C4:G4), and **rates** (C5:G15) are [named ranges](https://exceljet.net/glossary/named-range)
.

With check-in on December 3 and check-out on December 7 (4 nights) in a King room, the formula returns a total of $460.

Explanation 
------------

The [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 multiplies arrays together and returns the sum of products. The trick is to use simple array expressions to "cancel out" the irrelevant rates in the table. SUMPRODUCT then simply sums the rates that remain.

Working from the inside out, this formula uses [boolean logic](https://exceljet.net/glossary/boolean-logic)
 to "filter" the rate data. The filter is constructed with three expressions, provided as the first argument to SUMPRODUCT:

    (dates>=J5)* // date greater than or equal to Dec 3
    (dates<J6)* // date less than Dec 7
    (rooms=J4)* // room is "King"
    

Each of these expressions returns an [array](https://exceljet.net/glossary/array)
 of TRUE FALSE values:

    {FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE}*
    {TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}*
    {FALSE,FALSE,TRUE,FALSE,FALSE}
    

The math operation of multiplying the arrays together coerces the TRUE FALSE values to 1s and 0s, so we can visualize the operation more simply like this:

    {0;0;1;1;1;1;1;1;1;1;1}*
    {1;1;1;1;1;1;0;0;0;0;0}*
    {0,0,1,0,0}
    

The result is a two-dimensional array like this:

    {0,0,0,0,0;0,0,0,0,0;0,0,1,0,0;0,0,1,0,0;0,0,1,0,0;0,0,1,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0}
    

This is the array that does the filtering in this example. If we overlay the filter array on the rate area of the worksheet, it's easier to understand what's happening:

![Filter array overlaid on rate data](https://exceljet.net/sites/default/files/images/formulas/inline/nightly%20hotel%20rate%20calculation%20filter%20array.png "Filter array overlaid on data")

Notice the array only contains 1s where we want the rate information to come through. Every other value is zero. When this array is multiplied by the rate data (see below) the zeros will cancel out rate data that is not relevant to room, check-in, and check-out information.

The second argument provided to SUMPRODUCT contains all room rates, in the named range **rates** (C5:G15). This also is a two-dimensional array:

    {65,80,90,105,175;80,95,105,120,250;80,95,105,120,250;80,95,105,120,250;90,105,125,150,250;100,115,125,150,300;100,115,125,150,300;65,80,90,105,300;80,95,105,120,250;80,95,105,120,250;80,95,105,120,250}
    

Inside SUMPRODUCT, the filtering array described above is multiplied by the named range **rates**. Both arrays are the same size, the result is an array of the same dimensions. Notice only the rates associated with the stay (as defined by check-in, check-out, and room) have survived the filter:

    {0,0,0,0,0;0,0,0,0,0;0,0,105,0,0;0,0,105,0,0;0,0,125,0,0;0,0,125,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0}
    

Finally, SUMPRODUCT sums all values in the array and returns a final result, 460.

_Note: although the rate information is organized with vertical dates and horizontal rooms, it can be transposed and the formula will still function correctly._

### With the FILTER function

You can also solve this problem nicely with the new [FILTER function](https://exceljet.net/functions/filter-function)
:

    =SUM(FILTER(INDEX(rates,0,MATCH(J4,rooms,0)),(dates>=J5)*(dates<J6)))
    

The gist of the solution is that we use the [INDEX function](https://exceljet.net/functions/index-function)
 to extract [just the rates for a King room](https://exceljet.net/formulas/look-up-entire-column)
, and then we feed those rates to FILTER, which extracts just the rates for relevant dates. FILTER delivers these rates to the [SUM function](https://exceljet.net/functions/sum-function)
, which returns a final result.

Related formulas
----------------

[![Excel formula: SUMPRODUCT with IF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sumproduct_with_if.png "Excel formula: SUMPRODUCT with IF")](https://exceljet.net/formulas/sumproduct-with-if)

### [SUMPRODUCT with IF](https://exceljet.net/formulas/sumproduct-with-if)

In this example, the goal is to calculate a conditional sum with the SUMPRODUCT function to match the criteria shown in G5:G7. One way to do this is to use the IF function directly inside of SUMPRODUCT. Another more common alternative is to use Boolean logic to apply criteria. Both approaches are...

[![Excel formula: Cash denomination calculator](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cash_denomination_calculator.png "Excel formula: Cash denomination calculator")](https://exceljet.net/formulas/cash-denomination-calculator)

### [Cash denomination calculator](https://exceljet.net/formulas/cash-denomination-calculator)

In this example, the goal is to build a "cash denomination calculator." A cash denomination calculator is a tool for counting and verifying cash amounts. It can calculate the denominations needed to achieve a certain cash value. It can also perform the reverse calculation and determine the cash...

[![Excel formula: Easy bundle pricing with SUMPRODUCT](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/easy%20bundle%20pricing%20with%20SUMPRODUCT.png "Excel formula: Easy bundle pricing with SUMPRODUCT")](https://exceljet.net/formulas/easy-bundle-pricing-with-sumproduct)

### [Easy bundle pricing with SUMPRODUCT](https://exceljet.net/formulas/easy-bundle-pricing-with-sumproduct)

The SUMPRODUCT function multiplies ranges or arrays together and returns the sum of products. This sounds boring, but SUMPRODUCT is an elegant and versatile function, which this example illustrates nicely. In this example, SUMPRODUCT is configured with two arrays . The first array is the range that...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [SUMPRODUCT with IF](https://exceljet.net/formulas/sumproduct-with-if)
    
*   [Cash denomination calculator](https://exceljet.net/formulas/cash-denomination-calculator)
    
*   [Easy bundle pricing with SUMPRODUCT](https://exceljet.net/formulas/easy-bundle-pricing-with-sumproduct)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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