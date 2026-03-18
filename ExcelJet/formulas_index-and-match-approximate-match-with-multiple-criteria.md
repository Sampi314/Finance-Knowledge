# INDEX and MATCH approximate match with multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria#main-content)

[](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/index-and-match-approximate-match)
    
*   [Next](https://exceljet.net/formulas/index-and-match-case-sensitive)
    

[Lookup](https://exceljet.net/formulas#Lookup)

INDEX and MATCH approximate match with multiple criteria
========================================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[IF](https://exceljet.net/functions/if-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7761/download?token=j9CeGERs)
 (18.58 KB)

![Excel formula: INDEX and MATCH approximate match with multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/INDEX_and_MATCH_approximate_match_with_multiple_criteria.png "Excel formula: INDEX and MATCH approximate match with multiple criteria")

Summary
-------

To perform an approximate match lookup with multiple criteria, you can use an [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula, with help from the [IF function](https://exceljet.net/videos/the-if-function)
. In the example shown, the formula in G8 is:

    =INDEX(data[Cost],MATCH(G7,IF(data[Service]=G6,data[Weight]),1))
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D16. With "2-Day Air" in cell G6 and 72 in cell G7, the formula returns $45.00.

_Notes: (1) This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter in [older versions of Excel](https://exceljet.net/glossary/legacy-excel)
. (2) In the current version of Excel, you can use the same approach with an [XLOOKUP formula](https://exceljet.net/formulas/xlookup-approximate-match-with-multiple-criteria)
._

Generic formula
---------------

    =INDEX(range,MATCH(value,IF(range=A1,range),1))

Explanation 
------------

In this example, the goal is to look up the correct shipping cost for an item based on the shipping service selected and the item's weight. At the core, this is an approximate match lookup based on weight. The challenge is that we also need to filter by service. This means we must apply criteria in two steps: (1) match based on Service and (2) match based on Weight. The screen below shows the basic idea:

![INDEX and MATCH with two conditions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/INDEX_and_MATCH_approximate_match_with_multiple_criteria_cropped.png "INDEX and MATCH with two conditions")

One way to solve this problem is with an [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 and the [IF function](https://exceljet.net/functions/if-function)
 to perform the required filtering. This works because the IF function returns 12 results, which map to the 12 rows in the table. This means MATCH will still return the correct row in the table even after IF has filtered out the other weights. See below for more details.

### Background reading

This article assumes you are familiar with Excel Tables and INDEX and MATCH. If not, see:

*   [Excel Tables](https://exceljet.net/articles/excel-tables)
     - introduction and overview
*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
     - overview with simple examples

### Basic INDEX and MATCH

In INDEX and MATCH formulas, the MATCH function finds the position of an item in a range, and the INDEX function returns the value at that position. If you are new to INDEX and MATCH, [see this overview](https://exceljet.net/articles/index-and-match)
.

Looking at this example from the inside out, the core of the solution is an approximate match lookup based on weight. To illustrate, the screen below shows a simplified version of the same problem with the Service removed completely:

![INDEX and MATCH simple approximate match](https://exceljet.net/sites/default/files/images/formulas/inline/INDEX_and_MATCH_simple_approximate_match.png "INDEX and MATCH simple approximate match")

The formula in cell F5 is:

    =INDEX(C5:C8,MATCH(F4,B5:B8,1))

Notice the _match\_type_ argument inside MATCH is set to 1, to locate the largest value in B5:B8 that is _less than or equal to_ the lookup value in cell F4. In this case, the largest value less than or equal to 72 is 60, so MATCH returns 3 to INDEX as a row number, and INDEX returns $18.00 as a final result:

    =INDEX(C5:C8,3) // returns 18

So far, so good. We have a simple working formula that returns the correct cost based on an approximate match lookup. The complication is that we also need to match based on Service. To do that, we need to extend the formula to handle multiple criteria.

### Adding criteria for service

We know how to look up costs based on weight. The remaining challenge is that we also need to take into account Service. For simple exact-match scenarios, we can use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
, [as explained here](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
. But in this example, we need to perform an approximate match, so using Boolean logic will become complicated. Another approach is to "filter out" extraneous entries in the table so we are left only with entries that correspond to the Service we are looking up. The classic way to do this is with the [IF function](https://exceljet.net/functions/if-function)
. This is the approach used in the example shown, where the formula in cell G8 is:

    =INDEX(data[Cost],MATCH(G7,IF(data[Service]=G6,data[Weight]),1))

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

The filtering is done with the IF function, which appears inside the MATCH function like this:

    IF(data[Service]=G6,data[Weight])

This code tests the values in the Service column to see if they match the value in G6. Where there is a match, the corresponding values in with Weight column are returned. If there is no match, the IF function returns FALSE. Because there are 12 rows in the table, the IF function returns an [array](https://exceljet.net/glossary/array)
 that contains 12 results like this:

    {FALSE;FALSE;FALSE;FALSE;1;16;60;120;FALSE;FALSE;FALSE;FALSE}

Notice the only weights that remain in the array are those that correspond to the "2-Day-Air" service; all other weights have been replaced with FALSE. You can visualize this operation in the original data like this:

![What the weights look like after the IF function runs](https://exceljet.net/sites/default/files/images/formulas/inline/INDEX_and_MATCH_approximate_match_after_IF_function.png "What the weights look like after the IF function runs")

This [array](https://exceljet.net/glossary/array)
 is delivered directly to the [MATCH function](https://exceljet.net/functions/match-function)
 as the _lookup\_array:_

    MATCH(G7,{FALSE;FALSE;FALSE;FALSE;1;16;60;120;FALSE;FALSE;FALSE;FALSE},1)

The MATCH function then simply ignores the FALSE values and tries to match the remaining numbers. With a weight of 72 in cell G7, the MATCH function matches 60 and returns 7 to the INDEX function as _row\_num_:

    =INDEX(data[Cost],7)  // returns 45

With a row number of 7, INDEX returns $45.00 as the final result.

_Remember that we are using MATCH in an approximate match mode. With m__atch\_type set to 1, values in the Weight column must be sorted in ascending order for MATCH to work correctly. See our [MATCH function page](https://exceljet.net/functions/match-function)
 for more information._

Related formulas
----------------

[![Excel formula: INDEX and MATCH approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match.png "Excel formula: INDEX and MATCH approximate match")](https://exceljet.net/formulas/index-and-match-approximate-match)

### [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table to the right. For convenience only, grade (G5:G9) and score (F5:F9) are named ranges . This is a classic "approximate-match" lookup problem because it is unlikely that a...

[![Excel formula: Two-way approximate match multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20approximate%20match%20multiple%20criteria%20v2.png "Excel formula: Two-way approximate match multiple criteria")](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)

### [Two-way approximate match multiple criteria](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)

The goal is to lookup a feed rate based on material, hardness, and drill bit diameter. Feed rate values are in the named range data (D6:H16). This can be done with a two-way INDEX and MATCH formula. One MATCH function works out the row number (material and hardness), and the other MATCH function...

[![Excel formula: XLOOKUP approximate match with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_approximate_match_with_multiple_criteria.png "Excel formula: XLOOKUP approximate match with multiple criteria")](https://exceljet.net/formulas/xlookup-approximate-match-with-multiple-criteria)

### [XLOOKUP approximate match with multiple criteria](https://exceljet.net/formulas/xlookup-approximate-match-with-multiple-criteria)

In this example, the goal is to look up the correct shipping cost for an item based on the shipping service selected and the weight of the item. The challenge is that we also need to filter by service. This means we need to apply criteria in two steps: (1) match based on Service, and (2) match...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

### [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

In this video we're going to combine INDEX and MATCH together to look things up. Here we have the city population data we looked at before. We used the INDEX function to retrieve information about a city with a hard-coded position value. When we supply a number, INDEX retrieves information for the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Two-way%20lookup%20with%20INDEX%20and%20MATCH%20approximate-Thumb.png)](https://exceljet.net/videos/two-way-lookup-with-index-and-match-approximate)

### [Two-way lookup with INDEX and MATCH approximate](https://exceljet.net/videos/two-way-lookup-with-index-and-match-approximate)

In this video we'll look at how to build a two-way lookup with INDEX and MATCH using an approximate match. Here we have a simple cost calculator which looks up cost based on a material's width and height. The match needs to be approximate. For example, if the width is 250, and the height is 325,...

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
    
*   [Two-way approximate match multiple criteria](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)
    
*   [XLOOKUP approximate match with multiple criteria](https://exceljet.net/formulas/xlookup-approximate-match-with-multiple-criteria)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    
*   [Two-way lookup with INDEX and MATCH approximate](https://exceljet.net/videos/two-way-lookup-with-index-and-match-approximate)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Excel Tables](https://exceljet.net/training/excel-tables)
    

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