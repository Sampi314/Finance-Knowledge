# FILTER to remove columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-to-remove-columns

---

[Skip to main content](https://exceljet.net/formulas/filter-to-remove-columns#main-content)

[](https://exceljet.net/formulas/filter-to-remove-columns#)

*   [Previous](https://exceljet.net/formulas/filter-to-extract-matching-values)
    
*   [Next](https://exceljet.net/formulas/filter-to-show-duplicate-values)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

FILTER to remove columns
========================

by Dave Bruns · Updated 27 Jun 2024

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[MATCH](https://exceljet.net/functions/match-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6198/download?token=ONo7v4Dl)
 (14.53 KB)

![Excel formula: FILTER to remove columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/FILTER%20to%20remove%20columns.png "Excel formula: FILTER to remove columns")

Summary
-------

To filter columns, supply a horizontal array for the _include_ argument. In the example shown, the formula in I5 is:

    =FILTER(B5:G12,(B4:G4="a")+(B4:G4="c")+(B4:G4="e"))
    

The result is a filtered set of data that contains only columns A, C, and E from the source data.

Generic formula
---------------

    =FILTER(data,(header="a")+(header="b"))

Explanation 
------------

Although FILTER is more commonly used to filter rows, you can also filter columns, the trick is to supply an array with the same number of columns as the source data. In this example, we construct the array we need with [boolean logic](https://exceljet.net/glossary/boolean-logic)
, also called Boolean algebra.

In Boolean algebra, [multiplication corresponds to AND logic, and addition corresponds to OR logic](https://exceljet.net/videos/boolean-algebra-in-excel)
. In the example shown, we are using Boolean algebra with OR logic (addition) to target only the columns A, C, and E like this:

    (B4:G4="a")+(B4:G4="c")+(B4:G4="e")
    

After each expression is evaluated, we have three arrays of TRUE/FALSE values:

    {TRUE,FALSE,FALSE,FALSE,FALSE,FALSE}+
    {FALSE,FALSE,TRUE,FALSE,FALSE,FALSE}+
    {FALSE,FALSE,FALSE,FALSE,TRUE,FALSE}
    

The math operation (addition) converts the TRUE and FALSE values to 1s and 0s, so you can think of the operation like this:

    {1,0,0,0,0,0}+
    {0,0,1,0,0,0}+
    {0,0,0,0,1,0}
    

In the end, we have a single [horizontal array](https://exceljet.net/glossary/array)
 of 1s and 0s:

    {1,0,1,0,1,0}
    

which is delivered directly to the FILTER function as the _include_ argument:

    =FILTER(B5:G12,{1,0,1,0,1,0})
    

Notice there are 6 columns in the source data and 6 values in the array, all either 1 or 0. FILTER uses this array as a filter to include only columns 1, 3, and 5 from the source data. Columns 2, 4, and 6 are removed. In other words, the only columns that survive are associated with 1s.

### With the MATCH function

Applying OR logic with addition as shown above works fine, but it doesn't scale well, and makes it impossible to use a range of values from a worksheet as criteria. As an alternative, you can use the [MATCH function](https://exceljet.net/functions/match-function)
 together with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 like this to construct the _include_ argument more efficiently:

    =FILTER(B5:G12,ISNUMBER(MATCH(B4:G4,{"a","c","e"},0)))
    

The MATCH function is configured to look for all column headers in the [array constant](https://exceljet.net/glossary/array-constant)
 {"a","c","e"} as shown. We do it this way so that the result from MATCH has dimensions compatible with the source data, which contains 6 columns. Notice also that the third argument in MATCH is set as zero to force an exact match.

After MATCH runs, it returns an array like this:

    {1,#N/A,2,#N/A,3,#N/A}
    

This array goes directly into ISNUMBER, which returns another array:

    {TRUE,FALSE,TRUE,FALSE,TRUE,FALSE}
    

As above, this array is horizontal and contains 6 values separated by commas. FILTER uses the array to remove columns 2, 4, and 6.

### With a range

Since the column headers are already on the worksheet in the range I4:K4, the formula above can easily be adapted to use the range directly like this:

    =FILTER(B5:G12,ISNUMBER(MATCH(B4:G4,I4:K4,0)))
    

The range I4:K4 is evaluated as {"a","c","e"}, and behaves just like the array constant in the formula above.

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

[![Excel formula: Filter by column, sort by row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20by%20column%20sort%20by%20row.png "Excel formula: Filter by column, sort by row")](https://exceljet.net/formulas/filter-by-column-sort-by-row)

### [Filter by column, sort by row](https://exceljet.net/formulas/filter-by-column-sort-by-row)

Note: FILTER is a new dynamic array function in Excel 365 . In other versions of Excel, there are alternatives , but they are more complex. In this example, the goal is to filter the data shown in B5:G15 by year, then sort the results in descending order. In addition, the result should include the...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

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
    
*   [Filter by column, sort by row](https://exceljet.net/formulas/filter-by-column-sort-by-row)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

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