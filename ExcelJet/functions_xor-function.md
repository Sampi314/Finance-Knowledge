# Excel XOR function | Exceljet

**Source:** https://exceljet.net/functions/xor-function

---

[Skip to main content](https://exceljet.net/functions/xor-function#main-content)

[](https://exceljet.net/functions/xor-function#)

*   [Previous](https://exceljet.net/functions/true-function)
    
*   [Next](https://exceljet.net/functions/date-function)
    

Excel 2013

[Logical](https://exceljet.net/functions#Logical)

XOR Function
============

by Dave Bruns · Updated 13 Nov 2022

Related functions 
------------------

[OR](https://exceljet.net/functions/or-function)

[NOT](https://exceljet.net/functions/not-function)

[AND](https://exceljet.net/functions/and-function)

[IF](https://exceljet.net/functions/if-function)

![Excel XOR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20xor.png "Excel XOR function")

Summary
-------

The XOR function performs what is called "exclusive OR". With two logical statements, XOR returns TRUE if either statement is TRUE, but returns FALSE if both statements are TRUE. If neither is TRUE, XOR also returns FALSE.

Purpose 
--------

Perform exclusive OR

Return value 
-------------

TRUE or FALSE

Syntax
------

    =XOR(logical1,[logical2],...)

*   _logical1_ - An expression, constant, or reference that evaluates to TRUE or FALSE.
*   _logical2_ - \[optional\] An expression, constant, or reference that evaluates to TRUE or FALSE.

Using the XOR function 
-----------------------

The XOR function performs what is called "exclusive OR", in contrast to the "inclusive OR" performed by the [OR function](https://exceljet.net/functions/or-function)
. Whereas the OR function returns true if _any_ input is TRUE, XOR only returns TRUE in specific cases. In the simplest case, with just two logical statements, XOR returns TRUE only if one of the logicals is TRUE. If both values are TRUE, XOR returns FALSE.

The concept of exclusive OR is more common in the world of programming. In plain English, you can think of a sentence like this: "I'm either going to visit New York or San Francisco this summer". Nothing prevents the speaker from visiting both, but the meaning is clearly that they plan to visit only one or the other. If they visit one or the other, the original statement is TRUE. If they visit neither or both, the original statement is FALSE.

### Example #1 - two values

In the example shown, the formula in D5, copied down, is:

    =XOR(B5,C5)
    

At each row, XOR only returns TRUE when B5 and C5 contain a single TRUE or equivalent value.

### Example #2 - more than two values

With more than 2 values, the behavior of XOR is a bit different. With three or more logicals, XOR only returns TRUE when the number of TRUE values is odd, as shown in the following example:

![XOR with more than two logicals](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_xor_example2.png "XOR with more than two logicals")

In this example, XOR is given a range with five values in a single [argument](https://exceljet.net/glossary/function-argument)
 instead of five separate arguments. The formula in G6 copied down is:

    =XOR(B6:F6)
    

The result is TRUE only when the number of TRUE values columns B through F is an odd number.

### Notes

*   Logical arguments must evaluate to TRUE or FALSE, 1 or 0, or be references that contain logical values.
*   XOR returns #VALUE! if no logical values are found.
*   With more than two logicals, XOR returns TRUE when the number of TRUE logicals is odd, and FALSE if not.
*   XOR was introduced in Excel 2013.

XOR function examples
---------------------

[![Excel formula: One or the other not both](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/one%20or%20the%20other%20not%20both.png "Excel formula: One or the other not both")](https://exceljet.net/formulas/one-or-the-other-not-both)

### [One or the other not both](https://exceljet.net/formulas/one-or-the-other-not-both)

In this example, the XOR function contains two expressions, one to test for an "x" in column C, and one to test for an "x" in column D. C5="x" // TRUE if coffee is "x" D5="x" // TRUE if tea is "x" With two logical criteria, XOR has a particular behavior, summarized in the table below: Coffee Tea...

Related functions
-----------------

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [One or the other not both](https://exceljet.net/formulas/one-or-the-other-not-both)
    

### Functions

*   [OR Function](https://exceljet.net/functions/or-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Articles

*   [How to build logical formulas](https://exceljet.net/plc/how-to-build-logical-formulas)
    

### Links

*   [Microsoft XOR function documentation](https://support.office.com/en-us/article/xor-function-1548d4c2-5e47-4f77-9a92-0533bba14f37)
    

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