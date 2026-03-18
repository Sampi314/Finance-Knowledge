# List most frequently occurring numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/list-most-frequently-occurring-numbers

---

[Skip to main content](https://exceljet.net/formulas/list-most-frequently-occurring-numbers#main-content)

[](https://exceljet.net/formulas/list-most-frequently-occurring-numbers#)

*   [Previous](https://exceljet.net/formulas/link-to-multiple-sheets)
    
*   [Next](https://exceljet.net/formulas/longest-winning-streak)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

List most frequently occurring numbers
======================================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[MODE](https://exceljet.net/functions/mode-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: List most frequently occurring numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/list%20most%20frequently%20occuring%20numbers.png "Excel formula: List most frequently occurring numbers")

Summary
-------

To list the most frequently occurring numbers in a column (i.e. most common, second most common, third most common, etc), you can an array formula based on four Excel functions: [IF](https://exceljet.net/functions/if-function)
, [MODE](https://exceljet.net/functions/mode-function)
, [MATCH](https://exceljet.net/functions/match-function)
, and [ISNUMBER](https://exceljet.net/functions/isnumber-function)
. In the example shown, the formula in D5 is:

    {=MODE(IF(1-ISNUMBER(MATCH(data,$D$4:D4,0)),data))}
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16. The formula is then copied to rows below D5 to output the desired list of most frequent numbers.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

Generic formula
---------------

    {=MODE(IF(1-ISNUMBER(MATCH(data,exp_rng,0)),data))}

Explanation 
------------

The core of this formula is the MODE function, which returns the most frequently occurring number in a range or array. The rest of the formula just constructs a filtered array for MODE to use in each row. The [expanding range](https://exceljet.net/glossary/expanding-reference)
 $D$4:D4 works to exclude numbers already output in $D$4:D4.

Working from the inside out:

1.  The MATCH checks all numbers in the named range "data" against existing numbers in the [expanding range](https://exceljet.net/glossary/expanding-reference)
     $D$4:D4
2.  ISNUMBER converts matched values to TRUE and non-matched values to FALSE
3.  1-NUMBER reverses the array, and the math operation outputs ones and zeros
4.  IF uses the array output of #3 above to filter the original list of values, excluding numbers already in $D$4:D4
5.  The MODE function returns the most frequent number in the array output in step #4

In cell D5, no filtering occurs and the output of each step above looks like this:

    {#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A}
    {FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    {1;1;1;1;1;1;1;1;1;1;1;1}
    {93;92;93;94;95;96;97;98;99;93;97;95}
    93
    

In cell D6, with 93 already in D5, the output looks like this:

    {2;#N/A;2;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;2;#N/A;#N/A}
    {TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE}
    {0;1;0;1;1;1;1;1;1;0;1;1}
    {FALSE;92;FALSE;94;95;96;97;98;99;FALSE;97;95}
    95
    

### Handling errors

The MODE function will return the #N/A error when there is no mode. As you copy the formula down into subsequent rows, you will likely run into the #N/A error. To trap this error and return an [empty string](https://exceljet.net/glossary/empty-string)
 ("") instead, you can use IFERROR like this:

    =IFERROR(MODE(IF(1-ISNUMBER(MATCH(data,$D$4:D4,0)),data)),"")
    

Related formulas
----------------

[![Excel formula: Most frequently occurring text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequent%20text2.png "Excel formula: Most frequently occurring text")](https://exceljet.net/formulas/most-frequently-occurring-text)

### [Most frequently occurring text](https://exceljet.net/formulas/most-frequently-occurring-text)

Working from the inside out, the MATCH function matches the range against itself. That is, we give the MATCH function the same range for lookup value and lookup array (B5:F5). Because the lookup value contains more than one value (an array), MATCH returns an array of results, where each number...

[![Excel formula: Most frequently occurring number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequently%20occurring%20number.png "Excel formula: Most frequently occurring number")](https://exceljet.net/formulas/most-frequently-occurring-number)

### [Most frequently occurring number](https://exceljet.net/formulas/most-frequently-occurring-number)

The MODE function is fully automatic and will return the most frequently occurring number in a set of numbers. For example: =MODE(1,2,4,4,5,5,5,6) // returns 5 In the example shown, we give MODE the range B4:K4, so the formula is solved like this: =MODE(B4:K4) =MODE({1,2,2,1,1,2,2,2,1,1}) =2

[![Excel formula: Filter values in array formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20values%20in%20array%20formula.png "Excel formula: Filter values in array formula")](https://exceljet.net/formulas/filter-values-in-array-formula)

### [Filter values in array formula](https://exceljet.net/formulas/filter-values-in-array-formula)

In this example, the goal is to filter the values in one array by the values in another array. For convenience, data (B4:D11) and filter (F4:F6) are named ranges . The solution is based on the MATCH function with the ISNUMBER function . This is a pattern you will see often in more advanced formulas...

Related functions
-----------------

[![Excel MODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mode%20function.png "Excel MODE function")](https://exceljet.net/functions/mode-function)

### [MODE Function](https://exceljet.net/functions/mode-function)

The Excel MODE function returns the most frequently occurring number in a numeric data set. For example, =MODE(1,2,4,4,5,5,5,6) returns 5.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Most frequently occurring text](https://exceljet.net/formulas/most-frequently-occurring-text)
    
*   [Most frequently occurring number](https://exceljet.net/formulas/most-frequently-occurring-number)
    
*   [Filter values in array formula](https://exceljet.net/formulas/filter-values-in-array-formula)
    

### Functions

*   [MODE Function](https://exceljet.net/functions/mode-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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