# Excel CONVERT function | Exceljet

**Source:** https://exceljet.net/functions/convert-function

---

[Skip to main content](https://exceljet.net/functions/convert-function#main-content)

[](https://exceljet.net/functions/convert-function#)

*   [Previous](https://exceljet.net/functions/complex-function)
    
*   [Next](https://exceljet.net/functions/dec2bin-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

CONVERT Function
================

by Dave Bruns · Updated 12 Jan 2026

![Excel CONVERT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_convert.png "Excel CONVERT function")

Summary
-------

The Excel CONVERT function converts a number in one measurement system to another. For example, you can use CONVERT to convert feet into meters, pounds into kilograms, Fahrenheit to Celsius, gallons into liters, and for many other unit conversions.

Purpose 
--------

Convert measurement units

Return value 
-------------

A number in the new measurement system

Syntax
------

    =CONVERT(number,from_unit,to_unit)

*   _number_ - The numeric value to convert.
*   _from\_unit_ - The starting units for number.
*   _to\_unit_ - The ending units for the result.

Using the CONVERT function 
---------------------------

The CONVERT function converts a number in one measurement system to another. For example, you can use CONVERT to convert feet into meters, pounds into kilograms, gallons into liters, and for many other unit conversions.

> The CONVERT function is case-sensitive. You must supply units as shown below. For example, to convert yards to meters, use a lowercase "yd" and lowercase "m", like this: `=CONVERT(100,"yd","m")`

### Examples

The formulas below use the CONVERT function to convert yards to meters, Celsius to Fahrenheit, gallons to liters, and square meters to square yards:

    =CONVERT(100,"yd","m") // returns 91.44
    =CONVERT(22,"C","F") // returns 71.6
    =CONVERT(1,"gal","l") // returns 3.79
    =CONVERT(100,"m2","ft2") // returns 1076.39
    

To round the results returned by CONVERT, nest CONVERT inside the [ROUND function](https://exceljet.net/functions/round-function)
:

    =ROUND(CONVERT(100,"yd","m"),0) // yards to meters, returns 91
    =ROUND(CONVERT(5,"mi","km"),1) // miles to kilometers, returns 8.0
    =ROUND(CONVERT(150,"lbm","kg"),1) // pounds to kilograms, returns 68.0
    

### Conversion categories

The tables below show the units available to the CONVERT function in each category. In all cases, Unit can be used for either from\_unit or to\_unit in the same category.

*   [Mass](https://exceljet.net/functions/convert-function#mass)
    
*   [Distance](https://exceljet.net/functions/convert-function#distance)
    
*   [Time](https://exceljet.net/functions/convert-function#time)
    
*   [Pressure](https://exceljet.net/functions/convert-function#pressure)
    
*   [Force](https://exceljet.net/functions/convert-function#force)
    
*   [Energy](https://exceljet.net/functions/convert-function#energy)
    
*   [Power](https://exceljet.net/functions/convert-function#power)
    
*   [Magnetism](https://exceljet.net/functions/convert-function#magnetism)
    
*   [Temperature](https://exceljet.net/functions/convert-function#temperature)
    
*   [Liquid](https://exceljet.net/functions/convert-function#liquid)
    
*   [Volume](https://exceljet.net/functions/convert-function#volume)
    
*   [Area](https://exceljet.net/functions/convert-function#area)
    
*   [Information](https://exceljet.net/functions/convert-function#information)
    
*   [Metric prefixes](https://exceljet.net/functions/convert-function#metric-prefixes)
    
*   [Binary prefixes](https://exceljet.net/functions/convert-function#binary-prefixes)
    

### Mass

Use these units to convert between different measures of weight and mass. This is useful for recipes, shipping calculations, and scientific applications. For example:

    =CONVERT(150,"lbm","kg") // pounds to kilograms, returns 68.04
    =CONVERT(500,"g","ozm") // grams to ounces, returns 17.64
    =CONVERT(1,"stone","lbm") // stone to pounds, returns 14
    

| Mass | Unit |
| --- | --- |
| Gram | "g" |
| Slug | "sg" |
| Pound mass (avoirdupois) | "lbm" |
| U (atomic mass unit) | "u" |
| Ounce mass (avoirdupois) | "ozm" |
| Grain | "grain" |
| U.S. (short) hundredweight | "cwt" or "shweight" |
| Imperial hundredweight | "uk\_cwt" or "lcwt" ("hweight") |
| Stone | "stone" |
| Ton | "ton" |
| Imperial ton | "uk\_ton" or "LTON" ("brton") |

### Distance

These units allow you to perform conversions related to length and distance. For example:

    =CONVERT(5,"mi","km") // miles to kilometers, returns 8.05
    =CONVERT(6,"ft","m") // feet to meters, returns 1.83
    =CONVERT(100,"cm","in") // centimeters to inches, returns 39.37
    

| Distance | Unit |
| --- | --- |
| Meter | "m" |
| Statute mile | "mi" |
| Nautical mile | "Nmi" |
| Inch | "in" |
| Foot | "ft" |
| Yard | "yd" |
| Angstrom | "ang" |
| Ell | "ell" |
| Light-year | "ly" |
| Parsec | "parsec" or "pc" |
| Pica (1/72 inch) | "Picapt" or "Pica" |
| Pica (1/6 inch) | "pica" |
| U.S survey mile (statute mile) | "survey\_mi" |

### Time

Convert between different units of time with these options. For example:

    =CONVERT(2.5,"hr","min") // hours to minutes, returns 150
    =CONVERT(90,"mn","hr") // minutes to hours, returns 1.5
    =CONVERT(1,"day","sec") // days to seconds, returns 86400
    

| Time | Unit |
| --- | --- |
| Year | "yr" |
| Day | "day" or "d" |
| Hour | "hr" |
| Minute | "mn" or "min" |
| Second | "sec" or "s" |

### Pressure

Use these units for pressure-related conversions, commonly needed in engineering and scientific contexts. For example:

    =CONVERT(1,"atm","psi") // atmospheres to PSI, returns 14.70
    =CONVERT(30,"psi","Pa") // PSI to pascals, returns 206842.7188
    =CONVERT(760,"mmHg","atm") // mmHg to atmospheres, returns 1
    

| Pressure | Unit |
| --- | --- |
| Pascal | "Pa" (or "p") |
| Atmosphere | "atm" (or "at") |
| mm of Mercury | "mmHg" |
| PSI | "psi" |
| Torr | "Torr" |

### Force

These units handle conversions related to force, useful in physics and engineering calculations. For example:

    =CONVERT(100,"N","lbf") // newtons to pound-force, returns 22.48
    =CONVERT(50,"lbf","N") // pound-force to newtons, returns 222.41
    =CONVERT(1,"N","dyn") // newtons to dynes, returns 100000
    

| Force | Unit |
| --- | --- |
| Newton | "N" |
| Dyne | "dyn" (or "dy") |
| Pound force | "lbf" |
| Pond | "pond" |

### Energy

Convert between various energy units with these options. This is helpful for comparing energy consumption, nutritional values, and fuel efficiency. For example:

    =CONVERT(1000,"J","cal") // joules to calories, returns 238.846
    =CONVERT(1,"BTU","Wh") // BTU to watt-hours, returns 0.293
    =CONVERT(100,"cal","J") // calories to joules, returns 418.68
    

| Energy | Unit |
| --- | --- |
| Joule | "J" |
| Erg | "e" |
| Thermodynamic calorie | "c" |
| IT calorie | "cal" |
| Electron volt | "eV" (or "ev") |
| Horsepower-hour | "HPh" (or "hh") |
| Watt-hour | "Wh" (or "wh") |
| Foot-pound | "flb" |
| BTU | "BTU" (or "btu") |

### Power

Use these units for power-related conversions, such as comparing engine ratings or electrical consumption. For example:

    =CONVERT(1,"HP","W") // horsepower to watts, returns 745.7
    =CONVERT(1500,"W","HP") // watts to horsepower, returns 2.01
    =CONVERT(100,"HP","kW") // horsepower to kilowatts, returns 74.57
    

| Power | Unit |
| --- | --- |
| Horsepower | "HP" (or "h") |
| Pferdestärke | "PS" |
| Watt | "W" (or "w") |

### Magnetism

These units allow conversions between magnetic field strength measurements. For example:

    =CONVERT(1,"T","ga") // tesla to gauss, returns 10000
    =CONVERT(5000,"ga","T") // gauss to tesla, returns 0.5
    

| Magnetism | Unit |
| --- | --- |
| Tesla | "T" |
| Gauss | "ga" |

### Temperature

Convert between temperature scales with these units. Unlike other conversions, temperature conversions involve both scaling and offset adjustments. For example:

    =CONVERT(32,"F","C") // Fahrenheit to Celsius, returns 0
    =CONVERT(100,"C","F") // Celsius to Fahrenheit, returns 212
    =CONVERT(0,"C","K") // Celsius to Kelvin, returns 273.15
    

| Temperature | Unit |
| --- | --- |
| Degree Celsius | "C" (or "cel") |
| Degree Fahrenheit | "F" (or "fah") |
| Kelvin | "K" (or "kel") |
| Degrees Rankine | "Rank" |
| Degrees Réaumur | "Reau" |

### Liquid

Use these units for liquid volume conversions, ideal for cooking, beverage calculations, and fuel measurements. Note the distinction between U.S. and U.K. (Imperial) measures. For example:

    =CONVERT(1,"gal","l") // US gallons to liters, returns 3.79
    =CONVERT(2,"cup","ml") // cups to milliliters, returns 473.18
    =CONVERT(1,"uk_gal","gal") // UK gallons to US gallons, returns 1.20
    

| Liquid measure | Unit |
| --- | --- |
| Teaspoon | "tsp" |
| Modern teaspoon | "tspm" |
| Tablespoon | "tbs" |
| Fluid ounce | "oz" |
| Cup | "cup" |
| U.S. pint | "pt" (or "us\_pt") |
| U.K. pint | "uk\_pt" |
| Quart | "qt" |
| Imperial quart (U.K.) | "uk\_qt" |
| Gallon | "gal" |
| Imperial gallon (U.K.) | "uk\_gal" |
| Liter | "l" or "L" ("lt") |

### Volume

These units handle three-dimensional volume conversions, useful for shipping, storage, and construction calculations. For example:

    =CONVERT(1,"m3","ft3") // cubic meters to cubic feet, returns 35.31
    =CONVERT(100,"ft3","yd3") // cubic feet to cubic yards, returns 3.70
    =CONVERT(1,"barrel","gal") // oil barrels to gallons, returns 42
    

| Volume | Unit |
| --- | --- |
| Cubic angstrom | "ang3" or "ang^3" |
| U.S. oil barrel | "barrel" |
| U.S. bushel | "bushel" |
| Cubic feet | "ft3" or "ft^3" |
| Cubic inch | "in3" or "in^3" |
| Cubic light-year | "ly3" or "ly^3" |
| Cubic meter | "m3" or "m^3" |
| Cubic Mile | "mi3" or "mi^3" |
| Cubic yard | "yd3" or "yd^3" |
| Cubic nautical mile | "Nmi3" or "Nmi^3" |
| Cubic Pica | "Picapt3", "Picapt^3", "Pica3" or "Pica^3" |
| Gross Registered Ton | "GRT" ("regton") |
| Measurement ton (freight ton) | "MTON" |

### Area

Convert between surface area measurements with these units, helpful for real estate, landscaping, and flooring projects. For example:

    =CONVERT(1,"ha","us_acre") // hectares to acres, returns 2.47
    =CONVERT(1000,"ft2","m2") // square feet to square meters, returns 92.90
    =CONVERT(1,"mi2","km2") // square miles to square kilometers, returns 2.59
    

| Area | Unit |
| --- | --- |
| International acre | "uk\_acre" |
| U.S. survey/statute acre | "us\_acre" |
| Square angstrom | "ang2" or "ang^2" |
| Are | "ar" |
| Square feet | "ft2" or "ft^2" |
| Hectare | "ha" |
| Square inches | "in2" or "in^2" |
| Square light-year | "ly2" or "ly^2" |
| Square meters | "m2" or "m^2" |
| Morgen | "Morgen" |
| Square miles | "mi2" or "mi^2" |
| Square nautical miles | "Nmi2" or "Nmi^2" |
| Square Pica | "Picapt2", "Pica2", "Pica^2" or "Picapt^2" |
| Square yards | "yd2" or "yd^2" |

### Information

Use these units to convert between digital storage measurements. Combine with metric or binary prefixes (see below) for larger units like kilobytes, megabytes, and gigabytes. For example:

    =CONVERT(1,"byte","bit") // bytes to bits, returns 8
    =CONVERT(1024,"byte","kbyte") // bytes to kilobytes, returns 1.024
    =CONVERT(500,"Mbyte","Gbyte") // megabytes to gigabytes, returns 0.5
    =CONVERT(2000,"Gbyte","Tbyte") // gigabytes to terabytes, returns 2
    

Note that metric prefixes (k, M, G, T) use powers of 1000, which is how storage is typically marketed. For actual computing where powers of 1024 matter, use binary prefixes (ki, Mi, Gi, Ti) instead:

    =CONVERT(1024,"byte","kibyte") // bytes to kibibytes, returns 1
    =CONVERT(1024,"Mibyte","Gibyte") // mebibytes to gibibytes, returns 1
    

| Information | Unit |
| --- | --- |
| Bit | "bit" |
| Byte | "byte" |

### Metric prefixes

The prefixes shown in the table below can be used with metric units by prepending the abbreviation to the unit. This allows you to work with very large or very small quantities. For example:

    =CONVERT(1,"kg","g") // kilograms to grams, returns 1000
    =CONVERT(5,"cm","m") // centimeters to meters, returns 0.05
    =CONVERT(1,"MW","W") // megawatts to watts, returns 1000000
    

| Prefix | Multiplier | Abbreviation |
| --- | --- | --- |
| yotta | 1E+24 | "Y" |
| zetta | 1E+21 | "Z" |
| exa | 1E+18 | "E" |
| peta | 1E+15 | "P" |
| tera | 1E+12 | "T" |
| giga | 1000000000 | "G" |
| mega | 1000000 | "M" |
| kilo | 1000 | "k" |
| hecto | 100 | "h" |
| deka | 10  | "da" or "e" |
| deci | 0.1 | "d" |
| centi | 0.01 | "c" |
| milli | 0.001 | "m" |
| micro | 0.000001 | "u" |
| nano | 0.000000001 | "n" |
| pico | 1E-12 | "p" |
| femto | 1E-15 | "f" |
| atto | 1E-18 | "a" |
| zepto | 1E-21 | "z" |
| yocto | 1E-24 | "y" |

### Binary prefixes

[The binary unit prefixes](https://en.wikipedia.org/wiki/Binary_prefix)
 below can be used with "bits" and "bytes". Unlike metric prefixes that use powers of 10, binary prefixes use powers of 2, which is how computers actually measure storage. For example:

    =CONVERT(1,"kibyte","byte") // kibibytes to bytes, returns 1024
    =CONVERT(1,"Gibyte","Mibyte") // gibibytes to mebibytes, returns 1024
    =CONVERT(1024,"Mibyte","Gibyte") // mebibytes to gibibytes, returns 1
    

| Binary Prefix | Value | Abbreviation | Decimal |
| --- | --- | --- | --- |
| yobi | 2^80 | "Yi" | yotta |
| zebi | 2^70 | "Zi" | zetta |
| exbi | 2^60 | "Ei" | exa |
| pebi | 2^50 | "Pi" | peta |
| tebi | 2^40 | "Ti" | tera |
| gibi | 2^30 | "Gi" | giga |
| mebi | 2^20 | "Mi" | mega |
| kibi | 2^10 | "ki" | kilo |

### Notes

*   The CONVERT function is case-sensitive.
*   CONVERT will return the #N/A error when a unit string is not recognized.
*   CONVERT will return the #N/A error when units are not compatible.
*   CONVERT will return the #VALUE! error when a number is not valid.
*   A number of measurement units were added to CONVERT in Excel 2013.

CONVERT function examples
-------------------------

[![Excel formula: BMI calculation formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/bmi%20calculation%20formula.png "Excel formula: BMI calculation formula")](https://exceljet.net/formulas/bmi-calculation-formula)

### [BMI calculation formula](https://exceljet.net/formulas/bmi-calculation-formula)

This example shows one way to calculate BMI (Body Mass Index) in Excel. The standard BMI formula is: BMI = weight (kg) / height (m) 2 The approach used here is to first convert height in inches and feet to meters, and weight in pounds to kilograms, then use the standard metric formula for BMI. This...

[![Excel formula: Celsius to Fahrenheit conversion](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/celsius%20to%20fahrenheit%20conversion.png "Excel formula: Celsius to Fahrenheit conversion")](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)

### [Celsius to Fahrenheit conversion](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)

In this example, the goal is to convert the Celsius temperatures shown in column B to Fahrenheit temperatures in column C. The solution shown in the worksheet above relies on the CONVERT function, which can convert a number in one measurement system to another. CONVERT is fully automatic and based...

[![Excel formula: Carry-on baggage Inches to centimeters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/carry-on%20baggage%20Inches%20to%20centimeters.png "Excel formula: Carry-on baggage Inches to centimeters")](https://exceljet.net/formulas/carry-on-baggage-inches-to-centimeters)

### [Carry-on baggage Inches to centimeters](https://exceljet.net/formulas/carry-on-baggage-inches-to-centimeters)

The CONVERT function requires three arguments: number, from\_unit, and to\_unit. As long as the units specified are in the same category (weight, distance, temperature, etc.) , CONVERT will automatically perform a conversion and return a numeric result in the specified "to unit". In the example shown...

[![Excel formula: Convert pounds to kilograms](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20pounds%20to%20kilograms.png "Excel formula: Convert pounds to kilograms")](https://exceljet.net/formulas/convert-pounds-to-kilograms)

### [Convert pounds to kilograms](https://exceljet.net/formulas/convert-pounds-to-kilograms)

This formula relies on the CONVERT function , which can convert a number in one measurement system to another. To perform the conversion, CONVERT relies on "from" and "to" units entered as text. As long as the units specify valid options, CONVERT will automatically perform a conversion and return a...

CONVERT function videos
-----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/how-to-create-an-excel-table)

### [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)

In this video, we'll look at how to create an Excel table. Here we have some data that is a good candidate for a table. Each row represents an entry or record with information that belongs together. Each column has a unique name. The first step in creating a table is to remove any blank rows or...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20trace%20formula%20relationships-thumb.png)](https://exceljet.net/videos/how-to-trace-formula-relationships)

### [How to trace formula relationships](https://exceljet.net/videos/how-to-trace-formula-relationships)

In this video, we'll look at how to quickly find formulas and trace how they are related to one another using the concept of precedents and dependents. Here we have a simple model that shows the expense of making coffee at home vs. buying coffee in a coffee shop. Let's take a look through the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Carry-on baggage Inches to centimeters](https://exceljet.net/formulas/carry-on-baggage-inches-to-centimeters)
    
*   [Convert pounds to kilograms](https://exceljet.net/formulas/convert-pounds-to-kilograms)
    
*   [BMI calculation formula](https://exceljet.net/formulas/bmi-calculation-formula)
    
*   [Celsius to Fahrenheit conversion](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)
    

### Videos

*   [How to trace formula relationships](https://exceljet.net/videos/how-to-trace-formula-relationships)
    
*   [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)
    

### Links

*   [Microsoft CONVERT function documentation](https://support.office.com/en-us/article/convert-function-d785bef1-808e-4aac-bdcd-666c810f9af2)
    

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