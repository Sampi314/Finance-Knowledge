# Simple currency conversion - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/simple-currency-conversion

---

[Skip to main content](https://exceljet.net/formulas/simple-currency-conversion#main-content)

[](https://exceljet.net/formulas/simple-currency-conversion#)

*   [Previous](https://exceljet.net/formulas/show-formula-text-with-formula)
    
*   [Next](https://exceljet.net/formulas/sort-and-extract-unique-values)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Simple currency conversion
==========================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Simple currency conversion](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/simple%20currency%20conversion4.png "Excel formula: Simple currency conversion")

Summary
-------

To convert from a given currency to other specific currencies, you can use the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 with a lookup table that contains conversion rates. In the example shown, the formula in E5 is:

    =VLOOKUP(D5,xtable,2,0)*B5
    

Where "xtable" is the [named range](https://exceljet.net/articles/named-ranges)
 G5:H10. As the formula is copied down, it converts the amount in column B from US Dollars (USD) to the currency indicated in column D.

Generic formula
---------------

    =VLOOKUP(currency,xtable,column,0)*amount

Explanation 
------------

The formula in this example converts amounts in USD to other currencies using currency codes and a simple lookup table. The available currencies and exact conversion rates can be adjusted by editing the values in the table on the right. The core of this formula is the VLOOKUP function, configured like this:

    =VLOOKUP(D5,xtable,2,0)
    

The inputs to VLOOKUP are given as follows:

*   _lookup\_value_ - the currency code in D5
*   _table\_array_ - the currency conversion table in G5:H10, given as the named range **xtable**
*   _col\_index\_num_ - 2, because we want to return values from column H
*   _range\_lookup_ - 0, because we want VLOOKUP to perform an exact match

For more information on VLOOKUP, see this [detailed overview](https://exceljet.net/functions/vlookup-function)
.

In this configuration, VLOOKUP finds the currency in the table and retrieves the conversion rate from column H. The result from VLOOKUP is then multiplied by the value in B5, which is the number of US dollars to convert.

_Note: If a currency code does not exist in the table, VLOOKUP will return a #N/A error._

### Nested IF equivalent

Note that it is possible to build a formula to do a currency conversion by nesting multiple IF functions together and hardcoding the currency rates directly into the formula like this:

    =IF(D5="usd",1,
    IF(D5="eur",0.84,
    IF(D5="yen",112.35,
    IF(D5="can",1.23,
    IF(D5="gpb",0.74,
    IF(D5="cny",6.59))))))*B5
    

_Note: in the formula above, [line breaks](https://exceljet.net/shortcuts/insert-line-break-in-cell)
 have been added for [better readability](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
._

I present this option here to illustrate how the VLOOKUP option is superior. It's a much simpler formula, and the exchange rate values are not stored redundantly in many different formulas. In addition, keeping the lookup table on the worksheet makes it easy to see and edit the exchange rates (in one place) at any time.

Related formulas
----------------

[![Excel formula: Map text to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20text%20to%20numbers.png "Excel formula: Map text to numbers")](https://exceljet.net/formulas/map-text-to-numbers)

### [Map text to numbers](https://exceljet.net/formulas/map-text-to-numbers)

This formula uses the value in cell F7 for a lookup value, the range B6:C10 for the lookup table, the number 2 to indicate "2nd column", and zero as the last argument to force an exact match. Although in this case we are mapping text values to numeric outputs, the same formula can handle text to...

[![Excel formula: Lookup up cost for product or service](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20up%20cost%20for%20product%20or%20service.png "Excel formula: Lookup up cost for product or service")](https://exceljet.net/formulas/lookup-up-cost-for-product-or-service)

### [Lookup up cost for product or service](https://exceljet.net/formulas/lookup-up-cost-for-product-or-service)

This is a basic example of VLOOKUP in "exact match" mode. The lookup value is B6, the table is the range B5:C7, the column is 2, and the last argument, FALSE, forces VLOOKUP to do an exact match. (Read why this is necessary here ). If VLOOKUP finds a matching value, the associated cost will be...

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: Nested IF function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nested_if_function_example.png "Excel formula: Nested IF function example")](https://exceljet.net/formulas/nested-if-function-example)

### [Nested IF function example](https://exceljet.net/formulas/nested-if-function-example)

The goal is to assign a grade to each score in column C according to the rules in the table in the range F4:G9. One way to do this in Excel is to use a series of nested IF functions. Generally, nested IFs formulas are used to test more than one condition and return a different result for each...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20make%20a%20nested%20IF%20formula%20easier%20to%20read.png)](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

### [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

In this video we're going to look at how to make a nested IF formula more readable by adding line breaks. Here I have a worksheet that calculates sales commissions based on the commission structure shown in the table. For example, we can see that King sold $124,500 and gets a commission of 5%,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20replace%20nested%20IFs%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

### [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

You might build or inherit a worksheet that uses a series of nested IF statements to assign values of some kind. Many people use nested IF statements this way because the approach is easy once you get the hang of it. But nested IF statements can be difficult to maintain and debug. Let's look at how...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Map text to numbers](https://exceljet.net/formulas/map-text-to-numbers)
    
*   [Lookup up cost for product or service](https://exceljet.net/formulas/lookup-up-cost-for-product-or-service)
    
*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [Nested IF function example](https://exceljet.net/formulas/nested-if-function-example)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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