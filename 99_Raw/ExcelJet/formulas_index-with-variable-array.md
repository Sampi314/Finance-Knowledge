# INDEX with variable array - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/index-with-variable-array

---

[Skip to main content](https://exceljet.net/formulas/index-with-variable-array#main-content)

[](https://exceljet.net/formulas/index-with-variable-array#)

*   [Previous](https://exceljet.net/formulas/index-and-match-with-variable-columns)
    
*   [Next](https://exceljet.net/formulas/join-tables-with-index-and-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

INDEX with variable array
=========================

by Dave Bruns · Updated 21 Dec 2019

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

![Excel formula: INDEX with variable array](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/INDEX%20with%20variable%20array.png "Excel formula: INDEX with variable array")

Summary
-------

To set up an INDEX and MATCH formula where the array provided to INDEX is variable, you can use the CHOOSE function. In the example shown, the formula in I5, copied down, is:

    =INDEX(CHOOSE(H5,Table1,Table2),MATCH(G5,Table1[Model],0),2)
    

With Table1 and Table2 as indicated in the screenshot.

Generic formula
---------------

    =INDEX(CHOOSE(number,array1,array2),MATCH(value,range,0))

Explanation 
------------

At the core, this is a normal [INDEX and MATCH function](https://exceljet.net/articles/index-and-match)
:

    =INDEX(array,MATCH(value,range,0))
    

Where the [MATCH function](https://exceljet.net/functions/match-function)
 is used to find the correct row to return from array, and the [INDEX function](https://exceljet.net/functions/index-function)
 returns the value at that array.

However, in this case we want to make the array variable, so that the range given to INDEX can be changed on the fly. We do this with the CHOOSE function:

    CHOOSE(H5,Table1,Table2)
    

The [CHOOSE function](https://exceljet.net/functions/choose-function)
 returns a value from a list using a given position or index. The value can be a constant, a cell reference, an [array](https://exceljet.net/glossary/array)
, or a range. In the example, the numeric index is provided in column H. When the index number is 1, we use Table1. When the index is 2, we feed Table2 to INDEX:

    CHOOSE(1,Table1,Table2) // returns Table1
    CHOOSE(2,Table1,Table2) // returns Table2
    

_Note: the ranges provided to CHOOSE don't need to be [tables](https://exceljet.net/glossary/excel-table)
, or [named ranges](https://exceljet.net/glossary/named-range)
._

In I5, the number in column H is 1, so CHOOSE returns Table1, and the formula resolves to:

    =INDEX(Table1,MATCH("A",Table1[Model],0),2)
    

The MATCH function returns the position of "A" in Table1, which is 1, and INDEX returns the value at row 1, column 2 of Table1, which is $20.00

    =INDEX(Table1,1,2) // returns $20.00
    

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

[![Excel formula: Join tables with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join%20tables%20with%20INDEX%20and%20MATCH%202.png "Excel formula: Join tables with INDEX and MATCH")](https://exceljet.net/formulas/join-tables-with-index-and-match)

### [Join tables with INDEX and MATCH](https://exceljet.net/formulas/join-tables-with-index-and-match)

This formula pulls the customer name and state from the customer table into the order table. The MATCH function is used to locate the right customer and the INDEX function is used to retrieve the data. Retrieving customer name Working from the inside out, the MATCH function is used to get a row...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20MATCH%20Function%20for%20exact%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

### [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

The MATCH function finds the relative position of an item in a list. MATCH can find exact matches or approximate matches. In this video, we'll look at how to use MATCH to find an exact match. The MATCH function takes three arguments: the lookup\_value, which is the value you're looking up, the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

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
    
*   [Join tables with INDEX and MATCH](https://exceljet.net/formulas/join-tables-with-index-and-match)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    
*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    

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