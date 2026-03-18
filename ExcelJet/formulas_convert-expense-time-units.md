# Convert expense time units - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-expense-time-units

---

[Skip to main content](https://exceljet.net/formulas/convert-expense-time-units#main-content)

[](https://exceljet.net/formulas/convert-expense-time-units#)

*   [Previous](https://exceljet.net/formulas/convert-column-number-to-letter)
    
*   [Next](https://exceljet.net/formulas/convert-feet-and-inches-to-inches)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Convert expense time units
==========================

by Dave Bruns · Updated 5 Oct 2020

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/5739/download?token=Ss6XbCG7)
 (11.59 KB)

![Excel formula: Convert expense time units](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20expense%20time%20units.png "Excel formula: Convert expense time units")

Summary
-------

To convert an expense in one time unit (i.e. daily, weekly, monthly, etc.) to other time units, you can use a two-way INDEX and MATCH formula. In the example shown, the formula in E5 (copied across and down) is :

    =$C5*INDEX(data,MATCH($D5,vunits,0),MATCH(F$4,hunits,0))
    

where **data** (O5:S9), **vunits** (N5:N9), and **hunits** (O4:S4) are [named ranges](https://exceljet.net/glossary/named-range)
, as explained below.

Explanation 
------------

To convert an expense in one time unit (i.e. daily, weekly, monthly, etc.) to other time units, you can use a two-way INDEX and MATCH formula. In the example shown, the formula in E5 (copied across and down) is :

    =$C5*INDEX(data,MATCH($D5,vunits,0),MATCH(F$4,hunits,0))
    

This formula uses a lookup table with [named ranges](https://exceljet.net/glossary/named-range)
 as shown below:

![Conversion table for lookups](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/normalize%20expense%20time%20unit%20conversion%20table.png?itok=wnV9ZxPa "Conversion table for lookups")

Named ranges: **data** (O5:S9), **vunits** (N5:N9), and **hunits** (O4:S4).

### Introduction

The goal is to convert an expense in one time unit, to an equivalent expense in other time units. For example, if we have a _monthly_ expense of $30, we want to calculate an _annual_ expense of $360, a _weekly_ expense of $7.50, etc.

Like so many challenges in Excel, much depends on how you approach the problem. You might first be tempted to consider a chain of [nested IF](https://exceljet.net/articles/nested-ifs)
 formulas. This can be done, but you'll end up with a long and complicated formula.

A cleaner approach is to build a lookup table that contains conversion factors for all possible conversions, then use a two-way [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
 to retrieve the required value for a given conversion. Once you have the value, you can simply multiply by the original amount.

### The conversion table

The conversion table has the same values for both vertical and horizontal labels: daily, weekly, biweekly, monthly, and annual. The "from" units are listed vertically, and the "to" units are listed horizontally. For the purposes of this example, we want to match the row first, then the column. So, if we want to convert a monthly expense to an annual expense, we match the "monthly" row, and the "annual" column, and return 12.

![Conversion value lookup steps](https://exceljet.net/sites/default/files/images/formulas/inline/normalize%20expense%20time%20unit%20lookup%20steps.png "Conversion value lookup steps")

To populate the table itself, we use a mix of simple formulas and constants:

![Conversion value formulas and constants](https://exceljet.net/sites/default/files/images/formulas/inline/normalize%20expense%20time%20unit%20conversion%20values.png "Conversion value formulas and constants")

_Note: Customize conversion values to meet your specific needs. Entering a value as =1/7 is an easy way to avoid entering long decimal values._

### The lookup formula

Since we need to locate a conversion value based on two inputs, a "from" time unit and a "to" time unit, we need a two-way lookup formula. INDEX and MATCH provides a nice solution.  In the example shown, the formula in E5 is:

    =$C5*INDEX(data,MATCH($D5,vunits,0),MATCH(F$4,hunits,0))
    

Working from the inside out, the first [MATCH function](https://exceljet.net/functions/match-function)
 locates the correct row:

    MATCH($D5,vunits,0) // find row, returns 4
    

We pull the original "from" time unit from column D, which we use to find the right row in the named range **vunits** (N5:N9). Note $D5 is a [mixed reference](https://exceljet.net/glossary/mixed-reference)
 with the _column_ locked, so the formula can be copied across. 

The second MATCH function locates the column:

    MATCH(F$4,hunits,0) // find column, returns 5
    

Here, we get the lookup value from the column header in row 4, and use this to find the right "to" column in the named range **hunits** (O4:S4). Again, note F$4 is a mixed reference with the _row_ locked, so the formula can be copied down. 

After both MATCH formulas return results to INDEX, we have:

    =$C5*INDEX(data,4,5)
    

The _array_ provided to INDEX is the named range **data**, (O5:S9). With a row of 4 and column of 5, [INDEX](https://exceljet.net/functions/index-function)
 returns 12, so we get a final result of 12000 like this:

    =$C5*INDEX(data,4,5)
    =1000*12
    =12000
    

Related formulas
----------------

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: Two-way lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20lookup%20with%20INDEX%20and%20MATCH.png "Excel formula: Two-way lookup with INDEX and MATCH")](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

### [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

In this example, the goal is to perform a two-way lookup, sometimes called a matrix lookup . This means we need to create a match on both rows and columns and return the value at the intersection of this two-way match The core of this formula is INDEX, which is simply retrieving a value from C6:G10...

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

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20do%20a%20two-way%20lookup%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

### [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

In this video we'll look at how to set up a classic two-way lookup using INDEX and MATCH . Here we have a list of salespeople with monthly sales figures. What we want to do is add a formula in Q6 that looks up and retrieves a sales number based on the name and month above. To do this, we'll use the...

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

*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    
*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    

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