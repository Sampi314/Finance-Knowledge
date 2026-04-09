# Count cells equal to case sensitive - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-equal-to-case-sensitive

---

[Skip to main content](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive#main-content)

[](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive#)

*   [Previous](https://exceljet.net/formulas/count-cells-equal-to)
    
*   [Next](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)
    

[Count](https://exceljet.net/formulas#Count)

Count cells equal to case sensitive
===================================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[EXACT](https://exceljet.net/functions/exact-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6712/download?token=HUgSDRSy)
 (14.84 KB)

![Excel formula: Count cells equal to case sensitive](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20equal%20to%20case%20sensitive.png "Excel formula: Count cells equal to case sensitive")

Summary
-------

To count cells that contain specific text, taking into account upper and lower case, you can use a formula based on the [EXACT function](https://exceljet.net/functions/exact-function)
 together with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, E5 contains this formula, copied down:

    =SUMPRODUCT(--EXACT(D5,data))
    

Where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15. The result is a case-sensitive count for each code in column D.

Generic formula
---------------

    =SUMPRODUCT(--EXACT(value,range))

Explanation 
------------

In this example, the goal is to count codes in a case-sensitive way. The [COUNTIF function](https://exceljet.net/functions/countif-function)
 and the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 are both good options for counting text values, but neither is case-sensitive, so they can't be used to solve this problem. The solution is to use the [EXACT function](https://exceljet.net/functions/exact-function)
 to compare codes and the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to add up the results.

### EXACT function

The EXACT function's sole purpose is to compare text in a case-sensitive manner. EXACT takes two [arguments](https://exceljet.net/glossary/function-argument)
: _text1_ and _text2._ If _text1_ and _text2_ match exactly (considering upper and lower case), EXACT returns TRUE. Otherwise, EXACT returns FALSE:

    =EXACT("abc","abc") // returns TRUE
    =EXACT("abc","ABC") // returns FALSE
    =EXACT("abc","Abc") // returns FALSE
    

### Worksheet example

In the example shown, we have four codes in column D and some duplicated codes in B5:B15, the [named range](https://exceljet.net/glossary/named-range)
 **data**. We want to count how many times each code in D5:D8 appears in B5:B15, and this count needs to be case-sensitive. The formula in E5, copied down, is:

    =SUMPRODUCT((--EXACT(D5,data)))
    

Working from the inside-out, we are using the [EXACT function](https://exceljet.net/functions/exact-function)
 to compare each code in column D with **data** (B5:B15):

    --EXACT(D5,data)
    

EXACT compares the value in D5 ("ABC") to all values in B5:B15. Because we are giving EXACT _multiple_ values in the second argument, it returns _multiple_ results. In total, EXACT returns 11 values (one for each code in B5:B15) in an [array](https://exceljet.net/glossary/array)
 like this:

    --{TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE}
    

Each TRUE represents an exact match of "ABC" in B5:B15. Each FALSE represents a value in B5:B15 that does not match "ABC". Because we want to _count_ results, we use a [double-negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to convert TRUE and FALSE values into 1's and 0's. The resulting array looks like this:

    {1;0;0;0;0;0;0;1;1;0;1} // 11 results
    

Using the double-negative like this is an example of [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. Now that we have an array of 1's and 0's, the only remaining task is to sum things up.

### SUMPRODUCT function

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 is a versatile function that appears in many formulas because of its ability to handle array operations natively in older versions of Excel. The array created in the previous step is delivered directly to the SUMPRODUCT function:

    =SUMPRODUCT({1;0;0;0;0;0;0;1;1;0;1}) // returns 4
    

With just one array to process, SUMPRODUCT sums all numbers in the array and returns the final result: 4.

_Note: Because SUMPRODUCT can handle arrays natively, it's not necessary to use Control+Shift+Enter to enter this formula. In Excel 365, you can use the [SUM function](https://exceljet.net/functions/sum-function)
 instead of SUMPRODUCT. To read more about this, see [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)
_

Related formulas
----------------

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Count cells that contain case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20case%20sensitive.png "Excel formula: Count cells that contain case sensitive")](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)

### [Count cells that contain case sensitive](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)

In this example, the goal is to count codes that appear as substrings in a case-sensitive way. The functions COUNTIF and COUNTIFS are both good options for counting text values, but these functions are not case-sensitive, so they can't be used to solve this problem. The solution is to use the FIND...

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

[![Excel formula: Case sensitive lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case%20sensitive%20lookup.png "Excel formula: Case sensitive lookup")](https://exceljet.net/formulas/case-sensitive-lookup)

### [Case sensitive lookup](https://exceljet.net/formulas/case-sensitive-lookup)

In this example, the goal is to perform a case-sensitive lookup on the name in column B, based on a lookup value entered in cell E5. By default, Excel is not case-sensitive. This means that standard lookup functions like VLOOKUP , XLOOKUP , and INDEX and MATCH are also not case-sensitive. These...

[![Excel formula: Count specific words in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_words_1.png "Excel formula: Count specific words in a cell")](https://exceljet.net/formulas/count-specific-words-in-a-cell)

### [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)

B4 is the cell we're counting words in, and C4 contains the substring (word or any substring) you are counting. SUBSTITUTE removes the substring from the original text and LEN calculates the length of the text without the substring. This number is then subtracted from the length of the original...

[![Excel formula: VLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20case%20sensitive.png "Excel formula: VLOOKUP case-sensitive ")](https://exceljet.net/formulas/vlookup-case-sensitive)

### [VLOOKUP case-sensitive](https://exceljet.net/formulas/vlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on Color with VLOOKUP. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". This presents several challenges. First, Excel is not case-sensitive by default, and there is no built-in...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20operations%20in%20array%20formulas-Play.png)](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

In this video, we'll look at why boolean operations are important in array formulas. Boolean operations are a key building block in the world of dynamic array formulas. To illustrate, let's look at some simple order data. Given the data shown, how can we total orders from Texas using an array...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)
    
*   [Count cells that contain case sensitive](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)
    
*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Case sensitive lookup](https://exceljet.net/formulas/case-sensitive-lookup)
    
*   [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)
    
*   [VLOOKUP case-sensitive](https://exceljet.net/formulas/vlookup-case-sensitive)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    

### Videos

*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    

### Articles

*   [The double negative in Excel formulas](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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