# Filter and sort without errors - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-and-sort-without-errors

---

[Skip to main content](https://exceljet.net/formulas/filter-and-sort-without-errors#main-content)

[](https://exceljet.net/formulas/filter-and-sort-without-errors#)

*   [Previous](https://exceljet.net/formulas/filter-and-exclude-columns)
    
*   [Next](https://exceljet.net/formulas/filter-and-transpose-horizontal-to-vertical)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter and sort without errors
==============================

by Dave Bruns · Updated 9 Dec 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SORT](https://exceljet.net/functions/sort-function)

![Excel formula: Filter and sort without errors](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter_and_sort_without_errors.png "Excel formula: Filter and sort without errors")

Summary
-------

A formula based on the [FILTER](https://exceljet.net/functions/filter-function)
 and [SORT](https://exceljet.net/functions/sort-function)
 may return an error when no data is returned. To suppress certain errors when no data matches criteria, you can provide an [array constant](https://exceljet.net/glossary/array-constant)
 to FILTER to keep the SORT function happy. In the example shown, the formula in E8 is:

    =SORT(FILTER(data,(data[Date]>=F4)*(data[Date]<=F5),{"No data",""}),2)

where **data** is an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range B5:C15.

Generic formula
---------------

    =SORT(FILTER(data,include_logic,{"No data",""}),2)

Explanation 
------------

A common situation in Excel is to use the [SORT function](https://exceljet.net/functions/sort-function)
 to sort results returned by the [FILTER function](https://exceljet.net/functions/filter-function)
. However, a formula based on the FILTER and SORT may return an error when no data is returned. In this example, the goal is to create a formula based on FILTER and SORT that will not return an error when the FILTER function returns no data.

### Problem

The formula below returns a #CALC! error because there are no rows in the data with dates between April 1 and April 30:

    =SORT(FILTER(data,(data[Date]>=F4)*(data[Date]<=F5)),2)

![Example of #CALC! error with FILTER and SORT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/filter_and_sort_without_errors_-_error_example.png "Example of #CALC! error with FILTER and SORT")

This happens because when FILTER returns no data, it returns a #CALC error by default and this error "bubbles up" to SORT. You might try to handle this problem by providing a value for the _if\_empty_ argument in FILTER like this:

    =SORT(FILTER(data,(data[Date]>=F4)*(data[Date]<=F5),"No data"),2)

However, this causes the SORT function to return a #VALUE! error, because SORT is configured to sort by column index 2, and there is no second column when the text string "No data" is returned by FILTER:

![Example of #VALUE! error with FILTER and SORT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/filter_and_sort_without_errors_-_value_error_example.png "Example of #VALUE! error with FILTER and SORT")

In other words, when FILTER returns "No data" as a result, the configuration for SORT no longer works.

### Solution

One solution to the problem described above is to provide an [array constant](https://exceljet.net/glossary/array-constant)
 like this to FILTER as the _if\_empty_ argument:

    {"No data",""}) // array constant

The array constant is set up to be a [horizontal array](https://exceljet.net/glossary/array)
 by using a comma instead of a semi-colon. The first cell contains "No data" and the second cell is empty. The entire formula looks like this:

    =SORT(FILTER(data,(data[Date]>=F4)*(data[Date]<=F5),{"No data",""}),2)

Now when FILTER returns no data, it returns the message "No data" as a two column array constant, and the SORT function harmlessly "sorts" the array constant by the second column and returns it unchanged to cell E8 where it spills into the range E8:F8:

![Example of FILTER and SORT without errors](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/filter_and_sort_without_errors.png "Example of FILTER and SORT without errors")

### Array constant size

In general, you should adjust the array constant to match the number of columns in the data supplied to FILTER. For example, if the data had 4 columns, you could use an array constant with 4 values like this:

    {"No data","","",""} // 4 values

This allows the SORT function to be configured to sort by any column without an error. Also note you can supply whatever values you like in the array constant; empty strings are not required.

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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