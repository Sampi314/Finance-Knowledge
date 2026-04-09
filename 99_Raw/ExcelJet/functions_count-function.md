# Excel COUNT function | Exceljet

**Source:** https://exceljet.net/functions/count-function

---

[Skip to main content](https://exceljet.net/functions/count-function#main-content)

[](https://exceljet.net/functions/count-function#)

*   [Previous](https://exceljet.net/functions/correl-function)
    
*   [Next](https://exceljet.net/functions/counta-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

COUNT Function
==============

by Dave Bruns · Updated 12 May 2023

Related functions 
------------------

[COUNT](https://exceljet.net/functions/count-function)

[COUNTA](https://exceljet.net/functions/counta-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[COUNTBLANK](https://exceljet.net/functions/countblank-function)

![Excel COUNT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")

Summary
-------

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored.

Purpose 
--------

Count numbers

Return value 
-------------

Count of numeric values

Syntax
------

    =COUNT(value1,[value2],...)

*   _value1_ - An item, cell reference, or range.
*   _value2_ - \[optional\] An item, cell reference, or range.

Using the COUNT function 
-------------------------

The COUNT function returns the count of numeric values in the list of supplied [arguments](https://exceljet.net/glossary/function-argument)
. COUNT takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form of _value1_, _value2_, _value3_, etc. Arguments can be individual hardcoded values, cell references, or ranges up to a total of 255 arguments. All numbers are counted, including negative numbers, percentages, dates, times, fractions, and formulas that return numbers. COUNT _ignores_ text values, errors, and empty cells. The COUNT function is similar to the [COUNTA function](https://exceljet.net/functions/counta-function)
, but COUNTA _includes_ numbers and text in the count.

### Examples

The COUNT function counts numeric values and ignores text values:

    =COUNT(1,2,3) // returns 3
    =COUNT(1,"a","b") // returns 1
    =COUNT("apple",100,125,150,"orange") // returns 3
    

Typically, the COUNT function is used on a range. For example, to count numeric values in the range A1:A10:

    =COUNT(A1:A100) // count numbers in A1:A10
    

In the example shown, COUNT is set up to count numbers in the range B5:B15:

    =COUNT(B5:B15) // returns 6
    

COUNT returns 6, since there are 6 numeric values in the range B5:B15. Text values and blank cells are ignored. Note that [dates](https://exceljet.net/glossary/excel-date)
 and [times](https://exceljet.net/glossary/excel-time)
 are numbers, and therefore included in the count.

### Functions for counting

*   To count numbers only, use the [COUNT function](https://exceljet.net/functions/count-function)
    .
*   To count numbers and text, use the [COUNTA function](https://exceljet.net/functions/counta-function)
    .
*   To count with one condition, use the [COUNTIF function](https://exceljet.net/functions/countif-function)
    
*   To count with multiple conditions, use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
    .
*   To count empty cells, use the [COUNTBLANK function](https://exceljet.net/functions/countblank-function)
    .

### Notes

*   COUNT can handle up to 255 arguments.
*   COUNT ignores the logical values TRUE and FALSE.
*   COUNT ignores text values, errors, and empty cells.

COUNT function examples
-----------------------

[![Excel formula: Filter values in array formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20values%20in%20array%20formula.png "Excel formula: Filter values in array formula")](https://exceljet.net/formulas/filter-values-in-array-formula)

### [Filter values in array formula](https://exceljet.net/formulas/filter-values-in-array-formula)

In this example, the goal is to filter the values in one array by the values in another array. For convenience, data (B4:D11) and filter (F4:F6) are named ranges . The solution is based on the MATCH function with the ISNUMBER function . This is a pattern you will see often in more advanced formulas...

[![Excel formula: Cell contains specific words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_words.png "Excel formula: Cell contains specific words")](https://exceljet.net/formulas/cell-contains-specific-words)

### [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)

In this example, the goal is to test the text in a cell and return TRUE if it contains one or more specific words, and FALSE if not. Notice the emphasis here is on words, not substrings. For example, if we are testing for the word "green" and the text contains the word "evergreen" but not the word...

[![Excel formula: Only calculate if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20not%20blank%20then%20calculate2.png "Excel formula: Only calculate if not blank")](https://exceljet.net/formulas/only-calculate-if-not-blank)

### [Only calculate if not blank](https://exceljet.net/formulas/only-calculate-if-not-blank)

The goal is to verify the input of all required values before calculating a result. In the worksheet shown, the SUM function is used as an example only. You can use the same approach with any formula to prevent calculation until all required values are available. The logic can be adjusted in many...

[![Excel formula: Average last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_5_columns.png "Excel formula: Average last n columns")](https://exceljet.net/formulas/average-last-n-columns)

### [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)

In this example, the goal is to average the last n columns in a set of data, where n is a variable entered in cell K5 that can be changed at any time. Since more data may be added, a key requirement is to average amounts by position. For convenience, the values to average are in the named range...

[![Excel formula: Cell contains all of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_all_of_many_things.png "Excel formula: Cell contains all of many things")](https://exceljet.net/formulas/cell-contains-all-of-many-things)

### [Cell contains all of many things](https://exceljet.net/formulas/cell-contains-all-of-many-things)

In this example, the goal is to build a formula that will return TRUE if a given cell contains all values that appear in a given range. We could build a formula that uses nested IF statements to check for each value, but that won't scale well if we have a lot of values to test because each new...

[![Excel formula: Validate strong password](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/validate_strong_password.png "Excel formula: Validate strong password")](https://exceljet.net/formulas/validate-strong-password)

### [Validate strong password](https://exceljet.net/formulas/validate-strong-password)

In this example, the goal is to check for "strong" passwords. What makes a password strong depends on the rules it must follow. In this case, a strong password must meet the following six conditions: At least 8 and not more than 15 characters long Contains at least one uppercase (A-Z) letter...

[![Excel formula: Cell contains number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_number.png "Excel formula: Cell contains number")](https://exceljet.net/formulas/cell-contains-number)

### [Cell contains number](https://exceljet.net/formulas/cell-contains-number)

In this example, the goal is to test the passwords in column B to see if they contain a number. This is a surprisingly tricky problem because Excel doesn't have a function that will let you test for a number inside a text string directly. Note this is different from checking if a cell value is a...

[![Excel formula: Count cells that contain numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20numbers.png "Excel formula: Count cells that contain numbers")](https://exceljet.net/formulas/count-cells-that-contain-numbers)

### [Count cells that contain numbers](https://exceljet.net/formulas/count-cells-that-contain-numbers)

In this example, the goal is to count the number of cells in a range that contain numbers. This problem can be solved with the COUNT function or the SUMPRODUCT function. Both methods are explained below. COUNT function The COUNT function counts the number of cells in a range that contain numeric...

[![Excel formula: Count numbers in text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_numbers_in_text_string.png "Excel formula: Count numbers in text string")](https://exceljet.net/formulas/count-numbers-in-text-string)

### [Count numbers in text string](https://exceljet.net/formulas/count-numbers-in-text-string)

In this example, the goal is to count numbers that appear in column B. The COUNT function is designed to only count numeric values, but because all values in the range B5:B15 are text , COUNT will return zero. One approach is to split the characters in each text value into an array , then use the...

[![Excel formula: Data validation specific characters only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Data%20validation%20specific%20characters%20only.png "Excel formula: Data validation specific characters only")](https://exceljet.net/formulas/data-validation-specific-characters-only)

### [Data validation specific characters only](https://exceljet.net/formulas/data-validation-specific-characters-only)

Working from the inside out, the MID function is used to generate an array from text entered in B5 with this snippet: MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1) explained in detail here . The result is an array like this: {"A";"A";"A";"-";"1";"1";"1"} which goes into MATCH as the lookup value. For...

[![Excel formula: Count total matches in two ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20total%20matches%20in%20two%20ranges.png "Excel formula: Count total matches in two ranges")](https://exceljet.net/formulas/count-total-matches-in-two-ranges)

### [Count total matches in two ranges](https://exceljet.net/formulas/count-total-matches-in-two-ranges)

In this example, the goal is to count the number of exact matches in two ranges, ignoring the sort order or location of the values in each range. This problem can be solved with the COUNTIF function or with the MATCH function. Each approach is explained below. Note: Both formulas below use the...

[![Excel formula: Count unique dates ignore time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20dates%20ignore%20time.png "Excel formula: Count unique dates ignore time")](https://exceljet.net/formulas/count-unique-dates-ignore-time)

### [Count unique dates ignore time](https://exceljet.net/formulas/count-unique-dates-ignore-time)

In this example, the goal is to count the unique dates in a range of timestamps (i.e. dates that contain dates and times). In addition, we also want to create the table of results seen in E7:F9. For convenience, data is the named range B5:B16. Basic count To get a count of individual dates that...

[![Excel formula: Sort text and numbers with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20mixed%20data%20with%20a%20formula.png "Excel formula: Sort text and numbers with formula")](https://exceljet.net/formulas/sort-text-and-numbers-with-formula)

### [Sort text and numbers with formula](https://exceljet.net/formulas/sort-text-and-numbers-with-formula)

This formula first generates a rank value using an expression based on COUNTIF: =COUNTIF(data,"<="...

[![Excel formula: Count unique dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20dates2.png "Excel formula: Count unique dates")](https://exceljet.net/formulas/count-unique-dates)

### [Count unique dates](https://exceljet.net/formulas/count-unique-dates)

Traditionally, counting unique items with an Excel formula has been a tricky problem, because there hasn't been a dedicated unique function. However, that changed when dynamic arrays were added to Excel 365 , along with several new functions, including UNIQUE. Note: In older versions of Excel, you...

[![Excel formula: Data validation no punctuation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20no%20punctuation.png "Excel formula: Data validation no punctuation")](https://exceljet.net/formulas/data-validation-no-punctuation)

### [Data validation no punctuation](https://exceljet.net/formulas/data-validation-no-punctuation)

Data validation rules are triggered when a user adds or changes a cell value. When a custom formula returns TRUE, validation passes and the input is accepted. When a formula returns FALSE, validation fails and the input is rejected with a popup message. In this case, we have previously defined the...

COUNT function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Create%20a%20dynamic%20reference%20to%20a%20named%20range-thumb.png)](https://exceljet.net/videos/create-a-dynamic-reference-to-a-named-range)

### [Create a dynamic reference to a named range](https://exceljet.net/videos/create-a-dynamic-reference-to-a-named-range)

In this video we'll look at how to create a dynamic reference to a named range using the INDIRECT function . Let's take a look. Here we have a simple table that summarizes sales by salesperson over a four-month period. What we're going to do is use the INDIRECT function to make a dynamic reference...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNT%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-count-function)

### [How to use the COUNT function](https://exceljet.net/videos/how-to-use-the-count-function)

The COUNT function is a simple function that counts numbers. Let's take a look. The COUNT function counts numeric values. For example, if I enter the formula =COUNT(B7:B11), Excel will return "4" because that range contains four numbers total. The COUNT function ignores blank cells and text values...

Related functions
-----------------

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel COUNTBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20countblank%20function.png "Excel COUNTBLANK function")](https://exceljet.net/functions/countblank-function)

### [COUNTBLANK Function](https://exceljet.net/functions/countblank-function)

The Excel COUNTBLANK function returns a count of empty cells in a [range](https://exceljet.net/glossary/range)
. Cells that contain text, numbers, errors, spaces, etc. are _not_ counted. Formulas that return empty strings ("") _are_ counted as blank.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain numbers](https://exceljet.net/formulas/count-cells-that-contain-numbers)
    
*   [Count numbers in text string](https://exceljet.net/formulas/count-numbers-in-text-string)
    
*   [Sort text and numbers with formula](https://exceljet.net/formulas/sort-text-and-numbers-with-formula)
    
*   [Filter values in array formula](https://exceljet.net/formulas/filter-values-in-array-formula)
    
*   [Count unique dates](https://exceljet.net/formulas/count-unique-dates)
    
*   [Data validation no punctuation](https://exceljet.net/formulas/data-validation-no-punctuation)
    
*   [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)
    
*   [Count total matches in two ranges](https://exceljet.net/formulas/count-total-matches-in-two-ranges)
    
*   [Dynamic range between two matches](https://exceljet.net/formulas/dynamic-range-between-two-matches)
    
*   [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)
    

### Videos

*   [How to use the COUNT function](https://exceljet.net/videos/how-to-use-the-count-function)
    
*   [Create a dynamic reference to a named range](https://exceljet.net/videos/create-a-dynamic-reference-to-a-named-range)
    

### Functions

*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [COUNTBLANK Function](https://exceljet.net/functions/countblank-function)
    

### Links

*   [Microsoft COUNT function documentation](https://support.office.com/en-us/article/count-function-a59cd7fc-b623-4d93-87a4-d23bf411294c)
    

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