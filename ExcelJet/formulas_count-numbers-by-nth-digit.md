# Count numbers by nth digit - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-numbers-by-nth-digit

---

[Skip to main content](https://exceljet.net/formulas/count-numbers-by-nth-digit#main-content)

[](https://exceljet.net/formulas/count-numbers-by-nth-digit#)

*   [Previous](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/count-numbers-by-range)
    

[Count](https://exceljet.net/formulas#Count)

Count numbers by nth digit
==========================

by Dave Bruns · Updated 21 Aug 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[MID](https://exceljet.net/functions/mid-function)

![Excel formula: Count numbers by nth digit](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20numbers%20by%20nth%20digit.png "Excel formula: Count numbers by nth digit")

Summary
-------

To count numbers where the nth digit is a specific number, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in E5 is:

    =SUMPRODUCT(--(MID(data,3,1)=D5))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15 and the numbers in column D are entered as [text values](https://exceljet.net/glossary/text-value)
.

Generic formula
---------------

    =SUMPRODUCT(--(MID(range,n,1)="x"))

Explanation 
------------

In this example, the goal is to count numbers in the range B5:B15 ([named](https://exceljet.net/glossary/named-range)
 **data**) where the third digit is a specific number, indicated in column D. You might think the COUNTIF function would be a good way to solve this problem. However, for reasons explained below, COUNTIF won't work. Instead, you can use the SUMPRODUCT and [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. See below for a full explanation.

### COUNTIF function

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 returns the count of cells that meet one or more criteria, and supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. You would think you could use the COUNTIF function with the question mark (?) and asterisk (\*) wildcards to count numbers where the third digit is 1 like this:

    =COUNTIF(data,"??1*") // returns 0
    

However, COUNTIF will return zero. The problem is that using any wildcard in _criteria_ means that COUNTIF will interpret the pattern as a text value, whereas the values in column B are _numeric_. As a result, COUNTIF will never find a matching number and the result will always be zero. As a workaround, you might try the trick below to coerce the numbers in **data** to text by [concatenating](https://exceljet.net/glossary/concatenation)
 an [empty string](https://exceljet.net/glossary/empty-string)
 ("") to the range like this:

    =COUNTIF(data&"","???1") // throws error
    

However, this will cause Excel to throw the generic "There's a problem with this formula" error, so it's not possible to even enter the formula. This happens because COUNTIF is in a [group of eight functions that require an actual range](https://exceljet.net/articles/excels-racon-functions)
 for _range_ arguments. This means you can't use an [array operation](https://exceljet.net/glossary/array-operation)
 to modify the _range_ argument inside COUNTIF, COUNTIFS, SUMIF, SUMIFS, etc.

### SUMPRODUCT function

Another way to solve this problem is with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
, the [MID function](https://exceljet.net/functions/mid-function)
, and [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. To count numbers in **data** where the third digit is 1, we can use SUMPRODUCT like this:

    =SUMPRODUCT(--(MID(data,3,1)="1")) // returns 2
    

Working from the inside out, the MID function is used to extract and test the third digit from the numbers in **data** like this:

    MID(data,3,1)="1"
    

Because we give MID 11 numbers in the range B5:B15, MID returns an [array](https://exceljet.net/glossary/array)
 with 11 results:

    {"3";"4";"5";"2";"3";"2";"4";"1";"3";"3";"1"}="25"
    

Note that MID automatically converts the numbers to text, so we use the text value "1" for the comparison. The result is an array of TRUE and FALSE values:

    {FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE}
    

In this array, TRUE values correspond to numbers where the third digit is 3. We want to count these results, but first we need to convert the TRUE and FALSE values to 1s and 0s. To do this, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--).

    --{FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE}
    

The resulting array contains only 1s and 0s and is delivered directly to the SUMPRODUCT function:

    =SUMPRODUCT({0;0;0;0;0;0;0;1;0;0;1})
    

With only a single array to process, SUMPRODUCT sums the items in the array and returns 2 as result. In this formula, note we are hardcoding the value "1" and we set _num\_chars_ to 1 inside the MID function. To adapt the formula for the worksheet shown, we a reference to cell D5 like this:

    =SUMPRODUCT(--(MID(data,3,1)=D5))
    

As the formula is copied down, it returns the count of numbers in **data** where the third digit equals the numbers in column D. Note that the numbers in column D are entered as [text values](https://exceljet.net/glossary/text-value)
, since the result from MID will also be text. You can avoid this requirement by adapting the formula to coerce the value in D5 to text:

    =SUMPRODUCT(--(MID(data,3,1)=D5&""))
    

Here we [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 an empty string ("") to the D5, which will convert a numeric value to text. This version of the formula will work when there are numbers in column D, or text values.

_Note: In Excel 365 and Excel 2021 you can use the [SUM function](https://exceljet.net/functions/sum-function)
 instead of SUMPRODUCT if you prefer. [This article provides more detail](https://exceljet.net/articles/why-sumproduct)
._

Related formulas
----------------

[![Excel formula: Count cells that contain n characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20n%20characters.png "Excel formula: Count cells that contain n characters")](https://exceljet.net/formulas/count-cells-that-contain-n-characters)

### [Count cells that contain n characters](https://exceljet.net/formulas/count-cells-that-contain-n-characters)

In this example, the goal is to count the number of cells in B5:B15 that contain a given number of characters, where the number of characters n is provided as a variable in cell E4. SUMPRODUCT with LEN One way to solve this problem is to use the SUMPRODUCT function with the LEN function . In the...

[![Excel formula: Count specific characters in text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_specific_characters_in_text.png "Excel formula: Count specific characters in text string")](https://exceljet.net/formulas/count-specific-characters-in-text-string)

### [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)

In this example, the goal is to count the number of occurrences of a character in a cell or text string. Strangely, Excel does not have a function dedicated to counting characters, so we need to use a formula that computes a count manually. The typical way to do this is to use a formula based on...

[![Excel formula: Count cells that begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20begin%20with.png "Excel formula: Count cells that begin with")](https://exceljet.net/formulas/count-cells-that-begin-with)

### [Count cells that begin with](https://exceljet.net/formulas/count-cells-that-begin-with)

In this example, the goal is to count cells in the range B5:B16 that begin with specific text, which is provided in column D. For convenience, the range B5:B16 is named data . COUNTIF function The simplest way to solve this problem is with the COUNTIF function and a wildcard. COUNTIF supports three...

[![Excel formula: Count numbers that begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20numbers%20that%20begin%20with.png "Excel formula: Count numbers that begin with")](https://exceljet.net/formulas/count-numbers-that-begin-with)

### [Count numbers that begin with](https://exceljet.net/formulas/count-numbers-that-begin-with)

In this example, the goal is to count numbers in the range B5:B15 ( named data ) that begin with the numbers shown in column D. You would think this would be a good problem to solve with the COUNTIF function but for reasons explained below, COUNTIF won't work. Instead, you can use the SUMPRODUCT...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain n characters](https://exceljet.net/formulas/count-cells-that-contain-n-characters)
    
*   [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)
    
*   [Count cells that begin with](https://exceljet.net/formulas/count-cells-that-begin-with)
    
*   [Count numbers that begin with](https://exceljet.net/formulas/count-numbers-that-begin-with)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    

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