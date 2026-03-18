# Lookup first negative value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lookup-first-negative-value

---

[Skip to main content](https://exceljet.net/formulas/lookup-first-negative-value#main-content)

[](https://exceljet.net/formulas/lookup-first-negative-value#)

*   [Previous](https://exceljet.net/formulas/lookup-and-sum-column)
    
*   [Next](https://exceljet.net/formulas/lookup-last-file-version)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Lookup first negative value
===========================

by Dave Bruns · Updated 6 Dec 2022

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[FILTER](https://exceljet.net/functions/filter-function)

[TAKE](https://exceljet.net/functions/take-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7381/download?token=EuLg2SdU)
 (14.97 KB)

![Excel formula: Lookup first negative value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lookup%20first%20negative%20value.png "Excel formula: Lookup first negative value")

Summary
-------

To lookup the first negative value in a set of data, you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
. In the example shown, the formula in cell E5 is:

    =XLOOKUP(1,--(data[Low]<0),data)
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:C16. The result is the sixth row in the table, since this is the first negative value in the Low column. Because we provide **data** for _return\_array_, the result includes _both_ the date and the value. See below for details and alternatives.

Generic formula
---------------

    =XLOOKUP(1,--(range<0),range)

Explanation 
------------

In this example, the goal is to lookup the first negative value in a set of data. In addition, we also want to get the corresponding date. All data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 called **data,** in the range B5:C16. This information represents the low temperature in Fahrenheit (F) for the dates as shown. There are several ways to solve this problem, as explained below.

### XLOOKUP function

A simple solution is to use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 with [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. This is the approach in the workbook shown, where the formula in cell E5 is:

    =XLOOKUP(1,--(data[Low]<0),data)
    

Notice that _lookup\_value_ is given as 1. In this particular example, we _could_ use TRUE instead of 1. However, you will often see 1 used as a lookup value because it is compact, and because it will continue to work nicely as the logic to target specific values becomes more complex.

To target negative values, _lookup\_array_ is provided as this expression:

    --(data[Low]<0)
    

Since there are 12 values in **data\[Low\],** the result inside the parentheses is an [array](https://exceljet.net/glossary/array)
 of 12 TRUE and FALSE values like this:

    {FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE}
    

Because we have already set _lookup\_value_ to 1, we need to convert this array to the numeric values 1 and 0. The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is a simple way to perform this conversion. The resulting array looks like this:

    {0;0;0;0;0;1;0;0;0;1;1;0}
    

The 1s in this array correspond to the negative numbers in the Low column. The array is returned directly to XLOOKUP as the _lookup\_array_, so we can rewrite the formula at this point like this:

    =XLOOKUP(1,{0;0;0;0;0;1;0;0;0;1;1;0},data)
    

By default, XLOOKUP will match the _first_ occurrence of the _lookup\_value_, so it matches the 1 at row 6. Because the _return\_array_ is given as **data**, (B5:C16) XLOOKUP returns row 6 from the table as a final result. The two values in row 6 [spill](https://exceljet.net/glossary/spill)
 into cells E5 and F5 as shown.

As an alternative to the single formula above, you could use two separate formulas like this:

    =XLOOKUP(1,--(data[Low]<0),data[Date]) // date
    =XLOOKUP(1,--(data[Low]<0),data[Low]) // low
    

Notice the only difference in these formulas is the value given for the _result\_array._

### INDEX and MATCH

This problem can also be solved with an [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula like this:

    =INDEX(data,MATCH(1,--(data[Low]<0),0),0)
    

Notice that the [MATCH function](https://exceljet.net/functions/match-function)
 is configured like the XLOOKUP function above. Also note that _column\_num_ inside INDEX is given as 0, to cause the [INDEX function](https://exceljet.net/functions/index-function)
 to return [an entire row](https://exceljet.net/formulas/look-up-entire-row)
 of data (i.e. both Date and Low). After the expression **data\[Low\]<0** is evaluated and converted to 1s and 0s, we have:

    =INDEX(data,MATCH(1,{0;0;0;0;0;1;0;0;0;1;1;0},0),0)
    

Next, MATCH returns the position of the first 1 in _lookup\_array_ (6) to INDEX as _row\_num:_

    =INDEX(data,6,0)
    

Finally, INDEX returns row 6 from **data** as a final result. As with XLOOKUP above, you could also use two separate formulas like this:

    =INDEX(data,MATCH(1,--(data[Low]<0),0),1) // date
    =INDEX(data,MATCH(1,--(data[Low]<0),0),2) // low
    

Notice the only difference is the value provided for _column\_num_.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 that must be entered with Control + Shift + Enter in [Legacy Excel.](https://exceljet.net/glossary/legacy-excel)
_

### FILTER function

Another interesting way  to solve this problem is to use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [TAKE function](https://exceljet.net/functions/take-function)
 like this:

    =TAKE(FILTER(data,data[Low]<0),1)
    

Working from the inside out, FILTER is given **data** for _array_, and  the expression **data\[Low\]<0** for the _include_ [argument](https://exceljet.net/glossary/function-argument)
. With this configuration, FILTER returns the 3 rows in **data** that have negative values in the Low column. Note that the result from FILTER includes both columns, Date and Low. This data is returned directly to the TAKE function as the _array_ argument, with _row_ given as 1. TAKE then returns just row 1 from the matching data as a final result.

TAKE is a new function currently still in [beta](https://exceljet.net/version/beta)
. If you have a version of Excel without take, you can use INDEX instead like this:

    =INDEX(FILTER(data,data[Low]<0),1)
    

_Note: Without the TAKE or INDEX, FILTER will return and display all 3 rows in **data** that have negative values in the Low column._

Related formulas
----------------

[![Excel formula: Lookup lowest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20lowest%20value.png "Excel formula: Lookup lowest value")](https://exceljet.net/formulas/lookup-lowest-value)

### [Lookup lowest value](https://exceljet.net/formulas/lookup-lowest-value)

Working from the inside out, the MIN function is used to find the lowest bid in the range C5:C9: MIN(C5:C9) // returns 99500 The result, 99500, is fed into the MATCH function as the lookup value: MATCH(99500,C5:C9,0) // returns 4 Match then returns the location of this value in the range, 4, which...

[![Excel formula: Lookup lowest Monday tide](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20lowest%20monday%20tide.png "Excel formula: Lookup lowest Monday tide")](https://exceljet.net/formulas/lookup-lowest-monday-tide)

### [Lookup lowest Monday tide](https://exceljet.net/formulas/lookup-lowest-monday-tide)

At a high level, this example is about finding a minimum value based on multiple criteria. To do that, we are using the MIN function together with two nested IF functions : {=MIN(IF(day=I5,IF(tide="L",pred)))} working from the inside out, the first IF checks if the day is "Mon", based on the value...

[![Excel formula: XLOOKUP with Boolean OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20boolean%20OR%20logic.png "Excel formula: XLOOKUP with Boolean OR logic")](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)

### [XLOOKUP with Boolean OR logic](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)

In this example, the goal is to use XLOOKUP to find the first "red" or "pink" record in the data as shown. All data is in an Excel Table named data in the range B5:E14. This means the formulas below use structured references . As a result, the formulas will automatically include new data added to...

[![Excel formula: Get information about max value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_information_corresponding_to_max_value.png "Excel formula: Get information about max value")](https://exceljet.net/formulas/get-information-about-max-value)

### [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)

An interesting problem in Excel is how to look up information related to the maximum value in a set of data. For example, if you have a dataset of property listings and prices, you might want to find details about the property with the highest price. The best way to solve this problem depends on...

[![Excel formula: Sum first n matching values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20first%20n%20matching%20values_0.png "Excel formula: Sum first n matching values")](https://exceljet.net/formulas/sum-first-n-matching-values)

### [Sum first n matching values](https://exceljet.net/formulas/sum-first-n-matching-values)

In this example, the goal is to sum the first n matching values in a set of data. Specifically, we want to sum the first 3 values for both Red and Blue, based on the order they appear in the table. There are 12 values total; 6 entries each for Red and Blue. All data is in Excel Table named data in...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Lookup lowest value](https://exceljet.net/formulas/lookup-lowest-value)
    
*   [Lookup lowest Monday tide](https://exceljet.net/formulas/lookup-lowest-monday-tide)
    
*   [XLOOKUP with Boolean OR logic](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)
    
*   [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)
    
*   [Sum first n matching values](https://exceljet.net/formulas/sum-first-n-matching-values)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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