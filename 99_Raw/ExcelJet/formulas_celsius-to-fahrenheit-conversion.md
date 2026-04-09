# Celsius to Fahrenheit conversion - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/celsius-to-fahrenheit-conversion

---

[Skip to main content](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion#main-content)

[](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion#)

*   [Previous](https://exceljet.net/formulas/cash-denomination-calculator)
    
*   [Next](https://exceljet.net/formulas/change-negative-numbers-to-positive)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Celsius to Fahrenheit conversion
================================

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[CONVERT](https://exceljet.net/functions/convert-function)

[NOT](https://exceljet.net/functions/not-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

![Excel formula: Celsius to Fahrenheit conversion](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/celsius%20to%20fahrenheit%20conversion.png "Excel formula: Celsius to Fahrenheit conversion")

Summary
-------

To build a simple table to convert temperature from Celsius to Fahrenheit, you can use the [CONVERT function](https://exceljet.net/functions/convert-function)
. In the example shown, the formula in C5 is:

    =CONVERT(B5,"C","F")
    

As the formula is copied down, it converts the Celsius temperatures listed in column B to Fahrenheit temperatures. The results in column C will update automatically when values in column B change.

Generic formula
---------------

    =CONVERT(A1,"C","F")

Explanation 
------------

In this example, the goal is to convert the Celsius temperatures shown in column B to Fahrenheit temperatures in column C. The solution shown in the worksheet above relies on the CONVERT function, which can convert a number in one measurement system to another. CONVERT is fully automatic and based on "from" and "to" unit strings. As long as the units valid options in the same category (weight, distance, temperature, etc.), CONVERT will automatically perform a conversion and return a numeric result.

### Celsius to Fahrenheit

To convert from Celsius to Fahrenheit, use a "C" for Celsius and an "F" for Fahrenheit like this:

    =CONVERT(B5,"C","F")
    

_Note: unit strings are case-sensitive. Both the "C" and "F" must be uppercase._

### Handling empty cells

If a cell in column B is empty, the CONVERT function will interpret the value as zero and return 32. To prevent this from happening, you can adjust the formula to test for a value first like this:

    =IF(B5<>"",CONVERT(B5,"C","F"),"")

Here, the [IF function](https://exceljet.net/functions/if-function)
 is used to check if cell B5 is not empty. If so, the original CONVERT formula is run. If the cell is empty, IF returns an empty string ("") as a result, which looks like a blank cell in Excel. As an alternative, you can use the [NOT](https://exceljet.net/functions/not-function)
 and [ISBLANK](https://exceljet.net/functions/isblank-function)
 functions together like so:

    =IF(NOT(ISBLANK(B5)),CONVERT(B5,"C","F"),"")

The result from this formula is exactly the same.

### Fahrenheit to Celsius

To convert from Fahrenheit to Celsius, the formula would be:

    =CONVERT(B5,"F","C")
    

### Other conversions

You can use CONVERT to convert weight, distance, time, pressure, force, energy, power, magnetism, temperature, liquid, and volume. Unit strings must be valid and in the proper case. [This page shows available options in each category](https://exceljet.net/functions/convert-function)
.

Related formulas
----------------

[![Excel formula: Convert inches to feet and inches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Convert%20inches%20to%20feet%20and%20inches.png "Excel formula: Convert inches to feet and inches")](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)

### [Convert inches to feet and inches](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)

In this example, the goal is to create a formula that converts a numeric value in inches to a format that displays inches and feet, as seen in the table below: Input Output 9 0' 9" 12 1' 0" 30 2' 6" 75 6' 3" The math for this problem is fairly simple, but the problem is more complex because we need...

[![Excel formula: Carry-on baggage Inches to centimeters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/carry-on%20baggage%20Inches%20to%20centimeters.png "Excel formula: Carry-on baggage Inches to centimeters")](https://exceljet.net/formulas/carry-on-baggage-inches-to-centimeters)

### [Carry-on baggage Inches to centimeters](https://exceljet.net/formulas/carry-on-baggage-inches-to-centimeters)

The CONVERT function requires three arguments: number, from\_unit, and to\_unit. As long as the units specified are in the same category (weight, distance, temperature, etc.) , CONVERT will automatically perform a conversion and return a numeric result in the specified "to unit". In the example shown...

Related functions
-----------------

[![Excel CONVERT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_convert.png "Excel CONVERT function")](https://exceljet.net/functions/convert-function)

### [CONVERT Function](https://exceljet.net/functions/convert-function)

The Excel CONVERT function converts a number in one measurement system to another. For example, you can use CONVERT to convert feet into meters, pounds into kilograms, Fahrenheit to Celsius, gallons into liters, and for many other unit conversions.

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

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
    
*   [Carry-on baggage Inches to centimeters](https://exceljet.net/formulas/carry-on-baggage-inches-to-centimeters)
    

### Functions

*   [CONVERT Function](https://exceljet.net/functions/convert-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    

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