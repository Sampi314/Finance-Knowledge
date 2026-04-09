# Multiple matches in comma separated list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/multiple-matches-in-comma-separated-list

---

[Skip to main content](https://exceljet.net/formulas/multiple-matches-in-comma-separated-list#main-content)

[](https://exceljet.net/formulas/multiple-matches-in-comma-separated-list#)

*   [Previous](https://exceljet.net/formulas/multiple-chained-vlookups)
    
*   [Next](https://exceljet.net/formulas/multiple-matches-into-separate-columns)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Multiple matches in comma separated list
========================================

by Dave Bruns · Updated 21 May 2021

Related functions 
------------------

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

![Excel formula: Multiple matches in comma separated list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/multiple%20matches%20in%20comma%20separated%20result2.png "Excel formula: Multiple matches in comma separated list")

Summary
-------

To lookup and retrieve multiple matches in a comma separated list (in a single cell) you can use the IF function with the TEXTJOIN function. In the example shown, the formula in F5 is:

    {=TEXTJOIN(", ",TRUE,IF(group=E5,name,""))}
    

_This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

This formula uses the [named ranges](https://exceljet.net/glossary/named-range)
 "name" (B5:B11) and "group" (C5:C11).

> TEXTJOIN is available in [Excel 365](https://exceljet.net/glossary/excel-365)
>  and Excel 2019.

Generic formula
---------------

    {=TEXTJOIN(", ",TRUE,IF(rng1=E5,rng2,""))}

Explanation 
------------

The core of this formula is the IF function, which "filters" the names in the table by color like this:

    IF(group=E5,name,""))
    

The logical test checks each cell in the named range "group" for the color value in E5 (red in this case). The result is an array like this:

    {FALSE;FALSE;TRUE;TRUE;FALSE;FALSE;TRUE}
    

That result is used in turn to filter names from the named range "name":

    {"Matt";"Sally";"Jude";"Aya";"Elle";"Linda";"George"}
    

For each TRUE, the name survives, for each FALSE, IF returns an [empty string](https://exceljet.net/glossary/empty-string)
 ("").

The result of IF looks is this array:

    {"";"";"Jude";"Aya";"";"";"George"}
    

which goes into the TEXTJOIN function as text1.

TEXTJOIN is configured to use a comma as the delimiter, and to ignore empty values. The final result is this text string:

"Jude, Aya, George"

### Line break instead of comma

To join matches with a line break instead of a comma, you can adjust the formula like this:

    =TEXTJOIN(CHAR(10),TRUE,IF(group=E5,name,""))
    

The [CHAR function](https://exceljet.net/functions/char-function)
 returns the code used for a line break. You will also need to [enable text wrapping](https://exceljet.net/videos/how-to-wrap-text-in-cells-in-excel)
.

### Multiple conditions

You can't use the AND or OR functions in an array formula like this because they only return a single result. You can use boolean logic like this for AND:

    =TEXTJOIN(", ",TRUE,IF((condition1)*(condition2),name,""))
    

[Explained in more detail here](https://exceljet.net/formulas/if-with-boolean-logic)
.

Related formulas
----------------

[![Excel formula: Join cells with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join%20cells%20with%20comma_0.png "Excel formula: Join cells with comma")](https://exceljet.net/formulas/join-cells-with-comma)

### [Join cells with comma](https://exceljet.net/formulas/join-cells-with-comma)

Working from the inside out, the formula first joins the values the 5 cells to the left using the concatenation operator (...

[![Excel formula: List holidays between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20holidays%20between%20two%20dates.png "Excel formula: List holidays between two dates")](https://exceljet.net/formulas/list-holidays-between-two-dates)

### [List holidays between two dates](https://exceljet.net/formulas/list-holidays-between-two-dates)

At a high level, this formula uses a nested IF function to return an array of holidays between two dates. This array is then processed by the TEXTJOIN function, which converts the array to text using a comma as the delimiter. Working from the inside out, we generate the array of matching holidays...

Related functions
-----------------

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Join cells with comma](https://exceljet.net/formulas/join-cells-with-comma)
    
*   [List holidays between two dates](https://exceljet.net/formulas/list-holidays-between-two-dates)
    

### Functions

*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    

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