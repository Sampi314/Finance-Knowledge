# Split text and numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/split-text-and-numbers

---

[Skip to main content](https://exceljet.net/formulas/split-text-and-numbers#main-content)

[](https://exceljet.net/formulas/split-text-and-numbers#)

*   [Previous](https://exceljet.net/formulas/split-numbers-from-units-of-measure)
    
*   [Next](https://exceljet.net/formulas/split-text-string-at-specific-character)
    

[Text](https://exceljet.net/formulas#Text)

Split text and numbers
======================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[FIND](https://exceljet.net/functions/find-function)

[MIN](https://exceljet.net/functions/min-function)

[RIGHT](https://exceljet.net/functions/right-function)

[LEFT](https://exceljet.net/functions/left-function)

![Excel formula: Split text and numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/split%20text%20and%20numbers.png "Excel formula: Split text and numbers")

Summary
-------

To separate text and numbers, you can use a formula based on the [FIND function](https://exceljet.net/functions/find-function)
, the [MIN function](https://exceljet.net/functions/min-function)
, and the [LEN function](https://exceljet.net/functions/len-function)
 with the [LEFT](https://exceljet.net/functions/left-function)
 or [RIGHT](https://exceljet.net/functions/right-function)
 function, depending on whether you want to extract the text or the number. In the example shown, the formula in C5 is:

    =MIN(FIND({0,1,2,3,4,5,6,7,8,9},B5&"0123456789"))
    

which returns 7, the position of the number 3 in the string "apples30".

Generic formula
---------------

    =MIN(FIND({0,1,2,3,4,5,6,7,8,9},A1&"0123456789"))

Explanation 
------------

### Overview

The formula looks complex, but the mechanics are in fact quite simple.

As with most formulas that split or extract text, the key is to locate the _position_ of the thing you are looking for. Once you have the position, you can use other functions to extract what you need.

In this case, we are assuming that numbers and text are combined, and that the number appears after the text. From the original text, which appears in one cell, you want to split the text and numbers into separate cells, like this:

|     |     |     |
| --- | --- | --- |
| **Original** | **Text** | **Number** |
| Apples30 | Apples | 30  |
| peaches24 | peaches | 24  |
| oranges12 | oranges | 12  |
| peaches0 | peaches | 0   |

As stated above, the key in this case is to locate the starting position of the number, which you can do with a formula like this:

    =MIN(FIND({0,1,2,3,4,5,6,7,8,9},A1&"0123456789"))
    

Once you have the position, to extract just the text, use:

    =LEFT(A1,position-1)
    

And, to extract just the number, use:

    =RIGHT(A1,LEN(A1)-position+1)
    

In the first formula above, we are using the FIND function to locate the starting position of the number. For the find\_text, we are using the array constant {0,1,2,3,4,5,6,7,8,9}, this causes the FIND function to perform a separate search for each value in the array constant. Since the array constant contains 10 numbers, the result will be an array with 10 values. For example, if original text is "apples30" the resulting array will be:

    {8,10,11,7,13,14,15,16,17,18}
    

Each number in this array represents the position of an item in the array constant inside the original text.

Next the MIN function returns the smallest value in the list, which corresponds to the position in of the _first number_ that appears in the original text. In essence, the FIND function gets all number positions, and MIN gives us the first number position: notice that 7 is the smallest value in the array, which corresponds to the position of the number 3 in original text.

You might be wondering about the odd construction for **within\_text** in the find function:

    B5&"0123456789"
    

This part of the formula concatenates every possible number 0-9 with the original text in B5. Unfortunately, FIND doesn't return zero when a value isn't found, so this is just a clever way to avoid errors that could occur when a number isn't found.

In this example, since we are assuming that the number will always appear _second_ in the original text, it works well because MIN forces only the smallest, or _first_ occurrence, of a number to be returned. As long as a number _does_ appear in the original text, that position will be returned.

If original text doesn't contain any numbers, a "bogus" position equal to the length of the original text + 1 will be returned. With this bogus position, the LEFT formula above will still return the text and RIGHT formula will return an [empty string](https://exceljet.net/glossary/empty-string)
 ("").

Related formulas
----------------

[![Excel formula: Split numbers from units of measure](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20numbers%20and%20units.png "Excel formula: Split numbers from units of measure")](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

### [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

Sometimes you encounter data that mixes units directly with numbers (i.e. 8km, 12v, 7.5hrs). Unfortunately, Excel will treat the numbers in this format as text, and you won't be able to perform math operations on such values. To split a number from a unit value, you need to determine the position...

[![Excel formula: Split dimensions into two parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20dimensions%20into%20two%20parts%20-%20left.png "Excel formula: Split dimensions into two parts")](https://exceljet.net/formulas/split-dimensions-into-two-parts)

### [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)

Background A common annoyance with data is that it may be represented as text instead of numbers. This is especially common with dimensions, which may appear in one text string that includes units, for example: 50 ft x 200 ft 153 ft x 324 ft Etc. In a spreadsheet, it's a lot more convenient to have...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

[![Excel formula: Extract text between parentheses](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20text%20in%20parentheses.png "Excel formula: Extract text between parentheses")](https://exceljet.net/formulas/extract-text-between-parentheses)

### [Extract text between parentheses](https://exceljet.net/formulas/extract-text-between-parentheses)

The foundation of this formula is the MID function, which extracts a specific number of characters from text, starting at a specific location. To figure out where to start extracting text, we use this expression: SEARCH("(",B5)+1 This locates the left parentheses and adds 1 to get the position of...

[![Excel formula: Get first name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_0.png "Excel formula: Get first name from name")](https://exceljet.net/formulas/get-first-name-from-name)

### [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)

In this example, the goal is to extract the first name from names that appear in <first> <middle> <last> format, where the middle name is optional. The easiest way to do this is with the newer TEXTBEFORE function. In older versions of Excel, you can use an alternative formula...

[![Excel formula: Get last name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_0.png "Excel formula: Get last name from name")](https://exceljet.net/formulas/get-last-name-from-name)

### [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)

In this example, the goal is to extract the last name from names that appear in <first> <middle> <last> format, where the middle name is not always present. The easiest way to do this is with the newer TEXTAFTER function. In older versions of Excel, you can use a significantly...

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

Related functions
-----------------

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20complex%20formula%20step%20by%20step-thumb.png)](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

### [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

When you look at a complex formula in Excel you may be completely baffled at first glance, but all complex formulas are just small steps added together. Let me show you an example. Here we have a list of names. We want to pull out the first name from the full name. There's an Excel function called...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)
    
*   [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    
*   [Extract text between parentheses](https://exceljet.net/formulas/extract-text-between-parentheses)
    
*   [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)
    
*   [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    

### Functions

*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    

### Videos

*   [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)
    

### Links

*   [Formula by Rick Rothstein on Mr Excel](http://www.mrexcel.com/forum/excel-questions/749876-separate-text-numbers.html)
    

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