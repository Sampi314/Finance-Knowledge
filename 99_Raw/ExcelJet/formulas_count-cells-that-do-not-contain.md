# Count cells that do not contain - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-do-not-contain

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-do-not-contain#main-content)

[](https://exceljet.net/formulas/count-cells-that-do-not-contain#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-contain-text)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that do not contain
===============================

by Dave Bruns · Updated 10 Feb 2025

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[SEARCH](https://exceljet.net/functions/search-function)

[FIND](https://exceljet.net/functions/find-function)

[NOT](https://exceljet.net/functions/not-function)

![Excel formula: Count cells that do not contain](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20do%20not%20contain.png "Excel formula: Count cells that do not contain")

Summary
-------

To count cells that _do not contain_ certain text, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 with a [wildcard](https://exceljet.net/glossary/wildcard)
. In the example shown, the formula in E5 is:

    =COUNTIF(data,"<>*a*")
    

In this formula, **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15. The result is 5 since five cells in B5:B15 do not contain the letter "a".

Generic formula
---------------

    =COUNTIF(range,"<>*txt*")

Explanation 
------------

In this example, the goal is to count cells that _do not contain_ a specific substring. This problem can be solved with the [COUNTIF function](https://exceljet.net/functions/countif-function)
 or the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. Both approaches are explained below. Although COUNTIF is _not_ case-sensitive, the SUMPRODUCT version of the formula can be adapted to perform a case-sensitive count. For convenience, **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15.

### COUNTIF function

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 counts cells in a range that meet supplied criteria. For example, to count the number of cells in a [range](https://exceljet.net/glossary/range)
 that contain "apple" you can use COUNTIF like this:

    =COUNTIF(range,"apple") // equal to "apple"
    

Note this is an exact match. To be included in the count, a cell must contain "apple" and only "apple". If a cell contains any other characters, it will not be counted. To reverse this operation and count cells that _do not contain_ "apple", you can add the not equal to (<>) [operator](https://exceljet.net/glossary/logical-operators)
 like this:

    =COUNTIF(range,"<>apple") // not equal to "apple"
    

The goal in this example is to count cells that _do not contain_ specific text, where the text is a _substring_ that can be anywhere in the cell. To do this, we need to use the asterisk (\*) character as a [wildcard](https://exceljet.net/glossary/wildcard)
. To count cells that contain the substring "apple", we can use a formula like this:

    =COUNTIF(range,"*apple*") // contains "apple"
    

The asterisk (\*) wildcard matches zero or more characters of any kind, so this formula will count cells that contain "apple" anywhere in the cell. To count cells that _do not contain_ the substring "apple", we add the not equal to (<>) operator like this:

    =COUNTIF(range,"<>*apple*") // does not contain "apple"
    

The formulas used in the worksheet shown follow the same pattern:

    =COUNTIF(data,"<>*a*") // does not contain "a"
    =COUNTIF(data,"<>*0*") // does not contain "0"
    =COUNTIF(data,"<>*-r*") // does not contain "-r"
    

**Data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15. The COUNTIF function supports three different wildcards, [see this page](https://exceljet.net/functions/countif-function)
 for more details.

Note the COUNTIF formula above won't work if you are targeting a particular number and cells contain _numeric_ data. This is because the wildcard automatically causes COUNTIF to look for text only (i.e. to look for "2" instead of just 2). In addition, COUNTIF is _not_ case-sensitive, so you can't perform a case-sensitive count. The SUMPRODUCT alternative explained below can handle both situations.

### With a cell reference

You can easily adjust this formula to use a cell reference in _criteria_. For example, if A1 contains the substring you want to exclude from the count, you can use a formula like this:

    =COUNTIF(range,"<>*"&A1&"*")
    

Inside COUNTIF, the two asterisks and the not equal to operator (<>) are [concatenated](https://exceljet.net/glossary/concatenation)
 to the value in A1, and the formula works as before.

### Exclude blanks

To exclude blank cells, you can switch to [COUNTIFS  function](https://exceljet.net/functions/countifs-function)
 and add another condition like this:

    =COUNTIFS(range,"<>*a*",range,"?*") // requires some text
    

The second condition means "at least one character".

See also: [50 examples of formula criteria](https://exceljet.net/articles/how-to-use-formula-criteria)

### SUMPRODUCT function

Another way to solve this problem is with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and [Boolean algebra](https://exceljet.net/glossary/boolean-logic)
. This approach has the benefit of being case-sensitive if needed. In addition, you can use this technique to target a number inside of a number, something you can't do with COUNTIF.

To count cells that contain specific text with SUMPRODUCT, you can use the [SEARCH function](https://exceljet.net/functions/search-function)
. SEARCH returns the position of text in a text string as a number. For example, the formula below returns 6 since the "a" appears first as the sixth character in the string:

    =SEARCH( "a","The cat sat") // returns 6
    

If the text is not found, SEARCH returns a #VALUE! error:

    =SEARCH( "x","The cat sat") // returns #VALUE!
    

Notice we do not need to use any wildcards because SEARCH will automatically find substrings. If we get a number from SEARCH, we know the substring _was_ found. If we get an error, we know the substring _was not_ found. This means we can add the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 to evaluate the result from SEARCH like this:

    =ISNUMBER(SEARCH( "a","The cat sat")) // returns TRUE
    =ISNUMBER(SEARCH( "x","The cat sat")) // returns FALSE
    

To reverse the operation, we add the [NOT function](https://exceljet.net/functions/not-function)
:

    =NOT(ISNUMBER(SEARCH( "a","The cat sat"))) // FALSE
    =NOT(ISNUMBER(SEARCH( "x","The cat sat"))) // TRUE
    

We now have what we need to count cells that do not contain a substring with SUMPRODUCT. Back in the example worksheet, to count cells that _do not contain_ "a" with SUMPRODUCT, you can use a formula like this

    =SUMPRODUCT(--NOT(ISNUMBER(SEARCH("a",data))))
    

Working from the inside out, SEARCH is configured to look for "a":

    SEARCH("a",data)
    

Because **data** (B5:B15) contains 11 cells, the result from SEARCH is an [array](https://exceljet.net/glossary/array)
 with 11 results:

    {1;1;1;1;2;2;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!}
    

In this array, numbers indicate the position of "a" in cells where "a" is found. The #VALUE! errors indicate cells where "a" was not found. To convert these results into a simple array of TRUE and FALSE values, we use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
:

    ISNUMBER(SEARCH("a",data))
    

ISNUMBER returns TRUE for any number and FALSE for errors. SEARCH delivers the array of results to ISNUMBER, and ISNUMBER converts the results to an array that contains only TRUE and FALSE values:

    {TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

In this array, TRUE corresponds to cells that contain "a" and FALSE corresponds to cells that do not contain "a". This is exactly the _opposite_ of what we need, so we use the  [NOT function](https://exceljet.net/functions/not-function)
 to reverse the array:

    NOT(ISNUMBER(SEARCH("a",data)))
    

The result from the  NOT function is:

    {FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE}
    

In this array, the TRUE values represent cells we want to count. However, we first need to convert the TRUE and FALSE values to their numeric equivalents, 1 and 0. To do this, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--):

    --NOT(ISNUMBER(SEARCH("a",data)))
    

The result inside of SUMPRODUCT looks like this:

    =SUMPRODUCT({0;0;0;0;0;0;1;1;1;1;1}) // returns 5
    

With a single array to process, SUMPRODUCT sums the array and returns 5 as a final result.

One benefit of this formula is it will find a number inside a numeric value. In addition, there is no need to use wildcards to indicate position, because SEARCH will automatically look through all text in a cell.

### Case-sensitive option

For a case-sensitive count, you can replace the SEARCH function with the [FIND function](https://exceljet.net/functions/find-function)
 like this:

    =SUMPRODUCT(--NOT(ISNUMBER(FIND("A",data))))
    

The FIND function works just like the SEARCH function, but is case-sensitive. Notice we have replaced "a" with "A" because FIND _is_ case-sensitive. If we used "a", the result would be 11 since there are no cells in B5:B15 that contain a lowercase "a". [This example provides more detail](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)
.

_Note: the SUMPRODUCT formulas above are more complex, but using_ [_Boolean operations in array formulas_](https://exceljet.net/videos/boolean-operations-in-array-formulas)
 _is a more powerful and flexible approach. It is also an important skill in modern functions like_ [_FILTER_](https://exceljet.net/functions/filter-function)
 _and_ [_XLOOKUP_](https://exceljet.net/functions/xlookup-function)
_, which often use this technique to select the right data. The syntax used by COUNTIF is unique to_ [_a group of eight functions_](https://exceljet.net/articles/excels-racon-functions)
 _and is therefore not as useful or portable._

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

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