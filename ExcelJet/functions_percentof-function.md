# Excel PERCENTOF function | Exceljet

**Source:** https://exceljet.net/functions/percentof-function

---

[Skip to main content](https://exceljet.net/functions/percentof-function#main-content)

[](https://exceljet.net/functions/percentof-function#)

*   [Previous](https://exceljet.net/functions/map-function)
    
*   [Next](https://exceljet.net/functions/pivotby-function)
    

Excel 365

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

PERCENTOF Function
==================

by Dave Bruns · Updated 11 Mar 2025

Related functions 
------------------

[GROUPBY](https://exceljet.net/functions/groupby-function)

[PIVOTBY](https://exceljet.net/functions/pivotby-function)

![Excel PERCENTOF function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_percentof_function.png "Excel PERCENTOF function")

Summary
-------

The Excel PERCENTOF function is designed to calculate the percentage of a subset of data with respect to all data. The output from PERCENTOF is a decimal number that can be formatted with Excel's percentage number format.

Purpose 
--------

Return a subset of data as a percentage of all data

Return value 
-------------

A decimal value that represents the percentage

Syntax
------

    =PERCENTOF(data_subset,all_data)

*   _data\_subset_ - A subset of data as a range or array.
*   _all\_data_ - All data as a range or array.

Using the PERCENTOF function 
-----------------------------

The PERCENTOF function is designed to return a subset of data as a percentage of a larger data set. The output from PERCENTOF is a decimal number that can be formatted with Excel's percentage number format. Essentially, PERCENTOF performs a calculation like this:

    =SUM(data_subset)/SUM(data_all)

The result will be a decimal number that must be [formatted as a percentage](https://exceljet.net/glossary/percentage-number-format)
. For example, if the subset of data is 250 and the full set of data is 1000, PERCENTOF will return 0.25:

    =PERCENTOF(250,1000) // returns 0.25

When 0.25 is formatted as a percentage, it will display as 25% on the worksheet.

### Worksheet Example

In the worksheet shown above, the formula in cell D5 looks like this:

    =PERCENTOF(C5,$C$5:$C$12)

The result is 37% (0.37) since $950 is 37% of the sum of the range C5:C12, which is $2570. As the formula is copied down, it returns each value in column C5:C12 as a percentage of $2570.

> Although PERCENTOF will work fine on its own, it was originally introduced as a companion to the [GROUPBY](https://exceljet.net/functions/groupby-function)
>  and [PIVOTBY](https://exceljet.net/functions/pivotby-function)
>  functions to provide a simple way to show data subsets as percentages in the output of these functions.

PERCENTOF function examples
---------------------------

[![Excel formula: GROUPBY with survey results](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/groupby_with_survey_results.png "Excel formula: GROUPBY with survey results")](https://exceljet.net/formulas/groupby-with-survey-results)

### [GROUPBY with survey results](https://exceljet.net/formulas/groupby-with-survey-results)

In May 2025, I ran a survey asking Exceljet newsletter subscribers what version of Excel they use most. This is an important question for Excel learning because the new dynamic array engine has completely changed how many formulas are written. These changes started rolling out after Excel 2019, so...

Related functions
-----------------

[![Excel GROUPBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_groupby_function.png "Excel GROUPBY function")](https://exceljet.net/functions/groupby-function)

### [GROUPBY Function](https://exceljet.net/functions/groupby-function)

The Excel GROUPBY function is designed to summarize data by grouping rows and aggregating values. The result is a summary table created with a single formula.

[![Excel PIVOTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_pivotby_function.png "Excel PIVOTBY function")](https://exceljet.net/functions/pivotby-function)

### [PIVOTBY Function](https://exceljet.net/functions/pivotby-function)

The Excel PIVOTBY function is designed to summarize data by grouping rows and columns. The result is a dynamic summary table created with a single formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [GROUPBY with survey results](https://exceljet.net/formulas/groupby-with-survey-results)
    

### Functions

*   [GROUPBY Function](https://exceljet.net/functions/groupby-function)
    
*   [PIVOTBY Function](https://exceljet.net/functions/pivotby-function)
    

### Links

*   [Microsoft PERCENTOF function documentation](https://support.microsoft.com/en-us/office/percentof-function-7c66da0a-ac30-45d0-bfc7-834a8bd7c962)
    

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