# Convert inches to feet and inches - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-inches-to-feet-and-inches

---

[Skip to main content](https://exceljet.net/formulas/convert-inches-to-feet-and-inches#main-content)

[](https://exceljet.net/formulas/convert-inches-to-feet-and-inches#)

*   [Previous](https://exceljet.net/formulas/convert-feet-and-inches-to-inches)
    
*   [Next](https://exceljet.net/formulas/convert-negative-numbers-to-zero)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Convert inches to feet and inches
=================================

by Dave Bruns · Updated 17 Jan 2025

Related functions 
------------------

[INT](https://exceljet.net/functions/int-function)

[MOD](https://exceljet.net/functions/mod-function)

[REPT](https://exceljet.net/functions/rept-function)

[ABS](https://exceljet.net/functions/abs-function)

[LET](https://exceljet.net/functions/let-function)

![Excel formula: Convert inches to feet and inches](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Convert%20inches%20to%20feet%20and%20inches.png "Excel formula: Convert inches to feet and inches")

Summary
-------

To convert a measurement in inches to inches and feet (i.e. 53 inches to 4' 5") you can use a formula based on the [INT](https://exceljet.net/functions/int-function)
 and [MOD](https://exceljet.net/functions/mod-function)
 functions. In the example shown, the formula in D5 is:

    =INT(B5/12)&"' "&MOD(B5,12)&""""

As the formula is copied down, it converts the inches in column B to feet and inches. Note that the result is a text string, since we need to embed single (') and double (") quotes. 

Generic formula
---------------

    =INT(A1/12)&"' "&MOD(A1,12)&""""

Explanation 
------------

In this example, the goal is to create a formula that converts a numeric value in inches to a format that displays inches and feet, as seen in the table below:

| Input | Output |
| --- | --- |
| 9   | 0' 9" |
| 12  | 1' 0" |
| 30  | 2' 6" |
| 75  | 6' 3" |

The math for this problem is fairly simple, but the problem is more complex because we need to assemble a text string that includes a single quote for feet (') and a double quote (") for inches. This means we need to [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 numbers after we perform the necessary calculations. The article below explains a basic formula for positive inputs with several variations. It also includes an adjusted formula to handle negative inches and a more modern formula based on the LET function.

### Basic formula

In the worksheet shown above, the formula in cell D5 looks like this:

    =INT(B5/12)&"' "&MOD(B5,12)&""""

This formula converts a numeric value in inches to text representing the same measurement in inches and feet. To get a value for feet, the [INT function](https://exceljet.net/functions/int-function)
 is used like this:

    =INT(B5/12) // get whole feet
    

Inside INT, the value in B5 is divided by 12. The INT function returns the integer portion of a decimal number and discards any decimal remainder. The result from INT is the number of whole feet in B5. To get a value for inches, we use the [MOD function](https://exceljet.net/functions/mod-function)
 like this:

    MOD(B5,12) // get inches
    

The MOD function divides B5 by 12 and returns the remainder, which corresponds to inches.  At this point, we have a number for feet and a number for inches. The remaining task is to concatenate these numbers together into a text string that includes a single quote for feet (') and a double quote (") for inches. We start by adding a single quote with a space to the value for feet:

    =INT(B5/12)&"' "

We add a space to separate the feet from the inches. Then we insert another ampersand (&) and add the MOD part of the formula:

    =INT(B5/12)&"' "&MOD(B5,12)

We finish with two sets of double quotes (""""):

    =INT(B5/12)&"' "&MOD(B5,12)&""""

The outer pair of double quotes tells Excel this is a _text value_. The inner pair of quotes causes Excel to return one double quote ("). Finally, all values are concatenated together, and Excel returns a result.

### Rounded inches

To round inches to a given number of decimal places, wrap the MOD function in the [ROUND function](https://exceljet.net/functions/round-function)
. For example, to round inches to one decimal:

    =INT(A1/12)&"' "&ROUND(MOD(A1,12),1)&""""
    

### With complete labels

To output a value like "8 feet 4 inches", you can adapt the formula like this:

    =INT(B5/12)&" feet "&MOD(B5,12)&" inches"
    

### Negative numbers

We need a different formula to work with negative inches as an input. One solution is to use a formula like this:

    =REPT("-",B5<0)&INT(ABS(B5)/12)&"' "&MOD(ABS(B5),12)&""""
    

This looks pretty complicated, but the core of this formula is almost the same as the original formula above. The difference is that we are using the [ABS function](https://exceljet.net/functions/abs-function)
 to convert the input in cell B5 to a positive number. This needs to happen twice, each time we use B5:

    =INT(ABS(B5)/12)&"' "&MOD(ABS(B5),12)&""""

After ABS runs, the formula works as before and returns a text string indicating feet and inches. The remaining step is to add a negative sign ("-") if the input is indeed negative. We do this with the [REPT function](https://exceljet.net/functions/rept-function)
 at the start of the formula. REPT is designed to repeat text values by providing a number for the second argument, for example:

    =REPT("A",1) // returns "A"
    =REPT("A",2) // returns "AA"
    =REPT("A",3) // returns "AAA"

In our formula, we use REPT in a tricky way like this:

    =REPT("-",B5<0)

When B5 is less than zero, the result is TRUE, which evaluates to 1. When B5 is not less than zero, the result is FALSE, which evaluates to 0. The REPT function only returns "-" when the value is negative, otherwise it returns an empty string. Essentially, the REPT formula mimics this longer IF formula:

     =IF(B5<0,"-","")

The final formula looks like this:

    =REPT("-",B5<0)&INT(ABS(B5)/12)&"' "&MOD(ABS(B5),12)&""""

![Formula adjusted to handle negative inputs](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/convert_inches_to_feet_and_inches_negative.png "Formula adjusted to handle negative inputs")

This formula will now correctly handle positive or negative input values.

> Note: one reason we need to deal with negative numbers differently is that the [INT function](https://exceljet.net/functions/int-function)
> , contrary to its name, actually rounds negative numbers down away from zero. Another approach would be to switch to the [TRUNC function](https://exceljet.net/functions/trunc-function)
> , which just chops off the decimal value and keeps the integer with the sign. I tried that at first, but in the end I decided it made more sense to leave the original formula logic intact and treat the negative sign as a separate step. 

### LET formula option

A problem like this is a perfect candidate for the [LET function](https://exceljet.net/functions/let-function)
, which makes it possible to assign variables inside a formula. Using LET, we can write an all-in-one formula like this:

    =LET(
    input,ABS(B5),
    sign,IF(B5<0,"-",""),
    feet,INT(input/12),
    inches,MOD(input,12),
    sign&feet&"' "&inches&"""")

This may look more complicated at first glance, but if you look closely, you will see that the first four lines create variables (input, sign, feet, inches) in a logical order. The last line concatenates the sign, feet, and inches together and returns the result. We only need to use the ABS function once. This formula will handle positive or negative inputs.

> This version of the formula does not use the REPT trick for the sake of readability, but it could.

Related formulas
----------------

[![Excel formula: Convert feet and inches to inches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20feet%20and%20inches%20to%20inches.png "Excel formula: Convert feet and inches to inches")](https://exceljet.net/formulas/convert-feet-and-inches-to-inches)

### [Convert feet and inches to inches](https://exceljet.net/formulas/convert-feet-and-inches-to-inches)

In this example the goal is to parse feet and inches out in the text strings shown in column B, and create a single numeric value for total inches. The challenge is that each of the two numbers is embedded in text. The formula can be divided into two parts. In the first part of the formula, feet...

[![Excel formula: Split dimensions into three parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_dimensions_into_three_parts.png "Excel formula: Split dimensions into three parts")](https://exceljet.net/formulas/split-dimensions-into-three-parts)

### [Split dimensions into three parts](https://exceljet.net/formulas/split-dimensions-into-three-parts)

In this example, the goal is to split the text strings in column B, which contain three dimensions in the form "L x W x H", into 3 separate dimensions. One problem with dimensions entered as text is that they can't be used for any kind of calculation. So, in addition, we want our final dimensions...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

Related functions
-----------------

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

[![Excel REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rept%20function.png "Excel REPT function")](https://exceljet.net/functions/rept-function)

### [REPT Function](https://exceljet.net/functions/rept-function)

The Excel REPT function repeats characters a given number of times. For example, =REPT("x",5) returns "xxxxx".

[![Excel ABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20abs%20function.png "Excel ABS function")](https://exceljet.net/functions/abs-function)

### [ABS Function](https://exceljet.net/functions/abs-function)

The Excel ABS function returns the absolute value of a number. ABS converts negative numbers to positive numbers, and positive numbers are unaffected.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20complex%20formula%20step%20by%20step-thumb.png)](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

### [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

When you look at a complex formula in Excel you may be completely baffled at first glance, but all complex formulas are just small steps added together. Let me show you an example. Here we have a list of names. We want to pull out the first name from the full name. There's an Excel function called...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Convert feet and inches to inches](https://exceljet.net/formulas/convert-feet-and-inches-to-inches)
    
*   [Split dimensions into three parts](https://exceljet.net/formulas/split-dimensions-into-three-parts)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    

### Functions

*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [REPT Function](https://exceljet.net/functions/rept-function)
    
*   [ABS Function](https://exceljet.net/functions/abs-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    

### Videos

*   [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)
    

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