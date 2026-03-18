# Remove line breaks - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-line-breaks

---

[Skip to main content](https://exceljet.net/formulas/remove-line-breaks#main-content)

[](https://exceljet.net/formulas/remove-line-breaks#)

*   [Previous](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)
    
*   [Next](https://exceljet.net/formulas/remove-text-by-matching)
    

[Text](https://exceljet.net/formulas#Text)

Remove line breaks
==================

by Dave Bruns · Updated 19 Sep 2020

Related functions 
------------------

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[CLEAN](https://exceljet.net/functions/clean-function)

![Excel formula: Remove line breaks](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove%20line%20breaks.png "Excel formula: Remove line breaks")

Summary
-------

To remove line breaks from a cell, or from text inside a formula, you can use a formula based on the SUBSTITUTE and CHAR functions. In the example shown, the formula in C5 is:

    =SUBSTITUTE(B5,CHAR(10),", ")
    

which replaces line breaks in B5 with commas.

Generic formula
---------------

    =SUBSTITUTE(A1,CHAR(10),", ")

Explanation 
------------

First, you should know that Excel contains two functions, CLEAN and TRIM, that can automatically remove line breaks and extra spaces from text. For example to strip all line breaks from a cell, you could use:

    =CLEAN(B5)
    

For a quick demo of CLEAN and TRIM, [watch this video](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
.

In this case, however, we are removing line breaks and _replacing them with commas_, so we are using the SUBSTITUTE function instead of CLEAN. SUBSTITUTE can locate matching text anywhere in a cell, and replace it with the text of your choice. SUBSTITUTE can accept up to four arguments, but we are using only the first three like this:

    =SUBSTITUTE(B5,CHAR(10),", ")
    

The text comes from cell B5.

The "old text" is entered as CHAR(10). This will match a line break character in a cell.

The "new text" is entered as ", ". This translates to a comma plus one space. We need the quotes because this is a text value.

SUBSTITUTE then replaces all line breaks in the cell with commas and returns the final result as text in C5. Because "old text" is an argument, you can change the comma to any other text you like.

Related formulas
----------------

[![Excel formula: Count line breaks in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20line%20breaks%20in%20cell.png "Excel formula: Count line breaks in cell")](https://exceljet.net/formulas/count-line-breaks-in-cell)

### [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)

First, the LEN function counts total characters in the cell B5. Next SUBSTITUTE removes all "line returns" from the text in B5 by looking for CHAR(10) which is the character code for the return character in Windows. LEN returns the result inside of a second LEN, which counts characters without...

[![Excel formula: Extract multiple lines from a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20multiple%20lines%20from%20a%20cell.png "Excel formula: Extract multiple lines from a cell")](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

### [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

At the core, this formula looks for a line delimiter ("delim") and replaces it with a large number of spaces using the SUBSTITUTE and REPT functions. Note: In older versions of Excel on a Mac, use CHAR(13) instead of CHAR(10). The CHAR function returns a character based on it's numeric code. The...

[![Excel formula: Remove unwanted characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20unwanted%20characters.png "Excel formula: Remove unwanted characters")](https://exceljet.net/formulas/remove-unwanted-characters)

### [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)

The SUBSTITUTE function can find and replace text in a cell, wherever it occurs. In this case, we are using SUBSTITUTE to find a character with code number 202, and replace it with an empty string (""), which effectively removes the character completely. How can you figure out which character(s)...

[![Excel formula: Remove text by matching](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20text%20by%20matching.png "Excel formula: Remove text by matching")](https://exceljet.net/formulas/remove-text-by-matching)

### [Remove text by matching](https://exceljet.net/formulas/remove-text-by-matching)

The SUBSTITUTE function lets you replace text by matching content. In this case, we want to remove hyphens from telephone numbers. The SUBSTITUTE function can handle this easily — we just need to provide a cell reference (B6), the text to remove ("-"), and the an empty string ("") for replacement...

[![Excel formula: Normalize text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/normalize%20text.png "Excel formula: Normalize text")](https://exceljet.net/formulas/normalize-text)

### [Normalize text](https://exceljet.net/formulas/normalize-text)

The formula shown in this example uses a series of nested SUBSTITUTE functions to strip out parentheses, hyphens, colons, semi-colons, exclamation marks, commas, and periods. The process runs from the inside out, with each SUBSTITUTE replacing one character with a single space, then handing off to...

[![Excel formula: Clean and reformat telephone numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/clean_and_reformat_telephone_numbers.png "Excel formula: Clean and reformat telephone numbers")](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

### [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

In this example, the goal is to clean up telephone numbers with inconsistent formatting and then reformat the numbers in the same way. In practice, this means we need to start by removing the extra non-numeric characters, including spaces, dashes, periods, and parentheses. Once these characters are...

Related functions
-----------------

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel CLEAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20clean%20function.png "Excel CLEAN function")](https://exceljet.net/functions/clean-function)

### [CLEAN Function](https://exceljet.net/functions/clean-function)

The Excel CLEAN function takes a text string and returns text that has been "cleaned" of line breaks and other non-printable characters.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20clean%20text%20with%20CLEAN%20and%20TRIM-thumb.png)](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

### [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

When you bring data into Excel you sometimes end up with extra spaces and other characters that cause problems. Excel contains two functions that can help you clean things up. Let's take a look. Here we have a list of movie titles that were copied in from some other system. You can see that there's...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20concatenate%20with%20line%20breaks-thumb.png)](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)

### [How to concatenate with line breaks](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)

In the real world, you often need to concatenate values in a way that includes line breaks and other punctuation. In this video we'll look at a clever way to make this task easier and less error-prone. A common example of a situation that requires concatenation is assembling a mailing address from...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)
    
*   [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)
    
*   [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)
    
*   [Remove text by matching](https://exceljet.net/formulas/remove-text-by-matching)
    
*   [Normalize text](https://exceljet.net/formulas/normalize-text)
    
*   [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
    

### Functions

*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [CLEAN Function](https://exceljet.net/functions/clean-function)
    

### Videos

*   [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)
    
*   [How to concatenate with line breaks](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)
    

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