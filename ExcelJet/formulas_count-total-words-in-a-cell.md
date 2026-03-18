# Count total words in a cell - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-total-words-in-a-cell

---

[Skip to main content](https://exceljet.net/formulas/count-total-words-in-a-cell#main-content)

[](https://exceljet.net/formulas/count-total-words-in-a-cell#)

*   [Previous](https://exceljet.net/formulas/count-total-characters-in-a-range)
    
*   [Next](https://exceljet.net/formulas/count-total-words-in-a-range)
    

[Text](https://exceljet.net/formulas#Text)

Count total words in a cell
===========================

by Dave Bruns · Updated 8 Jan 2024

Related functions 
------------------

[LEN](https://exceljet.net/functions/len-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[TRIM](https://exceljet.net/functions/trim-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8130/download?token=PNFLL79T)
 (17.29 KB)

![Excel formula: Count total words in a cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count_total_words_in_cell.png "Excel formula: Count total words in a cell")

Summary
-------

To count the total words in a cell, you can use a formula based on the [TEXTSPLIT](https://exceljet.net/functions/textsplit-function)
 and [COUNTA](https://exceljet.net/functions/counta-function)
 functions, with help from the [TRIM function](https://exceljet.net/functions/trim-function)
. In the example shown, the formula in cell D5, copied down, is:

    =COUNTA(TEXTSPLIT(TRIM(B5)," "))
    

The result in cell D5 is 6. As the formula is copied down, it returns the word counts for each Title as seen in column B.

Generic formula
---------------

    =COUNTA(TEXTSPLIT(TRIM(A1)," "))

Explanation 
------------

In this example, the goal is to count the total number of words in a cell. Excel doesn't have a dedicated function for counting words. However, with a little ingenuity, you can create a formula to perform this task using a combination of built-in functions. In newer versions of Excel, the best approach is to use the TEXTSPLIT and COUNTA functions. In older versions of Excel, you can use a more complicated formula based on the SUBSTITUTE and LEN functions. Both formulas use the TRIM function to clean up the source text before counting words, and both formulas are explained in detail below. This is a great example of how newer functions in Excel are simplifying older more complex formulas. While the older SUBSTITUTE option does work, it works indirectly and is not very intuitive. The TEXTSPLIT option is logical and straightforward; it just makes sense.

### TEXTSPLIT option

In newer versions of Excel, the best approach is to use the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 in a formula like this:

    =COUNTA(TEXTSPLIT(TRIM(B5)," "))

At a high level, this formula works in three distinct and logical steps:

1.  Clean up the text with TRIM (remove extra space)
2.  Create a list of words with TEXTSPLIT
3.  Count the words in the list with COUNTA

Working from the inside out, the [TRIM function](https://exceljet.net/functions/trim-function)
 is used first to remove any extra spaces:

    TRIM(B5) // remove extra spaces

TRIM will convert any runs of spaces into a single space, and remove any leading or trailing space characters. Next, TRIM returns the trimmed text directly to the TEXTSPLIT function as the text argument:

    TEXTSPLIT("All Quiet on the Western Front"," ")

The delimiter in TEXTSPLIT is provided as a single space (" ") since words are separated by spaces. The result from TEXTSPLIT is an array that contains the six words in the title cell B5. This array is returned directly to the [COUNTA function](https://exceljet.net/functions/counta-function)
 like this:

    =COUNTA({"All","Quiet","on","the","Western","Front"})

The COUNTA function will count both numbers and text. Because the array from TEXTSPLIT contains six words, COUNTA returns a final result of 6. As the formula is copied down, it returns a word count for each title in column B.

### Handling empty cells

If a cell is empty, or when a cell contains only space characters, TRIM will return an empty string (""). Unfortunately, the TEXTSPLIT function will return a #CALC! error if the source text is an empty text string and the COUNTA function will count the #CALC! error and return the incorrect result of 1. Consequently, we need a way to prevent the formula from returning 1 if blank or empty cells are a possibility. One way to handle this situation is to use a modified version of the formula like this:

    =IF(TRIM(B5)="",0,COUNTA(TEXTSPLIT(TRIM(B5)," ")))

Here, we first check for an empty cell (or a cell that contains only space) with the [IF function](https://exceljet.net/functions/if-function)
 and the TRIM function. If the result from TRIM is an empty string (""), IF simply returns 0 as a final result. Otherwise, IF runs the original formula which returns a word count as explained above.

### Adjusting delimiters

The formula in the example above assumes that words are delimited by spaces only. If you are working with text words separated by other delimiters, you will need to adjust the delimiters provided to TEXTSPLIT as needed. For example, to count words that may be separated by spaces, commas, or hyphens, you can use a modified formula like this:

    =COUNTA(TEXTSPLIT(TRIM(B5),{" ",",","-"},,1))

Here, we are providing the three delimiters as an array constant like this:

    {" ",",","-"}

TEXTSPLIT will split the incoming text when it encounters _any_ of these delimiters. In addition, we have set the _ignore\_empty_ argument in TEXTSPLIT to 1 (TRUE) to remove empty strings ("") that can be generated by consecutive delimiters that contain no content. We do this because COUNTA will (for some reason) count empty strings ("") as values. You would think that =COUNTA("") would return zero, but in fact, it returns 1. As a result, we need to remove empty values _before_ they are evaluated by COUNTA.

### Older versions of Excel

Older versions of Excel don't have the TEXTSPLIT function to work with, so they don't support the formula explained above. However, you can use a more complicated formula based on the [LEN](https://exceljet.net/functions/len-function)
 and [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
 functions, with help from the TRIM function like this:

    =LEN(TRIM(B5))-LEN(SUBSTITUTE(B5," ",""))+1
    

At a high level, this formula uses the LEN function to count the number of characters in the cell, with and without spaces, then uses the difference to figure out the word count:

1.  Clean up the text with TRIM
2.  Count characters in the result with LEN
3.  Remove all space characters with SUBSTITUTE
4.  Count characters in the result with LEN
5.  Subtract the second count from the first count
6.  Add 1 to get a final word count

This works because word count is equal to the number of spaces + 1, but it's a messy non-intuitive process.

The first part of the formula counts the characters in cell B5, after cleaning up spaces:

    =LEN(TRIM(B5)) // normalize space, count characters
    

Inside LEN, the [TRIM function](https://exceljet.net/functions/trim-function)
 removes any extra spaces between words, or at the beginning or end of the text. This is important since any extra spaces will throw off the word count. TRIM returns the trimmed text directly to the [LEN function](https://exceljet.net/functions/len-function)
:

    LEN("All Quiet on the Western Front") // returns 30
    

Since the text in cell B5 does not contain extra space characters, the text delivered by TRIM is unchanged and the result from LEN is 30. At this point, we have:

    =30-LEN(SUBSTITUTE(B5," ",""))+1
    

Next, we use the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 to remove _all space characters_ from the text:

    SUBSTITUTE(B5," ","") // strip all space
    

Notice SUBSTITUTE is configured to replace a single space character (" ") with an [empty string](https://exceljet.net/glossary/empty-string)
 (""). By default, SUBSTITUTE will replace _all_ spaces. The result is delivered to the LEN function, which returns the count:

    LEN("AllQuietontheWesternFront") // returns 25
    

LEN returns 25, the number of characters remaining _after all space has been removed_. We can now simplify the formula to the following:

    =30-25+1 // returns 6
    

The final result is 6 which is the number of words in cell B5. Notice we need to add 1 at the end because we are counting spaces between words, and there will always be one less space than there are words. However, this step can cause a problem with empty or blank cells, as explained below.

### Dealing with blank cells

The code explained above will return 1 even if a cell is empty, or contains only space. This happens because we are adding 1 _unconditionally_ to the result, which only makes sense if we have at least one word. To guard against this problem, you can adapt the formula as shown below:

    =LEN(TRIM(B5))-LEN(SUBSTITUTE(B5," ",""))+(TRIM(B5)<>"")
    

Notice this is the original formula except that we've replaced +1 with an expression:

    +(TRIM(B5)<>"")

This code first trims the text in cell B5, then it tests to see if the result is _not empty._ If TRIM returns actual text, the expression returns TRUE. If TRIM returns an empty string (""), because B5 is empty, or contains only space, the result is FALSE. The trick here is that Excel evaluates TRUE as 1 and FALSE as 0 when they are involved in any math operation. As a result, the expression adds 1 when there _is text_ in B5 and adds 0 if the cell is empty or contains only space.

Related formulas
----------------

[![Excel formula: Cell contains specific words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_words.png "Excel formula: Cell contains specific words")](https://exceljet.net/formulas/cell-contains-specific-words)

### [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)

In this example, the goal is to test the text in a cell and return TRUE if it contains one or more specific words, and FALSE if not. Notice the emphasis here is on words, not substrings. For example, if we are testing for the word "green" and the text contains the word "evergreen" but not the word...

[![Excel formula: Count total words in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_words_in_range.png "Excel formula: Count total words in a range")](https://exceljet.net/formulas/count-total-words-in-a-range)

### [Count total words in a range](https://exceljet.net/formulas/count-total-words-in-a-range)

For each cell in the range, SUBSTITUTE removes all spaces from the text, then LEN calculates the length of the text without spaces. This number is then subtracted from the length of the text with spaces, and the number 1 is added to the final result, since the number of words is the number of...

[![Excel formula: Count specific words in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_specific_words_in_range.png "Excel formula: Count specific words in a range")](https://exceljet.net/formulas/count-specific-words-in-a-range)

### [Count specific words in a range](https://exceljet.net/formulas/count-specific-words-in-a-range)

In the generic version of the formula, rng represents the range to check, and txt is the word or substring to count. In the example shown, B5:B8 is the range to check, and C2 contains the text (word or substring) to count. For each cell in the range, SUBSTITUTE removes the substring from the...

[![Excel formula: Count specific characters in text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_specific_characters_in_text.png "Excel formula: Count specific characters in text string")](https://exceljet.net/formulas/count-specific-characters-in-text-string)

### [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)

In this example, the goal is to count the number of occurrences of a character in a cell or text string. Strangely, Excel does not have a function dedicated to counting characters, so we need to use a formula that computes a count manually. The typical way to do this is to use a formula based on...

[![Excel formula: Count specific words in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_words_1.png "Excel formula: Count specific words in a cell")](https://exceljet.net/formulas/count-specific-words-in-a-cell)

### [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)

B4 is the cell we're counting words in, and C4 contains the substring (word or any substring) you are counting. SUBSTITUTE removes the substring from the original text and LEN calculates the length of the text without the substring. This number is then subtracted from the length of the original...

Related functions
-----------------

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

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

*   [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)
    
*   [Count total words in a range](https://exceljet.net/formulas/count-total-words-in-a-range)
    
*   [Count specific words in a range](https://exceljet.net/formulas/count-specific-words-in-a-range)
    
*   [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)
    
*   [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)
    

### Functions

*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [TRIM Function](https://exceljet.net/functions/trim-function)
    

### Videos

*   [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)
    

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