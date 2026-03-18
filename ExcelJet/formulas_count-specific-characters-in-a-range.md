# Count specific characters in a range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-specific-characters-in-a-range

---

[Skip to main content](https://exceljet.net/formulas/count-specific-characters-in-a-range#main-content)

[](https://exceljet.net/formulas/count-specific-characters-in-a-range#)

*   [Previous](https://exceljet.net/formulas/count-numbers-in-text-string)
    
*   [Next](https://exceljet.net/formulas/count-specific-characters-in-text-string)
    

[Text](https://exceljet.net/formulas#Text)

Count specific characters in a range
====================================

by Dave Bruns · Updated 29 Nov 2015

Related functions 
------------------

[LEN](https://exceljet.net/functions/len-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[UPPER](https://exceljet.net/functions/upper-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count specific characters in a range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/exceljet_count_specific_characters_in_range.png "Excel formula: Count specific characters in a range")

Summary
-------

If you need to count specific characters in a range of cells, you can do so with a formula that uses LEN and SUBSTITUTE, along with the SUMPRODUCT function. In the generic form of the formula (above), **rng** represents a range of cells that contain words and **txt** represents the character you need to count.

In the example, the active cell contains this formula:

    =SUMPRODUCT(LEN(B3:B7)-LEN(SUBSTITUTE(B3:B7,"o","")))
    

Generic formula
---------------

    =SUMPRODUCT(LEN(rng)-LEN(SUBSTITUTE(rng,txt,"")))

Explanation 
------------

For each cell in the range, SUBSTITUTE removes all the o's from the text, then LEN calculates the length of the text without o's. This number is then subtracted from the length of the text with o's.

Because we are using SUMPRODUCT, the result of all this calculation is a list of items (an array), where there is one item per cell in the range, and each item a number based on the calculation described above. In other words, we have a list of character counts, with one character count per cell.

SUMPRODUCT then sums the numbers in this list and returns a total for all cells in the range.

SUBSTITUTE is a case-sensitive function, so it will match case when performing a substitution. If you need to count both upper and lower case occurrences of a specific character, use the UPPER function inside SUBSTITUTE to convert the text to uppercase before the substitution occurs. Then supply an uppercase character for the text that's being counted.

The modified generic form of the formula looks like this:

    =SUMPRODUCT(LEN(rng)-LEN(SUBSTITUTE(UPPER(rng),TXT,"")))
    

Related formulas
----------------

[![Excel formula: Count specific characters in text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_specific_characters_in_text.png "Excel formula: Count specific characters in text string")](https://exceljet.net/formulas/count-specific-characters-in-text-string)

### [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)

In this example, the goal is to count the number of occurrences of a character in a cell or text string. Strangely, Excel does not have a function dedicated to counting characters, so we need to use a formula that computes a count manually. The typical way to do this is to use a formula based on...

[![Excel formula: Count specific words in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_words_1.png "Excel formula: Count specific words in a cell")](https://exceljet.net/formulas/count-specific-words-in-a-cell)

### [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)

B4 is the cell we're counting words in, and C4 contains the substring (word or any substring) you are counting. SUBSTITUTE removes the substring from the original text and LEN calculates the length of the text without the substring. This number is then subtracted from the length of the original...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Count specific words in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_specific_words_in_range.png "Excel formula: Count specific words in a range")](https://exceljet.net/formulas/count-specific-words-in-a-range)

### [Count specific words in a range](https://exceljet.net/formulas/count-specific-words-in-a-range)

In the generic version of the formula, rng represents the range to check, and txt is the word or substring to count. In the example shown, B5:B8 is the range to check, and C2 contains the text (word or substring) to count. For each cell in the range, SUBSTITUTE removes the substring from the...

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

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

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
    
*   [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Count specific words in a range](https://exceljet.net/formulas/count-specific-words-in-a-range)
    

### Functions

*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [UPPER Function](https://exceljet.net/functions/upper-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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