# Excel ISNUMBER function | Exceljet

**Source:** https://exceljet.net/functions/isnumber-function

---

[Skip to main content](https://exceljet.net/functions/isnumber-function#main-content)

[](https://exceljet.net/functions/isnumber-function#)

*   [Previous](https://exceljet.net/functions/isnontext-function)
    
*   [Next](https://exceljet.net/functions/isodd-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

ISNUMBER Function
=================

by Dave Bruns · Updated 7 Sep 2021

Related functions 
------------------

[ISBLANK](https://exceljet.net/functions/isblank-function)

[ISERR](https://exceljet.net/functions/iserr-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[ISEVEN](https://exceljet.net/functions/iseven-function)

[ISFORMULA](https://exceljet.net/functions/isformula-function)

[ISLOGICAL](https://exceljet.net/functions/islogical-function)

[ISNA](https://exceljet.net/functions/isna-function)

[ISNONTEXT](https://exceljet.net/functions/isnontext-function)

[ISODD](https://exceljet.net/functions/isodd-function)

[ISREF](https://exceljet.net/functions/isref-function)

[ISTEXT](https://exceljet.net/functions/istext-function)

![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")

Summary
-------

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Purpose 
--------

Test for numeric value

Return value 
-------------

A logical value (TRUE or FALSE)

Syntax
------

    =ISNUMBER(value)

*   _value_ - The value to check.

Using the ISNUMBER function 
----------------------------

The ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

The ISNUMBER function takes one [argument](https://exceljet.net/glossary/function-argument)
, _value_, which can be a cell reference, a formula, or a hardcoded value. Typically, _value_ is entered as a cell reference like A1. When _value_ is a number, the ISNUMBER function will return TRUE. Otherwise, ISNUMBER will return FALSE.

### Examples

The ISNUMBER function returns TRUE if _value_ is numeric:

    =ISNUMBER("apple") // returns FALSE
    =ISNUMBER(100) // returns TRUE
    

If cell A1 contains the number 100, ISNUMBER returns TRUE:

    =ISNUMBER(A1) // returns TRUE
    

If a cell contains a formula, ISNUMBER checks the result of the formula:

    =ISNUMBER(2+2) // returns TRUE
    =ISNUMBER(2^3) // returns TRUE
    =ISNUMBER(10 &" apples") // returns FALSE
    

Note: the ampersand (&) is the [concatenation](https://exceljet.net/glossary/concatenation)
 [operator](https://exceljet.net/glossary/math-operators)
 in Excel. When values are concatenated, the result is text.

### Count numeric values

To count cells in a range that contain numbers, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 like this:

    =SUMPRODUCT(--ISNUMBER(range))
    

The [double negative](https://exceljet.net/glossary/double-unary)
 coerces the TRUE and FALSE results from ISNUMBER into 1s and 0s and SUMPRODUCT sums the result.

### Notes

*   ISNUMBER will return TRUE for Excel [dates](https://exceljet.net/glossary/excel-date)
     and [times](https://exceljet.net/glossary/excel-time)
     since they are numeric.
*   ISNUMBER will return FALSE for empty cells and errors.

ISNUMBER function examples
--------------------------

[![Excel formula: If cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains.png "Excel formula: If cell contains")](https://exceljet.net/formulas/if-cell-contains)

### [If cell contains](https://exceljet.net/formulas/if-cell-contains)

The goal is to do something if a cell contains a given substring. For example, in the worksheet above, a formula returns "x" when a cell contains "abc". If you are familiar with Excel, you will probably think first of the IF function. However, one limitation of IF is that it does not support...

[![Excel formula: Filter contains one of many](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20contains%20one%20of%20many_0.png "Excel formula: Filter contains one of many")](https://exceljet.net/formulas/filter-contains-one-of-many)

### [Filter contains one of many](https://exceljet.net/formulas/filter-contains-one-of-many)

The FILTER function can filter data using a logical expression provided as the include argument. In this example, this argument is created with an expression that uses the ISNUMBER and MATCH functions like this: =ISNUMBER(MATCH(color,list,0)) MATCH is configured to look for each color in C5:C15...

[![Excel formula: FILTER case-sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20case%20sensitive.png "Excel formula: FILTER case-sensitive")](https://exceljet.net/formulas/filter-case-sensitive)

### [FILTER case-sensitive](https://exceljet.net/formulas/filter-case-sensitive)

This formula relies on the FILTER function to retrieve data based on a logical test . The array argument is provided as B5:D15, which contains all of the data without headers. The include argument is an expression based on the EXACT function: EXACT(B5:B15,"RED") The EXACT function compares two text...

[![Excel formula: Cell contains all of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_all_of_many_things.png "Excel formula: Cell contains all of many things")](https://exceljet.net/formulas/cell-contains-all-of-many-things)

### [Cell contains all of many things](https://exceljet.net/formulas/cell-contains-all-of-many-things)

In this example, the goal is to build a formula that will return TRUE if a given cell contains all values that appear in a given range. We could build a formula that uses nested IF statements to check for each value, but that won't scale well if we have a lot of values to test because each new...

[![Excel formula: Count cells equal to one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20one%20of%20many%20things.png "Excel formula: Count cells equal to one of many things")](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)

### [Count cells equal to one of many things](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)

In this example, the goal is to count the values in column B listed in the range E5:E7. One way to do this is to give the COUNTIF function all three values in the named range things (E5:E7) as criteria, then use the SUMPRODUCT function to get a total. The formula in G4 is: =SUMPRODUCT(COUNTIF(B5:...

[![Excel formula: FILTER with partial match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20partial%20match.png "Excel formula: FILTER with partial match")](https://exceljet.net/formulas/filter-with-partial-match)

### [FILTER with partial match](https://exceljet.net/formulas/filter-with-partial-match)

In this example, the goal is to extract a set of records that match a partial text string . To keep things simple, we are only matching one field in the data, the last name ("Last"). The core operation of this formula comes from the FILTER function (new in Excel 365 ) which extracts matching data...

[![Excel formula: Data validation require unique number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20require%20unique%20number.png "Excel formula: Data validation require unique number")](https://exceljet.net/formulas/data-validation-require-unique-number)

### [Data validation require unique number](https://exceljet.net/formulas/data-validation-require-unique-number)

Data validation rules are triggered when a user adds or changes a cell value. The AND function takes multiple arguments (logical expressions) and returns TRUE only when all arguments return TRUE. In this case, we need two conditions: Logical 1 tests if the input is a number using the ISNUMBER...

[![Excel formula: Range contains numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/range%20contains%20numbers.png "Excel formula: Range contains numbers")](https://exceljet.net/formulas/range-contains-numbers)

### [Range contains numbers](https://exceljet.net/formulas/range-contains-numbers)

Working from the inside out, the ISNUMBER function will return TRUE when given a number and FALSE if not. When you supply a range to ISNUMBER (i.e. an array ), ISNUMBER will return an array of results. In the example, the range C5:C9 contains 5 cells, so the array returned by ISNUMBER contains 5...

[![Excel formula: If cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20contains%20one%20of%20many%20things.png "Excel formula: If cell contains one of many things")](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

### [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

This formula uses two named ranges : things , and results . If you are porting this formula directly, be sure to use named ranges with the same names (defined based on your data). If you don't want to use named ranges, use absolute references instead. The core of this formula is this snippet:...

[![Excel formula: Split numbers from units of measure](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20numbers%20and%20units.png "Excel formula: Split numbers from units of measure")](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

### [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

Sometimes you encounter data that mixes units directly with numbers (i.e. 8km, 12v, 7.5hrs). Unfortunately, Excel will treat the numbers in this format as text, and you won't be able to perform math operations on such values. To split a number from a unit value, you need to determine the position...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

[![Excel formula: If cell contains this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains_this_or_that.png "Excel formula: If cell contains this or that")](https://exceljet.net/formulas/if-cell-contains-this-or-that)

### [If cell contains this or that](https://exceljet.net/formulas/if-cell-contains-this-or-that)

The goal is to do something if a cell contains one substring or another. Most users will think first of the IF function. However, one problem with IF is that it does not support wildcards like "?" and "\*". This means we can't use IF by itself to test for a substring like "abc" or "xyz" that might...

[![Excel formula: Sum if cells contain either x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_either_x_or_y.png "Excel formula: Sum if cells contain either x or y")](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y)

### [Sum if cells contain either x or y](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y)

In this example, the goal is to sum numbers in the range C5:C16 when text in the range B5:B16 contains the substring "red" OR the substring "blue". In other words, if the text in B5:B16 contains either of these two text values in any location, the corresponding number in C5:C16 should be included...

[![Excel formula: XLOOKUP match text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20match%20text%20contains.png "Excel formula: XLOOKUP match text contains")](https://exceljet.net/formulas/xlookup-match-text-contains)

### [XLOOKUP match text contains](https://exceljet.net/formulas/xlookup-match-text-contains)

The XLOOKUP function contains built-in support for wildcards, but this feature must be enabled explicitly by setting match mode to the number 2. In the example shown, XLOOKUP is configured to match the value entered in cell E5, which may appear anywhere in the lookup values in B5:B15. The formula...

ISNUMBER function videos
------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20find%20text%20with%20a%20formula-thumb.png)](https://exceljet.net/videos/how-to-find-text-with-a-formula)

### [How to find text with a formula](https://exceljet.net/videos/how-to-find-text-with-a-formula)

When you're working with text, you often need to pinpoint the location of some bit of text inside another. You can then use this position to extract or replace the text. In this video we'll look at how to locate the position of one text string inside another. Let's take a look. Excel contains two...

Related functions
-----------------

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

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

*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [LAMBDA strip characters](https://exceljet.net/formulas/lambda-strip-characters)
    
*   [Text is greater than number](https://exceljet.net/formulas/text-is-greater-than-number)
    
*   [FILTER case-sensitive](https://exceljet.net/formulas/filter-case-sensitive)
    
*   [LAMBDA contains which things](https://exceljet.net/formulas/lambda-contains-which-things)
    
*   [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    
*   [Sum if one of many things](https://exceljet.net/formulas/sum-if-one-of-many-things)
    
*   [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)
    
*   [Count total matches in two ranges](https://exceljet.net/formulas/count-total-matches-in-two-ranges)
    
*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    

### Videos

*   [How to find text with a formula](https://exceljet.net/videos/how-to-find-text-with-a-formula)
    

### Functions

*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [ISERR Function](https://exceljet.net/functions/iserr-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [ISEVEN Function](https://exceljet.net/functions/iseven-function)
    
*   [ISFORMULA Function](https://exceljet.net/functions/isformula-function)
    
*   [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    
*   [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)
    
*   [ISODD Function](https://exceljet.net/functions/isodd-function)
    
*   [ISREF Function](https://exceljet.net/functions/isref-function)
    
*   [ISTEXT Function](https://exceljet.net/functions/istext-function)
    

### Links

*   [Microsoft ISNUMBER function documentation](https://support.office.com/en-us/article/is-functions-0f2d7971-6019-40a0-a171-f2d869135665)
    

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