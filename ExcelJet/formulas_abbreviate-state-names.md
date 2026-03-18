# Abbreviate state names - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/abbreviate-state-names

---

[Skip to main content](https://exceljet.net/formulas/abbreviate-state-names#main-content)

[](https://exceljet.net/formulas/abbreviate-state-names#)

*   [Previous](https://exceljet.net/formulas/how-to-fix-the-value-error)
    
*   [Next](https://exceljet.net/formulas/add-leading-zeros-to-numbers)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Abbreviate state names
======================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Abbreviate state names](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Abbreviate%20state%20names.png "Excel formula: Abbreviate state names")

Summary
-------

To convert full state names to their two letter abbreviation (i.e. Minnesota > MN), you can use a simple formula based on VLOOKUP. In the example shown, the formula in E5 is:

    =VLOOKUP(C5,states,2,0)
    

Where "states" is the [named range](https://exceljet.net/glossary/named-range)
 G5:H55.

Generic formula
---------------

    =VLOOKUP(name,states,2,0)

Explanation 
------------

This formula relies on a table with columns for both the full state name and the 2-letter abbreviation. Because we are using VLOOKUP, the full name must be in the first column. For simplicity, the table has been named "states".

VLOOKUP is configured to get the lookup value from column C. The table array is the named range "states", the column index is 2, to retrieve the abbreviation from the second column). The final argument, range\_lookup, has been set to zero (FALSE) to force an exact match.

    =VLOOKUP(C5,states,2,0)
    

VLOOKUP locates the matching entry in the "states" table, and returns the corresponding 2-letter abbreviation.

### Generic mapping

This is a good example of how VLOOKUP can be used to convert values using a lookup table. This same approach can be used to lookup and convert many other types of values. For example, you could use VLOOKUP to map numeric error codes to human readable names.

### Reverse lookup

What if you have a state abbreviation, and want to lookup the full state name using the lookup table in the example? In that case, you'll need to switch to INDEX and MATCH. With a lookup value in A1, this formula will return a full state name with the lookup table as shown:

    =INDEX(G5:G55,MATCH(A1,H5:H55,0))
    

If you want to use the same named range "states" you can use this version to convert a 2-letter abbreviation to a full state name.

    =INDEX(INDEX(states,0,1),MATCH(A1,INDEX(states,0,2),0))
    

Here, we use INDEX to return whole columns by supplying a row number of zero. This is a cool and useful feature of the [INDEX function](https://exceljet.net/functions/index-function)
: if you supply zero for row, you get whole column(s) if you supply zero for column, you get whole row(s).

Related formulas
----------------

[![Excel formula: Group numbers with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/group_numbers_with_VLOOKUP.png "Excel formula: Group numbers with VLOOKUP")](https://exceljet.net/formulas/group-numbers-with-vlookup)

### [Group numbers with VLOOKUP](https://exceljet.net/formulas/group-numbers-with-vlookup)

In this example, the goal is to group ages into buckets. One way to do this is to prepare a table with age breakpoints in the first column, and the name of the appropriate group or bucket in the second column. Then use a lookup function to find the right bucket or group for each age. In the example...

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)

### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...

[![Excel formula: Map inputs to arbitrary values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20inputs%20to%20arbitrary%20values.png "Excel formula: Map inputs to arbitrary values")](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)

### [Map inputs to arbitrary values](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)

In this example, the goal is to map the numbers 1-6 to the arbitrary values seen in the table below. For example: If the input is 1, the output should be 10 If the input is 2, the output should be 81 If the input is 3, the output should be 17 If the input is 4, the output should be 23 And so on.....

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

[![Excel formula: Map inputs to arbitrary values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20inputs%20to%20arbitrary%20values.png "Excel formula: Map inputs to arbitrary values")](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)

### [Map inputs to arbitrary values](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)

In this example, the goal is to map the numbers 1-6 to the arbitrary values seen in the table below. For example: If the input is 1, the output should be 10 If the input is 2, the output should be 81 If the input is 3, the output should be 17 If the input is 4, the output should be 23 And so on.....

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Why%20VLOOKUP%20is%20better%20than%20nested%20IFs-thumb.png)](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

### [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

In this video we look at a few reasons why VLOOKUP is a better option than nested IF statements. In our last video, we used nested IF statements to calculate a commission rate based on a sales number. As a quick recap: The first formula is created with nested IF statements normally. The second...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20replace%20nested%20IFs%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

### [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

You might build or inherit a worksheet that uses a series of nested IF statements to assign values of some kind. Many people use nested IF statements this way because the approach is easy once you get the hang of it. But nested IF statements can be difficult to maintain and debug. Let's look at how...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20for%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

### [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

In a lot of cases, you'll use VLOOKUP to find exact matches based on some kind of unique id, but there are many situations where you'll want to use VLOOKUP to find non-exact matches. A classic case is using VLOOKUP to find a commission rate based on a sales number. Let's take a look. Here we have...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Group numbers with VLOOKUP](https://exceljet.net/formulas/group-numbers-with-vlookup)
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [Map inputs to arbitrary values](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    
*   [Map inputs to arbitrary values](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    

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