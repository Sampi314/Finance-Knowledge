# Remove text by matching - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-text-by-matching

---

[Skip to main content](https://exceljet.net/formulas/remove-text-by-matching#main-content)

[](https://exceljet.net/formulas/remove-text-by-matching#)

*   [Previous](https://exceljet.net/formulas/remove-line-breaks)
    
*   [Next](https://exceljet.net/formulas/remove-text-by-position)
    

[Text](https://exceljet.net/formulas#Text)

Remove text by matching
=======================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

![Excel formula: Remove text by matching](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove%20text%20by%20matching.png "Excel formula: Remove text by matching")

Summary
-------

To remove text from a cell based by matching content (not location), you can use the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
. In the example shown, the formula in C6 is:

    =SUBSTITUTE(B6,"-","")
    

Generic formula
---------------

    =SUBSTITUTE(B6,text_to_remove,"")

Explanation 
------------

The SUBSTITUTE function lets you replace text by matching content.

In this case, we want to remove hyphens from telephone numbers. The SUBSTITUTE function can handle this easily — we just need to provide a cell reference (B6), the text to remove ("-"), and the an [empty string](https://exceljet.net/glossary/empty-string)
 ("") for replacement text.

SUBSTITUTE will replace all instances of "-" with nothing.

_Note that SUBSTITUTE is a case-sensitive function._

### Removing more than one thing

If you need to remove more than one thing, you can nest multiple SUBSTITUTE functions. For example, to remove square brackets from text, you can use:

    =SUBSTITUTE(SUBSTITUTE(text, "[", ""), "]", "")
    

You can nest at several levels, as described in this more complex [formula to clean up telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
.

Related formulas
----------------

[![Excel formula: Remove text by position](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20text%20by%20position.png "Excel formula: Remove text by position")](https://exceljet.net/formulas/remove-text-by-position)

### [Remove text by position](https://exceljet.net/formulas/remove-text-by-position)

The replace function lets you replace text based on its location and length. In this case, we want to strip off the drive and path and leave only the document name. The length of this part of the string (text) is 24 and the starting position is 1, and the pattern never changes. The REPLACE function...

[![Excel formula: Remove leading and trailing spaces from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20leading%20and%20trailing%20spaces.png "Excel formula: Remove leading and trailing spaces from text")](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

### [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

The TRIM function is fully automatic. It removes both leading and trailing spaces from text strings, and also "normalizes" multiple spaces between words to one space character only. All you need to do is supply a reference to a cell. TRIM with CLEAN If you also need to remove line breaks from cells...

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

*   [Remove text by position](https://exceljet.net/formulas/remove-text-by-position)
    
*   [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)
    

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