# VLOOKUP with variable table array - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-with-variable-table-array

---

[Skip to main content](https://exceljet.net/formulas/vlookup-with-variable-table-array#main-content)

[](https://exceljet.net/formulas/vlookup-with-variable-table-array#)

*   [Previous](https://exceljet.net/formulas/vlookup-with-two-client-rates)
    
*   [Next](https://exceljet.net/formulas/vlookup-without-na-error)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP with variable table array
=================================

by Dave Bruns · Updated 12 Jun 2021

Related functions 
------------------

[INDIRECT](https://exceljet.net/functions/indirect-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[IF](https://exceljet.net/functions/if-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6686/download?token=vdDm3Zlj)
 (14.21 KB)

![Excel formula: VLOOKUP with variable table array](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP%20with%20variable%20table%20array.png "Excel formula: VLOOKUP with variable table array")

Summary
-------

To look up a value based on a variable table, you can use the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 together with the [INDIRECT function](https://exceljet.net/functions/indirect-function)
. In the example shown, the formula in G5, copied down, is:

    =VLOOKUP(E5,INDIRECT("vendor_"&F5),2,0)
    

where **vendor\_a** (B5:C8) and **vendor\_b** (B11:C14) are [named ranges](https://exceljet.net/glossary/named-range)
 or [Excel Tables](https://exceljet.net/glossary/excel-table)
. As the formula is copied down, it returns a cost for each color using the vendor in column F to dynamically assign the correct table.

Generic formula
---------------

    =VLOOKUP(A1,INDIRECT("text"),column)

Explanation 
------------

In this example, the goal is to set up VLOOKUP to retrieve costs based on a variable vendor name. In other words, we want a formula that allows us to switch tables dynamically based on a user-supplied value. There are two cost tables in the worksheet, one for Vendor A and one for Vendor B. Both tables are defined as the [named ranges](https://exceljet.net/glossary/named-range)
 **vendor\_a** (B5:C8) and **vendor\_b** (B11:C14).

At the core, this is a basic lookup problem, and we could use the VLOOKUP function to get the cost for a color like this:

    =VLOOKUP(E5,"vendor_a",2,0) // vendor a cost for red
    =VLOOKUP(E5,"vendor_b",2,0) // vendor b cost for red
    

These formulas work fine, but the table name provided to VLOOKUP is hard-coded, _not_ variable.

In thinking about how to make the table variable, notice the table names are identical except for the last letter ("a" or "b"). This means we can assemble the correct table for each vendor with [concatenation](https://exceljet.net/glossary/concatenation)
 like this:

    ="vendor_"&"a" // returns "vendor_a"
    ="vendor_"&"b" // returns "vendor_b"
    

And, since "a" and "b" are _already_ in column F, we can pick up that value directly:

    ="vendor_"&F5 // "vendor_a"
    

The above expression will correctly create the vendor name we need to perform a lookup. However, the formula below will fail with a #VALUE! error:

    =VLOOKUP(E5,"vendor_"&F5,2,0) // returns #VALUE!
    

Why is that? The formula above fails because Excel interprets the table as a [text value](https://exceljet.net/glossary/text-value)
, not a [range](https://exceljet.net/glossary/range)
. What we need is a way to tell Excel to interpret the text value like a cell reference. This is a job for the [INDIRECT function](https://exceljet.net/functions/indirect-function)
 which is designed to evaluate a text value as a reference. Once we wrap the original expression in INDIRECT, we'll get a proper reference:

    =INDIRECT("vendor_"&F5)
    =INDIRECT("vendor_a)
    =B5:C8
    

Carrying these changes into the final formula, we have:

    =VLOOKUP(E5,INDIRECT("vendor_"&F5),2,0) // returns 9.95
    

Now VLOOKUP will correctly look up the cost for Vendor A or B, depending on the letter entered in column F. In the worksheet as shown, the formula returns $9.95, since the cost for Red from Vendor A is $9.95 . If the vendor is changed to "b", VLOOKUP will dynamically switch tables and return $12.50.

### With the IF function

The example above is a nice illustration of the power of setting up a worksheet with consistently named tables, but this isn't strictly necessary to perform a lookup with a variable table name. For example, we could just use the [IF function](https://exceljet.net/functions/if-function)
 to swap tables like this:

    =VLOOKUP(E5,IF(F5="a",vendor_a,vendor_b),2,0)
    

Or, without named ranges:

    =VLOOKUP(E5,IF(F5="a",$B$5:$C$8,$B$11:$C$14),2,0)
    

Here, the IF function simply checks the value in column F and returns one range if the letter is "a", and another if not. This approach won't scale as well (the formula will become progressively more complex as we add more vendor tables) but it works fine. It also nicely demonstrates how one function can be [nested](https://exceljet.net/glossary/nesting)
 inside another to deliver a range instead of a single value.

Related formulas
----------------

[![Excel formula: INDEX with variable array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20with%20variable%20array.png "Excel formula: INDEX with variable array")](https://exceljet.net/formulas/index-with-variable-array)

### [INDEX with variable array](https://exceljet.net/formulas/index-with-variable-array)

At the core, this is a normal INDEX and MATCH function : =INDEX(array,MATCH(value,range,0)) Where the MATCH function is used to find the correct row to return from array, and the INDEX function returns the value at that array. However, in this case we want to make the array variable, so that the...

[![Excel formula: Dynamic reference to table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20reference%20table%20name.png "Excel formula: Dynamic reference to table")](https://exceljet.net/formulas/dynamic-reference-to-table)

### [Dynamic reference to table](https://exceljet.net/formulas/dynamic-reference-to-table)

In this example, the goal is to create a dynamic reference to an Excel Table in a formula. In other words, create a formula that can refer to an Excel table by name as a variable. The easiest way to do this in Excel is to assemble the reference as a text value using concatenation , then use the...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

[![Excel formula: Lookup with variable sheet name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup_with_variable_sheet_name.png "Excel formula: Lookup with variable sheet name")](https://exceljet.net/formulas/lookup-with-variable-sheet-name)

### [Lookup with variable sheet name](https://exceljet.net/formulas/lookup-with-variable-sheet-name)

In this example, the goal is to create a lookup formula with a variable sheet name. In other words, a formula that uses a sheet name typed into a cell to construct a reference to a range on that sheet. If the sheet name is changed, the reference should update automatically. The key to the solution...

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

Related functions
-----------------

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [INDEX with variable array](https://exceljet.net/formulas/index-with-variable-array)
    
*   [Dynamic reference to table](https://exceljet.net/formulas/dynamic-reference-to-table)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    
*   [Lookup with variable sheet name](https://exceljet.net/formulas/lookup-with-variable-sheet-name)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    

### Functions

*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    

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