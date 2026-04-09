# Map inputs to arbitrary values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/map-inputs-to-arbitrary-values

---

[Skip to main content](https://exceljet.net/formulas/map-inputs-to-arbitrary-values#main-content)

[](https://exceljet.net/formulas/map-inputs-to-arbitrary-values#)

*   [Previous](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    
*   [Next](https://exceljet.net/formulas/map-text-to-numbers)
    

[Grouping](https://exceljet.net/formulas#Grouping)

Map inputs to arbitrary values
==============================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

![Excel formula: Map inputs to arbitrary values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/map%20inputs%20to%20arbitrary%20values.png "Excel formula: Map inputs to arbitrary values")

Summary
-------

To map inputs to arbitrary values, you can use the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
. In the worksheet shown, the formula in cell F7 is:

    =VLOOKUP(F6,B5:C10,2,0)
    

With a lookup value of 4 in cell F6, the result is 23 based on the table in columns B and C.

Generic formula
---------------

    =VLOOKUP(input,map_table,column,0)

Explanation 
------------

In this example, the goal is to map the numbers 1-6 to the arbitrary values seen in the table below. For example:

*   If the input is 1, the output should be 10
*   If the input is 2, the output should be 81
*   If the input is 3, the output should be 17
*   If the input is 4, the output should be 23
*   And so on...

| Input | Output |
| --- | --- |
| 1   | 10  |
| 2   | 81  |
| 3   | 17  |
| 4   | 23  |
| 5   | 13  |
| 6   | 31  |

Although we could solve this problem with a complicated [nested IF formula](https://exceljet.net/articles/nested-ifs)
, a better option is to put the table on the worksheet and perform a lookup operation. The [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 provides an easy way to do this. In the example shown, the formula in F7 is:

    =VLOOKUP(F6,B5:C10,2,0)
    

*   _lookup\_value_ - the value in cell F6 (4)
*   _table\_array_ - the range B5:C10
*   _col\_index\_num_ - 2, to specify the second column
*   _range\_lookup_ - zero, to force an exact match

Although in this case, we are mapping numeric inputs to numeric outputs, the same basic approach will readily handle text values for both inputs and outputs. A good example is [converting test scores to grades](https://exceljet.net/formulas/vlookup-calculate-grades)
. 

### Alternative with CHOOSE

If you have a limited number of inputs, and if the inputs are numbers starting with 1, you can also use the [CHOOSE function](https://exceljet.net/functions/choose-function)
. For the example shown the equivalent formula based on CHOOSE is:

    =CHOOSE(F6,10,81,17,23,13,31)
    

The choose function is unwieldy for large amounts of data but for smaller data sets that map to a 1-based index, it has the advantage of being a simple "all in one" solution.

Related formulas
----------------

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)

### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

[![Excel formula: Sum text values like numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20text%20values%20like%20numbers.png "Excel formula: Sum text values like numbers")](https://exceljet.net/formulas/sum-text-values-like-numbers)

### [Sum text values like numbers](https://exceljet.net/formulas/sum-text-values-like-numbers)

The heart of this formula is a basic INDEX and MATCH formula, used to translate text values into numbers as defined in a lookup table. For example, to translate "EX" to the corresponding number, we would use: =INDEX(value,MATCH("EX",code,0)) which would return 4. The twist in this problem however...

[![Excel formula: Map text to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20text%20to%20numbers.png "Excel formula: Map text to numbers")](https://exceljet.net/formulas/map-text-to-numbers)

### [Map text to numbers](https://exceljet.net/formulas/map-text-to-numbers)

This formula uses the value in cell F7 for a lookup value, the range B6:C10 for the lookup table, the number 2 to indicate "2nd column", and zero as the last argument to force an exact match. Although in this case we are mapping text values to numeric outputs, the same formula can handle text to...

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

*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    
*   [Sum text values like numbers](https://exceljet.net/formulas/sum-text-values-like-numbers)
    
*   [Map text to numbers](https://exceljet.net/formulas/map-text-to-numbers)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    

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