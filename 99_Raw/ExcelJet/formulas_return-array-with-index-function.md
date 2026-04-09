# Return array with INDEX function - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/return-array-with-index-function

---

[Skip to main content](https://exceljet.net/formulas/return-array-with-index-function#main-content)

[](https://exceljet.net/formulas/return-array-with-index-function#)

*   [Previous](https://exceljet.net/formulas/repeat-sequence-of-numbers)
    
*   [Next](https://exceljet.net/formulas/reverse-a-list-or-range)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Return array with INDEX function
================================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[N](https://exceljet.net/functions/n-function)

![Excel formula: Return array with INDEX function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/return%20array%20with%20INDEX%20function.png "Excel formula: Return array with INDEX function")

Summary
-------

To get [INDEX](https://exceljet.net/functions/index-function)
 to return an array of items to another function, you can use an obscure trick based on the [IF](https://exceljet.net/functions/if-function)
 and [N](https://exceljet.net/functions/n-function)
 functions. In the example shown, the formula in E5 is:

    =SUM(INDEX(data,N(IF(1,{1,2,3}))))
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B10.

> In Excel 2021 and later, this trick is _not necessary_, thanks to [dynamic arrays](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
> . See the [TAKE function](https://exceljet.net/functions/take-function)
> .

Generic formula
---------------

    =SUM(INDEX(range,N(IF(1,{1,2,3}))))

Explanation 
------------

It is surprisingly tricky to get INDEX to return more than one value to another function. To illustrate, the following formula can be used to return the first three items in the named range "data", when entered as a multi-cell array formula.

    {=INDEX(data,{1,2,3})}
    

The results can be seen in the range D10:F10, which correctly contains 10, 15, and 20. However, if we wrap the formula in the [SUM function](https://exceljet.net/functions/sum-function)
:

    =SUM(INDEX(data,{1,2,3}))
    

The final result is 10, while it should be 45, even if entered as an array formula. The problem is that INDEX only returns the first item in the array to the SUM function. To force INDEX to return multiple items to SUM, you can wrap the array constant in the N and IF functions like this:

    =SUM(INDEX(data,N(IF(1,{1,2,3}))))
    

which returns a correct result of 45. Similarly, this formula:

    =SUM(INDEX(data,N(IF(1,{1,3,5}))))
    

correctly returns 60, the sum of 10, 20, and 30.

This obscure technique is sometimes called "dereferencing", because it stops INDEX from handling results as cell references, and subsequently dropping all but the first item in the array. Instead, INDEX delivers a full array of values to SUM. Jeff Weir has a [good explanation here on stackoverflow](https://stackoverflow.com/a/47189998/4071990)
.

Related formulas
----------------

[![Excel formula: Sum text values like numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20text%20values%20like%20numbers.png "Excel formula: Sum text values like numbers")](https://exceljet.net/formulas/sum-text-values-like-numbers)

### [Sum text values like numbers](https://exceljet.net/formulas/sum-text-values-like-numbers)

The heart of this formula is a basic INDEX and MATCH formula, used to translate text values into numbers as defined in a lookup table. For example, to translate "EX" to the corresponding number, we would use: =INDEX(value,MATCH("EX",code,0)) which would return 4. The twist in this problem however...

[![Excel formula: Lookup and sum column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Lookup%20and%20sum%20column.png "Excel formula: Lookup and sum column")](https://exceljet.net/formulas/lookup-and-sum-column)

### [Lookup and sum column](https://exceljet.net/formulas/lookup-and-sum-column)

The core of this formula uses the INDEX and MATCH function in a special way to return a full column instead of a single value. Working from the inside out, the MATCH function is used to find the correct column number for the fruit in I6: MATCH(I6,C4:F4,0) MATCH return 2 inside the INDEX function as...

[![Excel formula: Sum range with INDEX](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sum%20range%20with%20INDEX.png "Excel formula: Sum range with INDEX")](https://exceljet.net/formulas/sum-range-with-index)

### [Sum range with INDEX](https://exceljet.net/formulas/sum-range-with-index)

The INDEX function looks up values by position. For example, this formula retrieves the value for Acme sales in Jan: =INDEX(data,1,1) The INDEX function has a special and non-obvious behavior: when the row number argument is supplied as zero or null, INDEX retrieves all values in the column...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel N function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20n%20function.png "Excel N function")](https://exceljet.net/functions/n-function)

### [N Function](https://exceljet.net/functions/n-function)

The Excel N function returns a number when given a value. The N function can be used to convert TRUE and FALSE to 1 and 0 respectively. When given a text value, the N function returns zero.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum text values like numbers](https://exceljet.net/formulas/sum-text-values-like-numbers)
    
*   [Lookup and sum column](https://exceljet.net/formulas/lookup-and-sum-column)
    
*   [Sum range with INDEX](https://exceljet.net/formulas/sum-range-with-index)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [N Function](https://exceljet.net/functions/n-function)
    

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