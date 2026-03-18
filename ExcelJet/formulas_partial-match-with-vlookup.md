# Partial match with VLOOKUP - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/partial-match-with-vlookup

---

[Skip to main content](https://exceljet.net/formulas/partial-match-with-vlookup#main-content)

[](https://exceljet.net/formulas/partial-match-with-vlookup#)

*   [Previous](https://exceljet.net/formulas/partial-match-with-numbers-and-wildcard)
    
*   [Next](https://exceljet.net/formulas/position-of-first-partial-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Partial match with VLOOKUP
==========================

by Dave Bruns · Updated 3 Jun 2021

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6637/download?token=iz6EzMLj)
 (18.62 KB)

![Excel formula: Partial match with VLOOKUP](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Partial%20match%20with%20VLOOKUP.png "Excel formula: Partial match with VLOOKUP")

Summary
-------

To retrieve information from a table based on a partial match, you can use the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 in exact match mode with a [wildcard](https://exceljet.net/glossary/wildcard)
. In the example shown, the formula in H7 is:

    =VLOOKUP(value&"*",data,2,FALSE)
    

where **value** (H4) and **data** (B5:E104) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =VLOOKUP(value&"*",data,column,FALSE)

Explanation 
------------

In this example, the goal is to retrieve employee information from a table using only a partial match on the last name. In other words, by typing "Aya" into cell H4, the formula should retrieve information about Michael Ayala.

The [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 supports [wildcards](https://exceljet.net/glossary/wildcard)
, which makes it possible to perform a partial match on a lookup value. For instance, you can use VLOOKUP to retrieve values from a table based on typing in only part of a lookup value. To use wildcards with VLOOKUP, you must specify exact match mode by providing FALSE or 0 (zero) for the last argument called _range\_lookup_.

In this example, we use the asterisk (\*) as a wildcard which matches zero or more characters. To allow a partial match of the value typed into H4, which is [named](https://exceljet.net/glossary/named-range)
 "value," we supply a lookup value to VLOOKUP like this:

    value&"*" // create lookup value
    

This expression joins the text in the named range **value** with a wildcard using the ampersand (&) to [concatenate](https://exceljet.net/glossary/concatenation)
. If we type a string like "Aya" into the named range **value** (H4), the result is "Aya\*", which is returned directly to VLOOKUP as the lookup value. Placing the wildcard at the end results in a "begins with" match. This will cause VLOOKUP to match the first entry in column B that begins with "Aya."

Wildcard matching is convenient because you don't have to type in a full name, but you must be careful of duplicates or near duplicates. For example, the table contains both "Bailer" and a "Bailey," so typing "Bai" into H4 will return only the first match ("Bailer"), even though there are two names that begin with "Bai."

Note: in [Excel 365](https://exceljet.net/glossary/excel-365)
, the [FILTER function](https://exceljet.net/functions/filter-function)
 can display _all_ matches at the same time.

### Other columns

The formulas in the range H7:H10 are very similar; the only difference is the column index:

    =VLOOKUP(value&"*",data,2,FALSE) // first
    =VLOOKUP(value&"*",data,1,FALSE) // last
    =VLOOKUP(value&"*",data,3,FALSE) // id
    =VLOOKUP(value&"*",data,4,FALSE) // dept
    

### Contains type match

For a "contains type" match, where the search string can appear anywhere in the lookup value, you need to use two wildcards like this:

    =VLOOKUP("*"&value&"*",data,2,FALSE)
    

This will join an asterisk to both sides of the lookup value so that VLOOKUP will find the first match that _contains_ the text typed into H4.

_Note: you must set exact match mode using FALSE or 0 (zero) for the last argument in VLOOKUP when using wildcards._

### FILTER function

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the new [FILTER function](https://exceljet.net/functions/filter-function)
 provides a [more powerful way to filter on partial matches](https://exceljet.net/formulas/filter-with-partial-match)
.

Related formulas
----------------

[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)

### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...

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

[![Excel formula: FILTER with partial match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20partial%20match.png "Excel formula: FILTER with partial match")](https://exceljet.net/formulas/filter-with-partial-match)

### [FILTER with partial match](https://exceljet.net/formulas/filter-with-partial-match)

In this example, the goal is to extract a set of records that match a partial text string . To keep things simple, we are only matching one field in the data, the last name ("Last"). The core operation of this formula comes from the FILTER function (new in Excel 365 ) which extracts matching data...

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

*   [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    
*   [FILTER with partial match](https://exceljet.net/formulas/filter-with-partial-match)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    

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