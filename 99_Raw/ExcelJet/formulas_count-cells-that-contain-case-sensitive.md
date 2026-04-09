# Count cells that contain case sensitive - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-contain-case-sensitive

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive#main-content)

[](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-begin-with)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that contain case sensitive
=======================================

by Dave Bruns · Updated 17 Aug 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[FIND](https://exceljet.net/functions/find-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6725/download?token=intCfZkS)
 (14.97 KB)

![Excel formula: Count cells that contain case sensitive](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20contain%20case%20sensitive.png "Excel formula: Count cells that contain case sensitive")

Summary
-------

To count cells that contain specific text (i.e. contain a substring), taking into account upper and lower case, you can use a formula based on the [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [FIND](https://exceljet.net/functions/find-function)
 functions, together with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, E5 contains this formula, copied down:

    =SUMPRODUCT(--ISNUMBER(FIND(D5,data)))
    

Where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15. The result is a case-sensitive count of each substring listed in column D.

Generic formula
---------------

    =SUMPRODUCT(--ISNUMBER(FIND(value,data)))

Explanation 
------------

In this example, the goal is to count codes that appear as substrings in a case-sensitive way. The functions [COUNTIF](https://exceljet.net/functions/countif-function)
 and [COUNTIFS](https://exceljet.net/functions/countifs-function)
 are both good options for counting text values, but these functions are not case-sensitive, so they can't be used to solve this problem. The solution is to use the [FIND function](https://exceljet.net/functions/find-function)
 together with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 to check for substrings and the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to add up the results.

The FIND function is _always_ case-sensitive and takes three arguments: _find\_text,_ _within\_text_, and _start\_num_. _Find\_text_ is the text we want to look for, and _within\_text_ is the text we are looking inside of. _Start\_num_ is the position at which to start looking in _find\_text_. _Start\_num_ defaults to 1, so we aren't providing a value in this case, because we always want FIND to start at the first character. When _find\_text_ is found inside _within\_text_, FIND returns the _position_ of the found text as a number:

    =FIND("ABC","ABC-101") // returns 1
    =FIND("ABC","10-ABC-101") // returns 4
    

When _find\_text_ is _not found_, FIND returns the #VALUE! error:

    =FIND("ABC","XYZ-101") // returns #VALUE!
    

This means we can use the ISNUMBER function to convert the result from FIND into a TRUE and FALSE value. Any number will result in TRUE, and any error will result in FALSE:

    =ISNUMBER(FIND("ABC","ABC-101")) // returns TRUE
    =ISNUMBER(FIND("XYZ","ABC-101")) // returns FALSE
    

This idea is [explained in more detail here](https://exceljet.net/formulas/cell-contains-specific-text)
.

In the example shown, we have four substrings in column D and a variety of codes in B5:B15, which is the [named range](https://exceljet.net/glossary/named-range)
 **data**. We want to count how many times each substring in D5:D8 appears in B5:B15, and this count needs to be case-sensitive.

The formula in E5, copied down, is:

    =SUMPRODUCT(--ISNUMBER(FIND(D5,data)))
    

Working from the inside-out, the [FIND function](https://exceljet.net/functions/find-function)
 is used to look for a substring like this:

    FIND(D5,data)
    

FIND checks for the value in D5 ("ABC") in all cells in the **data**. Because we give FIND _multiple_ values in the _within\_text_ argument, it returns _multiple_ results. In total, FIND returns 11 values (one for each code in B5:B15) in an [array](https://exceljet.net/glossary/array)
 like this:

    {4;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;4;4;#VALUE!;4}
    

Each number represents a cell in B5:B15 that contains "ABC". Each #VALUE! represents a value in B5:B15 that does not contain "ABC". Looking more closely, we can see that FIND found "ABC" in 4 cells out of 11. This array is returned directly to the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 which converts each value to TRUE or FALSE:

    ISNUMBER({4;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;4;4;#VALUE!;4})
    

ISNUMBER returns an array of 11 TRUE and FALSE values:

    {TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE}
    

Because we want to _count_ results, we use a [double-negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to convert TRUE and FALSE values into 1's and 0's:

    --{TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE}
    

The resulting array looks like this:

    {1;0;0;0;0;0;0;1;1;0;1} // 11 results
    

Using the double-negative like this is an example of [Boolean logic](https://exceljet.net/glossary/boolean-logic)
, a technique for handling TRUE and FALSE values like 1's and 0's. The resulting array is delivered directly to the SUMPRODUCT function:

    =SUMPRODUCT({1;0;0;0;0;0;0;1;1;0;1}) // returns 4
    

With just one array to process, SUMPRODUCT sums all numbers in the array and returns the final result: 4. As the formula is copied down, it returns a count of each substring in column D. The reference to **data** does not change, because a [named range](https://exceljet.net/glossary/named-range)
 automatically behaves like an [absolute reference](https://exceljet.net/glossary/absolute-reference)
.

_Note: Because SUMPRODUCT can handle arrays natively, it's not necessary to use Control+Shift+Enter to enter this formula._

Related formulas
----------------

[![Excel formula: Count cells equal to case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20case%20sensitive.png "Excel formula: Count cells equal to case sensitive")](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)

### [Count cells equal to case sensitive](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)

In this example, the goal is to count codes in a case-sensitive way. The COUNTIF function and the COUNTIFS function are both good options for counting text values, but neither is case-sensitive, so they can't be used to solve this problem. The solution is to use the EXACT function to compare codes...

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

[![Excel formula: Count cells that begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20begin%20with.png "Excel formula: Count cells that begin with")](https://exceljet.net/formulas/count-cells-that-begin-with)

### [Count cells that begin with](https://exceljet.net/formulas/count-cells-that-begin-with)

In this example, the goal is to count cells in the range B5:B16 that begin with specific text, which is provided in column D. For convenience, the range B5:B16 is named data . COUNTIF function The simplest way to solve this problem is with the COUNTIF function and a wildcard. COUNTIF supports three...

[![Excel formula: Case sensitive lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case%20sensitive%20lookup.png "Excel formula: Case sensitive lookup")](https://exceljet.net/formulas/case-sensitive-lookup)

### [Case sensitive lookup](https://exceljet.net/formulas/case-sensitive-lookup)

In this example, the goal is to perform a case-sensitive lookup on the name in column B, based on a lookup value entered in cell E5. By default, Excel is not case-sensitive. This means that standard lookup functions like VLOOKUP , XLOOKUP , and INDEX and MATCH are also not case-sensitive. These...

[![Excel formula: Count specific words in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_words_1.png "Excel formula: Count specific words in a cell")](https://exceljet.net/formulas/count-specific-words-in-a-cell)

### [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)

B4 is the cell we're counting words in, and C4 contains the substring (word or any substring) you are counting. SUBSTITUTE removes the substring from the original text and LEN calculates the length of the text without the substring. This number is then subtracted from the length of the original...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells equal to case sensitive](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
    
*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Count cells that begin with](https://exceljet.net/formulas/count-cells-that-begin-with)
    
*   [Case sensitive lookup](https://exceljet.net/formulas/case-sensitive-lookup)
    
*   [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

### Articles

*   [The double negative in Excel formulas](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
    

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