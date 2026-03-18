# Excel LAMBDA function | Exceljet

**Source:** https://exceljet.net/functions/lambda-function

---

[Skip to main content](https://exceljet.net/functions/lambda-function#main-content)

[](https://exceljet.net/functions/lambda-function#)

*   [Previous](https://exceljet.net/functions/isomitted-function)
    
*   [Next](https://exceljet.net/functions/let-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

LAMBDA Function
===============

by Dave Bruns · Updated 19 Dec 2025

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LET](https://exceljet.net/functions/let-function)

[ISOMITTED](https://exceljet.net/functions/isomitted-function)

[MAP](https://exceljet.net/functions/map-function)

[SCAN](https://exceljet.net/functions/scan-function)

[REDUCE](https://exceljet.net/functions/reduce-function)

[MAKEARRAY](https://exceljet.net/functions/makearray-function)

[BYCOL](https://exceljet.net/functions/bycol-function)

[BYROW](https://exceljet.net/functions/byrow-function)

![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")

Summary
-------

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

Purpose 
--------

Create custom function

Return value 
-------------

As defined by formula

Syntax
------

    =LAMBDA(parameter,...,calculation)

*   _parameter_ - An input value for the function.
*   _calculation_ - The calculation to perform as the result of the function. Must be the last argument.

Using the LAMBDA function 
--------------------------

The LAMBDA function provides a way to create a custom function in Excel. Once defined and named, a LAMBDA function can be used anywhere in a workbook. LAMBDA functions can be very simple or quite complex, stringing together many Excel functions into one formula. A custom LAMBDA function does not require VBA or macros.

> LAMBDA is a new function available in [Excel 365](https://exceljet.net/glossary/excel-365)
>  only.

[Example 1](https://exceljet.net/functions/lambda-function#example1)
 | [Example 2](https://exceljet.net/functions/lambda-function#example2)
 | [Example 3](https://exceljet.net/functions/lambda-function#example3)
 | [Example 4](https://exceljet.net/functions/lambda-function#example4)

In computer programming, the term "lambda" refers to an anonymous function or expression. An anonymous function is a function defined without a name. In Excel, the LAMBDA function is first used to create a generic (unnamed) formula. Once a generic version has been created and tested, it is ported to the Name Manager, where it is formally defined and named.

One of the key benefits of a custom LAMBDA function is that the logic contained in the formula exists in just one place. This means there is just one copy of code to update when fixing problems or updating functionality, and changes will automatically propagate to all instances of the LAMBDA function in a workbook.

The [LET function](https://exceljet.net/functions/let-function)
 is often used together with the LAMBDA function. LET provides a way to declare variables and assign values in a formula. This makes more complicated formulas easier to read by reducing redundant code. The LET function can also improve performance by reducing the number of calculations performed by a formula.

By default, all arguments in a LAMBDA function are required. To create _optional_ arguments, see the [ISOMITTED function](https://exceljet.net/functions/isomitted-function)
.

### Creating a LAMBDA function

LAMBDA functions are typically created and debugged in the formula bar on a worksheet, then moved into the name manager to assign a name that can be used anywhere in a workbook.

There are four basic steps to creating and using a custom LAMBDA function:

1.  Verify the logic you will use with a standard formula
2.  Create and test a generic (unnamed) LAMBDA version of the formula
3.  Name and define the LAMBDA formula with the name manager
4.  Call the new custom function with the defined name

The examples below discuss these steps in more detail.

### Example 1 - basic example

To illustrate how LAMBDA works, let's begin with a very simple formula:

    =x*y // multiply x and y
    

In Excel, this formula would typically use cell references like this:

    =B5*C5 // with cell references
    

![Standard formula version](https://exceljet.net/sites/default/files/images/functions/inline/lambda%20standard%20formula.png " Standard formula version")

As you can see, the formula works fine, so we are ready to move on to creating a generic LAMBDA formula (unnamed version). The first thing to consider is if the formula requires inputs (parameters). In this case, the answer is "yes" – the formula requires a value for x, and a value for y. With that established, we start off with the LAMBDA function, then add the required parameters for user input:

    =LAMBDA(x,y  // begin with input parameters
    

Next, we need to add the actual calculation, x\*y:

    =LAMBDA(x,y,x*y)
    

If you enter the formula at this point, you'll get a #CALC! error. This happens because the formula has no input values to work with since there are no longer any cell references. To test the formula, we need to use a special syntax like this:

    =LAMBDA(x,y,x*y)(B5,C5) // testing syntax
    

This syntax, where parameters are supplied at the end of a LAMBDA function in a separate set of parentheses, is unique to LAMBDA functions. This allows the formula to be tested directly on the worksheet before the LAMBDA is named. In the screen below, you can see that the generic LAMBDA function in F5 returns exactly the same result as the original formula in E5:

![Generic (unnamed) lambda version](https://exceljet.net/sites/default/files/images/functions/inline/lambda%20unnamed%20formula.png "Generic (unnamed) lambda version")

We are now ready to name the LAMBDA function with the [Name Manager](https://exceljet.net/glossary/name-manager)
. First, copy the formula, _but do not include_ the testing parameters at the end. Next, open the Name Manager with the shortcut [Control + F3](https://exceljet.net/shortcuts/open-the-name-manager)
, and click New.

![Click New in Name Manager](https://exceljet.net/sites/default/files/images/functions/inline/name%20manager%20new.png "Click New in Name Manager")

In the New Name dialog, enter the name "XBYY", leave the scope set to "Workbook", and paste the formula you copied into the "Refers to" input area. (Tip: Use the tab key to navigate to the "Refers to" field).

![Name and define LAMBDA in name manager](https://exceljet.net/sites/default/files/images/functions/inline/name%20manager%20define%20new%20lambda.png "Name and define LAMBDA in name manager")

Make sure the formula begins with an equals sign (=). Now that the LAMBDA formula has a name, it can be used in the workbook like any other function. In the screen below, the formula in G5, copied down, is:

    =XBYY(B5,C5)
    

The screen below shows how things look in the workbook:

![Named LAMBDA function in action](https://exceljet.net/sites/default/files/images/functions/inline/named%20lambda%20function.png "Named LAMBDA function in action")

The new custom function returns the same result as the other two formulas.

> Custom LAMBDA names have [certain restrictions](https://exceljet.net/functions/lambda-function#lambda_naming_rules)
>  you should be aware of.

### Example 2 - volume of sphere

In this example, we'll convert a formula to calculate the volume of a sphere into a custom LAMBDA function. The general [Excel formula for calculating the volume of a sphere](https://exceljet.net/formulas/volume-of-a-sphere)
 is:

    =4/3*PI()*A1^3 // volume of sphere
    

where A1 represents the radius. The screen below shows this formula in action:

![Standard Excel formula for volume of sphere](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/lambda%20sphere%20volume%20original%20formula.png?itok=5dm2Yy6S "Standard Excel formula for volume of sphere")

Notice this formula only requires one input (radius) to calculate volume, so our LAMBDA function will only need one parameter (r), which will appear as the first argument. Here is the formula converted to LAMBDA:

    =LAMBDA(r,4/3*PI()*r^3) // generic lambda
    

Back in the worksheet, we've replaced the original formula with the generic LAMBDA version. Notice we are using the testing syntax, which allows us to plug in B5 for radius:

![Generic (unnamed) LAMBDA formula for volume of sphere](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/lambda%20sphere%20volume%20generic%20lambda.png?itok=LnUqPvfU "Generic (unnamed) LAMBDA formula for volume of sphere")

The results from the generic LAMBDA formula are exactly the same as the original formula, so the next step is to define and name this LAMBDA formula with the [Name Manager](https://exceljet.net/glossary/name-manager)
, as explained above. The name used for a LAMBDA function can be any valid Excel name. In this case, we'll name the formula "SphereVolume".

Back in the worksheet, we've replaced the generic (unnamed) LAMBDA formula with the named LAMBDA version and entered B5 for r. Notice that the results returned by the custom _SphereVolume_ function are exactly the same as those of previous results.

![Named LAMBDA formula for volume of sphere](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/lambda%20sphere%20volume%20named%20lambda.png?itok=m-vnqcxU "Named LAMBDA formula for volume of sphere")

### Example 3 - count words

In this example, we'll create a LAMBDA function to count words. Excel doesn't have a function for this purpose, but you can count words in a cell with a custom formula based on the [LEN](https://exceljet.net/functions/len-function)
 and [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
 functions like this:

    =LEN(TRIM(A1))-LEN(SUBSTITUTE(A1," ",""))+1
    

[Read the detailed explanation here](https://exceljet.net/formulas/count-total-words-in-a-cell)
. Here is the formula in action in a worksheet:

![Standard formula for counting words](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/lambda%20count%20words%20standard%20formula.png?itok=sgvcM-Fk "Standard formula for counting words")

Notice we get an incorrect count of 1 when the formula is given an empty cell (B10). We'll address this problem below.

This formula only requires one input: the text containing words. In our LAMBDA function, we'll name this argument "text". Here is the formula converted to LAMBDA:

    =LAMBDA(text,LEN(TRIM(text))-LEN(SUBSTITUTE(text," ",""))+1)
    

Notice "text" appears as the _first_ argument, and the calculation is the second and _final_ argument. In the screen below, we've replaced the original formula with the generic LAMBDA version. Notice we are using the testing syntax, which allows us to plug in B5 for text:

    =LAMBDA(text,LEN(TRIM(text))-LEN(SUBSTITUTE(text," ",""))+1)(B5)
    

![Generic LAMBDA for counting words](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/lambda%20count%20words%20generic%20lambda.png?itok=sRWlG_C- "Generic LAMBDA for counting words")

The results from the generic LAMBDA formula are the same as the original formula, so the next step is to define and name this LAMBDA formula with the [Name Manager](https://exceljet.net/glossary/name-manager)
, as explained previously. We'll name this formula "CountWords".

Below, we've replaced the generic (unnamed) LAMBDA formula with the named LAMBDA version, and entered B5 for text. Notice we get exactly the same results.

![Named LAMBDA for counting words - CountWords](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/lambda%20count%20words%20named%20lambda.png?itok=XpiQDLPt "Named LAMBDA for counting words - CountWords")

The formula used in the Name Manager to define CountWords is the same as above, without the testing syntax:

    =LAMBDA(text,LEN(TRIM(text))-LEN(SUBSTITUTE(text," ",""))+1)
    

#### Fixing the empty cell problem

As mentioned above, the formula above returns an incorrect count of 1 when a cell is empty. This problem can be fixed by replacing +1 with the code below:

    =LEN(TRIM(B5))-LEN(SUBSTITUTE(B5," ",""))+(LEN(TRIM(B5))>0)
    

[Full explanation here](https://exceljet.net/formulas/count-total-words-in-a-cell)
. To update the existing named LAMBDA formula, we again need to use the Name Manager:

1.  Open the Name Manager
2.  Select the name "CountWords" and click "Edit"
3.  Replace the "Refers to" code with this formula:

    =LAMBDA(text,LEN(TRIM(text))-LEN(SUBSTITUTE(text," ",""))+(LEN(TRIM(text))>0))
    

Once the Name Manager is closed, the CountWords works correctly on empty cells, as seen below:

![After updating CountWords in Name Manager](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/lambda%20count%20words%20named%20lambda%20fixed.png?itok=4m0DHLl- "After updating CountWords in Name Manager")

> Note: Updating the code _once_ in the Name Manager updates _all instances_ of the CountWords formula at once. This is a key benefit of custom functions created with LAMBDA – formula updates can be managed in one place.

### Example 4 - Number to words

Custom LAMBDA functions can be quite sophisticated, and they can even include sub-routines that encapsulate reusable logic. In the worksheet below, "NumberToWords" is a custom lambda that will convert a number like 123 into "One hundred twenty three" or "One hundred twenty three dollars" when currency is specified as USD:

![Custom function for converting numbers into words](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/number_to_words.png "Custom function for converting numbers into words")

This is a complex problem in Excel, usually handled with VBA (Visual Basic). In this case, however, all required logic is contained in a single LAMBDA with about 80 lines of code. This is what the code looks like in the [Excel Labs](https://techcommunity.microsoft.com/blog/excelblog/advanced-formula-environment-is-becoming-excel-labs-a-microsoft-garage-project/3736518)
 Advanced Formula Environment:

![Custom lambda in the Advanced Formula Environment](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/number_to_words_afe_example.png "Custom lambda in the Advanced Formula Environment")

You can find the full source code and a downloadable workbook [on this page](https://exceljet.net/formulas/number-to-words)
.

### LAMBDA naming rules

When naming a custom LAMBDA function in Excel, there are some restrictions you should be aware of:

1.  The name must be between 1 to 255 characters long.
2.  The name must start with a letter (A-Z, a-z) or an underscore (\_).
3.  The name must not contain spaces or special characters like @, !, #, $, %, etc.
4.  The name must not be a cell reference like A1, C2, X100, etc.
5.  The name must not conflict with an existing Excel function like SUM, COUNT, TEXT, etc.

The last point, 5, is especially important. While Excel will stop you from breaking the first 4 rules, it will not prevent you from naming your custom LAMBDA after an existing function. If you break this rule, the name will be created, but your custom function will never be invoked since Excel will default to existing function names. The result can be very confusing. Avoid this trouble by making sure your custom function name is unique.

> Be aware that custom LAMBDA names _are case-sensitive_. The names "MYFUNCTION", "MyFunction", and "myfunction", are all considered unique names for a custom LAMBDA.

LAMBDA function examples
------------------------

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

[![Excel formula: Get column totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20column%20totals.png "Excel formula: Get column totals")](https://exceljet.net/formulas/get-column-totals)

### [Get column totals](https://exceljet.net/formulas/get-column-totals)

In this example, the goal is to return an array with 7 subtotals, one for each day of the week, as seen in columns C:I. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We...

[![Excel formula: LAMBDA strip trailing characters recursive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20strip%20trailing%20characters%20recursive.png "Excel formula: LAMBDA strip trailing characters recursive")](https://exceljet.net/formulas/lambda-strip-trailing-characters-recursive)

### [LAMBDA strip trailing characters recursive](https://exceljet.net/formulas/lambda-strip-trailing-characters-recursive)

LAMBDA function can be used to create custom, reusable functions in Excel. This example illustrates a feature called recursion, in which a function calls itself. Recursion can be used to create elegant, compact, non-redundant code. This example is primarily proof of concept, to show a very simple...

[![Excel formula: Count columns that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20columns%20that%20contain%20specific%20values.png "Excel formula: Count columns that contain specific values")](https://exceljet.net/formulas/count-columns-that-contain-specific-values)

### [Count columns that contain specific values](https://exceljet.net/formulas/count-columns-that-contain-specific-values)

In this example, the goal is to count the number of columns in the data that contain 19 (the value in cell I4). The main challenge in this problem is that the value might appear in any row, and more than once in the same column. If we wanted to simply count the total number of times a value...

[![Excel formula: Sum numbers with text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20numbers%20with%20text.png "Excel formula: Sum numbers with text")](https://exceljet.net/formulas/sum-numbers-with-text)

### [Sum numbers with text](https://exceljet.net/formulas/sum-numbers-with-text)

In this example, one goal is to sum the numbers that appear in the range B5:B16. A second more challenging goal is to create the table of results seen in E7:F12. For convenience, data is the named range B5:B16. Total sum To sum all the numbers that appear in B5:B16, ignoring text, the formula in E5...

[![Excel formula: LAMBDA split text to array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20split%20text%20to%20array.png "Excel formula: LAMBDA split text to array")](https://exceljet.net/formulas/lambda-split-text-to-array)

### [LAMBDA split text to array](https://exceljet.net/formulas/lambda-split-text-to-array)

Excel did not originally offer the TEXTSPLIT function. This article describes how to use the LAMBDA function to create a custom function that splits text as a workaround. It's a good example of how the LAMBDA function can be used to bridge a gap, but the workaround is no longer necessary. I leave...

[![Excel formula: Find and replace multiple values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find-and-replace-multiple-values.png "Excel formula: Find and replace multiple values")](https://exceljet.net/formulas/find-and-replace-multiple-values)

### [Find and replace multiple values](https://exceljet.net/formulas/find-and-replace-multiple-values)

There is no built-in function to perform a series of find and replace operations in Excel, but you can create a formula that does the same thing. The goal in this example is to replace multiple ("find") values with corresponding ("replace") values in a single "replace all" operation. The text...

[![Excel formula: Count rows that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20that%20contain%20specific%20values.png "Excel formula: Count rows that contain specific values")](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

### [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

In this example, the goal is to count the number of rows in the data that contain the value in cell G4, which is 19. The main challenge in this problem is that the value might appear in any column, and might appear more than once in the same row. If we wanted to simply count the total number of...

[![Excel formula: Sum by quarter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20quarter.png "Excel formula: Sum by quarter")](https://exceljet.net/formulas/sum-by-quarter)

### [Sum by quarter](https://exceljet.net/formulas/sum-by-quarter)

In this example, the goal is to sum the amounts in column C by quarter in column G. Column D is a helper column , and the formula to calculate quarters from the dates in column B is explained below. All data is in an Excel Table named data in the range B5:E16. This problem can be solved with the...

[![Excel formula: LAMBDA contains which things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20contains%20which%20strings.png "Excel formula: LAMBDA contains which things")](https://exceljet.net/formulas/lambda-contains-which-things)

### [LAMBDA contains which things](https://exceljet.net/formulas/lambda-contains-which-things)

The goal in this example is to use a formula to report which things exist in a cell. The list of things to check for is in the named range things (E5:E9). The result is returned as a comma separated text string. The first step in creating a custom function with the LAMBDA function is to verify the...

[![Excel formula: Look up and return to single cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup_and_return_to_single_cell.png "Excel formula: Look up and return to single cell")](https://exceljet.net/formulas/look-up-and-return-to-single-cell)

### [Look up and return to single cell](https://exceljet.net/formulas/look-up-and-return-to-single-cell)

In this example, the goal is to look up and retrieve all names for a given team and return them in a single cell as a comma‑separated list. At the core, this is a lookup problem, but the twist is that we want to return multiple matches for each team, not just one. That means traditional lookup...

[![Excel formula: Hours that overlap specific time blocks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/hours_that_overlap_specific_time_blocks.png "Excel formula: Hours that overlap specific time blocks")](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)

### [Hours that overlap specific time blocks](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)

In this example, the goal is to calculate exactly how much of a task, shift, or event falls inside one or more defined blocks of time. The formula accepts a start and end time for the overall task or shift, as well as a start and end time for the block of interest. In the worksheet shown, the Start...

[![Excel formula: Calculate running total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate%20running%20total.png "Excel formula: Calculate running total")](https://exceljet.net/formulas/calculate-running-total)

### [Calculate running total](https://exceljet.net/formulas/calculate-running-total)

In this example, the goal is to calculate a running total in column D of the worksheet as shown. A running total, or cumulative sum, is a set of partial sums that changes as more data is collected. Each calculation represents the sum of values up to that point. In this example, each calculation...

[![Excel formula: Get row totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20row%20totals.png "Excel formula: Get row totals")](https://exceljet.net/formulas/get-row-totals)

### [Get row totals](https://exceljet.net/formulas/get-row-totals)

In this example, the goal is to return an array with nine subtotals, one for each of the colors named in column B. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We can'...

[![Excel formula: LAMBDA contains one of many](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20contains%20one%20of%20many.png "Excel formula: LAMBDA contains one of many")](https://exceljet.net/formulas/lambda-contains-one-of-many)

### [LAMBDA contains one of many](https://exceljet.net/formulas/lambda-contains-one-of-many)

Excel does not provide a dedicated "contains" function, but you can create a custom function to test if a cell contains one or many strings with the LAMBDA function . LAMBDA functions do not require VBA, but are only available in Excel 365 . The first step in creating a custom LAMBDA function is to...

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel ISOMITTED function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_isomitted_function.png "Excel ISOMITTED function")](https://exceljet.net/functions/isomitted-function)

### [ISOMITTED Function](https://exceljet.net/functions/isomitted-function)

The Excel ISOMITTED function is a helper function for LAMBDA functions to allow optional arguments. Inside a LAMBDA function, ISOMITTED will return TRUE when an argument has not been provided.

[![Excel MAP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20map%20function.png "Excel MAP function")](https://exceljet.net/functions/map-function)

### [MAP Function](https://exceljet.net/functions/map-function)

The Excel MAP function "maps" a custom LAMBDA function to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array.

[![Excel SCAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")](https://exceljet.net/functions/scan-function)

### [SCAN Function](https://exceljet.net/functions/scan-function)

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other...

[![Excel REDUCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20reduce%20function.png "Excel REDUCE function")](https://exceljet.net/functions/reduce-function)

### [REDUCE Function](https://exceljet.net/functions/reduce-function)

The Excel REDUCE function applies a custom LAMBDA function to each element in a given array and accumulates results to a single value.

[![Excel MAKEARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20makearray%20function.png "Excel MAKEARRAY function")](https://exceljet.net/functions/makearray-function)

### [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)

The Excel MAKEARRAY function returns an array with specified rows and columns, based on a custom [LAMBDA calculation](https://exceljet.net/functions/lambda-function)
. MAKEARRAY can be used to create arrays with variable dimensions based on a calculation....

[![Excel BYCOL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20bycol%20function.png "Excel BYCOL function")](https://exceljet.net/functions/bycol-function)

### [BYCOL Function](https://exceljet.net/functions/bycol-function)

The Excel BYCOL function applies a function to each column in a given array and returns one result per column. BYCOL can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate running total](https://exceljet.net/formulas/calculate-running-total)
    
*   [Sum numbers with text](https://exceljet.net/formulas/sum-numbers-with-text)
    
*   [Number to words](https://exceljet.net/formulas/number-to-words)
    
*   [Get row totals](https://exceljet.net/formulas/get-row-totals)
    
*   [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)
    
*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    
*   [LAMBDA append range](https://exceljet.net/formulas/lambda-append-range)
    
*   [Count columns that contain specific values](https://exceljet.net/formulas/count-columns-that-contain-specific-values)
    
*   [LAMBDA replace characters recursive](https://exceljet.net/formulas/lambda-replace-characters-recursive)
    
*   [Get column totals](https://exceljet.net/formulas/get-column-totals)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [ISOMITTED Function](https://exceljet.net/functions/isomitted-function)
    
*   [MAP Function](https://exceljet.net/functions/map-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    
*   [REDUCE Function](https://exceljet.net/functions/reduce-function)
    
*   [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)
    
*   [BYCOL Function](https://exceljet.net/functions/bycol-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    

### Links

*   [Microsoft LAMBDA function documentation](https://support.microsoft.com/en-us/office/lambda-function-bd212d27-1cd1-4321-a34a-ccbf254b8b67)
    

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