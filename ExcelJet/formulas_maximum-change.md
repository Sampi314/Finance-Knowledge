# Maximum change - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/maximum-change

---

[Skip to main content](https://exceljet.net/formulas/maximum-change#main-content)

[](https://exceljet.net/formulas/maximum-change#)

*   [Previous](https://exceljet.net/formulas/max-value-with-variable-column)
    
*   [Next](https://exceljet.net/formulas/maximum-if-multiple-criteria)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Maximum change
==============

by Dave Bruns · Updated 28 Apr 2025

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[LET](https://exceljet.net/functions/let-function)

[HSTACK](https://exceljet.net/functions/hstack-function)

[SORT](https://exceljet.net/functions/sort-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7732/download?token=NCdcURuZ)
 (15.79 KB)

![Excel formula: Maximum change](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/maximum_change.png "Excel formula: Maximum change")

Summary
-------

To calculate the maximum change in a set of data when the change itself is not part of the data, you can use an array formula that performs the change calculation inside the MAX function. In the example shown, the formula in F4 is:

    =MAX(data[High]-data[Low])
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D16. The result is 23, the maximum difference between high and low values in one day, which occurred on June 9 in the data as shown.

_Note: this is an_ [_array formula_](https://exceljet.net/glossary/array-formula)
 _and must be entered with Control + Shift + Enter in_ [_Legacy Excel_](https://exceljet.net/glossary/legacy-excel)
_. In the latest version of Excel, the formula "just works"._

Generic formula
---------------

    =MAX(range1-range2)

Explanation 
------------

In the example shown, the goal is to calculate the maximum difference between the "High" values in column C and the "Low" values in column D. Because the difference between High and Low is not part of the data, the calculation must occur in the formula itself. This is a classic example of an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
.

### Excel Table

For convenience, all data is in an [Excel Table](https://exceljet.net/glossary/excel-table)
 named **data** in the range B5:D16. Excel Tables are a convenient way to work with data in Excel because they (1) automatically expand to include new data and (2) offer [structured references](https://exceljet.net/videos/introduction-to-structured-references)
, which let you refer to data by name instead of by address. If you are new to Excel Tables, [this article provides an overview](https://exceljet.net/articles/excel-tables)
. Also, see this short video:

> Video: [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)

### Array formula

This is a classic array formula problem. Subtracting the lows from the highs is an [array operation](https://exceljet.net/glossary/array-operation)
 that requires special handling in older versions of Excel. In Legacy Excel, you must enter the formula with control + shift + enter. When you enter the formula this way, you will see the formula enclosed in curly braces like this:

    {=MAX(data[High]-data[Low])}

_Note: This is an array formula and must be entered with control + shift + enter in_ [_Legacy Excel._](https://exceljet.net/glossary/legacy-excel)
 _If you open the workbook in an older version of Excel you will see that Excel automatically adds the curly braces. This is done to make sure the formula works properly. If you re-enter the formula without control + shift + enter, you will see an incorrect result. In the current version of Excel, you will not see the curly braces, and it is not necessary to enter the formula in a special way._

> Video: [What is an array formula?](https://exceljet.net/videos/what-is-an-array-formula)

### Maximum change

To calculate the maximum change, the formula in cell F5 is:

    =MAX(data[High]-data[Low])
    

After the table references are evaluated, we have the high and low values in array form:

    =MAX({79;77;76;69;72;76;79;83;85;79;82;83}-{68;69;64;55;59;60;64;69;62;60;73;76})

After subtraction, we have a single array inside the MAX function. The values in this array represent change:

    =MAX({11;8;12;14;13;16;15;14;23;19;9;7})

The MAX function returns 23, the maximum change between high and low in this set of data.

### Minimum change

To return the minimum change, replace the MAX function with the [MIN function](https://exceljet.net/functions/min-function)
:

    ​=MIN(data[High]-data[Low])

### Absolute change

In the table shown, the high values are always greater than the low values, which means the change itself will be a positive number. If you are comparing two columns of data where that is not true, the change will sometimes be negative. If you want to ignore the negative sign, you can add the [ABS function](https://exceljet.net/functions/abs-function)
 to the formula like this:

    =MAX(ABS(data[High]-data[Low]))

The ABS function returns the absolute value of a number, so it will convert any negative numbers to positive numbers. The MAX function will then return the maximum absolute value change.

### Date of max change

You may also want to know the date of the maximum change. In the worksheet shown, cell G5 contains an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
 to return the date associated with the max change:

    =INDEX(data[Date],MATCH(F5,data[High]-data[Low],0))

_Note: This is an array formula and must be entered with control + shift + enter in_ [_Legacy Excel._](https://exceljet.net/glossary/legacy-excel)

The gist of this formula is that we are using the maximum change value like a "key" to locate the date. Most of the work is done in the [MATCH function](https://exceljet.net/functions/match-function)
, which calculates the matching row number like this:

    =MATCH(F5,data[High]-data[Low],0)
    =MATCH(23,{11;8;12;14;13;16;15;14;23;19;9;7},0)
    =9

Note that we run the same change calculation explained above inside MATCH as the _lookup\_array_. Then we match the value in cell F5 against all changes in _lookup\_array_, which we know contains the max change. MATCH returns 9 to INDEX as _row\_num_, and INDEX returns June 9 as a final result.

    =INDEX(data[Date],9) // returns 9-Jun

_Note: if the change values contain duplicates, MATCH will match the first occurrence and INDEX will return the date of the first occurrence._

### XLOOKUP

If your version of Excel has XLOOKUP, you can write a more compact version of the date lookup like this:

    =XLOOKUP(F5,data[High]-data[Low],data[Date])

The logic is the same as with INDEX and MATCH: we look for the max change in F5 inside an array of calculated changes and return the corresponding date. In addition to offering a more streamlined formula, the XLOOKUP function gives you [controls to return the first or last match](https://exceljet.net/functions/xlookup-function)
.

### All in one formula

In the [dynamic array version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can use a formula that creates the entire table in one step:

    =LET(
    dates,data[Date],
    change,data[High]-data[Low],
    data,HSTACK(change,dates),
    result,TAKE(SORT(data,1,-1),1),
    VSTACK({"Max","Date"},result)
    )

The screen below shows what this formula looks like in the worksheet:

![All in one formula to show max change and date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/maximum_change_all_in_one_formula.png "All in one formula to show max change and date")

We use the [LET function](https://exceljet.net/functions/let-function)
 to assign values to four variables: _dates_, _change_, _data_, and _result_. The values for _dates_ come from the Date column directly:

    =LET(
    dates,data[Date],
    

The values for _change_ come from the change calculation explained above:

    ​=LET(
    dates,data[Date],
    change,data[High]-data[Low],

Next, we assemble the two columns we want in the final result using the [HSTACK function](https://exceljet.net/functions/hstack-function)
 to join _change_ to _dates_:

    =LET(
    dates,data[Date],
    change,data[High]-data[Low],
    data,HSTACK(change,dates),

This creates a two-column array with _change_ values in the first column and _date_ values in the second column. The result is assigned to _data_. Next, we assign a value to the _result_ using SORT and TAKE:

    =LET(
    dates,data[Date],
    change,data[High]-data[Low],
    data,HSTACK(change,dates),
    result,TAKE(SORT(data,1,-1),1),

Inside TAKE, we use the [SORT function](https://exceljet.net/functions/sort-function)
 to sort _data_ by the first column in descending order. Then we use the [TAKE function](https://exceljet.net/functions/take-function)
 to retrieve just the first row, which (because we sorted in descending order by change) contains the maximum change and date of maximum change. Last, we assemble our table with the [VSTACK function](https://exceljet.net/functions/vstack-function)
, which returns a final result:

    =LET(
    dates,data[Date],
    change,data[High]-data[Low],
    data,HSTACK(change,dates),
    result,TAKE(SORT(data,1,-1),1),
    VSTACK({"Max","Date"},result)
    )

The result is the entire table shown in the range F4:G5.

Notes:

1.  To return the nth largest values, change the 2nd argument in TAKE to n. For example, to return the top 3 changes, you can ask TAKE for 3 rows instead of 1 row.
2.  To return the _minimum_ change, change the 3rd argument in SORT to 1 to sort in _ascending_ order

Related formulas
----------------

[![Excel formula: Minimum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_if_multiple_criteria.png "Excel formula: Minimum if multiple criteria")](https://exceljet.net/formulas/minimum-if-multiple-criteria)

### [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)

In this example, the goal is to get the minimum value for a given group above a specific temperature. In other words, we want the min value after applying multiple criteria. The easiest way to solve this problem is with the MINIFS function. However, if you need more flexibility (for example, you...

[![Excel formula: Maximum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_if_multiple_criteria.png "Excel formula: Maximum if multiple criteria")](https://exceljet.net/formulas/maximum-if-multiple-criteria)

### [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)

In this example, the goal is to get the maximum value for a given group below a specific temperature. In other words, we want the max value after applying multiple criteria. The easiest way to solve this problem is with the MAXIFS function. However, if you need more flexibility (i.e., you need to...

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20maximum%20and%20minimum%20values-thumb.png)](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

### [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

In this video we'll look at how to calculate minimum and maximum values in Excel. Let's take a look. Here we have a list of properties, that includes an address, a price, and a variety of other information. Let's calculate the maximum and minimum values in this list. First, I'm going to create a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20is%20an%20array%20formula%3F-play.png)](https://exceljet.net/videos/what-is-an-array-formula)

### [What is an array formula?](https://exceljet.net/videos/what-is-an-array-formula)

In this video, we'll answer the question: What is an array formula? In the world of Excel formulas, the term "array formula" is probably responsible for more confusion than just about any other concept. This is because the definition of an array formula has become mixed up with the requirement to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20SORT%20function%20example-Play.png)](https://exceljet.net/videos/basic-sort-function-example)

### [Basic SORT function example](https://exceljet.net/videos/basic-sort-function-example)

In this video, we’ll look at a basic example of sorting with the SORT function . Sorting with formulas is one of those traditionally hard problems in Excel that new dynamic array formulas have made much easier. In this worksheet, we have a list of names, scores, and groups. Currently the data is...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)
    
*   [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    

### Videos

*   [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)
    
*   [What is an array formula?](https://exceljet.net/videos/what-is-an-array-formula)
    
*   [Basic SORT function example](https://exceljet.net/videos/basic-sort-function-example)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Excel Tables](https://exceljet.net/training/excel-tables)
    
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