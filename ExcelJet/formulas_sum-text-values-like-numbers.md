# Sum text values like numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-text-values-like-numbers

---

[Skip to main content](https://exceljet.net/formulas/sum-text-values-like-numbers#main-content)

[](https://exceljet.net/formulas/sum-text-values-like-numbers#)

*   [Previous](https://exceljet.net/formulas/sum-roman-numbers)
    
*   [Next](https://exceljet.net/formulas/text-is-greater-than-number)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Sum text values like numbers
============================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[N](https://exceljet.net/functions/n-function)

![Excel formula: Sum text values like numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20text%20values%20like%20numbers.png "Excel formula: Sum text values like numbers")

Summary
-------

To translate text values into numbers and sum the result, you can use an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
, and the [SUM function](https://exceljet.net/functions/sum-function)
. In the example shown, the formula in H5 is:

    {=SUM(INDEX(value,N(IF(1,MATCH(C5:G5,code,0)))))}
    

where "code" is the [named range](https://exceljet.net/glossary/named-range)
 K5:K9, and "value" is the named range L5:L9.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
, and must be entered with control + shift + enter._

Explanation 
------------

The heart of this formula is a basic INDEX and MATCH formula, used to translate text values into numbers as defined in a lookup table. For example, to translate "EX" to the corresponding number, we would use:

    =INDEX(value,MATCH("EX",code,0))
    

which would return 4.

The twist in this problem however is that we want to translate and sum a _range of text values_ in columns C through G to numbers. This means we need to provide more than one lookup value, and we need INDEX to return more than one result. The standard approach is a formula like this:

    =SUM(INDEX(value,MATCH(C5:G5,code,0)))
    

After MATCH runs, we have an array with 5 items:

    =SUM(INDEX(value,{2,2,3,2,5}))
    

So it seems INDEX should return 5 results to SUM. However, if you try this, the INDEX function will return only one result SUM. To get INDEX to return multiple results, we need to use a rather [obscure trick](https://exceljet.net/formulas/return-array-with-index-function)
, and wrap MATCH in N and IF like this:

    N(IF(1,MATCH(C5:G5,code,0)))
    

This effectively forces INDEX to provide more than one value to the SUM function. After INDEX runs, we have:

    =SUM({3,3,2,3,-1})
    

And the SUM function returns the sum of items in the array, 10. For a good write up on this behavior, see [this article by Jeff Weir](https://stackoverflow.com/questions/47187863/can-excels-index-function-return-array/47189998#47189998)
 on the StackOverflow site.

Related formulas
----------------

[![Excel formula: Map inputs to arbitrary values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20inputs%20to%20arbitrary%20values.png "Excel formula: Map inputs to arbitrary values")](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)

### [Map inputs to arbitrary values](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)

In this example, the goal is to map the numbers 1-6 to the arbitrary values seen in the table below. For example: If the input is 1, the output should be 10 If the input is 2, the output should be 81 If the input is 3, the output should be 17 If the input is 4, the output should be 23 And so on.....

[![Excel formula: Map text to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20text%20to%20numbers.png "Excel formula: Map text to numbers")](https://exceljet.net/formulas/map-text-to-numbers)

### [Map text to numbers](https://exceljet.net/formulas/map-text-to-numbers)

This formula uses the value in cell F7 for a lookup value, the range B6:C10 for the lookup table, the number 2 to indicate "2nd column", and zero as the last argument to force an exact match. Although in this case we are mapping text values to numeric outputs, the same formula can handle text to...

[![Excel formula: Return array with INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/return%20array%20with%20INDEX%20function.png "Excel formula: Return array with INDEX function")](https://exceljet.net/formulas/return-array-with-index-function)

### [Return array with INDEX function](https://exceljet.net/formulas/return-array-with-index-function)

It is surprisingly tricky to get INDEX to return more than one value to another function. To illustrate, the following formula can be used to return the first three items in the named range "data", when entered as a multi-cell array formula. {=INDEX(data,{1,2,3})} The results can be seen in the...

[![Excel formula: Translate letters to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/translate%20letters%20to%20numbers.png "Excel formula: Translate letters to numbers")](https://exceljet.net/formulas/translate-letters-to-numbers)

### [Translate letters to numbers](https://exceljet.net/formulas/translate-letters-to-numbers)

At the core, this formula uses an array operation to generate an array of letters from the input text, translates each letter individually to a number, then joins all numbers together again and returns the output as a string. To parse the input string into an array or letters, we use MID, ROW, LEN...

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

*   [Map inputs to arbitrary values](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)
    
*   [Map text to numbers](https://exceljet.net/formulas/map-text-to-numbers)
    
*   [Return array with INDEX function](https://exceljet.net/formulas/return-array-with-index-function)
    
*   [Translate letters to numbers](https://exceljet.net/formulas/translate-letters-to-numbers)
    

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