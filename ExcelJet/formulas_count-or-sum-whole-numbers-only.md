# Count or sum whole numbers only - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-or-sum-whole-numbers-only

---

[Skip to main content](https://exceljet.net/formulas/count-or-sum-whole-numbers-only#main-content)

[](https://exceljet.net/formulas/count-or-sum-whole-numbers-only#)

*   [Previous](https://exceljet.net/formulas/count-or-sum-variance)
    
*   [Next](https://exceljet.net/formulas/count-paired-items-in-listed-combinations)
    

[Count](https://exceljet.net/formulas#Count)

Count or sum whole numbers only
===============================

by Dave Bruns · Updated 15 Jun 2022

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6732/download?token=DTX3YXBP)
 (15.08 KB)

![Excel formula: Count or sum whole numbers only](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20or%20sum%20whole%20numbers%20only.png "Excel formula: Count or sum whole numbers only")

Summary
-------

To count or sum values that are whole numbers, you can use a formula based on the [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 and [MOD](https://exceljet.net/functions/mod-function)
 functions. In the example shown, the formula in G5 is:

    =SUMPRODUCT(--(MOD(shares,1)=0))
    

where **shares** is the [named range](https://exceljet.net/glossary/named-range)
 C5:C15.

Generic formula
---------------

    =SUMPRODUCT(--(MOD(range,1)=0))

Explanation 
------------

In this example, the goal is to get a count of people that hold shares in whole numbers. For example, Bob holds 100 shares (even), so he _should_ be included in the whole number count, while Cindy holds 50.5 shares, so she _should not_ be included in the whole number count.

The first problem is how to determine whole numbers. This can be done with the [INT](https://exceljet.net/functions/int-function)
, [TRUNC](https://exceljet.net/functions/trunc-function)
, or MOD functions [as explained in detail here](https://exceljet.net/formulas/number-is-whole-number)
. In this example shown above, we are using the [MOD function](https://exceljet.net/functions/mod-function)
 option:

    =MOD(A1,1)=0 // TRUE for whole numbers
    

Now that we know how to test for a whole number, how can we use this approach to get a _count_ of whole numbers? You might at first be tempted to use the [COUNTIF](https://exceljet.net/functions/countif-function)
 or [COUNTIFS](https://exceljet.net/functions/countifs-function)
 functions. However, these functions won't let you use an [array](https://exceljet.net/glossary/array)
\* in place of the _range_ argument, so COUNTIF won't work:

    =COUNTIF(MOD(shares,1),0) // won't work!
    

_\* MOD(shares,1) is technically an [array operation](https://exceljet.net/glossary/array-operation)
 that returns an array of values. [See this article for more information](https://exceljet.net/articles/excels-racon-functions)
 about limitations in COUNTIF, SUMIF, etc._

Instead, we need a way to work with the array directly with [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. Boolean logic is a technique for building formulas that take advantage of the fact that TRUE = 1, and FALSE = 0 in math operations.  In the example shown, this is what the formula in G5 does:

    =SUMPRODUCT(--(MOD(shares,1)=0))
    

Working from the inside out, we first run all values through the MOD test shown above:

    =MOD(shares,1)=0 // test all values
    

Because there are eleven values in **shares** (C5:C15), we get eleven results in an [array](https://exceljet.net/glossary/array)
 like this:

    {TRUE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;TRUE;TRUE}
    

In this array, TRUE values represent a whole number, and FALSE values represent a decimal number. Next, we need to convert the TRUE and FALSE values to 1s and 0s. To do this, we use a [double-negative](https://exceljet.net/glossary/double-unary)
 (--):

    --{TRUE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;TRUE;TRUE}
    

This operation returns a numeric array composed only of 1s and 0s:

    {1;0;0;1;1;1;1;0;0;1;1}
    

This is exactly what we need to count whole numbers. This array is returned directly to the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
:

    =SUMPRODUCT({1;0;0;1;1;1;1;0;0;1;1}) // returns 7
    

With just one array to process, SUMPRODUCT returns the sum of all items in the array, 7, which is the count of whole numbers in the range C5:C15.

### Count decimal values

To change the formula to count numbers with decimal values, we only need to change the [logical operator](https://exceljet.net/glossary/logical-operators)
 in the MOD snippet from an equal sign (=) to the not equal to (<>) operator. The formula in G6:

    =SUMPRODUCT(--(MOD(shares,1)<>0)) // returns 4
    

Note the only change to the formula is the logical operator.

### Sum whole number shares

To sum whole numbers only, we need to extend the formula a bit by multiplying the Boolean array explained above by the values in the [named range](https://exceljet.net/glossary/named-range)
 **shares.** The formula in H5 calculates the total number of shares in the whole number group:

    =SUMPRODUCT(--(MOD(shares,1)=0)*shares)
    

Notice the formula is _almost_ the same as above. The result is that the zero values effectively cancel out the shares in the decimal group:

    =SUMPRODUCT(--(MOD(shares,1)=0)*shares)
    =SUMPRODUCT({1;0;0;1;1;1;1;0;0;1;1}*{100;50.5;110.75;25;50;75;50;60.25;120.75;100;50})
    =SUMPRODUCT({100;0;0;25;50;75;50;0;0;100;50})
    =450
    

### Sum whole number share values

To sum the values associated with whole number shares, we need to adjust the formula again. This time instead of multiplying the Boolean array by **shares**, we multiply by **value**. The formula in I5 is:

    =SUMPRODUCT(--(MOD(shares,1)=0)*value)
    

The formula is solved in exactly the same way:

    =SUMPRODUCT(--(MOD(shares,1)=0)*value)
    =SUMPRODUCT({1;0;0;1;1;1;1;0;0;1;1}*{2500;1262.5;2768.75;625;1250;1875;1250;1506.25;3018.75;2500;1250})
    =SUMPRODUCT({2500;0;0;625;1250;1875;1250;0;0;2500;1250})
    =11250
    

As above, the zero values in the Boolean array cancel out values for non-whole number shares, and the final result returned by SUMPRODUCT is 11250.

### SUM or SUMPRODUCT?

Why are we using SUMPRODUCT and not the [SUM function](https://exceljet.net/functions/sum-function)
? It's a good question.

In older versions of Excel (anything but [Excel 365](https://exceljet.net/glossary/excel-365)
) the same formula with SUM works, but must be entered as an [array formula](https://exceljet.net/glossary/array-formula)
 with Control + Shift + Enter. In Excel 365, SUM will _just work_, since [Excel 365 handles arrays natively](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. Using SUMPRODUCT ensures that the formula will work in all versions of Excel without requiring Control + Shift + Enter. For more details, see [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)

Related formulas
----------------

[![Excel formula: Number is whole number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/number%20is%20whole%20number.png "Excel formula: Number is whole number")](https://exceljet.net/formulas/number-is-whole-number)

### [Number is whole number](https://exceljet.net/formulas/number-is-whole-number)

In this example, the goal is to test if a numeric value is a whole number. There are several ways to go about this. One of the easiest ways is to use the MOD function with a divisor of 1. Any whole number divided by 1 will result in a remainder of zero: =MOD(5,1)=0 // whole numbers return zero Any...

[![Excel formula: Highlight integers only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20integers%20only.png "Excel formula: Highlight integers only")](https://exceljet.net/formulas/highlight-integers-only)

### [Highlight integers only](https://exceljet.net/formulas/highlight-integers-only)

The MOD function returns the remainder after division. With a divisor of 1, MOD will return zero for any whole number. We use this fact to construct a simple formula that tests the result of MOD. When the result is zero (i.e. when the number is an integer) the formula returns TRUE, triggering the...

[![Excel formula: Get integer part of a number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20integer%20part%20of%20a%20number.png "Excel formula: Get integer part of a number")](https://exceljet.net/formulas/get-integer-part-of-a-number)

### [Get integer part of a number](https://exceljet.net/formulas/get-integer-part-of-a-number)

With TRUNC, no rounding takes place. The TRUNC function simply slices off the decimal part of the number with default settings. TRUNC actually takes an optional second argument to specify the precision of truncation, but when you don't supply this optional argument, it is assumed to be zero, and...

[![Excel formula: Extract date from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20date%20from%20date%20and%20time.png "Excel formula: Extract date from a date and time")](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

### [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

Excel handles dates and time using a scheme in which dates are serial numbers and times are fractional values . For example, June 1, 2000 12:00 PM is represented in Excel as the number 36678.5, where 36678 is the date portion and .5 is the time portion. If you have dates that include time, you can...

Related functions
-----------------

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

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

*   [Number is whole number](https://exceljet.net/formulas/number-is-whole-number)
    
*   [Highlight integers only](https://exceljet.net/formulas/highlight-integers-only)
    
*   [Get integer part of a number](https://exceljet.net/formulas/get-integer-part-of-a-number)
    
*   [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)
    

### Functions

*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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