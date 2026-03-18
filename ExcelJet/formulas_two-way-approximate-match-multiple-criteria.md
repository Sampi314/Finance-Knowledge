# Two-way approximate match multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria#main-content)

[](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)
    
*   [Next](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Two-way approximate match multiple criteria
===========================================

by Dave Bruns · Updated 22 Nov 2019

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[IF](https://exceljet.net/functions/if-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/5681/download?token=0PE2u_Un)
 (11.68 KB)

![Excel formula: Two-way approximate match multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/two-way%20approximate%20match%20multiple%20criteria%20v2.png "Excel formula: Two-way approximate match multiple criteria")

Summary
-------

To perform a two-way approximate match lookup with multiple criteria, you can use an array formula based on [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, with help from the [IF function](https://exceljet.net/videos/the-if-function)
 to apply criteria. In the example shown, the formula in K8 is:

    =INDEX(data,MATCH(K6,IF(material=K5,hardness),1),MATCH(K7,diameter,1))
    

where **data** (D6:H16), **diameter** (D5:H5), **material** (B6:B16), and **hardness** (C6:C16) are [named ranges](https://exceljet.net/glossary/named-range)
 used for convenience only.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter_

> _This is an advanced array formula. If you are new to INDEX and MATCH, [start here](https://exceljet.net/articles/index-and-match)
> ._

Explanation 
------------

The goal is to lookup a feed rate based on material, hardness, and drill bit diameter. Feed rate values are in the named range **data** (D6:H16).

This can be done with a two-way INDEX and MATCH formula. One [MATCH function](https://exceljet.net/functions/match-function)
 works out the row number (material and hardness), and the other MATCH function finds the column number (diameter). The [INDEX function](https://exceljet.net/functions/index-function)
 returns the final result.

![Core formula is two-way INDEX and MATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/core%20formua%20is%20two-way%20INDEX%20and%20MATCH.png?itok=3OQwff3k "Core formula is two-way INDEX and MATCH")

In the example shown, the formula in K8 is:

    =INDEX(data,
    MATCH(K6,IF(material=K5,hardness),1), // get row
    MATCH(K7,diameter,1)) // get column
    

(Line breaks added for readability only).

The tricky bit is that material and hardness need to be handled together. We need to restrict MATCH to the hardness values for a given material (Low Carbon Steel in the example shown).

We can do this with the IF function. Essentially, we use IF to "throw away" irrelevant values before we look for a match.

### Details

The INDEX function is given the named range **data** (D6:H16) as for array. The first MATCH function works out the row number:

    MATCH(K6,IF(material=K5,hardness),1) // get row num
    

To locate the correct row, we need to do an exact match on material, and an approximate match on hardness. We do this by using the IF function to first filter out irrelevant hardness:

    IF(material=K5,hardness) // filter
    

We test all of the values in **material** (B6:B16) to see if they match the value in K5 ("Low Carbon Steel"). If so, the hardness value is passed through. If not, IF returns FALSE. The result is an [array](https://exceljet.net/glossary/array)
 like this:

    {FALSE;FALSE;FALSE;85;125;175;225;FALSE;FALSE;FALSE;FALSE}
    

Notice the only surviving values are those associated with Low Carbon Steel. The other values are now FALSE. This array is returned directly to the MATCH function as the lookup\_array.

The lookup value for match comes from K6, which contains the given hardness, 176. MATCH is configured for approximate match by setting match\_type to 1. With these settings, MATCH ignores FALSE values and returns the position of an exact match or the next smallest value.

_Note: hardness values must be sorted in ascending order for each material._

With hardness given as 176, MATCH returns 6, delivered directly to INDEX as the row number. We can now rewrite the original formula like this:

    =INDEX(data,6,MATCH(K7,diameter,1))
    

The second MATCH formula finds the correct column number by performing an approximate match on diameter:

    MATCH(K7,diameter,1) // get column num
    

_Note: values in **diameter** D5:H5 must be sorted in ascending order._

The lookup value comes from K7 (0.75), and the lookup\_array is the named range **diameter** (D5:H5).

As before, the [MATCH](https://exceljet.net/functions/match-function)
 is set to approximate match by setting match\_type to 1.

With diameter given as 0.75, MATCH returns 3, delivered directly to the INDEX function as the column number. The original formula now resolves to:

    =INDEX(data,6,3) // returns 0.015
    

INDEX returns a final result of 0.015, the value from F11.

Related formulas
----------------

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: INDEX and MATCH approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match.png "Excel formula: INDEX and MATCH approximate match")](https://exceljet.net/formulas/index-and-match-approximate-match)

### [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table to the right. For convenience only, grade (G5:G9) and score (F5:F9) are named ranges . This is a classic "approximate-match" lookup problem because it is unlikely that a...

[![Excel formula: Two-way lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20lookup%20with%20INDEX%20and%20MATCH.png "Excel formula: Two-way lookup with INDEX and MATCH")](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

### [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

In this example, the goal is to perform a two-way lookup, sometimes called a matrix lookup . This means we need to create a match on both rows and columns and return the value at the intersection of this two-way match The core of this formula is INDEX, which is simply retrieving a value from C6:G10...

[![Excel formula: INDEX and MATCH approximate match with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match_with_multiple_criteria.png "Excel formula: INDEX and MATCH approximate match with multiple criteria")](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)

### [INDEX and MATCH approximate match with multiple criteria](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)

In this example, the goal is to look up the correct shipping cost for an item based on the shipping service selected and the item's weight. At the core, this is an approximate match lookup based on weight. The challenge is that we also need to filter by service. This means we must apply criteria in...

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

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20do%20a%20two-way%20lookup%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

### [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

In this video we'll look at how to set up a classic two-way lookup using INDEX and MATCH . Here we have a list of salespeople with monthly sales figures. What we want to do is add a formula in Q6 that looks up and retrieves a sales number based on the name and month above. To do this, we'll use the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20MATCH%20to%20find%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-match-to-find-approximate-matches)

### [How to use MATCH to find approximate matches](https://exceljet.net/videos/how-to-use-match-to-find-approximate-matches)

In this video we'll look at how to use the MATCH function to find approximate matches. This is useful for things like determining a commission tier based on a sales number, figuring out a tax rate based on income, or calculating postage based on weight. Let's take a look. In this example, we have a...

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

*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)
    
*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    
*   [INDEX and MATCH approximate match with multiple criteria](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)
    
*   [How to use MATCH to find approximate matches](https://exceljet.net/videos/how-to-use-match-to-find-approximate-matches)
    
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