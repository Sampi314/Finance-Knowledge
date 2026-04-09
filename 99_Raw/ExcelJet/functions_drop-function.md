# Excel DROP function | Exceljet

**Source:** https://exceljet.net/functions/drop-function

---

[Skip to main content](https://exceljet.net/functions/drop-function#main-content)

[](https://exceljet.net/functions/drop-function#)

*   [Previous](https://exceljet.net/functions/detectlanguage-function)
    
*   [Next](https://exceljet.net/functions/expand-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

DROP Function
=============

by Dave Bruns · Updated 18 Jun 2025

Related functions 
------------------

[TAKE](https://exceljet.net/functions/take-function)

[EXPAND](https://exceljet.net/functions/expand-function)

[CHOOSEROWS](https://exceljet.net/functions/chooserows-function)

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

![Excel DROP function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")

Summary
-------

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array.

Purpose 
--------

Remove portion of an array

Return value 
-------------

The remaining array

Syntax
------

    =DROP(array,[rows],[col])

*   _array_ - The source array or range.
*   _rows_ - \[optional\] Number of rows to drop.
*   _col_ - \[optional\] Number of columns to drop.

Using the DROP function 
------------------------

The DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array. When positive numbers are provided for _rows_ or _columns_, DROP removes values from the start or top of the array. Negative numbers remove values from the end or bottom of the array.

The DROP function takes three arguments: _array_, _rows_, and _columns_. _Array_ is required, along with at least one value for _rows_ or _columns_. _Array_ can be a [range](https://exceljet.net/glossary/range)
 or an in-memory [array](https://exceljet.net/glossary/array)
 from another formula. _Rows_ and _columns_ can be negative or positive. Positive numbers remove values from the start of the _array_; negative numbers remove values from the end of the _array_. Both rows and columns default to zero: if no value is supplied, DROP will return all rows/columns in the result.

### Basic usage

To use DROP, provide an [array](https://exceljet.net/glossary/array)
 or [range](https://exceljet.net/glossary/range)
, and numbers for rows and/or columns:

    =DROP(array,3) // drop first 3 rows
    =DROP(array,,3) // drop first 3 columns
    =DROP(array,3,2) // drop first 3 rows and 2 columns
    

Notice in the second example above, no value is provided for rows.

### Drop from start

To remove rows or columns from the _start_ of a range or array, provide _positive_ numbers for rows and columns. In the worksheet below, the formula in F3 is:

    =DROP(B3:D11,6) // drop first 6 rows
    

The DROP function removes the first 6 rows from B3:D11 and returns the resulting array.

The second formula in F8 is:

    =DROP(B3:D11,5,1) // drop first 5 rows and column 1
    

The DROP function removes the first 5 rows and column 1 from B3:D11 and returns the result.

![DROP function - remove from start](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/DROP%20function%20-%20remove%20from%20start.png?itok=J8ag9s82 "DROP function - remove from start")

Notice that if a value for _rows_ or _columns_ is not provided, DROP returns _all_ rows or columns. For example, in the first formula above, a value for _columns_ is not provided and DROP returns all 3 columns as a result. In other words, _rows_ and _columns_ both default to zero.

### Drop from end

To remove values from the _end_ of an array, provide negative numbers for _rows_ and _columns_. In the worksheet below, the formula in cell F3 is:

    =DROP(B3:D11,-6)
    

With a negative 6 for _rows_, DROP removes the last 6 rows from B3:D11.

The formula in F8 is:

    =DROP(B3:D11,-5,-1)
    

With a negative 5 for _rows_ and a negative 1 for _columns_, DROP removes the last 5 rows and the last 1 column from B3:D11 and returns the resulting [array](https://exceljet.net/glossary/array)
 to cell F8.

![DROP function - drop from end of array](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/DROP%20function%20-%20drop%20from%20end%20of%20array.png?itok=FksEPKMi "DROP function - drop from end of array")

Notice in the first example, no value for _columns_ is given and DROP returns all columns as a result.

### DROP vs. TAKE

The DROP and TAKE functions both return a subset of an array, but they work in opposite ways. While the [DROP function](https://exceljet.net/functions/drop-function)
 _removes_ specific rows or columns from an array, the [TAKE function](https://exceljet.net/functions/take-function)
 _extracts_ specific rows or columns from an array:

    =DROP(array,1) // remove first row
    =TAKE(array,1) // get first row
    

Which function to use depends on the situation.

### Notes

*   _Rows_ and _columns_ are both optional, but at least one must be provided.
*   If _rows_ or _columns_ is zero, DROP returns all rows/columns.
*   If _rows_ > total rows, DROP returns a #VALUE! error
*   If _columns_ > total columns, DROP returns a #VALUE! error

DROP function examples
----------------------

[![Excel formula: Extract numbers from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract_numbers_from_text.png "Excel formula: Extract numbers from text")](https://exceljet.net/formulas/extract-numbers-from-text)

### [Extract numbers from text](https://exceljet.net/formulas/extract-numbers-from-text)

In this example, the goal is to extract the numbers from a set of property listings which describe the number of bedrooms and bathrooms, the size of the house in sq. ft., and the size of the lot in acres. Traditionally, this kind of problem has been quite difficult in Excel because each number must...

[![Excel formula: Split full name into parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_full_name_into_parts.png "Excel formula: Split full name into parts")](https://exceljet.net/formulas/split-full-name-into-parts)

### [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)

In this example, the goal is to split the names in column B into three separate parts (First, Middle, and Last) with a single formula. In cases where there is no middle name, the Middle column should be blank. In cases where there are two middle names, the Middle column should contain both names...

[![Excel formula: Cash denomination calculator](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cash_denomination_calculator.png "Excel formula: Cash denomination calculator")](https://exceljet.net/formulas/cash-denomination-calculator)

### [Cash denomination calculator](https://exceljet.net/formulas/cash-denomination-calculator)

In this example, the goal is to build a "cash denomination calculator." A cash denomination calculator is a tool for counting and verifying cash amounts. It can calculate the denominations needed to achieve a certain cash value. It can also perform the reverse calculation and determine the cash...

[![Excel formula: Longest winning streak](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/longest_winning_streak.png "Excel formula: Longest winning streak")](https://exceljet.net/formulas/longest-winning-streak)

### [Longest winning streak](https://exceljet.net/formulas/longest-winning-streak)

In this example, the goal is to calculate a count for the longest winning streak in a set of data. In the worksheet shown, wins ("W") and losses ("L") are recorded in column C, so this means we want to count the longest consecutive series of W's. Although we are specifically counting the longest...

[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)

### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...

[![Excel formula: Count numbers by range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20numbers%20by%20range.png "Excel formula: Count numbers by range")](https://exceljet.net/formulas/count-numbers-by-range)

### [Count numbers by range](https://exceljet.net/formulas/count-numbers-by-range)

In this example, the goal is to count ages in column C according to the brackets defined in columns E and F. All data is in an Excel Table named data defined in the range B5:C16. A simple way to solve this problem is with the COUNTIFS function. If you are using Excel 365 or Excel 2021, another easy...

[![Excel formula: Tiered discounts based on quantity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/tiered_discounts_based_on_quantity.png "Excel formula: Tiered discounts based on quantity")](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)

### [Tiered discounts based on quantity](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)

This example shows a workbook designed to apply discounts based on seven pricing tiers. The total quantity of items is entered as a variable in cell C4. The discount is applied via the unit costs in E7:E13, which decrease as the quantity increases. The first 200 items have an undiscounted price of...

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

[![Excel formula: Income tax bracket calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/income%20tax%20bracket%20calculation_0.png "Excel formula: Income tax bracket calculation")](https://exceljet.net/formulas/income-tax-bracket-calculation)

### [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)

In this example, the goal is to calculate the total income tax owed in a progressive tax system with multiple tax brackets, as shown in the worksheet. The article below first reviews how taxes are computed in a progressive system. Next, it shows how to accomplish this task in Excel using two...

Related functions
-----------------

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel EXPAND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20expand%20function.png "Excel EXPAND function")](https://exceljet.net/functions/expand-function)

### [EXPAND Function](https://exceljet.net/functions/expand-function)

The EXPAND function expands an array by adding rows and columns, which are supplied as separate arguments. The numbers given for rows and columns represent the dimensions of the final array....

[![Excel CHOOSEROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20chooserows%20function.png "Excel CHOOSEROWS function")](https://exceljet.net/functions/chooserows-function)

### [CHOOSEROWS Function](https://exceljet.net/functions/chooserows-function)

The Excel CHOOSEROWS function returns specific rows from an array or range. The rows to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a row in the given array.

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

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
    
*   [Tiered discounts based on quantity](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)
    
*   [Extract numbers from text](https://exceljet.net/formulas/extract-numbers-from-text)
    
*   [Count numbers by range](https://exceljet.net/formulas/count-numbers-by-range)
    
*   [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)
    
*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    
*   [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)
    
*   [Cash denomination calculator](https://exceljet.net/formulas/cash-denomination-calculator)
    
*   [Longest winning streak](https://exceljet.net/formulas/longest-winning-streak)
    

### Functions

*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [EXPAND Function](https://exceljet.net/functions/expand-function)
    
*   [CHOOSEROWS Function](https://exceljet.net/functions/chooserows-function)
    
*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    

### Links

*   [Microsoft DROP function documentation](https://support.microsoft.com/en-us/office/drop-function-1cb4e151-9e17-4838-abe5-9ba48d8c6a34)
    

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