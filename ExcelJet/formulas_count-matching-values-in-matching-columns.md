# Count matching values in matching columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-matching-values-in-matching-columns

---

[Skip to main content](https://exceljet.net/formulas/count-matching-values-in-matching-columns#main-content)

[](https://exceljet.net/formulas/count-matching-values-in-matching-columns#)

*   [Previous](https://exceljet.net/formulas/count-matches-between-two-columns)
    
*   [Next](https://exceljet.net/formulas/count-missing-values)
    

[Count](https://exceljet.net/formulas#Count)

Count matching values in matching columns
=========================================

by Dave Bruns · Updated 22 Jun 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[MATCH](https://exceljet.net/functions/match-function)

[SEARCH](https://exceljet.net/functions/search-function)

![Excel formula: Count matching values in matching columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Count%20matching%20values%20in%20matching%20columns.png "Excel formula: Count matching values in matching columns")

Summary
-------

To count matching values in matching columns, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 together with the [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [MATCH](https://exceljet.net/functions/match-function)
 functions. In the example shown, the formula in J6 is:

    =SUMPRODUCT(ISNUMBER(MATCH(headers,{"A","B"},0))*ISNUMBER(MATCH(data,{"z","c"},0)))
    

where **data** (B5:G14) and **headers** (B4:G4) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is 22, since there are 22 values that are either "z" or "c" in columns labeled "A" or "B".

Explanation 
------------

In this example, the goal is to count "z" or "c" values in the [named range](https://exceljet.net/glossary/named-range)
 **data**, but only when the column header is "A" or "B". The formula used to perform this calculation is based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
:

    =SUMPRODUCT(ISNUMBER(MATCH(headers,{"A","B"},0))*ISNUMBER(MATCH(data,{"z","c"},0)))
    

Working from the inside out, note that SUMPRODUCT contains a single [argument](https://exceljet.net/glossary/function-argument)
, which is composed of this expression:

    ISNUMBER(MATCH(headers,{"A","B"},0))*ISNUMBER(MATCH(data,{"z","c"},0))
    

This expression is formed from two parts, each representing a logical test. The left part tests column headers, and the right tests values.  The two parts are joined with multiplication (\*) because the overall logic is AND, and multiplication corresponds to AND in [Boolean algebra](https://exceljet.net/glossary/boolean-logic)
.

On the _left_, the [MATCH function](https://exceljet.net/functions/match-function)
 is used with the ISNUMBER function to match target columns:

    ISNUMBER(MATCH(headers,{"A","B"},0)) // match "A" or "B"
    

Inside MATCH, notice the arguments are "reversed" to maintain the existing data structure: the **header** values are used for the _lookup\_value_ argument, and the _array_ argument is provided as an [array constant](https://exceljet.net/glossary/array-constant)
 that contains the values we are looking for, "A" and "B". The result from MATCH is an [array](https://exceljet.net/glossary/array)
 composed of #N/A errors or numbers. The numbers indicate matched positions:

    {1,2,#N/A,1,2,#N/A}
    

There are 6 items in this array because we are testing 6 columns. The numbers represent matched columns and errors represent columns that do not match. This array is returned and handed off to the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
:

    ISNUMBER({1,2,#N/A,1,2,#N/A}) // convert to TRUE or FALSE
    

which returns an array like this:

    {TRUE,TRUE,FALSE,TRUE,TRUE,FALSE}
    

Note the TRUE values correspond to columns that are either "A" or "B". This completes the column matching logic.

On the _right_ side of the expression, we have similar logic to test the values themselves:

    ISNUMBER(MATCH(data,{"z","c"},0))
    

The MATCH function is again used to check for two values "z" or "c" with the same reversed argument approach. Because the named range data contains 60 values, the result from MATCH is an array with 60 values:

    {2,#N/A,2,#N/A,1,1;#N/A,#N/A,2,2,1,2;2,2,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,1,2,2,2;#N/A,2,#N/A,2,#N/A,1;2,#N/A,2,2,2,2;2,2,#N/A,2,#N/A,2;#N/A,2,#N/A,#N/A,2,#N/A;1,#N/A,1,1,#N/A,1;2,1,2,#N/A,#N/A,2}
    

The ISNUMBER function again translates this array into TRUE and FALSE values:

    {TRUE,FALSE,TRUE,FALSE,TRUE,TRUE;FALSE,FALSE,TRUE,TRUE,TRUE,TRUE;TRUE,TRUE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,TRUE,TRUE,TRUE,TRUE;FALSE,TRUE,FALSE,TRUE,FALSE,TRUE;TRUE,FALSE,TRUE,TRUE,TRUE,TRUE;TRUE,TRUE,FALSE,TRUE,FALSE,TRUE;FALSE,TRUE,FALSE,FALSE,TRUE,FALSE;TRUE,FALSE,TRUE,TRUE,FALSE,TRUE;TRUE,TRUE,TRUE,FALSE,FALSE,TRUE}
    

Now the original expression above (inside SUMPRODUCT) can be written like this:

    {TRUE,TRUE,FALSE,TRUE,TRUE,FALSE}*{TRUE,FALSE,TRUE,FALSE,TRUE,TRUE;FALSE,FALSE,TRUE,TRUE,TRUE,TRUE;TRUE,TRUE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,TRUE,TRUE,TRUE,TRUE;FALSE,TRUE,FALSE,TRUE,FALSE,TRUE;TRUE,FALSE,TRUE,TRUE,TRUE,TRUE;TRUE,TRUE,FALSE,TRUE,FALSE,TRUE;FALSE,TRUE,FALSE,FALSE,TRUE,FALSE;TRUE,FALSE,TRUE,TRUE,FALSE,TRUE;TRUE,TRUE,TRUE,FALSE,FALSE,TRUE}
    

Note the multiplication operator is still there, just after the first array. In Excel any math operation will automatically convert TRUE and FALSE values to their numeric equivalents, 1 and 0. This means you can think of the expression like this:

    {1,1,0,1,1,0}*{1,0,1,0,1,1;0,0,1,1,1,1;1,1,0,0,0,0;0,0,1,1,1,1;0,1,0,1,0,1;1,0,1,1,1,1;1,1,0,1,0,1;0,1,0,0,1,0;1,0,1,1,0,1;1,1,1,0,0,1}
    

After the expression is evaluated, we have a single array like this:

    {1,0,0,0,1,0;0,0,0,1,1,0;1,1,0,0,0,0;0,0,0,1,1,0;0,1,0,1,0,0;1,0,0,1,1,0;1,1,0,1,0,0;0,1,0,0,1,0;1,0,0,1,0,0;1,1,0,0,0,0}
    

This array is delivered to the SUMPRODUCT function as the _array1_ argument. Then, with only one array to process, SUMPRODUCT sums the items in the array and returns a final result: 22.

_Note: although SUMPRODUCT can handle multiple arrays as separate arguments, you will see many formulas that place all logic into a single argument. Doing so takes advantage of the fact that Excel automatically coerces TRUE and FALSE values to 1s and 0s during any math operation. When the logic is separated into separate arrays, an [additional step](https://exceljet.net/videos/how-to-convert-booleans-to-numbers)
 must be taken to convert to 1s and 0s. For more details, see [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)
_

### Contains logic

In the example shown above testing logic is "equal to". The columns must be equal to "A" or "B" and the values must be equal to "z" or "c". But sometimes you need to test with "contains" logic. For example, test for values that _contain_ "z" or _contain_ "c".

One consequence of reversing the arguments inside the MATCH function is that [wildcards](https://exceljet.net/glossary/wildcard)
 can't be used with the lookup values, because these values appear as the _array_ argument. If you need to test values using _contains_ logic, you can switch to another approach based on [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 with the [SEARCH function](https://exceljet.net/functions/search-function)
. For example, to match values that _contain_ "x" or "c", you can use an expression like this:

    =ISNUMBER(SEARCH("z",data))+ISNUMBER(SEARCH("c",data))
    

Note we are joining each test with the [addition operator](https://exceljet.net/glossary/math-operators)
 (+) because in Boolean algebra [addition corresponds to OR logic](https://exceljet.net/videos/boolean-algebra-in-excel)
. The final formula would then look like this:

    =SUMPRODUCT(ISNUMBER(MATCH(headers,{"A","B"},0))*(ISNUMBER(SEARCH("z",data))+ISNUMBER(SEARCH("c",data))))
    

Note an additional set of parentheses () have been added to control [order of operations](https://exceljet.net/glossary/order-of-operations)
.

Related formulas
----------------

[![Excel formula: Sum matching columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20matching%20columns.png "Excel formula: Sum matching columns")](https://exceljet.net/formulas/sum-matching-columns)

### [Sum matching columns](https://exceljet.net/formulas/sum-matching-columns)

At the core, this formula relies on the SUMPRODUCT function to sum values in matching columns in the named range data C5:G14. If all data were provided to SUMPRODUCT in a single range, the result would be the sum of all values in the range: =SUMPRODUCT(data) // all data, returns 387 To apply a...

[![Excel formula: Sum matching columns and rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_matching_columns_and_rows.png "Excel formula: Sum matching columns and rows")](https://exceljet.net/formulas/sum-matching-columns-and-rows)

### [Sum matching columns and rows](https://exceljet.net/formulas/sum-matching-columns-and-rows)

In this example, the goal is to sum values in matching columns and rows. Specifically, we want to sum values in data (C5:G14) where the column code is "A" and the day is "Wed". One way to solve this problem is with the SUMPRODUCT function , which can handle array operations natively, without...

[![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")](https://exceljet.net/formulas/sum-every-nth-column)

### [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)

In this example, the goal is to sum every nth value by column in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value by column, if n =3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and n is entered into...

[![Excel formula: Sum columns based on adjacent criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20columns%20based%20on%20adjacent%20criteria.png "Excel formula: Sum columns based on adjacent criteria")](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)

### [Sum columns based on adjacent criteria](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)

In this example, the goal is to sum the values in columns C, E, G, and I conditionally using the text values in columns B, D, F, and H for criteria. This problem can be solved with the SUMPRODUCT function , which is designed to multiply ranges or arrays together and return the sum of products. The...

[![Excel formula: Copy value from every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20column.png "Excel formula: Copy value from every nth column")](https://exceljet.net/formulas/copy-value-from-every-nth-column)

### [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)

In Excel, you can't easily create formulas that skip columns following a certain pattern, because the references in the formula will automatically change to maintain the relationship between the original source cell and the new target cell. However, with a little work, it's possible to construct...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum matching columns](https://exceljet.net/formulas/sum-matching-columns)
    
*   [Sum matching columns and rows](https://exceljet.net/formulas/sum-matching-columns-and-rows)
    
*   [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
    
*   [Sum columns based on adjacent criteria](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)
    
*   [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    

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