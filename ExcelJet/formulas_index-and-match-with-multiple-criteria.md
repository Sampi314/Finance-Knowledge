# INDEX and MATCH with multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/index-and-match-with-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/index-and-match-with-multiple-criteria#main-content)

[](https://exceljet.net/formulas/index-and-match-with-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/index-and-match-two-column-lookup)
    
*   [Next](https://exceljet.net/formulas/index-and-match-with-variable-columns)
    

[Lookup](https://exceljet.net/formulas#Lookup)

INDEX and MATCH with multiple criteria
======================================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/5380/download?token=ATZDmPLa)
 (15.02 KB)

![Excel formula: INDEX and MATCH with multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/INDEX%20and%20MATCH%20with%20multiple%20criteria.png "Excel formula: INDEX and MATCH with multiple criteria")

Summary
-------

To lookup values with INDEX and MATCH, using multiple criteria, you can use an array formula. In the example shown, the formula in H8 is:

    =INDEX(E5:E11,MATCH(1,(H5=B5:B11)*(H6=C5:C11)*(H7=D5:D11),0))
    

The result is $17.00, the price of a Large Red T-shirt. This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
.

_Note: In the current version of Excel, you can use the [same approach](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
 with the XLOOKUP function._

Generic formula
---------------

    =INDEX(range1,MATCH(1,(A1=range2)*(B1=range3)*(C1=range4),0))

Explanation 
------------

This is a more advanced formula. For basics, see [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

Normally, an INDEX MATCH formula is configured with MATCH set to look through a one-column range and provide a match based on given criteria. Without concatenating values in a [helper column](https://exceljet.net/glossary/helper-column)
, or in the formula itself, there's no way to supply more than one criteria.

This formula works around this limitation by using [boolean logic](https://exceljet.net/glossary/boolean-logic)
 to create an [array](https://exceljet.net/glossary/array)
 of ones and zeros to represent rows matching all 3 criteria, then using MATCH to match the first 1 found. The temporary array of ones and zeros is generated with this snippet:

    (H5=B5:B11)*(H6=C5:C11)*(H7=D5:D11)
    

Here we compare the item in H5 against all items, the size in H6 against all sizes, and the color in H7 against all colors. The initial result is three arrays of TRUE/FALSE results like this:

    {TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;TRUE}*{FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE}*{TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE}
    

Tip: [use F9 to see these results](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
. Just select an expression in the formula bar, and press F9.

The math operation (multiplication) transforms the TRUE FALSE values to 1s and 0s:

    {1;1;1;0;0;0;1}*{0;0;1;0;0;1;0}*{1;0;1;0;0;0;1}
    

After multiplication, we have a single array like this:

    {0;0;1;0;0;0;0}
    

which is fed into the MATCH function as the lookup array, with a lookup value of 1:

    MATCH(1,{0;0;1;0;0;0;0})
    

At this point, the formula is a standard INDEX MATCH formula. The MATCH function returns 3 to INDEX:

    =INDEX(E5:E11,3)
    

and INDEX returns a final result of $17.00.

### Array visualization

The arrays explained above can be difficult to visualize. The image below shows the basic idea. Columns B, C, and D correspond to the data in the example. Column F is created by multiplying the three columns together. It is the array handed off to MATCH.

![INDEX and MATCH with multiple criteria - array visualization](https://exceljet.net/sites/default/files/images/formulas/inline/INDEX%20and%20MATCH%20with%20multiple%20criteria%20array%20visualization.png "INDEX and MATCH with multiple criteria - array visualization")

### Non-array version

It is possible to add another INDEX to this formula, avoiding the need to enter as an array formula with control + shift + enter:

    =INDEX(rng1,MATCH(1,INDEX((A1=rng2)*(B1=rng3)*(C1=rng4),0,1),0))
    

The INDEX function can handle arrays natively, so the second INDEX is added only to "catch" the array created with the boolean logic operation and return the same array again to MATCH. To do this, INDEX is configured with zero rows and one column. The zero row trick causes INDEX to return column 1 from the array (which is already one column anyway).

Why would you want the non-array version? Sometimes, people forget to enter an array formula with control + shift + enter, and the formula returns an incorrect result. So, a non-array formula is more "bulletproof". However, the tradeoff is a more complex formula.

_Note: In [Excel 365](https://exceljet.net/glossary/excel-365)
, it is not necessary to enter array formulas in a special way._

Related formulas
----------------

[![Excel formula: VLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20muliple%20criteria.png "Excel formula: VLOOKUP with multiple criteria")](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

### [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

In the example shown, we want to look up employee departments and groups using VLOOKUP by matching the first and last name of an employee. One limitation of VLOOKUP is that it only handles one condition: the lookup\_value, which is matched against the first column in the table. This makes it...

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: INDEX and MATCH case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case-sensitive%20INDEX%20and%20MATCH.png "Excel formula: INDEX and MATCH case-sensitive ")](https://exceljet.net/formulas/index-and-match-case-sensitive)

### [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the first name in column B, based on a lookup value in cell F6. By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP , XLOOKUP , and INDEX and MATCH . These formulas will simply return...

[![Excel formula: SUMIFS multiple criteria lookup in table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS%20multiple%20criteria%20lookup%20in%20table.png "Excel formula: SUMIFS multiple criteria lookup in table")](https://exceljet.net/formulas/sumifs-multiple-criteria-lookup-in-table)

### [SUMIFS multiple criteria lookup in table](https://exceljet.net/formulas/sumifs-multiple-criteria-lookup-in-table)

This example shows how the SUMIFS function can sometimes be used to "lookup" numeric values, as an alternative to more complicated multi-criteria lookup formulas. This approach is less flexible than more general lookup formulas based on INDEX and MATCH (or VLOOKUP) but it's also more...

[![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

### [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for lookup\_value and lookup\_array . How can we...

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

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20do%20a%20two-way%20lookup%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

### [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

In this video we'll look at how to set up a classic two-way lookup using INDEX and MATCH . Here we have a list of salespeople with monthly sales figures. What we want to do is add a formula in Q6 that looks up and retrieves a sales number based on the name and month above. To do this, we'll use the...

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

*   [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
    
*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)
    
*   [SUMIFS multiple criteria lookup in table](https://exceljet.net/formulas/sumifs-multiple-criteria-lookup-in-table)
    
*   [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    
*   [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)
    
*   [Two-way lookup with INDEX and MATCH approximate](https://exceljet.net/videos/two-way-lookup-with-index-and-match-approximate)
    

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