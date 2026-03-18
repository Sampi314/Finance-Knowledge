# Lookup value between two numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lookup-value-between-two-numbers

---

[Skip to main content](https://exceljet.net/formulas/lookup-value-between-two-numbers#main-content)

[](https://exceljet.net/formulas/lookup-value-between-two-numbers#)

*   [Previous](https://exceljet.net/formulas/lookup-up-cost-for-product-or-service)
    
*   [Next](https://exceljet.net/formulas/lookup-with-variable-sheet-name)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Lookup value between two numbers
================================

by Dave Bruns · Updated 17 Jun 2022

Related functions 
------------------

[LOOKUP](https://exceljet.net/functions/lookup-function)

![Excel formula: Lookup value between two numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lookup%20value%20between%20two%20numbers.png "Excel formula: Lookup value between two numbers")

Summary
-------

To lookup values between two values and return a corresponding result, you can use the LOOKUP function and a sorted table. In the example shown, the formula in C5 is:

    =LOOKUP(B5,mins,results)
    

where "mins" is the [named range](https://exceljet.net/glossary/named-range)
 E5:E9, and "results" is the named range G5:G9.

Generic formula
---------------

    =LOOKUP(B5,minimums,results)

Explanation 
------------

The LOOKUP function does an approximate match lookup in one range, and returns the corresponding value in another.

Although the table in this example includes both maximum and minimum values, we only need to use the minimum values. This is because when LOOKUP can't find a match, it will match the next smallest value. LOOKUP is configured like this:

*   The lookup values come from column B.
*   The lookup vector is entered as the named range "mins" (E5:E9)
*   The result vector is entered as the named range "results" (G5:G9)

LOOKUP behaves like this:

*   If LOOKUP encounters an exact match in the lookup vector, the corresponding value in the result vector is returned.
*   If no exact match is found, LOOKUP will traverse the lookup vector until a larger value is found, then "step back" to the previous row and return a result.
*   If the lookup value is greater than the largest value in the lookup vector, LOOKUP will return a result associated with the last value in the lookup vector.

_Note: values in the lookup vector must be sorted in ascending order._

### Literally between

Although the example above works fine, and effectively locates a value "between" a min and max in the lookup table, it really only uses the min values. With a named range "maxs" for maximum values, you can write a literal version of the formula like this:

    =LOOKUP(2,1/((B5>=mins)*(B5<=maxs)),results)
    

This version returns the associated value in the result vector when the value in B5 is literally between both the min and max value in a given row. In case of duplicates, this formula will return the last match. [Explanation of logic is here](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
.

Related formulas
----------------

[![Excel formula: Group numbers with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/group_numbers_with_VLOOKUP.png "Excel formula: Group numbers with VLOOKUP")](https://exceljet.net/formulas/group-numbers-with-vlookup)

### [Group numbers with VLOOKUP](https://exceljet.net/formulas/group-numbers-with-vlookup)

In this example, the goal is to group ages into buckets. One way to do this is to prepare a table with age breakpoints in the first column, and the name of the appropriate group or bucket in the second column. Then use a lookup function to find the right bucket or group for each age. In the example...

[![Excel formula: Find closest match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_closest_match_0.png "Excel formula: Find closest match")](https://exceljet.net/formulas/find-closest-match)

### [Find closest match](https://exceljet.net/formulas/find-closest-match)

In this example, the goal is to find the closest match to a target value entered in cell E5. Although it may not look like it, this is essentially a look-up problem. The easiest way to solve this problem is with the XLOOKUP function . However in older versions of Excel without the XLOOKUP function...

[![Excel formula: Lookup number plus or minus N](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20number%20plus%20or%20minus%20n.png "Excel formula: Lookup number plus or minus N")](https://exceljet.net/formulas/lookup-number-plus-or-minus-n)

### [Lookup number plus or minus N](https://exceljet.net/formulas/lookup-number-plus-or-minus-n)

In this example, the goal is to look up a number with a certain amount of allowed tolerance, defined as n . In other words, with a given lookup number we are trying to find a number in a set of data that is ± n . In the worksheet shown, the number to find is in cell G4 and the number used for n is...

Related functions
-----------------

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Group numbers with VLOOKUP](https://exceljet.net/formulas/group-numbers-with-vlookup)
    
*   [Find closest match](https://exceljet.net/formulas/find-closest-match)
    
*   [Lookup number plus or minus N](https://exceljet.net/formulas/lookup-number-plus-or-minus-n)
    

### Functions

*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    

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