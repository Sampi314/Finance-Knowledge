# Remove unwanted characters - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-unwanted-characters

---

[Skip to main content](https://exceljet.net/formulas/remove-unwanted-characters#main-content)

[](https://exceljet.net/formulas/remove-unwanted-characters#)

*   [Previous](https://exceljet.net/formulas/remove-text-by-variable-position)
    
*   [Next](https://exceljet.net/formulas/replace-one-character-with-another)
    

[Text](https://exceljet.net/formulas#Text)

Remove unwanted characters
==========================

by Dave Bruns · Updated 2 Mar 2023

Related functions 
------------------

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[CHAR](https://exceljet.net/functions/char-function)

[CODE](https://exceljet.net/functions/code-function)

[LEFT](https://exceljet.net/functions/left-function)

[CLEAN](https://exceljet.net/functions/clean-function)

![Excel formula: Remove unwanted characters](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove%20unwanted%20characters.png "Excel formula: Remove unwanted characters")

Summary
-------

To remove specific unwanted characters in Excel, you can use a formula based on the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
. In the example shown, the formula in C4 is:

    =SUBSTITUTE(B4,CHAR(202),"")
    

Which removes a series of 4 invisible characters at the start of each cell in column B.

Generic formula
---------------

    =SUBSTITUTE(B4,CHAR(code),"")

Explanation 
------------

The [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 can find and replace text in a cell, wherever it occurs. In this case, we are using SUBSTITUTE to find a character with code number 202, and replace it with an [empty string](https://exceljet.net/glossary/empty-string)
 (""), which effectively removes the character completely.

How can you figure out which character(s) need to be removed, when they are invisible? To get the unique code number for the first character in a cell, you can use a formula based on the [CODE](https://exceljet.net/functions/code-function)
 and [LEFT](https://exceljet.net/functions/left-function)
 functions:

    =CODE(LEFT(B4))
    

Here, the LEFT function, without the optional second argument, returns the first character on the left. This goes into the CODE function, which reports the characters code value, which is 202 in the example shown.

For more general cleaning, see the [TRIM function](https://exceljet.net/functions/trim-function)
 and the [CLEAN function](https://exceljet.net/functions/clean-function)
.

### All in one formula

In this case, since we are stripping leading characters, we could combine both formulas in one, like so:

    =SUBSTITUTE(B4,CHAR(CODE(LEFT(B4))),"")
    

Here, instead of providing character 202 explicitly to SUBSTITUTE, we are using CODE and CHAR to provide a code dynamically, using the first character in the cell.

Related formulas
----------------

[![Excel formula: Clean and reformat telephone numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/clean_and_reformat_telephone_numbers.png "Excel formula: Clean and reformat telephone numbers")](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

### [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

In this example, the goal is to clean up telephone numbers with inconsistent formatting and then reformat the numbers in the same way. In practice, this means we need to start by removing the extra non-numeric characters, including spaces, dashes, periods, and parentheses. Once these characters are...

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

[![Excel formula: Strip html from text or numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip%20html%20from%20text%20or%20numbers.png "Excel formula: Strip html from text or numbers")](https://exceljet.net/formulas/strip-html-from-text-or-numbers)

### [Strip html from text or numbers](https://exceljet.net/formulas/strip-html-from-text-or-numbers)

The MID function returns characters using a fixed starting point and ending point. In this case, the markup consists of the html bold tag, which appears at the start of each cell and the associated closing tag, which appears at the end. The MID function has been configured to always start at 4,...

[![Excel formula: Remove leading and trailing spaces from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20leading%20and%20trailing%20spaces.png "Excel formula: Remove leading and trailing spaces from text")](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

### [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

The TRIM function is fully automatic. It removes both leading and trailing spaces from text strings, and also "normalizes" multiple spaces between words to one space character only. All you need to do is supply a reference to a cell. TRIM with CLEAN If you also need to remove line breaks from cells...

Related functions
-----------------

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel CHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")](https://exceljet.net/functions/char-function)

### [CHAR Function](https://exceljet.net/functions/char-function)

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

[![Excel CODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20code%20function.png "Excel CODE function")](https://exceljet.net/functions/code-function)

### [CODE Function](https://exceljet.net/functions/code-function)

The Excel CODE function returns a numeric code for a given character.  For example, CODE("a") returns the code 97....

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel CLEAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20clean%20function.png "Excel CLEAN function")](https://exceljet.net/functions/clean-function)

### [CLEAN Function](https://exceljet.net/functions/clean-function)

The Excel CLEAN function takes a text string and returns text that has been "cleaned" of line breaks and other non-printable characters.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20CHAR%20and%20CODE%20functions-thumb.png)](https://exceljet.net/videos/how-to-use-char-and-code-functions)

### [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)

Each character you see displayed in Excel has a number. Excel has two functions that work with these numbers directly: CODE and CHAR (Character). Let's look first at the CODE function . The CODE function accepts one argument, which is the text for which you'd like a numeric code. If I use CODE with...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    
*   [Strip html from text or numbers](https://exceljet.net/formulas/strip-html-from-text-or-numbers)
    
*   [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)
    

### Functions

*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [CHAR Function](https://exceljet.net/functions/char-function)
    
*   [CODE Function](https://exceljet.net/functions/code-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [CLEAN Function](https://exceljet.net/functions/clean-function)
    

### Videos

*   [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)
    

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