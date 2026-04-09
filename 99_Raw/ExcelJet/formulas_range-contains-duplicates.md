# Range contains duplicates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/range-contains-duplicates

---

[Skip to main content](https://exceljet.net/formulas/range-contains-duplicates#main-content)

[](https://exceljet.net/formulas/range-contains-duplicates#)

*   [Previous](https://exceljet.net/formulas/random-sort-formula)
    
*   [Next](https://exceljet.net/formulas/range-contains-one-of-many-substrings)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Range contains duplicates
=========================

by Dave Bruns · Updated 6 Dec 2022

Related functions 
------------------

[OR](https://exceljet.net/functions/or-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7100/download?token=H0dkRt8c)
 (16.22 KB)

![Excel formula: Range contains duplicates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/range%20contains%20duplicates.png "Excel formula: Range contains duplicates")

Summary
-------

To test if a [range](https://exceljet.net/glossary/range)
 or list contains duplicates, you can use a formula based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
 and the [OR function](https://exceljet.net/functions/or-function)
. In the example shown, the formula in cell E5 is:

    =OR(COUNTIF(data,data)>1)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

Generic formula
---------------

    =OR(COUNTIF(range,range)>1)

Explanation 
------------

In this example, the goal is to test if a given range contains duplicate values and return TRUE if duplicates exist and FALSE if not. This is essentially a counting problem and the solution is based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
, which counts values in a range that meet supplied criteria. The formula used in E5 is:

    =OR(COUNTIF(data,data)>1)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16.

### Background study

Below are related links to help you understand how this formula works:

*   [What is an array formula?](https://exceljet.net/videos/what-is-an-array-formula)
     - 3 min video
*   [What is an array?](https://exceljet.net/videos/what-is-an-array)
     - 3 min video

### COUNTIF function

Working from the inside-out, the core of the formula is based on the COUNTIF function:

    COUNTIF(data,data)
    

Here, **data** (B5:B16) is given for both range and criteria. Typically, criteria is supplied as a _single_ value, but in this case **data** contains 12 values. The result is that COUNTIF returns 12 counts (one for each value) in a single [array](https://exceljet.net/glossary/array)
 like this:

    {1;1;2;1;1;1;1;2;1;1;1;1}
    

In "modern" versions of Excel that support [dynamic arrays](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can enter the COUNTIF formula above as a standalone formula and you will see the results [spill](https://exceljet.net/glossary/spill)
 onto the worksheet. Most values in the array are 1 but notice that the third value and eighth value are 2, which indicate duplicate values. The value 155 occurs twice at these positions in the range, which is why the count for that number is 2.

In this particular problem, we don't care about the specific numbers returned by COUNTIF, we only care if any number is greater than 1. Therefore, we use the greater than [operator](https://exceljet.net/glossary/logical-operators)
 (>) to check the result:

    =COUNTIF(data,data)>1
    ={1;1;2;1;1;1;1;2;1;1;1;1}>1
    

The result is an array of TRUE and FALSE values.

    {FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE}
    

This is the information we need to solve the problem. If any value in the array is TRUE, it means we have duplicates. If all values are FALSE, it means there are no duplicates. To check the array, we can use the OR function.

### OR function

The array above is returned directly to the OR function:

    =OR({FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE})
    

The [OR function](https://exceljet.net/functions/or-function)
 returns TRUE if _any_ given argument evaluates to TRUE, and returns FALSE only if all supplied arguments evaluate to FALSE. The final result is TRUE, since at least one value in the array is TRUE.

_Note: COUNTIF will automatically ignore empty cells in this configuration, which return a count of 0._

### SUMPRODUCT alternative

To avoid an array formula that requires Control + Shift + Enter, you can use the SUMPRODUCT alternative below:

    =SUMPRODUCT(--(COUNTIF(data,data)>1))>0
    

As above, the counts are checked for any numbers greater than 1, resulting in an array of TRUE and FALSE values. The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) converts the TRUE and FALSE values to 1s and 0s, and the result is delivered to SUMPRODUCT, which returns the total. Finally, the total from SUMPRODUCT is checked against zero. Since the total is greater than zero, the formula returns TRUE as a final result.

This is still an array formula but the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 handles the array operation natively, so it is not necessary to use Control + Shift + Enter.

### Count duplicates

To _count_ the number of duplicates in the range you can adapt the formula like this:

    =SUMPRODUCT(--(COUNTIF(data,data)>1))
    

_Note: this is also an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
, but because [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 can handle the array operation natively, it is not necessary to use control + shift + enter._

The configuration of COUNTIF is the same as the original formula above, so we end up with the same array of TRUE and FALSE values. The [double negative](https://exceljet.net/glossary/double-unary)
 (--) converts the TRUE and FALSE values to 1s and 0s, and the result is delivered to SUMPRODUCT, which returns the sum of the array:

    =SUMPRODUCT({0;0;1;0;0;0;0;1;0;0;0;0}) // returns 2
    

_Note: the [SUM function](https://exceljet.net/functions/sum-function)
 will also work fine in place of SUMPRODUCT, but the formula be entered with control + shift + enter in older versions of Excel._

Related formulas
----------------

[![Excel formula: Highlight duplicate values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20duplicate%20values.png "Excel formula: Highlight duplicate values")](https://exceljet.net/formulas/highlight-duplicate-values)

### [Highlight duplicate values](https://exceljet.net/formulas/highlight-duplicate-values)

COUNTIF simply counts the number of times each value appears in the range. When the count is more than 1, the formula returns TRUE and triggers the rule. When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the...

[![Excel formula: Highlight duplicate rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20duplicate%20rows.png "Excel formula: Highlight duplicate rows")](https://exceljet.net/formulas/highlight-duplicate-rows)

### [Highlight duplicate rows](https://exceljet.net/formulas/highlight-duplicate-rows)

In the formula, COUNTIFS counts the number of times each value in a cell appears in its "parent" column. By definition, each value must appear at least once, so when the count > 1, the value must be a duplicate. The references are carefully locked so the formula will return true only when all 3...

[![Excel formula: Flag first duplicate in a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/flag%20first%20duplicate%20in%20a%20list.png "Excel formula: Flag first duplicate in a list")](https://exceljet.net/formulas/flag-first-duplicate-in-a-list)

### [Flag first duplicate in a list](https://exceljet.net/formulas/flag-first-duplicate-in-a-list)

At the core, this formula is composed of two sets of the COUNTIF function wrapped in the IF function . The outer IF + COUNTIF first checks to see if the value in question (B4) appears more than once in the list: =IF(COUNTIF($B$4:$B$11,B4)>1 If not, the outer IF function returns an empty string...

[![Excel formula: Find duplicate values in two columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find%20duplicate%20values%20in%20two%20columns.png "Excel formula: Find duplicate values in two columns")](https://exceljet.net/formulas/find-duplicate-values-in-two-columns)

### [Find duplicate values in two columns](https://exceljet.net/formulas/find-duplicate-values-in-two-columns)

This formula uses two named ranges, "range1" (B5:B12) and "range2" (D5:D10). The core of this formula is the COUNTIF function, which returns a count of each value in both range inside the AND function: COUNTIF(range1,B5) // count in range1 COUNTIF(range2,B5) // count in range2 COUNTIF will either...

[![Excel formula: Sort and extract unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20and%20extract%20unique%20values.png "Excel formula: Sort and extract unique values")](https://exceljet.net/formulas/sort-and-extract-unique-values)

### [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)

Note: the core idea of this formula is adapted from an example in Mike Girvin's excellent book Control+Shift+Enter . The example shown uses several formulas, which are described below. At a high level, the MMULT function is used to compute a numeric rank in a helper column (column C), and this rank...

[![Excel formula: Count unique text values in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20text%20values%20in%20a%20range.png "Excel formula: Count unique text values in a range")](https://exceljet.net/formulas/count-unique-text-values-in-a-range)

### [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)

This formula is more complicated than a similar formula that uses FREQUENCY to count unique numeric values because FREQUENCY doesn't normally work with non-numeric values. As a result, a large part of the formula simply transforms the non-numeric data into numeric data that FREQUENCY can handle...

[![Excel formula: Range contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20specific%20text.png "Excel formula: Range contains specific text")](https://exceljet.net/formulas/range-contains-specific-text)

### [Range contains specific text](https://exceljet.net/formulas/range-contains-specific-text)

The COUNTIF function counts cells that meet supplied criteria, and returns a count of occurrences found. If no cells meet criteria, COUNTIF returns zero. The asterisk (\*) is a wildcard for one or more characters. By concatenating asterisks before and after the value in D5, the formula will count...

Related functions
-----------------

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Highlight duplicate values](https://exceljet.net/formulas/highlight-duplicate-values)
    
*   [Highlight duplicate rows](https://exceljet.net/formulas/highlight-duplicate-rows)
    
*   [Flag first duplicate in a list](https://exceljet.net/formulas/flag-first-duplicate-in-a-list)
    
*   [Find duplicate values in two columns](https://exceljet.net/formulas/find-duplicate-values-in-two-columns)
    
*   [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)
    
*   [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)
    
*   [Range contains specific text](https://exceljet.net/formulas/range-contains-specific-text)
    

### Functions

*   [OR Function](https://exceljet.net/functions/or-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Links

*   [Check list for duplicate numbers (Chandoo)](http://chandoo.org/wp/2012/06/28/check-list-for-duplicate-numbers/)
    

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