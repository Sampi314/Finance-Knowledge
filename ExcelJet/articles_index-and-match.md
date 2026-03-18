# How to use INDEX and MATCH | Exceljet

**Source:** https://exceljet.net/articles/index-and-match

---

[Skip to main content](https://exceljet.net/articles/index-and-match#main-content)

[](https://exceljet.net/articles/index-and-match#)

*   [Previous](https://exceljet.net/articles/29-ways-to-save-time-with-excel-formulas)
    
*   [Next](https://exceljet.net/articles/custom-number-formats)
    

How to use INDEX and MATCH
==========================

by Dave Bruns · Updated 14 Mar 2025

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/6246/download?token=-jmXlzF8)
 (21.44 KB)

![How to use INDEX and MATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/Index___Match_artwork.jpeg "How to use INDEX and MATCH")

Summary
-------

INDEX and MATCH is the most popular tool in Excel for performing more advanced lookups. This is because INDEX and MATCH are incredibly flexible – you can do horizontal and vertical lookups, 2-way lookups, left lookups, case-sensitive lookups, and even lookups based on multiple criteria. If you want to improve your Excel skills, INDEX and MATCH should be on your list. See below for many examples.

This article explains in simple terms how to use INDEX and MATCH together to perform lookups. It takes a step-by-step approach, first explaining INDEX, then MATCH, then showing you how to combine the two functions together to create a dynamic two-way lookup. There are more advanced examples further down the page.

### Table of Contents

*   [The INDEX Function](https://exceljet.net/articles/index-and-match#index_function)
    
*   [The MATCH function](https://exceljet.net/articles/index-and-match#match_function)
    
*   [INDEX and MATCH together](https://exceljet.net/articles/index-and-match#index_and_match)
    
*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/articles/index-and-match#two_way_lookup)
    
*   [Left lookup with INDEX and MATCH](https://exceljet.net/articles/index-and-match#left_lookup)
    
*   [INDEX and MATCH with multiple criteria](https://exceljet.net/articles/index-and-match#multiple_criteria)
    
*   [Case-sensitive lookup](https://exceljet.net/articles/index-and-match#case_sensitive_lookup)
    
*   [Finding the closest match](https://exceljet.net/articles/index-and-match#closest_match)
    
*   [INDEX and XMATCH](https://exceljet.net/articles/index-and-match#index_and_xmatch)
    
*   [More examples](https://exceljet.net/articles/index-and-match#more_examples)
    

### The INDEX Function

The INDEX function in Excel is fantastically flexible and powerful, and you'll find it in a huge number of Excel formulas, especially advanced formulas. But what does INDEX actually do? In a nutshell, INDEX retrieves the value at a given location in a range. For example, let's say you have a table of planets in our solar system (see below), and you want to get the name of the 4th planet, Mars, with a formula. You can use INDEX like this:

    =INDEX(B3:B11,4)
    

![Using INDEX to get the name of the 4th planet](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/get%20name%20of%204th%20planet%20with%20index2.png?itok=9uHIE_Rv "Using INDEX to get the name of the 4th planet")  
_INDEX returns the value in the 4th row of the range._

Video: [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What if you want to get the diameter of Mars with INDEX? In that case, we can supply both a row number and a column number, and provide a larger range. The INDEX formula below uses the full range of data in B3:D11, with a row number of 4 and column number of 2:

    =INDEX(B3:D11,4,2)
    

![Using INDEX to get the diameter of the 4th planet](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/diameter%20of%204th%20planet%20with%20index2.png?itok=iOLAnr4q "Using INDEX to get the diameter of the 4th planet")  
_INDEX retrieves the value at row 4, column 2._

To summarize, INDEX gets a value at a given location in a range of cells based on numeric position. When the range is one-dimensional, you only need to supply a row number. When the range is two-dimensional, you'll need to supply both the row and column numbers.

At this point, you may be thinking "So what? How often do you actually know the position of something in a spreadsheet?"

Exactly right. We need a way to locate the position of things we're looking for.

Enter the MATCH function.

### The MATCH function

The MATCH function is designed for one purpose: find the position of an item in a range. For example, we can use MATCH to get the position of the word "peach" in this list of fruits like this:

    =MATCH("peach",B3:B9,0)
    

![Using MATCH to find position in a vertical range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/match%20to%20find%20position%20in%20vertical%20range.png?itok=ErAROygr "Using MATCH to find position in a vertical range")  
_MATCH returns 3, since "Peach" is the 3rd item. MATCH is not case-sensitive._

MATCH doesn't care if a range is horizontal or vertical, as you can see below:

    =MATCH("peach",C4:I4,0)
    

![Using MATCH to find position in a horizontal range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/Position%20of%20peach%20in%20horizonal%20array.png?itok=tVWkbhOU "Using MATCH to find position in a horizontal range")  
_Same result with a horizontal range, MATCH returns 3._

Video: [How to use MATCH for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

_Important: The last argument in the MATCH function is match\_type. Match\_type is important and controls whether matching is exact or approximate. In many cases, you will want to use zero (0) to force exact match behavior. Match\_type defaults to 1, which means approximate match, so it's important to provide a value. See the_ [_MATCH page_](https://exceljet.net/functions/match-function)
 _for more details._

### INDEX and MATCH together

Now that we've covered the basics of INDEX and MATCH, how do we combine the two functions in a single formula? Consider the data below, a table showing a list of salespeople and monthly sales numbers for three months: January, February, and March.

![Sales by salesperson by month](https://exceljet.net/sites/default/files/images/articles/inline/sales%20by%20salesperson%20table2_0.png "Sales by salesperson by month")

Let's say we want to write a formula that returns the sales number for February for a given salesperson. From the discussion above, we know we can give INDEX a row and column number to retrieve a value. For example, to return the February sales number for Frantz, we provide the range C3:E11 with a row 5 and column 2:

    =INDEX(C3:E11,5,2) // returns $5194
    

But we obviously don't want to hardcode numbers. Instead, we want a _dynamic_ lookup.

How will we do that? The MATCH function of course. MATCH will work perfectly for finding the positions we need. Working one step at a time, let's leave the column hardcoded as 2 and make the row number dynamic. Here's the revised formula, with the MATCH function nested inside INDEX in place of 5:

    =INDEX(C3:E11,MATCH("Frantz",B3:B11,0),2)
    

Taking things one step further, we'll use the value from H2 in MATCH:

    =INDEX(C3:E11,MATCH(H2,B3:B11,0),2)
    

![INDEX and MATCH to find Feb sales for any name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/INDEX%20and%20MATCH%20to%20find%20Feb%20sales%20for%20any%20name.png?itok=sI2xPorv "INDEX and MATCH to find Feb sales for any name")  
_MATCH finds "Frantz" and returns 5 to INDEX for row._

To summarize:

1.  INDEX needs numeric positions.
2.  MATCH finds those positions.
3.  MATCH is [nested](https://exceljet.net/glossary/nesting)
     inside INDEX.

Let's now tackle the column number.

### Two-way lookup with INDEX and MATCH

Above, we used the MATCH function to find the row number dynamically, but we hardcoded the column number. How can we make the formula fully dynamic so we can return sales for any given salesperson in any given month? The trick is to use MATCH twice – once to get a row position, and once to get a column position.

From the examples above, we know MATCH works fine with both horizontal and vertical arrays. That means we can easily find the position of a given month with MATCH. For example, this formula returns the position of March, which is 3:

    =MATCH("Mar",C2:E2,0) // returns 3
    

But of course, _we don't want to hardcode any values_, so let's update the worksheet to allow the input of a month name, and use MATCH to find the column number we need. The screen below shows the result:

![Dynamic lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/dynamic%20lookup%20with%20INDEX%20and%20MATCH.png?itok=jIUT-_g- "Dynamic lookup with INDEX and MATCH")  
_A fully dynamic, two-way lookup with INDEX and MATCH._

    =INDEX(C3:E11,MATCH(H2,B3:B11,0),MATCH(H3,C2:E2,0))
    

The first MATCH formula returns 5 to INDEX as the row number, and the second MATCH formula returns 3 to INDEX as the column number. Once MATCH runs, the formula simplifies to:

    =INDEX(C3:E11,5,3)
    

and INDEX correctly returns $10,525, the sales number for Frantz in March.

Note: you could use [Data Validation](https://exceljet.net/articles/excel-data-validation-guide)
 to create dropdown menus to select salesperson and month.

Video: [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

Video: [How to debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
 (to see MATCH return values)

### Left lookup

One of the key advantages of INDEX and MATCH over the VLOOKUP function is the ability to perform a "left lookup". Simply put, this just means a lookup where the ID column is to the _right_ of the values you want to retrieve, as seen in the example below:

![Left lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/left%20lookup%20with%20index%20and%20match.png?itok=NOfYtwRe "Left lookup with INDEX and MATCH")

[Read a detailed explanation here](https://exceljet.net/formulas/left-lookup-with-index-and-match)
.

### Index and Match with multiple criteria

One of the trickiest problems in Excel is a lookup based on multiple criteria. In other words, a lookup that matches on more than one column at the same time. A nice way to handle these problems is to use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
, a technique for handling TRUE and FALSE values like 1s and 0s. You can see this approach below, where we are using INDEX and MATCH and Boolean logic to find a price based on three values: Item, Color, and Size:

![INDEX and MATCH with multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/INDEX%20and%20MATCH%20with%20multiple%20criteria.png?itok=18lhFBQa "INDEX and MATCH with multiple criteria")

[Read a detailed explanation here](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
. You can use this [same approach with XLOOKUP](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
.

_Note: this is an_ [_array formula_](https://exceljet.net/glossary/array-formula)
 _and must be entered with control + shift + enter in Excel 2019 and older._

For a quick introduction to Booleans in Excel, see these videos from our Dynamic Array Formulas course:

*   [Introduction to Booleans](https://exceljet.net/videos/introduction-to-booleans)
    
*   [Boolean Algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
    

> One benefit of INDEX and MATCH formulas is that they use numeric indexing. This makes it easy to customize behavior to match specific data patterns. For example, you can use a [step-based formula](https://exceljet.net/formulas/step-based-lookup-example)
>  to jump directly to relevant data.

### Case-sensitive lookup

By itself, the MATCH function is not case-sensitive. However, you use the [EXACT function](https://exceljet.net/functions/exact-function)
 with INDEX and MATCH to perform a lookup that respects upper and lower case, as shown below:

![Case-sensitive lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/case%20sensitive%20lookup.png?itok=QJBMMVyy "Case-sensitive lookup with INDEX and MATCH")

[Read a detailed explanation here](https://exceljet.net/formulas/case-sensitive-lookup)
.

_Note: this is an_ [_array formula_](https://exceljet.net/glossary/array-formula)
 _and must be entered with control + shift + enter in Excel 2019 and older._

### Closest match

Another example that shows off the flexibility of INDEX and MATCH is the problem of finding the _closest match_. In the example below, we use the [MIN function](https://exceljet.net/functions/min-function)
 together with the [ABS function](https://exceljet.net/functions/abs-function)
 to _create_ a lookup value and a lookup array _inside_ the MATCH function. Essentially, we use MATCH to find the smallest difference. Then, we use INDEX to retrieve the associated trip from column B.

![Find closest match with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/find%20closest%20match.png?itok=uqx3HlCW "Find closest match with INDEX and MATCH")

[Read a detailed explanation here](https://exceljet.net/formulas/find-closest-match)
.

_Note: this is an_ [_array formula_](https://exceljet.net/glossary/array-formula)
 _and must be entered with control + shift + enter in Excel 2019 and older._

### INDEX and XMATCH

The current version of Excel includes the [XMATCH function](https://exceljet.net/functions/xmatch-function)
, which is an upgraded replacement for the MATCH function. Like the MATCH function, XMATCH performs a lookup and returns a numeric position. Also like MATCH, XMATCH can perform lookups in vertical or horizontal ranges, supports both approximate and exact matches, and allows wildcards (\* ?) for partial matches. But XMATCH adds even more features. The 5 key differences between XMATCH and MATCH are as follows:

1.  XMATCH defaults to an exact match, while MATCH defaults to an approximate match.
2.  XMATCH can find the next larger item _or_ the next smaller item.
3.  XMATCH can perform a reverse search (i.e. search from last to first).
4.  XMATCH does not require values to be sorted when performing an approximate match.
5.  XMATCH can perform a binary search, which is specifically optimized for speed.
6.  XMATCH can perform a regex match, a powerful way to match complex text patterns.

So, can you simply use XMATCH in an INDEX and MATCH formula instead of MATCH? Yes, absolutely. Using XMATCH instead of the MATCH function "upgrades" the formula to include the benefits listed above.

> Using XMATCH instead of the MATCH function "upgrades" the formula to include the benefits listed above.

### Replacing MATCH with XMATCH

For exact-match problems, XMATCH is a drop-in replacement for the MATCH function. You can simply change "MATCH" to "XMATCH" as shown below:

    =MATCH(value,array,0) // exact match
    =XMATCH(value,array,0) // exact match
    

_Note: since XMATCH defaults to an exact match, the zero above is not required. However, when converting MATCH in exact-match mode to XMATCH, you can leave the zero if you like._

For approximate matches, XMATCH behavior is _different_ when _match\_type_ is set to 1:

    =MATCH(value,array,1) // exact match or next smallest
    =XMATCH(value,array,1) // exact match or next *largest*
    

In addition, XMATCH allows -1 for match type, which is _not available_ with MATCH:

    =XMATCH(value,array,-1) // exact match or next smallest
    

_Note: the MATCH function does not offer the search mode argument at all._

XMATCH can also be configured to perform a reverse search and a binary search. For a full description of all of the options available with XMATCH, [see this page](https://exceljet.net/functions/xmatch-function)
.

### More examples of INDEX + MATCH

Here are some more basic examples of INDEX and MATCH in action, each with a detailed explanation:

*   [Basic INDEX and MATCH exact](https://exceljet.net/formulas/index-and-match-exact-match)
     (features Toy Story)
*   [Basic INDEX and MATCH approximate](https://exceljet.net/formulas/index-and-match-approximate-match)
     (grades)
*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
     (approximate match)

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)
    
*   [XLOOKUP vs VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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