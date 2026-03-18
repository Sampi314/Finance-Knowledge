# INDEX and MATCH approximate match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/index-and-match-approximate-match

---

[Skip to main content](https://exceljet.net/formulas/index-and-match-approximate-match#main-content)

[](https://exceljet.net/formulas/index-and-match-approximate-match#)

*   [Previous](https://exceljet.net/formulas/index-and-match-all-partial-matches)
    
*   [Next](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)
    

[Lookup](https://exceljet.net/formulas#Lookup)

INDEX and MATCH approximate match
=================================

by Dave Bruns · Updated 27 Mar 2023

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: INDEX and MATCH approximate match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/INDEX_and_MATCH_approximate_match.png "Excel formula: INDEX and MATCH approximate match")

Summary
-------

This example shows how to use [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 to calculate the correct grade for a given score using an external table. This requires an "approximate match" since it is unlikely that the actual score exists in the table. The formula in cell D5 is:

    =INDEX(grade,MATCH(C5,score,1))
    

where **grade** (G5:G9) and **score** (F5:F9) are [named ranges](https://exceljet.net/glossary/named-range)
. In cell D5, the formula returns "C", the correct grade for a score of 79. As the formula is copied down, a grade is returned for each name in the list.

Generic formula
---------------

    =INDEX(grade,MATCH(A1,score,1))

Explanation 
------------

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table to the right. For convenience only, **grade** (G5:G9) and **score** (F5:F9) are [named ranges](https://exceljet.net/glossary/named-range)
. This is a classic "approximate-match" lookup problem because it is unlikely that a score will be found in the lookup table. Instead, the table acts to group scores into buckets. For a given score, we want to match the largest value in the table that is less than or equal to the score. This problem can be solved with an [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula like this:

    =INDEX(grade,MATCH(C5,score,1))

### Background reading

This article assumes you are familiar with INDEX and MATCH. If not, see:

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
     - overview with simple examples

### The MATCH function

The [MATCH function](https://exceljet.net/functions/match-function)
 locates a value in a set of data and returns its _position_. In this example, the formula uses MATCH to find the correct row for a given score. MATCH is configured to look for the value in C5 in the named range **score** (F5:F9):

    MATCH(C5,score,1) // returns 3
    

Here, the _lookup\_value_ is the score in C5, the _lookup\_array_ is the named range **score** (F5:F9), and _match\_type_ is set to 1, for an approximate match. A match type of 1 will cause MATCH to find the first value in the table that is less than or equal to the lookup value in C5. In this case, the score is 79, so MATCH returns 3. Now that we have the correct row number, we need to retrieve the grade in that row. This is a job for the INDEX function.

### The INDEX function

The [INDEX function](https://exceljet.net/functions/index-function)
 is designed to retrieve values at a known location. In this example, the MATCH function returns a result of 3 directly to the INDEX function as the _row\_num_ argument. Once MATCH returns 3 we can simplify the formula to:

    =INDEX(grade,3) // returns "C"
    

With _array_ provided as the named range **grade** (G5:G9) and a row number of 3, INDEX returns the value at the 3rd row in G5:G9, which is "C".

_Note: For MATCH to work correctly with match\_type of 1, the scores in_ F5:F9 _must be sorted in ascending order. For more information, see our [MATCH function page](https://exceljet.net/functions/match-function)
._

Related formulas
----------------

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: INDEX and MATCH case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case-sensitive%20INDEX%20and%20MATCH.png "Excel formula: INDEX and MATCH case-sensitive ")](https://exceljet.net/formulas/index-and-match-case-sensitive)

### [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the first name in column B, based on a lookup value in cell F6. By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP , XLOOKUP , and INDEX and MATCH . These formulas will simply return...

[![Excel formula: Two-way lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20lookup%20with%20INDEX%20and%20MATCH.png "Excel formula: Two-way lookup with INDEX and MATCH")](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

### [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

In this example, the goal is to perform a two-way lookup, sometimes called a matrix lookup . This means we need to create a match on both rows and columns and return the value at the intersection of this two-way match The core of this formula is INDEX, which is simply retrieving a value from C6:G10...

[![Excel formula: Match next highest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/match%20next%20highest%20value.png "Excel formula: Match next highest value")](https://exceljet.net/formulas/match-next-highest-value)

### [Match next highest value](https://exceljet.net/formulas/match-next-highest-value)

This formula is a standard version of INDEX + MATCH with a small twist. Working from the inside out, MATCH is used find the correct row number for the value in F4, 2100. Without the third argument, match\_type, defined, MATCH defaults to approximate match and returns 2. The small twist is that we...

[![Excel formula: INDEX and MATCH descending order](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20and%20MATCH%20descending%20order.png "Excel formula: INDEX and MATCH descending order")](https://exceljet.net/formulas/index-and-match-descending-order)

### [INDEX and MATCH descending order](https://exceljet.net/formulas/index-and-match-descending-order)

This formula uses -1 for match type to allow an approximate match on values sorted in descending order. The MATCH part of the formula looks like this: MATCH(F4,B5:B9,-1) Using the lookup value in cell F4, MATCH finds the first value in B5:B9 that is greater than or equal to the lookup value. If an...

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

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

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

*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)
    
*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    
*   [Match next highest value](https://exceljet.net/formulas/match-next-highest-value)
    
*   [INDEX and MATCH descending order](https://exceljet.net/formulas/index-and-match-descending-order)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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