# VLOOKUP two-way lookup  - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-two-way-lookup

---

[Skip to main content](https://exceljet.net/formulas/vlookup-two-way-lookup#main-content)

[](https://exceljet.net/formulas/vlookup-two-way-lookup#)

*   [Previous](https://exceljet.net/formulas/vlookup-tax-rate-calculation)
    
*   [Next](https://exceljet.net/formulas/vlookup-variable-commission-split)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP two-way lookup
======================

by Dave Bruns · Updated 4 Apr 2023

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")

Summary
-------

To perform a two-way lookup (i.e. a matrix lookup), you can combine the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 with the [MATCH function](https://exceljet.net/functions/match-function)
 to get a column number. In the example shown, the formula in cell H6 is

    =VLOOKUP(H4,B5:E16,MATCH(H5,B4:E4,0),0)
    

Cell H4 provides the lookup value for the row ("Colby"), and cell H5 supplies the lookup value for the column ("Feb". The result is 9,350, the value for Colby in February.

Generic formula
---------------

    =VLOOKUP(value,table,MATCH(value,range,0),0)

Explanation 
------------

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a _dynamic column index number_ by using the MATCH function to locate the right column. This technique allows you to create a dynamic two-way lookup, matching on both rows _and_ columns. It can also make a VLOOKUP formula more resilient. VLOOKUP can break when columns are inserted or removed from a table, but a formula that uses VLOOKUP + MATCH can continue to work correctly even changes are made to columns.

### VLOOKUP formula

This is a standard VLOOKUP exact match formula with one exception: the column index is supplied by the MATCH function. If we remove the MATCH function, the core VLOOKUP formula to match the name in H4 and retrieve a value for February is:

    =VLOOKUP(H4,B5:E16,3,0)

The _lookup\_value_ is the name in cell H4, the _table\_array_ is the range B5:E16, the _col\_index\_num_ is hardcoded as 3 (to retrieve values from the "Feb" column), and _range\_lookup_ is set to 0 to force an exact match. (Note: you can use either zero or FALSE for _range\_lookup_ with the same result). With these inputs, the formula returns 9,350, the value for Colby in February.

### MATCH formula

The goal in this example is to dynamically generate a column number for VLOOKUP based on the value in cell H5. To do this, we use the MATCH function like this:

    MATCH(H5,B4:E4,0) // returns 3

The _lookup\_value_ is the month abbreviation in cell H5, the _lookup\_array_ is the range B4:E4, and _match\_type_ is set to zero (0) to specify an exact match. With this configuration, MATCH returns 3 since the matching value is in cell D4, which is the third value in the range B4:E4. Note that the lookup array given to MATCH (BB4:E4) representing column headers deliberately includes cell B4, even though cell B4 does not contain a month name. This is done so that the number returned by MATCH is in sync with the lookup table given by VLOOKUP. In other words, we need to give MATCH a range that spans the same number of columns as the lookup table given to VLOOKUP.

### VLOOKUP + MATCH

The final formula with VLOOKUP and MATCH together is:

    =VLOOKUP(H4,B5:E16,MATCH(H5,B4:E4,0),0)

Notice that the MATCH function is provided to VLOOKUP _as the column index number_. Excel evaluates the formula from the inside out. The MATCH function is evaluated and returns 3 directly to VLOOKUP as _col\_num\_index_:

    =VLOOKUP(H4,B5:E16,3,0)

The VLOOKUP function then runs and returns a final result of 9,350. This is the value for Colby in February. Note that the month lookup is now dynamic. For example, if the month is changed to "Mar", MATCH returns 4 and VLOOKUP returns a final result of 12,550.

Related formulas
----------------

[![Excel formula: Two-way lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20lookup%20with%20INDEX%20and%20MATCH.png "Excel formula: Two-way lookup with INDEX and MATCH")](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

### [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

In this example, the goal is to perform a two-way lookup, sometimes called a matrix lookup . This means we need to create a match on both rows and columns and return the value at the intersection of this two-way match The core of this formula is INDEX, which is simply retrieving a value from C6:G10...

[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)

### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

[![Excel formula: Get nth match with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_match_with_VLOOKUP.png "Excel formula: Get nth match with VLOOKUP")](https://exceljet.net/formulas/get-nth-match-with-vlookup)

### [Get nth match with VLOOKUP](https://exceljet.net/formulas/get-nth-match-with-vlookup)

The table contains basic order information, with columns for Date, Product, Name, and Amount. The Helper column is used to create a special lookup value, as explained below. The goal is to retrieve the nth matching record in a table for a specific product, which is entered in cell I4. For example,...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20replace%20nested%20IFs%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

### [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

You might build or inherit a worksheet that uses a series of nested IF statements to assign values of some kind. Many people use nested IF statements this way because the approach is easy once you get the hang of it. But nested IF statements can be difficult to maintain and debug. Let's look at how...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20for%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

### [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

In a lot of cases, you'll use VLOOKUP to find exact matches based on some kind of unique id, but there are many situations where you'll want to use VLOOKUP to find non-exact matches. A classic case is using VLOOKUP to find a commission rate based on a sales number. Let's take a look. Here we have...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Why%20VLOOKUP%20is%20better%20than%20nested%20IFs-thumb.png)](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

### [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

In this video we look at a few reasons why VLOOKUP is a better option than nested IF statements. In our last video, we used nested IF statements to calculate a commission rate based on a sales number. As a quick recap: The first formula is created with nested IF statements normally. The second...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    
*   [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    
*   [Get nth match with VLOOKUP](https://exceljet.net/formulas/get-nth-match-with-vlookup)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    
*   [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)
    

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