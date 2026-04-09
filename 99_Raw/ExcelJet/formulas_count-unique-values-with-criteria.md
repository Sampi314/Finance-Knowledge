# Count unique values with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-unique-values-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/count-unique-values-with-criteria#main-content)

[](https://exceljet.net/formulas/count-unique-values-with-criteria#)

*   [Previous](https://exceljet.net/formulas/count-unique-values)
    
*   [Next](https://exceljet.net/formulas/detailed-let-function-example)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Count unique values with criteria
=================================

by Dave Bruns · Updated 12 Nov 2025

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[FILTER](https://exceljet.net/functions/filter-function)

[LEN](https://exceljet.net/functions/len-function)

[SUM](https://exceljet.net/functions/sum-function)

[COUNTA](https://exceljet.net/functions/counta-function)

![Excel formula: Count unique values with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20unique%20values%20with%20criteria.png "Excel formula: Count unique values with criteria")

Summary
-------

To count unique values with one or more conditions, you can use a formula based on [UNIQUE](https://exceljet.net/functions/unique-function)
, [LEN](https://exceljet.net/functions/len-function)
, and [FILTER](https://exceljet.net/functions/filter-function)
. In the example shown, the formula in H7 is:

    =SUM(--(LEN(UNIQUE(FILTER(B6:B15,C6:C15=H6,"")))>0))
    

which returns 3, since there are three unique names in B6:B15 associated with Omega.

_Note: this formula requires_ [_Dynamic Array Formulas_](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
_, available only in_ [_Excel 365_](https://exceljet.net/glossary/excel-365)
_. With an older version of Excel, you can use_ [_more complex alternative formulas_](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
_._

Generic formula
---------------

    =SUM(--(LEN(UNIQUE(FILTER(range,criteria,"")))>0))

Explanation 
------------

In this example, the goal is to count unique values that meet one or more specific conditions. In the example shown, the formula used in cell H7 is:

    =SUM(--(LEN(UNIQUE(FILTER(B6:B15,C6:C15=H6,"")))>0))
    

At the core, this formula uses the FILTER function to apply criteria, and the UNIQUE function to extract the unique values that remain. Working from the inside out, the [FILTER function](https://exceljet.net/functions/filter-function)
 is used to apply criteria and extract only names that are associated with the "Omega" project:

    FILTER(B6:B15,C6:C15=H6,"") // Omega names only
    

Notice the _if\_empty_ argument in FILTER is set to an [empty string](https://exceljet.net/glossary/empty-string)
 (""), which is important due to the way we count final results. The result from FILTER is an [array](https://exceljet.net/glossary/array)
 like this:

    {"Jim";"Jim";"Carl";"Sue";"Carl"}
    

Next, the [UNIQUE function](https://exceljet.net/videos/the-unique-function)
 is used to remove duplicates:

    UNIQUE({"Jim";"Jim";"Carl";"Sue";"Carl"})
    

which results in a new array like this:

    {"Jim";"Carl";"Sue"} // after UNIQUE
    

At this point, we have a unique list of names associated with Omega, and we just need to count them. For reasons explained below, we do this with the LEN function and the SUM function. To make things clear, we'll first rewrite the formula to include the unique list:

    =SUM(--(LEN({"Jim";"Carl";"Sue"})>0))
    

The [LEN function](https://exceljet.net/functions/len-function)
 gets the length of each item in the list, and returns an array of lengths:

    LEN({"Jim";"Carl";"Sue"}) // returns {3;4;3}
    

Next, we check if lengths are greater than zero:

    LEN({3;4;3)>0 // returns {TRUE;TRUE;TRUE}
    

And use a [double negative](https://exceljet.net/glossary/double-unary)
 to coerce the TRUE and FALSE values to 1s and 0s:

    --({TRUE;TRUE;TRUE}) // returns {1;1;1}
    

Finally, we add up the results with the [SUM function](https://exceljet.net/functions/sum-function)
:

    =SUM({1;1;1}) // returns 3
    

Note that because we are checking the length of each item returned by UNIQUE, empty cells that meet criteria are ignored. Likewise, if FILTER returns an empty string (""), which has a length of zero, it will not be included in the count.

This formula is dynamic and will recalculate immediately if source data is changed.

### Count unique with multiple criteria

To count unique values based on multiple criteria, can extend the "include" logic inside FILTER. For example, to count unique names for the Omega project in June only, use:

    =SUM(--(LEN(UNIQUE(FILTER(B6:B15,(C6:C15=H6)*(D6:D15="june"),"")))>0))
    

This is an example of using [boolean logic](https://exceljet.net/glossary/boolean-logic)
 to apply more than one condition. The approach is [explained in more detail here](https://exceljet.net/formulas/unique-values-ignore-blanks)
.

For more details, see this training video: [How to filter with multiple criteria](https://exceljet.net/videos/how-to-filter-with-multiple-criteria)
.

### COUNTA

It is possible to write a simpler formula that relies on the [COUNTA function](https://exceljet.net/functions/counta-function)
. However, an important caveat is that COUNTA will return 1 when there are no matching values. This is because the FILTER function returns an error when no data matches criteria, and this error ends up being counted by the COUNTA function. The basic COUNTA formula looks like this: 

    =COUNTA(UNIQUE(FILTER(B6:B15,C6:C15=H6)))
    

Again, this formula will return 1 when there is no matching data. It will also include empty cells that meet criteria. The formula based on LEN and SUM is a better option.

### No dynamic arrays

If you are using an older version of Excel without dynamic array support, you can use a [more complex formula](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
. For a more general discussion of dynamic array alternatives, see [Alternatives to Dynamic Array Formulas](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are new in Excel.

Related formulas
----------------

[![Excel formula: Count unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20values.png "Excel formula: Count unique values")](https://exceljet.net/formulas/count-unique-values)

### [Count unique values](https://exceljet.net/formulas/count-unique-values)

This example uses the UNIQUE function to extract unique values. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. These are returned directly to the COUNTA function as an array like this: =COUNTA({"red";"amber";"green";"blue";"...

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

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_filter_with_multiple_criteria-thumb.png)](https://exceljet.net/videos/how-to-filter-with-multiple-criteria)

### [How to filter with multiple criteria](https://exceljet.net/videos/how-to-filter-with-multiple-criteria)

In this lesson we'll show you how to filter data using more than one column. Let's take a look. Here we have a table that contains 300 property listings. Each entry has information for price, address, property type, bedrooms, baths, square footage, cost per square foot, year built, and date listed...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count unique values](https://exceljet.net/formulas/count-unique-values)
    
*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    
*   [Distinct values](https://exceljet.net/formulas/distinct-values)
    
*   [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)
    
*   [Unique values with criteria](https://exceljet.net/formulas/unique-values-with-criteria)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    

### Videos

*   [How to filter with multiple criteria](https://exceljet.net/videos/how-to-filter-with-multiple-criteria)
    

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