# Excel ISBLANK function | Exceljet

**Source:** https://exceljet.net/functions/isblank-function

---

[Skip to main content](https://exceljet.net/functions/isblank-function#main-content)

[](https://exceljet.net/functions/isblank-function#)

*   [Previous](https://exceljet.net/functions/info-function)
    
*   [Next](https://exceljet.net/functions/iserr-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

ISBLANK Function
================

by Dave Bruns · Updated 9 Feb 2024

Related functions 
------------------

[ISERR](https://exceljet.net/functions/iserr-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[ISEVEN](https://exceljet.net/functions/iseven-function)

[ISFORMULA](https://exceljet.net/functions/isformula-function)

[ISLOGICAL](https://exceljet.net/functions/islogical-function)

[ISNA](https://exceljet.net/functions/isna-function)

[ISNONTEXT](https://exceljet.net/functions/isnontext-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[ISODD](https://exceljet.net/functions/isodd-function)

[ISREF](https://exceljet.net/functions/isref-function)

[ISTEXT](https://exceljet.net/functions/istext-function)

![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")

Summary
-------

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

Purpose 
--------

Test if a cell is empty

Return value 
-------------

A logical value (TRUE or FALSE)

Syntax
------

    =ISBLANK(value)

*   _value_ - The value to check.

Using the ISBLANK function 
---------------------------

The ISBLANK function is a simple function to test if a cell is empty or not. If a cell is empty, ISBLANK returns TRUE. If a cell contains any value, ISBLANK returns FALSE. ISBLANK function takes one argument, _value_, which is a cell reference like A1. For example, if cell A1 contains nothing at all, the ISBLANK function will return TRUE:

    =ISBLANK(A1) // returns TRUE
    

If cell A1 contains _any value_ or _any formula_, the ISBLANK function will return FALSE:

    =ISBLANK(A1) // returns false
    

> The word "blank" is ambiguous in Excel, because a cell that contains only a space character will _look_ blank but _not_ be empty. It is best to think of ISBLANK to mean "is empty" since it will return FALSE when a cell looks blank but is not empty.

### Things to know about the ISBLANK function

Here are some things you should know about the ISBLANK function:

1.  You can use ISBLANK to test for empty cells in a dataset.
2.  You can use the ISBLANK function to trigger a Conditional Formatting rule that highlights all empty cells (see below).
3.  You can combine ISBLANK with the IF function to display a custom message if a cell is empty. For example, you might display "Input Required" if a cell is blank.
4.  You can use ISBLANK to stop a formula from calculating when certain cells are empty. For details, [see this example](https://exceljet.net/formulas/only-calculate-if-not-blank)
    .
5.  You can combine ISBLANK with the NOT function to reverse the logic to "is not blank" (see below).
6.  Instead of =ISBLANK(A1), you can use the syntax A1="". See below for details.
7.  If you want to _count_ blank cells see the [COUNTBLANK function](https://exceljet.net/functions/countblank-function)
    .

### Example - test if cells are empty

In the worksheet below, the ISBLANK function is used to test if cells in column B are empty. The formula in cell C5 is:

    =ISBLANK(B5)

![ISBLANK example - test for empty cells in column B](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_isblank_function_basic_example_0.png "ISBLANK example - test for empty cells in column B")

As the formula is copied down, it returns TRUE if the corresponding cell in column B is empty and FALSE if not. Notice the result in cell C8 is FALSE even though cell B8 looks empty. However, because cell B8 contains a single space, it is not empty.

### Example - Is not empty

To reverse the logic and test for cells that are _not blank_ (not empty) you can nest ISBLANK inside the [NOT function](https://exceljet.net/functions/not-function)
 like this:

    =NOT(ISBLANK(A1)) // test not blank
    

You can see this approach in the worksheet below. The formula in cell C5 is:

    =NOT(ISBLANK(B5))

![ISBLANK example - test for non-empty cells in column B](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_isblank_function_not_blank.png "ISBLANK example - test for non-empty cells in column B")

The above formula will return TRUE when a cell is not empty, and FALSE when a cell is empty. Notice this exactly reverses the results seen with ISBLANK alone.

### Example - If a date is blank

A classic example of the ISBLANK function is to test if a cell is empty and display a custom message if so. The worksheet below contains a list of tasks in column C. In column D, a date is present if a task is complete. In column E, the ISBLANK function is used together with the [IF function](https://exceljet.net/functions/if-function)
 to mark tasks that do not have a date as "Open". The formula in cell E5, copied down, is:

    =IF(ISBLANK(D5),"Open","")

![ISBLANK example - if date is empty task is open](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_isblank_function_example_if_date_is_blank.png "ISBLANK example - if date is empty task is open")

You can easily extend this formula to mark tasks that do have a date as "Closed" like this:

    =IF(ISBLANK(D5),"Open","Closed")

### Example - highlight blank cells

You can use the ISBLANK function to quickly highlight empty cells with Conditional Formatting. In the worksheet below, the formula used to highlight blank cells is:

    =ISBLANK(C5)

When ISBLANK returns TRUE, it triggers a Conditional Formatting rule that applies a bright fill color to empty cells in the range C5:J16. This makes it easy to see at a glance which students are missing quiz scores:

![ISBLANK example - conditional formatting to highlight empty cells](https://exceljet.net/sites/default/files/images/functions/inline/highlight_blank_cells.png "ISBLANK example - conditional formatting to highlight empty cells")

The formatting is dynamic — if the data changes, the highlighting will automatically update as required. For step-by-step instructions, [see this example](https://exceljet.net/formulas/highlight-blank-cells)
.

### ISBLANK alternative syntax

Many formulas will use an abbreviated syntax to test for empty cells, instead of the ISBLANK function. This syntax uses an [empty string](https://exceljet.net/glossary/empty-string)
 ("") with Excel's [math operators](https://exceljet.net/glossary/math-operators)
 "=" or "<>". For example, to test if A1 is empty, you can use:

    =A1="" // TRUE if A1 is empty
    

To test if A1 is not empty:

    =A1<>"" // TRUE if A1 is not empty
    

This syntax can be used interchangeably with ISBLANK. For example, inside the [IF function](https://exceljet.net/functions/if-function)
:

    =IF(ISBLANK(A1),result1,result2) // if A1 is empty
    

is equivalent to:

    =IF(A1="",result1,result2) // if A1 is empty
    

Likewise, the formula:

    =IF(NOT(ISBLANK(A1)),result1,result2)
    

is the same, as:

    =IF(A1<>"",result1,result2)
    

Both will return _result1_ when A1 is not empty and _result2_ when A1 is empty.

### Handling empty strings returned by formulas

If a cell contains _any formula_, the ISBLANK function and the alternatives above will return FALSE, even if the formula returns an empty string (""). This can cause problems when the goal is to count or process blank cells that include empty strings. One workaround is to use the [LEN function](https://exceljet.net/functions/len-function)
 to test for a length of zero. For example, the formula below will return TRUE if A1 is empty or contains a formula that returns an empty string:

    =LEN(A1)=0 // TRUE if empty
    

So, inside the IF function, you can use LEN like this:

    =IF(LEN(A1)=0,result1,result2) // if A1 is empty
    

You can use this same approach to [count cells that are not blank](https://exceljet.net/formulas/count-cells-that-are-not-blank)
.

ISBLANK function examples
-------------------------

[![Excel formula: Only calculate if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20not%20blank%20then%20calculate2.png "Excel formula: Only calculate if not blank")](https://exceljet.net/formulas/only-calculate-if-not-blank)

### [Only calculate if not blank](https://exceljet.net/formulas/only-calculate-if-not-blank)

The goal is to verify the input of all required values before calculating a result. In the worksheet shown, the SUM function is used as an example only. You can use the same approach with any formula to prevent calculation until all required values are available. The logic can be adjusted in many...

[![Excel formula: Calculate days open](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20days%20open.png "Excel formula: Calculate days open")](https://exceljet.net/formulas/calculate-days-open)

### [Calculate days open](https://exceljet.net/formulas/calculate-days-open)

In this example, the goal is to calculate the number of days a ticket/case/issue has been open. We start counting on the date a ticket was opened and stop counting on the date a ticket was closed. If there is no closed date, the ticket is still open. Because dates in Excel are just serial numbers...

[![Excel formula: Return blank if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/return_blank_if.png "Excel formula: Return blank if")](https://exceljet.net/formulas/return-blank-if)

### [Return blank if](https://exceljet.net/formulas/return-blank-if)

The goal is to display a blank cell based on a specific condition. In the worksheet shown, we want to return the value from column C, but only when the value in column B is "A". If the value in column B is anything else, we want to display nothing. The easiest way to solve this problem is with the...

[![Excel formula: If cell is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_blank.png "Excel formula: If cell is blank")](https://exceljet.net/formulas/if-cell-is-blank)

### [If cell is blank](https://exceljet.net/formulas/if-cell-is-blank)

In the example worksheet, column D contains a date when a task is completed. If the task is not yet complete, the cell in column D will be empty (blank). In column E, the goal is to display the word "Open" when there is no date in column D. If there is a date in column D, the formula in column E...

[![Excel formula: Get first non-blank value in a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_non-blank_value_in_a_list.png "Excel formula: Get first non-blank value in a list")](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

### [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

The gist of this problem is that we want to get the first non-blank cell, but we don't have a direct way to do that in Excel. The easiest way to solve this problem is with the XLOOKUP function. XLOOKUP function The XLOOKUP function is a modern upgrade to the VLOOKUP function. XLOOKUP is very...

[![Excel formula: Highlight blank cells](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight_blank_cells.png "Excel formula: Highlight blank cells")](https://exceljet.net/formulas/highlight-blank-cells)

### [Highlight blank cells](https://exceljet.net/formulas/highlight-blank-cells)

In this example, the goal is to highlight empty cells in the range C5:J16 with conditional formatting. This is a quick and easy way to locate missing values in a data set. To apply a conditional formatting rule to highlight empty cells, follow these steps: Select the range that contains empty cells...

[![Excel formula: Add row numbers and skip blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add%20row%20numbers%20and%20skip%20blanks.png "Excel formula: Add row numbers and skip blanks")](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks)

### [Add row numbers and skip blanks](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks)

In the example shown, the goal is to add row numbers in column B only when there is a value in column C. The formula in B5 is: =IF(ISBLANK(C5),"",COUNTA($C$5:C5)) The IF function first checks if cell C5 has a value with the ISBLANK function : ISBLANK(C5) // TRUE if empty, FALSE if not If C5 is...

[![Excel formula: If cell is not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_not_blank_0.png "Excel formula: If cell is not blank")](https://exceljet.net/formulas/if-cell-is-not-blank)

### [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)

The goal is to create a formula that returns "Done" in column E when a cell in column D is not blank (i.e., contains a value). In the worksheet shown, column D records the date a task is completed. If column D contains a date (i.e. is not empty), we can assume the task is complete. This problem can...

[![Excel formula: Celsius to Fahrenheit conversion](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/celsius%20to%20fahrenheit%20conversion.png "Excel formula: Celsius to Fahrenheit conversion")](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)

### [Celsius to Fahrenheit conversion](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)

In this example, the goal is to convert the Celsius temperatures shown in column B to Fahrenheit temperatures in column C. The solution shown in the worksheet above relies on the CONVERT function, which can convert a number in one measurement system to another. CONVERT is fully automatic and based...

[![Excel formula: If not blank multiple cells](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_not_blank_multiple_cells.png "Excel formula: If not blank multiple cells")](https://exceljet.net/formulas/if-not-blank-multiple-cells)

### [If not blank multiple cells](https://exceljet.net/formulas/if-not-blank-multiple-cells)

The goal is to return the first non-blank value in each row from columns B:E, moving left to right. One way to solve this problem is with a series of nested IF statements. Since all cells are contiguous (connected) another way to get the first value is with the XLOOKUP function. Both approaches are...

[![Excel formula: Check register balance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/check%20register%20balance.png "Excel formula: Check register balance")](https://exceljet.net/formulas/check-register-balance)

### [Check register balance](https://exceljet.net/formulas/check-register-balance)

The value in G5 is hard-coded. The formula picks up the value in G5, then subtracts the value (if any) in E6 and adds the value (if any) in F6. When the credit or debit values are empty, they behave like zero and have no effect on the result. When this formula is copied down column G, it will...

[![Excel formula: Count line breaks in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20line%20breaks%20in%20cell.png "Excel formula: Count line breaks in cell")](https://exceljet.net/formulas/count-line-breaks-in-cell)

### [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)

First, the LEN function counts total characters in the cell B5. Next SUBSTITUTE removes all "line returns" from the text in B5 by looking for CHAR(10) which is the character code for the return character in Windows. LEN returns the result inside of a second LEN, which counts characters without...

ISBLANK function videos
-----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20join%20values%20with%20the%20ampersand-thumb_0.png)](https://exceljet.net/videos/how-to-join-values-with-the-ampersand)

### [How to join values with the ampersand](https://exceljet.net/videos/how-to-join-values-with-the-ampersand)

Often, you'll need to join together values in Excel. A good example is when you have first, last, and middle names in separate columns and you want to join these together into one name. This is referred to as "concatenation." In this example, we have first, middle, and last names shown separately...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20trap%20errors%20in%20formulas-thumb.png)](https://exceljet.net/videos/how-to-trap-errors-in-formulas)

### [How to trap errors in formulas](https://exceljet.net/videos/how-to-trap-errors-in-formulas)

In this video, we'll look at a few ways to trap errors. Trapping errors can make your spreadsheets more professional by making them less cluttered and more friendly to use. In this first worksheet, we have a simple table that shows test scores for 5 sections. The total questions in each section are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20search%20box%20with%20conditional%20formatting.png)](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

### [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

In this video, we'll look at a way to create a search box that highlights rows in a table, by using conditional formatting, and a formula that checks several columns at once. This is a great alternative to filtering, because you can see the information you're looking for highlighted in context. Let...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20fill%20in%20missing%20data%20part%202-thumb_0.png)](https://exceljet.net/videos/how-to-fill-in-missing-data-part-2)

### [How to fill in missing data part 2](https://exceljet.net/videos/how-to-fill-in-missing-data-part-2)

In this video, we're going to build on the technique we covered in an earlier video, where we added in missing data using formulas. Here again we have a music collection with some missing data. The twist, in this case, is that the Artist isn't in the right column. Instead of column B, it appears in...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20join%20cell%20values%20with%20CONCATENATE-thumb.png)](https://exceljet.net/videos/how-to-join-cell-values-with-concatenate)

### [How to join cell values with CONCATENATE](https://exceljet.net/videos/how-to-join-cell-values-with-concatenate)

In this video we'll look at the CONCATENATE function , which is an alternative to using the ampersand character to join values. This is the same example we looked at previously: a table which contains first, middle, and last names. In column E, I'll add a formula that uses the CONCATENATE function...

Related functions
-----------------

[![Excel ISERR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserr%20function.png "Excel ISERR function")](https://exceljet.net/functions/iserr-function)

### [ISERR Function](https://exceljet.net/functions/iserr-function)

The Excel ISERR function returns TRUE for any error type except the #N/A error. You can use the ISERR function together with the IF function to test for an error and display a custom message, or perform a different calculation if found.

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

[![Excel ISEVEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iseven%20function.png "Excel ISEVEN function")](https://exceljet.net/functions/iseven-function)

### [ISEVEN Function](https://exceljet.net/functions/iseven-function)

The Excel ISEVEN function returns TRUE when a value is an even number, and FALSE when a value is an odd number. ISEVEN will return the #VALUE error if a value is not numeric.

[![Excel ISFORMULA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isformula%20function.png "Excel ISFORMULA function")](https://exceljet.net/functions/isformula-function)

### [ISFORMULA Function](https://exceljet.net/functions/isformula-function)

The Excel ISFORMULA function returns TRUE if a cell contains a formula, and FALSE if not. When a cell contains a formula ISFORMULA will return TRUE regardless of the formula's output or error conditions.

[![Excel ISLOGICAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20islogical%20function.png "Excel ISLOGICAL function")](https://exceljet.net/functions/islogical-function)

### [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)

The Excel ISLOGICAL function returns TRUE when a cell contains the logical values TRUE or FALSE, and returns FALSE for cells that contain any other value, including empty cells. 

[![Excel ISNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isna%20function.png "Excel ISNA function")](https://exceljet.net/functions/isna-function)

### [ISNA Function](https://exceljet.net/functions/isna-function)

The Excel ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs.

[![Excel ISNONTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnontext%20function.png "Excel ISNONTEXT function")](https://exceljet.net/functions/isnontext-function)

### [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)

The Excel ISNONTEXT function returns TRUE when a cell contains any value except text. This includes numbers, dates, times, errors, and formulas that do not return text. ISNONTEXT also returns TRUE when a cell is empty.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel ISODD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isodd%20function.png "Excel ISODD function")](https://exceljet.net/functions/isodd-function)

### [ISODD Function](https://exceljet.net/functions/isodd-function)

The Excel ISODD function returns TRUE when a value is an odd number, and FALSE when a value is an even number. ISODD will return the #VALUE error if a value is not numeric.

[![Excel ISREF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isref%20function.png "Excel ISREF function")](https://exceljet.net/functions/isref-function)

### [ISREF Function](https://exceljet.net/functions/isref-function)

The Excel ISREF returns TRUE when a cell contains a reference and FALSE if not. You can use the ISREF function to check for a reference in a formula.

[![Excel ISTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20istext%20function.png "Excel ISTEXT function")](https://exceljet.net/functions/istext-function)

### [ISTEXT Function](https://exceljet.net/functions/istext-function)

The Excel ISTEXT function returns TRUE when a cell contains a [text value](https://exceljet.net/glossary/text-value)
, and FALSE if the cell contains any other value. You can use the ISTEXT function to check if a cell contains a text value, or a numeric value entered as text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Highlight blank cells](https://exceljet.net/formulas/highlight-blank-cells)
    
*   [Celsius to Fahrenheit conversion](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)
    
*   [Only calculate if not blank](https://exceljet.net/formulas/only-calculate-if-not-blank)
    
*   [If not blank multiple cells](https://exceljet.net/formulas/if-not-blank-multiple-cells)
    
*   [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)
    
*   [Return blank if](https://exceljet.net/formulas/return-blank-if)
    
*   [Check register balance](https://exceljet.net/formulas/check-register-balance)
    
*   [Calculate days open](https://exceljet.net/formulas/calculate-days-open)
    
*   [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)
    
*   [If cell is blank](https://exceljet.net/formulas/if-cell-is-blank)
    

### Videos

*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
*   [How to trap errors in formulas](https://exceljet.net/videos/how-to-trap-errors-in-formulas)
    
*   [How to fill in missing data part 2](https://exceljet.net/videos/how-to-fill-in-missing-data-part-2)
    
*   [How to join values with the ampersand](https://exceljet.net/videos/how-to-join-values-with-the-ampersand)
    
*   [How to join cell values with CONCATENATE](https://exceljet.net/videos/how-to-join-cell-values-with-concatenate)
    

### Functions

*   [ISERR Function](https://exceljet.net/functions/iserr-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [ISEVEN Function](https://exceljet.net/functions/iseven-function)
    
*   [ISFORMULA Function](https://exceljet.net/functions/isformula-function)
    
*   [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    
*   [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [ISODD Function](https://exceljet.net/functions/isodd-function)
    
*   [ISREF Function](https://exceljet.net/functions/isref-function)
    
*   [ISTEXT Function](https://exceljet.net/functions/istext-function)
    

### Links

*   [Microsoft ISBLANK function documentation](https://support.office.com/en-us/article/is-functions-0f2d7971-6019-40a0-a171-f2d869135665)
    

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