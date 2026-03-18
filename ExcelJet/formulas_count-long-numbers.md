# Count long numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-long-numbers

---

[Skip to main content](https://exceljet.net/formulas/count-long-numbers#main-content)

[](https://exceljet.net/formulas/count-long-numbers#)

*   [Previous](https://exceljet.net/formulas/count-items-in-list)
    
*   [Next](https://exceljet.net/formulas/count-matches-between-two-columns)
    

[Count](https://exceljet.net/formulas#Count)

Count long numbers
==================

by Dave Bruns · Updated 21 Aug 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Count long numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20long%20numbers.png "Excel formula: Count long numbers")

Summary
-------

To count numbers longer than 15 digits, you can enter the numbers as text and use the [SUM](https://exceljet.net/functions/sum-function)
 or [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 function to perform the count. In the example shown, the formula in E5 is:

    =SUM(--(data=B5))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15.

_Note: The [COUNTIF function](https://exceljet.net/functions/countif-function)
 will not count the numbers in this example correctly, as explained below._

Generic formula
---------------

    SUM(--(range=value))

Explanation 
------------

In this example the goal is to count numbers longer than 15 digits with a formula. The [COUNTIF function](https://exceljet.net/functions/countif-function)
 may seem like this logical choice. However, if you try to count very long numbers (16+ digits) in a range with the COUNTIF function, you may see incorrect results, due to a bug in how [RACON functions](https://exceljet.net/articles/excels-racon-functions)
 handle long numbers, even when the numbers are stored as text. You can see this problem in the worksheet below. All counts in column D are _incorrect_. Each number in column B is unique, yet the count returned by COUNTIF suggests the numbers are duplicates.

![COUNTIF counts are incorrect due to long number problem](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20long%20numbers%20with%20COUNTIF%20does%20not%20work.png?itok=JWZzzGOw "COUNTIF counts are incorrect due to long number problem")

     =COUNTIF(data,B5)
    

This problem is related to how Excel handles numbers. Excel can only handle 15 significant digits, and if you enter a number with more than 15 digits in Excel, you will see the trailing digits silently converted to zero. The counting problem mentioned above arises from this limit.

Normally, you can avoid this limit by entering long [numbers as text](https://exceljet.net/videos/how-to-enter-numbers-as-text-in-excel)
, either by starting the number with a single quote (i.e. '999999999999999999) or by formatting the cell(s) as Text before entering. As long as you don't need to perform math operations on a number, this is a good solution, and it will handle long numbers like credit card numbers and serial numbers without losing any numbers.

However, if you try to use COUNTIF to count a number with more than 15 digits (even when stored as text) you may see incorrect results. This happens because COUNTIF internally converts the text value back to a number at some point during processing, which triggers the 15 digit limit described above. With trailing digits converted to zero, long numbers may look like duplicates to [RACON functions](https://exceljet.net/articles/excels-racon-functions)
 like COUNTIF, COUNTIFS, SUMIF, SUMIFS, etc. The solution is to use the SUM function or the SUMPRODUCT function, as explained below.

### SUM function

One solution is to replace the COUNTIF formula with a formula that uses the [SUM function](https://exceljet.net/functions/sum-function)
. In the example shown, the formula in E5 is:

    =SUM(--(data=B5))
    

The formula uses the [named range](https://exceljet.net/glossary/named-range)
 **data** (B5:B9) and [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 to count values. Working from the inside out, this expression compares all values in **data** (B5:B15) with the value in B5:

    data=B5
    

Because **data** contains 11 cells, the result is an [array](https://exceljet.net/glossary/array)
 of TRUE/FALSE results like this:

    {TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

Notice that the TRUE value corresponds to the first number in the range B5:B15, and all remaining values are FALSE. This tells us the number 1234567891234567 occurs just once in the data. Because the SUM function will ignore the logical values TRUE and FALSE, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to convert the TRUE and FALSE values to 1s and 0s:

    --(data=B5) // returns {1;0;0;0;0;0;0;0;0;0;0}
    

This results in an array containing only 1s and 0s, which is returned directly to the SUM function:

    =SUM({1;0;0;0;0;0;0;0;0;0;0}) // returns 1
    

The SUM function sums the items in the array and returns 1 as a final result.

_Note: this formula must be entered with Control + Shift + Enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

### SUMPRODUCT function

In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, the formula above is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered in a special way. To avoid this step, you can replace the SUM function with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 like this:

    =SUMPRODUCT(--(data=B5))
    

The behavior of the formula is the same, but because SUMPRODUCT is in a small group of functions that can handle [array operations](https://exceljet.net/glossary/array-operation)
 natively, the formula requires no special handling. For more on this topic, see [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)

Related formulas
----------------

[![Excel formula: Count items in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20items%20in%20list.png "Excel formula: Count items in list")](https://exceljet.net/formulas/count-items-in-list)

### [Count items in list](https://exceljet.net/formulas/count-items-in-list)

In this example, the goal is to create a count of each color in column B. The simplest way to solve this problem is with the COUNTIFS function. COUNTIFS function The COUNTIFS function returns the count of cells that meet one or more criteria. COUNTIFS can be used with criteria based on dates,...

[![Excel formula: Count numbers with leading zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20numbers%20with%20leading%20zeros.png "Excel formula: Count numbers with leading zeros")](https://exceljet.net/formulas/count-numbers-with-leading-zeros)

### [Count numbers with leading zeros](https://exceljet.net/formulas/count-numbers-with-leading-zeros)

In this example, the goal is to count numbers that contain leading zeros. In cell E5, we have the code "009875" and we want to count how many times this code appears in the range B5:B16. The challenge is that Excel can be finicky with leading zeros. Technically, the values in B5:B16 are text , as...

[![Excel formula: Count specific words in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_specific_words_in_range.png "Excel formula: Count specific words in a range")](https://exceljet.net/formulas/count-specific-words-in-a-range)

### [Count specific words in a range](https://exceljet.net/formulas/count-specific-words-in-a-range)

In the generic version of the formula, rng represents the range to check, and txt is the word or substring to count. In the example shown, B5:B8 is the range to check, and C2 contains the text (word or substring) to count. For each cell in the range, SUBSTITUTE removes the substring from the...

[![Excel formula: Count cells that do not contain errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain%20errors.png "Excel formula: Count cells that do not contain errors")](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)

### [Count cells that do not contain errors](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)

In this example, the goal is to count the number of cells in a range that do not contain errors. The best way to solve this problem is to use the SUMPRODUCT function together with the ISERROR function. You can also use the COUNTIF function or COUNTIFS function to exclude specific errors. Both...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count items in list](https://exceljet.net/formulas/count-items-in-list)
    
*   [Count numbers with leading zeros](https://exceljet.net/formulas/count-numbers-with-leading-zeros)
    
*   [Count specific words in a range](https://exceljet.net/formulas/count-specific-words-in-a-range)
    
*   [Count cells that do not contain errors](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Links

*   [15-significant-digit issue with SUMIF(S), COUNTIF(S), AVERAGEIF(S) (wmfexcel.com)](https://wmfexcel.com/2015/01/24/15-significant-digit-issue-with-sumifs-countifs-averageifs/)
    

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