# Filter data between dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-data-between-dates

---

[Skip to main content](https://exceljet.net/formulas/filter-data-between-dates#main-content)

[](https://exceljet.net/formulas/filter-data-between-dates#)

*   [Previous](https://exceljet.net/formulas/filter-contains-one-of-many)
    
*   [Next](https://exceljet.net/formulas/filter-every-nth-row)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter data between dates
=========================

by Dave Bruns · Updated 28 Apr 2025

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[DATE](https://exceljet.net/functions/date-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7945/download?token=uN6ugRU6)
 (14.71 KB)

![Excel formula: Filter data between dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter_data_between_dates.png "Excel formula: Filter data between dates")

Summary
-------

To filter data to extract records between two dates, you can use the FILTER function with [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. In the example shown, the formula in F8 is:

    =FILTER(B5:D16,(C5:C16>=F5)*(C5:C16<=G5),"No data")
    

The result is a list of records with dates between 15-Jan-23 and 15-Mar-23, inclusive.

Generic formula
---------------

    =FILTER(data,(dates>=A1)*(dates<=A2),"No data")

Explanation 
------------

The goal is to extract records with dates that are greater than or equal to a start date in F5 and less than or equal to an end date in G5. You might think we can use the [AND function](https://exceljet.net/functions/and-function)
 inside FILTER to solve this problem. However, because AND returns just a single value, this won't work. Instead, we use something called "Boolean logic" to validate the dates.

### Background study

Use the links below to learn the concepts explained in this article.

*   [How to use the FILTER function](https://exceljet.net/functions/filter-function)
     - overview with examples
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
     - 3 min intro video
*   [Boolean logic in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
     - 3 min video
*   [Boolean operations in array operations](https://exceljet.net/videos/boolean-operations-in-array-formulas)
     - 3 min video
*   [Dynamic array formulas](https://exceljet.net/training/dynamic-array-formulas)
     - paid training

### FILTER function

This formula uses the [FILTER function](https://exceljet.net/functions/filter-function)
 to retrieve data based on a logical test created with a [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 expression. The _array_ argument is provided as B5:D16, which contains the full set of data without headers. The _include_ argument is based on two logical comparisons:

    (C5:C16>=F5)*(C5:C16<=G5)
    

This is an example of Boolean logic. The expression on the left checks if dates are greater than or equal to the "From" date in F5. The expression on the right checks if dates are less than or equal to the "To" date in G5. The two expressions are joined with a multiplication [operator](https://exceljet.net/glossary/math-operators)
 (\*), which creates an AND relationship. After logical expressions are evaluated, we have two [arrays](https://exceljet.net/glossary/array)
 that contain TRUE and FALSE values like this:

     {FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE}*{TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

Notice there are 12 results in each array, one for each date in the data. The multiplication operation automatically converts the TRUE and FALSE values to 1s and 0s, so you should visualize the operation like this:

    {0;1;1;1;1;1;1;1;1;1;1;1}*{1;1;1;1;1;0;0;0;0;0;0;0}

After multiplication is complete, the final result is a single array like this:

    {0;1;1;1;1;0;0;0;0;0;0;0}
    

Note that there are four 1s in the array, which correspond to the four dates that pass the logical test. This array is delivered to the FILTER function as the _include_ argument and used to filter the data:

    =FILTER(B5:D16,{0;1;1;1;1;0;0;0;0;0;0;0},"No data")

Only the rows with a result of 1 are included in the final output. The _if\_empty_ argument is set to "No data" in case no matching data is found.

> For more details on FILTER, see: [How to use the FILTER function](https://exceljet.net/functions/filter-function)
> .

### With hardcoded start and end dates

In the example shown, we are picking up valid dates from cells F5 and G5. This makes the formula easier to write and more flexible since the dates can easily be changed at any time. However, in certain situations, you may want to hardcode dates into the formula. The safest way to do this in Excel is to use the [DATE function](https://exceljet.net/functions/date-function)
 as shown below:

    =FILTER(B5:D16,(C5:C16>=DATE(2023,1,15))*(C5:C16<=DATE(2023,3,15)),"No data")

The structure of this formula is the same as the original formula above, but the start date of January 15, 2023, and the end date of March 15, 2023, are now provided directly with the DATE function.

Related formulas
----------------

[![Excel formula: Filter by date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter_by_date.png "Excel formula: Filter by date")](https://exceljet.net/formulas/filter-by-date)

### [Filter by date](https://exceljet.net/formulas/filter-by-date)

This example shows how to filter dates using Excel's FILTER function. Several common date-based filtering patterns are shown below, including filtering by month, filtering by a specific date, and filtering by month and year. Filter by month In the worksheet below, the goal is to filter the data to...

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: FILTER with complex multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20complex%20multiple%20criteria.png "Excel formula: FILTER with complex multiple criteria")](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

### [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

In this example, we need to construct logic that filters data to include: account begins with "x" AND region is "east", and month is NOT April. The filtering logic of this formula (the include argument) is created by chaining together three expressions that use boolean logic on arrays in the data...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20with%20two%20criteria-play.png)](https://exceljet.net/videos/filter-function-with-two-criteria)

### [FILTER function with two criteria](https://exceljet.net/videos/filter-function-with-two-criteria)

In this video, we’ll set up the FILTER function with two criteria. The FILTER function is designed to extract data from a list or table using supplied criteria. In this worksheet, we have data that contains an order number, amount, name, and state. Our goal is to use the FILTER function to extract...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Filter by date](https://exceljet.net/formulas/filter-by-date)
    
*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    

### Videos

*   [FILTER function with two criteria](https://exceljet.net/videos/filter-function-with-two-criteria)
    

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