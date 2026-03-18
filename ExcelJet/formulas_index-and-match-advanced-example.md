# INDEX and MATCH advanced example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/index-and-match-advanced-example

---

[Skip to main content](https://exceljet.net/formulas/index-and-match-advanced-example#main-content)

[](https://exceljet.net/formulas/index-and-match-advanced-example#)

*   [Previous](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
    
*   [Next](https://exceljet.net/formulas/index-and-match-all-matches)
    

[Lookup](https://exceljet.net/formulas#Lookup)

INDEX and MATCH advanced example
================================

by Dave Bruns · Updated 4 Oct 2023

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[LEFT](https://exceljet.net/functions/left-function)

![Excel formula: INDEX and MATCH advanced example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/index%20and%20match%20advanced%20example.png "Excel formula: INDEX and MATCH advanced example")

Summary
-------

In this example, the goal is to determine the correct points to assign based on a given lift amount. Points are in column B, lift data is in columns C:I, and age is in row 4. The formula in L12 uses [INDEX](https://exceljet.net/functions/index-function)
, [MATCH](https://exceljet.net/functions/match-function)
, and the [LEFT](https://exceljet.net/functions/left-function)
 function:

    =INDEX(points,MATCH(L6,INDEX(data,0,MATCH(L5,--LEFT(age,2),1)),-1))
    

where **points** (B5:B25), **age** (C4:I4), and **data** (C5:I25) are [named ranges](https://exceljet.net/glossary/named-range)
. The formula returns is 89 points, based on an age of 28 in L5, and a lift of 295 in L6.

_Notes: this is an advanced formula. For step-by-step introduction to INDEX and MATCH, [see this article](https://exceljet.net/articles/index-and-match)
. This is also an [array formula](https://exceljet.net/glossary/array-formula)
 that must be entered with control + shift + enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
. In [Excel 365](https://exceljet.net/glossary/excel-365)
, the formula does not need special handling._

Explanation 
------------

This example is based on a fitness assessment where the goal is to award points based on how much weight was lifted at a given age. The solution described below is based on an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
, but there are several tricky elements that must be considered, making this problem much more difficult than your average lookup problem. The formula in L12 is:

    =INDEX(points,MATCH(L6,INDEX(data,0,MATCH(L5,--LEFT(age,2),1)),-1))
    

The formulas in L8:L10 are for additional explanation only. They show how the problem can be broken down into intermediate steps.

### Data layout

The first step is to verify the structure of the data and the behavior that will be needed to solve this problem. In column B, the range B5:B25 contains points. The formula will ultimately need to return a number from this range as the final result. In row 4, the range C4:I4 contains age ranges. Finally, the range C5:I25 contains lift data. There are three [named ranges](https://exceljet.net/glossary/named-range)
 in the worksheet: **points** (B5:B25), **age** (C4:I4), and **data** (C5:I25). These named ranges are for convenience only, to make the formula easier to read and write.

![Data layout for this example](https://exceljet.net/sites/default/files/images/formulas/inline/index%20and%20match%20advanced%20data%20layout.png "Data layout for this example")

### Behavior

When a user enters an age in L5 and a lift in L6, the formula should calculate points based on these two inputs. This means the formula needs to match the correct age column, locate the best match in the lift data, then traverse back to column B to get a final result. At a high level, there are three steps:

1.  look up the age column
2.  Look up lift
3.  Retrieve points

The screen below shows an overview:

![INDEX and MATCH formula behavior](https://exceljet.net/sites/default/files/images/formulas/inline/index%20and%20match%20advanced%20formula%20behavior.png "INDEX and MATCH formula behavior")

_Note: the formulas in L8:L10 are just to make it easier to understand how the formula works, they are not used in the final formula in L12._

### Complications

This problem is notable because the configuration is "backwards" from what is usually expected. Instead of matching an outer row and column, and retrieving a value from inside the table, we need to _match a value inside the table_ and traverse back to an outer column (points). Also note that both the age lookup and the lift lookup are approximate match lookups, and the lift data appears in descending order. Finally, the ages in row 4 are text strings, whereas the age in L5 is numeric.

### Age column

To get the correct age column we can use the [MATCH function](https://exceljet.net/functions/match-function)
 together with the [LEFT function](https://exceljet.net/functions/left-function)
 like this:

    =MATCH(L5,--LEFT(age,2),1)
    

Working from the inside out, the first step is to identify the correct column number by matching the age in L5 against the age ranges in C4:I4. This is more difficult than usual, because while the age in L5 is a number, the age ranges in C4:I4 are [text strings](https://exceljet.net/glossary/text-value)
. Looking at the age ranges, the first thing to note is that we only need the first number in each age range to get the right match:

![The first number in the age ranges is all we need](https://exceljet.net/sites/default/files/images/formulas/inline/index%20and%20match%20advanced%20formula%20first%20number%20in%20age%20ranges.png "The first number in the age ranges is all we need")'

We can extract just the first number of each age range with the [LEFT function](https://exceljet.net/functions/left-function)
 like this:

    --LEFT(age,2)
    

Because we are giving MATCH a range that contains 7 values, we get back 7 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {"17","22","27","32","37","42","47"}
    

The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) converts these text values to actual numbers, resulting in an array of numeric values:

    {17,22,27,32,37,42,47}
    

We now have what we need to get the column number with the MATCH function. The array above as _lookup\_array_, and with age in L5, we have:

    =MATCH(L5,{17,22,27,32,37,42,47},1)
    

We use 1 for _match\_type_, because we want to find the largest value that is less than or equal to age. Simplifying, we have:

    =MATCH(28,{17,22,27,32,37,42,47},1) // returns 3
    

The MATCH function returns 3 since 27 is the correct match, and the third item in the list.

### The lift

Now that we know which age column we should use to look up the lift, we can move on to that task. This too is complicated. We know the column number is 3, and we know the lift data is in **data** (C5:I25), but how do we look up a lift of 295 with that information?  The trick is to extract just column 3 (age range 27-31) before we look up the lift. We can do that with the INDEX function like this:

    =INDEX(data,0,3) // returns column 3
    

By providing zero for _row\_num_ and 3 for _column\_num_, [INDEX will return the entire third column](https://exceljet.net/formulas/look-up-entire-column)
 of **data** (C5:I25), which is the range E5:E25. So, putting it all together, we have:

    INDEX(data,0,MATCH(L5,--LEFT(age,2),1)) // returns E5:E25
    

The MATCH function returns 3 to the [INDEX function](https://exceljet.net/functions/index-function)
 as _column\_num_, and INDEX returns column 3 of **data**. We now have what we need to finally look up the lift. To do this, we embed the code above into another MATCH function:

    MATCH(L6,INDEX(data,0,MATCH(L5,--LEFT(age,2),1)),-1)
    

Note the _lookup\_value_ is the lift from cell L6 (295) and _match\_type_ is -1, since the lift data appears in _descending_ order and we want to find the smallest value that is greater than or equal to the lift. The _lookup\_array_ is created with the code explained above. Simplifying, we have:

    MATCH(295,E5:E25,-1) // returns 12
    

MATCH returns 12 because 300 is the smallest value that is greater than or equal to 295, the position of 300 is in row 12 of E5:E25. Just to recap, all of the code below simply returns the number 12:

    MATCH(L6,INDEX(data,0,MATCH(L5,--LEFT(age,2),1)),-1) // returns 12
    

We now have everything we need to solve the problem. We know the correct lift is in row 12 and column 3 of data, so we just need to traverse back across row 12 to retrieve the corresponding value from **points** (B5:B25). How can we do that? This is actually the easiest step in the problem. All we need to do is give the [INDEX function](https://exceljet.net/functions/index-function)
 the **points** range with a row number:

    =INDEX(points,12) // returns 89
    

### Recap

Putting everything together, the final formula in L12 is:

    =INDEX(points,MATCH(L6,INDEX(data,0,MATCH(L5,--LEFT(age,2),1)),-1))
    

The _inner_ MATCH function returns 3 to the _inner_ INDEX as _column\_num_:

    =INDEX(points,MATCH(L6,INDEX(data,0,3),-1))
    

With 0 for _row\_num_, INDEX returns the range E5:E25 to the _outer_ MATCH as _lookup\_array_:

    =INDEX(points,MATCH(L6,E5:E25,-1))
    

The _outer_ MATCH returns 12 as _row\_num_ to INDEX_:_

    =INDEX(points,12)
    

Finally, the INDEX function returns 89, the points awarded for a lift of 295 at age 28.

Related formulas
----------------

[![Excel formula: Two-way approximate match multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20approximate%20match%20multiple%20criteria%20v2.png "Excel formula: Two-way approximate match multiple criteria")](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)

### [Two-way approximate match multiple criteria](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)

The goal is to lookup a feed rate based on material, hardness, and drill bit diameter. Feed rate values are in the named range data (D6:H16). This can be done with a two-way INDEX and MATCH formula. One MATCH function works out the row number (material and hardness), and the other MATCH function...

[![Excel formula: INDEX and MATCH descending order](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20and%20MATCH%20descending%20order.png "Excel formula: INDEX and MATCH descending order")](https://exceljet.net/formulas/index-and-match-descending-order)

### [INDEX and MATCH descending order](https://exceljet.net/formulas/index-and-match-descending-order)

This formula uses -1 for match type to allow an approximate match on values sorted in descending order. The MATCH part of the formula looks like this: MATCH(F4,B5:B9,-1) Using the lookup value in cell F4, MATCH finds the first value in B5:B9 that is greater than or equal to the lookup value. If an...

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

*   [Two-way approximate match multiple criteria](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)
    
*   [INDEX and MATCH descending order](https://exceljet.net/formulas/index-and-match-descending-order)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    

### Videos

*   [How to use MATCH to find approximate matches](https://exceljet.net/videos/how-to-use-match-to-find-approximate-matches)
    
*   [Two-way lookup with INDEX and MATCH approximate](https://exceljet.net/videos/two-way-lookup-with-index-and-match-approximate)
    

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