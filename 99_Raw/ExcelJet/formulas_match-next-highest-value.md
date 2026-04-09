# Match next highest value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/match-next-highest-value

---

[Skip to main content](https://exceljet.net/formulas/match-next-highest-value#main-content)

[](https://exceljet.net/formulas/match-next-highest-value#)

*   [Previous](https://exceljet.net/formulas/match-long-text)
    
*   [Next](https://exceljet.net/formulas/max-if-criteria-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Match next highest value
========================

by Dave Bruns · Updated 30 Apr 2017

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Match next highest value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/match%20next%20highest%20value.png "Excel formula: Match next highest value")

Summary
-------

To match the "next highest" value in a lookup table, you can use a formula based on INDEX and MATCH. In the example shown, the formula in F6 is:

    =INDEX(level,MATCH(F4,points)+1)
    

where "level" is the named range C5:C9, and "points" is the named range B5:B9.

Generic formula
---------------

    =INDEX(data,MATCH(lookup,values)+1)

Explanation 
------------

This formula is a standard version of INDEX + MATCH with a small twist.

Working from the inside out, MATCH is used find the correct row number for the value in F4, 2100. Without the third argument, match\_type, defined, MATCH defaults to approximate match and returns 2.

The small twist is that we add 1 to this result to override the matched result and return 3 as the row number for INDEX.

With level (C5:C9) supplied as the array, and 3 as the row number, INDEX returns "Gold":

    =INDEX(level,3) // returns Gold
    

### Another option

The above approach works fine for simple lookups. If you want to use MATCH to find the "next largest" match in more traditional way, you can sort the lookup array in descending order, and [use MATCH as described on this page](https://exceljet.net/formulas/next-largest-match-with-the-match-function)
.

Related formulas
----------------

[![Excel formula: Next largest match with the MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Next%20largest%20match%20with%20the%20MATCH%20function.png "Excel formula: Next largest match with the MATCH function")](https://exceljet.net/formulas/next-largest-match-with-the-match-function)

### [Next largest match with the MATCH function](https://exceljet.net/formulas/next-largest-match-with-the-match-function)

The default behavior of the MATCH function is to match the "next smallest" value in a list that's sorted in ascending order. Essentially, MATCH moves forward in the list until it encounters a value larger than the lookup value, then drops back to the previous value. So, when lookup values are...

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

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Next largest match with the MATCH function](https://exceljet.net/formulas/next-largest-match-with-the-match-function)
    
*   [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)
    

### Functions

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