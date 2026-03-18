# Lookup number plus or minus N - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lookup-number-plus-or-minus-n

---

[Skip to main content](https://exceljet.net/formulas/lookup-number-plus-or-minus-n#main-content)

[](https://exceljet.net/formulas/lookup-number-plus-or-minus-n#)

*   [Previous](https://exceljet.net/formulas/lookup-lowest-value)
    
*   [Next](https://exceljet.net/formulas/lookup-up-cost-for-product-or-service)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Lookup number plus or minus N
=============================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[ABS](https://exceljet.net/functions/abs-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Lookup number plus or minus N](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lookup%20number%20plus%20or%20minus%20n.png "Excel formula: Lookup number plus or minus N")

Summary
-------

To look up a number in a set of data that is plus or minus (±) **n**, where **n** is the allowed tolerance, you can use the XLOOKUP function, or INDEX and MATCH, as explained below. In the example shown, the formula in cell F8 is:

    =XLOOKUP(1,--(ABS(data[Amount]-G4)<=G5),data)
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D15.

Generic formula
---------------

    =XLOOKUP(1,--(ABS(range-number)<=n),range)

Explanation 
------------

In this example, the goal is to look up a number with a certain amount of allowed tolerance, defined as **n**. In other words, with a given lookup number we are trying to find a number in a set of data that is ± **n**. In the worksheet shown, the number to find is in cell G4 and the number used for **n** is in G5. All data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range B5:D15 named "data". This problem can be solved with the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 or with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 together with [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. Both options are explained below.

### XLOOKUP function

The XLOOKUP function is a modern replacement for the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
. A key benefit of XLOOKUP is that it can handle [array operations](https://exceljet.net/glossary/array-operation)
 as the _lookup\_array_ or _return\_array_. This means we can construct the _lookup\_array_ we need as part of the formula. We start off by providing _lookup\_value_ as 1:

    =XLOOKUP(1,
    

_Note: The lookup value of 1 has nothing to do with the value for **n**, which is also 1 in this case. It is simply a common convention when using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 in lookup formulas._ 

Next, we create the _lookup\_array_ with this expression:

    --(ABS(data[Amount]-G4)<=G5)
    

Inside the ABS function, we subtract the value in cell G4 (5000) from all values in **data\[Amount\]**. Since we have 11 values in the **Amount** column, we get 11 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {-3499.65;19350.86;-1;-3750.5;4099.75;6999.75;-700.15;1750.75;9999.9;-2899.15;5249.65}
    

Notice some values are negative. Next, the [ABS function](https://exceljet.net/functions/abs-function)
 returns the absolute value of these values:

    {3499.65;19350.86;1;3750.5;4099.75;6999.75;700.15;1750.75;9999.9;2899.15;5249.65}
    

Each value is then checked against the value for **n** in cell G5 (1). We are looking for values that are less than or equal to 1. You can see that the third number is in this range. The result is a new array that contains TRUE and FALSE values:

    {FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

In this array, a TRUE value indicates we have found a matching value that is within plus or minus n of our lookup value. Notice the third value is TRUE, while all others are FALSE. Next, because we are using 1 for _lookup\_value_, we use a [double-negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to convert the TRUE and FALSE values to 1s and 0s:

    {0;0;1;0;0;0;0;0;0;0;0}
    

Moving back to the XLOOKUP formula, we now have:

    =XLOOKUP(1,{0;0;1;0;0;0;0;0;0;0;0},data)
    

Now it's clear why we are using 1 for _lookup\_value_. XLOOKUP matches 1 and returns the third row of **data**.

### INDEX and MATCH option

This problem can also be solved with an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
 like this:

    =INDEX(data,MATCH(1,--(ABS(data[Amount]-G4)<=G5),0),0)
    

The [MATCH function](https://exceljet.net/functions/match-function)
 is configured just like XLOOKUP above:

    MATCH(1,--(ABS(data[Amount]-G4)<=G5),0)
    

The _lookup\_value_ is 1 and the _lookup\_array_ is created with the [ABS function](https://exceljet.net/functions/abs-function)
 as above. After _lookup\_array_ is evaluated, we have:

    MATCH(1,{0;0;1;0;0;0;0;0;0;0;0},0)
    

The [MATCH function](https://exceljet.net/functions/match-function)
 matches the third value (1), and returns 3 to the [INDEX function](https://exceljet.net/functions/index-function)
 as the _row\_num_:

    =INDEX(data,3,0)
    

Because _column\_num_ is set to zero, INDEX returns the entire third row from the data as a final result. In the current version of Excel, the result will spill into three cells, but in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, you will see only the first value. To display all values, you can either enter the formula as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
, or use three separate formulas to return values for each of the columns like this:

    =INDEX(data,MATCH(1,--(ABS(data[Amount]-G4)<=G5),0),1) // amount
    =INDEX(data,MATCH(1,--(ABS(data[Amount]-G4)<=G5),0),2) // date
    =INDEX(data,MATCH(1,--(ABS(data[Amount]-G4)<=G5),0),3) // client
    

Note the only difference in the formulas above is the column number.

Related formulas
----------------

[![Excel formula: Find closest match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_closest_match_0.png "Excel formula: Find closest match")](https://exceljet.net/formulas/find-closest-match)

### [Find closest match](https://exceljet.net/formulas/find-closest-match)

In this example, the goal is to find the closest match to a target value entered in cell E5. Although it may not look like it, this is essentially a look-up problem. The easiest way to solve this problem is with the XLOOKUP function . However in older versions of Excel without the XLOOKUP function...

[![Excel formula: Lookup value between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20value%20between%20two%20numbers.png "Excel formula: Lookup value between two numbers")](https://exceljet.net/formulas/lookup-value-between-two-numbers)

### [Lookup value between two numbers](https://exceljet.net/formulas/lookup-value-between-two-numbers)

The LOOKUP function does an approximate match lookup in one range, and returns the corresponding value in another. Although the table in this example includes both maximum and minimum values, we only need to use the minimum values. This is because when LOOKUP can't find a match, it will match the...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel ABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20abs%20function.png "Excel ABS function")](https://exceljet.net/functions/abs-function)

### [ABS Function](https://exceljet.net/functions/abs-function)

The Excel ABS function returns the absolute value of a number. ABS converts negative numbers to positive numbers, and positive numbers are unaffected.

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

*   [Find closest match](https://exceljet.net/formulas/find-closest-match)
    
*   [Lookup value between two numbers](https://exceljet.net/formulas/lookup-value-between-two-numbers)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [ABS Function](https://exceljet.net/functions/abs-function)
    
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