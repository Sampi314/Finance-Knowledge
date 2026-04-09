# Partial match with numbers and wildcard - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/partial-match-with-numbers-and-wildcard

---

[Skip to main content](https://exceljet.net/formulas/partial-match-with-numbers-and-wildcard#main-content)

[](https://exceljet.net/formulas/partial-match-with-numbers-and-wildcard#)

*   [Previous](https://exceljet.net/formulas/next-largest-match-with-the-match-function)
    
*   [Next](https://exceljet.net/formulas/partial-match-with-vlookup)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Partial match with numbers and wildcard
=======================================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[MATCH](https://exceljet.net/functions/match-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Partial match with numbers and wildcard](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/partial%20match%20with%20numbers%20and%20wildcard.png "Excel formula: Partial match with numbers and wildcard")

Summary
-------

To perform a partial (wildcard) match against numbers, you can use an array formula based on the [MATCH function](https://exceljet.net/functions/match-function)
 and the [TEXT function](https://exceljet.net/functions/text-function)
. In the example shown, the formula in E6 is:

    =MATCH("*"&E5&"*",TEXT(data,"0"),0)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15. The result is 7 since the number in B11 (the seventh row in **data**) contains 99.

_This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Generic formula
---------------

    {=MATCH("*"&number&"*",TEXT(range,"0"),0)}

Explanation 
------------

Excel supports the [wildcard](https://exceljet.net/glossary/wildcard)
 characters "\*" and "?", and these wildcards can be used to perform partial (substring) matches in various lookup formulas. However, if you use wildcards with a number, you'll convert the numeric value to a text value. In other words, "\*"&99&"\*" = "\*99\*" (a text string), and if you try to find a text value in a range of numbers, the match will fail.

One solution is to convert the numeric values to text with the [TEXT function](https://exceljet.net/functions/text-function)
 like this:

    =MATCH("*"&E5&"*",TEXT(data,"0"),0)
    

_This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

This formula uses the TEXT function to transform the numbers in B5:B10 to text with the [number format](https://exceljet.net/articles/custom-number-formats)
 "0". Because we give the entire range to TEXT, we get back all values converted to text in an [array](https://exceljet.net/glossary/array)
, which is returned directly to the MATCH function as the _array_ argument. With the numbers converted to text, the MATCH function can find a partial match as usual.

Note that MATCH must be configured for exact match to use wildcards, by setting the 3rd argument to zero (0) or FALSE.

### Another option

Another way to transform a number to text is to [concatenate](https://exceljet.net/glossary/concatenation)
 the numbers to an [empty string](https://exceljet.net/glossary/empty-string)
 ("") with the ampersand (&) [operator](https://exceljet.net/glossary/math-operators)
 like this:

    =MATCH("*"&E5&"*",data&"",0)
    

The numbers in **data** become text without formatting, and the result is the same as above, 7.

Related formulas
----------------

[![Excel formula: INDEX and MATCH case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case-sensitive%20INDEX%20and%20MATCH.png "Excel formula: INDEX and MATCH case-sensitive ")](https://exceljet.net/formulas/index-and-match-case-sensitive)

### [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the first name in column B, based on a lookup value in cell F6. By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP , XLOOKUP , and INDEX and MATCH . These formulas will simply return...

[![Excel formula: Position of first partial match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/position%20of%20first%20partial%20match.png "Excel formula: Position of first partial match")](https://exceljet.net/formulas/position-of-first-partial-match)

### [Position of first partial match](https://exceljet.net/formulas/position-of-first-partial-match)

The MATCH function returns the position or "index" of the first match based on a lookup value in a range. MATCH supports wildcard matching with an asterisk "\*" (one or more characters) or a question mark "?" (one character), but only when t he third argument, match\_type, is set to FALSE or zero. In...

[![Excel formula: Partial match with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Partial%20match%20with%20VLOOKUP.png "Excel formula: Partial match with VLOOKUP")](https://exceljet.net/formulas/partial-match-with-vlookup)

### [Partial match with VLOOKUP](https://exceljet.net/formulas/partial-match-with-vlookup)

In this example, the goal is to retrieve employee information from a table using only a partial match on the last name. In other words, by typing "Aya" into cell H4, the formula should retrieve information about Michael Ayala. The VLOOKUP function supports wildcards , which makes it possible to...

Related functions
-----------------

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)
    
*   [Position of first partial match](https://exceljet.net/formulas/position-of-first-partial-match)
    
*   [Partial match with VLOOKUP](https://exceljet.net/formulas/partial-match-with-vlookup)
    

### Functions

*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

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