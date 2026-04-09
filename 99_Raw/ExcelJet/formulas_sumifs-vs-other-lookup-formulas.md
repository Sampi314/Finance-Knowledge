# SUMIFS vs other lookup formulas - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sumifs-vs-other-lookup-formulas

---

[Skip to main content](https://exceljet.net/formulas/sumifs-vs-other-lookup-formulas#main-content)

[](https://exceljet.net/formulas/sumifs-vs-other-lookup-formulas#)

*   [Previous](https://exceljet.net/formulas/sum-multiple-tables)
    
*   [Next](https://exceljet.net/formulas/sumifs-with-excel-table)
    

[Tables](https://exceljet.net/formulas#Tables)

SUMIFS vs other lookup formulas
===============================

by Dave Bruns · Updated 23 Oct 2023

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[LOOKUP](https://exceljet.net/functions/lookup-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/5719/download?token=IwYlvjuf)
 (11.79 KB)

![Excel formula: SUMIFS vs other lookup formulas](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sumifs%20vs%20lookup%20formula.png "Excel formula: SUMIFS vs other lookup formulas")

Summary
-------

In certain cases, you can use SUMIFS like a lookup formula to retrieve a numeric value. In the example shown, the formula in G6 is:

    =SUMIFS(sales,region,G4,quarter,G5)
    

where **region** (B5:B20), **quarter** (C5:C20), and **sales** (D5:D20) are [named ranges](https://exceljet.net/glossary/named-range)
.

The result is Q3 sales for the Central region, 127,250.

Explanation 
------------

If you are new to the SUMIFS function, you can find a [basic overview with many examples here](https://exceljet.net/functions/sumifs-function)
.

The SUMIFS function is designed to sum numeric values based on one or more criteria. In specific cases however, you may be able to use SUMIFS to "look up" a numeric value that meets required criteria. The main reasons to do this are simplicity and speed.

In the example shown, we have quarterly sales data for four regions. We start off by giving SUMIFS a sum range, and the first condition, which tests region for the value in G4, "Central":

    =SUMIFS(sales,region,G4 // sum range, region is "Central"
    

*   Sum range is **sales** (D5:D20)
*   Criteria range 1 is **region** (B5:B20)
*   Criteria 1 is G4 ("Central")

We then add the second range/criteria pair, which checks quarter:

    =SUMIFS(sales,region,G4,quarter,G5) // and quarter is "Q3"
    

*   Criteria range 2 is **quarter** (C5:C20)
*   Criteria 2 is G5 ("Q3")

With these criteria, SUMIFS returns 127,250, the Central Q3 sales number.

The behavior of SUMIFS is to sum _all matching values_. However, because there is just _one matching value_, the result is the same as the value itself.

Below, we look at several lookup formula options.

Lookup formula options
----------------------

This section briefly reviews other formula options that yield the same result. With the exception of SUMPRODUCT (at the bottom), these are more traditional lookup formulas that locate the position of the target value, and return the value at that location.

### With VLOOKUP

Unfortunately, VLOOKUP is not a good solution to this problem. With a helper column, it is possible to build a VLOOKUP formula to match with multiple criteria ([example here](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
), but it's an awkward process that requires you to tinker with the source data.

### With INDEX and MATCH

[INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 is a very flexible lookup combination that can be used for all kinds of lookup problems, and this example is no exception. With INDEX and MATCH, we can lookup sales by region and quarter with an array formula like this:

    {=INDEX(sales,MATCH(1,(region=G4)*(quarter=G5),0))}
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
, and must be entered with control + shift + enter._

The trick with this approach is to use [boolean logic](https://exceljet.net/glossary/boolean-logic)
 with array operations inside the MATCH function to build an array of 1s and 0s as the lookup array. Then we can ask the [MATCH function](https://exceljet.net/functions/match-function)
 find the number 1. Once the lookup array is created, the formula resolves to:

    =INDEX(sales,MATCH(1,{0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0},0))
    

With only 1 remaining in the lookup array, MATCH returns a position of 11 to the [INDEX function](https://exceljet.net/functions/index-function)
, and INDEX returns the sales number at that position, 127,250.

For more details, see : [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

### With XLOOKUP

[XLOOKUP](https://exceljet.net/functions/xlookup-function)
 is a flexible new function in Excel that can handle arrays natively. With XLOOKUP, we can use exactly the same approach as with INDEX and MATCH, using boolean logic and array operations to create a lookup array:

    =XLOOKUP(1,(region=G4)*(quarter=G5),sales)
    

Once the array operations have run, the formula resolves to:

    =XLOOKUP(1,{0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0},sales)
    

And XLOOKUP returns the same result as above, 127,250.

More: [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

### With LOOKUP

The [LOOKUP function](https://exceljet.net/functions/lookup-function)
 is an older function in Excel that many people don't even know about. One of LOOKUP's key strengths is that it can handle arrays natively. However, LOOKUP has a few distinct weaknesses:

*   Can't be locked in "exact match mode"
*   Always assumes lookup data is sorted, A-Z
*   Always returns an approximate match (if exact match can't be found)

Nonetheless, LOOKUP can be used to solve this problem nicely like this:

    =LOOKUP(2,1/((region=G4)*(quarter=G5)),sales)
    

which simplifies to:

    =LOOKUP(2,{#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;1;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!},sales)
    

If you look closely, you can see a single number 1 in a sea of #DIV/0! errors. This represents the value we want to retrieve.

We use a lookup value of 2 because we can't guarantee the array is sorted. So, we force all non-matching rows to errors, and ask LOOKUP to find a 2. LOOKUP ignores the errors and dutifully scans the entire array looking for 2. When the number 2 can't be found, LOOKUP "backs up" and matches the last non-error value, which is the 1 in the 11th position. The result is the same as above, 127,250.

[More detailed explanation here](https://exceljet.net/formulas/lookup-latest-price)
.

### With SUMPRODUCT

As usual, you can also use the Swiss Army Knife [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to solve this problem as well. The trick is to use boolean logic and array operations to "zero out" all but the one value we want:

    =SUMPRODUCT(sales*((region=G4)*(quarter=G5)))
    

After the array math inside SUMPRODUCT is complete, the formula simplifies to:

    =SUMPRODUCT({0;0;0;0;0;0;0;0;0;0;127250;0;0;0;0;0})
    

This is technically not really a lookup formula, but it behaves like one. With just a single array to process, the SUMPRODUCT function returns the sum of the array, 12,7250.

See [this example](https://exceljet.net/formulas/sumproduct-with-if)
 for a more complete explanation.

In spirit, the SUMPRODUCT option is closest to the SUMIFS formula since we are _summing_ values based on multiple criteria. As before, it works fine as long as there is only one matching result.

### Summary

SUMIF can indeed be used like a lookup formula, and configuration may be simpler than a more conventional lookup formula. In addition, if you are working with a large data set, SUMIFS will be a very fast option. However, you must keep in mind two key requirements:

1.  The result must be numeric data
2.  Criteria must match only one result

If the situation doesn't meet both requirements, SUMIFS is not a good choice.

Related formulas
----------------

[![Excel formula: SUMIFS with Excel Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS%20with%20Excel%20Table.png "Excel formula: SUMIFS with Excel Table")](https://exceljet.net/formulas/sumifs-with-excel-table)

### [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)

This formula uses structured references to feed table ranges into the SUMIFS function. The sum range is provided as Table1\[Total\] , the criteria range is provided as Table1\[Item\] , and criteria comes from values in column I. The formula in I5 is: =SUMIFS(Table1\[Total\],Table1\[Item\],H5) which...

[![Excel formula: Two-way summary with SUMIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20summary%20with%20sumifs.png "Excel formula: Two-way summary with SUMIFS")](https://exceljet.net/formulas/two-way-summary-with-sumifs)

### [Two-way summary with SUMIFS](https://exceljet.net/formulas/two-way-summary-with-sumifs)

The SUMIFS function is designed to sum numeric values using multiple criteria. In the example shown, the data in the range B5:E15 shows a sales pipeline where each row is an opportunity owned by a salesperson, at a specific stage. The formula in H5 is: =SUMIFS(value,name,$G5,stage,H$4) The first...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20SUMIFS%20with%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)

### [How to use SUMIFS with an Excel Table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)

In this video, we'll look at how to use the SUMIFS function with an Excel Table. On this worksheet, I have two identical sets of order data. I'm going to walk through the process of constructing a summary of sales by item for both sets of data. With the data on the left, I'll use standard formulas...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)
    
*   [Two-way summary with SUMIFS](https://exceljet.net/formulas/two-way-summary-with-sumifs)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [How to use SUMIFS with an Excel Table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)
    

### Links

*   [SUMIFS vs VLOOKUP (excel-university.com)](https://www.excel-university.com/tag/battle/)
    

### Training

*   [Excel Tables](https://exceljet.net/training/excel-tables)
    

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