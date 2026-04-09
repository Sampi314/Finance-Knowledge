# BMI calculation formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/bmi-calculation-formula

---

[Skip to main content](https://exceljet.net/formulas/bmi-calculation-formula#main-content)

[](https://exceljet.net/formulas/bmi-calculation-formula#)

*   [Previous](https://exceljet.net/formulas/basic-text-sort-formula)
    
*   [Next](https://exceljet.net/formulas/build-hyperlink-with-vlookup)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

BMI calculation formula
=======================

by Dave Bruns · Updated 13 Nov 2024

Related functions 
------------------

[CONVERT](https://exceljet.net/functions/convert-function)

[POWER](https://exceljet.net/functions/power-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/5746/download?token=bNBkTgLx)
 (10.86 KB)

![Excel formula: BMI calculation formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/bmi%20calculation%20formula.png "Excel formula: BMI calculation formula")

Summary
-------

This example shows one way to calculate BMI (Body Mass Index) in Excel. In the worksheet shown, we first convert height and weight to metric units, then use a standard metric formula to calculate BMI. The formula in H5 is:

    =G5/F5^2
    

which returns calculated BMI based on a weight in G5 and height in F5.

### What is BMI?

BMI stands for Body Mass Index. It is a simple (and inexpensive) way to assess body fat based on height and weight only. BMI is a screening tool that can be used to identify individuals who are underweight, overweight, or obese. However, BMI is not a diagnostic tool. You can read more about BMI on the [CDC website](https://www.cdc.gov/bmi/faq/)
.

Generic formula
---------------

    =weight/height^2

Explanation 
------------

This example shows one way to calculate BMI (Body Mass Index) in Excel. The standard BMI formula is:

**BMI = weight (kg) / height (m)2**

The approach used here is to first convert height in inches and feet to meters, and weight in pounds to kilograms, then use the standard metric formula for BMI. This makes it easy to collect height and weight in commonly used units (in the United States), and also shows the metric amounts used in the calculation.

The main challenge in this example is that most people in the United States still use the [US customary measurement](https://en.wikipedia.org/wiki/United_States_customary_units)
 system to record height and weight, not the metric system. The first step, therefore, is to capture this information in commonly used units. This is done in columns B (feet) C (inches) and D (pounds).

Then, to calculate height in meters, we use the [CONVERT function](https://exceljet.net/functions/convert-function)
 twice in cell F5:

    =CONVERT(B5,"ft","m")+CONVERT(C5,"in","m")
    

The first CONVERT converts feet to meters:

    =CONVERT(B5,"ft","m") // feet to meters
    

The second converts inches to meters:

    =CONVERT(C5,"in","m") // inches to meters
    

Then the two values are simply added together to get a total height in meters.

To calculate weight in kilograms, we use CONVERT again in cell G5:

    =CONVERT(D5,"lbm","kg") // pounds to kilograms
    

Finally, we are ready to apply the standard BMI formula. The formula in H5 is:

    =G5/F5^2 // calculate BMI
    

To square height, we use Excel's [operator](https://exceljet.net/glossary/math-operators)
 for exponentiation, the caret (^).

### Alternatives

The formulas used above can be simplified somewhat. To calculate height, we can use a single CONVERT function like this:

    =CONVERT(B5*12+C5,"in","m")
    

In other words, we convert feet to inches directly inside CONVERT's _number_ argument. When Excel evaluates the formula, this operation happens before the CONVERT function runs. Not quite as readable, but more compact.

Note: Excel's [order of operations](https://exceljet.net/glossary/order-of-operations)
 makes it unnecessary to wrap B5\*12 in parentheses.

Similarly, we could convert inches to feet inside CONVERT like this:

    =CONVERT(B5+C5/12,"ft","m")
    

The result is the same as above. The key point is that you are free to [nest](https://exceljet.net/glossary/nesting)
 other calculations directly in a function argument.

As an alternative to the caret (^), the [POWER function](https://exceljet.net/functions/power-function)
 can be used to raise to a power like this:

    = G5/POWER(F5,2)
    

Related formulas
----------------

[![Excel formula: Convert feet and inches to inches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20feet%20and%20inches%20to%20inches.png "Excel formula: Convert feet and inches to inches")](https://exceljet.net/formulas/convert-feet-and-inches-to-inches)

### [Convert feet and inches to inches](https://exceljet.net/formulas/convert-feet-and-inches-to-inches)

In this example the goal is to parse feet and inches out in the text strings shown in column B, and create a single numeric value for total inches. The challenge is that each of the two numbers is embedded in text. The formula can be divided into two parts. In the first part of the formula, feet...

Related functions
-----------------

[![Excel CONVERT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_convert.png "Excel CONVERT function")](https://exceljet.net/functions/convert-function)

### [CONVERT Function](https://exceljet.net/functions/convert-function)

The Excel CONVERT function converts a number in one measurement system to another. For example, you can use CONVERT to convert feet into meters, pounds into kilograms, Fahrenheit to Celsius, gallons into liters, and for many other unit conversions.

[![Excel POWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20power%20function.png "Excel POWER function")](https://exceljet.net/functions/power-function)

### [POWER Function](https://exceljet.net/functions/power-function)

The Excel POWER function returns a number raised to a given power. The POWER function is an alternative to the [exponent operator](https://exceljet.net/glossary/math-operators)
 (^).

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
    

### Functions

*   [CONVERT Function](https://exceljet.net/functions/convert-function)
    
*   [POWER Function](https://exceljet.net/functions/power-function)
    

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