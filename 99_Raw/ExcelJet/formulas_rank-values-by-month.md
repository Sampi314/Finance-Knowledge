# Rank values by month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/rank-values-by-month

---

[Skip to main content](https://exceljet.net/formulas/rank-values-by-month#main-content)

[](https://exceljet.net/formulas/rank-values-by-month#)

*   [Previous](https://exceljet.net/formulas/rank-race-results)
    
*   [Next](https://exceljet.net/formulas/rank-with-ordinal-suffix)
    

[Rank](https://exceljet.net/formulas#Rank)

Rank values by month
====================

by Dave Bruns · Updated 29 Jul 2022

Related functions 
------------------

[LARGE](https://exceljet.net/functions/large-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[TEXT](https://exceljet.net/functions/text-function)

[IF](https://exceljet.net/functions/if-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6158/download?token=IJkR5oJ0)
 (15.42 KB)

![Excel formula: Rank values by month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/display%20ranked%20names%20by%20month.png "Excel formula: Rank values by month")

Summary
-------

To display a list of names, ranked by a numeric value, you can use formulas based on [LARGE](https://exceljet.net/functions/large-function)
, [INDEX](https://exceljet.net/functions/index-function)
, [MATCH](https://exceljet.net/functions/match-function)
, with help from the [TEXT function](https://exceljet.net/functions/text-function)
. In the example shown, the formula in G5 is:

    =LARGE(IF(TEXT(date,"mmmm")=G$4,amount),$F5)
    

And the formula in G10 is:

    =INDEX(client,MATCH(1,(amount=G5)*(TEXT(date,"mmmm")=G$9),0))
    

where **client** (B5:B17) **date** (C5:C17) and **amount** (D5:D17) are [named ranges](https://exceljet.net/glossary/named-range)
.

_Note: these are [array formulas](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Explanation 
------------

This example is set up in two parts for clarity: (1) a formula to determine the top 3 amounts for each month and (2) a formula to retrieve the client name for each of the top 3 monthly amounts.

Note there is no actual rank in the source data. Instead, we are using the LARGE function to work directly with amounts. Another approach would be to add rank to the source data with the [RANK function](https://exceljet.net/functions/rank-function)
, and use the rank value to retrieve client names.

### Part 1: retrieve top 3 amounts each month

To retrieve the top 3 amounts for each week, the formula in G5 is:

    =LARGE(IF(TEXT(date,"mmmm")=G$4,amount),$F5)
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Working from the inside out, we first use the TEXT function to get month names for each date in the named range **date**:

    TEXT(date,"mmmm") // get month names
    

The [custom number format](https://exceljet.net/articles/custom-number-formats)
 "mmmm" will return a string like "April", "May", "June" for each name in the named range **date**. The result is an [array](https://exceljet.net/glossary/array)
 of month names like this:

    {"April";"April";"April";"April";"May";"May";"May";"May";"May";"June";"June";"June";"June"}
    

The TEXT function delivers this array to the [IF function](https://exceljet.net/videos/the-if-function)
, which is configured to filter dates on a given month by testing the month name against the value in G4 (a [mixed reference](https://exceljet.net/glossary/mixed-reference)
, so the formula can be copied down and across):

    IF(TEXT(date,"mmmm")=G$4,amount) // filter on month
    

Only amounts in April survive and make it through IF; all other values are FALSE:

    {10500;15200;18500;12500;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

Finally, the LARGE function uses the value in F5 (also a mixed reference) to return the "nth" largest value that remains. In cell G5, LARGE returns 18,500, the "1st" largest value. As the formula is copied down and across the table, the LARGE function returns the top 3 amounts in each of the three months.

Now that we know the top 3 values in each month, we can use this information like a "key" to retrieve the client name for each.

### Part 2: retrieve client names

Note: This is an example of using INDEX and MATCH with multiple criteria. If this concept is new to you, [here is a basic example](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
.

![Formula to retrieve names based on rank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/display%20ranked%20names%20by%20month%20name%20formula.png?itok=VD_vIl7Z "Formula to retrieve names based on rank")

To retrieve the name associated with the top three values in G5:I7, we use [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
:

    =INDEX(client,MATCH(1,(amount=G5)*(TEXT(date,"mmmm")=G$9),0))
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Working from the inside out, the MATCH function is configured to use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 like this:

    MATCH(1,(amount=G5)*(TEXT(date,"mmmm")=G$9),0)
    

The _lookup\_value_ is 1, and the _lookup\_array_ is constructed with this expression:

    (amount=G5)*(TEXT(date,"mmmm")=G$9)
    

The expression that creates the _lookup\_array_ uses Boolean logic to "filter out" amounts that are (1) not in April, and (2) not the value in G5 (18,500). The result is an array of 1s and 0s like this:

    {0;0;1;0;0;0;0;0;0;0;0;0;0}
    

With a _lookup\_value_ of 1 and zero for _match\_type_ (to force an exact match) MATCH returns 3 directly to the INDEX function:

    =INDEX(client,3) // returns "Janus"
    

INDEX returns the third value in the named range client, "Janus".

As the formula is copied down and across the table, it returns the top 3 clients in each of the three months.

Related formulas
----------------

[![Excel formula: Rank function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20function%20example1.png "Excel formula: Rank function example")](https://exceljet.net/formulas/rank-function-example)

### [Rank function example](https://exceljet.net/formulas/rank-function-example)

You can use the RANK function to rank numeric values. RANK has two modes of operation: ranking values where the largest value is #1 (order = 0), and ranking values where the lowest value is #1 (order = 1). In this case, we are ranking test scores, so the highest value should rank #1, so we omit the...

[![Excel formula: Rank if formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20with%20criteria.png "Excel formula: Rank if formula")](https://exceljet.net/formulas/rank-if-formula)

### [Rank if formula](https://exceljet.net/formulas/rank-if-formula)

Although Excel has a RANK function , there is no RANKIF function to perform a conditional rank. However, you can easily create a conditional RANK with the COUNTIFS function. The COUNTIFS function can perform a conditional count using two or more criteria. Criteria are entered in range/criteria...

Related functions
-----------------

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Rank function example](https://exceljet.net/formulas/rank-function-example)
    
*   [Rank if formula](https://exceljet.net/formulas/rank-if-formula)
    

### Functions

*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

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