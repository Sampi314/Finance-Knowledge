# Match first does not begin with - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/match-first-does-not-begin-with

---

[Skip to main content](https://exceljet.net/formulas/match-first-does-not-begin-with#main-content)

[](https://exceljet.net/formulas/match-first-does-not-begin-with#)

*   [Previous](https://exceljet.net/formulas/lookup-with-variable-sheet-name)
    
*   [Next](https://exceljet.net/formulas/match-first-error)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Match first does not begin with
===============================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[LEFT](https://exceljet.net/functions/left-function)

![Excel formula: Match first does not begin with](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/match%20first%20occurrence%20does%20not%20contain.png "Excel formula: Match first does not begin with")

Summary
-------

To match the first value that does not begin with a specific string, you can use an array based on the MATCH and LEFT functions. In the example shown, the formula in F5 is:

    {=MATCH(TRUE,IF(LEFT(code,1)<>"N",TRUE),0)}
    

where "code" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B12.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

Generic formula
---------------

    {=MATCH(TRUE,IF(LEFT(range,1)<>"N",TRUE),0)}

Explanation 
------------

The key to this formula is the array or TRUE and FALSE values constructed with this expression:

    LEFT(code,1)<>"N"
    

Here, each value in the [named range](https://exceljet.net/glossary/named-range)
 "code" is evaluated with the logical test "first letter is not N". The result is an array or TRUE and FALSE values like this:

    {FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE}
    

This array is fed into the MATCH function as the lookup array. The lookup value is TRUE, and match type is set to zero to force an exact match. The MATCH function returns the position of the first value that does not begin with the letter "N" (Z09876), which is 5.

### INDEX and MATCH

To retrieve a value associated with the position returned by MATCH, you can add the INDEX function. In example shown, the formula in F6 is:

    {=INDEX(value,MATCH(TRUE,LEFT(code,1)<>"N",0))}
    

Note we are using the same MATCH formula above to provide a row number to INDEX, with the array set to the named range "value". As before, MATCH returns 5. INDEX then returns the value at that position, -23.

As before, this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter.

Related formulas
----------------

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

[![Excel formula: Match first occurrence does not contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/match%20first%20occurrence%20does%20not%20contain.png "Excel formula: Match first occurrence does not contain")](https://exceljet.net/formulas/match-first-occurrence-does-not-contain)

### [Match first occurrence does not contain](https://exceljet.net/formulas/match-first-occurrence-does-not-contain)

This formula depends on a TRUE or FALSE result from a logical test, where FALSE represents the value you are looking for. In the example, the logical test is data="red", entered as the lookup\_array argument in the MATCH function: =MATCH(FALSE,data="red",0) Once the test is run, it returns an array...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

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

*   [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)
    
*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)
    
*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    
*   [XLOOKUP wildcard contains substring](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)
    
*   [Match first occurrence does not contain](https://exceljet.net/formulas/match-first-occurrence-does-not-contain)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    

### Articles

*   [How to build logical formulas](https://exceljet.net/plc/how-to-build-logical-formulas)
    

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