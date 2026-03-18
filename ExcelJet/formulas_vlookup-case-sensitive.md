# VLOOKUP case-sensitive  - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-case-sensitive

---

[Skip to main content](https://exceljet.net/formulas/vlookup-case-sensitive#main-content)

[](https://exceljet.net/formulas/vlookup-case-sensitive#)

*   [Previous](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)
    
*   [Next](https://exceljet.net/formulas/vlookup-faster-vlookup)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP case-sensitive
======================

by Dave Bruns · Updated 28 Mar 2023

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[EXACT](https://exceljet.net/functions/exact-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7083/download?token=2A138bDM)
 (15.84 KB)

![Excel formula: VLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP%20case%20sensitive.png "Excel formula: VLOOKUP case-sensitive ")

Summary
-------

To create a case-sensitive lookup with the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
, you can use the [EXACT function](https://exceljet.net/functions/exact-function)
. In the example shown, the formula in G5 is:

    =VLOOKUP(TRUE,CHOOSE({1,2},EXACT(data[Color],F5),data[Qty]),2,0)
    

where "data" is an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range B5:D16. In this configuration, VLOOKUP matches the text "RED" in row 5 of the table and returns 10 from the Qty column in the same row. This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
 or Excel 2021.

_Note: With [XLOOKUP](https://exceljet.net/functions/xlookup-function)
, or [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, the approach is the same but the formulas are more straightforward: [XLOOKUP example](https://exceljet.net/formulas/xlookup-case-sensitive)
, [INDEX and MATCH example](https://exceljet.net/formulas/index-and-match-case-sensitive)
._

Generic formula
---------------

    =VLOOKUP(TRUE,CHOOSE({1,2},EXACT(range1,A1),range2),2,0)

Explanation 
------------

In this example, the goal is to perform a case-sensitive lookup on Color with VLOOKUP. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". This presents several challenges. First, Excel is _not_ case-sensitive by default, and there is no built-in setting to make VLOOKUP case-sensitive. For example, if we try a standard VLOOKUP formula in exact match mode, we get the wrong result:

    =VLOOKUP("RED",data,3,0) // returns 17
    

VLOOKUP matches "Red" in row 3, and returns 17. The correct result is 10.

The second challenge is the table itself. Unlike XLOOKUP or INDEX and MATCH, VLOOKUP _requires_ the entire table to be provided in the _table\_array_ argument. Normally, this is not a problem. However, to enable a case-sensitive VLOOKUP, we can't use the existing table as-is, and this means we need to take special steps to _assemble_ a table that will work for this problem.

The overall process looks like this:

1.  Use the EXACT function to check the Color column for the lookup value.
2.  Join the results from EXACT to the Qty column with the CHOOSE function.
3.  Provide the resulting array to VLOOKUP as the _table\_array_ argument.
4.  Configure VLOOKUP to look for TRUE in the new table.

The result is a case-sensitive lookup with VLOOKUP. Read on for a complete explanation.

### Background reading

This article assumes you are familiar with the VLOOKUP function and Excel Tables. If not, see:

*   [Excel Tables](https://exceljet.net/articles/excel-tables)
     - introduction and overview
*   [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
     - overview with examples
*   [EXACT function](https://exceljet.net/functions/exact-function)
     - overview

### EXACT function

The [EXACT function](https://exceljet.net/functions/exact-function)
 is designed to perform a case-sensitive comparison of two text values. If the two values match exactly, EXACT returns TRUE. If not, EXACT returns FALSE. The twist in this case is that we need to check every value in the Color column against the value in F5. Fortunately, the EXACT function will do this.

Working from the inside out, we set up the EXACT function like this:

    =EXACT(data[Color],F5)
    

Since there are 12 values in the Color column, the EXACT function will return a vertical [array](https://exceljet.net/glossary/array)
 with 12 TRUE and FALSE results like this:

    {FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

Notice the position of TRUE (5) corresponds to row 5 in the table, where Color is "RED". EXACT returns FALSE for every other value, including "Red" in row 3. This gives us an array we can use in the next step.

### CHOOSE function

We now have an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values that will function as a key to which row(s) in the table match "RED". The problem is that the array is not actually part of the table, and VLOOKUP needs an entire table as the _table\_array_ argument. In addition, the first column in the table must contain lookup values. What we need is a _new_ table, that combines the result from EXACT with the values in the Qty column.

Enter the [CHOOSE function](https://exceljet.net/functions/choose-function)
. Normally, the CHOOSE function is used to select a value by numeric position. For example, to get the second value from a list of three values, you could use CHOOSE like this:

    =CHOOSE(2,value1,value2,value3) // returns value2
    

CHOOSE is flexible when it comes to values, which can be any mix of constants, cell references, arrays, or ranges. In this case, we give CHOOSE the array created by the EXACT function as _value1_ and the Qty column in the table as _value2_. Then, for _index\_num_, we provide the [array constant](https://exceljet.net/glossary/array-constant)
 {1,2} like this:

    =CHOOSE({1,2},EXACT(data[Color],F5),data[Qty]) 
    

The array constant is the tricky part. By using the array {1,2} we are requesting _value1_ and _value2_ at the same time. As a result, the array from EXACT and data\[Qty\] are "glued" together and returned as a single array. This array only exists in memory, but it looks like this:

![The array created by the CHOOSE function](https://exceljet.net/sites/default/files/images/formulas/inline/array%20created%20by%20the%20CHOOSE%20function.png "The array created by the CHOOSE function")

As you can see, the array has 2-columns. We now have a table we can use in VLOOKUP.

_Note: whenever you see =CHOOSE({1,2} you should think "2 things are being joined together"._

### VLOOKUP function

Next, we need to connect the code above to the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
. We know the first column in the array we created contains TRUE or FALSE values, so we start with a lookup value of TRUE:

    =VLOOKUP(TRUE,
    

This may seem strange, but remember that the original color values are gone (replaced by TRUE and FALSE) and so we need to look for TRUE and not "RED". Next, for the _table\_array_ argument, we add the code that creates our custom table:

    =VLOOKUP(TRUE,CHOOSE({1,2},EXACT(data[Color],F5),data[Qty])
    

The array created by CHOOSE is returned directly to the VLOOKUP function as the _table\_array_ argument. Because the values we want to retrieve are in the second column, we set _col\_index\_num_ to 2. Then we set the _range\_lookup_ argument to zero or FALSE, to enable an exact match. The final formula in G5 is:

    =VLOOKUP(TRUE,CHOOSE({1,2},EXACT(data[Color],F5),data[Qty]),2,0)
    

VLOOKUP matches the text "RED" in row 5 of the table and returns 10 as a final result.

_Note: This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
 or Excel 2021._

Related formulas
----------------

[![Excel formula: INDEX and MATCH case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case-sensitive%20INDEX%20and%20MATCH.png "Excel formula: INDEX and MATCH case-sensitive ")](https://exceljet.net/formulas/index-and-match-case-sensitive)

### [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the first name in column B, based on a lookup value in cell F6. By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP , XLOOKUP , and INDEX and MATCH . These formulas will simply return...

[![Excel formula: XLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20case%20sensitive.png "Excel formula: XLOOKUP case-sensitive ")](https://exceljet.net/formulas/xlookup-case-sensitive)

### [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the color in the "Color" column. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP...

[![Excel formula: Case sensitive lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case%20sensitive%20lookup.png "Excel formula: Case sensitive lookup")](https://exceljet.net/formulas/case-sensitive-lookup)

### [Case sensitive lookup](https://exceljet.net/formulas/case-sensitive-lookup)

In this example, the goal is to perform a case-sensitive lookup on the name in column B, based on a lookup value entered in cell E5. By default, Excel is not case-sensitive. This means that standard lookup functions like VLOOKUP , XLOOKUP , and INDEX and MATCH are also not case-sensitive. These...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)
    
*   [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)
    
*   [Case sensitive lookup](https://exceljet.net/formulas/case-sensitive-lookup)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    

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