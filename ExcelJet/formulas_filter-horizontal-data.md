# Filter horizontal data - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-horizontal-data

---

[Skip to main content](https://exceljet.net/formulas/filter-horizontal-data#main-content)

[](https://exceljet.net/formulas/filter-horizontal-data#)

*   [Previous](https://exceljet.net/formulas/filter-exclude-blank-values)
    
*   [Next](https://exceljet.net/formulas/filter-last-n-valid-entries)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter horizontal data
======================

by Dave Bruns · Updated 11 Jul 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6368/download?token=dX9OvqfD)
 (15.72 KB)

![Excel formula: Filter horizontal data](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Filter%20horizontal%20data.png "Excel formula: Filter horizontal data")

Summary
-------

To filter data arranged horizontally in columns, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
.  In the example shown, the formula in C9 is:

    =TRANSPOSE(FILTER(data,group="fox"))
    

where **data** (C4:L6) and **group** (C5:L5) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =FILTER(data,logic)

Explanation 
------------

_Note: FILTER is a new [dynamic array](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 function in [Excel 365](https://exceljet.net/glossary/excel-365)
. In other versions of Excel, there are [alternatives](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
, but they are more complex._

There are ten columns of data in the range C4:L6. The goal is to filter this horizontal data and extract only columns (records) where the group is "fox". For convenience and readability, the worksheet contains three [named ranges](https://exceljet.net/glossary/named-range)
: **data** (C4:L6) and **group** (C5:L5), and **age** (C6:L6).

The [FILTER function](https://exceljet.net/functions/filter-function)
 can be used to extract data arranged vertically (in rows) or horizontally (in columns). FILTER will return the matching data in the same orientation.  No special setup is required. In the example shown, the formula in C9 is:

    =FILTER(data,group="fox")
    

Working from the inside out, the _include_ argument for FILTER is a logical expression:

    group="fox" // test for "fox"
    

When the logical expression is evaluated, it returns an array of 10 TRUE and FALSE values:

    {TRUE,FALSE,TRUE,FALSE,FALSE,TRUE,TRUE,TRUE,TRUE,FALSE}
    

_Note: the commas (,) [in this array](https://exceljet.net/glossary/array)
 indicate columns. Semicolons (;) would indicate rows._

The array contains one value per column in the data, and each TRUE corresponds to a column where the group is "fox". This array is returned directly to FILTER as the _include_ argument, and it performs the actual filtering:

    FILTER(data,{TRUE,FALSE,TRUE,FALSE,FALSE,TRUE,TRUE,TRUE,TRUE,FALSE})
    

Only data that corresponds to TRUE values passes the filter, so FILTER returns the 6 columns where the group is "fox". FILTER returns this data in the original horizontal structure. Because FILTER is a [dynamic array function](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, the results [spill](https://exceljet.net/glossary/spill)
 into the range C9:H11.

This is a dynamic solution – if any source data in C4:L6 changes, the results from FILTER automatically update.

### Transpose to vertical format

To transpose the results from FILTER into a vertical (rows) format, you can wrap the TRANSPOSE function around the FILTER function like this:

    =TRANSPOSE(FILTER(data,group="fox"))
    

The result looks like this:

![FILTER and TRANSPOSE horizontal data](https://exceljet.net/sites/default/files/images/formulas/inline/Filter%20horizontal%20data%20transposed.png "FILTER and TRANSPOSE horizontal data")

This formula is [explained in more detail here](https://exceljet.net/formulas/filter-and-transpose-horizontal-to-vertical)
.

### Filter on age

The same basic formula can be used to filter the data in different ways. For example, to filter data to show only columns where age is less than 22, you can use a formula like this:

    =FILTER(data,age<22)
    

FILTER returns the four matching columns of data:

![FILTER columns by age < 22](https://exceljet.net/sites/default/files/images/formulas/inline/Filter%20horizontal%20data%20by%20age.png "FILTER columns by age < 22")

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

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

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

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