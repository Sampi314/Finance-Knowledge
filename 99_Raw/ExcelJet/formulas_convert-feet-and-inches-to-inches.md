# Convert feet and inches to inches - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-feet-and-inches-to-inches

---

[Skip to main content](https://exceljet.net/formulas/convert-feet-and-inches-to-inches#main-content)

[](https://exceljet.net/formulas/convert-feet-and-inches-to-inches#)

*   [Previous](https://exceljet.net/formulas/convert-expense-time-units)
    
*   [Next](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Convert feet and inches to inches
=================================

by Dave Bruns · Updated 14 May 2021

Related functions 
------------------

[LEFT](https://exceljet.net/functions/left-function)

[FIND](https://exceljet.net/functions/find-function)

[MID](https://exceljet.net/functions/mid-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6593/download?token=coeUlHeE)
 (13.61 KB)

![Excel formula: Convert feet and inches to inches](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20feet%20and%20inches%20to%20inches.png "Excel formula: Convert feet and inches to inches")

Summary
-------

To convert a measurement in feet and inches to inches only (i.e. 4'5" to 53) you can use a formula based on several functions, including [LEFT](https://exceljet.net/functions/left-function)
, [FIND](https://exceljet.net/functions/find-function)
, [MID](https://exceljet.net/functions/mid-function)
, [ABS](https://exceljet.net/functions/abs-function)
, and [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
. In the example shown, the formula in D5 is:

    =LEFT(B5,FIND("'",B5)-1)*12+ABS(SUBSTITUTE(MID(B5,FIND("'",B5)+1,LEN(B5)),"""",""))
    

Generic formula
---------------

    =LEFT(A1,FIND("'",A1)-1)*12+ABS(SUBSTITUTE(MID(A1,FIND("'",A1)+1,LEN(A1)),"""",""))
    

Explanation 
------------

In this example the goal is to parse feet and inches out in the [text strings](https://exceljet.net/glossary/text-value)
 shown in column B, and create a single numeric value for total inches. The challenge is that each of the two numbers is embedded in text. The formula can be divided into two parts. In the first part of the formula, feet are extracted and converted to inches. In the second part, inches are extracted and added to the result.

### Extracting feet

To extract feet and convert them to inches, we use the following snippet:

    =LEFT(B5,FIND("'",B5)-1)*12
    

Working from the inside out, the [FIND function](https://exceljet.net/functions/find-function)
 is used to locate the position of the single quote (') in the string:

    FIND("'",B5) // returns 2
    

We then subtract 1 (-1) and feed the result into the [LEFT function](https://exceljet.net/functions/left-function)
 as the number of characters to extract from the left:

    LEFT(B5,1) // returns "8"
    

For cell B5, LEFT returns "8," which is then multiplied by 12 to get 96 inches. Note that the [LEFT function](https://exceljet.net/functions/left-function)
 will return a _text value_, but the [math operation](https://exceljet.net/glossary/math-operators)
 of multiplying by 12 will _automatically_ convert the text to a number.

### Extracting inches

In the second part of the formula, we extract the value for inches from the text with this snippet:

    SUBSTITUTE(MID(B5,FIND("'",B5)+1,LEN(B5)),"""","")
    

Here we again locate the position of the single quote (') in the string with FIND. This time, however, we _add_ 1 (+1) so that we start extracting _after_ the single quote:

    FIND("'",B5)+1 // returns 3
    

The result is 3, which we feed into the [MID function](https://exceljet.net/functions/mid-function)
 as the start number:

    MID(B5,3,LEN(B5))
    

For the number of characters to extract, we cheat and use the [LEN function](https://exceljet.net/functions/len-function)
. LEN will return the total characters in B5 (5), which is a larger number of characters than remain in the string. However, MID will simply extract all remaining characters without complaint:

    MID(B5,3,5) // returns " 4"""
    

For B5, MID will return " 4""", which goes into the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 as text:

    SUBSTITUTE(" 4""","""","") // returns " 4"
    

The [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 is configured to replace the double quote (") character with an [empty string](https://exceljet.net/glossary/empty-string)
 (""). In B5, SUBSTITUTE returns " 4" as text. As before, the math operation of addition will convert text value (with a space) to a number automatically, and the formula in B5 will give a final result of 100. However, to guard against a hyphen, we hand off the number returned by SUBSTITUTE to the ABS function for reasons explained below.

_Note: the use of four quote characters ("""") to refer to a single double quote character (") is somewhat confusing. In brief, the outer quotes indicate a text value, the second quote is an escape character, and the third quote is the actual value. [More details here](https://exceljet.net/formulas/double-quotes-inside-a-formula)
._

### Handling the hyphen

The measurements in B12:B13, include a hyphen (-) between feet and inches. When a hyphen is present between feet and inches, it will cause Excel to interpret the inch value as a _negative_ number and create an incorrect result, since inches will be subtracted instead of added. To guard against this problem, we hand off the number extracted for inches to the [ABS function](https://exceljet.net/functions/abs-function)
. For example, in B12, [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
 returns "-3 1/2" and ABS returns 3.5:

    ABS("-3 1/2") // returns 3.5
    

Using the ABS function this way allows the same formula to handle both cases. If a hyphen _is_ present, ABS interprets the value as negative and flips the value to a positive number. If a hyphen _is not_ present, ABS returns the number unchanged. ABS also coerces the text value to a number.

### Other units

Once you have a numeric measurement in inches, you can use the [CONVERT function](https://exceljet.net/functions/convert-function)
 to convert to other units of measure.

Related formulas
----------------

[![Excel formula: Convert inches to feet and inches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Convert%20inches%20to%20feet%20and%20inches.png "Excel formula: Convert inches to feet and inches")](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)

### [Convert inches to feet and inches](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)

In this example, the goal is to create a formula that converts a numeric value in inches to a format that displays inches and feet, as seen in the table below: Input Output 9 0' 9" 12 1' 0" 30 2' 6" 75 6' 3" The math for this problem is fairly simple, but the problem is more complex because we need...

[![Excel formula: Split dimensions into three parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_dimensions_into_three_parts.png "Excel formula: Split dimensions into three parts")](https://exceljet.net/formulas/split-dimensions-into-three-parts)

### [Split dimensions into three parts](https://exceljet.net/formulas/split-dimensions-into-three-parts)

In this example, the goal is to split the text strings in column B, which contain three dimensions in the form "L x W x H", into 3 separate dimensions. One problem with dimensions entered as text is that they can't be used for any kind of calculation. So, in addition, we want our final dimensions...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

Related functions
-----------------

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

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

*   [Convert inches to feet and inches](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)
    
*   [Split dimensions into three parts](https://exceljet.net/formulas/split-dimensions-into-three-parts)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    

### Functions

*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    

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