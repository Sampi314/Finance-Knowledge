# Excel SUM function | Exceljet

**Source:** https://exceljet.net/functions/sum-function

---

[Skip to main content](https://exceljet.net/functions/sum-function#main-content)

[](https://exceljet.net/functions/sum-function#)

*   [Previous](https://exceljet.net/functions/subtotal-function)
    
*   [Next](https://exceljet.net/functions/sumif-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

SUM Function
============

by Dave Bruns · Updated 6 Jan 2022

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel SUM function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")

Summary
-------

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Purpose 
--------

Add numbers together

Return value 
-------------

The sum of values supplied.

Syntax
------

    =SUM(number1,[number2],[number3],...)

*   _number1_ - The first value to sum.
*   _number2_ - \[optional\] The second value to sum.
*   _number3_ - \[optional\] The third value to sum.

Using the SUM function 
-----------------------

The SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

The SUM function takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form _number1_, _number2_, _number3_, etc. up to 255 total. Arguments can be a hardcoded constant, a cell reference, or a [range](https://exceljet.net/glossary/range)
. All numbers in the arguments provided are summed. The SUM function automatically ignores empty cells and text values, which makes SUM useful for summing cells that may contain text values.

The SUM function will sum hardcoded values and numbers that result from formulas. If you need to sum a range and _ignore_ existing subtotals, see the [SUBTOTAL function](https://exceljet.net/functions/subtotal-function)
.

### Examples

Typically, the SUM function is used with ranges. For example:

    =SUM(A1:A9) // sum 9 cells in A1:A9
    =SUM(A1:F1) // sum 6 cells in A1:F1
    =SUM(A1:A100) // sum 100 cells in A1:A100
    

Values in all arguments are summed together, so the following formulas are equivalent:

    =SUM(A1:A5)
    =SUM(A1,A2,A3,A4,A5)
    =SUM(A1:A3,A4:A5)
    

In the example shown, the formula in D12 is:

    =SUM(D6:D10) // returns 9.05
    

References do not need to be next to one another. For example:

    =SUM(A1,F13,E100)
    

### Sum with text values

The SUM function automatically ignores text values without returning an error. This can be useful in [situations like this](https://exceljet.net/formulas/odometer-gas-mileage-log)
, where the first formula would otherwise throw an error.

### Keyboard shortcut

Excel provides a keyboard shortcut to [automatically sum a range of cells above](https://exceljet.net/shortcuts/autosum-selected-cells)
. You can see a demonstration [in this video](https://exceljet.net/videos/23-excel-formula-tips)
.

### Notes

*   SUM automatically ignores empty cells and cells with text values.
*   If arguments contain errors, SUM will return an error.
*   The [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
     can sum while ignoring errors.
*   SUM can handle up to 255 total arguments.
*   Arguments can be supplied as constants, ranges, [named ranges](https://exceljet.net/glossary/named-range)
    , or cell references.

SUM function examples
---------------------

[![Excel formula: Sum if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_not_blank.png "Excel formula: Sum if not blank")](https://exceljet.net/formulas/sum-if-not-blank)

### [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)

In this example, the goal is to sum the Amounts in C5:C16 when the Lead in D5:D16 is not blank (i.e., not empty). A good way to solve this problem is to use the SUMIFS function . However, you can also use the SUMPRODUCT function or the FILTER function , as explained below. Because SUMPRODUCT and...

[![Excel formula: Sum every nth row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20row.png "Excel formula: Sum every nth row")](https://exceljet.net/formulas/sum-every-nth-row)

### [Sum every nth row](https://exceljet.net/formulas/sum-every-nth-row)

In this example, the goal is to sum every nth value in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value (every other value), if n =3, we want to sum every third value, and so on. All data is in the range B5:B16 and n is entered into cell F5 as...

[![Excel formula: Sum numbers in single cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_numbers_in_cell.png "Excel formula: Sum numbers in single cell")](https://exceljet.net/formulas/sum-numbers-in-single-cell)

### [Sum numbers in single cell](https://exceljet.net/formulas/sum-numbers-in-single-cell)

The goal is to sum numbers that appear inside a single cell as seen in column B. Technically, the numbers in each cell are a single text string, and the numbers are separated by commas, which is referred to as a "delimiter". In the current version of Excel, the easiest way to solve this problem is...

[![Excel formula: Lookup and sum column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Lookup%20and%20sum%20column.png "Excel formula: Lookup and sum column")](https://exceljet.net/formulas/lookup-and-sum-column)

### [Lookup and sum column](https://exceljet.net/formulas/lookup-and-sum-column)

The core of this formula uses the INDEX and MATCH function in a special way to return a full column instead of a single value. Working from the inside out, the MATCH function is used to find the correct column number for the fruit in I6: MATCH(I6,C4:F4,0) MATCH return 2 inside the INDEX function as...

[![Excel formula: Volunteer hours requirement calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volunteer%20hours%20requirement%20calculation.png "Excel formula: Volunteer hours requirement calculation")](https://exceljet.net/formulas/volunteer-hours-requirement-calculation)

### [Volunteer hours requirement calculation](https://exceljet.net/formulas/volunteer-hours-requirement-calculation)

In this example, the goal create a formula that will return TRUE when a volunteer has successfully logged the required number of hours in each of the three categories. Two requirements must be satisfied: A volunteer should have at least 5 hours in each of the three categories. A volunteer needs to...

[![Excel formula: Sum multiple tables](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sum%20multiple%20tables.png "Excel formula: Sum multiple tables")](https://exceljet.net/formulas/sum-multiple-tables)

### [Sum multiple tables](https://exceljet.net/formulas/sum-multiple-tables)

This formula uses structured references to refer to the "Amount" column in each table. The structured references in this formula resolve to normal references like this: =SUM(Table1\[Amount\],Table2\[Amount\]) =SUM(C7:C11,F7:F13) =1495.5 When rows or columns are added or removed from either table, the...

[![Excel formula: Data validation don't exceed total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20dont%20exceed%20total.png "Excel formula: Data validation don't exceed total")](https://exceljet.net/formulas/data-validation-dont-exceed-total)

### [Data validation don't exceed total](https://exceljet.net/formulas/data-validation-dont-exceed-total)

Data validation rules are triggered when a user adds or changes a cell value. In this case, we need a formula that returns FALSE as long as entries in C6:C9 sum to a total equal to or below 1000. We use the SUM function to sum a fixed range and then simply compare the result to 1000 using less than...

[![Excel formula: Sum every n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20n%20rows.png "Excel formula: Sum every n rows")](https://exceljet.net/formulas/sum-every-n-rows)

### [Sum every n rows](https://exceljet.net/formulas/sum-every-n-rows)

In this example, the goal is to calculate a weekly total using the data as shown. Notice each week corresponds to 5 rows of data (Monday-Friday) so we will need to sum values in every 5 rows. To build a range that corresponds to the correct 5 rows for each week, we use the OFFSET function. To sum...

[![Excel formula: SUMIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS_with_multiple_criteria_and_OR_logic.png "Excel formula: SUMIFS with multiple criteria and OR logic")](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)

### [SUMIFS with multiple criteria and OR logic](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)

In this example, the goal is to sum the value of orders that have a status of "Complete" or "Pending". This is a slightly tricky problem in Excel because the SUMIFS function is designed for conditional sums based on multiple criteria, but all criteria must be TRUE in order for a value to be...

[![Excel formula: Sum race time splits](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sum%20race%20time%20splits.png "Excel formula: Sum race time splits")](https://exceljet.net/formulas/sum-race-time-splits)

### [Sum race time splits](https://exceljet.net/formulas/sum-race-time-splits)

Excel times are fractional numbers . This means you can add times together with the SUM function to get total durations. However, you must take care to enter times with the right syntax and use a suitable time format to display results, as explained below. Enter times in the correct format You must...

[![Excel formula: Sum entire column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20entire%20column.png "Excel formula: Sum entire column")](https://exceljet.net/formulas/sum-entire-column)

### [Sum entire column](https://exceljet.net/formulas/sum-entire-column)

In this example, the goal is to return the total for an entire column in an Excel worksheet. One way to do this is to use a full column reference. Full column references Excel supports " full column " like this: =SUM(A:A) // sum all of column A =SUM(C:C) // sum all of column C =SUM(A:C) // sum all...

[![Excel formula: Sum top n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20top%20n%20values%20with%20criteria.png "Excel formula: Sum top n values with criteria")](https://exceljet.net/formulas/sum-top-n-values-with-criteria)

### [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)

In this example, the goal is to sum the largest n values in a set of data after applying specific criteria. In the worksheet shown, we want to sum the three largest values, so n is equal to 3. At a high level, this problem breaks down into three separate steps: Apply criteria to select specific...

[![Excel formula: Sum last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_last_n_columns.png "Excel formula: Sum last n columns")](https://exceljet.net/formulas/sum-last-n-columns)

### [Sum last n columns](https://exceljet.net/formulas/sum-last-n-columns)

In this example, the goal is to sum the last n columns in a set of data, where n is a variable that can be changed at any time. In the latest version of Excel, the easiest way to solve this problem is with the TAKE function . In older versions of Excel you can use the OFFSET function , as explained...

[![Excel formula: Running total in Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20total%20in%20table2.png "Excel formula: Running total in Table")](https://exceljet.net/formulas/running-total-in-table)

### [Running total in Table](https://exceljet.net/formulas/running-total-in-table)

At the core, this formula has a simple pattern like this: =SUM(first:current) Where "first" is the first cell in the Total column, and "current" is a reference to a cell in the current row of the Total column. To get the a reference to the first cell, we use INDEX like this: INDEX(\[Total\],1) Here,...

[![Excel formula: Sum first n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_first_n_rows.png "Excel formula: Sum first n rows")](https://exceljet.net/formulas/sum-first-n-rows)

### [Sum first n rows](https://exceljet.net/formulas/sum-first-n-rows)

In the example shown, we have a list of amounts by month. The goal is to dynamically sum values through a given number of months using a variable n in cell E5. Since month names are just text, and months are listed in order, the key requirement is to sum amounts by position , starting with cell C5...

SUM function videos
-------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20trace%20a%20formula%20error-thumb.png)](https://exceljet.net/videos/how-to-trace-a-formula-error)

### [How to trace a formula error](https://exceljet.net/videos/how-to-trace-a-formula-error)

In this video we'll look at how to trace a formula error. Here we have a simple sales summary for a team of salespeople over a period of 4 months. You can see that we have monthly totals in the bottom row and totals for each salesperson in the last column. Below the table, we have a sales target...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20Excel%20Table%20ranges%20work-Thumb.png)](https://exceljet.net/videos/how-excel-table-ranges-work)

### [How Excel Table ranges work](https://exceljet.net/videos/how-excel-table-ranges-work)

In this video, we'll take a closer look at how table ranges work. One of the most useful features of Excel Tables is that they create a dynamic range. A dynamic range automatically expands to handle new data, so it works well for reports, pivot tables, or charts that need to show the latest...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20Table%20Options-Thumb.png)](https://exceljet.net/videos/excel-table-options)

### [Excel Table Options](https://exceljet.net/videos/excel-table-options)

In this video, we'll look at the options available for Excel Tables. Excel provides four settings for Tables you should be aware of. The first option controls whether a table range will automatically adjust as data changes. By default, this option is enabled, since this feature is a key benefit of...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20convert%20booleans%20to%20numbers-PLay.png)](https://exceljet.net/videos/how-to-convert-booleans-to-numbers)

### [How to convert Booleans to numbers](https://exceljet.net/videos/how-to-convert-booleans-to-numbers)

In this video, we'll look at some ways you can convert TRUE and FALSE values in Excel to 1s and 0s. When working with more advanced formulas, especially array formulas, you need to know how to convert TRUE and FALSE values in Excel to their numeric equivalents, 1 and 0. This is best explained with...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20an%20average%20value-thumb.png)](https://exceljet.net/videos/how-to-calculate-an-average-value)

### [How to calculate an average value](https://exceljet.net/videos/how-to-calculate-an-average-value)

In this video we'll look at how to calculate an average value. Let's take a look. In this worksheet we have a list of 16 properties, each with a price and other information. Let's calculate an average price. First, I'll create a named range for the prices. This makes the formulas easier to read and...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)

### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)

In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_use_text_formatting-thumb.png)](https://exceljet.net/videos/how-to-use-text-formatting-in-excel)

### [How to use text formatting in Excel](https://exceljet.net/videos/how-to-use-text-formatting-in-excel)

In this lesson we'll look at the Text format. It may seem strange to format numbers as text, but there are times when it makes sense. The Text format displays numbers exactly as they were entered. Let's take a look. In column B of our table we have a set of numbers that are displayed as we like,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20is%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/what-is-an-excel-table)

### [What is an Excel Table](https://exceljet.net/videos/what-is-an-excel-table)

In this video, we'll introduce the idea of an Excel Table. So, what is an Excel Table? An Excel table is a rectangular range of data that has been defined and named in a particular way. To illustrate, here I have two rectangular ranges of data. Both ranges contain exactly the same data but neither...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_edit_a_formula-thumb.png)](https://exceljet.net/videos/how-to-edit-a-formula)

### [How to edit a formula](https://exceljet.net/videos/how-to-edit-a-formula)

One thing you'll need to do in Excel is check and edit formulas to keep them in sync with other worksheet changes. Editing a formula in Excel is similar to editing other content. One difference is that you can update cell references using drag and drop. Let's take a look. Here we have a worksheet...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20is%20a%20function%3F-thumb_0.png)](https://exceljet.net/videos/what-is-a-function)

### [What is a function?](https://exceljet.net/videos/what-is-a-function)

What's a function? A function is a special type of formula. You can think of a function as a pre-built formula with a specific purpose created to save time. Excel has hundreds of functions. To introduce the idea of a function, we'll look at the SUM function . The SUM function is one of the most...

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells equal to this or that](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)
    
*   [Sum numbers in single cell](https://exceljet.net/formulas/sum-numbers-in-single-cell)
    
*   [Sum every n rows](https://exceljet.net/formulas/sum-every-n-rows)
    
*   [Sum matching columns](https://exceljet.net/formulas/sum-matching-columns)
    
*   [Sum across multiple worksheets](https://exceljet.net/formulas/sum-across-multiple-worksheets)
    
*   [Count unique text values with criteria](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Sum time](https://exceljet.net/formulas/sum-time)
    
*   [Count missing values](https://exceljet.net/formulas/count-missing-values)
    
*   [Dropdown sum with all option](https://exceljet.net/formulas/dropdown-sum-with-all-option)
    

### Videos

*   [What is a function?](https://exceljet.net/videos/what-is-a-function)
    
*   [How to edit a formula](https://exceljet.net/videos/how-to-edit-a-formula)
    
*   [How to use relative references - example 2](https://exceljet.net/videos/how-to-use-relative-references-example-2)
    
*   [How to use text formatting in Excel](https://exceljet.net/videos/how-to-use-text-formatting-in-excel)
    
*   [How to add a calculated field to a pivot table](https://exceljet.net/videos/how-to-add-a-calculated-field-to-a-pivot-table)
    
*   [Examples of flagged errors in formulas](https://exceljet.net/videos/examples-of-flagged-errors-in-formulas)
    
*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    
*   [How to trace a formula error](https://exceljet.net/videos/how-to-trace-a-formula-error)
    
*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [How to use the SUM function](https://exceljet.net/videos/how-to-use-the-sum-function)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Links

*   [Microsoft SUM function documentation](https://support.office.com/en-us/article/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)
    

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