# Left lookup with INDEX and MATCH - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/left-lookup-with-index-and-match

---

[Skip to main content](https://exceljet.net/formulas/left-lookup-with-index-and-match#main-content)

[](https://exceljet.net/formulas/left-lookup-with-index-and-match#)

*   [Previous](https://exceljet.net/formulas/join-tables-with-index-and-match)
    
*   [Next](https://exceljet.net/formulas/left-lookup-with-vlookup)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Left lookup with INDEX and MATCH
================================

by Dave Bruns · Updated 6 Dec 2022

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7468/download?token=nd9LlkIp)
 (15.53 KB)

![Excel formula: Left lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/left%20lookup%20with%20index%20and%20match_0.png "Excel formula: Left lookup with INDEX and MATCH")

Summary
-------

To perform a left lookup with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, set up the [MATCH function](https://exceljet.net/functions/match-function)
 to locate the lookup value in the column that contains lookup values. Then use the [INDEX function](https://exceljet.net/functions/index-function)
 to retrieve values at that position. In the example shown, the formula in H5 is:

    =INDEX(data[Item],MATCH(G5,data[ID],0))
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:E15.

Generic formula
---------------

    =INDEX(range,MATCH(A1,range,0))

Explanation 
------------

In this example, the goal is to lookup data to the _left_ of an ID that appears as the last column in the table. In other words, we need to locate a match in column E, then retrieve a value from a column to the left. This is one of those problems that is [difficult with VLOOKUP](https://exceljet.net/formulas/left-lookup-with-vlookup)
, but easy with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 or [XLOOKUP](https://exceljet.net/functions/xlookup-function)
. Both options are explained below.

### Background study

*   [What is an Excel Table](https://exceljet.net/videos/what-is-an-excel-table)
     (3 min. video)
*   [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)
     (3 min. video)
*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
     (overview)
*   [Excel Tables](https://exceljet.net/articles/excel-tables)
     (overview)

### INDEX and MATCH

One of the advantages of using [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 over [VLOOKUP](https://exceljet.net/functions/vlookup-function)
 is that INDEX and MATCH can easily work with lookup values in _any column_ of the data. In the example shown, columns B through E contain product data with a unique ID in column E. Using the ID in column G as a lookup value, the formulas in the range H5:J6 use INDEX and MATCH to retrieve the correct item, color, and price. In cell H5, the formula used to lookup Item is:

    =INDEX(data[Item],MATCH(G5,data[ID],0))
    

Working from the inside out, the [MATCH function](https://exceljet.net/functions/match-function)
 is used to locate the value in G5 in the ID column like this:

    MATCH(G5,data[ID],0) // returns 3
    

Here, the _lookup\_value_ is G5, the _lookup\_array_ is **data\[ID\]** (E5:E15), and _match\_type_ is set to zero for an exact match. The result from MATCH is 3, since the ID 1003 occurs in the third row of the table. This value is returned directly to the [INDEX function](https://exceljet.net/functions/index-function)
 as _row\_num_. With _array_ provided as **data\[Item\],** INDEX returns "T-shirt" as a final result:

    =INDEX(item,3) // returns "T-shirt"
    

The same approach is used to retrieve the correct item, color, and price. The formulas in H5, I5, and J5 are as follows:

    =INDEX(data[Item],MATCH(G5,data[ID],0)) // get item
    =INDEX(data[Color],MATCH(G5,data[ID],0)) // get color
    =INDEX(data[Price],MATCH(G5,data[ID],0)) // get price
    

Notice the MATCH function is used exactly the same way in each formula. The only difference is the array given to INDEX. Once MATCH returns 3 as a result for ID 1003, we have:

    =INDEX(data[Item],3) // returns "T-shirt"
    =INDEX(data[Color],3) // returns "Black"
    =INDEX(data[Price],3) // returns 19
    

Each formula above returns the correct result for the ID 1003.

### Locking references

The formulas above use normal references to make them easier to read. To lock references so that the _same_ formula can be copied into the range H5:J6, we need to adjust the formula as follows:

    =INDEX(data[Item],MATCH($G5,data[[ID]:[ID]],0))
    

Notice the reference to $G5 is now a [mixed reference](https://exceljet.net/glossary/mixed-reference)
 with the column locked. Also notice the reference to the ID column in the Excel Table **data** is also locked with the following syntax:

    data[[ID]:[ID]] // locked
    

This syntax is unique to [structured references](https://exceljet.net/glossary/structured-reference)
, which are a feature of [Excel Tables](https://exceljet.net/articles/excel-tables)
.

Video: [How to copy and lock structured references](https://exceljet.net/videos/how-to-copy-and-lock-structured-references)

### XLOOKUP function

The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 is a modern replacement of the VLOOKUP function. One of the features that VLOOKUP lacks, and XLOOKUP provides, is the ability to "look left" in a lookup operation. The equivalent XLOOKUP formulas to retrieve Item, Color, and Price are:

    =XLOOKUP(G5,data[ID],data[Item]) // item
    =XLOOKUP(G5,data[ID],data[Color]) // color
    =XLOOKUP(G5,data[ID],data[Price]) // price
    

In these formulas _lookup\_value_ comes from G5, _lookup\_array_ is always **data\[ID\]**, and _return\_array_ is the column from which to return data.

In addition, because XLOOKUP runs on the new [dynamic array engine in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can retrieve values from all three columns at the same time like this:

    =XLOOKUP(G5,data[ID],data[[Color]:[ID]])
    

This will cause XLOOKUP to return all three values at the same time as a [spill range](https://exceljet.net/glossary/spill-range)
.

Related formulas
----------------

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

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

[![Excel formula: Left lookup with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Look%20left%20with%20VLOOKUP.png "Excel formula: Left lookup with VLOOKUP")](https://exceljet.net/formulas/left-lookup-with-vlookup)

### [Left lookup with VLOOKUP](https://exceljet.net/formulas/left-lookup-with-vlookup)

One of the VLOOKUP function's key limitations is that it can only look up values to the right. In other words, the column that contains lookup values must sit to the left of the values you want to retrieve with VLOOKUP. There is no way to override this behavior since it is hardwired into the...

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
    
*   [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)
    
*   [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)
    
*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    
*   [Join tables with INDEX and MATCH](https://exceljet.net/formulas/join-tables-with-index-and-match)
    
*   [Left lookup with VLOOKUP](https://exceljet.net/formulas/left-lookup-with-vlookup)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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