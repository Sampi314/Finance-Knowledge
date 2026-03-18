# Replace one character with another - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/replace-one-character-with-another

---

[Skip to main content](https://exceljet.net/formulas/replace-one-character-with-another#main-content)

[](https://exceljet.net/formulas/replace-one-character-with-another#)

*   [Previous](https://exceljet.net/formulas/remove-unwanted-characters)
    
*   [Next](https://exceljet.net/formulas/replace-one-delimiter-with-another)
    

[Text](https://exceljet.net/formulas#Text)

Replace one character with another
==================================

by Dave Bruns · Updated 22 Oct 2023

Related functions 
------------------

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

![Excel formula: Replace one character with another](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/replace%20one%20character%20with%20another.png "Excel formula: Replace one character with another")

Summary
-------

To replace or substitute all occurrences of one character with another character, you can use the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
. In the example shown, the formula in C6 is:

    =SUBSTITUTE(B6," ","-")
    

Generic formula
---------------

    =SUBSTITUTE(ref,old,new)

Explanation 
------------

The SUBSTITUTE function is full automatic. All you need to do is supply "old text" and "new text". SUBSTITUTE will replace every instance of the old text with the new text.

If you need to perform more than one replacement at the same time, you'll need to nest multiple SUBSTITUTE functions. See this "[clean telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
" formula for an example.

If you need to replace a character at a specific location, see the [REPLACE function](https://exceljet.net/functions/replace-function)
.

Related formulas
----------------

[![Excel formula: Clean and reformat telephone numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/clean_and_reformat_telephone_numbers.png "Excel formula: Clean and reformat telephone numbers")](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

### [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

In this example, the goal is to clean up telephone numbers with inconsistent formatting and then reformat the numbers in the same way. In practice, this means we need to start by removing the extra non-numeric characters, including spaces, dashes, periods, and parentheses. Once these characters are...

Related functions
-----------------

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
    

### Functions

*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    

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