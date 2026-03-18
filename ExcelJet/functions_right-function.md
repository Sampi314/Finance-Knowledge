# Excel RIGHT function | Exceljet

**Source:** https://exceljet.net/functions/right-function

---

[Skip to main content](https://exceljet.net/functions/right-function#main-content)

[](https://exceljet.net/functions/right-function#)

*   [Previous](https://exceljet.net/functions/rept-function)
    
*   [Next](https://exceljet.net/functions/search-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

RIGHT Function
==============

by Dave Bruns · Updated 22 Feb 2024

Related functions 
------------------

[LEFT](https://exceljet.net/functions/left-function)

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")

Summary
-------

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

Purpose 
--------

Extract text from the right of a string

Return value 
-------------

One or more characters.

Syntax
------

    =RIGHT(text,[num_chars])

*   _text_ - The text from which to extract characters on the right.
*   _num\_chars_ - \[optional\] The number of characters to extract, starting on the right. Default = 1.

Using the RIGHT function 
-------------------------

The RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. The first argument, _text_, is the _text_ string to extract from. This is typically a reference to a cell that contains text. The second argument, called _num\_chars_, specifies the number of characters to extract. If _num\_chars_ is not provided, it defaults to 1. If _num\_chars_ is greater than the number of characters available, RIGHT returns the _entire_ text string. Although RIGHT is a simple function, it shows up in many more advanced formulas that test or manipulate text in a specific way.

### RIGHT function basics

To extract text with RIGHT, just provide the text and the number of characters to extract. The formulas below show how to extract one, two, and three characters with RIGHT:

    =RIGHT("apple",1) // returns "e"
    =RIGHT("apple",2) // returns "le"
    =RIGHT("apple",3) // returns "ple"

If the optional argument _num\_chars_ is not provided, it defaults to 1:

    =RIGHT("ABC") // returns "C"
    

If _num\_chars_ exceeds the length of the text string, RIGHT returns the entire string:

    =RIGHT("apple",100) // returns "apple"
    

When RIGHT is used on a numeric value, the result is text:

    =RIGHT(1500,3) // returns "500" as text
    

### Example - extract state abbreviation

The RIGHT function can be used to extract a specific number of characters from the end of a text string. For example, to extract the last two characters from "Portland, OR" you can use RIGHT like this:

    =RIGHT("Los Angeles, CA",2) // returns "CA"
    

Of course, it doesn't make sense to extract text from a text string that you have to type into a formula. A more typical example is to work with values that _already exist in cells_, as seen in the worksheet below. The formula in cell D5, copied down, is:

    =RIGHT(B5,2)

![RIGHT function example - extract state abbreviation](https://exceljet.net/sites/default/files/images/functions/inline/right_function_example_extract_state.png "RIGHT function example - extract state abbreviation")

Notice _num\_chars_ is provided as 2 to extract the last two letters from each city and state. The result is the two-letter abbreviation for the state.

### Example - extract the last character

An interesting quirk of the RIGHT function is that the number of characters to extract is not required and defaults to 1. This can be useful in cases where you only want to extract the last character of a text string, as seen below. Here, the formula in cell D5 looks like this:

    =RIGHT(B5)

![RIGHT function example - extract last character](https://exceljet.net/sites/default/files/images/functions/inline/right_function_example_extract_last_character.png "RIGHT function example - extract last character")

As you can see, without a value for _num\_chars_, RIGHT extracts the last character from each product, which corresponds to the size.

### Example - RIGHT with UPPER

You can easily combine RIGHT with other functions in Excel to get a more specific result. For example, you could nest the RIGHT function inside the UPPER function to convert the result from RIGHT to uppercase. You can see this approach in the worksheet below, where the formula in cell D5 looks like this:

    =UPPER(RIGHT(B5,3))

![RIGHT function example - RIGHT with UPPER](https://exceljet.net/sites/default/files/images/functions/inline/right_function_example_right_with_upper.png "RIGHT function example - RIGHT with UPPER")

All text in column B is lowercase. The RIGHT function extracts the state code as before and returns the result to the UPPER function, which converts the code to uppercase.

### Example - RIGHT with IF

You can easily combine the RIGHT function with the IF function to create "if cell ends with" logic. In the example below, a formula is used to flag codes that end with "HNN" with an "x". The formula in cell D5 is:

    =IF(RIGHT(B5,3)="hnn","x","")

![RIGHT function example - IF cell ends with](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/right_function_example_if_cell_ends_with.png "RIGHT function example - IF cell ends with")

As the formula is copied down, the RIGHT function returns the last 3 characters in each value, which are compared to "hnn" as a logical test. When the result is TRUE, IF returns "x". When the result is FALSE, IF returns an empty string "". The result is that the codes in column B that end with "abc" are clearly marked.

> RIGHT is not case-sensitive as you can see in the formula above. To perform a case-sensitive test you can combine RIGHT with the EXACT function. [Example here](https://exceljet.net/formulas/cell-ends-with)
> .

### Example - RIGHT with FIND

A common challenge with the RIGHT function is extracting a _variable_ number of characters, depending on the location of a _specific character_ in the text string. To handle this situation you can use the RIGHT function together with the FIND function in a generic formula like this:

    =RIGHT(text,LEN(text)-FIND(character,text)) // extract text after character
    

FIND returns the position of the character, and RIGHT returns all text to the right of that position. The screen below shows how this formula can be applied in a worksheet. The formula in cell D5 is:

    =RIGHT(B5,LEN(B5)-FIND(" ",B5))

![RIGHT function example - get last name from full name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/right_function_example_get_last_name.png "RIGHT function example - get last name from full name")

As the formula is copied down the LEN function returns the length of the text string in cell B5. Next, the FIND function returns the position of the space character " " as a number. The result from FIND is then subtracted from the result from LEN and returned to RIGHT as the _num\_chars_ argument. Finally, the RIGHT function returns all text after the space, which corresponds to the last name in this simplified example. You can read a more [detailed explanation here](https://exceljet.net/formulas/get-last-name-from-name)
.

### Related functions

The RIGHT function is used to extract text from the _right_ side of a text string. Use the [LEFT function](https://exceljet.net/functions/left-function)
 to extract text starting from the _left_ side of the text, and the [MID function](https://exceljet.net/functions/mid-function)
 to extract from the _middle_ of text. The [LEN function](https://exceljet.net/functions/len-function)
 returns the length of a text string as a count of characters and is often combined with LEFT, MID, and RIGHT.

> In the latest version of Excel, newer functions like [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
> , [TEXTAFTER](https://exceljet.net/functions/textafter-function)
> , and [TEXTSPLIT](https://exceljet.net/functions/textsplit-function)
>  greatly simplify certain text operations and make some traditional formulas that use the RIGHT function obsolete. [Example here](https://exceljet.net/formulas/get-name-from-email-address)
> .

### Notes

*   RIGHT is not case-sensitive.
*   RIGHT can extract numbers as well as text.
*   The output from RIGHT is _always_ text.
*   RIGHT ignores [number formatting](https://exceljet.net/glossary/number-format)
     when extracting characters.
*   _Num\_chars_ is optional and defaults to 1.

RIGHT function examples
-----------------------

[![Excel formula: Split numbers from units of measure](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20numbers%20and%20units.png "Excel formula: Split numbers from units of measure")](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

### [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

Sometimes you encounter data that mixes units directly with numbers (i.e. 8km, 12v, 7.5hrs). Unfortunately, Excel will treat the numbers in this format as text, and you won't be able to perform math operations on such values. To split a number from a unit value, you need to determine the position...

[![Excel formula: Remove first character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20first%20character.png "Excel formula: Remove first character")](https://exceljet.net/formulas/remove-first-character)

### [Remove first character](https://exceljet.net/formulas/remove-first-character)

This formula uses the REPLACE function to replace the first character in a cell with an empty string (""). The arguments for REPLACE are configured as follows: old\_text is the original value from column B start\_num is hardcoded as the number 1 num\_chars comes from column C new\_text is entered as an...

[![Excel formula: Remove protocol from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_protocol_from_url.png "Excel formula: Remove protocol from URL")](https://exceljet.net/formulas/remove-protocol-from-url)

### [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)

In this example, the goal is to remove the protocol from a list of URLs. To remove the protocol from a URL, we need to remove the first part of the URL. Protocols typically look like this: http:// https:// sftp:// Notice that all protocols end with a double slash ("//"). In the current version of...

[![Excel formula: Parse time string to time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/parse%20time%20string%20to%20time.png "Excel formula: Parse time string to time")](https://exceljet.net/formulas/parse-time-string-to-time)

### [Parse time string to time](https://exceljet.net/formulas/parse-time-string-to-time)

In this example, the goal is to parse a text string into a proper Excel time . First, note that the cells in F5:F13 are formatted as Text prior to entry . This allows the times to contain leading zeros like "083000". Alternately, you can enter these time strings with a single quote at the start...

[![Excel formula: Cell ends with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_ends_with.png "Excel formula: Cell ends with")](https://exceljet.net/formulas/cell-ends-with)

### [Cell ends with](https://exceljet.net/formulas/cell-ends-with)

In this example, the goal is to test values in column B to see if they end with a specific text string, which is "jwb" in the worksheet shown. This problem can be solved with the RIGHT function, as explained below. RIGHT function The RIGHT function extracts a given number of characters from the...

[![Excel formula: Get date from day number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20date%20from%20day%20number.png "Excel formula: Get date from day number")](https://exceljet.net/formulas/get-date-from-day-number)

### [Get date from day number](https://exceljet.net/formulas/get-date-from-day-number)

The DATE function builds dates from separate year, month, and day values. One of its tricks is the ability to roll forward to correct dates when given days and months that are "out of range". For example, DATE returns April 9, 2016, with the following arguments: =DATE(2016,1,100) There is no 100th...

[![Excel formula: Split dimensions into two parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20dimensions%20into%20two%20parts%20-%20left.png "Excel formula: Split dimensions into two parts")](https://exceljet.net/formulas/split-dimensions-into-two-parts)

### [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)

Background A common annoyance with data is that it may be represented as text instead of numbers. This is especially common with dimensions, which may appear in one text string that includes units, for example: 50 ft x 200 ft 153 ft x 324 ft Etc. In a spreadsheet, it's a lot more convenient to have...

[![Excel formula: Highlight cells that end with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20end%20with.png "Excel formula: Highlight cells that end with")](https://exceljet.net/formulas/highlight-cells-that-end-with)

### [Highlight cells that end with](https://exceljet.net/formulas/highlight-cells-that-end-with)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each cell in B4:G12, and the reference to B4 will change to the address of each cell being evaluated...

[![Excel formula: Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20date%20ddmmyy%20to%20mmddyy.png "Excel formula: Convert text date dd/mm/yy to mm/dd/yy")](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)

### [Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)

The core of this formula is the DATE function, which is used to assemble a proper Excel date value. The DATE function requires valid year, month, and day values, so these are parsed out of the original text string as follows: 1. The year value is extracted with the RIGHT function: RIGHT(B5,2)+2000...

[![Excel formula: Get domain from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_from_email_address_0.png "Excel formula: Get domain from email address")](https://exceljet.net/formulas/get-domain-from-email-address)

### [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)

In this example, the goal is to extract just the domain name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTAFTER function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the RIGHT, LEN, and FIND...

[![Excel formula: Get first name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_with_comma.png "Excel formula: Get first name from name with comma")](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

### [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

In this example, the goal is to extract the first name from a list of names in "Last, First" format as seen in column B. There are several ways to approach this problem. In the current version of Excel, the easiest solution is to use the TEXTAFTER function. In older versions of Excel, it can be...

[![Excel formula: Normalize size units to Gigabytes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/normalize%20units%20to%20gigabytes.png "Excel formula: Normalize size units to Gigabytes")](https://exceljet.net/formulas/normalize-size-units-to-gigabytes)

### [Normalize size units to Gigabytes](https://exceljet.net/formulas/normalize-size-units-to-gigabytes)

Important: This formula assumes that units are the last 2 characters of the text value that includes both a number and a unit of measure. This formula works because digital units have a "power of 10" relationship. At the core, this formula separates the number part of the size from the unit, then...

[![Excel formula: Get last line in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20line%20in%20cell.png "Excel formula: Get last line in cell")](https://exceljet.net/formulas/get-last-line-in-cell)

### [Get last line in cell](https://exceljet.net/formulas/get-last-line-in-cell)

This formula takes advantage of the fact that TRIM will remove any number of leading spaces. We look for line breaks and "flood" the text with spaces where we find one. Then we come back and grab text from the right. Working from the inside out, we use the SUBSTITUTE function to find all line...

[![Excel formula: Convert text to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20to%20date.png "Excel formula: Convert text to date")](https://exceljet.net/formulas/convert-text-to-date)

### [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)

The DATE function creates a valid date using three arguments: year, month, and day: =DATE(year,month,day) In cell C6, we use the LEFT, MID, and RIGHT functions to extract each of these components from a text string, and feed the results into the DATE function: =DATE(LEFT(B6,4),MID(B6,5,2),RIGHT(B6,...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

RIGHT function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20combine%20functions%20in%20a%20formula-thumb.png)](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)

### [How to combine functions in a formula](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)

In this video I'm going to show you how you can use multiple Excel functions to split, manipulate, and rejoin values inside a single formula. Here we have some sample data and, in column B, we have text values with a number at the end. What we want to do is increment these numbers using the value...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20extract%20text%20with%20LEFT%20and%20RIGHT-thumb_0.png)](https://exceljet.net/videos/how-to-extract-text-with-left-and-right)

### [How to extract text with LEFT and RIGHT](https://exceljet.net/videos/how-to-extract-text-with-left-and-right)

In this video, we'll look at how to use the RIGHT and LEFT functions to extract specific text from data. Let's take a look. Here we have some customer data. To illustrate how to extract text using the LEFT and RIGHT functions, I'll use them both to pull out just certain parts of this information...

Related functions
-----------------

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

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

*   [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)
    
*   [Cell ends with](https://exceljet.net/formulas/cell-ends-with)
    
*   [Normalize size units to Gigabytes](https://exceljet.net/formulas/normalize-size-units-to-gigabytes)
    
*   [Split dimensions into three parts](https://exceljet.net/formulas/split-dimensions-into-three-parts)
    
*   [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)
    
*   [Convert text to numbers](https://exceljet.net/formulas/convert-text-to-numbers)
    
*   [Parse time string to time](https://exceljet.net/formulas/parse-time-string-to-time)
    
*   [Get last word](https://exceljet.net/formulas/get-last-word)
    
*   [Remove first character](https://exceljet.net/formulas/remove-first-character)
    
*   [Count between dates by age range](https://exceljet.net/formulas/count-between-dates-by-age-range)
    

### Videos

*   [How to extract text with LEFT and RIGHT](https://exceljet.net/videos/how-to-extract-text-with-left-and-right)
    
*   [How to combine functions in a formula](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)
    

### Functions

*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    

### Links

*   [Microsoft RIGHT function documentation](https://support.office.com/en-us/article/right-rightb-functions-240267ee-9afa-4639-a02b-f19e1786cf2f)
    

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