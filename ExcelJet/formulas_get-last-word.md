# Get last word - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-last-word

---

[Skip to main content](https://exceljet.net/formulas/get-last-word#main-content)

[](https://exceljet.net/formulas/get-last-word#)

*   [Previous](https://exceljet.net/formulas/get-last-line-in-cell)
    
*   [Next](https://exceljet.net/formulas/get-unicode-sequence-from-text)
    

[Text](https://exceljet.net/formulas#Text)

Get last word
=============

by Dave Bruns · Updated 30 Jan 2020

Related functions 
------------------

[TRIM](https://exceljet.net/functions/trim-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[RIGHT](https://exceljet.net/functions/right-function)

[REPT](https://exceljet.net/functions/rept-function)

![Excel formula: Get last word](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20last%20word.png "Excel formula: Get last word")

Summary
-------

To get the last word from a text string, you can use a formula based on the [TRIM](https://exceljet.net/functions/trim-function)
, [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
, [RIGHT](https://exceljet.net/functions/right-function)
, and [REPT](https://exceljet.net/functions/rept-function)
 functions. In the example shown, the formula in C6 is:

    =TRIM(RIGHT(SUBSTITUTE(B6," ",REPT(" ",100)),100))
    

Which returns the word "time".

Generic formula
---------------

    =TRIM(RIGHT(SUBSTITUTE(text," ",REPT(" ",100)),100))

Explanation 
------------

This formula is an interesting example of a "brute force" approach that takes advantage of the fact that TRIM will remove _any number_ of leading spaces.

Working from the inside out, we use the SUBSTITUTE function to find all spaces in the text, and replace each space with 100 spaces:

    SUBSTITUTE(B6," ",REPT(" ",100))
    

So, for example, with the text string "one two three" the result is going to look like this:

    one----------two----------three
    

With hyphens representing spaces for readability. Keep in mind that there will be 100 spaces between each word.

Next, the RIGHT function extracts 100 characters, starting from the right. The result will look like this:

    -------three
    

Finally, the TRIM function removes all leading spaces, and returns the last word.

Note: We are using 100 arbitrarily because that should be a big enough number to handle very long words. If you have some odd situation with super long words, bump this number up as needed.

### Handling inconsistent spacing

If the text you are working with has inconsistent spacing (i.e. extra spaces between words, extra leading or trailing spaces, etc.) This formula won't work correctly. To handle this situation, add an extra TRIM function inside the substitute function like so:

    =TRIM(RIGHT(SUBSTITUTE(TRIM(B6)," ",REPT(" ",100)),100))
    

This will normalize all spaces before the main logic runs.

Related formulas
----------------

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Get first word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_first_word_1.png "Excel formula: Get first word")](https://exceljet.net/formulas/get-first-word)

### [Get first word](https://exceljet.net/formulas/get-first-word)

FIND returns the position (as a number) of the first occurrence of a space character in the text. This position, minus one, is fed into the LEFT function as num\_chars . The LEFT function then extracts characters starting at the left side of the text, up to (position - 1). Handling one word If a...

[![Excel formula: Count total words in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_total_words_in_cell.png "Excel formula: Count total words in a cell")](https://exceljet.net/formulas/count-total-words-in-a-cell)

### [Count total words in a cell](https://exceljet.net/formulas/count-total-words-in-a-cell)

In this example, the goal is to count the total number of words in a cell. Excel doesn't have a dedicated function for counting words. However, with a little ingenuity, you can create a formula to perform this task using a combination of built-in functions. In newer versions of Excel, the best...

[![Excel formula: Normalize text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/normalize%20text.png "Excel formula: Normalize text")](https://exceljet.net/formulas/normalize-text)

### [Normalize text](https://exceljet.net/formulas/normalize-text)

The formula shown in this example uses a series of nested SUBSTITUTE functions to strip out parentheses, hyphens, colons, semi-colons, exclamation marks, commas, and periods. The process runs from the inside out, with each SUBSTITUTE replacing one character with a single space, then handing off to...

Related functions
-----------------

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rept%20function.png "Excel REPT function")](https://exceljet.net/functions/rept-function)

### [REPT Function](https://exceljet.net/functions/rept-function)

The Excel REPT function repeats characters a given number of times. For example, =REPT("x",5) returns "xxxxx".

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20clean%20text%20with%20CLEAN%20and%20TRIM-thumb.png)](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

### [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

When you bring data into Excel you sometimes end up with extra spaces and other characters that cause problems. Excel contains two functions that can help you clean things up. Let's take a look. Here we have a list of movie titles that were copied in from some other system. You can see that there's...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)
    
*   [Get first word](https://exceljet.net/formulas/get-first-word)
    
*   [Count total words in a cell](https://exceljet.net/formulas/count-total-words-in-a-cell)
    
*   [Normalize text](https://exceljet.net/formulas/normalize-text)
    

### Functions

*   [TRIM Function](https://exceljet.net/functions/trim-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [REPT Function](https://exceljet.net/functions/rept-function)
    

### Videos

*   [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)
    

### Links

*   [Nice explanation on MrExcel.com by T. Valko (Biff)](http://www.mrexcel.com/forum/excel-questions/635070-formula-return-last-word-cell-2.html#post3151626)
    

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