# Count cells that contain n characters - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-contain-n-characters

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-contain-n-characters#main-content)

[](https://exceljet.net/formulas/count-cells-that-contain-n-characters#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-contain-errors)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that contain n characters
=====================================

by Dave Bruns · Updated 17 Aug 2022

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[LEN](https://exceljet.net/functions/len-function)

[REPT](https://exceljet.net/functions/rept-function)

![Excel formula: Count cells that contain n characters](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20contain%20n%20characters.png "Excel formula: Count cells that contain n characters")

Summary
-------

To count the number of cells that contain **n** characters, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 with the [LEN function](https://exceljet.net/functions/len-function)
. In the example shown, the formula in E6 is:

    =SUMPRODUCT(--(LEN(B5:B15)=E4))
    

The result is 4, since there are four cells in B5:B15 that contain five characters.

Generic formula
---------------

    =SUMPRODUCT(--(LEN(range)=n))

Explanation 
------------

In this example, the goal is to count the number of cells in B5:B15 that contain a given number of characters, where the number of characters **n** is provided as a variable in cell E4. 

### SUMPRODUCT with LEN

One way to solve this problem is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 with the [LEN function](https://exceljet.net/functions/len-function)
. In the example shown, the formula in E6 is:

    =SUMPRODUCT(--(LEN(B5:B15)=E4))
    

Working from the inside out, the LEN function is used to get the length of each value in the range like this:

    LEN(B5:B15)
    

Since the [range](https://exceljet.net/glossary/range)
 B5:B15 contains 11 cells, LEN returns 11 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {5;4;5;6;5;4;6;6;5;4;7}
    

Each number in the array is the length of a cell in B5:B15. This array is then compared to cell E4, which contains the number 5. The result is a new array containing 11 TRUE and FALSE values. To summarize:

    =LEN(B5:B15)=E4
    ={5;4;5;6;5;4;6;6;5;4;7}=5
    ={TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE}
    

Each TRUE value corresponds to a cell in B5:B15 that contains 5 characters.

Next, a [double-negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is used to convert the TRUE and FALSE values to 1s and 0s, and the resulting array is delivered directly to the SUMPRODUCT function:

    =SUMPRODUCT({1;0;1;0;1;0;0;0;1;0;0}) // returns 4
    

SUMPRODUCT returns the sum of the array, 4, as a final result. If a new number is entered in cell E4, the formula will recalculate and return a new result.

### COUNTIF function

Another way to solve this problem is with the COUNTIF function and the question mark (?) [wildcard](https://exceljet.net/glossary/wildcard)
. [COUNTIF supports three wildcards](https://exceljet.net/functions/countifs-function)
 that can be used in the _criteria_ [argument](https://exceljet.net/glossary/function-argument)
: question mark (?), asterisk(\*), or tilde (~). A question mark (?) matches any one character and an asterisk (\*) matches zero or more characters of any kind. In this example, we can use the question mark (?) wildcard to count cells that contain 5 characters like this:

    =COUNTIF(B5:B15,"?????") // returns 4
    

The "?" symbol is a [wildcard](https://exceljet.net/glossary/wildcard)
 in Excel that means "match any single character", so this pattern will count cells that contain five characters. To adapt the formula above to use **n** from cell E4, we can add the [REPT function](https://exceljet.net/functions/rept-function)
 like this:

    =COUNTIF(B5:B15,REPT("?",E4))
    

The REPT function repeats the "?" five times inside COUNTIF, so the result is the same.

_Note: One difference in the COUNTIF formula is that COUNTIF with "?" as a wildcard will only count characters in [text values](https://exceljet.net/glossary/text-value)
 — cells that contain numeric values will not be counted. The SUMPRODUCT + LEN formula on the other hand will count characters of any kind, including numbers._

Related formulas
----------------

[![Excel formula: Count cells over n characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20over%20n%20characters.png "Excel formula: Count cells over n characters")](https://exceljet.net/formulas/count-cells-over-n-characters)

### [Count cells over n characters](https://exceljet.net/formulas/count-cells-over-n-characters)

In this example, the goal is to count the number of cells in a range that are over a certain number of characters in length, where the number ( n ) is provided as a variable in cell F4. This problem can be solved with the SUMPRODUCT and LEN functions like this: =SUMPRODUCT(N(LEN(B5:B15)>F4)) //...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rept%20function.png "Excel REPT function")](https://exceljet.net/functions/rept-function)

### [REPT Function](https://exceljet.net/functions/rept-function)

The Excel REPT function repeats characters a given number of times. For example, =REPT("x",5) returns "xxxxx".

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells over n characters](https://exceljet.net/formulas/count-cells-over-n-characters)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [REPT Function](https://exceljet.net/functions/rept-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

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