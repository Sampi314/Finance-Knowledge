# Excel HLOOKUP function | Exceljet

**Source:** https://exceljet.net/functions/hlookup-function

---

[Skip to main content](https://exceljet.net/functions/hlookup-function#main-content)

[](https://exceljet.net/functions/hlookup-function#)

*   [Previous](https://exceljet.net/functions/getpivotdata-function)
    
*   [Next](https://exceljet.net/functions/hyperlink-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

HLOOKUP Function
================

by Dave Bruns · Updated 24 Jul 2021

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[LOOKUP](https://exceljet.net/functions/lookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

[FILTER](https://exceljet.net/functions/filter-function)

![Excel HLOOKUP function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20hlookup%20function.png "Excel HLOOKUP function")

Summary
-------

The Excel HLOOKUP function finds and retrieve a value from data in a horizontal table. The "H" in HLOOKUP stands for "horizontal", and lookup values must appear in the first row of the table, moving horizontally to the right. HLOOKUP supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for finding partial matches.

Purpose 
--------

Look up a value in a table arranged horizontally

Return value 
-------------

The matched value from a table.

Syntax
------

    =HLOOKUP(lookup_value,table_array,row_index,[range_lookup])

*   _lookup\_value_ - The value to look up.
*   _table\_array_ - The table from which to retrieve data.
*   _row\_index_ - The row number from which to retrieve data.
*   _range\_lookup_ - \[optional\] A Boolean to indicate exact match or approximate match. Default = TRUE = approximate match.

Using the HLOOKUP function 
---------------------------

The HLOOKUP function can locate and retrieve a value from data in a _horizontal table_. Like the "V" in [VLOOKUP](https://exceljet.net/functions/vlookup-function)
 which stands for "vertical", the "H" in HLOOKUP stands for "horizontal". The lookup values must appear in the _first_ row of the table, moving horizontally to the right. HLOOKUP supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for finding partial matches.

HLOOKUP searches for a value in the _first row_ of a table. When it finds a match, it retrieves a value at that column from the row given. Use HLOOKUP when lookup values are located in the first row of a table. Use VLOOKUP when lookup values are located in the first column of a table.

HLOOKUP takes four [arguments](https://exceljet.net/glossary/function-argument)
. The first argument, called _lookup\_value_, is the value to look up. The second argument, _table\_array_, is a range that contains the lookup table. The third argument, _row\_index\_num_ is the row number in the table from which to retrieve a value. In the example shown, HLOOKUP is used to look up values from row 2 (Level) and row 3 (Bonus) in the table. The fourth and final argument, _range\_lookup_, controls matching. Use TRUE or 1 for an approximate match and FALSE or 0 for an exact match.

### Example #1 - approximate match

In the example shown, the goal is to look up the correct Level and Bonus for the sales amounts in C5:C13. The lookup table is in H4:J6, which is the [named range](https://exceljet.net/glossary/named-range)
 "table". Note this is an approximate match scenario. For each amount in C5:C13, the goal is to find the _best_ match, not an _exact_ match.  To lookup Level, the formula in cell D5, copied down, is:

    =HLOOKUP(C5,table,2,1) // get level
    

 To get Bonus, the formula in E5, copied down, is:

    =HLOOKUP(C5,table,3,1) // get bonus
    

Notice the only difference between the two formulas is the row index number: Level comes from row 2 in the lookup table, while Bonus comes from row 3. The match mode has been set explicitly to approximate match by providing the last argument, _range\_lookup_, as 1.

### Example #2 - exact match

In the screen below, the goal is to look up the correct level for a numeric rating 1-4. In cell D5, the HLOOKUP formula, copied down, is:

    =HLOOKUP(C5,table,2,FALSE) // exact match
    

![HLOOKUP exact match example](https://exceljet.net/sites/default/files/images/functions/inline/hlookup%20example%20exact%20match.png)

where table is the [named range](https://exceljet.net/glossary/named-range)
 G4:J5. Notice the last argument, _range\_lookup_ is set to FALSE to require an exact match.

### Notes

*   _Range\_lookup_ controls whether the lookup value needs to match exactly or not. The default is TRUE = allow non-exact match.
*   Set _range\_lookup_ to FALSE to require an exact match.
*   If _range\_lookup_ is omitted or TRUE, and no exact match is found, HLOOKUP will match the nearest value in the table that is _still less than the lookup value_. However, HLOOKUP will still match an exact value if one exists.
*   If _range\_lookup_ is TRUE , lookup values in the first row of the table must be sorted in ascending order. Otherwise, HLOOKUP may return an incorrect or unexpected value.
*   If _range\_lookup_ is FALSE (exact match), values in the first row of the lookup table do not need to be sorted.

HLOOKUP function examples
-------------------------

[![Excel formula: XLOOKUP horizontal lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20horizontal%20lookup.png "Excel formula: XLOOKUP horizontal lookup")](https://exceljet.net/formulas/xlookup-horizontal-lookup)

### [XLOOKUP horizontal lookup](https://exceljet.net/formulas/xlookup-horizontal-lookup)

In this example, the goal is to perform a horizontal lookup to determine the correct quantity-based discount. The range G6:L7 contains quantity-based discounts. Column B contains random quantities used when testing the formula. This problem can be easily solved with the XLOOKUP function or the...

[![Excel formula: Get first text value in a row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_text_value_in_a_row.png "Excel formula: Get first text value in a row")](https://exceljet.net/formulas/get-first-text-value-in-a-row)

### [Get first text value in a row](https://exceljet.net/formulas/get-first-text-value-in-a-row)

The goal is to return the first text value in each row, ignoring both blank cells and cells that contain numbers. This problem can be solved using the HLOOKUP function. In newer versions of Excel, you can use the XLOOKUP function, which is a more modern lookup function that can look up values in...

HLOOKUP function videos
-----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20HLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-hlookup)

### [How to use HLOOKUP](https://exceljet.net/videos/how-to-use-hlookup)

In this video, we'll look at how to use the HLOOKUP function. HLOOKUP works just like VLOOKUP , but instead of getting the value of an item from a certain column in a table, HLOOKUP gets a value from a certain row in a table. Let's take a look. Here's the VLOOKUP commission example we've looked at...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

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

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get first text value in a row](https://exceljet.net/formulas/get-first-text-value-in-a-row)
    
*   [XLOOKUP horizontal lookup](https://exceljet.net/formulas/xlookup-horizontal-lookup)
    

### Videos

*   [How to use HLOOKUP](https://exceljet.net/videos/how-to-use-hlookup)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Links

*   [Microsoft HLOOKUP function documentation](https://support.office.com/en-us/article/hlookup-function-a3034eec-b719-4ba3-bb65-e1ad662ed95f)
    

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