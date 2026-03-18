# Count total words in a range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-total-words-in-a-range

---

[Skip to main content](https://exceljet.net/formulas/count-total-words-in-a-range#main-content)

[](https://exceljet.net/formulas/count-total-words-in-a-range#)

*   [Previous](https://exceljet.net/formulas/count-total-words-in-a-cell)
    
*   [Next](https://exceljet.net/formulas/double-quotes-inside-a-formula)
    

[Text](https://exceljet.net/formulas#Text)

Count total words in a range
============================

by Dave Bruns · Updated 23 Jun 2015

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[LEN](https://exceljet.net/functions/len-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[TRIM](https://exceljet.net/functions/trim-function)

![Excel formula: Count total words in a range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/exceljet_count_words_in_range.png "Excel formula: Count total words in a range")

Summary
-------

If you want to count the total words in a range of cells, you can do with a formula that uses LEN and SUBSTITUTE, along with the SUMPRODUCT function. In the generic form of the formula above, rng represents a range of cells that contain words.

In the example above, we are using:

    =SUMPRODUCT(LEN(TRIM(B3:B7))-LEN(SUBSTITUTE(B3:B7," ",""))+1)
    

Generic formula
---------------

    =SUMPRODUCT(LEN(TRIM(rng))-LEN(SUBSTITUTE(rng," ",""))+1)

Explanation 
------------

For each cell in the range, SUBSTITUTE removes all spaces from the text, then LEN calculates the length of the text without spaces. This number is then subtracted from the length of the text with spaces, and the number 1 is added to the final result, since the number of words is the number of spaces + 1. We're using TRIM to remove any extra spaces between words, or at the beginning or end of the text.

The result of all this calculation is a list of items, where there is one item per cell in the range, and each item a number based on the calculation above. In other words, we have a list of word counts, with one word count per cell.

SUMPRODUCT then sums this list and returns a total for all cells in the range.

Note that the formula inside SUMPRODUCT will return 1 even if a cell is empty. If you need to guard against this problem, you can add another array to SUMPRODUCT as below. The double hyphen coerces the result to 1's and 0's. We use TRIM again to make sure we don't count cells that have one or more spaces.

    =SUMPRODUCT((LEN(TRIM(B3:B7))-LEN(SUBSTITUTE(B3:B7," ",""))+1),--(TRIM(B3:B7)<>""))
    

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

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

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [TRIM Function](https://exceljet.net/functions/trim-function)
    

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