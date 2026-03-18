# Count total characters in a cell - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-total-characters-in-a-cell

---

[Skip to main content](https://exceljet.net/formulas/count-total-characters-in-a-cell#main-content)

[](https://exceljet.net/formulas/count-total-characters-in-a-cell#)

*   [Previous](https://exceljet.net/formulas/count-specific-words-in-a-range)
    
*   [Next](https://exceljet.net/formulas/count-total-characters-in-a-range)
    

[Text](https://exceljet.net/formulas#Text)

Count total characters in a cell
================================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: Count total characters in a cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20total%20characters%20in%20a%20cell.png "Excel formula: Count total characters in a cell")

Summary
-------

To count the total characters in a cell, you can use the [LEN function](https://exceljet.net/functions/len-function)
. In the example shown, the formula in cell C5, copied down, is:

    =LEN(B5)
    

The result in C5 is 3, which is the total number of characters in cell B5.

Generic formula
---------------

    =LEN(a1)

Explanation 
------------

The LEN function is fully automatic. In the example, the formula in the active cell is:

    =LEN(B5)
    

The LEN function simply counts all characters that appear in a cell. All characters are counted, including space characters, as you can see in cell C9.

### Numbers

Numbers in Excel (including dates, times, currency, etc.) are often formatted with a [number format](https://exceljet.net/articles/custom-number-formats)
. It's important to understand that the characters that makeup numbers are counted in their raw form (i.e. number formatting is not included). For example, because [Excel dates are serial numbers](https://exceljet.net/glossary/excel-date)
, the result in cell C11 is 5, since the date in B11 is actually the number 42005.

Related formulas
----------------

[![Excel formula: Count total characters in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_characters_in_cell.png "Excel formula: Count total characters in a range")](https://exceljet.net/formulas/count-total-characters-in-a-range)

### [Count total characters in a range](https://exceljet.net/formulas/count-total-characters-in-a-range)

SUMPRODUCT accepts the range B3:B6 as an array of four cells. For each cell in the array, LEN calculates the length of the text as a number. The result is an array that contains 4 numbers. SUMPRODUCT then sums the items in this array and returns the total.

[![Excel formula: Count specific characters in text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_specific_characters_in_text.png "Excel formula: Count specific characters in text string")](https://exceljet.net/formulas/count-specific-characters-in-text-string)

### [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)

In this example, the goal is to count the number of occurrences of a character in a cell or text string. Strangely, Excel does not have a function dedicated to counting characters, so we need to use a formula that computes a count manually. The typical way to do this is to use a formula based on...

Related functions
-----------------

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count total characters in a range](https://exceljet.net/formulas/count-total-characters-in-a-range)
    
*   [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)
    

### Functions

*   [LEN Function](https://exceljet.net/functions/len-function)
    

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