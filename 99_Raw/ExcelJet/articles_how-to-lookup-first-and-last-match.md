# How to lookup first and last match | Exceljet

**Source:** https://exceljet.net/articles/how-to-lookup-first-and-last-match

---

[Skip to main content](https://exceljet.net/articles/how-to-lookup-first-and-last-match#main-content)

[](https://exceljet.net/articles/how-to-lookup-first-and-last-match#)

*   [Previous](https://exceljet.net/articles/excel-formula-errors)
    
*   [Next](https://exceljet.net/articles/excel-formulas-and-functions)
    

How to lookup first and last match
==================================

by Dave Bruns · Updated 23 Oct 2023

![How to lookup first and last match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/How_to_lookup_first_and_last_match.jpeg)

Summary
-------

If VLOOKUP finds more than one match, will you get the first match or the last match? It's a trick question. It depends :) This article explains this confusing topic in detail, with lots of examples.

_Update: in the [current version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 to get all matches and the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 to [get the last match](https://exceljet.net/formulas/get-last-match)
 only. Depending on your needs, FILTER might be a better option than first or last match._

One of the more confusing aspects of lookup functions in Excel is understanding how to get the first or last match in a set of data with more than one match. This is because Excel's behavior changes depending  (1) whether you are performing an exact or approximate match, and (2) whether data is sorted or not.

For example, if we use VLOOKUP to get the price for "green" in the data below, which price will we get?

![VLOOKUP which match will we get?](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/VLOOKUP%20which%20match.png?itok=ncHVoSMC "VLOOKUP which match will we get?")

Read on for the answer and more interesting examples.

Notes:

*   The examples below use [named ranges](https://exceljet.net/glossary/named-range)
     (as noted in the images) to keep formulas simple.
*   Function reference links: [VLOOKUP](https://exceljet.net/functions/vlookup-function)
    , [INDEX](https://exceljet.net/functions/index-function)
    , [MATCH](https://exceljet.net/functions/match-function)
    , and [LOOKUP](https://exceljet.net/functions/lookup-function)
    .

### Exact match = first

When doing an exact match, you'll always get the first match, period. It doesn't matter if data is sorted or not. In the screen below, the lookup value in E5 is "red". The [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
, in exact match mode, returns the price for the first match:

    =VLOOKUP(E5,data,2,FALSE)
    

![VLOOKUP exact match finds first match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/VLOOKUP%20exact%20match.png?itok=kFrRTFqd "VLOOKUP exact match finds first match")

Notice the last argument in VLOOKUP is FALSE to force exact match.

### Approximate match = last

If you are doing an approximate match, _and data is sorted by lookup value_, you'll get the last match. Why? Because during an approximate match Excel scans through values until a value larger than the lookup value is found, then it "steps back" to the previous value.

In the screen below, VLOOKUP is set to approximate match mode, and colors are sorted. VLOOKUP returns the price for the last "green":

    =VLOOKUP(E5,data,2,TRUE)
    

![VLOOKUP approximate match finds last match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/VLOOKUP%20approximate%20match_0.png?itok=cX2VpJXn "VLOOKUP approximate match finds last match")

Notice the last argument in VLOOKUP is TRUE for approximate match.

### Approximate match + unsorted data = danger

With standard approximate match lookups, _data must be sorted by lookup value_. With unsorted data, you may see normal-looking results that are totally incorrect. This problem is more likely with VLOOKUP because [VLOOKUP defaults to approximate match](https://exceljet.net/articles/danger-beware-vlookup-defaults)
 when no fourth argument is provided.

To illustrate this problem, see the example below. Data is _unsorted_ and VLOOKUP, with no fourth argument provided, defaults to approximate match. Notice there is no "red" with a price of $17.00, yet VLOOKUP happily returns this invalid result:

    =VLOOKUP(E5,data,2)
    

![Example of VLOOKUP approximate match wrong result](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/VLOOKUP%20approximate%20match%20wrong%20result.png?itok=JJiEfcqP "Example of VLOOKUP approximate match wrong result")

For this reason, I recommend always setting the last argument for VLOOKUP explicitly: TRUE = approximate match, FALSE = exact match. The argument _is_ optional, but providing a value makes you think about it, and provides a visual reminder in the future.

We'll look at how to overcome the problem of last match and unsorted data below.

### "Normal" approximate match

At this point, you may be feeling a little confused and disoriented about the idea that approximate match can return the last match in some cases. If so, don't worry. Using approximate match to get the last match is not the "normal" case. Typically, you'll see approximate match used to assign values according to some kind of scale. A classic example is using VLOOKUP in approximate match mode to assign grades, which works beautifully:

    =VLOOKUP(E5,key,2,TRUE)
    

![VLOOKUP approximate match to assign grades](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/VLOOKUP%20approximate%20match%20to%20assign%20grades.png?itok=gWqjvXpF "VLOOKUP approximate match to assign grades")

In cases like this, the lookup table _deliberately_ does not include duplicate values, so the whole idea of "last matching value" is irrelevant. [More details on this formula here](https://exceljet.net/formulas/vlookup-calculate-grades)
.

The information above is to provide background and context for how matching works in Excel, so that the approaches described below make sense.

### Practical applications

How can we use the behavior described above in a practical situation? Well, one common scenario is looking up the "latest" or "last" entry for an item. For example, below we are using VLOOKUP in approximate match mode to find the latest price for Sandals. Notice data is sorted by item, then by date, so the latest price for a given item appears last:

    =VLOOKUP(F5,data,3,TRUE)
    

![VLOOKUP approximate match + sorted data = latest price](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/VLOOKUP%20approximate%20match%20to%20find%20latest%20price.png?itok=b2MYOtvw "VLOOKUP approximate match + sorted data = latest price")

### INDEX and MATCH

Other lookup functions can be used this way as well. Below, we are using an equivalent [INDEX](https://exceljet.net/functions/index-function)
 and [MATCH](https://exceljet.net/functions/match-function)
 formula find the latest price with the same data. Notice MATCH is configured to approximate match for items sorted in ascending order by setting the third argument to 1:

    =INDEX(price,MATCH(F5,item,1))
    

![INDEX and MATCH approximate to find latest price](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/INDEX%20and%20MATCH%20to%20find%20latest%20price.png?itok=phSC5MCy "INDEX and MATCH approximate to find latest price")

### LOOKUP function

The [LOOKUP function](https://exceljet.net/functions/lookup-function)
 can also be used in this case. LOOKUP _always_ performs an approximate match, so it works well in "last match" scenarios. The formula is quite simple:

    =LOOKUP(F5,item,price)
    

### ![LOOKUP function to find latest price](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/LOOKUP%20function%20to%20find%20latest%20price.png?itok=zbqBcsBy "LOOKUP function to find latest price")

### Last match with unsorted data

What if you want the last match, but data isn't sorted by lookup value? In other words, you want to apply criteria to find a match, and you simply want the last item in the data that matches your criteria? This is actually a case where the LOOKUP function shines, because LOOKUP can handle array operations natively, without control + shift + enter. This means we can dynamically build a lookup array to locate the data we want using simple logical expressions.

For example, have a look at the formula below:

    =LOOKUP(2,1/(item=F5),price)
    

![LOOKUP function to find last match with unsorted data](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/LOOKUP%20function%20to%20find%20last%20match%20unsorted%20data.png?itok=yrwVcgps "LOOKUP function to find last match with unsorted data")

This formula finds the latest price for Sandals in _unsorted_ data.

You may not have seen a formula like this before, so let's break it down in steps. Working from the inside out, we first apply the criteria with a simple logical expression:

    item=F5
    

This results in an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values, where TRUE corresponds to items that are "sandals" and FALSE corresponds to all other values:

    {FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE}
    

Next, we divide the number 1 by this array. During division, TRUE becomes 1 and FALSE becomes zero, so you should visualize the operation like this:

    1/{0;1;0;1;0;0;1;0}
    

One divided by one is one, and one divided by zero is #DIV/0, so the result is another array, this one containing only 1s and #DIV/0 errors:

    {#DIV/0!;1;#DIV/0!;1;#DIV/0!;#DIV/0!;1;#DIV/0!}
    

Don't worry, there is a method to this madness :)

Now, you may have noticed that the lookup value is the number 2. This may seem puzzling.  How will LOOKUP ever find the number 2 in an array that contains only 1s and errors? It won't. We are using 2 as a lookup value to force LOOKUP to scan to the _end of the data_.

The LOOKUP function will automatically ignore errors, so the only thing left to match are the 1s. It will scan through the 1s looking for a 2 that will never be found. When it reaches the end of the array, it will "step back" to the last valid value – the last 1 – which corresponds to the last match based on criteria provided. 

### INDEX and MATCH array version

The beauty of the [LOOKUP function](https://exceljet.net/functions/lookup-function)
 is it can handle the array operation described above natively in [older versions of Excel](https://exceljet.net/glossary/legacy-excel)
 without requiring you to enter as an [array formula](https://exceljet.net/glossary/array-formula)
 with control + shift + enter. However, you can certainly use an array formula if you like. Here is the equivalent INDEX and MATCH  formula, which must be entered with control + shift + enter in older versions of Excel:

    =INDEX(price,MATCH(2,1/(item=F5),1))
    

_Note: in the [current version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, the above formula will just work without special handling. Also, the newer [XMATCH function](https://exceljet.net/functions/xmatch-function)
 and [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 can be directly configured to return the last match._

### Last non-blank cell

The approach above turns out to be really useful. For example, by tweaking the logic a bit, we can do things like find the last non-empty cell in a column:

    =LOOKUP(2,1/(B:B<>""),B:B)
    

![Using LOOKUP to find the last non-blank cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/LOOKUP%20last%20non%20blank.png?itok=Espl9kv2 "Using LOOKUP to find the last non-blank cell")

This formula is [described in more detail here](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
.

### Lookup nth match? All matches?

If you've made it this far, you may be wondering how you would find the second or third match, or how you would retrieve all matches? Here are some links for you:

*   [How to get nth match with VLOOKUP](https://exceljet.net/formulas/get-nth-match-with-vlookup)
    
*   [How to get nth match with INDEX and MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [How to get all matches INDEX and MATCH](https://exceljet.net/formulas/index-and-match-all-matches)
    

You'll notice formulas like this get complicated. There are some cool new functions coming to Excel in 2019 that will make these solutions much simpler. Stay tuned. In the meantime, don't forget that [Pivot Tables](https://exceljet.net/articles/excel-pivot-tables)
 are a great way to explore data _without formulas_.

### What's next?

Below are guides to learn more about Excel formulas. We also offer [online video training](https://exceljet.net/training)
.

*   [Formula basics](https://exceljet.net/articles/excel-formulas-and-functions)
     - if you're just getting started
*   [500 formula examples](https://exceljet.net/formulas)
     with full explanations
*   [101 important Excel functions](https://exceljet.net/articles/101-excel-functions)
    
*   [Guide to all Excel functions](https://exceljet.net/functions)
     (work in progress)
*   [Formula criteria - 50 examples](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [Formulas for conditional formatting](https://exceljet.net/conditional-formatting-formulas)
    

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    
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