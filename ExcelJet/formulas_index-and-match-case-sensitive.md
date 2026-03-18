# INDEX and MATCH case-sensitive  - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/index-and-match-case-sensitive

---

[Skip to main content](https://exceljet.net/formulas/index-and-match-case-sensitive#main-content)

[](https://exceljet.net/formulas/index-and-match-case-sensitive#)

*   [Previous](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/index-and-match-descending-order)
    

[Lookup](https://exceljet.net/formulas#Lookup)

INDEX and MATCH case-sensitive
==============================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[EXACT](https://exceljet.net/functions/exact-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7041/download?token=n1Tp-QIL)
 (19.13 KB)

![Excel formula: INDEX and MATCH case-sensitive ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/case-sensitive%20INDEX%20and%20MATCH.png "Excel formula: INDEX and MATCH case-sensitive ")

Summary
-------

To perform a case-sensitive lookup with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, you can use the [EXACT function](https://exceljet.net/functions/exact-function)
. In the example shown, the formula in cell G6 is:

    =INDEX(data,MATCH(TRUE,EXACT(F6,data[First]),0),3)
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:B104. The result is a case-sensitive match for "JANET", which appears as the second "Janet" in the list of names. The final result returned by INDEX is "Fulfillment". Cell G5 contains a standard formula that is not case-sensitive.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter in Excel 2019 and earlier._

Generic formula
---------------

    =INDEX(data,MATCH(TRUE,EXACT(value,range),0),col_num)

Explanation 
------------

In this example, the goal is to perform a case-sensitive lookup on the first name in column B, based on a lookup value in cell F6. By default, Excel is _not_ case-sensitive and this applies to standard lookup formulas like [VLOOKUP](https://exceljet.net/functions/vlookup-function)
, [XLOOKUP](https://exceljet.net/functions/xlookup-function)
, and [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
. These formulas will simply return the _first_ match, ignoring case. For example, the formula in cell G5 is a standard INDEX and MATCH formula that is _not_ case-sensitive:

    =INDEX(data,MATCH(F5,data[First],0),3) // returns "Sales"
    

Since MATCH is not case sensitive, it returns the first match for "Janet" in row 2 of the table, even though the lookup value is "JANET" in uppercase.

We need a way to get Excel to compare case. The [EXACT function](https://exceljet.net/functions/exact-function)
 is perfect for this task, but the way we use it is a little unusual. Instead of comparing one [text value](https://exceljet.net/glossary/text-value)
 to another, we compare one text value to _many_ values. In a nutshell, we use the EXACT function to generate an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values, then use the MATCH function to locate the first TRUE.

### Background reading

This article assumes you are familiar with Excel Tables and INDEX and MATCH. If not, see:

*   [Excel Tables](https://exceljet.net/articles/excel-tables)
     - introduction and overview
*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
     - overview with simple examples

### EXACT function

Working from the inside out, we first use the EXACT function to compare the lookup value in F6 with every value in the "First" column in the table:

    EXACT(F6,data[First])
    

Because we give EXACT an [array](https://exceljet.net/glossary/array)
 of values as a second argument, we will _get back_ an array of TRUE and FALSE results. The first 10 results in this array look like this:

    {FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;...
    

_Note: the actual array will contain 100 values since there are 100 rows in the table._

This array is created by checking the value in F6 against every cell in the "First" column of the table. A TRUE value indicates an exact, case-sensitive match. A FALSE value means no exact match. Based on the results above, we have an exact match at row 6 of the table.

### MATCH function

Now we need to get the position (row number) of the TRUE value in this array. With INDEX and MATCH formulas, this is done with the [MATCH function](https://exceljet.net/functions/match-function)
. The twist in this case is that we set up MATCH to look for TRUE instead of the original lookup value in F6:

    MATCH(TRUE,EXACT(F6,data[First]),0) // returns 6
    

Inside the MATCH function, _lookup\_value_ is TRUE, _lookup\_array_ comes from EXACT, and the _match\_type_ [argument](https://exceljet.net/glossary/function-argument)
 is set to 0 for exact match. It may seem strange to ask MATCH to look for TRUE, but remember that the EXACT function is creating an array of TRUE and FALSE values. When EXACT delivers this array to MATCH, the original data is no longer available. The MATCH function returns 6.

_Note: MATCH will always return the first match if there are duplicate lookup values._

### INDEX and MATCH

Now that we have a row number, we just need to use the [INDEX function](https://exceljet.net/functions/index-function)
 to retrieve the value at the right row and column intersection. The MATCH function returns the number 6 for _row\_num_, as explained above. The _column\_num_ argument is hardcoded as 3, since _array_ is given as **data**, which includes all three columns. The final formula is:

    =INDEX(data,MATCH(TRUE,EXACT(F6,data[First]),0),3)
    

With a row number of 6 and a column number of 3, INDEX returns a final result of "Fulfillment".

### With XLOOKUP

With the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
, we can build a more compact formula with the same result:

    =XLOOKUP(TRUE,EXACT(F6,data[First]),data[Department])
    

This formula works exactly the same as the INDEX and MATCH option explained above. The EXACT function is used to compare all values in the "First" column of the table with the value in cell F6. The result is returned directly to XLOOKUP as the _lookup\_array_. The _lookup\_value_ is set to TRUE, and _return\_array_ is the "Department" column. For a more detailed explanation of XLOOKUP, [see this example](https://exceljet.net/formulas/xlookup-case-sensitive)
.

Related formulas
----------------

[![Excel formula: XLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20case%20sensitive.png "Excel formula: XLOOKUP case-sensitive ")](https://exceljet.net/formulas/xlookup-case-sensitive)

### [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the color in the "Color" column. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP...

[![Excel formula: VLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20case%20sensitive.png "Excel formula: VLOOKUP case-sensitive ")](https://exceljet.net/formulas/vlookup-case-sensitive)

### [VLOOKUP case-sensitive](https://exceljet.net/formulas/vlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on Color with VLOOKUP. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". This presents several challenges. First, Excel is not case-sensitive by default, and there is no built-in...

[![Excel formula: FILTER case-sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20case%20sensitive.png "Excel formula: FILTER case-sensitive")](https://exceljet.net/formulas/filter-case-sensitive)

### [FILTER case-sensitive](https://exceljet.net/formulas/filter-case-sensitive)

This formula relies on the FILTER function to retrieve data based on a logical test . The array argument is provided as B5:D15, which contains all of the data without headers. The include argument is an expression based on the EXACT function: EXACT(B5:B15,"RED") The EXACT function compares two text...

[![Excel formula: SUMPRODUCT case-sensitive lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT_case_sensitive_lookup.png "Excel formula: SUMPRODUCT case-sensitive lookup")](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)

### [SUMPRODUCT case-sensitive lookup](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)

The SUMPRODUCT function multiplies arrays together and returns the sum of products. If only one array is supplied, SUMPRODUCT will simply sum the items in the array. For example, if we give SUMPRODUCT one array in the form of the data\[Qty\] column: =SUMPRODUCT(data\[Qty\]) // returns 54 SUMPRODUCT...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)
    
*   [VLOOKUP case-sensitive](https://exceljet.net/formulas/vlookup-case-sensitive)
    
*   [FILTER case-sensitive](https://exceljet.net/formulas/filter-case-sensitive)
    
*   [SUMPRODUCT case-sensitive lookup](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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