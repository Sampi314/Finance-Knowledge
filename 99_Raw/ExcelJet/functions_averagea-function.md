# Excel AVERAGEA function | Exceljet

**Source:** https://exceljet.net/functions/averagea-function

---

[Skip to main content](https://exceljet.net/functions/averagea-function#main-content)

[](https://exceljet.net/functions/averagea-function#)

*   [Previous](https://exceljet.net/functions/average-function)
    
*   [Next](https://exceljet.net/functions/averageif-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

AVERAGEA Function
=================

by Dave Bruns · Updated 22 Sep 2021

Related functions 
------------------

[AVERAGE](https://exceljet.net/functions/average-function)

[AVERAGEIF](https://exceljet.net/functions/averageif-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

![Excel AVERAGEA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20averagea%20function.png "Excel AVERAGEA function")

Summary
-------

The Excel AVERAGEA function returns the average of a set of supplied values. Unlike AVERAGE, AVERAGEA will also evaluate the logical values TRUE and FALSE, and numbers represented as text, whereas AVERAGE ignores these values during calculation

Purpose 
--------

Get the average of a group of numbers and text

Return value 
-------------

A number representing the average.

Syntax
------

    =AVERAGEA(value1,[value2],...)

*   _value1_ - A value or reference to a value that can be evaluated as a number.
*   _value2_ - \[optional\] A value or reference to a value that can be evaluated as a number.

Using the AVERAGEA function 
----------------------------

The AVERAGEA function returns the average of a set of supplied values. AVERAGEA will include the logical values TRUE and FALSE, and numbers represented as text in the calculation. The [AVERAGE function](https://exceljet.net/functions/average-function)
 ignores these values during calculation

AVERAGEA takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form of _value1, value2, value3_, etc. up to 255 total. Arguments can include numbers, cell references, ranges, arrays, and constants. Empty cells are ignored, but zero (0) values are included. 

### Examples

To average values in the range A1:A10, including logical the logical values TRUE (1) and FALSE (0) and numbers entered as text, use AVERAGEA like this:

    =AVERAGEA(A1:A10) // average numbers, logicals, numbers as text
    

One confusing aspect of the [AVERAGE function](https://exceljet.net/functions/average-function)
 compared to the AVERAGEA function is that both functions will evaluate logicals and numbers entered as text _when they are hardcoded as constants in a formula_:

    =AVERAGE(TRUE,2) // returns 1.5
    =AVERAGEA(TRUE,2) // returns 1.5
    =AVERAGE("3",2) // returns 2.5
    =AVERAGEA("3",2) // returns 2.5
    

However, the AVERAGE function _will_ ignore logicals or numbers entered as text _when they appear in cell references_. You can see this behavior in the worksheet example shown above.

### Notes

*   _Values_ can be supplied as numbers, ranges, named ranges, or cell references that contain values. Up to 255 arguments can be supplied.
*   To calculate the average, Excel adds the numeric value of each value together and divides by the total number of _values_ supplied.
*   AVERAGEA evaluates TRUE as 1 and FALSE as zero.

Related functions
-----------------

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel AVERAGEIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageif.png "Excel AVERAGEIF function")](https://exceljet.net/functions/averageif-function)

### [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)

The Excel AVERAGEIF function calculates the average of numbers in a range that meet supplied criteria. AVERAGEIF criteria can include logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching.

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)
    
*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    

### Links

*   [Microsoft AVERAGEA function documentation](https://support.office.com/en-us/article/averagea-function-f5f84098-d453-4f4c-bbba-3d2c66356091)
    

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