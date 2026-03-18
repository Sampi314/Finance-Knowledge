# INDEX and MATCH exact match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/index-and-match-exact-match

---

[Skip to main content](https://exceljet.net/formulas/index-and-match-exact-match#main-content)

[](https://exceljet.net/formulas/index-and-match-exact-match#)

*   [Previous](https://exceljet.net/formulas/index-and-match-descending-order)
    
*   [Next](https://exceljet.net/formulas/index-and-match-on-multiple-columns)
    

[Lookup](https://exceljet.net/formulas#Lookup)

INDEX and MATCH exact match
===========================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7780/download?token=86qBFJFd)
 (16.01 KB)

![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")

Summary
-------

This example shows how to use [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 to get information from a table based on an exact match. In the example shown, the formula in cell H6 is:

    =INDEX(B5:E16,MATCH(H4,B5:B16,0),2)
    

With "Toy Story" in cell H4, the MATCH function returns 4, and the INDEX function returns 1995, the year the movie Toy Story was released. See below for more details.

Generic formula
---------------

    =INDEX(range,MATCH(value,range,0),column)

Explanation 
------------

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX and MATCH formula that looks up information using the movie title. If you are new to INDEX and MATCH formulas, [this article](https://exceljet.net/articles/index-and-match)
 provides a detailed overview with many examples.

### MATCH function

This formula uses the [MATCH function](https://exceljet.net/functions/match-function)
 to get the row position of Toy Story in the table, and the [INDEX function](https://exceljet.net/functions/index-function)
 to retrieve a value at that row. MATCH is configured to look for the movie title in cell H4 in the range B5:B16:

    MATCH(H4,B5:B16,0)
    

Note that the _match\_type_ argument is set to zero (0), to force MATCH to perform an _exact match_. MATCH locates "Toy Story" on row 4 and returns this number to INDEX as the row number.

### INDEX function

The [INDEX function](https://exceljet.net/functions/index-function)
 is configured with an array that includes _all data_ in the table, and the column number is hard-coded as 2 to retrieve the Year value from column 2 in the table.

    =INDEX(B5:E16,MATCH(H4,B5:B16,0),2) // get year

Once MATCH returns 4 to INDEX as the row number, we can simplify the formula to:

    =INDEX(B5:E16,4,2) // returns 1995
    

INDEX then retrieves the value at the intersection of the 4th row and 2nd column in the array, which is 1995. The other formulas in the example are identical except for the column number:

    =INDEX(B5:E16,MATCH(H4,B5:B16,0),2) // year
    =INDEX(B5:E16,MATCH(H4,B5:B16,0),3) // rank
    =INDEX(B5:E16,MATCH(H4,B5:B16,0),4) // sales
    

Note: normally, we would use [absolute references](https://exceljet.net/glossary/absolute-reference)
 to lock references like this:

    =INDEX($B$5:$E$16,MATCH($H$4,$B$5:$B$16,0),2) // year

This will allow the formula to be copied into the range H6:H8 with these ranges locked. Then only the column number needs to be changed. However, in the examples above, we are using [relative references](https://exceljet.net/glossary/relative-reference)
 to make the formulas easier to read.

Video: [What is an absolute reference?](https://exceljet.net/videos/whats-an-absolute-reference)

### INDEX with a single column

In the example above, INDEX receives an array that contains all data in the table. However, you can easily rewrite the formulas to provide INDEX with one column only, which eliminates the need to supply a column number:

    =INDEX(C5:C16,MATCH(H4,B5:B16,0)) // year
    =INDEX(D5:D16,MATCH(H4,B5:B16,0)) // rank
    =INDEX(E5:E16,MATCH(H4,B5:B16,0)) // sales

In each case, INDEX receives a one-column array that corresponds to the data being retrieved, and MATCH supplies the row number.

### INDEX with TRANSPOSE

The current version of Excel supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. This means a formula can return multiple values, and these values will [spill](https://exceljet.net/glossary/spill)
 onto the worksheet into multiple cells. This means it is possible to return the year, rank, and sales value all in one go. The trick is to give INDEX all 3 columns in the range C5:E16, then specify zero (0) for the row number:

    INDEX(C5:E16,MATCH(H4,B5:B16,0),0)

Providing zero for the _column\_num_ argument will cause INDEX to return an [entire row of data](https://exceljet.net/formulas/look-up-entire-row)
. With "Toy Story" in cell H4, we get back a [horizontal array](https://exceljet.net/glossary/array)
 of values like this:

    {1995,4,394436586}  // {year,rank,sales}

This is the year, rank, and sales for Toy Story. To transform the horizontal data into a _vertical_ array, we can nest the INDEX and MATCH formula inside the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 like this:

    =TRANSPOSE(INDEX(C5:E16,MATCH(H4,B5:B16,0),0))

The result is a vertical array that will land in cell H6 and spill into the range H6:H8 all in one step, with only one formula required.

> [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
>  - a detailed introduction with more examples

Related formulas
----------------

[![Excel formula: INDEX and MATCH approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match.png "Excel formula: INDEX and MATCH approximate match")](https://exceljet.net/formulas/index-and-match-approximate-match)

### [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table to the right. For convenience only, grade (G5:G9) and score (F5:F9) are named ranges . This is a classic "approximate-match" lookup problem because it is unlikely that a...

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

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

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
    
*   [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)
    
*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    
*   [Join tables with INDEX and MATCH](https://exceljet.net/formulas/join-tables-with-index-and-match)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

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