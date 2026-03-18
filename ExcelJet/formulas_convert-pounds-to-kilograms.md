# Convert pounds to kilograms - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-pounds-to-kilograms

---

[Skip to main content](https://exceljet.net/formulas/convert-pounds-to-kilograms#main-content)

[](https://exceljet.net/formulas/convert-pounds-to-kilograms#)

*   [Previous](https://exceljet.net/formulas/convert-numbers-to-1-or-0)
    
*   [Next](https://exceljet.net/formulas/copy-value-from-every-nth-column)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Convert pounds to kilograms
===========================

by Dave Bruns · Updated 6 Jun 2019

Related functions 
------------------

[CONVERT](https://exceljet.net/functions/convert-function)

![Excel formula: Convert pounds to kilograms](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20pounds%20to%20kilograms.png "Excel formula: Convert pounds to kilograms")

Summary
-------

To build a simple table to convert pounds into kilograms (and [stones](https://en.wikipedia.org/wiki/Stone_(unit))
!) you can use the CONVERT function. In the example shown, the formula in C5, copied down, is:

    =CONVERT(B5,"lbm","kg")
    

Results will update automatically when values in column B change.

Generic formula
---------------

    =CONVERT(A1,"lbm","kg")

Explanation 
------------

This formula relies on the [CONVERT function](https://exceljet.net/functions/convert-function)
, which can convert a number in one measurement system to another. To perform the conversion, CONVERT relies on "from" and "to" units entered as text. As long as the units specify valid options, CONVERT will automatically perform a conversion and return a numeric result.

To convert pounds to kilograms, the formula used is in C5, copied down, is:

    =CONVERT(B5,"lbm","kg")
    

_Note: CONVERT is case-sensitive, so the text values used for units must match exactly._

### Kilograms to pounds

To convert from kilograms to pounds, the formula would be:

    =CONVERT(B5,"kg","lbm")
    

### Pounds to Stones

To convert pounds to kilograms, the formula used in D5, copied down, is

    =CONVERT(B5,"lbm","stone")
    

### Table set-up

The table in the example shown uses formulas to make it easy to change the staring point and range of the values in column B. The formula in B5 simply points to G4:

    =G4
    

The formula in G5, copied down, is:

    =B5+$G$5
    

When values in G4 or G5 are changed, the values in column B update dynamically.

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

[![Excel formula: Celsius to Fahrenheit conversion](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/celsius%20to%20fahrenheit%20conversion.png "Excel formula: Celsius to Fahrenheit conversion")](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)

### [Celsius to Fahrenheit conversion](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)

In this example, the goal is to convert the Celsius temperatures shown in column B to Fahrenheit temperatures in column C. The solution shown in the worksheet above relies on the CONVERT function, which can convert a number in one measurement system to another. CONVERT is fully automatic and based...

Related functions
-----------------

[![Excel CONVERT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_convert.png "Excel CONVERT function")](https://exceljet.net/functions/convert-function)

### [CONVERT Function](https://exceljet.net/functions/convert-function)

The Excel CONVERT function converts a number in one measurement system to another. For example, you can use CONVERT to convert feet into meters, pounds into kilograms, Fahrenheit to Celsius, gallons into liters, and for many other unit conversions.

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
    
*   [Celsius to Fahrenheit conversion](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)
    

### Functions

*   [CONVERT Function](https://exceljet.net/functions/convert-function)
    

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