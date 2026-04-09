# Count unique values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-unique-values

---

[Skip to main content](https://exceljet.net/formulas/count-unique-values#main-content)

[](https://exceljet.net/formulas/count-unique-values#)

*   [Previous](https://exceljet.net/formulas/count-unique-dates-ignore-time)
    
*   [Next](https://exceljet.net/formulas/count-unique-values-with-criteria)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Count unique values
===================

by Dave Bruns · Updated 6 Jan 2025

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[COUNTA](https://exceljet.net/functions/counta-function)

![Excel formula: Count unique values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20unique%20values.png "Excel formula: Count unique values")

Summary
-------

To count unique values in a set of data, you can use the [UNIQUE function](https://exceljet.net/functions/unique-function)
 together with the [COUNTA function](https://exceljet.net/functions/counta-function)
. In the example shown, the formula in F5 is:

    =COUNTA(UNIQUE(B5:B16))
    

which returns 7, since there are seven unique colors in B5:B16.

Generic formula
---------------

    =COUNTA(UNIQUE(data))

Explanation 
------------

This example uses the UNIQUE function to extract unique values. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. These are returned directly to the COUNTA function as an array like this:

    =COUNTA({"red";"amber";"green";"blue";"purple";"pink";"gray"})
    

Unlike the [COUNT function](https://exceljet.net/functions/count-function)
, which counts only numbers, COUNTA counts both text and numbers. Since there are seven items in _array_, COUNTA returns 7. This formula is dynamic and will recalculate immediately when source data is changed.

### With a cell reference

You can also refer to a list of unique values already extracted to the worksheet with the UNIQUE function using a special kind of cell reference. The formula in D5 is:

    =UNIQUE(B5:B16)
    

Which returns the seven values seen in D5:D11. To count these values with a dynamic reference, you can use a formula like this:

    =COUNTA(D5#)
    

The hash character (#) tells Excel to refer to the [spill range](https://exceljet.net/glossary/spill-range)
 created by UNIQUE. Like the all-in-one formula above, this formula is dynamic and will adapt when data is added or removed from the original range.

### Count unique and ignore blank cells

If blank (i.e., empty) cells exist in the range, the can increase the count by 1. The problem is that the empty cells evaluate to zero (0), and UNIQUE returns the zero along with other unique values. Then COUNTA counts the zero. To count unique values while ignoring blank cells, you can add the FILTER function like this:

    =COUNTA(UNIQUE(FILTER(data,data<>"")))
    

Here, FILTER is configured to select only non-empty cells, so empty cells are excluded and never make it to the UNIQUE function. This approach is [explained in more detail here](https://exceljet.net/formulas/unique-values-ignore-blanks)
. You can also filter [unique values with criteria](https://exceljet.net/formulas/unique-values-with-criteria)
.

### No data

One limitation of the formula above is that it will incorrectly return 1 even if there aren't _any_ values in the data range. This alternative formula will count all values returned by UNIQUE that have a length greater than zero. In other words, it will count all values with at least one character:

    =SUM(--(LEN(UNIQUE(B5:B16))>0))
    

Here, the [LEN function](https://exceljet.net/functions/len-function)
 is used to check the length of results from UNIQUE. The lengths are then checked to see if they are greater than zero, and results are counted with the SUM function. This is an example of [boolean logic](https://exceljet.net/glossary/boolean-logic)
. This formula will also exclude empty cells from results.

### Dynamic source range

UNIQUE won't automatically change the source range if data is added or deleted. To give UNIQUE a dynamic range that will automatically resize as needed, you can use an [Excel Table](https://exceljet.net/articles/excel-tables)
, or create a [dynamic named range](https://exceljet.net/glossary/dynamic-named-range)
 with a formula.

### No dynamic arrays

If you are using an older version of Excel without dynamic array support, [here are some alternatives](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are new in Excel.

Related formulas
----------------

[![Excel formula: Extract unique items from a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20unique%20items%20from%20a%20list.png "Excel formula: Extract unique items from a list")](https://exceljet.net/formulas/extract-unique-items-from-a-list)

### [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)

The core of this formula is a basic lookup with INDEX: =INDEX(list,row) In other words, give INDEX the list and a row number, and INDEX will retrieve a value to add to the unique list. The hard work is figuring out the ROW number to give INDEX, so that we get unique values only. This is done with...

[![Excel formula: Distinct values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/distinct%20values.png "Excel formula: Distinct values")](https://exceljet.net/formulas/distinct-values)

### [Distinct values](https://exceljet.net/formulas/distinct-values)

This example uses the UNIQUE function . With default settings, UNIQUE will output a list of unique values, i.e. values that appear one or more times in the source data. However, UNIQUE has an optional third argument, called occurs\_once that, when set to TRUE, will cause UNIQUE to return only values...

[![Excel formula: Unique values ignore blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20ignore%20blanks.png "Excel formula: Unique values ignore blanks")](https://exceljet.net/formulas/unique-values-ignore-blanks)

### [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)

This example uses the UNIQUE function together with the FILTER function. Working from the inside out, the FILTER function is first used to remove any blank values from the data: FILTER(B5:B16,B5:B16<>"") The <> symbol is a logical operator that means "does not equal". For more examples...

[![Excel formula: Unique values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20with%20criteria.png "Excel formula: Unique values with criteria")](https://exceljet.net/formulas/unique-values-with-criteria)

### [Unique values with criteria](https://exceljet.net/formulas/unique-values-with-criteria)

This example uses the UNIQUE function together with the FILTER function. Working from the inside out, the FILTER function is first used to remove limit data to values associated with group A only: FILTER(B5:B16,C5:C16=E4) Notice we are picking up the value "A" directly from the header in cell E4...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    
*   [Distinct values](https://exceljet.net/formulas/distinct-values)
    
*   [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)
    
*   [Unique values with criteria](https://exceljet.net/formulas/unique-values-with-criteria)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    

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