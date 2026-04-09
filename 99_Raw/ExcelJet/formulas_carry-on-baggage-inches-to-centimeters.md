# Carry-on baggage Inches to centimeters - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/carry-on-baggage-inches-to-centimeters

---

[Skip to main content](https://exceljet.net/formulas/carry-on-baggage-inches-to-centimeters#main-content)

[](https://exceljet.net/formulas/carry-on-baggage-inches-to-centimeters#)

*   [Previous](https://exceljet.net/formulas/cap-percentage-at-specific-amount)
    
*   [Next](https://exceljet.net/formulas/cash-denomination-calculator)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Carry-on baggage Inches to centimeters
======================================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[CONVERT](https://exceljet.net/functions/convert-function)

![Excel formula: Carry-on baggage Inches to centimeters](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/carry-on%20baggage%20Inches%20to%20centimeters.png "Excel formula: Carry-on baggage Inches to centimeters")

Summary
-------

To convert metric measurements for allowed carry-on baggage size to inches, or vice versa, you can use the [CONVERT function](https://exceljet.net/functions/sumifs-function)
. In the example shown, the formula in F5, copied down and across, is:

    =CONVERT(C5,"in","cm")
    

Generic formula
---------------

    =CONVERT(A1,"in","cm")

Explanation 
------------

The CONVERT function requires three arguments: number, from\_unit, and to\_unit. As long as the units specified are in the same category (weight, distance, temperature, etc.) , CONVERT will automatically perform a conversion and return a numeric result in the specified "to unit".

In the example shown, the top table is set up to convert from inches to centimeters, and the bottom table is set up to convert from centimeters to inches. The formulas in F5 and F9, which are copied across and down, are as follows:

    =CONVERT(C5,"in","cm") // F5
    =CONVERT(C9,"cm","in") // F9
    

Related formulas
----------------

[![Excel formula: Convert pounds to kilograms](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20pounds%20to%20kilograms.png "Excel formula: Convert pounds to kilograms")](https://exceljet.net/formulas/convert-pounds-to-kilograms)

### [Convert pounds to kilograms](https://exceljet.net/formulas/convert-pounds-to-kilograms)

This formula relies on the CONVERT function , which can convert a number in one measurement system to another. To perform the conversion, CONVERT relies on "from" and "to" units entered as text. As long as the units specify valid options, CONVERT will automatically perform a conversion and return a...

[![Excel formula: Convert inches to feet and inches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Convert%20inches%20to%20feet%20and%20inches.png "Excel formula: Convert inches to feet and inches")](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)

### [Convert inches to feet and inches](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)

In this example, the goal is to create a formula that converts a numeric value in inches to a format that displays inches and feet, as seen in the table below: Input Output 9 0' 9" 12 1' 0" 30 2' 6" 75 6' 3" The math for this problem is fairly simple, but the problem is more complex because we need...

[![Excel formula: Celsius to Fahrenheit conversion](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/celsius%20to%20fahrenheit%20conversion.png "Excel formula: Celsius to Fahrenheit conversion")](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)

### [Celsius to Fahrenheit conversion](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)

In this example, the goal is to convert the Celsius temperatures shown in column B to Fahrenheit temperatures in column C. The solution shown in the worksheet above relies on the CONVERT function, which can convert a number in one measurement system to another. CONVERT is fully automatic and based...

[![Excel formula: Split dimensions into three parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_dimensions_into_three_parts.png "Excel formula: Split dimensions into three parts")](https://exceljet.net/formulas/split-dimensions-into-three-parts)

### [Split dimensions into three parts](https://exceljet.net/formulas/split-dimensions-into-three-parts)

In this example, the goal is to split the text strings in column B, which contain three dimensions in the form "L x W x H", into 3 separate dimensions. One problem with dimensions entered as text is that they can't be used for any kind of calculation. So, in addition, we want our final dimensions...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

Related functions
-----------------

[![Excel CONVERT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_convert.png "Excel CONVERT function")](https://exceljet.net/functions/convert-function)

### [CONVERT Function](https://exceljet.net/functions/convert-function)

The Excel CONVERT function converts a number in one measurement system to another. For example, you can use CONVERT to convert feet into meters, pounds into kilograms, Fahrenheit to Celsius, gallons into liters, and for many other unit conversions.

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

*   [Convert pounds to kilograms](https://exceljet.net/formulas/convert-pounds-to-kilograms)
    
*   [Convert inches to feet and inches](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)
    
*   [Celsius to Fahrenheit conversion](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)
    
*   [Split dimensions into three parts](https://exceljet.net/formulas/split-dimensions-into-three-parts)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    

### Functions

*   [CONVERT Function](https://exceljet.net/functions/convert-function)
    

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