# Lookup lowest value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lookup-lowest-value

---

[Skip to main content](https://exceljet.net/formulas/lookup-lowest-value#main-content)

[](https://exceljet.net/formulas/lookup-lowest-value#)

*   [Previous](https://exceljet.net/formulas/lookup-lowest-monday-tide)
    
*   [Next](https://exceljet.net/formulas/lookup-number-plus-or-minus-n)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Lookup lowest value
===================

by Dave Bruns · Updated 17 Apr 2021

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[MIN](https://exceljet.net/functions/min-function)

![Excel formula: Lookup lowest value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lookup%20lowest%20value.png "Excel formula: Lookup lowest value")

Summary
-------

To lookup information associated with the lowest value in table, you can use a formula based on INDEX, MATCH, and MIN functions.

In the example shown, a formula is used to identify the name of the contractor with the lowest bid. The formula in F6 is:

    =INDEX(B5:B9,MATCH(MIN(C5:C9),C5:C9,0))
    

Generic formula
---------------

    =INDEX(range,MATCH(MIN(vals),vals,0))

Explanation 
------------

Working from the inside out, the MIN function is used to find the lowest bid in the range C5:C9:

    MIN(C5:C9) // returns 99500
    

The result, 99500, is fed into the MATCH function as the lookup value:

    MATCH(99500,C5:C9,0) // returns 4
    

Match then returns the location of this value in the range, 4, which goes into INDEX as the row number along with B5:B9 as the array:

    =INDEX(B5:B9, 4) // returns Cymbal
    

The INDEX function then returns the value at that position: Cymbal.

Related formulas
----------------

[![Excel formula: INDEX and MATCH case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case-sensitive%20INDEX%20and%20MATCH.png "Excel formula: INDEX and MATCH case-sensitive ")](https://exceljet.net/formulas/index-and-match-case-sensitive)

### [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the first name in column B, based on a lookup value in cell F6. By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP , XLOOKUP , and INDEX and MATCH . These formulas will simply return...

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: Minimum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_if_multiple_criteria.png "Excel formula: Minimum if multiple criteria")](https://exceljet.net/formulas/minimum-if-multiple-criteria)

### [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)

In this example, the goal is to get the minimum value for a given group above a specific temperature. In other words, we want the min value after applying multiple criteria. The easiest way to solve this problem is with the MINIFS function. However, if you need more flexibility (for example, you...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20MATCH%20Function%20for%20exact%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

### [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

The MATCH function finds the relative position of an item in a list. MATCH can find exact matches or approximate matches. In this video, we'll look at how to use MATCH to find an exact match. The MATCH function takes three arguments: the lookup\_value, which is the value you're looking up, the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20do%20a%20two-way%20lookup%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

### [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

In this video we'll look at how to set up a classic two-way lookup using INDEX and MATCH . Here we have a list of salespeople with monthly sales figures. What we want to do is add a formula in Q6 that looks up and retrieves a sales number based on the name and month above. To do this, we'll use the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)
    
*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    
*   [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)
    

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