# Excel CLEAN function | Exceljet

**Source:** https://exceljet.net/functions/clean-function

---

[Skip to main content](https://exceljet.net/functions/clean-function#main-content)

[](https://exceljet.net/functions/clean-function#)

*   [Previous](https://exceljet.net/functions/char-function)
    
*   [Next](https://exceljet.net/functions/code-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

CLEAN Function
==============

by Dave Bruns · Updated 2 Mar 2023

Related functions 
------------------

[TRIM](https://exceljet.net/functions/trim-function)

![Excel CLEAN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20clean%20function.png "Excel CLEAN function")

Summary
-------

The Excel CLEAN function takes a text string and returns text that has been "cleaned" of line breaks and other non-printable characters.

Purpose 
--------

Strip non-printable characters from text

Return value 
-------------

Text with non-printable characters removed.

Syntax
------

    =CLEAN(text)

*   _text_ - The text to clean.

Using the CLEAN function 
-------------------------

The CLEAN function accepts a text string and returns text that has been "cleaned" of line breaks and other non-printable characters. You can use CLEAN to strip non-printing characters and strip line breaks from text. For example, to clean text in cell A1:

    =CLEAN(A1) // clean text in A1
    

The CLEAN function accepts just one argument, text, which can be a [text string](https://exceljet.net/glossary/text-value)
 or number. CLEAN removes the first 32 non-printable characters in the 7-bit ASCII code (values 0 through 31), if any are found, and returns the result. Text without these characters is returned unchanged. Note that CLEAN _will_ remove line breaks if found.

CLEAN will not remove extra space characters. To remove extra space, use the [TRIM function](https://exceljet.net/functions/trim-function)
. You can use CLEAN and TRIM together in one formula like this:

    =TRIM(CLEAN(A1)) // clean and remove extra space
    

### ASCII limitation

The CLEAN function removes the first 32 (non-printable) characters in the 7-bit ASCII code (values 0 through 31) from text. Unicode contains other non-printable characters that are not removed. To remove specific characters beyond the first 32 ASCII characters, you can use the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 with the [CHAR function](https://exceljet.net/functions/char-function)
. For example to remove character 202:

    =SUBSTITUTE(A1,CHAR(202),"") // remove character 202
    

You can use the [CODE function](https://exceljet.net/functions/code-function)
 to determine the number for a problematic character, then use that number inside CHAR to return the character in a formula. See [this page](https://exceljet.net/formulas/remove-unwanted-characters)
 for more information.

CLEAN function examples
-----------------------

[![Excel formula: Remove unwanted characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20unwanted%20characters.png "Excel formula: Remove unwanted characters")](https://exceljet.net/formulas/remove-unwanted-characters)

### [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)

The SUBSTITUTE function can find and replace text in a cell, wherever it occurs. In this case, we are using SUBSTITUTE to find a character with code number 202, and replace it with an empty string (""), which effectively removes the character completely. How can you figure out which character(s)...

[![Excel formula: Remove leading and trailing spaces from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20leading%20and%20trailing%20spaces.png "Excel formula: Remove leading and trailing spaces from text")](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

### [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

The TRIM function is fully automatic. It removes both leading and trailing spaces from text strings, and also "normalizes" multiple spaces between words to one space character only. All you need to do is supply a reference to a cell. TRIM with CLEAN If you also need to remove line breaks from cells...

[![Excel formula: Remove line breaks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20line%20breaks.png "Excel formula: Remove line breaks")](https://exceljet.net/formulas/remove-line-breaks)

### [Remove line breaks](https://exceljet.net/formulas/remove-line-breaks)

First, you should know that Excel contains two functions, CLEAN and TRIM, that can automatically remove line breaks and extra spaces from text. For example to strip all line breaks from a cell, you could use: =CLEAN(B5) For a quick demo of CLEAN and TRIM, watch this video . In this case, however,...

CLEAN function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20clean%20text%20with%20CLEAN%20and%20TRIM-thumb.png)](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

### [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

When you bring data into Excel you sometimes end up with extra spaces and other characters that cause problems. Excel contains two functions that can help you clean things up. Let's take a look. Here we have a list of movie titles that were copied in from some other system. You can see that there's...

Related functions
-----------------

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

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
    
*   [Remove line breaks](https://exceljet.net/formulas/remove-line-breaks)
    
*   [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)
    

### Videos

*   [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)
    

### Functions

*   [TRIM Function](https://exceljet.net/functions/trim-function)
    

### Links

*   [Microsoft CLEAN function documentation](https://support.office.com/en-us/article/clean-function-26f3d7c5-475f-4a9c-90e5-4b8ba987ba41)
    

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