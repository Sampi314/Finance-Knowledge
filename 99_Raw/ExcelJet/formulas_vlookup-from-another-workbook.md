# VLOOKUP from another workbook - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-from-another-workbook

---

[Skip to main content](https://exceljet.net/formulas/vlookup-from-another-workbook#main-content)

[](https://exceljet.net/formulas/vlookup-from-another-workbook#)

*   [Previous](https://exceljet.net/formulas/vlookup-from-another-sheet)
    
*   [Next](https://exceljet.net/formulas/vlookup-if-blank-return-blank)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP from another workbook
=============================

by Dave Bruns · Updated 10 May 2023

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

![Excel formula: VLOOKUP from another workbook](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/vlookup%20from%20another%20workbook.png "Excel formula: VLOOKUP from another workbook")

Summary
-------

To look up and retrieve information stored in a separate (external) workbook, you can use the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 with a full reference to the other workbook. In the example shown, the formula in C5 is:

    =VLOOKUP(B5,'[product data.xlsx]Sheet1'!$B$5:$E$13,4,0)
    

The single quotes (') in the formula above are necessary because "product data.xlsx" contains a space character.

Generic formula
---------------

    =VLOOKUP(B5,[workbook]sheet!table,4,0)

Explanation 
------------

In this example, the goal is to use VLOOKUP to find and retrieve price information for a given product stored in an external Excel workbook. The workbook exists in the same directory and the data in the file looks like this:

![Sample product data in an external workbook](https://exceljet.net/sites/default/files/images/formulas/inline/sample%20product%20data%20in%20external%20workbook.png "Sample product data in an external workbook")

Note the data itself is in the [range](https://exceljet.net/glossary/range)
 B5:E13.

### VLOOKUP formula

The formula used to solve the problem in C5, copied down, is:

    =VLOOKUP(B5,'[product data.xlsx]Sheet1'!$B$5:$E$13,4,0)
    

This is a standard use of the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 to retrieve data from the 4th column in a table:

*   _lookup\_value_ comes from B5
*   _table\_array_ is a reference to a range in an external workbook
*   _col\_index_ is 4, to retrieve data from column 4
*   _range\_lookup_ is zero to force an exact match

The only difference is the special syntax used for external references, in the "t_able\_array_" argument. The syntax for external references is:

    '[workbook]sheet'!range
    

*   **workbook** - the name of the external workbook (product data.xlsx)
*   **sheet** \- the name of the sheet containing the range (Sheet1)
*   **range** - the actual range for the table array ($B$5:$E$13)

Note the workbook and sheet part of the reference are enclosed in single quotes (') because the file name "product data.xlsx" contains a space character. Also, note the range is entered as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
. This allows the formula to be copied down the column without the range changing.

### Entering the reference

The easiest way to enter a reference to an external range is to use the "point and click" method. Begin entering the VLOOKUP function normally. Then, when entering the _table\_array_ argument, browse to the external workbook and select the range directly in the other file. Excel will construct the needed reference automatically.

Note the reference will change depending on whether the external file is open or not. If the external workbook is open, VLOOKUP will show the workbook name and address for the _table\_array_ argument, as in the screenshot above. If the external file is not open, VLOOKUP will display the full file path to the workbook + workbook name and address.

### Handling spaces and punctuation

Note the reference to the workbook is enclosed in square brackets, and the entire workbook + sheet is enclosed in single quotes. The single quotes (') are required when the workbook or sheet name contains space or punctuation characters

Related formulas
----------------

[![Excel formula: VLOOKUP from another sheet](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20from%20another%20sheet2.png "Excel formula: VLOOKUP from another sheet")](https://exceljet.net/formulas/vlookup-from-another-sheet)

### [VLOOKUP from another sheet](https://exceljet.net/formulas/vlookup-from-another-sheet)

In this example, we have a table of employee locations like this on Sheet2: On Sheet1, we retrieve the building location for each team member using this formula: =VLOOKUP(B5,Sheet2!$B$5:$C$104,2,0) The lookup value is the employee ID, from cell B5. For the table array, we use the range $B$5:$C$104...

[![Excel formula: Dynamic workbook reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20workbook%20reference.png "Excel formula: Dynamic workbook reference")](https://exceljet.net/formulas/dynamic-workbook-reference)

### [Dynamic workbook reference](https://exceljet.net/formulas/dynamic-workbook-reference)

In this example, the goal is to create a reference to an external workbook with variable information. The easiest way to do this is to assemble the reference to a range or cell in another workbook as a text value , then use the INDIRECT function to convert the text to an actual reference. In Excel...

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)

### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...

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

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20for%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

### [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

In a lot of cases, you'll use VLOOKUP to find exact matches based on some kind of unique id, but there are many situations where you'll want to use VLOOKUP to find non-exact matches. A classic case is using VLOOKUP to find a commission rate based on a sales number. Let's take a look. Here we have...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Why%20VLOOKUP%20is%20better%20than%20nested%20IFs-thumb.png)](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

### [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

In this video we look at a few reasons why VLOOKUP is a better option than nested IF statements. In our last video, we used nested IF statements to calculate a commission rate based on a sales number. As a quick recap: The first formula is created with nested IF statements normally. The second...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20to%20merge%20tables-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-to-merge-tables)

### [How to use VLOOKUP to merge tables](https://exceljet.net/videos/how-to-use-vlookup-to-merge-tables)

In this video I'll demonstrate how you can use VLOOKUP to join data in separate tables. In this worksheet we have two tables. In the first table, we have order data. You can see that we've got a date, customer id, product, and total. In a second sheet we have customer data. We've got first and last...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP from another sheet](https://exceljet.net/formulas/vlookup-from-another-sheet)
    
*   [Dynamic workbook reference](https://exceljet.net/formulas/dynamic-workbook-reference)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    
*   [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)
    
*   [How to use VLOOKUP to merge tables](https://exceljet.net/videos/how-to-use-vlookup-to-merge-tables)
    

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