# Count specific words in a cell - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-specific-words-in-a-cell

---

[Skip to main content](https://exceljet.net/formulas/count-specific-words-in-a-cell#main-content)

[](https://exceljet.net/formulas/count-specific-words-in-a-cell#)

*   [Previous](https://exceljet.net/formulas/count-specific-characters-in-text-string)
    
*   [Next](https://exceljet.net/formulas/count-specific-words-in-a-range)
    

[Text](https://exceljet.net/formulas#Text)

Count specific words in a cell
==============================

by Dave Bruns · Updated 4 Jan 2022

Related functions 
------------------

[LEN](https://exceljet.net/functions/len-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[UPPER](https://exceljet.net/functions/upper-function)

![Excel formula: Count specific words in a cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/exceljet_count_words_1.png "Excel formula: Count specific words in a cell")

Summary
-------

If you need to count how many times a specific a word (or any substring) appears inside a cell, you can use a formula that uses [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
 and [LEN](https://exceljet.net/functions/len-function)
. In the generic form of the formula above, "text" represents a cell that contains text, and "word" represents the word or substring being counted. In the example, we are using this formula:

    =(LEN(B4)-LEN(SUBSTITUTE(B4,C4,"")))/LEN(C4)
    

Generic formula
---------------

    =(LEN(text)-LEN(SUBSTITUTE(text,word,"")))/LEN(word)

Explanation 
------------

B4 is the cell we're counting words in, and C4 contains the substring (word or any substring) you are counting.

SUBSTITUTE removes the substring from the original text and LEN calculates the length of the text without the substring. This number is then subtracted from the length of the original text. The result is the number of characters that were removed by SUBSTITUTE.

Finally, the number of characters removed is divided by the length of the substring. So, if a substring is 5 characters long, and there are 10 characters missing after it's been removed from the original text, we know the substring appeared twice in the original text.

### Handling case

SUBSTITUTE is a case-sensitive function, so it will match case when running a substitution. If you need to count both upper and lower case occurrences of a word or substring, use the UPPER function inside SUBSTITUTE to convert the text to uppercase before running the substitution:

    =(LEN(B4)-LEN(SUBSTITUTE(UPPER(B4),UPPER(C4),"")))/LEN(C4)
    

Because this formula converts the substring and the text to uppercase before performing the substitution, it will work equally well with text in any case.

### Normalizing text

Counting words in Excel is tricky because Excel doesn't support regular expressions. As a result, it's difficult to target the words you want to count exactly, while ignoring substrings and other partial matches (i.e. find "fox " but not "foxes"). Punctuation and case variations make this problem quite challenging.

One workaround is to use [another formula](https://exceljet.net/formulas/normalize-text)
 in a [helper column](https://exceljet.net/glossary/helper-column)
 to "normalize text" as a first step. Then use the formula on this page to count words wrapped in space characters to get an accurate count (i.e. you can look for " fox " in the normalized text.

_Note: this approach is only as good as the normalized text you are able to create, and you might need to adjust the normalizing formula many times to get the result you need._

Related formulas
----------------

[![Excel formula: Count specific characters in text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_specific_characters_in_text.png "Excel formula: Count specific characters in text string")](https://exceljet.net/formulas/count-specific-characters-in-text-string)

### [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)

In this example, the goal is to count the number of occurrences of a character in a cell or text string. Strangely, Excel does not have a function dedicated to counting characters, so we need to use a formula that computes a count manually. The typical way to do this is to use a formula based on...

[![Excel formula: Count specific words in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_specific_words_in_range.png "Excel formula: Count specific words in a range")](https://exceljet.net/formulas/count-specific-words-in-a-range)

### [Count specific words in a range](https://exceljet.net/formulas/count-specific-words-in-a-range)

In the generic version of the formula, rng represents the range to check, and txt is the word or substring to count. In the example shown, B5:B8 is the range to check, and C2 contains the text (word or substring) to count. For each cell in the range, SUBSTITUTE removes the substring from the...

[![Excel formula: Count specific characters in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_specific_characters_in_range.png "Excel formula: Count specific characters in a range")](https://exceljet.net/formulas/count-specific-characters-in-a-range)

### [Count specific characters in a range](https://exceljet.net/formulas/count-specific-characters-in-a-range)

For each cell in the range, SUBSTITUTE removes all the o's from the text, then LEN calculates the length of the text without o's. This number is then subtracted from the length of the text with o's. Because we are using SUMPRODUCT, the result of all this calculation is a list of items (an array),...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

Related functions
-----------------

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel UPPER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20upper%20function.png "Excel UPPER function")](https://exceljet.net/functions/upper-function)

### [UPPER Function](https://exceljet.net/functions/upper-function)

The Excel UPPER function converts a text string to all uppercase letters. Numbers, punctuation, and spaces are not affected.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)
    
*   [Count specific words in a range](https://exceljet.net/formulas/count-specific-words-in-a-range)
    
*   [Count specific characters in a range](https://exceljet.net/formulas/count-specific-characters-in-a-range)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    

### Functions

*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [UPPER Function](https://exceljet.net/functions/upper-function)
    

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