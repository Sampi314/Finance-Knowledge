# Get location of value in 2D array - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-location-of-value-in-2d-array

---

[Skip to main content](https://exceljet.net/formulas/get-location-of-value-in-2d-array#main-content)

[](https://exceljet.net/formulas/get-location-of-value-in-2d-array#)

*   [Previous](https://exceljet.net/formulas/get-last-match-cell-contains)
    
*   [Next](https://exceljet.net/formulas/get-nth-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get location of value in 2D array
=================================

by Dave Bruns · Updated 29 Apr 2025

Related functions 
------------------

[TOCOL](https://exceljet.net/functions/tocol-function)

[IF](https://exceljet.net/functions/if-function)

[ADDRESS](https://exceljet.net/functions/address-function)

[ROW](https://exceljet.net/functions/row-function)

[COLUMN](https://exceljet.net/functions/column-function)

[MAP](https://exceljet.net/functions/map-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8436/download?token=IbVadjKr)
 (32.26 KB)

![Excel formula: Get location of value in 2D array](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get_location_of_value_in_2D_array.png "Excel formula: Get location of value in 2D array")

Summary
-------

To find the coordinates of all matching values in a 2D array you can use a formula based on the [IF function](https://exceljet.net/functions/if-function)
 and the [TOCOL function](https://exceljet.net/functions/tocol-function)
. In the worksheet shown, the formula in cell N8 is:

    =TOCOL(IF(C5:L16=N5,C4:L4&B5:B16,NA()),2)

When the formula is entered, it returns the coordinates of each cell that contains the value entered in cell N5, using the values in row 4 and column B for coordinates. If the value in N5, or if the range C5:L16 are updated, the the formula will return a new set of results. This formula can be adjusted to return Excel cell addresses, as explained below.

Generic formula
---------------

    =TOCOL(IF(data=A1,range1&range2,NA()),2)

Explanation 
------------

In this example, the goal is to return a list of the locations for a specific value in a 2D array of values (i.e., a table). The target value is entered in cell N5, and the table being tested is in the range C4:L16. The coordinates are supplied from row 4 and column B, as seen in the worksheet. In the current version of Excel, which supports dynamic array formulas, an easy way to solve this problem is with the IF function together with the TOCOL function. Although this example shown is generic, you can adapt a formula like this to perform a variety of tasks, including:

*   Track the location of specific items in a warehouse.
*   List open seats in a venue or classroom.
*   Show the location of items on a game board.
*   Find open time slots in a schedule grid.

> The [TOCOL function](https://exceljet.net/functions/tocol-function)
>  is a new function in Excel designed to flatten 2D arrays into a single column. By default, TOCOL will scan values by row, but it can also scan values by column. In addition, TOCOL can be configured to optionally ignore errors, a feature we use in this example.

### Conditional formatting to highlight matches

Although it is not needed to list matched locations, the worksheet shown in the example is configured to highlight the value in N5 wherever it appears with a [conditional formatting](https://exceljet.net/conditional-formatting-formulas)
 rule applied to the range C5:L16. This makes it easy to see at a glance where matching values are located. To create a rule like this:

1.  Select the range C5:L16.
2.  Home > Conditional Formatting > New rule.
3.  Use a formula to determine which cells to format.
4.  Enter the formula "=C5=$N$5" in the input area.
5.  Select the formatting of your choice.
6.  Click OK to save the rule.

Video: [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### Returning arbitrary coordinates

In the worksheet shown above, we are returning a set of coordinates based on the values entered in row 4 and column B. These values are arbitrary and can be customized as desired. In the worksheet shown, the formula in cell N8 is:

    =TOCOL(IF(C5:L16=N5,C4:L4&B5:B16,NA()),2)

Working from the inside out, the core of this formula is based on the [IF function](https://exceljet.net/functions/if-function)
, which is configured like this:

    IF(C5:L16=N5,C4:L4&B5:B16,NA())

*   _logical\_test_ - C5:L16=N5
*   _value\_if\_true_ - C4:L4&B5:B16
*   _value\_if\_false_ - NA()

The key to understanding this operation is to remember that we are testing 120 values in the table (12 rows x 10 columns), which means the IF function will return 120 results. The IF function evaluates each value in C5:L1 against the value in N5 and returns a single array with 120 TRUE/FALSE values like this:

    {FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,TRUE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE,FALSE;TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE}

The TRUE values indicate a match, and the FALSE values indicate non-matching cells. Inside the _value\_if\_true_ argument, the expression "C4:L4&B5:B16" joins the values in C4:L4 to the values in B5:B16 using [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
. The result is an array of 120 coordinates, one for each cell in the table:

    {"x1","y1","z1","a1","b1","c1","q1","r1","s1","t1";"x2","y2","z2","a2","b2","c2","q2","r2","s2","t2";"x3","y3","z3","a3","b3","c3","q3","r3","s3","t3";"x4","y4","z4","a4","b4","c4","q4","r4","s4","t4";"x5","y5","z5","a5","b5","c5","q5","r5","s5","t5";"x6","y6","z6","a6","b6","c6","q6","r6","s6","t6";"x7","y7","z7","a7","b7","c7","q7","r7","s7","t7";"x8","y8","z8","a8","b8","c8","q8","r8","s8","t8";"x9","y9","z9","a9","b9","c9","q9","r9","s9","t9";"x10","y10","z10","a10","b10","c10","q10","r10","s10","t10";"x11","y11","z11","a11","b11","c11","q11","r11","s11","t11";"x12","y12","z12","a12","b12","c12","q12","r12","s12","t12"}

As IF works through the results, it returns the associated coordinate for each TRUE created by the logical test. For FALSE results, IF uses the [NA function](https://exceljet.net/functions/na-function)
 to return a #N/A error. The result from IF is an array that contains 120 results, one for each cell in the table:

    {#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,"y3",#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,"t3";#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,"q4",#N/A,#N/A,#N/A;"x5",#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,"a8",#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,"q11",#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A}

If you look closely, you can see 6 matched locations floating in a sea of #N/A errors. These correspond to cells in B5:L16 that contain the same value as N5. The entire array is delivered to the [TOCOL function](https://exceljet.net/functions/tocol-function)
, which is configured like this:

    =TOCOL(IF(...),2)

*   array - result from the IF function
*   ignore - 2, to ignore errors

Now you can see why we've configured TOCOL to ignore all errors; we only want to keep values associated with matches, discarding the #N/A errors in the process. The result from TOCOL is a single array that contains six coordinates:

    {"y3";"t3";"q4";"x5";"a8";"q11"}

This array lands in cell N8 and spills into the range N8:N14. If the value in N5 or the values in B5:L16 are changed, the formula will return new results. The coordinates in C4:L4 and B5:B16 can be customized as desired.

### Returning cell addresses

In the example above, the goal is to return (arbitrary) coordinates entered in C4:L4 and B5:B16. The idea is that you can customize these values as needed to support your particular use case. However, you might also want to return Excel native cell addresses. To do that, you can use a modified version of the formula that adds the [ADDRESS function](https://exceljet.net/functions/address-function)
 like this:

    =TOCOL(IF(C5:L16=N5,ADDRESS(ROW(C5:L16),COLUMN(C5:L16),4),NA()),2)

![Listing cell addresses with the ADDRESS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/Get_location_of_value_in_2D_array_using_cell_addresses.png "Listing cell addresses with the ADDRESS function")

The overall structure and flow of this formula are the same as the original explained above: IF tests each value and returns the locations of matching cells, and the TOCOL function removes the errors and stacks the remaining values in a column:

    IF(C5:L16=N5,ADDRESS(ROW(C5:L16),COLUMN(C5:L16),4),NA())

*   _logical\_test_ - C5:L16=N5
*   _value\_if\_true_ - ADDRESS(ROW(C5:L16),COLUMN(C5:L16),4)
*   _value\_if\_false_ - NA()

The difference is in the _value\_if\_true_ argument, which uses the ADDRESS function to create an address for each matching value with help from the [ROW function](https://exceljet.net/functions/row-function)
 and the [COLUMN function](https://exceljet.net/functions/column-function)
:

    ADDRESS(ROW(C5:L16),COLUMN(C5:L16),4)

*   _row\_num_ - ROW(C5:L16)
*   _column\_num_ - COLUMN(C5:L16)
*   _abs\_num_ - 4, for relative address format

After IF runs, it returns an array of results (mostly errors) to TOCOL:

    =TOCOL({#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,"D7",#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,"L7";#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,"I8",#N/A,#N/A,#N/A;"C9",#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,"F12",#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,"I15",#N/A,#N/A,#N/A;#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A,#N/A},2)

As before, TOCOL is configured to ignore errors, and the final result is a single array with six matching cell addresses like his:

    {"D7";"L7";"I8";"C9";"F12";"I15"}

> The ADDRESS function can optionally return absolute addresses or R1C1-style addresses by adjusting the abs\_num argument. For details, see our [ADDRESS function page](https://exceljet.net/functions/address-function)
> .

### Returning numeric coordinates in brackets

The worksheet below shows another way to return numeric coordinates, this time using a "\[1,1\]" syntax relative to the table of values. The formula in cell N8 has been modified like this:

    =TOCOL(IF(C5:L16=N5,"["&C4:L4&","&B5:B16&"]",NA()),2)

Here again, we use concatenation to assemble numeric coordinates in square brackets when a cell matches the value in N5:

    "["&C4:L4&","&B5:B16&"]"

Otherwise, the formula's structure is the same. You can see the result below:

![Listing numeric coordinates in square brackets](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/Get_location_of_value_in_2D_array_in_square_brackets.png "Listing numeric coordinates in square brackets")

If you are new to the concept of concatenation, see: [How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
.

_Note: In the worksheet above, the numeric coordinates are manually entered in C4:L4 and B5:B16. However, the formula could easily be adjusted to use the_ [_SEQUENCE function_](https://exceljet.net/functions/sequence-function)
 _to automatically create numeric sequences to match the size of any table._

### MAP function alternative

Because I'm always on the lookout for good [MAP function](https://exceljet.net/functions/map-function)
 examples, I want to mention that you can also use MAP to solve a problem like this. The equivalent formula for the first example explained above is:

    =TOCOL(MAP(C5:L16,C4:L4&B5:B16,LAMBDA(a,b,IF(a=N5,b,NA()))),2)

Although MAP requires a custom LAMBDA calculation, it also provides a framework to separate the logic in the formula into discrete parts. In addition, because MAP iterates through values individually, you can combine MAP with functions like AND and OR. Normally, this is not possible with arrays because AND and OR are aggregate functions that return a single result.

### TEXTJOIN alternative

If you only want a list of coordinates as a text string (i.e., you don't want individual results in separate cells), you can use the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 in a formula like this:

    =TEXTJOIN(", ",1,IF(C5:L16=N5,C4:L4&B5:B16,""))

Here, we configure IF to return empty strings ("") instead of #N/A errors, and then we configure TEXTJOIN to ignore empty values and join the coordinates together, separated by a comma and a space (", ").

_Note: TOCOL does not ignore empty strings ("") in the same way as TEXTJOIN, which is why the TOCOL formula is based on ignoring errors. I'm not sure why this is. It would be better if TOCOL also ignored empty strings in formulas._ [_Let me know_](https://exceljet.net/contact)
 _if you notice this changing at some point in the future!_

Related formulas
----------------

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

[![Excel formula: Get address of lookup result](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_address_of_lookup_result.png "Excel formula: Get address of lookup result")](https://exceljet.net/formulas/get-address-of-lookup-result)

### [Get address of lookup result](https://exceljet.net/formulas/get-address-of-lookup-result)

There are certain functions in Excel that return a cell reference as a result rather than a value. Two of these functions are XLOOKUP and INDEX . The presence of the cell reference in the result is not obvious, because Excel immediately resolves the reference to the value in that cell. You can...

[![Excel formula: XLOOKUP match any column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20match%20any%20column.png "Excel formula: XLOOKUP match any column")](https://exceljet.net/formulas/xlookup-match-any-column)

### [XLOOKUP match any column](https://exceljet.net/formulas/xlookup-match-any-column)

In this example, we have a table that contains 6 columns of codes, and each row of codes belongs to a group in column B. The goal is to lookup any code in C5:H15, and return the name of the group the code belongs to. The challenge is that the code may be in any one of the six columns, and...

Related functions
-----------------

[![Excel TOCOL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20tocol%20function.png "Excel TOCOL function")](https://exceljet.net/functions/tocol-function)

### [TOCOL Function](https://exceljet.net/functions/tocol-function)

The Excel TOCOL function transforms an array into a single column. By default, TOCOL will scan values by row, but TOCOL can also scan values by column.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel ADDRESS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20address%20function.png "Excel ADDRESS function")](https://exceljet.net/functions/address-function)

### [ADDRESS Function](https://exceljet.net/functions/address-function)

The Excel ADDRESS function returns the address for a cell based on a given row and column number. For example, =ADDRESS(1,1) returns $A$1. ADDRESS can return an address in relative, mixed, or absolute format, and can be used to construct a cell reference inside a formula.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

[![Excel MAP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20map%20function.png "Excel MAP function")](https://exceljet.net/functions/map-function)

### [MAP Function](https://exceljet.net/functions/map-function)

The Excel MAP function "maps" a custom LAMBDA function to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    
*   [Get address of lookup result](https://exceljet.net/formulas/get-address-of-lookup-result)
    
*   [XLOOKUP match any column](https://exceljet.net/formulas/xlookup-match-any-column)
    

### Functions

*   [TOCOL Function](https://exceljet.net/functions/tocol-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [ADDRESS Function](https://exceljet.net/functions/address-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [MAP Function](https://exceljet.net/functions/map-function)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Conditional Formatting](https://exceljet.net/training/conditional-formatting)
    

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