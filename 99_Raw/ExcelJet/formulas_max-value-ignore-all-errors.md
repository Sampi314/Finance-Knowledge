# Max value ignore all errors - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/max-value-ignore-all-errors

---

[Skip to main content](https://exceljet.net/formulas/max-value-ignore-all-errors#main-content)

[](https://exceljet.net/formulas/max-value-ignore-all-errors#)

*   [Previous](https://exceljet.net/formulas/max-of-every-nth-column)
    
*   [Next](https://exceljet.net/formulas/max-value-on-given-weekday)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Max value ignore all errors
===========================

by Dave Bruns · Updated 8 Feb 2023

Related functions 
------------------

[AGGREGATE](https://exceljet.net/functions/aggregate-function)

[MAXIFS](https://exceljet.net/functions/maxifs-function)

![Excel formula: Max value ignore all errors](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/max_value_ignore_all_errors.png "Excel formula: Max value ignore all errors")

Summary
-------

To get the maximum value in a set of data while ignoring all errors, you can use the [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
 with an option to ignore errors. In the example shown, the formula in D5 is:

    =AGGREGATE(4,6,B5:B16)

The result is the maximum value in B5:B16 (100) ignoring the two errors that appear in the range.

Generic formula
---------------

    =AGGREGATE(4,6,data)

Explanation 
------------

In this example, the goal is to return the maximum value in a set of data while ignoring any errors that might exist. This problem can be solved with the AGGREGATE function or with the MAXIFS function, as explained below.

### MAX with errors

The standard way to retrieve the maximum value in a range of data is the [MAX function](https://exceljet.net/functions/max-function)
. However, if we try to use MAX like this:

    =MAX(B5:B16) // returns #N/A

The MAX function returns #N/A as a result because the range B5:B16 contains errors. The problem with MAX is that it will return an error if the data contains errors.

### AGGREGATE function

The [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
 is a useful function that can run an aggregate calculation like AVERAGE, COUNT, MAX, MIN, etc., while optionally ignoring errors. A total of 19 operations are available, specified by a function number provided as the first argument. The [table here](https://exceljet.net/functions/aggregate-function#function_numbers)
 contains a complete list of available operations. In this case we want to use the number 4 for _function\_num_, which specifies the MAX operation. For the second argument, _options_, we provide the number 6, which indicates "ignore all errors". For _array_, we provide the range B5:B16. The final formula looks like this:

    =AGGREGATE(4,6,B5:B16)
    

To recap, the number 4 specifies MAX, and the number 6 is an option to ignore errors. With these settings, AGGREGATE returns the maximum value in the range, which is 100.

### Alternative with MAXIFS

Another way to solve this problem is with the [MAXIFS function](https://exceljet.net/functions/maxifs-function)
, which can calculate a max value after applying one or more conditions to filter out unwanted values. If values in the data set are known to be positive, a simple way to ignore errors is to check for values greater than zero like this:

    =MAXIFS(data,data,">0")

This works because the "greater or equal to zero" expression effectively removes error values, and MAXIFS returns the maximum value from the remaining 10 values, 100. You can also use the MAXIFS function with more specific criteria like this:

    =MAXIFS(data,data,"<>#N/A") // ignore NA errors
    =MAXIFS(data,data,"<>#DIV/0!") // ignore DIV/0 errors
    =MAXIFS(data,data,"<>#N/A",data,"<>#DIV/0!") // ignore both

All formulas above use the not equal to ("<>") [operator](https://exceljet.net/glossary/logical-operators)
. The first formula calculates a maximum after excluding #N/A errors. The second formula calculates a maximum after excluding #DIV/0! errors. The last formula uses two conditions to exclude both #N/A and #DIV/0! errors.

Related formulas
----------------

[![Excel formula: Average and ignore errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average%20and%20ignore%20errors2.png "Excel formula: Average and ignore errors")](https://exceljet.net/formulas/average-and-ignore-errors)

### [Average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)

In this example, the goal is to average a list of values that may contain errors. The values to average are in the named range data (B5:B15). Normally, you can use the AVERAGE function to calculate an average. However, if the data contains errors, AVERAGE will return an error. You can see this in...

[![Excel formula: Average numbers ignore zero](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_numbers_ignore_zero.png "Excel formula: Average numbers ignore zero")](https://exceljet.net/formulas/average-numbers-ignore-zero)

### [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)

In this example, the goal is to calculate an average of the quiz scores in columns C, D, E, and F for each person. However, the result needs to ignore any zeros that appear in the data. This formula can be easily solved with the AVERAGEIF function or the AVERAGEIFS function . It can also be solved...

Related functions
-----------------

[![Excel AGGREGATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20aggregate%20function.png "Excel AGGREGATE function")](https://exceljet.net/functions/aggregate-function)

### [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)

The Excel AGGREGATE function returns an aggregate calculation like AVERAGE, COUNT, MAX, etc., optionally ignoring hidden rows and errors. A total of 19 operations are available, specified by function number in the first argument (see table for options).

[![Excel MAXIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxifs%20function.png "Excel MAXIFS function")](https://exceljet.net/functions/maxifs-function)

### [MAXIFS Function](https://exceljet.net/functions/maxifs-function)

The Excel MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MAXIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)
    
*   [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)
    

### Functions

*   [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)
    
*   [MAXIFS Function](https://exceljet.net/functions/maxifs-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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