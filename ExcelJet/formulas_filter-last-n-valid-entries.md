# FILTER last n valid entries - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-last-n-valid-entries

---

[Skip to main content](https://exceljet.net/formulas/filter-last-n-valid-entries#main-content)

[](https://exceljet.net/formulas/filter-last-n-valid-entries#)

*   [Previous](https://exceljet.net/formulas/filter-horizontal-data)
    
*   [Next](https://exceljet.net/formulas/filter-on-first-or-last-n-values)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

FILTER last n valid entries
===========================

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[INDEX](https://exceljet.net/functions/index-function)

![Excel formula: FILTER last n valid entries](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20last%20n%20valid%20entries.png "Excel formula: FILTER last n valid entries")

Summary
-------

To FILTER and extract the last n "valid" entries based on a logical test, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 together with [INDEX](https://exceljet.net/functions/index-function)
 and [SEQUENCE](https://exceljet.net/functions/sequence-function)
. In the example shown, the formula in F5 is:

    =INDEX(FILTER(data,temp<75),SORT(SEQUENCE(3,1,SUM(--(temp<75)),-1)),SEQUENCE(1,COLUMNS(data)))
    

where **data** (B5:D15) and **temp** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
 .

Generic formula
---------------

    =INDEX(FILTER(data,logic),SORT(SEQUENCE(n,1,SUM(--(logic)),-1)),SEQUENCE(1,COLUMNS(data)))

Explanation 
------------

The goal in this example is to display the last 3 valid entries from the table shown, where "valid" is defined as a temperature of less than 75 in the "Temp" column. At a high level, the FILTER function is used to filter entries based on a logical test, and the INDEX function is used to extract the last 3 entries from the filtered list. Working from the inside out, we use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 to construct a row number value for the [INDEX function](https://exceljet.net/functions/index-function)
 like this:

    SORT(SEQUENCE(3,1,SUM(--(temp<75)),-1))
    

SEQUENCE is configured to create an array of 3 rows x 1 column. The step value is -1, and the start number is defined by this snippet:

    SUM(--(temp<75)) // returns 7
    

Here we are counting temp values less than 75. Because the named range **temp** contains twelve values, the result is an [array](https://exceljet.net/glossary/array)
 of 12 TRUE and FALSE values:

    {TRUE;TRUE;TRUE;FALSE;FALSE;TRUE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE}
    

The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is used to coerce the TRUE and FALSE results to 1s and 0s, and the [SUM function](https://exceljet.net/videos/how-to-use-the-sum-function)
 returns the total:

    SUM({1;1;1;0;0;1;1;0;0;1;0;1}) // returns 7
    

This number is returned directly to SEQUENCE for the start value. Now we have:

    =SORT(SEQUENCE(3,1,7,-1))
    =SORT({7;6;5})
    ={5;6;7}
    
    

We use SORT to ensure that values are returned in the same order they appear in the source data. This array is handed off to the INDEX function as the _row\_num_ argument:

    =INDEX(FILTER(data,temp<75),{5;6;7},SEQUENCE(1,COLUMNS(data)))
    

In a similar way, SEQUENCE is also used to generate an array for columns:

    SEQUENCE(1,COLUMNS(data)) // returns {1,2,3}
    

which is given to INDEX for the _columns_ argument. Now we have:

    =INDEX(FILTER(data,temp<75),{5;6;7},{1,2,3})
    

The next step is to construct the array for INDEX to work with. We only want to work with "valid" entries, so we use the [FILTER function](https://exceljet.net/functions/filter-function)
 to retrieve a list of entries where the **temp** value is less than 75:

    FILTER(data,temp<75)
    

The _array_ argument is data, and the _include_ argument is the expression **temp**<75. This can be translated literally as "return values from the named range **data** where values in **temp** are less than 75". The result is a 2D [array](https://exceljet.net/glossary/array)
 with 3 columns and 7 rows:

    {"0100",72,5;"0101",74,8;"0102",74,7;"0105",72,8;"0106",71,6;"0109",74,9;"0111",72,8}
    

Notice rows associated **temp** values greater than or equal to 75 have been removed. This array is returned to the INDEX function for its _array_ argument.

Finally, the [INDEX function](https://exceljet.net/functions/index-function)
 returns the last 3 entries from the array returned by FILTER.

_Note: Both the value for **n** and the logic used to test for valid entries is arbitrary in this example and can be adjusted as needed to suit your needs._

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

[![Excel formula: FILTER on first or last n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20on%20first%20or%20last%20n%20values.png "Excel formula: FILTER on first or last n values")](https://exceljet.net/formulas/filter-on-first-or-last-n-values)

### [FILTER on first or last n values](https://exceljet.net/formulas/filter-on-first-or-last-n-values)

In this example, the goal is to extract the first 3 values or the last 3 values from the named range data (B5:B15). We also want to exclude any empty cells from our results. In the worksheet shown the formula in cell D5 is: =INDEX(FILTER(data,data<>""),SEQUENCE(3,1,1,1)) Working from the...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

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
    
*   [FILTER on first or last n values](https://exceljet.net/formulas/filter-on-first-or-last-n-values)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

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