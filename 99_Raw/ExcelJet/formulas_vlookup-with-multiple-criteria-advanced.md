# VLOOKUP with multiple criteria advanced - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced

---

[Skip to main content](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced#main-content)

[](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced#)

*   [Previous](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/vlookup-with-numbers-and-text)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP with multiple criteria advanced
=======================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7089/download?token=4Y8sGDKT)
 (17.49 KB)

![Excel formula: VLOOKUP with multiple criteria advanced](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP%20with%20multiple%20criteria%20advanced.png "Excel formula: VLOOKUP with multiple criteria advanced")

Summary
-------

To apply multiple criteria with the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 you can use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 and the [CHOOSE function](https://exceljet.net/functions/choose-function)
. In the example shown, the formula in H8 is:

    =VLOOKUP(1,CHOOSE({1,2},(H5=data[Item])*(H6=data[Size])*(H7=data[Color]),data[Price]),2,0)
    

where "data" is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in B5:E15. The result is $30.00, the price of a Large Red Hoodie.

_This is an [array formula](https://exceljet.net/glossary/array-formula)
, and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Explanation 
------------

In this example, the goal is to use VLOOKUP to retrieve the price for a given item based on three criteria: name, size, and color, which are entered in H5:H7. For example, for a Blue Medium T-shirt, VLOOKUP should return $16.00.

The [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 does not handle multiple criteria natively. Normally VLOOKUP looks through the leftmost column in a table for a match, and returns a value from a given column in a matching row. There is no built-in way to supply multiple criteria.

This example works around this limitation by using Boolean logic to create an [array](https://exceljet.net/glossary/array)
 of ones and zeros that represent rows that meet multiple conditions, then using this array to create a _new_ table to provide to VLOOKUP. The overall process looks like this:

*   Use Boolean logic to test Item, Size, and Color
*   Create a new table with the [CHOOSE function](https://exceljet.net/functions/choose-function)
    
*   Provide the new table to VLOOKUP
*   Configure VLOOKUP to look for 1 in the new table

This is a flexible way to apply multiple criteria with the VLOOKUP function. The logic can be extended as needed to apply more conditions, and each condition can use Excel's full range of formula logic.

_Note: This example shows an advanced technique to handle multiple criteria with VLOOKUP.  If you have more basic needs, [this formula](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
 takes a simple approach with a helper column. Other more flexible options include [INDEX and MATCH](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
 and [XLOOKUP](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
._

### Background study

This article assumes you are familiar with the VLOOKUP function and Excel Tables. If not, see:

*   [Excel Tables](https://exceljet.net/articles/excel-tables)
     - introduction and overview
*   [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
     - overview with examples
*   [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
     - 3 minute video

### Boolean algebra for criteria

Working from the inside-out, the snippet below uses [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 to create a temporary [array](https://exceljet.net/glossary/array)
 of ones and zeros:

    (H5=data[Item])*(H6=data[Size])*(H7=data[Color])
    

Here we compare the item in H5 against all items, the size in H6 against all sizes, and the color in H7 against all colors. The initial result is three arrays of TRUE/FALSE values like this:

    ={FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE}*{FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE}*{TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE}
    

The math operation of multiplying the arrays together converts the TRUE FALSE values to 1s and 0s:

    ={0;0;0;0;1;1;1;1;0;0;0}*{0;0;1;0;0;0;1;0;0;0;1}*{1;0;1;0;0;0;1;0;0;1;0}
    

And after multiplication, we have a single array like this:

    {0;0;0;0;0;0;1;0;0;0;0}
    

The process described above can be visualized as seen below. The "Result" array shows that the 7th row in the table meets all three conditions. 

![Multiple criteria boolean array visualization](https://exceljet.net/sites/default/files/images/formulas/inline/VLOOKUP%20multiple%20criteria%20boolean%20algebra%20array.png "Multiple criteria boolean array visualization")

In the next step, we'll use the Result array to build a new table that we can use with VLOOKUP.

### Creating a new table

We now have an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values that will work as a key to which row(s) in the table meet criteria. The problem is that this array is not actually part of the table VLOOKUP needs as the _table\_array_ argument. What we need is a _new_ table, that combines the Result array from the Boolean operation above with the Price column of the table. We can do this with the CHOOSE function.

Normally, the [CHOOSE function](https://exceljet.net/functions/choose-function)
 is used to select a value by numeric position. For example, to get the second value from a list of three values, you could use CHOOSE like this:

    =CHOOSE(2,"red","blue","green") // returns "blue"
    

Notice the _index\_num_ argument is provided as 2 to get the second value. CHOOSE is flexible, and the values it accepts can be a mix of constants, cell references, arrays, and ranges. For this problem, we need to give CHOOSE two arrays:  the Boolean result array, and the Price column of the table. Then, for _index\_num_, we provide the [array constant](https://exceljet.net/glossary/array-constant)
 {1,2} like this:

    CHOOSE({1,2},(H5=data[Item])*(H6=data[Size])*(H7=data[Color]),data[Price])
    

The array constant is the tricky part. By using {1,2} for _index\_num_ we are requesting the first and second value at the same time. The CHOOSE function dutifully complies, and returns both arrays "glued" together in a single array that looks like this:

    {0,15;0,16;0,17;0,17.5;0,28;0,29;1,30;0,32;0,20;0,21;0,22}
    

In the above format, it is hard to see the structure of the array. However, if we place the array in an Excel worksheet, the structure becomes clear. As you can see, the array is a 2-column table:

![Table created by CHOOSE in memory](https://exceljet.net/sites/default/files/images/formulas/inline/VLOOKUP%20multiple%20criteria%20array%20created%20by%20choose.png "Table created by CHOOSE in memory")

We now have a new table we can use in VLOOKUP.

### VLOOKUP function

All of the work done so far has just one purpose: to create a new table that can be used in VLOOKUP as the _table\_array_ argument. Now we need to configure the VLOOKUP function. We start by providing a lookup value of 1, to match the structure of the new table:

    =VLOOKUP(1
    

Next, we drop in the code explained above for _table\_array_:

    =VLOOKUP(1,CHOOSE({1,2},(H5=data[Item])*(H6=data[Size])*(H7=data[Color]),data[Price])
    

To wrap things up, we set _col\_index\_num_ to 2, and _range\_lookup_ to 0. The final formula in H8 is:

    =VLOOKUP(1,CHOOSE({1,2},(H5=data[Item])*(H6=data[Size])*(H7=data[Color]),data[Price]),2,0)
    

VLOOKUP matches the 1 in row 7, and returns 30 as a final result. If any of the input values in H5:H7 change, a new table is assembled and VLOOKUP returns a new result.

_Note: This is an [array formula](https://exceljet.net/glossary/array-formula)
, and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Related formulas
----------------

[![Excel formula: VLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20muliple%20criteria.png "Excel formula: VLOOKUP with multiple criteria")](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

### [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

In the example shown, we want to look up employee departments and groups using VLOOKUP by matching the first and last name of an employee. One limitation of VLOOKUP is that it only handles one condition: the lookup\_value, which is matched against the first column in the table. This makes it...

[![Excel formula: INDEX and MATCH with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20and%20MATCH%20with%20multiple%20criteria.png "Excel formula: INDEX and MATCH with multiple criteria")](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

### [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

This is a more advanced formula. For basics, see How to use INDEX and MATCH . Normally, an INDEX MATCH formula is configured with MATCH set to look through a one-column range and provide a match based on given criteria. Without concatenating values in a helper column , or in the formula itself,...

[![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

### [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for lookup\_value and lookup\_array . How can we...

[![Excel formula: VLOOKUP with 2 lookup tables](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20two%20lookup%20tables.png "Excel formula: VLOOKUP with 2 lookup tables")](https://exceljet.net/formulas/vlookup-with-2-lookup-tables)

### [VLOOKUP with 2 lookup tables](https://exceljet.net/formulas/vlookup-with-2-lookup-tables)

Working from the inside out, the IF function in this formula, which is entered as the "table\_array" argument in VLOOKUP, runs a logical test on the value in column C "Years", which represents the number of years a salesperson has been with a company. If C5 is less than 2, then table1 is returned as...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

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

*   [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
    
*   [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
    
*   [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
    
*   [VLOOKUP with 2 lookup tables](https://exceljet.net/formulas/vlookup-with-2-lookup-tables)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    

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