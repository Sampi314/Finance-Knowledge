# Excel Formula Errors | Exceljet

**Source:** https://exceljet.net/articles/excel-formula-errors

---

[Skip to main content](https://exceljet.net/articles/excel-formula-errors#main-content)

[](https://exceljet.net/articles/excel-formula-errors#)

*   [Previous](https://exceljet.net/articles/excel-pivot-tables)
    
*   [Next](https://exceljet.net/articles/how-to-lookup-first-and-last-match)
    

Excel Formula Errors
====================

by Dave Bruns · Updated 29 Mar 2024

![Excel Formula Errors](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/Excel_functions_you_should_know_0.jpeg "Excel Formula Errors")

Summary
-------

Formula errors are useful because they tell you clearly that something is wrong in a worksheet. This guide shows examples of each of the Excel formula errors you might run into and provides information on how to investigate and correct the error. It also explains two methods to quickly find errors in a worksheet or workbook.

Formulas are the heart of Excel. They can do everything from basic math to complex data analysis. But sometimes, they don't work as expected. If you work in Excel a lot, you've probably seen many formula errors like #DIV/0, #NAME?, and #N/A. In fact, the more you work with formulas, the more errors you'll run into :)

Although formulas errors can be scary and frustrating, they are quite useful, because they tell you something is wrong. This is much better than _not knowing_. The most disastrous Excel problems come from _normal-looking_ worksheets that quietly return _incorrect_ results. Trust me, this is not the kind of problem you want to explain to your boss in a meeting.

Most formula errors are the result of small mistakes, like a typo, the wrong cell reference, or deleting a cell referred to by another formula. When you run into a formula error, don't panic. Stay calm and methodically investigate until you find the cause. Ask yourself, "What is this error telling me?" Experiment with trial and error. As you gain more experience, you'll be able to avoid many errors, and more quickly correct errors that do arise.

### Table of contents

*   [About Excel Formula Errors](https://exceljet.net/articles/excel-formula-errors#about_formula_errors)
    *   [#DIV/0! Error](https://exceljet.net/articles/excel-formula-errors#div_error)
        
    *   [#NAME? Error](https://exceljet.net/articles/excel-formula-errors#name_error)
        
    *   [#N/A Error](https://exceljet.net/articles/excel-formula-errors#na_error)
        
    *   [#NUM! Error](https://exceljet.net/articles/excel-formula-errors#num_error)
        
    *   [#VALUE! Error](https://exceljet.net/articles/excel-formula-errors#value_error)
        
    *   [#REF! Error](https://exceljet.net/articles/excel-formula-errors#ref_error)
        
    *   [#NULL! Error](https://exceljet.net/articles/excel-formula-errors#null_error)
        
    *   [\#### Error](https://exceljet.net/articles/excel-formula-errors#hashtag_error)
        
    *   [#SPILL! Error](https://exceljet.net/articles/excel-formula-errors#spill_error)
        
    *   [#CALC! Error](https://exceljet.net/articles/excel-formula-errors#calc_error)
        
    *   [#BLOCKED! Error](https://exceljet.net/articles/excel-formula-errors#blocked_error)
        
    *   [Circular Reference Errors](https://exceljet.net/articles/excel-formula-errors#circular_reference_errors)
        
*   [How to find formula errors](https://exceljet.net/articles/excel-formula-errors#how_to_find_formula%20errors)
    
*   [How to fix formula errors](https://exceljet.net/articles/excel-formula-errors#how_to_fix_formula%20errors)
    
*   [How to trap errors](https://exceljet.net/articles/excel-formula-errors#how_to_trap_errors)
    
*   [Error-related Functions in Excel](https://exceljet.net/articles/excel-formula-errors#error_related_functions)
    

### About Excel formula errors

There are 10 different formula errors you are likely to run into at some point as you work with Excel formulas. This section shows examples of each formula error, with information and links on how to correct the error.

### #DIV/0! error

As the name suggests, the #DIV/0! error appears when a formula tries to divide by zero, or by a value equivalent to zero. You may see a #DIV/0! error when data is not yet complete. For example, a cell in the worksheet is blank because data has not been entered, or is not yet available. You also may see the divide by zero error with the [AVERAGEIF](https://exceljet.net/functions/averageif-function)
 and [AVERAGEIFS](https://exceljet.net/functions/averageifs-function)
 functions, when given criteria do not match any cells in the range. For example, in the worksheet below, the DIV error is displayed in cell D4 because C4 is empty. Empty cells are evaluated as zero by Excel, and B4 can't be divided by zero:

![Excel #DIV/0!  error example](https://exceljet.net/sites/default/files/images/articles/inline/Excel%20DIV%20error%20example.png "Excel #DIV/0!  error example")

In many cases, empty cells or missing values are unavoidable. You can use the [IFERROR function](https://exceljet.net/functions/iferror-function)
 to trap the #DIV/0! and display a more friendly message if you like.

More: [How to fix the #DIV/0! error](https://exceljet.net/formulas/how-to-fix-the-div0-error)

### #NAME? error

The #NAME? error indicates that Excel does not recognize something. This could be a function name misspelled, a [named range](https://exceljet.net/glossary/named-range)
 that doesn't exist, or a cell reference entered incorrectly. For example, in the screen below, the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 in F3 is misspelled "VLOKUP". VLOKUP is not a valid name, so the formula returns #NAME?.

![Excel #NAME? error example](https://exceljet.net/sites/default/files/images/articles/inline/Excel%20NAME%20error%20example.png "Excel #NAME? error example")

To fix a #NAME? error, you must find the problem, and then correct spelling or syntax. For more details and examples, [see this page](https://exceljet.net/formulas/how-to-fix-the-name-error)
.

> Video: [How to use F9 to debug a formula error](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

### #N/A error

The #N/A error appears when something can't be found. It tells you something is missing or misspelled. This could be a product code not yet available, an employee name misspelled, a color that doesn't exist, etc. Often, #N/A errors are caused by extra space characters, misspellings, or an incomplete lookup table. The functions most commonly affected by the #N/A error are classic lookup functions, including VLOOKUP, HLOOKUP, LOOKUP, and MATCH. For example, in the screen below, the formula in F3 returns #N/A because "Bacon" is not in the lookup table:

![Excel #N/A error example](https://exceljet.net/sites/default/files/images/articles/inline/Excel%20NA%20error%20example.png "Excel #N/A error example")

_If the value in E3 is changed to an existing value like "Coffee", "Eggs", etc. VLOOKUP will work normally and retrieve the item cost._

The best way to prevent #N/A errors is to make sure lookup values and lookup tables are correct and complete. If necessary, you can trap the #N/A error with IFERROR or IFNA and display a more friendly message, or display nothing at all. '

More information: [How to fix the #N/A error.](https://exceljet.net/formulas/how-to-fix-the-na-error)

### #NUM! error

The #NUM! error occurs when a number is too large or small, or when a calculation is impossible. For example, if you try to calculate the square root of a negative number, you'll see a #NUM error:

![Excel #NUM! error example](https://exceljet.net/sites/default/files/images/articles/inline/Excel%20NUM%20error%20example.png "Excel #NUM! error example")

_In the screen above the SQRT function is used to calculate the square root numbers in column B. The formula in C5 returns the #NUM! error because the value in B5 is negative, and it is not possible to compute the square root of a negative number._

You might also run into the #NUM error if you reverse start and end dates inside the [DATEDIF function](https://exceljet.net/functions/datedif-function)
. In general, fixing the #NUM! error is a matter of adjusting inputs as required to make a calculation possible again.

More information: [How to fix the #NUM! error](https://exceljet.net/formulas/how-to-fix-the-num-error)
.

> Video: [Examples of Excel formula errors](https://exceljet.net/videos/examples-of-flagged-errors-in-formulas)

### #VALUE! error

The #VALUE! error appears when a value is not an expected or valid type (i.e. date, time, number, text, etc.) This can happen when a cell is left blank, when a text value is given to a function that expects a numeric value, or when dates are evaluated as text by Excel. For example, in the screen below, cell C3 contains the text "NA", and the formula in F2 returns the #VALUE! error.

![Excel #VALUE! error example](https://exceljet.net/sites/default/files/images/articles/inline/Excel%20VALUE%20error%20example.png "Excel #VALUE! error example")

Below, the [MONTH function](https://exceljet.net/functions/month-function)
 can't extract a month value from "apple", since "apple" is not a date:

![Excel #VALUE! error example with MONTH function](https://exceljet.net/sites/default/files/images/articles/inline/Excel%20VALUE%20error%20example%202.png "Excel #VALUE! error example with MONTH function")

Note: you may also see a #VALUE! error if you create an [array formula](https://exceljet.net/glossary/array-formula)
 and forget to enter the formula with Control + Shift + Enter.

To fix a #VALUE! error, you need to track down the problematic value and supply the right type of value. For more details and examples, [see this page](https://exceljet.net/formulas/how-to-fix-the-value-error)
.

### #REF! error

The #REF! error is one of the most common errors you'll see in Excel formulas. It occurs when a reference becomes invalid. In many cases, this is because sheets, rows, or columns have been removed, or because a formula with relative references has been copied to a new location where references are invalid. For example, in the screen below, the formula in C8 was copied to E4. At this new location, since the range C3:C7 is relative, it becomes invalid and the formula returns #REF!:

![Excel #REF error example](https://exceljet.net/sites/default/files/images/articles/inline/Excel%20REF%20error%20example.png "Excel #REF error example")

#REF! errors can be somewhat tricky to fix because the original cell reference is gone forever. If you delete a row or column and then see #REF! errors, you should undo the action immediately and adjust the formulas first.

[More details on #REF! errors.](https://exceljet.net/formulas/how-to-fix-the-ref-error)

### #NULL! error

The #NULL! error is quite rare in Excel, and is usually the result of a typo where a space character is used instead of a comma (,) or colon (:) between two cell references. For example, in the screen below the formula in F3 returns the #NULL error:

![Excel #NULL! error example](https://exceljet.net/sites/default/files/images/articles/inline/Excel%20NULL%20error%20example.png "Excel #NULL! error example")

Technically, this is because the space character is the "range intersect" [operator](https://exceljet.net/glossary/math-operators)
 and the #NULL! error is reporting that the two ranges (C3 and C7) do not intersect. In most cases, you can correct a NULL error by replacing a space with a comma or colon as needed.

More: [How to fix the #NULL! error](https://exceljet.net/formulas/how-to-fix-the-null-error)

### \#### error

Although technically not an error, you may also see a formula that displays a string of hash characters (###) instead of a normal result. For example, in the screen below, the formula in C3 is adding 5 days to the date in column B:

![Excel ##### error example](https://exceljet.net/sites/default/files/images/articles/inline/Excel%20hashtag%20error%20example.png "Excel ##### error example")

In this case, the hash or pound characters (###) appear because the dates in column C are formatted with a long format and do not fit into the column. To fix this error, just make the column wider.

_Note: Excel won't display negative dates. If a formula returns a negative date value, Excel will display #####._

More: [How to fix ##### errors](https://exceljet.net/formulas/how-to-fix-the-hashtag-error)

### #SPILL! error

The #SPILL error occurs when a formula outputs a [spill range](https://exceljet.net/glossary/spill-range)
 that runs into a cell that already contains data. For example, in the screen below, the [UNIQUE function](https://exceljet.net/functions/unique-function)
 is configured to extract a list of unique names into a spill range starting in D3. Because D5 contains "apple", the operation is stopped and the formula returns #SPILL!

![Excel #SPILL error example](https://exceljet.net/sites/default/files/images/articles/inline/Excel%20SPILL%20error%20example.png "Excel #SPILL error example")

When "apple" is deleted from D5, the formula will work normally, and return "Joe", "Sam", and "Mary".

Details: [How to fix #SPILL errors](https://exceljet.net/formulas/how-to-fix-the-spill-error)

Video: [Spilling and the spill range](https://exceljet.net/videos/spilling-and-the-spill-range)

### #CALC! error

The #CALC error occurs when a formula runs into a calculation error with an array. For example, in the screen below, the FILTER function is set up to filter the source data in B5:D11. However, the formula is asking for all data in the group "apple", which doesn't exist:

![Excel #CALC error example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/filter%20with%20calc%20error.png?itok=5z-txdJa "Excel #CALC error example")

If the formula is adjusted to filter on group "A", the formula will work normally:

    =FILTER(B5:D11,B5:B11="a")
    

> #SPILL! and #CALC! errors are related to "[Dynamic Arrays"](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  in Excel 365 and Excel 2021 only.

### #BLOCKED! error

The #BLOCKED! error in Excel occurs when certain resources or functions are restricted. The error can occur when a required resource cannot be accessed or by issues such as Excel 4.0 (XLM) macros being disabled. For example, in the worksheet below, the defined name "sheetnames" is based on an older Excel 4.0 macro command called GET.WORKBOOK ([details here](https://exceljet.net/formulas/list-sheet-names-with-formula)
). Because Excel 4.0 macros are disabled in the Trust Centered, Excel returns the #BLOCKED error.

![Excel #CALC error example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/Excel_BLOCKED_error_example.png "Excel #CALC error example")

To resolve this error in this particular case, Excel 4.0 macros must be enabled in the Trust Center and the file must be reopened. For a more complete explanation see [List sheet names with a formula](https://exceljet.net/formulas/list-sheet-names-with-formula)
.

### Circular reference errors

A circular reference occurs when a formula refers directly to its own cell, or refers to another cell that depends on the original cell. This creates an infinite loop that cannot be resolved. For example, if cell A1 contains a formula that refers to B1, and B1 contains a formula that refers to A1, this creates a circular reference. Circular reference errors do not appear on the worksheet like other errors in Excel. To find circular references, navigate to Formulas > Error checking > Circular references. For more details see [How to fix a circular reference error](https://exceljet.net/formulas/how-to-fix-a-circular-reference-error)
.

### How to find formula errors

There are three basic ways to find formula errors in Excel. The first way is simple observation. Because formula errors are displayed directly on the worksheet they are easy to spot in many worksheets. In larger worksheets or workbooks with many sheets, you can check for errors much faster with Excel's built-in tools. To select all errors on a given worksheet, you can use **Go To Special**. To generate a list of all errors in the entire workbook, you can use **Find and Replace**. Both options are explained below.

### Find errors with Go To Special

You can find all errors at once with Go To Special. Use the [keyboard shortcut](https://exceljet.net/shortcuts)
 Control + G, then click the "Special" button. Excel will display the dialog with the options seen below. To select only errors, choose Formulas + Errors, then click "OK":

![Excel Go To Special Formula Errors](https://exceljet.net/sites/default/files/images/articles/inline/go%20to%20special%20formula%20errors.png "Excel Go To Special Formula Errors")

After you press OK, Excel will select all errors on the current worksheet. Once selected, you can use the Tab key to move through the selection one cell at a time. If no errors are present, Excel will return the message "No cells were found".

_Note: Go To Special will only find errors on the current worksheet. To find all errors in a workbook, see the next section below._

### Find errors with Find and Replace

To find all errors in a workbook across multiple sheets, you can use Find and Replace:

1.  Open the Find and Replace dialog with the [keyboard shortcut](https://exceljet.net/shortcuts)
     Control + F.
2.  In the "Find what" input area, input the characters "#\*!" (without quotation marks).
3.  Next, select "Workbook" for "Within", and change "Look in" to "Values".
4.  Click the "Find All" button.
5.  Excel will display a list of matching errors in the workbook as seen below.

![Find all errors with Find and Replace](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/excel_formula_errors_find_errors_with_find_and_replace.png "Find all errors with Find and Replace")

The asterisk (\*) is a [wildcard](https://exceljet.net/glossary/wildcard)
 in Excel that will match any number of characters, so the idea here is to find values that start with a hash (#) and end with an exclamation point (!). Notice the list of errors contains multiple sheets. To navigate to each error, use the "Find Next" button or click a row in the list.

_Notes: (1) The search string "#\*!" will not find a #N/A error, which does not end with an exclamation point (!). To find #N/A errors, use a more general search string like "#\*" or a more specific string like "#N/A". (2) You can also enter individual errors directly. For example, you can enter "#N/A", "#DIV/0!", #REF!", etc. to find specific errors._

> It is also possible to [count errors in a workbook by sheet](https://exceljet.net/formulas/count-errors-in-all-sheets)
>  with a formula.

### How to fix formula errors

The basic process for fixing formula errors looks like this:

1.  Find the errors (see above).
2.  Identify each error and understand its meaning.
3.  Trace the error back to its source. If this is difficult, try the [trace error feature](https://exceljet.net/videos/how-to-trace-a-formula-error)
    .
4.  Figure out what's causing the error. If needed, break the formula into parts.
5.  Fix the error at the source or trap the error.

Remember that formula errors often "cascade" through a worksheet, when one error triggers another. As you find and fix the core issue(s), things often come together quickly.

Video: [Excel formula error examples](https://exceljet.net/videos/examples-of-flagged-errors-in-formulas)

Video: [Use F9 to debug a formula](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

### How to trap Errors

Trapping errors is a way of "catching" errors to stop them from appearing in the first place. This makes sense when you know certain errors are likely and you want to stop the errors from appearing on the worksheet. There are two basic approaches:

1.  Trap the error with [IFERROR](https://exceljet.net/functions/iferror-function)
     or [ISERROR](https://exceljet.net/functions/iserror-function)
    . With this approach, you are watching for an error, and providing an alternative value when an error is detected. [This page shows a VLOOKUP example](https://exceljet.net/formulas/vlookup-without-na-error)
    .
2.  Prevent calculation until required values are available. In this case, instead of watching for an error, you try to prevent the error from occurring by checking values first. [This page shows several examples](https://exceljet.net/formulas/only-calculate-if-not-blank)
    .

### Error-related functions in Excel

Excel provides several error-related functions, each with a different behavior. Click on the links below for more details:

*   The [ISERR function](https://exceljet.net/functions/iserr-function)
     returns TRUE for any error type except the #N/A error.
*   The [ISERROR function](https://exceljet.net/functions/iserror-function)
     returns TRUE for any error.
*   The [ISNA function](https://exceljet.net/functions/isna-function)
     returns TRUE for #N/A errors only.
*   The [ERROR.TYPE function](https://exceljet.net/functions/errortype-function)
     returns the numeric code for a given error.
*   The [IFERROR function](https://exceljet.net/functions/iferror-function)
     traps errors and provides an alternative result.
*   The [IFNA function](https://exceljet.net/functions/ifna-function)
     traps #N/A errors only and provides an alternative result.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

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