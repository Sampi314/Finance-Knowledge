# Normalize size units to Gigabytes - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/normalize-size-units-to-gigabytes

---

[Skip to main content](https://exceljet.net/formulas/normalize-size-units-to-gigabytes#main-content)

[](https://exceljet.net/formulas/normalize-size-units-to-gigabytes#)

*   [Previous](https://exceljet.net/formulas/nightly-hotel-rate-calculation)
    
*   [Next](https://exceljet.net/formulas/nth-root-of-number)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Normalize size units to Gigabytes
=================================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[MATCH](https://exceljet.net/functions/match-function)

[LEFT](https://exceljet.net/functions/left-function)

[RIGHT](https://exceljet.net/functions/right-function)

![Excel formula: Normalize size units to Gigabytes](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/normalize%20units%20to%20gigabytes.png "Excel formula: Normalize size units to Gigabytes")

Summary
-------

To normalize units to Gigabytes (or megabytes, kilobytes, etc.) you can use a clever formula based the MATCH, LEFT, and RIGHT functions. In the example shown, the formula in C5 is:

    =LEFT(B5,LEN(B5)-2)/10^((MATCH(RIGHT(B5,2),{"PB","TB","GB","MB","KB"},0)-3)*3)
    

_Note: for simplicity, we are using decimal (base 10) values, but there is a [binary standard](https://en.wikipedia.org/wiki/Gibibyte)
 as well. See below._

Generic formula
---------------

    =LEFT(A1,LEN(A1)-2)/10^((MATCH(RIGHT(A1,2),{"PB","TB","GB","MB","KB"},0)-3)*3)

Explanation 
------------

_Important: This formula assumes that units are the last 2 characters of the text value that includes both a number and a unit of measure._

This formula works because digital units have a "power of 10" relationship. At the core, this formula separates the number part of the size from the unit, then divides the number by the appropriate divisor to normalize to Gigabytes. The divisor is calculated as a power of 10, so the formula reduces to this:

    =number/10^power
    

To get the number, the formula extracts all characters from the left up to but not including the units:

    LEFT(B5,LEN(B5)-2)
    

To get "power", the formula matches the unit with a hard-coded array constant, {"PB","TB","GB","MB","KB"}:

    MATCH(RIGHT(B5,2),{"PB","TB","GB","MB","KB"},0)
    

The result from MATCH is the position of the unit in the array constant. For example, for the formula in C5, the unit is "KB", so the result is 5. This result is adjusted by subtracting 3, then multiplying the result by 3, which yields 6 as the power, which is used as the exponent to calculate the correct result in gigabytes:

    =900/10^6
    =900/1000000
    =0.0009
    

### Binary standard formula

Computers use the binary number system to store and report data size, but the prefixes like "kilo", "mega", "giga", etc. are based on the metric system. It's a confusing topic, but using decimal units for storage on a computer isn't really correct, and the discrepancy increases as units get larger. The formula below will normalize to binary units.

    =LEFT(A1,LEN(A1)-2)/2^((MATCH(RIGHT(A1,2),{"PB","TB","GB","MB","KB"},0)-3)*10)
    

With this formula, you are technically getting Gibibytes (GiB), not Gigabytes. More information [here](http://en.wikipedia.org/wiki/Gibibyte)
 and [here](https://en.wikipedia.org/wiki/Binary_prefix)
.

Related formulas
----------------

[![Excel formula: Split text and numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20text%20and%20numbers.png "Excel formula: Split text and numbers")](https://exceljet.net/formulas/split-text-and-numbers)

### [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)

Overview The formula looks complex, but the mechanics are in fact quite simple. As with most formulas that split or extract text, the key is to locate the position of the thing you are looking for. Once you have the position, you can use other functions to extract what you need. In this case, we...

[![Excel formula: Split numbers from units of measure](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20numbers%20and%20units.png "Excel formula: Split numbers from units of measure")](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

### [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

Sometimes you encounter data that mixes units directly with numbers (i.e. 8km, 12v, 7.5hrs). Unfortunately, Excel will treat the numbers in this format as text, and you won't be able to perform math operations on such values. To split a number from a unit value, you need to determine the position...

Related functions
-----------------

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)
    
*   [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)
    

### Functions

*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    

### Links

*   [Stackoverflow.com answer by Ron Rosenfeld](http://stackoverflow.com/a/31411173/4071990)
    

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