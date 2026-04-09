# Position of first partial match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/position-of-first-partial-match

---

[Skip to main content](https://exceljet.net/formulas/position-of-first-partial-match#main-content)

[](https://exceljet.net/formulas/position-of-first-partial-match#)

*   [Previous](https://exceljet.net/formulas/partial-match-with-vlookup)
    
*   [Next](https://exceljet.net/formulas/position-of-max-value-in-list)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Position of first partial match
===============================

by Dave Bruns · Updated 13 Jun 2018

Related functions 
------------------

[MATCH](https://exceljet.net/functions/match-function)

[INDEX](https://exceljet.net/functions/index-function)

![Excel formula: Position of first partial match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/position%20of%20first%20partial%20match.png "Excel formula: Position of first partial match")

Summary
-------

To get the position of the first partial match (i.e. the cell that _contains_ text you are looking for) you can use the MATCH function with wildcards.

In the example shown, the formula in E8 is:

    =MATCH("*"&E7&"*",B6:B11,0)
    

Generic formula
---------------

    =MATCH("*text*",rng,0)

Explanation 
------------

The MATCH function returns the position or "index" of the first match based on a lookup value in a range.

MATCH supports wildcard matching with an asterisk "\*" (one or more characters) or a question mark "?" (one character), but only when the third argument, match\_type, is set to FALSE or zero.

In the example, we pick up the value in cell E7 and use concatenation to combine this value with asterisks (\*) on either side. The lookup array is the range B6 to B11, and match\_type is set to zero to all partial matching with wildcards.

The result is the position of the first cell in the lookup range that contains the text "apple".

To retrieve the _value_ of a cell at a certain position, use the [INDEX function](https://exceljet.net/functions/index-function)
.

Related formulas
----------------

[![Excel formula: Partial match with numbers and wildcard](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/partial%20match%20with%20numbers%20and%20wildcard.png "Excel formula: Partial match with numbers and wildcard")](https://exceljet.net/formulas/partial-match-with-numbers-and-wildcard)

### [Partial match with numbers and wildcard](https://exceljet.net/formulas/partial-match-with-numbers-and-wildcard)

Excel supports the wildcard characters "\*" and "?", and these wildcards can be used to perform partial (substring) matches in various lookup formulas. However, if you use wildcards with a number, you'll convert the numeric value to a text value. In other words, "\*"&99&"\*" = "\*99\*" (a text...

[![Excel formula: Partial match with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Partial%20match%20with%20VLOOKUP.png "Excel formula: Partial match with VLOOKUP")](https://exceljet.net/formulas/partial-match-with-vlookup)

### [Partial match with VLOOKUP](https://exceljet.net/formulas/partial-match-with-vlookup)

In this example, the goal is to retrieve employee information from a table using only a partial match on the last name. In other words, by typing "Aya" into cell H4, the formula should retrieve information about Michael Ayala. The VLOOKUP function supports wildcards , which makes it possible to...

Related functions
-----------------

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Partial match with numbers and wildcard](https://exceljet.net/formulas/partial-match-with-numbers-and-wildcard)
    
*   [Partial match with VLOOKUP](https://exceljet.net/formulas/partial-match-with-vlookup)
    

### Functions

*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

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