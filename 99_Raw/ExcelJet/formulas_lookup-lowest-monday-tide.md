# Lookup lowest Monday tide - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lookup-lowest-monday-tide

---

[Skip to main content](https://exceljet.net/formulas/lookup-lowest-monday-tide#main-content)

[](https://exceljet.net/formulas/lookup-lowest-monday-tide#)

*   [Previous](https://exceljet.net/formulas/lookup-latest-price)
    
*   [Next](https://exceljet.net/formulas/lookup-lowest-value)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Lookup lowest Monday tide
=========================

by Dave Bruns · Updated 21 Feb 2020

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[IF](https://exceljet.net/functions/if-function)

[MIN](https://exceljet.net/functions/min-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/5700/download?token=pGOSVtP0)
 (15.65 KB)

![Excel formula: Lookup lowest Monday tide](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lookup%20lowest%20monday%20tide.png "Excel formula: Lookup lowest Monday tide")

Summary
-------

To find the lowest tide on a Monday, given a set of data with many days of high and low tides, you can use an array formula based on the IF and MIN functions. In the example shown, the formula in I6 is:

    {=MIN(IF(day=I5,IF(tide="L",pred)))}
    

which returns the lowest Monday tide in the data, -0.64

To retrieve the date of the lowest Monday tide, the formula in I7 is:

    {=INDEX(date,MATCH(1,(day=I5)*(tide="L")*(pred=I6),0))}
    

Where the worksheet contains the following [named ranges](https://exceljet.net/glossary/named-range)
: **date** (B5:B124), **day** (C5:C124), **time** (D5:D124), **pred** (E5:E124), **tide** (F5:F124).

_Both are [array formulas](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

Data from [tidesandcurrents.noaa.gov](https://tidesandcurrents.noaa.gov/)
 for Santa Cruz, California.

Explanation 
------------

At a high level, this example is about finding a minimum value based on multiple criteria. To do that, we are using the [MIN function](https://exceljet.net/functions/min-function)
 together with two nested [IF functions](https://exceljet.net/functions/if-function)
:

    {=MIN(IF(day=I5,IF(tide="L",pred)))}
    

working from the inside out, the first IF checks if the day is "Mon", based on the value in I5:

    IF(day=I5 // is day "Mon"
    

If the result is TRUE, we run another IF:

    IF(tide="L",pred) // if tide is "L" return prediction
    

In other words, if the day is "Mon", we check if the tide is "L". If so, we return the predicted tide level, using the [named range](https://exceljet.net/glossary/named-range)
 **pred**.

Notice we do not provide a "value if false" for either IF. That means if either logical test is FALSE, the outer IF will return FALSE. For more information on nested IFs, [see this article](https://exceljet.net/articles/nested-ifs)
.

It's important to understand that the data set includes 120 rows, so each of the named ranges in the formula contain 120 values. This is what makes this an array formula – we are processing many values at once. After both IFs are evaluated, the outer IF will return an array that contains 120 values like this:

    {FALSE;FALSE;FALSE;FALSE;FALSE;3.27;FALSE;0.3;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;2.02;FALSE;0.17;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;3.04;FALSE;-0.55;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;1.96;FALSE;-0.64;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;3;FALSE;-0.02;FALSE;FALSE;FALSE;FALSE}
    

The key thing to notice here is only values associated with Monday and low tide survive the trip through the nested IFs. The other values have been replaced with FALSE. In other words, we are using the double IF structure to "throw away" values we aren't interested in.

The array above is returned directly to the [MIN function](https://exceljet.net/functions/min-function)
. The MIN function automatically ignores the FALSE values, and returns the minimum value of those that remain, -0.64.

_This is an [array formulas](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

### Minimum with MINIFS

If you have Office 365 or Excel 2019, you can use the [MINIFS function](https://exceljet.net/functions/minifs-function)
 to get the lowest Monday tide like this:

    =MINIFS(pred,day,"Mon",tide,"L")
    

The result is the same, and this formula does not require control + shift + enter.

### Get the date

Once you find the minimum Monday tide level, you will undoubtedly want to know the date and time. This can be done with an [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula. The formula in I7 is:

    {=INDEX(date,MATCH(1,(day=I5)*(tide="L")*(pred=I6),0))}
    

Working from the inside out, we need to first locate the position of the lowest Monday tide with the MATCH function:

    MATCH(1,(day=I5)*(tide="L")*(pred=I6),0))
    

Here, we run through the same conditional tests we applied above to restrict processing to Monday low tides only. However, we apply one more test to restrict results to the minimum value now in I6, and we use a slightly simpler syntax based on [boolean logic](https://exceljet.net/glossary/boolean-logic)
 to apply criteria. We have three separate expressions, each testing one condition:

    (day=I5)* // day is "Mon"
    (tide="L")* // tide is "L"
    (pred=I6) // prediction is min value
    

Each of these expressions runs on 120 values and returns an array of 120 TRUE FALSE results. When these arrays are multiplied by one another, the TRUE FALSE values are coerced to 1s and 0s. The result is a single array like this:

    {0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0}
    

Because there is only one value in the entire data set that meets all three conditions, there is only a single 1 in the array.

Now you can see why we have configured the [MATCH function](https://exceljet.net/functions/match-function)
 to look for the number 1 in exact match mode. MATCH locates the 1, and returns a position of 88 directly to the [INDEX function](https://exceljet.net/functions/index-function)
. We can now rewrite the formula like this:

    =INDEX(date,88) // returns 23-Dec-19
    

The INDEX function then returns the 88th value in the named range **date**, which is 23-Dec-19. This is the date that corresponds to the lowest Monday tide level.

_This is an [array formulas](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

### Get the time

The formula to retrieve the time of the lowest Monday tide is almost the same as the formula to get the date. The only difference is that the named range **time** is provided to INDEX instead of **date**. The formula in I8 is:

    {=INDEX(time,MATCH(1,(day=I5)*(tide="L")*(pred=I6),0))}
    

In other respects the behavior of the formula is the same, so we end up with a similar result:

    =INDEX(time,88) // returns 2:44 PM
    

As before, INDEX returns the 88th item in the array, which is 2:44 PM.

_This is an [array formulas](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

_Note: in the event of a tie (two Monday low tides with the same value), the INDEX and MATCH formulas above will return the first match._

### Date and time with XLOOKUP

With the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
, you can simplify the formulas used to get the date and time associated with the lowest tide:

    =XLOOKUP(1,(day=I5)*(tide="L")*(pred=I6),date) // get date
    =XLOOKUP(1,(day=I5)*(tide="L")*(pred=I6),time) // get time
    

This is an example that nicely shows off XLOOKUP's flexibility. We can use exactly the same logic from the INDEX and MATCH formulas above, in a simple and elegant formula.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: Minimum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_if_multiple_criteria.png "Excel formula: Minimum if multiple criteria")](https://exceljet.net/formulas/minimum-if-multiple-criteria)

### [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)

In this example, the goal is to get the minimum value for a given group above a specific temperature. In other words, we want the min value after applying multiple criteria. The easiest way to solve this problem is with the MINIFS function. However, if you need more flexibility (for example, you...

[![Excel formula: Max if criteria match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max%20if%20criteria%20match.png "Excel formula: Max if criteria match")](https://exceljet.net/formulas/max-if-criteria-match)

### [Max if criteria match](https://exceljet.net/formulas/max-if-criteria-match)

The example shown contains almost 10,000 rows of data. The data represents temperature readings taken every 2 minutes over a period of days. For any given date (provided in cell H7), we want to get the maximum temperature on that date. Inside the IF function , logical test is entered as B5:B9391=H7...

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: INDEX and MATCH approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match.png "Excel formula: INDEX and MATCH approximate match")](https://exceljet.net/formulas/index-and-match-approximate-match)

### [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table to the right. For convenience only, grade (G5:G9) and score (F5:F9) are named ranges . This is a classic "approximate-match" lookup problem because it is unlikely that a...

[![Excel formula: Two-way approximate match multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20approximate%20match%20multiple%20criteria%20v2.png "Excel formula: Two-way approximate match multiple criteria")](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)

### [Two-way approximate match multiple criteria](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)

The goal is to lookup a feed rate based on material, hardness, and drill bit diameter. Feed rate values are in the named range data (D6:H16). This can be done with a two-way INDEX and MATCH formula. One MATCH function works out the row number (material and hardness), and the other MATCH function...

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

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20MATCH%20Function%20for%20exact%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

### [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

The MATCH function finds the relative position of an item in a list. MATCH can find exact matches or approximate matches. In this video, we'll look at how to use MATCH to find an exact match. The MATCH function takes three arguments: the lookup\_value, which is the value you're looking up, the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

### [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

In this video we're going to combine INDEX and MATCH together to look things up. Here we have the city population data we looked at before. We used the INDEX function to retrieve information about a city with a hard-coded position value. When we supply a number, INDEX retrieves information for the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)
    
*   [Max if criteria match](https://exceljet.net/formulas/max-if-criteria-match)
    
*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)
    
*   [Two-way approximate match multiple criteria](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    
*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    

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