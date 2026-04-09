# Excel DEVSQ function | Exceljet

**Source:** https://exceljet.net/functions/devsq-function

---

[Skip to main content](https://exceljet.net/functions/devsq-function#main-content)

[](https://exceljet.net/functions/devsq-function#)

*   [Previous](https://exceljet.net/functions/covariance.s-function)
    
*   [Next](https://exceljet.net/functions/expon.dist-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

DEVSQ Function
==============

by Dave Bruns · Updated 22 Sep 2021

Related functions 
------------------

[AVERAGE](https://exceljet.net/functions/average-function)

[STDEV](https://exceljet.net/functions/stdev-function)

[VAR](https://exceljet.net/functions/var-function)

[AVEDEV](https://exceljet.net/functions/avedev-function)

![Excel DEVSQ function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20devsq%20function.png "Excel DEVSQ function")

Summary
-------

The Excel DEVSQ function returns the sum of the squared deviations from the mean for a given set of data. 

Purpose 
--------

Get sum of squared deviations

Return value 
-------------

Calculated sum

Syntax
------

    =DEVSQ(number1,[number2],...)

*   _number1_ - First value or reference.
*   _number2_ - \[optional\] Second value or reference.

Using the DEVSQ function 
-------------------------

The Excel DEVSQ function calculates the sum of the squared deviations from the mean for a given set of data. Variance and standard deviation functions deal with negative deviations by squaring deviations before they are averaged. DEVSQ calculates the sum of the squared deviations from the mean, without dividing by N or by N-1.

The DEVSQ function takes multiple arguments in the form _number1_, _number2_, _number3_, etc. up to 255 total. Arguments can be a hardcoded constant, a cell reference, or a range. A single range or array can be provided instead of multiple arguments.

### Examples

In the example shown, the formula in G5 is:

    =DEVSQ(B5:B10)
    

The formulas in C5 and D5 are, respectively:

    =B5-$G$4 // deviation
    =C5^2 // squared deviation
    

The value in D12 (34) is simply the sum of D5:D10, and agrees with the value calculated directly by DEVSQ in G5.

### Notes

*   Arguments can be numbers, names, arrays, or references that contain numbers.
*   Empty cells, and cells that contain text or logical values are ignored.

Related functions
-----------------

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel STDEV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdev.png "Excel STDEV function")](https://exceljet.net/functions/stdev-function)

### [STDEV Function](https://exceljet.net/functions/stdev-function)

The Excel STDEV function returns the standard deviation for data that represents a sample. To calculate the standard deviation for an entire population, use STDEVP or STDEV.P.

[![Excel VAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_var.png "Excel VAR function")](https://exceljet.net/functions/var-function)

### [VAR Function](https://exceljet.net/functions/var-function)

The Excel VAR function estimates the variance of a sample of data. If data represents the entire population, use the VARP function or the newer VAR.P function. VAR ignores text values and logicals in references.

[![Excel AVEDEV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20avedev%20function.png "Excel AVEDEV function")](https://exceljet.net/functions/avedev-function)

### [AVEDEV Function](https://exceljet.net/functions/avedev-function)

The Excel AVEDEV function returns the average of the absolute value of deviations from the mean for a given set of data. Average deviation is a measure of variability.

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
    
*   [STDEV Function](https://exceljet.net/functions/stdev-function)
    
*   [VAR Function](https://exceljet.net/functions/var-function)
    
*   [AVEDEV Function](https://exceljet.net/functions/avedev-function)
    

### Links

*   [Microsoft DEVSQ function documentation](https://support.office.com/en-us/article/devsq-function-8b739616-8376-4df5-8bd0-cfe0a6caf444)
    

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