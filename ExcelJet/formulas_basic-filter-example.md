# Basic filter example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/basic-filter-example

---

[Skip to main content](https://exceljet.net/formulas/basic-filter-example#main-content)

[](https://exceljet.net/formulas/basic-filter-example#)

*   [Previous](https://exceljet.net/formulas/weighted-average)
    
*   [Next](https://exceljet.net/formulas/biggest-gainers-and-losers)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Basic filter example
====================

by Dave Bruns · Updated 2 Mar 2023

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")

Summary
-------

To query data and extract matching records, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
. In the example shown, the formula in G7 is:

    =FILTER(B5:E15,E5:E15=H4,"not found")
    

The result is recorded in the range B5:E15 where the State = "TX". Because FILTER returns more than one value, the results [spill](https://exceljet.net/glossary/spill)
 into the range G7:J10.

Generic formula
---------------

    =FILTER(data,range=value,"not found")

Explanation 
------------

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for the FILTER function, which is designed to return values that meet specific logical criteria from a set of data.

### FILTER function

The [FILTER function](https://exceljet.net/functions/filter-function)
 "filters" a range of data based on supplied criteria. In other words, the FILTER function will extract matching records from a set of data by applying one or more [logical tests](https://exceljet.net/glossary/logical-test)
. The result is an [array](https://exceljet.net/glossary/array)
 of matching values from the original data. The FILTER function takes three [arguments](https://exceljet.net/glossary/function-argument)
, and the generic syntax looks like this:

    =FILTER(array,include,[if_empty])

In this problem, _array_ is given as B5:E15, which contains the full set of data without headers:

    =FILTER(B5:E15,

The _include_ argument is an expression that runs a simple test for matching states:

    E5:E15=H4 // test state values
    

Placing this expression into FILTER as the second argument, we have:

    =FILTER(B5:E15,E5:E15=H4,

Finally, the optional _if\_empty_ argument is set to "not found" in case no matching data is found:

    =FILTER(B5:E15,E5:E15=H4,"not found")

Note the value for _if\_empty_ is a text string in double quotes (""). You can customize this message as you like. Supply an empty string ("") to display nothing. If you omit _if\_empty_ altogether, FILTER will return a #CALC! error when no data is returned.

When the formula above is entered, the _include_ argument is evaluated. Since there are 11 cells in the range E5:E11 and the value in H4 is "TX", the _include_ expression returns an array of 11 TRUE and FALSE like this:

    {TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE}
    

Notice the TRUE values in this array correspond to records in the data where the State is "TX". This array is used by the FILTER function to retrieve matching data. Only rows where the result is TRUE make it into the final output.

Video: [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

### Other fields and criteria

Other fields can be filtered in a similar way. For example, to filter the same data on orders that are greater than $100, you can use FILTER like this:

    =FILTER(B5:E15,C5:C15>100,"not found")
    

You can also configure the logic inside the _include_ argument to [apply more complex criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)
.

Related formulas
----------------

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: Filter exclude blank values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20exclude%20blank%20values.png "Excel formula: Filter exclude blank values")](https://exceljet.net/formulas/filter-exclude-blank-values)

### [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)

The FILTER function is designed to extract data that matches one or more criteria. In this case, we want to apply criteria that requires all three columns in the source data (Name, Group, and Room) to have data. In other words, if a row is missing any of these values, we want to exclude that row...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20is%20an%20array%3F-Play.png)](https://exceljet.net/videos/what-is-an-array)

### [What is an array?](https://exceljet.net/videos/what-is-an-array)

In this video, we'll answer the question "what is an array?" The term "array" comes from programming, but you'll hear it come up often in the context of more advanced Excel formulas. What does it really mean? An array is a structure or container that holds a collection of items. For example, this...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [What is an array?](https://exceljet.net/videos/what-is-an-array)
    

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