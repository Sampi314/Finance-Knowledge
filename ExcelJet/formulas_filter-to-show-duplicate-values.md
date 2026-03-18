# FILTER to show duplicate values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-to-show-duplicate-values

---

[Skip to main content](https://exceljet.net/formulas/filter-to-show-duplicate-values#main-content)

[](https://exceljet.net/formulas/filter-to-show-duplicate-values#)

*   [Previous](https://exceljet.net/formulas/filter-to-remove-columns)
    
*   [Next](https://exceljet.net/formulas/filter-values-within-tolerance)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

FILTER to show duplicate values
===============================

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[FILTER](https://exceljet.net/functions/filter-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: FILTER to show duplicate values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20to%20show%20duplicate%20values.png "Excel formula: FILTER to show duplicate values")

Summary
-------

To list duplicate values in a set of data based on a threshold count, you can use a formula based on [FILTER](https://exceljet.net/functions/filter-function)
, [UNIQUE](https://exceljet.net/functions/unique-function)
, and the [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the example shown, the formula in F5 is:

    =UNIQUE(FILTER(data,COUNTIF(data,data)>=D5))
    

This formula lists the duplicate values in the [named range](https://exceljet.net/glossary/named-range)
 **data** (B5:B16) using the "Min count" value in D5 as a minimum threshold. In other words, a value must occur in the data at least as many times as the number in D5.  The result from the formula is dynamic and will change if the number in D5 is changed.

Explanation 
------------

In this example, the goal is to list and count values that are duplicated in a set of data at least **n** times, where **n** is provided as a variable in cell D5. All data is in the [named range](https://exceljet.net/glossary/named-range)
 **data** (B5:B16). In the worksheet shown, the formula used in cell F5 is:

    =UNIQUE(FILTER(data,COUNTIF(data,data)>=D5))
    

Working from the inside out, the first step is to count the values in **data**. This is done with the [COUNTIF function](https://exceljet.net/functions/countif-function)
 like this:

    COUNTIF(data,data) // get all counts
    

Because there are 12 values in **data**, and **data** is used for both _range_ and _criteria_, COUNTIF returns an [array](https://exceljet.net/glossary/array)
 with 12 counts as a result:

    {4;1;3;1;2;4;2;3;1;4;3;4} // result from COUNTIF
    

Each number represents the count of one value in **data**. For example, because "Red" is the first value in **data**, and because "Red" occurs 4 times total, the first number in the array is 4. The next step is to compare these counts to the "Min count" in D5:

    =COUNTIF(data,data)>=D5
    ={4;1;3;1;2;4;2;3;1;4;3;4}>=D5
    

Cell D5 contains 2, so the result is an [array](https://exceljet.net/glossary/array)
 of 12 TRUE and FALSE values like this:

    ={TRUE;FALSE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE}
    

Each TRUE in this array represents a value that occurs at least 2 times in the data. This array is returned directly to the [FILTER function](https://exceljet.net/functions/filter-function)
 as the _include_ [argument](https://exceljet.net/glossary/function-argument)
, and FILTER uses the array to return values that correspond to TRUE. These are values that occur at least twice in the data:

    {"Red";"Green";"Purple";"Red";"Purple";"Green";"Red";"Green";"Red"}
    

FILTER returns the array to the [UNIQUE function](https://exceljet.net/videos/the-unique-function)
, and UNIQUE returns unique values:

    {"Red";"Green";"Purple"}
    

These values [spill](https://exceljet.net/glossary/spill)
 into range F5:F7 as the final result. Notice each of these values occurs at least 2 times in **data**.

### Summary count

To get the summary count seen in column G, the formula in G5 is:

    =COUNTIF(data,F5#)
    

With **data** as _range_, and the spill range F5# as _criteria_, COUNTIF returns the count that each value in column F appears in **data**.

### Dynamic source range

Because **data** (B5:B16) is a normal named range, it won't resize if data is added or deleted. To use a dynamic range that will automatically resize when needed, you can use an [Excel Table](https://exceljet.net/articles/excel-tables)
, or create a [dynamic named range](https://exceljet.net/glossary/dynamic-named-range)
 with a formula.

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

[![Excel formula: Unique values by count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20by%20count.png "Excel formula: Unique values by count")](https://exceljet.net/formulas/unique-values-by-count)

### [Unique values by count](https://exceljet.net/formulas/unique-values-by-count)

This example uses the UNIQUE function together with the FILTER function. You can see a more basic example here . The trick in this case is to apply criteria to the FILTER function to only allow values based on the count of occurrence. Working from the inside out, this is done with COUNTIF and the...

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
    
*   [Unique values by count](https://exceljet.net/formulas/unique-values-by-count)
    

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