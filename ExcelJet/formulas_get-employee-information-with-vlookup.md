# Get employee information with VLOOKUP - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-employee-information-with-vlookup

---

[Skip to main content](https://exceljet.net/formulas/get-employee-information-with-vlookup#main-content)

[](https://exceljet.net/formulas/get-employee-information-with-vlookup#)

*   [Previous](https://exceljet.net/formulas/get-cell-content-at-given-row-and-column)
    
*   [Next](https://exceljet.net/formulas/get-first-match-cell-contains)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get employee information with VLOOKUP
=====================================

by Dave Bruns · Updated 31 May 2023

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

[TAKE](https://exceljet.net/functions/take-function)

[DROP](https://exceljet.net/functions/drop-function)

![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")

Summary
-------

To look up employee information in a table with a unique id in the first column, you can use the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
. In the example shown, the formula in cell H6 is:

    =VLOOKUP(id,data,2,0)
    

where **id** (H4) and **data** (B4:E104) are [named ranges](https://exceljet.net/glossary/named-range)
.

_Note: although VLOOKUP is a simple way to solve this problem, you can also use XLOOKUP. Using XLOOKUP with a single table (the named range **data**) is an interesting challenge. See below for details._

Generic formula
---------------

    =VLOOKUP(id,data,column,0)

Explanation 
------------

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both approaches. For convenience, **id** (H4) and **data** (B4:E104) are [named ranges](https://exceljet.net/glossary/named-range)
.

### VLOOKUP function

VLOOKUP is an Excel function to get data from a table organized _vertically_. Lookup values must appear in the first column of the table passed into VLOOKUP. The data to retrieve is specified by column number, and the generic syntax for VLOOKUP looks like this:

    =VLOOKUP(lookup_value,table_array,column_index_num,range_lookup)

The syntax looks a bit scary in this form, but it is quite simple in practice. The formulas below show how to get the first name, last name, and email address with VLOOKUP:

    =VLOOKUP(id,data,2,0) // first
    =VLOOKUP(id,data,3,0) // last
    =VLOOKUP(id,data,4,0) // email

In these formulas, **id** is the named range B4 (which contains the lookup value), and **data** is the named range B4:E104 (the data in the table). Next, we have the column number, which is a number that indicates the column from which we want to retrieve data, where the first column is column 1 and contains lookup values. We provide 2 to retrieve the first name, 3 to retrieve the last name, and 4 to retrieve the email address. Notice that this is the _only thing changing_ in the formulas above, every other input remains the same. Finally, we have the last value, which is zero (0). We use zero in these formulas to tell VLOOKUP to only perform an exact match. In "exact match mode" VLOOKUP will only match an id value exactly. If an id is not found, VLOOKUP will return the #N/A error. With the number 869 in cell H4, the formulas above return the results seen in the worksheet in column H:

    =VLOOKUP(id,data,2,0) // returns "Julie"
    =VLOOKUP(id,data,3,0) // returns "Irons"
    =VLOOKUP(id,data,4,0) // returns "j.irons@abc.com"

To enter formulas like this, start with the first formula, then copy it down and change the column number as needed. The named ranges will behave like [absolute references](https://exceljet.net/glossary/absolute-reference)
 and will not change when the formula is copied to a new location.

_Note: VLOOKUP will perform an approximate match by default. This is a dangerous default in this case because the data is not sorted, and there is a good chance that VLOOKUP will return an incorrect result. It is therefore important_ to _require an exact match by using FALSE or 0 for the last [argument](https://exceljet.net/glossary/function-argument)
, which is called "range\_lookup". [More information here](https://exceljet.net/functions/vlookup-function)
._

### XLOOKUP function

Another way to solve this problem is with [XLOOKUP](https://exceljet.net/functions/xlookup-function)
, a modern upgrade to the VLOOKUP function. This minimal syntax for XLOOKUP looks like this:

    =XLOOKUP(lookup_value,lookup_array,return_array)

Unlike VLOOKUP, we don't give XLOOKUP the _entire table_. Instead, we provide separate ranges for _lookup\_array_ and _return\_array_. The formulas to look up the first name, last name, and email address with XLOOKUP look like this:

    =XLOOKUP(id,B5:B104,C5:C104) // first
    =XLOOKUP(id,B5:B104,D5:D104) // last
    =XLOOKUP(id,B5:B104,E5:E104) // email

Notice the only value changing is the range provided for _return\_array_, which varies according the to information we want to retrieve. We use C5:C104 for the first name, D5:D104 for the first name, and E5:E104 for the email address. The value for lookup\_value is the named range **id** (H4). See below for information on how to adapt this formula to use the existing named range **data** (B4:E104).

_Note: Normally, I would use absolute references to make the formulas easier to copy, but I have left these ranges relative to make them a bit easier to read._

### XLOOKUP with a named range

If we had named ranges for **ids**, **first**, **last**, and **email** defined, we could use them in XLOOKUP like this:

    =XLOOKUP(id,ids,first) // first
    =XLOOKUP(id,ids,last) // last
    =XLOOKUP(id,ids,email) // email

Similarly, if **data** was a proper [Excel Table](https://exceljet.net/articles/excel-tables)
, we could use structured references like so:

    =XLOOKUP(id,data[Id],data[First]) // first
    =XLOOKUP(id,data[Id],data[Last]) // last
    =XLOOKUP(id,data[Id],data[Email]) // email

Both of these options above would work well with XLOOKUP. However, in the example shown, we only have the named range **data** (B5:E104). Is there a way to use the entire table directly with XLOOKUP? Yes. It's a little tricky, but we can use the CHOOSECOLS function.

### XLOOKUP with CHOOSECOLS

One way to use XLOOKUP with the named range **data** is to use the CHOOSECOLS function like this:

    =XLOOKUP(id,CHOOSECOLS(data,1),CHOOSECOLS(data,2)) // first
    =XLOOKUP(id,CHOOSECOLS(data,1),CHOOSECOLS(data,3)) // last
    =XLOOKUP(id,CHOOSECOLS(data,1),CHOOSECOLS(data,4)) // email

The [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
 returns one or more columns from a range by numeric index. In the formulas above, we are using CHOOSECOLS to get the first column (1) for the _lookup\_array_ in all formulas. Then, for _result\_array_, we vary the number as needed to get to provide the correct range for first name (2), last name (3), and email address (4).

_Note: Excel purists will point out that we could also use the [INDEX function](https://exceljet.net/functions/index-function)
 to retrieve columns for XLOOKUP. Yes, absolutely._

### XLOOKUP with DROP and TAKE

Yet another way to solve this problem is to use the [TAKE function](https://exceljet.net/functions/take-function)
 with the [DROP function](https://exceljet.net/functions/drop-function)
 with the entire named range data:

    =XLOOKUP(id,TAKE(data,,1),DROP(data,,1))

This formula will return all first, last, and email all in one step and the result will spill into the worksheet in three cells _horizontally_. To get all three values in a _vertical_ array, you can wrap the above formula in the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
:

    =TRANSPOSE(XLOOKUP(id,TAKE(data,,1),DROP(data,,1)))

TRANSPOSE simply flips the orientation of the array returned by XLOOKUP.

Related formulas
----------------

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel DROP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")](https://exceljet.net/functions/drop-function)

### [DROP Function](https://exceljet.net/functions/drop-function)

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20for%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

### [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

In a lot of cases, you'll use VLOOKUP to find exact matches based on some kind of unique id, but there are many situations where you'll want to use VLOOKUP to find non-exact matches. A classic case is using VLOOKUP to find a commission rate based on a sales number. Let's take a look. Here we have...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20replace%20nested%20IFs%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

### [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

You might build or inherit a worksheet that uses a series of nested IF statements to assign values of some kind. Many people use nested IF statements this way because the approach is easy once you get the hang of it. But nested IF statements can be difficult to maintain and debug. Let's look at how...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    
*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [DROP Function](https://exceljet.net/functions/drop-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
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