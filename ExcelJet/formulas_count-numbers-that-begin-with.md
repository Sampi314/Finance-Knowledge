# Count numbers that begin with - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-numbers-that-begin-with

---

[Skip to main content](https://exceljet.net/formulas/count-numbers-that-begin-with#main-content)

[](https://exceljet.net/formulas/count-numbers-that-begin-with#)

*   [Previous](https://exceljet.net/formulas/count-numbers-by-range)
    
*   [Next](https://exceljet.net/formulas/count-numbers-with-leading-zeros)
    

[Count](https://exceljet.net/formulas#Count)

Count numbers that begin with
=============================

by Dave Bruns · Updated 21 Aug 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[LEFT](https://exceljet.net/functions/left-function)

[LEN](https://exceljet.net/functions/len-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Count numbers that begin with](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20numbers%20that%20begin%20with.png "Excel formula: Count numbers that begin with")

Summary
-------

To count numbers in a range that begin with specific numbers, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in E5 is:

    =SUMPRODUCT(--(LEFT(data,LEN(D5))=D5))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15 and the numbers in column D are entered as [text values](https://exceljet.net/glossary/text-value)
.

Generic formula
---------------

    =SUMPRODUCT(--(LEFT(range,2)="xx"))

Explanation 
------------

In this example, the goal is to count numbers in the range B5:B15 ([named](https://exceljet.net/glossary/named-range)
 **data**) that begin with the numbers shown in column D. You would think this would be a good problem to solve with the COUNTIF function but for reasons explained below, COUNTIF won't work. Instead, you can use the SUMPRODUCT and [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. See below for a full explanation.

### COUNTIF function

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 returns the count of cells that meet one or more criteria, and supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. You would think you could use the COUNTIF function with the asterisk wildcard (\*) like this:

    =COUNTIF(data,"25*") // returns 0
    

The problem however is using any wildcard character means _criteria_ must be handled as a text value in double quotes ("") whereas the values in column B are TRUE numbers. As a result, COUNTIF will never find a matching number and the result will always be zero. You might also think of this trick to coerce the numbers in **data** to text by [concatenating](https://exceljet.net/glossary/concatenation)
 an [empty string](https://exceljet.net/glossary/empty-string)
 ("") to the range like this:

    =COUNTIF(data&"","25*") // throws error
    

But this will throw an error, because COUNTIF is in a [group of eight functions that require an actual range](https://exceljet.net/articles/excels-racon-functions)
 for _range_ arguments. In other words, you can't use an [array operation](https://exceljet.net/glossary/array-operation)
 in place of a _range_ argument.

### SUMPRODUCT function

Another way to solve this problem is with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
, the [LEFT function](https://exceljet.net/functions/left-function)
, and [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. To count numbers in **data** that begin with 25, we can use a formula like this:

    =SUMPRODUCT(--(LEFT(data,2)="25")) // returns 5
    

Working from the inside out, the LEFT function is used to check all numbers in **data** like this:

    LEFT(data,2)="25"
    

Because we give LEFT 11 numbers in the range B5:B15, LEFT returns an [array](https://exceljet.net/glossary/array)
 with 11 results:

    {"25";"25";"35";"45";"25";"45";"25";"45";"25";"35";"55"}="25"
    

We then compare each value to "25" to force a TRUE or FALSE result. Note that LEFT automatically converts the numbers to text, so we use the text value "25" for the comparison. The result is an array of TRUE and FALSE values:

    {TRUE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE}
    

In this array, TRUE values correspond to numbers that begin with "25" and FALSE values represent numbers that don't. We want to count these results, but first we need to convert the TRUE and FALSE values to 1s and 0s. To do this, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--).

    --{TRUE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE}
    

The resulting array contains only 1s and 0s and is delivered directly to the SUMPRODUCT function:

    =SUMPRODUCT({1;1;0;0;1;0;1;0;1;0;0})
    

With only a single array to process, SUMPRODUCT sums the items in the array and returns 5 as result. In this formula, note we are hardcoding the value "25" and the length of 2. To adapt the formula for the worksheet shown, where the numbers we want to count appear in column D, we use the LEN function and a reference to cell D5 like this:

    =SUMPRODUCT(--(LEFT(data,LEN(D5))=D5))
    

The [LEN function](https://exceljet.net/functions/len-function)
 returns the number of characters in D5. This makes the formula more generic so it will support numbers of different lengths. Also note that the numbers in column D are entered as text values, since the result from LEFT will also be text. You can avoid this requirement by adapting the formula to coerce the value in D5 to text:

    =SUMPRODUCT(--(LEFT(data,LEN(D5))=D5&""))
    

Here we [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 an empty string ("") to the D5, which converts any number to text. This version of the formula will work when there are numbers in column D, or text values.

_Note: In Excel 365 and Excel 2021 you can use the [SUM function](https://exceljet.net/functions/sum-function)
 instead of SUMPRODUCT if you prefer. [This article provides more detail](https://exceljet.net/articles/why-sumproduct)
._

Related formulas
----------------

[![Excel formula: Count cells that contain positive numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cell%20that%20contain%20positive%20numbers.png "Excel formula: Count cells that contain positive numbers")](https://exceljet.net/formulas/count-cells-that-contain-positive-numbers)

### [Count cells that contain positive numbers](https://exceljet.net/formulas/count-cells-that-contain-positive-numbers)

In this example, the goal is to count the number of cells in a range that contain positive numbers. For convenience, the range B5:B15 is named data . This problem can be solved with the COUNTIF function or the SUMPRODUCT function. Both methods are explained below. COUNTIF function The COUNT...

[![Excel formula: Count cells between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20two%20numbers_0.png "Excel formula: Count cells between two numbers")](https://exceljet.net/formulas/count-cells-between-two-numbers)

### [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)

In this example, the goal is to count numbers that fall within specific ranges. The lower value comes from the "Start" column, and the upper value comes from the "End" column. For each range, we want to include both the lower value and the upper value. For convenience, the numbers being counted are...

[![Excel formula: Count cells that contain odd numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20odd%20numbers.png "Excel formula: Count cells that contain odd numbers")](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)

### [Count cells that contain odd numbers](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)

In this example, the goal is to count odd numbers in the range B5:B15, which is named data . This can be done with the SUMPRODUCT function together with the ISODD function. Instead of ISODD, the MOD function can also be used. Both approaches are explained below. SUMPRODUCT with ISODD The SUMPRODUCT...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

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

*   [Count cells that contain positive numbers](https://exceljet.net/formulas/count-cells-that-contain-positive-numbers)
    
*   [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)
    
*   [Count cells that contain odd numbers](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

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