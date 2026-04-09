# Unique values by count - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/unique-values-by-count

---

[Skip to main content](https://exceljet.net/formulas/unique-values-by-count#main-content)

[](https://exceljet.net/formulas/unique-values-by-count#)

*   [Previous](https://exceljet.net/formulas/unique-values)
    
*   [Next](https://exceljet.net/formulas/unique-values-case-sensitive)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Unique values by count
======================

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[FILTER](https://exceljet.net/functions/filter-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Unique values by count](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/unique%20values%20by%20count.png "Excel formula: Unique values by count")

Summary
-------

To extract a list of unique values from a set of data, filtered by count or occurrence, you can use [UNIQUE](https://exceljet.net/functions/unique-function)
 with [FILTER](https://exceljet.net/functions/filter-function)
, and apply criteria with the [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the example shown, the formula in D5 is:

    =UNIQUE(FILTER(data,COUNTIF(data,data)>1))
    

which outputs the 3 unique values that appear more than once in the [named range](https://exceljet.net/glossary/named-range)
 **data** (B5:B16).

_Note: In this example, we are extracting a unique list of values that appear more than once. In other words, we are creating a list of duplicates :) The language is somewhat confusing._

Generic formula
---------------

    =UNIQUE(FILTER(data,COUNTIF(data,data)>n))

Explanation 
------------

This example uses the UNIQUE function together with the FILTER function. You can see a [more basic example here](https://exceljet.net/formulas/unique-values-with-criteria)
.

The trick in this case is to apply criteria to the FILTER function to only allow values based on the count of occurrence. Working from the inside out, this is done with COUNTIF and the FILTER function here:

    FILTER(data,COUNTIF(data,data)>1)
    

The result from COUNTIF is an array of counts like this:

    {3;1;3;3;2;1;1;3;1;2;3;3}
    

which are checked with the logical comparison > 1 to yield an array or TRUE/FALSE values:

    {TRUE;FALSE;TRUE;TRUE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE;TRUE;TRUE}
    

Notice TRUE corresponds to values in the data that appear more than once. This array is returned to FILTER as the _include_ argument, used to filter the data. FILTER returns another array as a result:

    {"red";"green";"green";"blue";"red";"blue";"red";"green"}
    

This array is returned directly to the UNIQUE function as the _array_ argument. Notice of the 12 original values, only 8 survive.

UNIQUE then removes duplicates, and returns the final array:

    {"red";"green";"blue"}
    

If values in B5:B16 change, the output will update immediately.

### Count > 2

The formula in F5, which lists colors appearing at least 2 times in the source data, is:

    =UNIQUE(FILTER(data,COUNTIF(data,data)>2))
    

### Dynamic source range

Because **data** (B5:B15) is a normal named range, it won't resize if data is added or deleted. To use a dynamic range that will automatically resize when needed, you can use an [Excel Table](https://exceljet.net/articles/excel-tables)
, or create a [dynamic named range](https://exceljet.net/glossary/dynamic-named-range)
 with a formula.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: Unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values.png "Excel formula: Unique values")](https://exceljet.net/formulas/unique-values)

### [Unique values](https://exceljet.net/formulas/unique-values)

This example uses the UNIQUE function, which is fully automatic. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. UNIQUE is a dynamic function. If any data in B5:B16 changes, the output from UNIQUE will update immediately...

[![Excel formula: Distinct values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/distinct%20values.png "Excel formula: Distinct values")](https://exceljet.net/formulas/distinct-values)

### [Distinct values](https://exceljet.net/formulas/distinct-values)

This example uses the UNIQUE function . With default settings, UNIQUE will output a list of unique values, i.e. values that appear one or more times in the source data. However, UNIQUE has an optional third argument, called occurs\_once that, when set to TRUE, will cause UNIQUE to return only values...

[![Excel formula: Unique values ignore blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20ignore%20blanks.png "Excel formula: Unique values ignore blanks")](https://exceljet.net/formulas/unique-values-ignore-blanks)

### [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)

This example uses the UNIQUE function together with the FILTER function. Working from the inside out, the FILTER function is first used to remove any blank values from the data: FILTER(B5:B16,B5:B16<>"") The <> symbol is a logical operator that means "does not equal". For more examples...

[![Excel formula: Extract unique items from a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20unique%20items%20from%20a%20list.png "Excel formula: Extract unique items from a list")](https://exceljet.net/formulas/extract-unique-items-from-a-list)

### [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)

The core of this formula is a basic lookup with INDEX: =INDEX(list,row) In other words, give INDEX the list and a row number, and INDEX will retrieve a value to add to the unique list. The hard work is figuring out the ROW number to give INDEX, so that we get unique values only. This is done with...

[![Excel formula: Unique values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20with%20criteria.png "Excel formula: Unique values with criteria")](https://exceljet.net/formulas/unique-values-with-criteria)

### [Unique values with criteria](https://exceljet.net/formulas/unique-values-with-criteria)

This example uses the UNIQUE function together with the FILTER function. Working from the inside out, the FILTER function is first used to remove limit data to values associated with group A only: FILTER(B5:B16,C5:C16=E4) Notice we are picking up the value "A" directly from the header in cell E4...

[![Excel formula: FILTER to show duplicate values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20to%20show%20duplicate%20values.png "Excel formula: FILTER to show duplicate values")](https://exceljet.net/formulas/filter-to-show-duplicate-values)

### [FILTER to show duplicate values](https://exceljet.net/formulas/filter-to-show-duplicate-values)

In this example, the goal is to list and count values that are duplicated in a set of data at least n times, where n is provided as a variable in cell D5. All data is in the named range data (B5:B16). In the worksheet shown, the formula used in cell F5 is: =UNIQUE(FILTER(data,COUNTIF(data,data)...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Unique values](https://exceljet.net/formulas/unique-values)
    
*   [Distinct values](https://exceljet.net/formulas/distinct-values)
    
*   [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)
    
*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    
*   [Unique values with criteria](https://exceljet.net/formulas/unique-values-with-criteria)
    
*   [FILTER to show duplicate values](https://exceljet.net/formulas/filter-to-show-duplicate-values)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

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