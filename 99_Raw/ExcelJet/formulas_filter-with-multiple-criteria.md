# Filter with multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-with-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/filter-with-multiple-criteria#main-content)

[](https://exceljet.net/formulas/filter-with-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/filter-with-multiple-or-criteria)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter with multiple criteria
=============================

by Dave Bruns · Updated 28 Apr 2025

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

![Excel formula: Filter with multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter_with_multiple_criteria.png "Excel formula: Filter with multiple criteria")

Summary
-------

To filter data with multiple criteria, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 and simple [boolean logic](https://exceljet.net/glossary/boolean-logic)
 expressions. In the example shown, the formula in F5 is:

    =FILTER(B5:D16,(C5:C16="A")*(D5:D16>80),"No data")
    

The result returned by FILTER includes only rows where the group is "A" and the score is greater than 80. If no data meets criteria, FILTER returns "No data".

Generic formula
---------------

    =FILTER(range,(criteria1)*(criteria2),"No data")

Explanation 
------------

In this example, the goal is to filter data based on multiple criteria with the FILTER function. Specifically, we want to select data where (1) the group = "A" and (2) the Score is greater than 80. At first glance, it's not obvious how to do this with the FILTER function. Unlike older functions like [COUNTIFS](https://exceljet.net/functions/countifs-function)
 or [SUMIFS](https://exceljet.net/functions/sumifs-function)
, which provide multiple arguments for entering multiple conditions, the FILTER function only provides a single argument called "include" to filter data. The trick is to create logical expressions that use [Boolean algebra](https://exceljet.net/glossary/boolean-logic)
 to target the data of interest and supply these expressions as the _include_ argument.

### FILTER function

The FILTER function "filters" a range of data based on supplied criteria and extracts matching records. The generic syntax for FILTER looks like this:

    FILTER(array,include,[if_empty])

The idea with FILTER is that the _include_ argument is provided as a logical expression that targets data of interest. Most of the challenge in using FILTER is developing a logical expression that correctly targets data that meets all conditions.

> Video: [Basic FILTER function example](https://exceljet.net/videos/filter-function-basic-example)

### FILTER with multiple criteria

In this problem, we need to configure FILTER to apply two criteria: (1) Group is "A" and (2) Score is greater than 80. To start off, we provide all data (B5:D16) for the _array_ argument, because we want FILTER to return all three columns:

    =FILTER(B5:D16,

Next, we need to supply the logic needed to target records where the Group is "A". We do this with a simple logical expression:

    =C5:C16="A"

Here, we compare every value in the Group column to "A". Because we have 12 rows of data, the result is an [array](https://exceljet.net/glossary/array)
 that contains 12 TRUE and FALSE values like this:

    {TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE}

Notice the TRUE values in the array correspond to rows where the Group is "A". If we were to use this expression by itself as the _include_ argument, FILTER will return all 4 rows where the Group is "A". Next, we need to add logic to target records with the second condition: Score is greater than 80. This can be done with another simple logical expression:

    =D5:D16>80

Like the previous expression, this snippet will return an array that contains 12 TRUE and FALSE values:

    {TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE}

In this array, TRUE values indicate rows where the score is greater than 80. At this point, we have two simple logical expressions, and we need to join them inside the include argument. To do this, we need to add parentheses around both expressions (to control the [order of operations](https://exceljet.net/glossary/order-of-operations)
) and then _multiply_ to two expressions together:

    =(C5:C16="A")*(D5:D16>80)

We use multiplication (\*) because, under the [rules of Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
, multiplication corresponds to _AND logic_, and addition (+) corresponds to _OR logic_.

> Video: [Boolean algebra in Excel formulas](https://exceljet.net/videos/boolean-algebra-in-excel)

After each expression is evaluated, we have the following two [arrays](https://exceljet.net/glossary/array)
:

    ={TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE}*{TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE}
    

The math operation of multiplication converts the TRUE and FALSE values to 1s and 0s:

    ={1;0;0;1;0;0;1;0;0;1;0;0}*{1;1;0;1;1;1;1;0;1;0;1;0}

After multiplication, we have a single array:

    ={1;0;0;1;0;0;1;0;0;0;0;0}

Notice that the 1s in this array correspond to rows in the data where the Group is "A" and the score is greater than 80. This is exactly what we need to retrieve data that matches both conditions. This array is returned directly to FILTER as the _include_ argument:

    =FILTER(B5:D16,{1;0;0;1;0;0;1;0;0;0;0;0},"No data")

The final result from FILTER is the three rows in the data that meet the criteria.

Related formulas
----------------

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: Filter by date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter_by_date.png "Excel formula: Filter by date")](https://exceljet.net/formulas/filter-by-date)

### [Filter by date](https://exceljet.net/formulas/filter-by-date)

This example shows how to filter dates using Excel's FILTER function. Several common date-based filtering patterns are shown below, including filtering by month, filtering by a specific date, and filtering by month and year. Filter by month In the worksheet below, the goal is to filter the data to...

[![Excel formula: FILTER with complex multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20complex%20multiple%20criteria.png "Excel formula: FILTER with complex multiple criteria")](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

### [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

In this example, we need to construct logic that filters data to include: account begins with "x" AND region is "east", and month is NOT April. The filtering logic of this formula (the include argument) is created by chaining together three expressions that use boolean logic on arrays in the data...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20algebra%20in%20Excel-Play.png)](https://exceljet.net/videos/boolean-algebra-in-excel)

### [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

In this video, we’ll look at how boolean algebra is used for AND and OR logic in formulas. In Boolean algebra, there are only two possible results for a math operation: 1 or 0, which, as we know, correspond to the logical values TRUE and FALSE. AND logic corresponds to multiplication . Anything...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20operations%20in%20array%20formulas-Play.png)](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

In this video, we'll look at why boolean operations are important in array formulas. Boolean operations are a key building block in the world of dynamic array formulas. To illustrate, let's look at some simple order data. Given the data shown, how can we total orders from Texas using an array...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Filter by date](https://exceljet.net/formulas/filter-by-date)
    
*   [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Videos

*   [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

### Training

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