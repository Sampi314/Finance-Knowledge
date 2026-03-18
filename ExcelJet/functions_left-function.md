# Excel LEFT function | Exceljet

**Source:** https://exceljet.net/functions/left-function

---

[Skip to main content](https://exceljet.net/functions/left-function#main-content)

[](https://exceljet.net/functions/left-function#)

*   [Previous](https://exceljet.net/functions/fixed-function)
    
*   [Next](https://exceljet.net/functions/len-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

LEFT Function
=============

by Dave Bruns · Updated 22 Feb 2024

Related functions 
------------------

[RIGHT](https://exceljet.net/functions/right-function)

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

![Excel LEFT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20left.png "Excel LEFT function")

Summary
-------

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

Purpose 
--------

Extract text from the left of a string

Return value 
-------------

One or more characters.

Syntax
------

    =LEFT(text,[num_chars])

*   _text_ - The text from which to extract characters.
*   _num\_chars_ - \[optional\] The number of characters to extract, starting on the left. Default = 1.

Using the LEFT function 
------------------------

The LEFT function extracts a given number of characters from the _left_ side of a supplied text string. The first argument, _text_, is the _text_ string to extract from. This is typically a reference to a cell that contains text. The second argument, called _num\_chars_, specifies the number of characters to extract. If _num\_chars_ is not provided, it defaults to 1. If _num\_chars_ is greater than the number of characters available, LEFT returns the _entire_ text string. Although LEFT is a simple function, it shows up in many more advanced formulas that test or manipulate text in a specific way.

### LEFT function basics

To extract text with LEFT, just provide the text and the number of characters to extract. The formulas below show how to extract one, two, and three characters with LEFT:

    =LEFT("apple",1) // returns "a"
    =LEFT("apple",2) // returns "ap"
    =LEFT("apple",3) // returns "app"

If the optional argument _num\_chars_ is not provided, it defaults to 1:

    =LEFT("ABC") // returns "A"
    

If _num\_chars_ exceeds the length of the text string, LEFT returns the entire string:

    =LEFT("apple",100) // returns "apple"
    

When LEFT is used on a numeric value, the result is text:

    =LEFT(1000,3) // returns "100" as text
    

### Example - abbreviate month names

The LEFT function can be used to abbreviate text values. For example, to extract the first three characters of "January" you can use LEFT like this:

    =LEFT("January",3) // returns "Jan"
    

Of course, it doesn't make sense to abbreviate a text string that you have to type into a formula. A more typical example is to abbreviate text values that _already exist in cells_, as seen in the worksheet below. The formula in cell D5, copied down, is:

    =LEFT(B5,3)

![ LEFT function example - abbreviate month names](https://exceljet.net/sites/default/files/images/functions/inline/left_function_example_abbreviate_month_names.png " LEFT function example - abbreviate month names")

Notice _num\_chars_ is provided as 3 to extract the first 3 letters of each month.

### Example - extract the first character

An interesting quirk of the LEFT function is that the number of characters to extract is not required and defaults to 1. This can be useful in cases where you only want to extract the first character of a text string, as seen below. Here, the formula in cell D5 looks like this:

    =LEFT(B5)

![ LEFT function example - defaults to 1 character](https://exceljet.net/sites/default/files/images/functions/inline/left_function_example_defaults_to_1_character.png " LEFT function example - defaults to 1 character")

As you can see, without a value for _num\_chars_, LEFT extracts the first letter of each month.

### Example - LEFT with UPPER

You can easily combine LEFT with other functions in Excel to get a more specific result. For example, you could nest the LEFT function inside the UPPER function to convert the result from LEFT to uppercase. You can see this approach in the worksheet below, where the formula in cell D5 looks like this:

    =UPPER(LEFT(B5,3))

![Example - The LEFT function with the UPPER function](https://exceljet.net/sites/default/files/images/functions/inline/left_function_example_combine_with_other_functions.png "Example - The LEFT function with the UPPER function")

### Example - LEFT with IF

You can easily combine the LEFT function with the IF function to create "if cell begins with" logic. In the example below, a formula is used to flag codes that begin with "xyz" with an "x". The formula in cell D5 is:

    =IF(LEFT(B5,3)="xyz","x","")

![ LEFT function example - if cell begins with "xyz"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/left_function_example_if_cell_begins_with.png " LEFT function example - if cell begins with "xyz"")

As the formula is copied down, the LEFT function returns the first 3 characters in each value, which are compared to "xyz" as a logical test. When the result is TRUE, IF returns "x". When the result is FALSE, IF returns an empty string "". The result is that the codes in column B that begin with "xyz" are clearly marked.

> LEFT is not case-sensitive as you can see in the formula above. To perform a case-sensitive test you can combine LEFT with the EXACT function. [Example here](https://exceljet.net/formulas/cell-begins-with)
> .

### Example - LEFT with FIND

A common challenge with the LEFT function is extracting a _variable_ number of characters, depending on the location of a _specific character_ in the text string. To handle this situation you can use the LEFT function together with the [FIND function](https://exceljet.net/functions/find-function)
 in a generic formula like this:

    =LEFT(text,FIND(character,text)-1) // extract text up to character
    

FIND returns the position of the character, and LEFT returns all text to the left of that position. The screen below shows how this formula can be applied in a worksheet. The formula in cell D5 is:

    =LEFT(B5,FIND(" ",B5)-1)

![ LEFT function example - get first name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/left_function_example_get_first_name.png " LEFT function example - get first name")

As the formula is copied down, the FIND function returns the position of the space character " " as a number. The result, minus one, is returned to the LEFT function as the _num\_chars_ argument, which then extracts all text up to the first space. You can read a more [detailed explanation here](https://exceljet.net/formulas/get-first-name-from-name)
.

### Related functions

The LEFT function is used to extract text from the _left_ side of a text string. Use the [RIGHT function](https://exceljet.net/functions/right-function)
 to extract text starting from the _right_ side of the text, and the [MID function](https://exceljet.net/functions/mid-function)
 to extract from the _middle_ of text. The [LEN function](https://exceljet.net/functions/len-function)
 returns the length of a text string as a count of characters and is often combined with LEFT, MID, and RIGHT.

> In the latest version of Excel, newer functions like [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
> , [TEXTAFTER](https://exceljet.net/functions/textafter-function)
> , and [TEXTSPLIT](https://exceljet.net/functions/textsplit-function)
>  greatly simplify certain text operations and make some traditional formulas that use the LEFT function obsolete. [Example here](https://exceljet.net/formulas/get-name-from-email-address)
> .

### Notes

*   LEFT is not case-sensitive.
*   LEFT can extract numbers as well as text.
*   The output from LEFT is _always_ text.
*   LEFT ignores [number formatting](https://exceljet.net/glossary/number-format)
     when extracting characters.
*   _Num\_chars_ is optional and defaults to 1.

LEFT function examples
----------------------

[![Excel formula: Get workbook path only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_workbook_path_only.png "Excel formula: Get workbook path only")](https://exceljet.net/formulas/get-workbook-path-only)

### [Get workbook path only](https://exceljet.net/formulas/get-workbook-path-only)

In this example, the goal is to get the workbook path without the workbook name . For example, given a workbook called fruits.xlsx saved to: C:\\examples\\fruits.xlsx We want the path only like this: C:\\examples\\ TEXTBEFORE solution In a modern version of Excel (Excel 2021 or later) the simplest way...

[![Excel formula: Remove unwanted characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20unwanted%20characters.png "Excel formula: Remove unwanted characters")](https://exceljet.net/formulas/remove-unwanted-characters)

### [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)

The SUBSTITUTE function can find and replace text in a cell, wherever it occurs. In this case, we are using SUBSTITUTE to find a character with code number 202, and replace it with an empty string (""), which effectively removes the character completely. How can you figure out which character(s)...

[![Excel formula: Convert text to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert_text_to_numbers.png "Excel formula: Convert text to numbers")](https://exceljet.net/formulas/convert-text-to-numbers)

### [Convert text to numbers](https://exceljet.net/formulas/convert-text-to-numbers)

In this example, the goal is to convert the text values seen in column B to the numeric values seen in column D. There are several ways to fix this problem in Excel, but this article focuses on a formula-based approach to convert text values to numbers. It also explains how to convert values in...

[![Excel formula: Capitalize first letter in a text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/capitalize_first_letter.png "Excel formula: Capitalize first letter in a text string")](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)

### [Capitalize first letter in a text string](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)

One of the most important skills to learn with Excel formulas is the concept of nesting. Put simply, nesting just means putting one function inside another. Nesting is super useful, but it does take some practice. You have to learn to read a formula from the inside out. The formulas below are good...

[![Excel formula: Normalize size units to Gigabytes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/normalize%20units%20to%20gigabytes.png "Excel formula: Normalize size units to Gigabytes")](https://exceljet.net/formulas/normalize-size-units-to-gigabytes)

### [Normalize size units to Gigabytes](https://exceljet.net/formulas/normalize-size-units-to-gigabytes)

Important: This formula assumes that units are the last 2 characters of the text value that includes both a number and a unit of measure. This formula works because digital units have a "power of 10" relationship. At the core, this formula separates the number part of the size from the unit, then...

[![Excel formula: Remove first character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20first%20character.png "Excel formula: Remove first character")](https://exceljet.net/formulas/remove-first-character)

### [Remove first character](https://exceljet.net/formulas/remove-first-character)

This formula uses the REPLACE function to replace the first character in a cell with an empty string (""). The arguments for REPLACE are configured as follows: old\_text is the original value from column B start\_num is hardcoded as the number 1 num\_chars comes from column C new\_text is entered as an...

[![Excel formula: Split numbers from units of measure](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20numbers%20and%20units.png "Excel formula: Split numbers from units of measure")](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

### [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

Sometimes you encounter data that mixes units directly with numbers (i.e. 8km, 12v, 7.5hrs). Unfortunately, Excel will treat the numbers in this format as text, and you won't be able to perform math operations on such values. To split a number from a unit value, you need to determine the position...

[![Excel formula: Get workbook name and path without sheet](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_workbook_name_and_path_without_sheet.png "Excel formula: Get workbook name and path without sheet")](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)

### [Get workbook name and path without sheet](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)

In this example, the goal is to get a normal path to the current workbook, without a sheet name, and without the square brackets ("\[ \]") that normally enclose the workbook name. This is a pretty simple problem in the latest version of Excel, which provides the TEXTBEFORE function . In older...

[![Excel formula: Get last name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_with_comma.png "Excel formula: Get last name from name with comma")](https://exceljet.net/formulas/get-last-name-from-name-with-comma)

### [Get last name from name with comma](https://exceljet.net/formulas/get-last-name-from-name-with-comma)

In this example, the goal is to extract the last name from a list of names in "Last, First" format as seen in column B. In the current version of Excel, the easiest solution is to use the TEXTBEFORE function. In older versions of Excel, it can be solved with a more complex formula based on the LEFT...

[![Excel formula: Data validation must begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20must%20begin%20with.png "Excel formula: Data validation must begin with")](https://exceljet.net/formulas/data-validation-must-begin-with)

### [Data validation must begin with](https://exceljet.net/formulas/data-validation-must-begin-with)

Data validation rules are triggered when a user adds or changes a cell value. In this formula, the LEFT function is used to extract the first 3 characters of the input in C5. Next, the EXACT function is used to compare the extracted text to the text hard-coded into the formula, "MX-". EXACT...

[![Excel formula: Get date from day number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20date%20from%20day%20number.png "Excel formula: Get date from day number")](https://exceljet.net/formulas/get-date-from-day-number)

### [Get date from day number](https://exceljet.net/formulas/get-date-from-day-number)

The DATE function builds dates from separate year, month, and day values. One of its tricks is the ability to roll forward to correct dates when given days and months that are "out of range". For example, DATE returns April 9, 2016, with the following arguments: =DATE(2016,1,100) There is no 100th...

[![Excel formula: Count numbers that begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20numbers%20that%20begin%20with.png "Excel formula: Count numbers that begin with")](https://exceljet.net/formulas/count-numbers-that-begin-with)

### [Count numbers that begin with](https://exceljet.net/formulas/count-numbers-that-begin-with)

In this example, the goal is to count numbers in the range B5:B15 ( named data ) that begin with the numbers shown in column D. You would think this would be a good problem to solve with the COUNTIF function but for reasons explained below, COUNTIF won't work. Instead, you can use the SUMPRODUCT...

[![Excel formula: Sum matching columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20matching%20columns.png "Excel formula: Sum matching columns")](https://exceljet.net/formulas/sum-matching-columns)

### [Sum matching columns](https://exceljet.net/formulas/sum-matching-columns)

At the core, this formula relies on the SUMPRODUCT function to sum values in matching columns in the named range data C5:G14. If all data were provided to SUMPRODUCT in a single range, the result would be the sum of all values in the range: =SUMPRODUCT(data) // all data, returns 387 To apply a...

[![Excel formula: Count cells that begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20begin%20with.png "Excel formula: Count cells that begin with")](https://exceljet.net/formulas/count-cells-that-begin-with)

### [Count cells that begin with](https://exceljet.net/formulas/count-cells-that-begin-with)

In this example, the goal is to count cells in the range B5:B16 that begin with specific text, which is provided in column D. For convenience, the range B5:B16 is named data . COUNTIF function The simplest way to solve this problem is with the COUNTIF function and a wildcard. COUNTIF supports three...

[![Excel formula: Match long text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/match%20long%20text.png "Excel formula: Match long text")](https://exceljet.net/formulas/match-long-text)

### [Match long text](https://exceljet.net/formulas/match-long-text)

The MATCH function has a limit of 255 characters for the lookup value. If you try to use longer text, MATCH will return a #VALUE error. To workaround this limit you can use boolean logic and the LEFT, MID, and EXACT functions to parse and compare text. Note: this formula performs an exact match...

LEFT function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Dynamic%20arrays%20are%20native-PLay.png)](https://exceljet.net/videos/dynamic-arrays-are-native)

### [Dynamic arrays are native](https://exceljet.net/videos/dynamic-arrays-are-native)

In this video we'll look at how dynamic array behavior is native and deeply integrated in Excel. Although new dynamic array functions will get a lot of attention, it's important to understand that dynamic array behavior is native and deeply integrated. All formulas will now run on a new calculation...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20extract%20text%20with%20LEFT%20and%20RIGHT-thumb_0.png)](https://exceljet.net/videos/how-to-extract-text-with-left-and-right)

### [How to extract text with LEFT and RIGHT](https://exceljet.net/videos/how-to-extract-text-with-left-and-right)

In this video, we'll look at how to use the RIGHT and LEFT functions to extract specific text from data. Let's take a look. Here we have some customer data. To illustrate how to extract text using the LEFT and RIGHT functions, I'll use them both to pull out just certain parts of this information...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20complex%20formula%20step%20by%20step-thumb.png)](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

### [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

When you look at a complex formula in Excel you may be completely baffled at first glance, but all complex formulas are just small steps added together. Let me show you an example. Here we have a list of names. We want to pull out the first name from the full name. There's an Excel function called...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20extract%20a%20first%20name%20with%20a%20helper%20column-thumb.png)](https://exceljet.net/videos/how-to-extract-a-first-name-with-a-helper-column)

### [How to extract a first name with a helper column](https://exceljet.net/videos/how-to-extract-a-first-name-with-a-helper-column)

In this video we'll look at how to combine the FIND function with the LEFT function to extract the first name from a full name. Let's take a look. Excel's LEFT and RIGHT function s are easy to use when you know how many characters you want to extract. But what if you want to extract the first name...

Related functions
-----------------

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get first word](https://exceljet.net/formulas/get-first-word)
    
*   [Remove first character](https://exceljet.net/formulas/remove-first-character)
    
*   [Remove trailing slash from url](https://exceljet.net/formulas/remove-trailing-slash-from-url)
    
*   [If cell begins with x, y, or z](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)
    
*   [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)
    
*   [Get workbook path only](https://exceljet.net/formulas/get-workbook-path-only)
    
*   [Split dimensions into three parts](https://exceljet.net/formulas/split-dimensions-into-three-parts)
    
*   [Match first does not begin with](https://exceljet.net/formulas/match-first-does-not-begin-with)
    
*   [Normalize size units to Gigabytes](https://exceljet.net/formulas/normalize-size-units-to-gigabytes)
    
*   [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)
    

### Videos

*   [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)
    
*   [How to extract text with LEFT and RIGHT](https://exceljet.net/videos/how-to-extract-text-with-left-and-right)
    
*   [How to extract a first name with a helper column](https://exceljet.net/videos/how-to-extract-a-first-name-with-a-helper-column)
    
*   [Dynamic arrays are native](https://exceljet.net/videos/dynamic-arrays-are-native)
    

### Functions

*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    

### Links

*   [Microsoft LEFT function documentation](https://support.office.com/en-us/article/left-leftb-functions-9203d2d2-7960-479b-84c6-1ea52b99640c)
    

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