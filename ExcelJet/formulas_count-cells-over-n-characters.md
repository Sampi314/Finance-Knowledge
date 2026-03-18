# Count cells over n characters - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-over-n-characters

---

[Skip to main content](https://exceljet.net/formulas/count-cells-over-n-characters#main-content)

[](https://exceljet.net/formulas/count-cells-over-n-characters#)

*   [Previous](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-are-blank)
    

[Count](https://exceljet.net/formulas#Count)

Count cells over n characters
=============================

by Dave Bruns · Updated 17 Aug 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[LEN](https://exceljet.net/functions/len-function)

[N](https://exceljet.net/functions/n-function)

![Excel formula: Count cells over n characters](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20over%20n%20characters.png "Excel formula: Count cells over n characters")

Summary
-------

To count cells that contain more than a certain number of characters, you can use a formula based on the [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
, [LEN](https://exceljet.net/functions/len-function)
, and [N](https://exceljet.net/functions/n-function)
 functions. In the example shown, the formula in F6 is:

    =SUMPRODUCT(N(LEN(B5:B15)>F4))
    

where **n** comes from cell F4, which contains 40. The result is 5, since there are 5 cells in B5:B15 that contain more than 40 characters.

Generic formula
---------------

    =SUMPRODUCT(N(LEN(range)>n))

Explanation 
------------

In this example, the goal is to count the number of cells in a range that are over a certain number of characters in length, where the number (**n**) is provided as a variable in cell F4. This problem can be solved with the SUMPRODUCT and LEN functions like this:

    =SUMPRODUCT(N(LEN(B5:B15)>F4)) // returns 5
    

The formula returns 5 since there are five cells in B5:B15 that contain more than 40 characters.

### Reference calculation

The formula in C5, copied down, is based on the [LEN function](https://exceljet.net/functions/len-function)
:

    =LEN(B5) // returns 25
    

This calculation is provided for reference only and is not used by the formula above. The counts in column C make it easy to quickly check results.

### Checking length

Working from the inside out, the number of characters in each cell is calculated with the [LEN function](https://exceljet.net/functions/len-function)
 like this:

    LEN(B5:B15)
    

The [LEN function](https://exceljet.net/functions/len-function)
 runs on the range B5:B15. Because we give LEN multiple values, it returns multiple results in an [array](https://exceljet.net/glossary/array)
 like this:

    {25;47;46;45;42;32;36;34;36;40;46}
    

Each number in the array is the length of a cell in B5:B15. This array is evaluated with the logical expression ">F4", which creates an array of TRUE FALSE values:

    {FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE}
    

Each TRUE corresponds to a cell that contains more than 40 characters, since cell F4 contains 40. To convert the TRUE and FALSE values to their numeric equivalents, we use the [N function](https://exceljet.net/functions/n-function)
:

    N({FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE})
    

_Note: the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is another way to convert TRUE/FALSE to 1/0._

The result is an array of 1s and 0s:

    {0;1;1;1;1;0;0;0;0;0;1}
    

### Counting results

This array is returned directly to the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
, which returns the sum of numbers in the array:

    =SUMPRODUCT({0;1;1;1;1;0;0;0;0;0;1}) // returns 5
    

The final result is 5. Since **n** is provided as a variable in cell F4, it can be changed at any time and the formula will recalculate and return a new result.

### COUNTIFS function

This is an example of a problem that can't be solved directly with the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. This is because [COUNTIFS requires a range](https://exceljet.net/articles/excels-racon-functions)
 and won't allow processing of an array like that returned by the LEN function above. However, if you don't mind using a [helper column](https://exceljet.net/glossary/helper-column)
, you could use COUNTIFS on column C like this:

    =COUNTIFS(C5:C15,">"&F4) // returns 5
    

The result is the same as the SUMPRODUCT formula above. Note the greater than [operator](https://exceljet.net/glossary/logical-operators)
 (>) is enclosed in double quotes ("") and [concatenated](https://exceljet.net/articles/how-to-concatenate-in-excel)
 to F4.

Related formulas
----------------

[![Excel formula: Count cells that contain odd numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20odd%20numbers.png "Excel formula: Count cells that contain odd numbers")](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)

### [Count cells that contain odd numbers](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)

In this example, the goal is to count odd numbers in the range B5:B15, which is named data . This can be done with the SUMPRODUCT function together with the ISODD function. Instead of ISODD, the MOD function can also be used. Both approaches are explained below. SUMPRODUCT with ISODD The SUMPRODUCT...

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

[![Excel formula: Count cells that contain n characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20n%20characters.png "Excel formula: Count cells that contain n characters")](https://exceljet.net/formulas/count-cells-that-contain-n-characters)

### [Count cells that contain n characters](https://exceljet.net/formulas/count-cells-that-contain-n-characters)

In this example, the goal is to count the number of cells in B5:B15 that contain a given number of characters, where the number of characters n is provided as a variable in cell E4. SUMPRODUCT with LEN One way to solve this problem is to use the SUMPRODUCT function with the LEN function . In the...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

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

*   [Count cells that contain odd numbers](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)
    
*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Count cells that contain n characters](https://exceljet.net/formulas/count-cells-that-contain-n-characters)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [N Function](https://exceljet.net/functions/n-function)
    

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