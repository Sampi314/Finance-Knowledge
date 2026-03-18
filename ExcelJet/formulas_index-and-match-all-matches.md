# INDEX and MATCH all matches - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/index-and-match-all-matches

---

[Skip to main content](https://exceljet.net/formulas/index-and-match-all-matches#main-content)

[](https://exceljet.net/formulas/index-and-match-all-matches#)

*   [Previous](https://exceljet.net/formulas/index-and-match-advanced-example)
    
*   [Next](https://exceljet.net/formulas/index-and-match-all-partial-matches)
    

[Lookup](https://exceljet.net/formulas#Lookup)

INDEX and MATCH all matches
===========================

by Dave Bruns · Updated 5 Apr 2023

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[AND](https://exceljet.net/functions/and-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: INDEX and MATCH all matches](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/extract%20data%20with%20helper%20column4.png "Excel formula: INDEX and MATCH all matches")

Summary
-------

To return all matches with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 you can use a [helper column](https://exceljet.net/glossary/helper-column)
 to identify matching data. This avoids the complexity of a more advanced array formula and keeps the formula fast. In the example shown, the formula in H6 is:

    =IF($G6<=ct,INDEX(data,MATCH($G6,helper,0),1),"")
    

where **ct** (G3), **data** (B3:E52), and **helper** (E3:E52) are [named ranges](https://exceljet.net/glossary/named-range)
.

_Note: in the current version of Excel, the [FILTER function](https://exceljet.net/functions/filter-function)
 is a better way to solve this problem. The INDEX and MATCH formula explained here is meant for [legacy versions of Excel](https://exceljet.net/glossary/legacy-excel)
 that do not provide the FILTER function._

Generic formula
---------------

    =IF(rowcheck,INDEX(data,MATCH(rownum,helper,0),column),"")
    
    

Explanation 
------------

_Note: in more recent versions of Excel, the [FILTER function](https://exceljet.net/functions/filter-function)
 is a better way to solve this problem. The INDEX and MATCH formula explained here is meant for [legacy versions of Excel](https://exceljet.net/glossary/legacy-excel)
 that do not provide the FILTER function._

By default, lookup formulas in Excel like [VLOOKUP](https://exceljet.net/functions/vlookup-function)
 and [INDEX + MATCH](https://exceljet.net/articles/index-and-match)
 will find the _first match_, but not other matches that may exist in a set of data. However, with some effort, you can make INDEX and MATCH return all matches. One way to approach this problem is to use a helper column to return a numeric value that indicates a match. This makes it much easier to identify and extract multiple matches.

### Helper column

A [helper column](https://exceljet.net/glossary/helper-column)
 is a way to simplify a complex formula in Excel by breaking the problem down into smaller steps. In the worksheet shown, a helper column is used to identify matching data based on conditions entered in the range I3:J3. The formula in the helper column in cell E3 looks like this:

    =SUM(E2,AND(C3=$I$3,D3=$J$3))
    

The helper column tests each row in the data to see if the Department in column C matches the value in I3 and the Building in column D matches the value in J3. Both logical tests must return TRUE in order for AND to return TRUE.

For each row, the result from the [AND function](https://exceljet.net/functions/and-function)
 is added to the "value above" in the helper column to generate a count. The practical effect of this formula is an incrementing counter that only changes when a (new) match is found. Then the value remains the same until the next match is found. This works because the TRUE/FALSE results return by AND are coerced to 1/0 values as part of the sum operation. FALSE results add nothing and TRUE results add 1.

Back in the extraction area, the lookup formula for Name in column H looks like this:

    =IF($G6<=ct,INDEX(data,MATCH($G6,helper,0),1),"")
    

Working from the inside out, the INDEX + MATCH part of the formula looks up the name for the first match found, using the row number in column G as the match value:

    INDEX(data,MATCH($G6,helper,0),1)
    

[INDEX](https://exceljet.net/functions/index-function)
 receives all 3 columns of data as the array (named range "data"), and [MATCH](https://exceljet.net/functions/match-function)
 is configured to match the row number inside the helper column (the named range "helper") in exact match mode (3rd argument set to zero).

This is where the cleverness of the formula becomes apparent. The helper column obviously contains duplicates, but it doesn't matter, because MATCH will match only the first value. By design, each "first value" corresponds to the correct row in the data table.

The formulas in columns I and J are the same as H, except for the column number, which is increased in each case by one.

The IF statement that wraps the INDEX/MATCH formula performs a simple function — it checks each row number in the extraction area to see if the row number is less than or equal to the value in G3 ([named range](https://exceljet.net/glossary/named-range)
 "ct"), which is the total count of all matching records. If so, the INDEX/MATCH logic is run. If not, IF outputs an [empty string](https://exceljet.net/glossary/empty-string)
 ("").

The formula in G3 (named range "ct") is simple:

    =MAX(helper)
    

Since the maximum value in the helper column is the same as the total match count, the MAX function is all we need.

_Note: the extraction area needs to be manually configured to handle as much data as needed (i.e. 5 rows, 10 rows, 20 rows, etc.). In this example, it is limited to 5 rows only to keep the worksheet compact._

_I learned this technique in [Mike Girvin's](https://www.youtube.com/user/excelisfun)
 book [Control + Shift + Enter](http://www.amazon.com/gp/product/1615470077/?tag=exceljet-20)
._

### The FILTER function

If you have a [current version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, the [FILTER function](https://exceljet.net/functions/filter-function)
 is a better way to extract all matching records.

Related formulas
----------------

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: Get nth match with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_match_with_VLOOKUP.png "Excel formula: Get nth match with VLOOKUP")](https://exceljet.net/formulas/get-nth-match-with-vlookup)

### [Get nth match with VLOOKUP](https://exceljet.net/formulas/get-nth-match-with-vlookup)

The table contains basic order information, with columns for Date, Product, Name, and Amount. The Helper column is used to create a special lookup value, as explained below. The goal is to retrieve the nth matching record in a table for a specific product, which is entered in cell I4. For example,...

[![Excel formula: INDEX and MATCH all partial matches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_all_partial_matches.png "Excel formula: INDEX and MATCH all partial matches")](https://exceljet.net/formulas/index-and-match-all-partial-matches)

### [INDEX and MATCH all partial matches](https://exceljet.net/formulas/index-and-match-all-partial-matches)

Note: in the current version of Excel, the FILTER function is a better way to solve this problem. The INDEX and MATCH formula explained here is meant for legacy versions of Excel that do not provide the FILTER function. The core of this formula is the INDEX function, with AGGREGATE used to figure...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

### [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

In this video we're going to combine INDEX and MATCH together to look things up. Here we have the city population data we looked at before. We used the INDEX function to retrieve information about a city with a hard-coded position value. When we supply a number, INDEX retrieves information for the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [Get nth match with VLOOKUP](https://exceljet.net/formulas/get-nth-match-with-vlookup)
    
*   [INDEX and MATCH all partial matches](https://exceljet.net/formulas/index-and-match-all-partial-matches)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

### Videos

*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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