# Rank and score with INDEX and MATCH - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/rank-and-score-with-index-and-match

---

[Skip to main content](https://exceljet.net/formulas/rank-and-score-with-index-and-match#main-content)

[](https://exceljet.net/formulas/rank-and-score-with-index-and-match#)

*   [Previous](https://exceljet.net/formulas/quantity-based-discount)
    
*   [Next](https://exceljet.net/formulas/reverse-vlookup-example)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Rank and score with INDEX and MATCH
===================================

by Dave Bruns · Updated 1 Nov 2023

Related functions 
------------------

[RANK](https://exceljet.net/functions/rank-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7153/download?token=VBszrHiI)
 (16.36 KB)

![Excel formula: Rank and score with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/rank%20and%20score%20with%20INDEX%20and%20MATCH.png "Excel formula: Rank and score with INDEX and MATCH")

Summary
-------

To rank and assign points based on a score, you can use [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 with a table that maps rank to points. In the example shown, the formula in E5, copied down, is:

    =INDEX(tblPoints[Points],MATCH([@Rank],tblPoints[Rank],1))
    

where **tblData** (B5:E15) and **tblPoints** (G5:H10) are [Excel Tables](https://exceljet.net/glossary/excel-table)
.

Explanation 
------------

In this example, the goal is to assign points based on a ranked score. The scores to rank are in column C, and the calculated Rank is in column D. Points are awarded based on the table in G5:H10. Both **tblData** (B5:E15) and **tblPoints** (G5:H10) are [Excel Tables](https://exceljet.net/glossary/excel-table)
 created with [Control + T](https://exceljet.net/shortcuts/insert-table)
.

### Background study

*   [Excel Tables](https://exceljet.net/articles/excel-tables)
     (overview)
*   [What is an Excel Table](https://exceljet.net/videos/what-is-an-excel-table)
     (3 min. video)
*   [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)
     (3 min. video)
*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
     (overview)
*   [Basic index and match approximate](https://exceljet.net/formulas/index-and-match-approximate-match)
     (example)

### Calculating rank

The first part of the problem is to calculate the rank of each score in **tblData**. This is done with the [RANK function](https://exceljet.net/functions/rank-function)
 like this:

    =RANK([@Score],[Score])
    

This is an example of a [structured reference](https://exceljet.net/glossary/structured-reference)
, a special kind of reference that makes formulas that deal with Excel Tables easier to work with. Essentially, we get the rank of the current score \[@Score\], against all the other scores in \[Score\].

### Calculating points

Now that we have the rank in column D, we have what we need to calculate points. This is done by looking up the correct number of points to assign with INDEX and MATCH in the **tblPoints** table. The formula in column E is:

    =INDEX(tblPoints[Points],MATCH([@Rank],tblPoints[Rank],1))
    

Working from the inside out, we first figure out what row in the **tblPoints** table applies to the rank we are looking up with the [MATCH function](https://exceljet.net/functions/match-function)
:

    MATCH([@Rank],tblPoints[Rank],1)
    

The _lookup\_value_ is the Rank in column D, and the _lookup\_array_ is **tblPoints\[Rank\]**. _Match\_type_ is provided as 1, because we want to match the largest value in **tblPoints\[Rank\]** that is less than or equal to the Rank in column D. This doesn't affect the first 6 ranks, which will match exactly. But notice that once we reach rank 6, points drop to 3 and this will apply to _every_ rank after 6. Because Katrina's rank is 3, MATCH returns 3, which corresponds to row 3 in **tblPoints**.

MATCH returns this position directly to the [INDEX function](https://exceljet.net/functions/index-function)
 as the _row\_num_ argument. The Points column of **tblPoints** is provided for _array_:

    =INDEX(tblPoints[Points],3) // returns 10
    

INDEX returns 10 as the points awarded to Katrina. The points for the remaining rows in the table are calculated in the same way. See below for an adjustment to assign zero points to ranks after 6.

### No points after rank 6

In the example shown, we assign at least 3 points to every rank using MATCH in approximate match mode. If you want to assign zero points after a rank of 6, one option is to adjust the formula so that the [MATCH function](https://exceljet.net/functions/match-function)
 performs an exact match, then wrap the entire formula in the [IFNA function](https://exceljet.net/functions/ifna-function)
 like this:

    =IFNA(INDEX(tblPoints[Points],MATCH([@Rank],tblPoints[Rank],0)),0)
    

Setting _match\_type_ to 0 causes MATCH to perform an exact match. This will cause MATCH to return the #N/A error for any rank over 6. The IFNA function "catches" this error when it occurs, and returns 0. We could also use the [IFERROR function](https://exceljet.net/functions/iferror-function)
 to do the same thing, but IFERROR will catch _any_ error, so IFNA is a bit more conservative.

_Note: another easy option is to use the original formula, but add another row to the points table with rank = 7 and points = 0._

### With XLOOKUP or VLOOKUP

You can easily use the XLOOKUP function or the VLOOKUP function to lookup points, as an alternative to INDEX and MATCH. With the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
, the formula looks like this:

    =XLOOKUP(tblData[@Rank],tblPoints[Rank],tblPoints[Points],,-1)
    

Note the _match\_mode_ argument works a bit differently than _match\_type_ in the [MATCH function](https://exceljet.net/functions/match-function)
. For exact match or next smaller, we need to use -1.

With the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
, the formula looks like this:

    =VLOOKUP(tblData[@Rank],tblPoints,2,TRUE)
    

The last argument, _range\_lookup_, tells VLOOKUP to use approximate matching. In this mode, VLOOKUP will return an exact match or next smallest value. _Range\_lookup_ is optional and [defaults to TRUE](https://exceljet.net/articles/danger-beware-vlookup-defaults)
, but I like to set a value as a reminder of what is expected. 

### Training

If you want to learn more about Excel Tables or Excel Formulas, we offer [online video training](https://exceljet.net/training)
.

Related formulas
----------------

[![Excel formula: INDEX and MATCH approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match.png "Excel formula: INDEX and MATCH approximate match")](https://exceljet.net/formulas/index-and-match-approximate-match)

### [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table to the right. For convenience only, grade (G5:G9) and score (F5:F9) are named ranges . This is a classic "approximate-match" lookup problem because it is unlikely that a...

Related functions
-----------------

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

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

*   [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)
    

### Functions

*   [RANK Function](https://exceljet.net/functions/rank-function)
    
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