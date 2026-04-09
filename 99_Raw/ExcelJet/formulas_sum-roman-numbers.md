# Sum Roman numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-roman-numbers

---

[Skip to main content](https://exceljet.net/formulas/sum-roman-numbers#main-content)

[](https://exceljet.net/formulas/sum-roman-numbers#)

*   [Previous](https://exceljet.net/formulas/sum-every-3-cells)
    
*   [Next](https://exceljet.net/formulas/sum-text-values-like-numbers)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Sum Roman numbers
=================

by Dave Bruns · Updated 11 Jan 2023

Related functions 
------------------

[ARABIC](https://exceljet.net/functions/arabic-function)

[ROMAN](https://exceljet.net/functions/roman-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[SUM](https://exceljet.net/functions/sum-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6774/download?token=IABT2Aro)
 (14.49 KB)

![Excel formula: Sum Roman numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20roman%20numbers.png "Excel formula: Sum Roman numbers")

Summary
-------

To sum a range of [Roman numbers](https://en.wikipedia.org/wiki/Roman_numerals)
, you can use a formula based on the [ARABIC](https://exceljet.net/functions/arabic-function)
 and [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 functions. In the example shown, the formula in E5 is:

    =SUMPRODUCT(ARABIC(B5:B15))
    

The result is the sum of the Roman numbers in B5:B15. The Arabic numbers in C5:C15 are shown for reference only.

_Note: the [ARABIC function](https://exceljet.net/functions/arabic-function)
 was introduced in Excel 2013._

Generic formula
---------------

    =SUMPRODUCT(ARABIC(range))

Explanation 
------------

The goal in this example is to sum a range of Roman numbers. The challenge is that Roman numbers appear as text in Excel, not numeric values. If you try to use the [SUM function](https://exceljet.net/functions/sum-function)
 to sum a range of Roman numbers directly, the result is zero (0).

The solution is to use the [ARABIC function](https://exceljet.net/functions/arabic-function)
 to convert the Roman numbers to regular numbers, then sum the result. The ARABIC function takes a valid Roman number and returns its Arabic equivalent. For example:

    =ARABIC("V") // returns 5
    =ARABIC("IX") // returns 9
    =ARABIC("MMXXI") // returns 2021
    

Notice the Roman numbers are provided as [text strings](https://exceljet.net/glossary/text-value)
.

In the worksheet shown, we feed the entire range of Roman numbers in B5:B15 into the ARABIC function in one step:

    =ARABIC(B5:B15)
    

Because there are 11 cells in the range, the result is an [array](https://exceljet.net/glossary/array)
 that contains 11 numbers:

    {1;5;10;25;50;75;100;250;700;1900;2000}
    

Each number corresponds to a Roman number in B5:B15. This array is returned directly to the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
:

    =SUMPRODUCT({1;5;10;25;50;75;100;250;700;1900;2000}) // returns 5116
    

With just one array to process, SUMPRODUCT returns the sum of the numbers: 5116.

This example is a good example of the power of [nesting](https://exceljet.net/glossary/nesting)
 functions together. It also illustrates how [array formulas](https://exceljet.net/glossary/array-formula)
 can be quite simple.

_Note: the [ROMAN function](https://exceljet.net/functions/roman-function)
 performs the opposite conversion as the ARABIC function, converting Arabic numbers to Roman numbers._

### Why SUMPRODUCT and not SUM?

Why can't we use the SUM function like this:

    =SUM(ARABIC(B5:B15))
    

The answer is a bit complicated. In [Excel 365](https://exceljet.net/glossary/excel-365)
, you _can_ use SUM without any special consideration\*, since [Excel 365 handles arrays natively](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
:

    =SUM(ARABIC(B5:B15)) // works fine in Excel 365
    

In other versions of Excel, the SUM function will work, but must be entered as an array formula with [Control + Shift + Enter](https://exceljet.net/glossary/cse)
:

    {=SUM(ARABIC(B5:B15))} // array form in other versions
    

With SUMPRODUCT, the formula will work in all versions of Excel:

    =SUMPRODUCT(ARABIC(B5:B15)) // works in all versions
    

In other words, using SUMPRODUCT ensures the formula will work in all versions of Excel \*\* without any special handling. This is because SUMPRODUCT can handle many array operations natively.

_\* If an Excel 365 worksheet that uses the SUM option is opened in an earlier version of Excel, Excel will automatically convert the formula to the array form and you will see curly braces {} around the formula. The result will remain unchanged. However, if a user edits the formula, and doesn't re-enter with Control + Shift + Enter, SUM will not return the correct result._

_You will also see curly braces added to the SUMPRODUCT version when a worksheet created with Excel 365 is opened in older versions of Excel. However, in this case, the formula can be re-entered without Control + Shift + Enter and will still return the correct result. In other words, Excel changes the formula to the array form automatically since it contains an array operation, but the array form is not necessary since SUMPRODUCT can handle the array operation natively._

_\*\* The [ARABIC function](https://exceljet.net/functions/arabic-function)
 was introduced in Excel 2013._

Related formulas
----------------

[![Excel formula: Map inputs to arbitrary values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20inputs%20to%20arbitrary%20values.png "Excel formula: Map inputs to arbitrary values")](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)

### [Map inputs to arbitrary values](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)

In this example, the goal is to map the numbers 1-6 to the arbitrary values seen in the table below. For example: If the input is 1, the output should be 10 If the input is 2, the output should be 81 If the input is 3, the output should be 17 If the input is 4, the output should be 23 And so on.....

[![Excel formula: Map text to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20text%20to%20numbers.png "Excel formula: Map text to numbers")](https://exceljet.net/formulas/map-text-to-numbers)

### [Map text to numbers](https://exceljet.net/formulas/map-text-to-numbers)

This formula uses the value in cell F7 for a lookup value, the range B6:C10 for the lookup table, the number 2 to indicate "2nd column", and zero as the last argument to force an exact match. Although in this case we are mapping text values to numeric outputs, the same formula can handle text to...

[![Excel formula: Translate letters to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/translate%20letters%20to%20numbers.png "Excel formula: Translate letters to numbers")](https://exceljet.net/formulas/translate-letters-to-numbers)

### [Translate letters to numbers](https://exceljet.net/formulas/translate-letters-to-numbers)

At the core, this formula uses an array operation to generate an array of letters from the input text, translates each letter individually to a number, then joins all numbers together again and returns the output as a string. To parse the input string into an array or letters, we use MID, ROW, LEN...

[![Excel formula: Sum text values like numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20text%20values%20like%20numbers.png "Excel formula: Sum text values like numbers")](https://exceljet.net/formulas/sum-text-values-like-numbers)

### [Sum text values like numbers](https://exceljet.net/formulas/sum-text-values-like-numbers)

The heart of this formula is a basic INDEX and MATCH formula, used to translate text values into numbers as defined in a lookup table. For example, to translate "EX" to the corresponding number, we would use: =INDEX(value,MATCH("EX",code,0)) which would return 4. The twist in this problem however...

Related functions
-----------------

[![Excel ARABIC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_arabic.png "Excel ARABIC function")](https://exceljet.net/functions/arabic-function)

### [ARABIC Function](https://exceljet.net/functions/arabic-function)

The Excel ARABIC function converts a Roman numeral as text to an Arabic numeral. For example, the formula =ARABIC("VII") returns 7.

[![Excel ROMAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20roman%20function.png "Excel ROMAN function")](https://exceljet.net/functions/roman-function)

### [ROMAN Function](https://exceljet.net/functions/roman-function)

The Excel ROMAN function converts a number to a Roman numeral as text. For example, the formula =ROMAN(4) returns IV.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

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
    
*   [Translate letters to numbers](https://exceljet.net/formulas/translate-letters-to-numbers)
    
*   [Sum text values like numbers](https://exceljet.net/formulas/sum-text-values-like-numbers)
    

### Functions

*   [ARABIC Function](https://exceljet.net/functions/arabic-function)
    
*   [ROMAN Function](https://exceljet.net/functions/roman-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

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