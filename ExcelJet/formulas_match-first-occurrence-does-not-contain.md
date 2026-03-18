# Match first occurrence does not contain - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/match-first-occurrence-does-not-contain

---

[Skip to main content](https://exceljet.net/formulas/match-first-occurrence-does-not-contain#main-content)

[](https://exceljet.net/formulas/match-first-occurrence-does-not-contain#)

*   [Previous](https://exceljet.net/formulas/match-first-error)
    
*   [Next](https://exceljet.net/formulas/match-long-text)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Match first occurrence does not contain
=======================================

by Dave Bruns · Updated 15 Jun 2020

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SEARCH](https://exceljet.net/functions/search-function)

![Excel formula: Match first occurrence does not contain](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/match%20first%20occurrence%20does%20not%20contain.png "Excel formula: Match first occurrence does not contain")

Summary
-------

To get the position of the first match that does not contain a specific value, you can use an [array formula](https://exceljet.net/glossary/array-formula)
 based on the MATCH, SEARCH, and ISNUMBER functions. In the example shown, the formula in E5 is:

    {=MATCH(FALSE,data="red",0)}
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 B5"B12.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Generic formula
---------------

    {=MATCH(FALSE,logical_test,0)}

Explanation 
------------

This formula depends on a TRUE or FALSE result from a logical test, where FALSE represents the value you are looking for. In the example, the logical test is data="red", entered as the lookup\_array argument in the MATCH function:

    =MATCH(FALSE,data="red",0)
    

Once the test is run, it returns an array or TRUE and FALSE values:

    =MATCH(FALSE,{TRUE;TRUE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE},0)
    

With the lookup\_value set to FALSE, and match\_type set to zero to force and exact match, the MATCH function returns 4, the position of the first FALSE in the array.

### Get associated value

To retrieve the associated value from the Quantity column, where "quantity" is the named range C5:C12, you can use INDEX and MATCH together:

    {=INDEX(quantity,MATCH(FALSE,data="red",0))}
    

### Literal contains

If you need to match the first value that literally "does not contain", you can use a variant of the formula. For example to match the first value in data that does not contain an "r", you can use:

    {=MATCH(FALSE,ISNUMBER(SEARCH("r",data)),0)}
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

For more details about ISNUMBER + SEARCH, [see this page](https://exceljet.net/formulas/cell-contains-specific-text)
.

Related formulas
----------------

[![Excel formula: Match first does not begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/match%20first%20occurrence%20does%20not%20contain.png "Excel formula: Match first does not begin with")](https://exceljet.net/formulas/match-first-does-not-begin-with)

### [Match first does not begin with](https://exceljet.net/formulas/match-first-does-not-begin-with)

The key to this formula is the array or TRUE and FALSE values constructed with this expression: LEFT(code,1)<>"N" Here, each value in the named range "code" is evaluated with the logical test "first letter is not N". The result is an array or TRUE and FALSE values like this: {FALSE;FALSE;...

[![Excel formula: INDEX and MATCH approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match.png "Excel formula: INDEX and MATCH approximate match")](https://exceljet.net/formulas/index-and-match-approximate-match)

### [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table to the right. For convenience only, grade (G5:G9) and score (F5:F9) are named ranges . This is a classic "approximate-match" lookup problem because it is unlikely that a...

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: INDEX and MATCH case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case-sensitive%20INDEX%20and%20MATCH.png "Excel formula: INDEX and MATCH case-sensitive ")](https://exceljet.net/formulas/index-and-match-case-sensitive)

### [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the first name in column B, based on a lookup value in cell F6. By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP , XLOOKUP , and INDEX and MATCH . These formulas will simply return...

[![Excel formula: Two-way lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20lookup%20with%20INDEX%20and%20MATCH.png "Excel formula: Two-way lookup with INDEX and MATCH")](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

### [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

In this example, the goal is to perform a two-way lookup, sometimes called a matrix lookup . This means we need to create a match on both rows and columns and return the value at the intersection of this two-way match The core of this formula is INDEX, which is simply retrieving a value from C6:G10...

[![Excel formula: XLOOKUP wildcard contains substring](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_wildcard_contains_substring.png "Excel formula: XLOOKUP wildcard contains substring")](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)

### [XLOOKUP wildcard contains substring](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)

The goal is to look up the Title, Author, and Year in the list of books as shown using a formula based on a partial match and a wildcard. The text string to search for is entered in cell G4. All data is in an Excel Table named data in the range B5:D16. This problem can be easily solved with the...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

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

*   [Match first does not begin with](https://exceljet.net/formulas/match-first-does-not-begin-with)
    
*   [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)
    
*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)
    
*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    
*   [XLOOKUP wildcard contains substring](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
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