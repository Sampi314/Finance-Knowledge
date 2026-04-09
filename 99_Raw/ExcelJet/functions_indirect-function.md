# Excel INDIRECT function | Exceljet

**Source:** https://exceljet.net/functions/indirect-function

---

[Skip to main content](https://exceljet.net/functions/indirect-function#main-content)

[](https://exceljet.net/functions/indirect-function#)

*   [Previous](https://exceljet.net/functions/index-function)
    
*   [Next](https://exceljet.net/functions/lookup-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

INDIRECT Function
=================

by Dave Bruns · Updated 28 May 2025

![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")

Summary
-------

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

Purpose 
--------

Create a reference from text

Return value 
-------------

A valid worksheet reference.

Syntax
------

    =INDIRECT(ref_text,[a1])

*   _ref\_text_ - A reference supplied as text.
*   _a1_ - \[optional\] A boolean to indicate A1 or R1C1-style reference. Default is TRUE = A1 style.

Using the INDIRECT function 
----------------------------

The INDIRECT function converts a [text string](https://exceljet.net/glossary/text-value)
 like "Sheet1!A1" into a valid reference like `=Sheet1!A1`. That sounds simple enough, but of all Excel's [many functions](https://exceljet.net/functions)
, INDIRECT might be the most confusing to users. Why would you use _text_ when you can simply provide a normal reference? Well, one reason is that you already have a reference as text (perhaps in a cell), and you want to make Excel _understand the text as a reference_. Another reason is that you want to build a _dynamic reference_ using different bits of information. With text, it's easy to hardcode some values, pick up other values on the worksheet, and join the values together using [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
. The problem, however, is that once you have created a reference as text, Excel won't recognize it as a reference. To Excel, it's just an ordinary text value. _The INDIRECT function is like a magic wand that converts a text value to an actual reference._

> INDIRECT is a [volatile function](https://exceljet.net/glossary/volatile-function)
>  and can cause performance issues in large or complex worksheets.

### Quick syntax demo

INDIRECT takes two [arguments](https://exceljet.net/glossary/function-argument)
, in a generic syntax like this:

    =INDIRECT(ref_text,[a1])

_Ref\_text_ is the text string to evaluate as a reference. The second argument, _a1_, is optional and indicates the "style" of the reference provided. When _a1_ is omitted (or TRUE), INDIRECT evaluates _ref\_text_ as an "A1" style reference. When a1 is FALSE, INDIRECT evaluates _ref\_text_ as an "R1C1" style reference. For example:

    =INDIRECT("A1") // returns a reference to A1
    =INDIRECT("C5") // returns a reference to C5
    =INDIRECT("R1C1",FALSE) // returns a reference to A1
    =INDIRECT("R5C3",FALSE) // returns a reference to C5
    

_Note: the a1 argument only changes the way INDIRECT evaluates ref\_text, not the result._

### Things to know about INDIRECT

Here are some things you should know about the INDIRECT function:

*   The input to INDIRECT is _text_. You can create this text any way you like.
*   INDIRECT will evaluate the text and convert it into a _valid reference_.
*   If INDIRECT can't understand the text as a reference, it will return a #REF error.
*   INDIRECT can cause performance problems in large or complex worksheets. Use with care.

Here are a few ways you can use the INDIRECT function in a formula:

*   Create a formula that uses a sheet name entered in a cell.
*   Create a lookup formula with a variable lookup table.
*   A formula that can assemble a cell reference from bits of text
*   Create a fixed reference that will not change even when rows or columns are deleted
*   Create numeric arrays with the ROW function in older versions of Excel.

### Example 1 - the basic idea of INDIRECT

The worksheet below shows the basic idea of the INDIRECT function. The text entered in column E represents different ranges. However, if we try to use the text directly in the SUM function as a range, SUM returns zero:

![INDIRECT function example - the basic idea (before)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/indirect_function_example_-_the_basic_idea1.png "INDIRECT function example - the basic idea (before)")

This happens because SUM doesn't see the text value as a reference; it simply sees a text string:

    =SUM(E6)
    =SUM("C5:C6")
    =0

The solution is to add the INDIRECT function, which converts the text values into actual ranges:

![INDIRECT function example - the basic idea (after)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/indirect_function_example_-_the_basic_idea2.png "INDIRECT function example - the basic idea (after)")

Notice in the second line below, we still have a text value, but in the third line we have the range C5:C6, and SUM now returns 9:

    =SUM(INDIRECT(E6))
    =SUM(INDIRECT("C5:C6"))
    =SUM(C5:C6)
    =9

### Example 2 - Variable worksheet name

In the example shown below, INDIRECT is set up to use a variable sheet name. The formula in cell C5 is:

    =INDIRECT(B5&"!A1") // sheet name in B5 is variable
    

The formula in C5 concatenates the text in B5 to the string "!A1" and returns the result to INDIRECT. The INDIRECT function then evaluates the text and converts it to a valid reference. As the formula is copied down, it returns the value in cell A1 for each of the 5 sheets listed in column B.

![INDIRECT function example - variable worksheet name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/indirect_function_example_-_variable_worksheet_name.png "INDIRECT function example - variable worksheet name")

The formula is dynamic and responds to the sheet names in column B. If the sheet names are changed, the formula will automatically recalculate.

> Note: As explained in [this example](https://exceljet.net/formulas/dynamic-worksheet-reference)
> , sheet names that contain punctuation or spaces must be enclosed in single quotes ('). This is not specific to the INDIRECT function; the same limitation is true in all formulas. The modified formula is below.

If the sheet names in your worksheet include spaces or punctuation, use the formula below:

    =INDIRECT("'"&B5&"'!A1") // single quotes added

### Example 3 - INDIRECT with a dropdown list

Using the same approach explained in the example above, we can allow a user to _select a sheet name_ from a [dropdown list](https://exceljet.net/articles/dependent-dropdown-lists)
 and then construct a reference to cell A1 on the selected sheet with INDIRECT. The formula in cell C5 is the same:

    =INDIRECT(B5&"!A1") // sheet name from dropdown
    

![INDIRECT with a dropdown list to select sheet name](https://exceljet.net/sites/default/files/images/functions/inline/indirect_function_with_dropdown_list.png "INDIRECT with a dropdown list to select sheet name")

When a different sheet name is selected, the formula will recalculate. First, the sheet name in cell B5 will be concatenated to the text "!A1" to produce a text string like "August!A1". Next, INDIRECT will convert the text into a regular reference like `=August!A1`. Note that cell A1 is used only as an example. You can change the cell reference as desired.

### Example 4 - Variable lookup table

In the worksheet below, VLOOKUP is used to get costs for two vendors, A and B. Using the vendor indicated in column F, VLOOKUP _automatically_ uses the correct table:

![Example of INDIRECT for VLOOKUP with variable table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/VLOOKUP%20with%20variable%20table%20array.png?itok=BpLPyEoN "Example of INDIRECT for VLOOKUP with variable table")

The formula in G5 is:

    =VLOOKUP(E5,INDIRECT("vendor_"&F5),2,0)
    

Read a [full explanation here](https://exceljet.net/formulas/vlookup-with-variable-table-array)
.

### Example 5 - Fixed reference

Normally, a reference like A1:A100 will change if rows or columns are deleted. For example, if a row is deleted in this range, the reference will become A1:A99. To create a reference that will not change, you can use the INDIRECT function like this:

    =INDIRECT("A1:A100") // fixed reference
    

Because the text value is static, the reference created by INDIRECT will not change even when cells, rows, or columns are inserted or deleted. The formula below will always refer to the first 100 rows of column A.

### Example 6 - named range

The INDIRECT function can easily be used with named ranges. The worksheet below contains two [named ranges](https://exceljet.net/glossary/named-range)
: _Group1_ (B5:B12) and _Group2_ (C5:C12). When "Group1" or "Group2" is entered in cell F5, the formula in cell F6 sums the appropriate range using INDIRECT like this:

    =SUM(INDIRECT(F5))
    

The value in F5 is text, but INDIRECT converts the text into a valid range.

![Example of INDIRECT function with a named range](https://exceljet.net/sites/default/files/images/functions/inline/indirect%20function%20with%20named%20range.png "Example of INDIRECT function with a named range")

A specific example of this approach is [using named ranges to make dependent dropdown lists](https://exceljet.net/articles/dependent-dropdown-lists)
.

### Example 7 - Generate a numeric array

A more advanced use of INDIRECT is to create a numeric [array](https://exceljet.net/glossary/array)
 with the [ROW function,](https://exceljet.net/functions/row-function)
 like this:

    ROW(INDIRECT("1:10")) // create {1;2;3;4;5;6;7;8;9;10}
    

One use case is explained in [this formula](https://exceljet.net/formulas/sum-bottom-n-values)
, which sums the bottom n values in a range. You may also run into the ROW + INDIRECT approach in more complex formulas that need to assemble a numeric array "on the fly". One example is this formula, designed to [strip numeric characters from a string](https://exceljet.net/formulas/strip-numeric-characters-from-cell)
.

> Note: this approach only makes sense in older versions of Excel. In the current version of Excel, you can easily create a numeric sequence with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
> .

### Troubleshooting INDIRECT

Working with the INDIRECT function can be tricky because you can't actually see the reference it returns. Instead, you just see the value at the reference when it works, or an error if the reference is invalid. Here are some troubleshooting tips:

*   Be sure you have a good understanding of [How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
    . Many INDIRECT problems are caused by text values that can't be coerced into a valid reference.
*   Be sure to include single quotes when referencing sheet names that contain spaces or punctuation (i.e., `'Sheet 1'!A1`).
*   Debug the text string being delivered to INDIRECT [with the F9 key](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
     to confirm it meets expectations.
*   Work in small steps to make sure INDIRECT is returning the reference you expect before plugging it into a more complex formula.

### Notes

*   References created by INDIRECT are evaluated in real-time, and the value at the reference is returned.
*   When _ref\_text_ is an external reference to another workbook, the workbook must be open.
*   When _a1_ is TRUE (the default value), INDIRECT evaluates _ref\_text_ as an "A1" style reference.
*   When a1 is FALSE, INDIRECT evaluates _ref\_text_ as an "R1C1" style reference.
*   INDIRECT is a [volatile function](https://exceljet.net/glossary/volatile-function)
     and can cause performance issues in large or complex worksheets.

INDIRECT function examples
--------------------------

[![Excel formula: Formula with locked absolute reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/formula%20with%20locked%20absolute%20reference.png "Excel formula: Formula with locked absolute reference")](https://exceljet.net/formulas/formula-with-locked-absolute-reference)

### [Formula with locked absolute reference](https://exceljet.net/formulas/formula-with-locked-absolute-reference)

In this example, the goal is to create an "locked" reference that won't change when columns or rows are added or deleted in a worksheet, or during a copy / paste / cut operation. The INDIRECT function accepts text, and evaluates that text as a reference. As a result, the text is not susceptible to...

[![Excel formula: Indirect named range different sheet](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Indirect%20named%20range%20different%20sheet.png "Excel formula: Indirect named range different sheet")](https://exceljet.net/formulas/indirect-named-range-different-sheet)

### [Indirect named range different sheet](https://exceljet.net/formulas/indirect-named-range-different-sheet)

The formula above evaluates something like this: =SUM(INDIRECT("'"...

[![Excel formula: Dynamic reference to table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20reference%20table%20name.png "Excel formula: Dynamic reference to table")](https://exceljet.net/formulas/dynamic-reference-to-table)

### [Dynamic reference to table](https://exceljet.net/formulas/dynamic-reference-to-table)

In this example, the goal is to create a dynamic reference to an Excel Table in a formula. In other words, create a formula that can refer to an Excel table by name as a variable. The easiest way to do this in Excel is to assemble the reference as a text value using concatenation , then use the...

[![Excel formula: Increment cell reference with INDIRECT](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/increment%20cell%20reference%20with%20INDIRECT.png "Excel formula: Increment cell reference with INDIRECT")](https://exceljet.net/formulas/increment-cell-reference-with-indirect)

### [Increment cell reference with INDIRECT](https://exceljet.net/formulas/increment-cell-reference-with-indirect)

Consider a simple dynamic reference to Sheet2 using the INDIRECT in a formula like this: =INDIRECT($B$5&"!"&"A1") If we change the sheet name in B5 to another (valid) name, INDIRECT will return a reference to A1 in the new sheet. However, if we copy this formula down the column, the...

[![Excel formula: Data validation specific characters only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Data%20validation%20specific%20characters%20only.png "Excel formula: Data validation specific characters only")](https://exceljet.net/formulas/data-validation-specific-characters-only)

### [Data validation specific characters only](https://exceljet.net/formulas/data-validation-specific-characters-only)

Working from the inside out, the MID function is used to generate an array from text entered in B5 with this snippet: MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1) explained in detail here . The result is an array like this: {"A";"A";"A";"-";"1";"1";"1"} which goes into MATCH as the lookup value. For...

[![Excel formula: Search multiple worksheets for value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/search%20multiple%20worksheets%20for%20value.png "Excel formula: Search multiple worksheets for value")](https://exceljet.net/formulas/search-multiple-worksheets-for-value)

### [Search multiple worksheets for value](https://exceljet.net/formulas/search-multiple-worksheets-for-value)

The range B7:B9 contains the sheet names we want to include in the search. These are just text strings, and we need to do some work to get them to be recognized as valid sheet references. Working from the inside out, this expression is used to build a full sheet reference: "'"...

[![Excel formula: Lookup with variable sheet name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup_with_variable_sheet_name.png "Excel formula: Lookup with variable sheet name")](https://exceljet.net/formulas/lookup-with-variable-sheet-name)

### [Lookup with variable sheet name](https://exceljet.net/formulas/lookup-with-variable-sheet-name)

In this example, the goal is to create a lookup formula with a variable sheet name. In other words, a formula that uses a sheet name typed into a cell to construct a reference to a range on that sheet. If the sheet name is changed, the reference should update automatically. The key to the solution...

[![Excel formula: Count day of week between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20day%20of%20week%20between%20dates.png "Excel formula: Count day of week between dates")](https://exceljet.net/formulas/count-day-of-week-between-dates)

### [Count day of week between dates](https://exceljet.net/formulas/count-day-of-week-between-dates)

At the core, this formula uses the WEEKDAY function to test a number of dates to see if they land on a given day of week (dow) and the SUMPRODUCT function to tally up the total. When given a date, WEEKDAY simply returns a number between 1 and 7 that corresponds to a particular day of the week. With...

[![Excel formula: Reverse text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/reverse%20text%20string.png "Excel formula: Reverse text string")](https://exceljet.net/formulas/reverse-text-string)

### [Reverse text string](https://exceljet.net/formulas/reverse-text-string)

At the core, this formula uses the MID function to extract each character of a text string in reverse order. The starting character is given as a list of numbers in descending order hard-coded as array constant: MID(B5,{10,9,8,7,6,5,4,3,2,1},1) The text argument comes B5, and 1 is specified for the...

[![Excel formula: COUNTIFS with variable table column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/COUNTIFS%20with%20variable%20table%20column.png "Excel formula: COUNTIFS with variable table column")](https://exceljet.net/formulas/countifs-with-variable-table-column)

### [COUNTIFS with variable table column](https://exceljet.net/formulas/countifs-with-variable-table-column)

First, for context, it's important to note that you can use COUNTIFS with a regular structured reference like this: =COUNTIFS(Table1\[Swim\],"x") This is a much simpler formula, but you can't copy it down column H, because the column reference won't change. The example on this page therefore is meant...

[![Excel formula: Count errors in all sheets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_errors_in_all_sheets.png "Excel formula: Count errors in all sheets")](https://exceljet.net/formulas/count-errors-in-all-sheets)

### [Count errors in all sheets](https://exceljet.net/formulas/count-errors-in-all-sheets)

In this example, the goal is to count errors in a workbook by sheet, where the sheet names have been previously entered in a column as shown. This is a tricky problem in Excel for a couple of reasons. First, there is no direct way to generate a list of sheets in a workbook with a formula. Second,...

[![Excel formula: Sum bottom n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20bottom%20n%20values.png "Excel formula: Sum bottom n values")](https://exceljet.net/formulas/sum-bottom-n-values)

### [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)

In this example, the goal is to sum the smallest n values in a set of data, where n is a variable that can be easily changed. At a high level, the solution breaks down into two steps (1) extract the n smallest values from the data set and (2) sum the extracted values. This problem can be solved...

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Worksheet name exists](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/worksheet%20name%20exists.png "Excel formula: Worksheet name exists")](https://exceljet.net/formulas/worksheet-name-exists)

### [Worksheet name exists](https://exceljet.net/formulas/worksheet-name-exists)

The ISREF function returns TRUE for a valid worksheet reference and FALSE is not. In this case, we want to find out of a particular sheet exists in a workbook, so we construct a full reference by concatenating the sheet names in column B with an exclamation mark and "A1": B5...

[![Excel formula: Create array of numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20array%20of%20numbers.png "Excel formula: Create array of numbers")](https://exceljet.net/formulas/create-array-of-numbers)

### [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)

Note: In Excel 365 , the new SEQUENCE function is a better and easier way to create an array of numbers. The method explained below will work in previous versions. The core of this formula is a string that represents rows. For example, to create an array with 10 numbers, you can hard-code a string...

INDIRECT function videos
------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Create%20a%20dynamic%20reference%20to%20a%20worksheet-thumb.png)](https://exceljet.net/videos/create-a-dynamic-reference-to-a-worksheet)

### [Create a dynamic reference to a worksheet](https://exceljet.net/videos/create-a-dynamic-reference-to-a-worksheet)

In this video we'll look at how to create a dynamic reference to a worksheet in a formula. Sometimes you want to reference a worksheet dynamically in a formula, so it can be easily changed. In this workbook we have five weeks of test scores, each in the same format. Let's assume we want to build a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Create%20a%20dynamic%20reference%20to%20a%20named%20range-thumb.png)](https://exceljet.net/videos/create-a-dynamic-reference-to-a-named-range)

### [Create a dynamic reference to a named range](https://exceljet.net/videos/create-a-dynamic-reference-to-a-named-range)

In this video we'll look at how to create a dynamic reference to a named range using the INDIRECT function . Let's take a look. Here we have a simple table that summarizes sales by salesperson over a four-month period. What we're going to do is use the INDIRECT function to make a dynamic reference...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20find%20and%20highlight%20formulas-thumb.png)](https://exceljet.net/videos/how-to-find-and-highlight-formulas)

### [How to find and highlight formulas](https://exceljet.net/videos/how-to-find-and-highlight-formulas)

In this video, we're going to look at three ways to find formulas in a worksheet. Knowing where formulas are is the first step in understanding how a spreadsheet works. When you first open a worksheet you didn't create yourself, it may not be clear exactly where the formulas are. Of course, you can...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Data validation specific characters only](https://exceljet.net/formulas/data-validation-specific-characters-only)
    
*   [Worksheet name exists](https://exceljet.net/formulas/worksheet-name-exists)
    
*   [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)
    
*   [Formula with locked absolute reference](https://exceljet.net/formulas/formula-with-locked-absolute-reference)
    
*   [Convert column letter to number](https://exceljet.net/formulas/convert-column-letter-to-number)
    
*   [Increment cell reference with INDIRECT](https://exceljet.net/formulas/increment-cell-reference-with-indirect)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    
*   [Indirect named range different sheet](https://exceljet.net/formulas/indirect-named-range-different-sheet)
    
*   [Count numbers in text string](https://exceljet.net/formulas/count-numbers-in-text-string)
    

### Videos

*   [Create a dynamic reference to a named range](https://exceljet.net/videos/create-a-dynamic-reference-to-a-named-range)
    
*   [Create a dynamic reference to a worksheet](https://exceljet.net/videos/create-a-dynamic-reference-to-a-worksheet)
    
*   [How to find and highlight formulas](https://exceljet.net/videos/how-to-find-and-highlight-formulas)
    

### Links

*   [Microsoft INDIRECT function documentation](https://support.office.com/en-us/article/indirect-function-474b3a3a-8a26-4f44-b491-92b6306fa261)
    

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