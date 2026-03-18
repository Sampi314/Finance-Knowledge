# Filter values within tolerance - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-values-within-tolerance

---

[Skip to main content](https://exceljet.net/formulas/filter-values-within-tolerance#main-content)

[](https://exceljet.net/formulas/filter-values-within-tolerance#)

*   [Previous](https://exceljet.net/formulas/filter-to-show-duplicate-values)
    
*   [Next](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter values within tolerance
==============================

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[ABS](https://exceljet.net/functions/abs-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7066/download?token=jhc3Y9SP)
 (15.85 KB)

![Excel formula: Filter values within tolerance](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20values%20within%20tolerance.png "Excel formula: Filter values within tolerance")

Summary
-------

To extract and display values within a given tolerance from a larger set of data, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 together with the [ABS function](https://exceljet.net/functions/abs-function)
. In the example shown, the formula in F9 is:

    =FILTER(data,(data[Group]=G4)*(ABS(data[Value]-G5)<=G6))
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D16. The result is a list of the values in Group A that are within +/- 0.05 of 1.2.

Explanation 
------------

In this example, the goal is to list values in a given group that are within a given tolerance. The group is set in cell G4, and the target value is entered in cell G5. The allowed tolerance is entered in cell G6. The data comes from an [Excel Table](https://exceljet.net/articles/excel-tables)
 called **data** in the range B5:D16. The solution is built on the [FILTER function](https://exceljet.net/functions/filter-function)
 which can be used to extract and list data that meets multiple criteria. The beauty of this formula is that tolerance calculations do not need to be in the source data. The FILTER function creates the data it needs on the fly. When any of the variable inputs in G5:G6 are changed, or if source data changes, the results update immediately.

### Background reading

This article assumes you are familiar with Excel Tables and the FILTER function. If not, see:

*   [Excel Tables](https://exceljet.net/articles/excel-tables)
     - introduction and overview
*   [Value is within tolerance](https://exceljet.net/formulas/value-is-within-tolerance)
     - formula example
*   [The FILTER function](https://exceljet.net/functions/filter-function)
     - introduction and overview
*   [Basic FILTER function example](https://exceljet.net/formulas/basic-filter-example)
     (video)
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
     (paid training)

### Filter by Group

In order to extract records where the group is "A", we can use FILTER like this:

    =FILTER(data,data[Group]="A") // group A only
    

Here, the _array_ [argument](https://exceljet.net/glossary/function-argument)
 is the entire table, since we want both columns in the output. The _include_ argument is supplied as a simple [logical expression](https://exceljet.net/glossary/logical-test)
 that returns TRUE or FALSE for each value in the Group column:

    data[Group]="A" // returns TRUE or FALSE
    

Because we want the group to be a _variable_ input, we need to replace the hardcoded [text string](https://exceljet.net/glossary/text-value)
 "A" with a reference to cell G4, which allows the user to change the group as desired:

    =FILTER(data,data[Group]=G4)
    

Now when a user types "B" into cell G4, FILTER will extract all values from group B.

### Values within tolerance

The next task in the formula is to test for values within a given tolerance, where the target value comes from cell G5, and the acceptable tolerance is defined in cell G6. The generic logical expression for this test looks like this:

    ABS(value-target)<=tolerance)
    

The [ABS function](https://exceljet.net/functions/abs-function)
 is used to convert negative differences to positive values. [See this formula for a more detailed explanation](https://exceljet.net/formulas/value-is-within-tolerance)
. Mapping the cell references in the example to the generic formula, we get this logical expression:

    ABS(data[Value]-G5)<=G6)
    

This expression will return TRUE or FALSE for each number in the Value column. To extract all values within tolerance, ignoring group, we can use the expression above as the _include_ argument in FILTER:

    =FILTER(data,ABS(data[Value]-G5)<=G6) // ignore group
    

FILTER will ignore group and return _all values within tolerance_.

### Combining expressions

Now we need to combine both logical conditions above into a single formula. For this, we use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. Because we want to join the two expressions with AND (i.e. we want to enforce both conditions) we use the [multiplication operator](https://exceljet.net/glossary/math-operators)
 between the expressions like this:

    =(data[Group]=G4)*(ABS(data[Value]-G5)<=G6)
    

Each expression generates its own [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values, and the multiplication operation automatically coerces the TRUE and FALSE values to 1s and 0s. The standalone formula above will return 1 for values that meet both conditions, and 0 for other values.

Video: [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

Finally, we need to place the expression into the FILTER function as the _include_ argument:

    =FILTER(data,(data[Group]=G4)*(ABS(data[Value]-G5)<=G6))
    

This is the final formula. With "A" in G4, 1.2 in G5, and 0.05 in G6, the FILTER function returns rows in the table where values in Group A are within +/- 0.05 of 1.2. These results are returned to cell F9 and [spill](https://exceljet.net/glossary/spill)
 onto the worksheet. If any of the variable inputs in G4:G6 are changed, results are immediately updated.

### Filter on values out of tolerance

To reverse the logic explained above to show values that are _out of tolerance_, simply change the [logical operator](https://exceljet.net/glossary/logical-operators)
 in the tolerance expression from less than or equal to (<=), to greater than (>):

    =FILTER(data,(data[Group]=G4)*(ABS(data[Value]-G5)>G6))
    

The screen below shows the result:

![Reversed logic to show values out of tolerance](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/filter%20values%20out%20of%20tolerance.png?itok=7gUy9X_H "Reversed logic to show values out of tolerance")

Related formulas
----------------

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: FILTER on top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20on%20top%20n%20values.png "Excel formula: FILTER on top n values")](https://exceljet.net/formulas/filter-on-top-n-values)

### [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)

This formula uses the FILTER function to retrieve data based on a logical test constructed with the LARGE function. The LARGE function is a simple way to get the nth largest value in a range. Simply provide a range for the first argument ( array ), and a value for n as the second argument ( k ): =...

[![Excel formula: Biggest gainers and losers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/biggest%20gainers%20and%20losers.png "Excel formula: Biggest gainers and losers")](https://exceljet.net/formulas/biggest-gainers-and-losers)

### [Biggest gainers and losers](https://exceljet.net/formulas/biggest-gainers-and-losers)

In this example, the goal is to display the biggest 3 gainers and losers in a set of data where Start and End columns contain values at two points in time, and Change contains the percentage change in the values. The data in B5:E16 is defined as an Excel Table with the name data . Two formulas are...

[![Excel formula: Value is within tolerance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value%20is%20within%20tolerance.png "Excel formula: Value is within tolerance")](https://exceljet.net/formulas/value-is-within-tolerance)

### [Value is within tolerance](https://exceljet.net/formulas/value-is-within-tolerance)

In this example the goal is to check if values in column B are within a tolerance of .005. If a value is within tolerance, the formula should return "OK". If the value is out of tolerance, the formula should return "Fail". The expected value is listed in column C, and the allowed tolerance is...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel ABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20abs%20function.png "Excel ABS function")](https://exceljet.net/functions/abs-function)

### [ABS Function](https://exceljet.net/functions/abs-function)

The Excel ABS function returns the absolute value of a number. ABS converts negative numbers to positive numbers, and positive numbers are unaffected.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)
    
*   [Biggest gainers and losers](https://exceljet.net/formulas/biggest-gainers-and-losers)
    
*   [Value is within tolerance](https://exceljet.net/formulas/value-is-within-tolerance)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [ABS Function](https://exceljet.net/functions/abs-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

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