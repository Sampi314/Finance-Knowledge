# Left lookup with VLOOKUP - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/left-lookup-with-vlookup

---

[Skip to main content](https://exceljet.net/formulas/left-lookup-with-vlookup#main-content)

[](https://exceljet.net/formulas/left-lookup-with-vlookup#)

*   [Previous](https://exceljet.net/formulas/left-lookup-with-index-and-match)
    
*   [Next](https://exceljet.net/formulas/list-missing-values)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Left lookup with VLOOKUP
========================

by Dave Bruns · Updated 15 May 2024

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

![Excel formula: Left lookup with VLOOKUP](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Look%20left%20with%20VLOOKUP.png "Excel formula: Left lookup with VLOOKUP")

Summary
-------

To use VLOOKUP to perform a lookup to the left, you can use the [CHOOSE function](https://exceljet.net/functions/choose-function)
 to reorder the lookup table. In the example shown, the formula in F5 is:

    =VLOOKUP(E5,CHOOSE({1,2},score,rating),2,0)
    

where score (C5:C9) and rating (B5:B9) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =VLOOKUP(A1,CHOOSE({1,2},range2,range1),2,0)

Explanation 
------------

One of the [VLOOKUP function's](https://exceljet.net/functions/vlookup-function)
 key limitations is that it can only look up values to the right. In other words, the column that contains lookup values must sit to the left of the values you want to retrieve with VLOOKUP. There is no way to override this behavior since it is hardwired into the function. As a result, with normal configuration, there is no way to use VLOOKUP to look up a rating in column B based on a score in column C.

One workaround is to restructure the lookup table itself and move the lookup column to the left of the lookup value(s). That's the approach taken in this example, which uses the CHOOSE function reverse rating and score like this:

    CHOOSE({1,2},score,rating)
    

Normally, CHOOSE is used with a single index number as the first argument, and the remaining arguments are the values to choose from. However, here we give choose an [array constant](https://exceljet.net/glossary/array-constant)
 for the index number containing two numbers: {1,2}. Essentially, we are asking choose for both the first and second values.

The values are provided as the two named ranges in the example: score and rating. Notice however that we are providing these ranges in reversed order. The CHOOSE function selects both ranges in the order provided and returns the result as a single array like this:

    {5,"Excellent";4,"Good";3,"Average";2,"Poor";1,"Terrible"}
    

CHOOSE returns this array directly to VLOOKUP as the table array argument. In other words, CHOOSE is delivering a lookup table like this to VLOOKUP:

![Restructured lookup table](https://exceljet.net/sites/default/files/images/formulas/inline/restructured%20lookup%20table.png "Restructured lookup table")

Using the lookup value in E5, VLOOKUP locates a match inside the newly created table and returns a result from the second column.

### Reordering with the array constant

In the example shown, we are reordering the lookup table by reversing "rating" and "score" inside the CHOOSE function. However, we could instead use the array constant to reorder like this:

    CHOOSE({2,1},rating,score)
    

The result is exactly the same.

### With INDEX and MATCH

While the above example works fine, it isn't ideal. For one thing, most average users won't understand how the formula works. A more natural solution is [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
. Here is the equivalent formula:

    =INDEX(rating,MATCH(E5,score,0))
    

In fact, this is a good example of how INDEX and MATCH is more flexible than VLOOKUP.

Related formulas
----------------

[![Excel formula: Left lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/left%20lookup%20with%20index%20and%20match_0.png "Excel formula: Left lookup with INDEX and MATCH")](https://exceljet.net/formulas/left-lookup-with-index-and-match)

### [Left lookup with INDEX and MATCH](https://exceljet.net/formulas/left-lookup-with-index-and-match)

In this example, the goal is to lookup data to the left of an ID that appears as the last column in the table. In other words, we need to locate a match in column E, then retrieve a value from a column to the left. This is one of those problems that is difficult with VLOOKUP , but easy with INDEX...

[![Excel formula: VLOOKUP with variable table array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20variable%20table%20array.png "Excel formula: VLOOKUP with variable table array")](https://exceljet.net/formulas/vlookup-with-variable-table-array)

### [VLOOKUP with variable table array](https://exceljet.net/formulas/vlookup-with-variable-table-array)

In this example, the goal is to set up VLOOKUP to retrieve costs based on a variable vendor name. In other words, we want a formula that allows us to switch tables dynamically based on a user-supplied value. There are two cost tables in the worksheet, one for Vendor A and one for Vendor B. Both...

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

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

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

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

*   [Left lookup with INDEX and MATCH](https://exceljet.net/formulas/left-lookup-with-index-and-match)
    
*   [VLOOKUP with variable table array](https://exceljet.net/formulas/vlookup-with-variable-table-array)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    
*   [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)
    

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