# Standard deviation calculation - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/standard-deviation-calculation

---

[Skip to main content](https://exceljet.net/formulas/standard-deviation-calculation#main-content)

[](https://exceljet.net/formulas/standard-deviation-calculation#)

*   [Previous](https://exceljet.net/formulas/square-root-of-number)
    
*   [Next](https://exceljet.net/formulas/student-class-enrollment-with-table)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Standard deviation calculation
==============================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[STDEV.P](https://exceljet.net/functions/stdev.p-function)

[STDEV.S](https://exceljet.net/functions/stdev.s-function)

[STDEV](https://exceljet.net/functions/stdev-function)

[STDEVP](https://exceljet.net/functions/stdevp-function)

![Excel formula: Standard deviation calculation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/standard%20deviation%20calculation.png "Excel formula: Standard deviation calculation")

Summary
-------

To calculate the standard deviation of a data set, you can use the [STDEV.S](https://exceljet.net/functions/stdev.s-function)
 or [STDEV.P](https://exceljet.net/functions/stdev.p-function)
 function, depending on whether the data set is a sample, or represents the entire population. In the example shown, the formulas in F6 and F7 are:

    =STDEV.P(C5:C14) // F6
    =STDEV.S(C5:C14) // F7

Explanation 
------------

### Standard deviation in Excel

Standard deviation is a measure of how much variance there is in a set of numbers compared to the average (mean) of the numbers. To calculate standard deviation in Excel, you can use one of two primary functions, depending on the data set. If the data represents the entire population, you can use the [STDEV.P function](https://exceljet.net/functions/stdev.p-function)
. IF the data is just a sample, and you want to extrapolate to the entire population, you can use the [STDEV.S function](https://exceljet.net/functions/stdev.s-function)
 to correct for sample bias as explained below. Both functions are fully automatic.

### Bessel’s correction, STDEV.P vs. STDEV.S

When you calculate statistics for an entire population (mean, variance, etc.) results are accurate because all data is available. However, when you calculate statistics for a sample, results are estimates and therefore not as accurate.

[Bessel's correction](https://mathcenter.oxford.emory.edu/site/math117/besselCorrection/)
 is an adjustment made to correct for bias that occurs when working with sample data. It appears in formulas as n-1, where n is the count. When working with a sample population, Bessel's correction can provide a better estimation of the standard deviation. In the context of Excel and standard deviation, the key thing to understand is:

*   The STDEV.S function uses Bessel's correction
*   The STDEV.P function does not

When should you use STDEV.S, which includes Bessel’s correction? It depends. 

*   If you have data for an entire population, use STDEV.P
*   If you have an appropriately large sample _and_ you want to approximate standard deviation for the entire population, use the STDEV.S function.
*   If you have sample data, and only want standard deviation for the sample, without extrapolating for the entire population, use the STDEV.P function.

Remember that a small sample is not likely to be a good approximation of a population in most cases. On the other hand, a large enough sample size will approach the statistics produced for a population. In these cases, Bessel’s correction may not be useful.

### Manual calculations for standard deviation

The screen below shows how to manually calculate standard deviation in Excel.

![Example of manual calculation for standard deviation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/standard%20deviation%20calculation%20long%20form.png?itok=xFOAPB4j "Example of manual calculation for standard deviation")

Column D calculates Deviation, which the value minus mean. The formula in D5, copied down is:

    =C5-AVERAGE($C$5:$C$14)
    

Column E shows deviations squared. The formula in E5, copied down is:

    =(D5)^2
    

In H5 we calculate standard deviation for the population with this formula:

    =SQRT(SUM(E5:E14)/COUNT(E5:E14))
    

In H6 we calculate standard deviation for a sample with a formula that uses Bessel’s correction:

    =SQRT(SUM(E5:E14)/(COUNT(E5:E14)-1))
    

### Older functions

You may notice that Excel contains older functions, [STDEVP](https://exceljet.net/functions/dstdevp-function)
 and [STDEV](https://exceljet.net/functions/stdev-function)
 which also calculate standard deviation. In short:

*   STDEV.P replaces the STDEVP function, with identical behavior.
*   STDEV.S replaces the STDEV function, with identical behavior.

Although STDEVP and STDEV still exist for backwards compatibility, Microsoft recommends that people use the newer STDEV.P and STDEV.S functions instead.

Related formulas
----------------

[![Excel formula: Basic average example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic_average_example.png "Excel formula: Basic average example")](https://exceljet.net/formulas/basic-average-example)

### [Basic average example](https://exceljet.net/formulas/basic-average-example)

In this example, the goal is to calculate a quiz score average for each person listed in column D using the four scores in columns C, D, E, and F. The standard way to solve this problem in Excel is to use the AVERAGE function . AVERAGE function The AVERAGE function calculates the average (...

[![Excel formula: Coefficient of variation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/coefficient%20of%20variation.png "Excel formula: Coefficient of variation")](https://exceljet.net/formulas/coefficient-of-variation)

### [Coefficient of variation](https://exceljet.net/formulas/coefficient-of-variation)

The coefficient of variation measures the relative variability of data with respect to the mean. It represents a ratio of the standard deviation to the mean and can be a useful way to compare data series when means are different. It is sometimes called relative standard deviation (RSD). In this...

Related functions
-----------------

[![Excel STDEV.P function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdev.p.png "Excel STDEV.P function")](https://exceljet.net/functions/stdev.p-function)

### [STDEV.P Function](https://exceljet.net/functions/stdev.p-function)

The Excel STDEV.P function calculates the standard deviation for a sample set of data. STDEV.P calculates standard deviation using the "n" method, ignoring logical values and text.

[![Excel STDEV.S function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdev.s.png "Excel STDEV.S function")](https://exceljet.net/functions/stdev.s-function)

### [STDEV.S Function](https://exceljet.net/functions/stdev.s-function)

The Excel STDEV.S function calculates the standard deviation for a sample set of data. STDEV.S replaces the older STDEV function, with the same behavior.

[![Excel STDEV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdev.png "Excel STDEV function")](https://exceljet.net/functions/stdev-function)

### [STDEV Function](https://exceljet.net/functions/stdev-function)

The Excel STDEV function returns the standard deviation for data that represents a sample. To calculate the standard deviation for an entire population, use STDEVP or STDEV.P.

[![Excel STDEVP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdevp.png "Excel STDEVP function")](https://exceljet.net/functions/stdevp-function)

### [STDEVP Function](https://exceljet.net/functions/stdevp-function)

The STDEVP function calculates the standard deviation for data that represents a population. STDEVP has been replaced with a newer function called STDEV.P, which has the same behavior.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Basic average example](https://exceljet.net/formulas/basic-average-example)
    
*   [Coefficient of variation](https://exceljet.net/formulas/coefficient-of-variation)
    

### Functions

*   [STDEV.P Function](https://exceljet.net/functions/stdev.p-function)
    
*   [STDEV.S Function](https://exceljet.net/functions/stdev.s-function)
    
*   [STDEV Function](https://exceljet.net/functions/stdev-function)
    
*   [STDEVP Function](https://exceljet.net/functions/stdevp-function)
    

### Links

*   [Sample vs Population standard deviation (math.stackexchange.com)](https://math.stackexchange.com/questions/15098/sample-standard-deviation-vs-population-standard-deviation)
    
*   [Standard Deviation (wikipedia)](https://en.wikipedia.org/wiki/Standard_deviation)
    

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