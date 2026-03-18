# Excel EXACT function | Exceljet

**Source:** https://exceljet.net/functions/exact-function

---

[Skip to main content](https://exceljet.net/functions/exact-function#main-content)

[](https://exceljet.net/functions/exact-function#)

*   [Previous](https://exceljet.net/functions/dollar-function)
    
*   [Next](https://exceljet.net/functions/find-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

EXACT Function
==============

by Dave Bruns · Updated 23 Jun 2021

![Excel EXACT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")

Summary
-------

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

Purpose 
--------

Compare two text strings

Return value 
-------------

A boolean value (TRUE or FALSE)

Syntax
------

    =EXACT(text1,text2)

*   _text1_ - The first text string to compare.
*   _text2_ - The second text string to compare.

Using the EXACT function 
-------------------------

The EXACT function compares two text strings in a case-sensitive manner. If the two strings are exactly the same, EXACT returns TRUE. If the two strings are not the same (taking into account upper and lower case) EXACT returns FALSE.

The EXACT function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _text1_ and _text2_, which should be valid [text strings](https://exceljet.net/glossary/text-value)
. If these values are entered directly into the function, they should be enclosed in double quotes ("").

### Examples

Below are two examples of the EXACT function used with hardcoded strings. In the first example, the strings are identical, in the second example, the only difference is the capital "A":

    =EXACT("apple","apple") // returns TRUE
    =EXACT("Apple","apple") // returns FALSE
    

In the example shown, the formula in D6, copied down the column, is:

    =EXACT(B6,C6)
    

You can also use a normal equals sign (=) in a formula, but the comparison is not case sensitive:

    =("Apple"="apple") // returns TRUE
    

To count cells that contain specific text, taking into account upper and lower case characters, you can combine EXACT together with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 like this:

    =SUMPRODUCT(--EXACT(value,range))
    

[Detailed explanation here](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
.

### Notes

*   The standard equals to (=) [operator](https://exceljet.net/glossary/math-operators)
     is not case-sensitive.
*   EXACT is meant for text values, and will convert numeric values to text.

EXACT function examples
-----------------------

[![Excel formula: Highlight cells that equal](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20equal.png "Excel formula: Highlight cells that equal")](https://exceljet.net/formulas/highlight-cells-that-equal)

### [Highlight cells that equal](https://exceljet.net/formulas/highlight-cells-that-equal)

Note: Excel contains many built-in "presets" for highlighting values with conditional formatting, including a preset to highlight cells that equal a specific value. However, for more flexibility, you can use your own formula, as explained in this article. If you want to highlight cells that equal a...

[![Excel formula: Sum if case-sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_case_sensitive.png "Excel formula: Sum if case-sensitive")](https://exceljet.net/formulas/sum-if-case-sensitive)

### [Sum if case-sensitive](https://exceljet.net/formulas/sum-if-case-sensitive)

In this example, the goal is to sum the quantities in column C by the codes in column E in a case-sensitive manner. The SUMIF function and the SUMIFS function are both good options for counting text values, and both functions support wildcards . However, neither function is case-sensitive, so they...

[![Excel formula: Cell begins with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_begins_with.png "Excel formula: Cell begins with")](https://exceljet.net/formulas/cell-begins-with)

### [Cell begins with](https://exceljet.net/formulas/cell-begins-with)

In this example, the goal is to test values in column B to see if they begin with a specific text string, which is "xyz" in the worksheet shown. This problem can be solved with the LEFT function, as explained below. LEFT function The LEFT function extracts a given number of characters from the left...

[![Excel formula: Multiple cells have same value case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Multiple%20cells%20have%20same%20value%20case%20sensitive.png "Excel formula: Multiple cells have same value case sensitive")](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)

### [Multiple cells have same value case sensitive](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)

This formula uses the EXACT formula to compare a range of cells to a single value: =EXACT(B5:F5,B5) Because we give EXACT a range of values in the first argument, we get back an array result containing TRUE FALSE values: {TRUE,FALSE,TRUE,TRUE,TRUE} This array goes into the AND function, which...

[![Excel formula: SUMPRODUCT case-sensitive lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT_case_sensitive_lookup.png "Excel formula: SUMPRODUCT case-sensitive lookup")](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)

### [SUMPRODUCT case-sensitive lookup](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)

The SUMPRODUCT function multiplies arrays together and returns the sum of products. If only one array is supplied, SUMPRODUCT will simply sum the items in the array. For example, if we give SUMPRODUCT one array in the form of the data\[Qty\] column: =SUMPRODUCT(data\[Qty\]) // returns 54 SUMPRODUCT...

[![Excel formula: Highlight column differences](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20column%20differences.png "Excel formula: Highlight column differences")](https://exceljet.net/formulas/highlight-column-differences)

### [Highlight column differences](https://exceljet.net/formulas/highlight-column-differences)

In this example, the goal is to highlight differences in two ranges, B2:B11 and C2:C11, using conditional formatting. To do this, we need to create a new conditional formatting rule, triggered by a formula, like this: Select the range B2:C11, starting at cell B2. Select Home > Conditional...

[![Excel formula: Unique values case-sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique_values_case_sensitive.png "Excel formula: Unique values case-sensitive")](https://exceljet.net/formulas/unique-values-case-sensitive)

### [Unique values case-sensitive](https://exceljet.net/formulas/unique-values-case-sensitive)

In this example, the goal is to create a formula that will extract unique values from a range of data in a case-sensitive way. Normally, we would use the UNIQUE function to extract unique values. However, UNIQUE is not case-sensitive so it won't work in this situation. One way to solve this problem...

[![Excel formula: Compare two strings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/compare%20two%20strings.png "Excel formula: Compare two strings")](https://exceljet.net/formulas/compare-two-strings)

### [Compare two strings](https://exceljet.net/formulas/compare-two-strings)

By default, Excel is not case-sensitive. For example, with "APPLE" in A1, and "apple" in A2, the following formula will return TRUE: =A1=A2 // returns TRUE To compare text strings in a case-sensitive way, you can use the EXACT function . The Excel EXACT function compares two text strings, taking...

[![Excel formula: Count cells that begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20begin%20with.png "Excel formula: Count cells that begin with")](https://exceljet.net/formulas/count-cells-that-begin-with)

### [Count cells that begin with](https://exceljet.net/formulas/count-cells-that-begin-with)

In this example, the goal is to count cells in the range B5:B16 that begin with specific text, which is provided in column D. For convenience, the range B5:B16 is named data . COUNTIF function The simplest way to solve this problem is with the COUNTIF function and a wildcard. COUNTIF supports three...

[![Excel formula: XLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20case%20sensitive.png "Excel formula: XLOOKUP case-sensitive ")](https://exceljet.net/formulas/xlookup-case-sensitive)

### [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the color in the "Color" column. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP...

[![Excel formula: Data validation must begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20must%20begin%20with.png "Excel formula: Data validation must begin with")](https://exceljet.net/formulas/data-validation-must-begin-with)

### [Data validation must begin with](https://exceljet.net/formulas/data-validation-must-begin-with)

Data validation rules are triggered when a user adds or changes a cell value. In this formula, the LEFT function is used to extract the first 3 characters of the input in C5. Next, the EXACT function is used to compare the extracted text to the text hard-coded into the formula, "MX-". EXACT...

[![Excel formula: Highlight cells that end with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20end%20with.png "Excel formula: Highlight cells that end with")](https://exceljet.net/formulas/highlight-cells-that-end-with)

### [Highlight cells that end with](https://exceljet.net/formulas/highlight-cells-that-end-with)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each cell in B4:G12, and the reference to B4 will change to the address of each cell being evaluated...

[![Excel formula: Match long text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/match%20long%20text.png "Excel formula: Match long text")](https://exceljet.net/formulas/match-long-text)

### [Match long text](https://exceljet.net/formulas/match-long-text)

The MATCH function has a limit of 255 characters for the lookup value. If you try to use longer text, MATCH will return a #VALUE error. To workaround this limit you can use boolean logic and the LEFT, MID, and EXACT functions to parse and compare text. Note: this formula performs an exact match...

[![Excel formula: Case sensitive lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case%20sensitive%20lookup.png "Excel formula: Case sensitive lookup")](https://exceljet.net/formulas/case-sensitive-lookup)

### [Case sensitive lookup](https://exceljet.net/formulas/case-sensitive-lookup)

In this example, the goal is to perform a case-sensitive lookup on the name in column B, based on a lookup value entered in cell E5. By default, Excel is not case-sensitive. This means that standard lookup functions like VLOOKUP , XLOOKUP , and INDEX and MATCH are also not case-sensitive. These...

[![Excel formula: Multiple cells are equal](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple%20cells%20are%20equal.png "Excel formula: Multiple cells are equal")](https://exceljet.net/formulas/multiple-cells-are-equal)

### [Multiple cells are equal](https://exceljet.net/formulas/multiple-cells-are-equal)

The AND function is designed to evaluate multiple logical expressions, and returns TRUE only when all expressions are TRUE. In this case the we simply compare one range with another with a single logical expression: B5:D12=F5:H12 The two ranges, B5:B12 and F5:H12 are the same dimensions, 5 rows x 3...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that begin with](https://exceljet.net/formulas/count-cells-that-begin-with)
    
*   [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)
    
*   [Case sensitive lookup](https://exceljet.net/formulas/case-sensitive-lookup)
    
*   [Highlight cells that equal](https://exceljet.net/formulas/highlight-cells-that-equal)
    
*   [Multiple cells are equal](https://exceljet.net/formulas/multiple-cells-are-equal)
    
*   [Data validation allow uppercase only](https://exceljet.net/formulas/data-validation-allow-uppercase-only)
    
*   [Sum if case-sensitive](https://exceljet.net/formulas/sum-if-case-sensitive)
    
*   [Cell begins with](https://exceljet.net/formulas/cell-begins-with)
    
*   [Highlight cells that end with](https://exceljet.net/formulas/highlight-cells-that-end-with)
    
*   [VLOOKUP case-sensitive](https://exceljet.net/formulas/vlookup-case-sensitive)
    

### Links

*   [Microsoft EXACT function documentation](https://support.office.com/en-us/article/exact-function-d3087698-fc15-4a15-9631-12575cf29926)
    

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