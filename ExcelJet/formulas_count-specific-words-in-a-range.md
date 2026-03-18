# Count specific words in a range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-specific-words-in-a-range

---

[Skip to main content](https://exceljet.net/formulas/count-specific-words-in-a-range#main-content)

[](https://exceljet.net/formulas/count-specific-words-in-a-range#)

*   [Previous](https://exceljet.net/formulas/count-specific-words-in-a-cell)
    
*   [Next](https://exceljet.net/formulas/count-total-characters-in-a-cell)
    

[Text](https://exceljet.net/formulas#Text)

Count specific words in a range
===============================

by Dave Bruns · Updated 1 Oct 2017

Related functions 
------------------

[LEN](https://exceljet.net/functions/len-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[UPPER](https://exceljet.net/functions/upper-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count specific words in a range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/exceljet_count_specific_words_in_range.png "Excel formula: Count specific words in a range")

Summary
-------

To count how many times a specific a word (or any substring) appears inside a range of cells, you can use a formula based on the SUBSTITUTE, LEN, and SUMPRODUCT functions. In the example shown, the formula in C11 is:

    =SUMPRODUCT((LEN(B5:B8)-LEN(SUBSTITUTE(B5:B8,C2,"")))/LEN(C2))
    

Note: The formula on this page counts i_nstances of a word_ in a range. For example, if a cell contains two instances of a word, it will contribute 2 to the total count. If you just want to count _cells that contain a specific word_, [see this simple formula based on the COUNTIF function](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
.

Generic formula
---------------

    =SUMPRODUCT((LEN(rng)-LEN(SUBSTITUTE(rng,txt,"")))/LEN(txt))

Explanation 
------------

In the generic version of the formula, **rng** represents the range to check, and **txt** is the word or substring to count.

In the example shown, B5:B8 is the range to check, and C2 contains the text (word or substring) to count.

For each cell in the range, SUBSTITUTE removes the substring from the original text and LEN calculates the length of the text without the substring. This number is then subtracted from the length of the original text. The result is the number of characters that were removed by SUBSTITUTE.

Then, the number of characters removed is divided by the length of the substring. So, if a substring or word is 5 characters long, and there are 10 characters missing after it's been removed from the original text, we know the substring/word appeared twice in the original text.

Because the above calculation is wrapped in the SUMPRODUCT function, the result is an array that contains a number for each cell in the range. These numbers represent the number of occurrences of the substring in each cell. For this example, the array looks like this: {1;1;0;1}

Finally, SUMPRODUCT sums together all items in the array to get the total occurrences of substring in the range of cells.

### Ignoring case

SUBSTITUTE is a case-sensitive function, so it will match case when running a substitution. If you need to count both upper and lower case occurrences of a word or substring, use the UPPER function inside SUBSTITUTE to convert the text to uppercase before running the substitution:

    =SUMPRODUCT((LEN(rng)-LEN(SUBSTITUTE((UPPER(rng)),UPPER(txt),"")))/LEN(txt))
    

Related formulas
----------------

[![Excel formula: Count cells equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to.png "Excel formula: Count cells equal to")](https://exceljet.net/formulas/count-cells-equal-to)

### [Count cells equal to](https://exceljet.net/formulas/count-cells-equal-to)

In this example, the goal is to count cells equal to a specific value. In this case, we want to count cells that contain "red" in the range D5:D16. This problem can be solved with the COUNTIF function and the SUMPRODUCT function, as explained below. COUNTIF function One way to solve this problem is...

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

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

*   [Count cells equal to](https://exceljet.net/formulas/count-cells-equal-to)
    
*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)
    
*   [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)
    

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