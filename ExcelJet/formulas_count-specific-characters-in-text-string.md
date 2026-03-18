# Count specific characters in text string - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-specific-characters-in-text-string

---

[Skip to main content](https://exceljet.net/formulas/count-specific-characters-in-text-string#main-content)

[](https://exceljet.net/formulas/count-specific-characters-in-text-string#)

*   [Previous](https://exceljet.net/formulas/count-specific-characters-in-a-range)
    
*   [Next](https://exceljet.net/formulas/count-specific-words-in-a-cell)
    

[Text](https://exceljet.net/formulas#Text)

Count specific characters in text string
========================================

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[LEN](https://exceljet.net/functions/len-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[LOWER](https://exceljet.net/functions/lower-function)

![Excel formula: Count specific characters in text string](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count_specific_characters_in_text.png "Excel formula: Count specific characters in text string")

Summary
-------

To count the number of occurrences of a character in a text string, you can use a formula based on the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 and the [LEN function](https://exceljet.net/functions/len-function)
. In the example shown, the formula in cell D5 is:

    =LEN(B5)-LEN(SUBSTITUTE(B5,"a",""))
    

As the formula is copied down, it returns a count of the letter "a" in each text string in column B. Note that this formula _is case-sensitive_. See below for a version of the formula that _is not case-sensitive_.

Generic formula
---------------

    =LEN(A1)-LEN(SUBSTITUTE(A1,"a",""))

Explanation 
------------

In this example, the goal is to count the number of occurrences of a character in a cell or text string. Strangely, Excel does not have a function dedicated to counting characters, so we need to use a formula that computes a count manually. The typical way to do this is to use a formula based on the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 and the [LEN function](https://exceljet.net/functions/len-function)
.

### LEN Function

The LEN function calculates the number of characters in a text string. For example, given the text "amanda", LEN returns 6 since there are 6 characters total:

    =LEN("amanda") // returns 6
    

For more details, see [How to use the LEN function](https://exceljet.net/functions/len-function)
.

### SUBSTITUTE Function

The SUBSTITUTE function performs substitutions in a text string. For example, the formula below replaces each "a" in "Amanda" with an empty string (""):

    =SUBSTITUTE("amanda","a","") // returns "mnd"
    

The result is "mnd" since all 3 "a"s are replaced with "". However, note that SUBSTITUTE is case-sensitive, so if we provide the text "Amanda", only two of the a's are replaced:

    =SUBSTITUTE("Amanda","a","") // returns "Amnd"
    

For more details, see [How to use the SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
.

### LEN + SUBSTITUTE

The LEN and SUBSTITUTE functions can be combined to count a specific character in a text string. The idea is to calculate the length of the original text string, then subtract the length of the text string after removing all occurrences of the character. In the example shown, the formula in cell D5 is:

    =LEN(B5)-LEN(SUBSTITUTE(B5,"a",""))
    

This formula counts the number of a's that appear in cell B5. Notice the LEN function is used twice. The first LEN calculates the length of the original text string. The second LEN calculates the length of the text after all a's have been removed with the SUBSTITUTE function. Next, the result from the second LEN is subtracted from the result from the first LEN. The final result is the number of a's removed by SUBSTITUTE, which is equal to the count of a's in the original text. For example, with the text "banana" in cell A1, the formula calculates like this:

    =LEN(A1)-LEN(SUBSTITUTE(A1,"a",""))
    =LEN("banana")-LEN(SUBSTITUTE("banana","a",""))
    =LEN("banana")-LEN("bnn")
    =6-3
    =3
    

Note that this formula _is case-sensitive by default_ because the SUBSTITUTE function is case-sensitive. This means an uppercase "A" will not be counted. See below for an option that is not case-sensitive.

### Case-insensitive option

SUBSTITUTE is a case-sensitive function, so it will match the case when replacing text. This means that the original formula above will not count the "A" in cell B9, because SUBSTITUTE is configured to look for lowercase "a". If you need a _case-insensitive count_, one solution is to add the [LOWER function](https://exceljet.net/functions/lower-function)
 to the formula like this:

    =LEN(B5)-LEN(SUBSTITUTE(LOWER(B5),"a",""))
    

In this formula, the LOWER function runs first to convert all text to lowercase. The result is returned to SUBSTITUTE, and the formula then runs as before. All uppercase A's in the text are now lowercase, so they _will_ be included in the count. The screen below shows the result:

![Counting occurrences of characters in text - not case-sensitive](https://exceljet.net/sites/default/files/images/formulas/inline/count_specific_characters_in_text_not_case-sensitive.png "Counting occurrences of characters in text - not case-sensitive")

Notice that the count is now higher in cases where the text in column B includes an uppercase "A" that was previously not counted.

_Note: although we use the LOWER function in the above formula, an alternative approach is to use the_ [_UPPER function_](https://exceljet.net/functions/upper-function)
_, and then search for an uppercase "A". Both options will return the same result._

Related formulas
----------------

[![Excel formula: Count specific words in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_words_1.png "Excel formula: Count specific words in a cell")](https://exceljet.net/formulas/count-specific-words-in-a-cell)

### [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)

B4 is the cell we're counting words in, and C4 contains the substring (word or any substring) you are counting. SUBSTITUTE removes the substring from the original text and LEN calculates the length of the text without the substring. This number is then subtracted from the length of the original...

[![Excel formula: Count total characters in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20total%20characters%20in%20a%20cell.png "Excel formula: Count total characters in a cell")](https://exceljet.net/formulas/count-total-characters-in-a-cell)

### [Count total characters in a cell](https://exceljet.net/formulas/count-total-characters-in-a-cell)

The LEN function is fully automatic. In the example, the formula in the active cell is: =LEN(B5) The LEN function simply counts all characters that appear in a cell. All characters are counted, including space characters, as you can see in cell C9. Numbers Numbers in Excel (including dates, times,...

[![Excel formula: Count total characters in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_characters_in_cell.png "Excel formula: Count total characters in a range")](https://exceljet.net/formulas/count-total-characters-in-a-range)

### [Count total characters in a range](https://exceljet.net/formulas/count-total-characters-in-a-range)

SUMPRODUCT accepts the range B3:B6 as an array of four cells. For each cell in the array, LEN calculates the length of the text as a number. The result is an array that contains 4 numbers. SUMPRODUCT then sums the items in this array and returns the total.

[![Excel formula: Count specific characters in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_specific_characters_in_range.png "Excel formula: Count specific characters in a range")](https://exceljet.net/formulas/count-specific-characters-in-a-range)

### [Count specific characters in a range](https://exceljet.net/formulas/count-specific-characters-in-a-range)

For each cell in the range, SUBSTITUTE removes all the o's from the text, then LEN calculates the length of the text without o's. This number is then subtracted from the length of the text with o's. Because we are using SUMPRODUCT, the result of all this calculation is a list of items (an array),...

Related functions
-----------------

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel LOWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lower%20function.png "Excel LOWER function")](https://exceljet.net/functions/lower-function)

### [LOWER Function](https://exceljet.net/functions/lower-function)

The Excel LOWER function converts a text string to all lowercase letters. Numbers, punctuation, and spaces are not affected.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)
    
*   [Count total characters in a cell](https://exceljet.net/formulas/count-total-characters-in-a-cell)
    
*   [Count total characters in a range](https://exceljet.net/formulas/count-total-characters-in-a-range)
    
*   [Count specific characters in a range](https://exceljet.net/formulas/count-specific-characters-in-a-range)
    

### Functions

*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [LOWER Function](https://exceljet.net/functions/lower-function)
    

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