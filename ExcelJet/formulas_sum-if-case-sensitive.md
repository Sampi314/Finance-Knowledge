# Sum if case-sensitive - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-case-sensitive

---

[Skip to main content](https://exceljet.net/formulas/sum-if-case-sensitive#main-content)

[](https://exceljet.net/formulas/sum-if-case-sensitive#)

*   [Previous](https://exceljet.net/formulas/sum-if-between)
    
*   [Next](https://exceljet.net/formulas/sum-if-cell-contains-text-in-another-cell)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if case-sensitive
=====================

by Dave Bruns · Updated 28 Apr 2025

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[EXACT](https://exceljet.net/functions/exact-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7612/download?token=9MZaB1UG)
 (14.3 KB)

![Excel formula: Sum if case-sensitive](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_case_sensitive.png "Excel formula: Sum if case-sensitive")

Summary
-------

To calculate a case-sensitive "sum if", you can use a formula based on the [EXACT function](https://exceljet.net/functions/exact-function)
 and the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in F5, copied down, is:

    =SUMPRODUCT(--EXACT(E5,code)*qty)
    

Where **code** (B5:B15) and **qty** (C5:C15) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is a case-sensitive sum of quantities for each code listed in column E.

Generic formula
---------------

    =SUMPRODUCT(--EXACT(A1,range1)*range2)

Explanation 
------------

In this example, the goal is to sum the quantities in column C by the codes in column E in a case-sensitive manner. The [SUMIF function](https://exceljet.net/functions/sumif-function)
 and the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 are both good options for counting text values, and both functions support [wildcards](https://exceljet.net/glossary/wildcard)
. However, neither function is case-sensitive, so they can't be used to solve this problem. A good solution is to use the [EXACT function](https://exceljet.net/functions/exact-function)
 with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
, as explained below.

### Unique values

To generate the list of unique values in the range E5:E8, you would normally use the [UNIQUE function](https://exceljet.net/videos/the-unique-function)
. However, UNIQUE is not case-sensitive, so it will not work in this situation. [This article](https://exceljet.net/formulas/unique-values-case-sensitive)
 provides a formula that can extract unique values from a range of cells, taking into account upper and lowercase characters.

### EXACT function

The EXACT function has just one purpose: to compare text in a case-sensitive manner. EXACT takes two [arguments](https://exceljet.net/glossary/function-argument)
: _text1_ and _text2._ If _text1_ and _text2_ match exactly (considering upper and lower case), EXACT returns TRUE. Otherwise, EXACT returns FALSE:

    =EXACT("abc","abc") // returns TRUE
    =EXACT("abc","ABC") // returns FALSE
    =EXACT("abc","Abc") // returns FALSE
    =EXACT("ABC","ABC") // returns TRUE
    

### Worksheet example

In the example shown, we have four codes in column E, and we want to sum the values in column C using the codes that appear in column B. In other words, we want to sum the total quantity per code, and this calculation needs to be case-sensitive. For convenience, **code** (B5:B15) and **qty** (C5:C15) are [named ranges](https://exceljet.net/glossary/named-range)
. The formula in E5, copied down, is:

    =SUMPRODUCT(--EXACT(E5,code)*qty)
    

Working from the inside-out, we are using the [EXACT function](https://exceljet.net/functions/exact-function)
 to compare each code in column E with the [named range](https://exceljet.net/glossary/named-range)
 **code** (B5:B15):

    --EXACT(E5,code)
    

EXACT compares the value in E5 ("ABC") to _all_ values in B5:B15. Because the range contains 11 cells, EXACT returns 11 results (one for each code) in an [array](https://exceljet.net/glossary/array)
 like this:

    --{TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE}
    

Each TRUE represents an exact match of "ABC" in B5:B15. Each FALSE represents a non-match. Next, we use a [double-negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) operation to convert TRUE and FALSE values into 1's and 0's. The resulting array looks like this:

    {1;0;0;0;0;0;0;1;1;0;1} // 11 results
    

Note: technically, the double negative (--) is _unnecessary_ in this formula, because multiplying the TRUE and FALSE values by the numeric values in **qty** will _automatically_ convert TRUE and FALSE values to 1s and 0s. However, the double negative does no harm, and it makes the formula a bit easier to understand, because it signals a [Boolean operation](https://exceljet.net/videos/boolean-operations-in-array-formulas)
.

Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

At this point, we can simplify the formula like this:

    =SUMPRODUCT({1;0;0;0;0;0;0;1;1;0;1}*qty)

Next, we need to perform the multiplication step and sum things up.

### SUMPRODUCT function

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 is a versatile function that appears in many formulas because it can handle [array operations](https://exceljet.net/glossary/array-operation)
 natively in older versions of Excel. In this case, the array operation is performed by the EXACT function in the previous step. The remaining steps look like this:

    =SUMPRODUCT({1;0;0;0;0;0;0;1;1;0;1}*qty)
    =SUMPRODUCT({1;0;0;0;0;0;0;1;1;0;1}*{5;1;3;7;6;7;2;2;9;2;3})
    =SUMPRODUCT({5;0;0;0;0;0;0;2;9;0;3})
    =19
    

As you can see, the array returned by EXACT behaves like a filter that "cancels out" values in **qty** that are _not_ associated with the code "ABC". With just one array to process in the end, SUMPRODUCT sums all numbers in the array and returns the final result: 19. As the formula is copied down, we get the correct sum for each code in column E, taking into account upper and lower case characters.

_Note: Because SUMPRODUCT can handle arrays natively, it is not necessary to use Control+Shift+Enter to enter this formula. In_ [_Excel 365_](https://exceljet.net/glossary/excel-365)
_, you can replace SUMPRODUCT with the_ [_SUM function_](https://exceljet.net/functions/sum-function)
_. To read more about this, see_ [_Why SUMPRODUCT?_](https://exceljet.net/articles/why-sumproduct)

Related formulas
----------------

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

[![Excel formula: Sum if cells are equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_equal_to.png "Excel formula: Sum if cells are equal to")](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

### [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when cells in the range C5:C15 contain "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only a single condition. SUMIFS on the other...

[![Excel formula: Count cells that contain case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20case%20sensitive.png "Excel formula: Count cells that contain case sensitive")](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)

### [Count cells that contain case sensitive](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)

In this example, the goal is to count codes that appear as substrings in a case-sensitive way. The functions COUNTIF and COUNTIFS are both good options for counting text values, but these functions are not case-sensitive, so they can't be used to solve this problem. The solution is to use the FIND...

[![Excel formula: Count cells that contain case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20case%20sensitive.png "Excel formula: Count cells that contain case sensitive")](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)

### [Count cells that contain case sensitive](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)

In this example, the goal is to count codes that appear as substrings in a case-sensitive way. The functions COUNTIF and COUNTIFS are both good options for counting text values, but these functions are not case-sensitive, so they can't be used to solve this problem. The solution is to use the FIND...

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

*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    
*   [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)
    
*   [Count cells that contain case sensitive](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)
    
*   [Count cells that contain case sensitive](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)
    

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