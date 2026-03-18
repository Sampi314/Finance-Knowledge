# Count numbers with leading zeros - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-numbers-with-leading-zeros

---

[Skip to main content](https://exceljet.net/formulas/count-numbers-with-leading-zeros#main-content)

[](https://exceljet.net/formulas/count-numbers-with-leading-zeros#)

*   [Previous](https://exceljet.net/formulas/count-numbers-that-begin-with)
    
*   [Next](https://exceljet.net/formulas/count-occurrences-in-entire-workbook)
    

[Count](https://exceljet.net/formulas#Count)

Count numbers with leading zeros
================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMIF](https://exceljet.net/functions/sumif-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7242/download?token=KRqVf633)
 (17.5 KB)

![Excel formula: Count numbers with leading zeros](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20numbers%20with%20leading%20zeros.png "Excel formula: Count numbers with leading zeros")

Summary
-------

To count numbers that contain leading zeros, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 with a simple logical expression. In the example shown, the formula in cell F5 is:

    =SUMPRODUCT(--(code=E5))
    

where **code** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16.

Generic formula
---------------

    =SUMPRODUCT(--(range=value))

Explanation 
------------

In this example, the goal is to count numbers that contain leading zeros. In cell E5, we have the code "009875" and we want to count how many times this code appears in the range B5:B16. The challenge is that Excel can be finicky with leading zeros. Technically, the values in B5:B16 are [text](https://exceljet.net/glossary/text-value)
, as is the value in E5. However, sometimes text values that contain numbers are converted to _numeric_ values as they go through Excel's calculation engine. When this happens, the leading zeros will be silently removed, which can cause an incorrect result. The article below explains the problem in more detail. For convenience, **code** (B5:B16) and **qty** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
.

### COUNTIF with leading zeros

A common situation where leading zeros do not behave as expected is when functions like [COUNTIF](https://exceljet.net/functions/countif-function)
, [COUNTIFS](https://exceljet.net/functions/countifs-function)
, [SUMIF](https://exceljet.net/functions/sumif-function)
, [SUMIFS](https://exceljet.net/functions/sumifs-function)
, etc. are configured to use numbers with leading zeros. To demonstrate this problem, consider the formula below:

![COUNTIF with leading zeros does not work](https://exceljet.net/sites/default/files/images/formulas/inline/COUNTIF%20with%20leading%20zeros.png "COUNTIF with leading zeros does not work")

Here the [COUNTIF function](https://exceljet.net/functions/countif-function)
 is set up to count values in B4:B8 that are _equal_ to "01". We expect a result of 1, but COUNTIF returns 5.

    =COUNTIF(B4:B8,"01") // returns 5
    

Somewhere in the calculation process, the leading zeros get dropped and all cells evaluate to 1. This is clearly not the result we want, and shows a limitation of the COUNTIF function. Similarly, if we apply COUNTIF to the worksheet shown above, we get the incorrect result of 4:

    =COUNTIF(code,E5) // returns 4
    

The leading zeros in "009875" are stripped, and 9875 is counted 4 times, when the correct result for "009875"is 2.

_Note: COUNTIF is in a [group of 8 functions](https://exceljet.net/articles/excels-racon-functions)
 that share some particular quirks and limitations._

### SUMPRODUCT solution

A simple solution to this problem is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 like this:

    =SUMPRODUCT(--(code=E5))
    

Working from the inside out, we are using the following expression as a [logical test](https://exceljet.net/glossary/logical-test)
:

    code=E5
    

Because **code** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16, which contains 12 values, the expression yields 12 TRUE/FALSE results in an [array](https://exceljet.net/glossary/array)
 like this:

    {FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE}
    

The TRUE values in the array correspond to the cells in B5:B16 that contain "009875". You can see we have TRUE at the fourth cell (B8) and the ninth cell (B13).

Next, we use a [double negative](https://exceljet.net/glossary/double-unary)
 (--) to coerce the TRUE/FALSE values to 1s and 0s, which creates the following array:

    {0;0;0;1;0;0;0;0;1;0;0;0}
    

This array is delivered directly to the SUMPRODUCT function, which sums the array and returns a final result:

    =SUMPRODUCT({0;0;0;1;0;0;0;0;1;0;0;0}) // returns 2
    

This is an example of using [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
, and you will see many more advanced formulas use this technique. The nice thing about this approach is that it can be easily extended, as explained below.

### Sum quantities

As you might have guessed, if you try to use the [SUMIF function](https://exceljet.net/functions/sumif-function)
 to sum the quantities associated with code "009875", the same problem will occur. The formula below returns 14, when the correct result is 7:

    =SUMIF(code,E5,qty) // returns 14
    

The cause of the problem is the same: the leading zeros in "009875" get stripped during the SUMIF calculation, which causes "009875" to be grouped together with "9875", and SUMIF sums the quantities associated with both codes.

One of the nicest things about using SUMPRODUCT to perform conditional counts as we did above, is that we can easily extend the logic to perform conditional sums. In this case, all we need to do is multiply the counting logic by the [named range](https://exceljet.net/glossary/named-range)
 **qty** (C5:C16) like this:

    =SUMPRODUCT(--(code=E5)*qty)
    

This is the formula used in cell G5 of the worksheet. Since we already know that the expression:

    --(code=E5)
    

results in an array of 1s and 0s, we can simplify the formula like this:

    =SUMPRODUCT({0;0;0;1;0;0;0;0;1;0;0;0}*qty)
    

Then, evaluating quantities (**qty**), we get:

    =SUMPRODUCT({0;0;0;1;0;0;0;0;1;0;0;0}*{3;6;4;2;5;6;2;4;5;1;3;3})
    

After the two arrays are multiplied together we have:

    =SUMPRODUCT({0;0;0;2;0;0;0;0;5;0;0;0}) // returns 7
    

Notice how the zeros in the first array "cancel out" the irrelevant quantities in the second array. In other words, the exact same logic we used to count code "009875" is used to sum quantities associated with code "009875". The final result from SUMPRODUCT is 7.

SUMPRODUCT is a workhorse function that can solve many tricky problems in Excel. See [more examples here](https://exceljet.net/functions/sumproduct-function)
.

_Note: technically the double negative (--) is not needed in the formula to sum quantities above because the math operation of multiplying the two arrays together will automatically coerce the TRUE and FALSE values in the first arrays with 1s and 0s. However, the double negative does no harm and makes the counting and summing formulas easier to compare._

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

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    

### Training

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