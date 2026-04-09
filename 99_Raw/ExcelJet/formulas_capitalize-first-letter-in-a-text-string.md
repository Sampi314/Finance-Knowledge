# Capitalize first letter in a text string - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string

---

[Skip to main content](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string#main-content)

[](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string#)

*   [Previous](https://exceljet.net/formulas/add-line-break-based-on-os)
    
*   [Next](https://exceljet.net/formulas/cell-begins-with)
    

[Text](https://exceljet.net/formulas#Text)

Capitalize first letter in a text string
========================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[REPLACE](https://exceljet.net/functions/replace-function)

[UPPER](https://exceljet.net/functions/upper-function)

[LEFT](https://exceljet.net/functions/left-function)

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8128/download?token=fQsnrfD4)
 (14.72 KB)

![Excel formula: Capitalize first letter in a text string](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/capitalize_first_letter.png "Excel formula: Capitalize first letter in a text string")

Summary
-------

To capitalize the first letter in a text string, you can use a formula based on the [REPLACE function](https://exceljet.net/functions/replace-function)
, the [UPPER function](https://exceljet.net/functions/upper-function)
, and the [LEFT function](https://exceljet.net/functions/left-function)
. In the example shown, the formula in D5 is:

    =REPLACE(B5,1,1,UPPER(LEFT(B5)))
    

As the formula is copied down, it returns each sentence in column B with the first letter capitalized. All other letters in the sentence remain unchanged.

Generic formula
---------------

    =REPLACE(A1,1,1,UPPER(LEFT(A1)))

Explanation 
------------

_One of the most important skills to learn with Excel formulas is the concept of nesting. Put simply, nesting just means putting one function inside another. Nesting is super useful, but it does take some practice. You have to learn to read a formula from the inside out. The formulas below are good examples of nesting. Practice reading the formulas starting with the innermost functions._

In this example, the goal is to capitalize the first letter in a text string with a formula in Excel. This involves a bit of creative thinking because Excel does not offer a built-in function to capitalize only the first letter in a text string, unlike many other languages. This article explains a few approaches to the problem, including the formula featured in the worksheet above.

### What about the PROPER function?

The simplest way to capitalize the first letter in a text string is to use the [PROPER function](https://exceljet.net/functions/proper-function)
, which is designed to capitalize words. For example, if we give PROPER the word "apple", PROPER returns "Apple":

    =PROPER("apple") // returns "Apple"

This works very nicely for a single word or a person's name. However, it won't work in the worksheet shown because PROPER will capitalize _all words_. For example, If we give PROPER the text string "an apple a day", we get back "An Apple A Day":

    =PROPER("an apple a day") // returns "An Apple A Day"

PROPER is a handy function, but not well suited to this problem. We need a different approach.

### LEFT, UPPER, MID, and LEN

Another solution to this problem is to take a more literal approach: extract the first letter in the text string, capitalize it, and then concatenate the result to the remaining characters. This can be done with the formula below, which is based on four separate functions - LEFT, UPPER, MID, and LEN:

    =UPPER(LEFT(B5))&MID(B5,2,LEN(B5)-1)

This is an example of _nesting_ functions in Excel. Notice that the LEFT function is nested inside UPPER, and the LEN function is nested inside the MID function. The way to read nested functions is from the inside out:

1.  The LEFT function grabs the first letter.
2.  The UPPER function capitalizes the first letter.
3.  The LEN function calculates the length of the sentence.
4.  The MID function uses the length to get all remaining characters.
5.  The results from #2 and #4 are joined with [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
    .

The first expression uses the [LEFT function](https://exceljet.net/functions/left-function)
 to extract the first letter and the [UPPER function](https://exceljet.net/functions/upper-function)
 to capitalize the first letter:

    =UPPER(LEFT(B5))
    

> Note that there is no need to enter 1 for _num\_chars_ in LEFT since it is an optional argument that defaults to 1.

Since cell B5 contains the text string "perfect is the enemy of good", this part of the formula evaluates like this:

    =UPPER(LEFT(B5))
    =UPPER(LEFT("perfect is the enemy of good"))
    =UPPER("p")
    ="P"
    

The second expression extracts the remaining characters with the [MID function](https://exceljet.net/functions/mid-function)
:

    MID(B5,2,LEN(B5)-1)
    

The text comes from B5, the start number is hardcoded as 2, and _num\_chars_ is provided by subtracting 1 from the result of the [LEN function](https://exceljet.net/functions/len-function)
, which becomes 28:

    =MID(B5,2,LEN(B5)-1)
    =MID(B5,2,29-1))
    =MID(B5,2,28))
    ="erfect is the enemy of good"
    

> We subtract 1 because we have already dealt with the first character in the text string. However, MID won't complain if we ask for more characters than exist (it will simply extract everything), so technically we could omit the subtraction step and the formula will still return the same result.

Finally, the result from the first expression is joined to the result from the second expression with [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
 by using the ampersand (&) operator:

    =UPPER(LEFT(B5))&MID(B5,2,LEN(B5)-1)
    ="P"&"erfect is the enemy of good"
    ="Perfect is the enemy of good"

This formula works fine for the problem as stated: it will capitalize the first letter of the sentence and leave all remaining characters unchanged. But do we need four functions to perform this task? Can't we do better?

Yes, we can. If we move to a formula based on the REPLACE function...

### The REPLACE function

The [REPLACE function](https://exceljet.net/functions/replace-function)
 is designed to replace one or more characters in a text string specified by location with another text string. For example, we can replace the last 3 letters in "ABCDEF" with "XYZ" like this:

    =REPLACE("ABCDEF",4,3,"XYZ") // returns "ABCXYZ"

The arguments for REPLACE are provided as follows:

*   _old\_text_ - "ABCDEF"
*   _start\_num_ - 4
*   _num\_chars_ - 3
*   _new\_text_ - "XYZ"

In other words, REPLACE swaps three characters starting at character 4 with "XYZ". We can use the REPLACE function to solve this problem by replacing the first letter with a capitalized version of itself. This is the approach seen in the worksheet shown, where the formula in cell D5 is:

    =REPLACE(B5,1,1,UPPER(LEFT(B5)))

Again, we have a great example of nesting. Notice that the LEFT function is nested inside the UPPER function which is itself nested inside the REPLACE function:

1.  The LEFT function grabs the first letter.
2.  The UPPER function capitalizes the first letter.
3.  The REPLACE function replaces the first letter with a capitalized version.

The formula evaluates like this:

    =REPLACE(B5,1,1,UPPER(LEFT(B5)))
    =REPLACE(B5,1,1,UPPER(LEFT("perfect is the enemy of good.")))
    =REPLACE(B5,1,1,UPPER("p"))
    =REPLACE(B5,1,1,"P")
    ="Perfect is the enemy of good."

Compared to the previous formula, this formula only needs three functions and doesn't require concatenation at all. The REPLACE does the work of replacing the first letter in place, leaving all remaining characters unaffected.

_Note: If you do want to force all remaining characters to be lowercase, see the modification below._

### Lowercase all the rest

If you want to lowercase everything but the first letter, just wrap the text given to REPLACE in the [LOWER function](https://exceljet.net/functions/lower-function)
 like this

    =REPLACE(LOWER(B5),1,1,UPPER(LEFT(B5)))

The formula will work the same as before. The only difference is that the REPLACE function will begin with an entirely lowercase text string.

Related formulas
----------------

[![Excel formula: Remove leading and trailing spaces from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20leading%20and%20trailing%20spaces.png "Excel formula: Remove leading and trailing spaces from text")](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

### [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

The TRIM function is fully automatic. It removes both leading and trailing spaces from text strings, and also "normalizes" multiple spaces between words to one space character only. All you need to do is supply a reference to a cell. TRIM with CLEAN If you also need to remove line breaks from cells...

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

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

Related functions
-----------------

[![Excel REPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20replace%20function.png "Excel REPLACE function")](https://exceljet.net/functions/replace-function)

### [REPLACE Function](https://exceljet.net/functions/replace-function)

The Excel REPLACE function replaces characters at a specified position in a given text string with another text string. REPLACE a good solution when the text to replace can't easily be matched, but the location is predictable.

[![Excel UPPER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20upper%20function.png "Excel UPPER function")](https://exceljet.net/functions/upper-function)

### [UPPER Function](https://exceljet.net/functions/upper-function)

The Excel UPPER function converts a text string to all uppercase letters. Numbers, punctuation, and spaces are not affected.

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20complex%20formula%20step%20by%20step-thumb.png)](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

### [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

When you look at a complex formula in Excel you may be completely baffled at first glance, but all complex formulas are just small steps added together. Let me show you an example. Here we have a list of names. We want to pull out the first name from the full name. There's an Excel function called...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20change%20case%20with%20UPPER%2C%20LOWER%20and%20PROPER-thumb.png)](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

### [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

When you're working with text in Excel, you'll frequently need to change case. In this video we'll look at three functions that allow you to easily change case of text in Excel: UPPER, LOWER, and PROPER. In this worksheet, we have two columns that contain names. Column B contains last names in...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)
    
*   [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    
*   [Extract text between parentheses](https://exceljet.net/formulas/extract-text-between-parentheses)
    
*   [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    

### Functions

*   [REPLACE Function](https://exceljet.net/functions/replace-function)
    
*   [UPPER Function](https://exceljet.net/functions/upper-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

### Videos

*   [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)
    
*   [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)
    

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