# Next largest match with the MATCH function - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/next-largest-match-with-the-match-function

---

[Skip to main content](https://exceljet.net/formulas/next-largest-match-with-the-match-function#main-content)

[](https://exceljet.net/formulas/next-largest-match-with-the-match-function#)

*   [Previous](https://exceljet.net/formulas/nearest-location-with-xmatch)
    
*   [Next](https://exceljet.net/formulas/partial-match-with-numbers-and-wildcard)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Next largest match with the MATCH function
==========================================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Next largest match with the MATCH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Next%20largest%20match%20with%20the%20MATCH%20function.png "Excel formula: Next largest match with the MATCH function")

Summary
-------

To look up the "next largest" match in a set of values, you can use the MATCH function in approximate match mode, with -1 for match type. In the example shown, the formula in F7 is:

    =MATCH(F6,length,-1)
    

where "length" is the named range B5:B11, and "cost" is the named range C5:C11.

Generic formula
---------------

    =MATCH(value,array,-1)

Explanation 
------------

The default behavior of the MATCH function is to match the "next smallest" value in a list that's sorted in ascending order. Essentially, MATCH moves forward in the list until it encounters a value larger than the lookup value, then drops back to the previous value.

So, when lookup values are sorted in ascending order, both of these formulas return "next smallest":

    =MATCH(value,array) // default
    =MATCH(value,array,1) // explicit
    

However, by setting match type to -1, and sorting lookup values in descending order, MATCH will return the next largest match. So, as seen in the example:

    =MATCH(F6,length,-1)
    

returns 4, since 400 is the next largest match after 364.

### Find associated cost

The full INDEX/MATCH formula to retrieve the associated cost in cell F8 is:

    =INDEX(cost,MATCH(F6,length,-1))
    

Related formulas
----------------

[![Excel formula: Match next highest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/match%20next%20highest%20value.png "Excel formula: Match next highest value")](https://exceljet.net/formulas/match-next-highest-value)

### [Match next highest value](https://exceljet.net/formulas/match-next-highest-value)

This formula is a standard version of INDEX + MATCH with a small twist. Working from the inside out, MATCH is used find the correct row number for the value in F4, 2100. Without the third argument, match\_type, defined, MATCH defaults to approximate match and returns 2. The small twist is that we...

[![Excel formula: INDEX and MATCH approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match.png "Excel formula: INDEX and MATCH approximate match")](https://exceljet.net/formulas/index-and-match-approximate-match)

### [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table to the right. For convenience only, grade (G5:G9) and score (F5:F9) are named ranges . This is a classic "approximate-match" lookup problem because it is unlikely that a...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20MATCH%20Function%20for%20exact%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

### [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

The MATCH function finds the relative position of an item in a list. MATCH can find exact matches or approximate matches. In this video, we'll look at how to use MATCH to find an exact match. The MATCH function takes three arguments: the lookup\_value, which is the value you're looking up, the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Match next highest value](https://exceljet.net/formulas/match-next-highest-value)
    
*   [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    

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