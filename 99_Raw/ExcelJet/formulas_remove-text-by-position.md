# Remove text by position - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-text-by-position

---

[Skip to main content](https://exceljet.net/formulas/remove-text-by-position#main-content)

[](https://exceljet.net/formulas/remove-text-by-position#)

*   [Previous](https://exceljet.net/formulas/remove-text-by-matching)
    
*   [Next](https://exceljet.net/formulas/remove-text-by-variable-position)
    

[Text](https://exceljet.net/formulas#Text)

Remove text by position
=======================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[REPLACE](https://exceljet.net/functions/replace-function)

![Excel formula: Remove text by position](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove%20text%20by%20position.png "Excel formula: Remove text by position")

Summary
-------

To remove text from a cell by position, you can use the [REPLACE function](https://exceljet.net/functions/replace-function)
. In the example shown, the formula in C6 is:

    =REPLACE(B6,1,24,"")
    

which replaces the first 24 characters in the text with an [empty string](https://exceljet.net/glossary/empty-string)
 ("").

Generic formula
---------------

    =REPLACE(text,start,characters,"")

Explanation 
------------

The replace function lets you replace text based on its location and length. In this case, we want to strip off the drive and path and leave only the document name. The length of this part of the string (text) is 24 and the starting position is 1, and the pattern never changes.

The REPLACE function can handle this easily, we just need to provide a cell reference (B6), a starting position (1), the number of characters to replace (24), and the text to use for the replacement (""):

    =REPLACE(B6,1,24,"")
    

For the replacement, we use an [empty string](https://exceljet.net/glossary/empty-string)
 ("") which causes REPLACE to effectively remove characters 1-24.

### Alternative with SUBSTITUTE

Since the text in this case never varies, we could also use the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 to perform the name operation:

    =SUBSTITUTE(B6,"C:\Users\dave\Documents\","")
    

Related formulas
----------------

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

[![Excel formula: Remove characters from right](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_characters_from_right.png "Excel formula: Remove characters from right")](https://exceljet.net/formulas/remove-characters-from-right)

### [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)

In this example, the goal is to remove the asterisk (\*) at the end of each text city/country name in column B. As usual, there are many ways to solve a problem like this in Excel. In the article below, we'll look at two good options. The first is a traditional formula based on the LEFT function and...

[![Excel formula: Remove first character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20first%20character.png "Excel formula: Remove first character")](https://exceljet.net/formulas/remove-first-character)

### [Remove first character](https://exceljet.net/formulas/remove-first-character)

This formula uses the REPLACE function to replace the first character in a cell with an empty string (""). The arguments for REPLACE are configured as follows: old\_text is the original value from column B start\_num is hardcoded as the number 1 num\_chars comes from column C new\_text is entered as an...

[![Excel formula: Remove text by variable position](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20text%20by%20variable%20position.png "Excel formula: Remove text by variable position")](https://exceljet.net/formulas/remove-text-by-variable-position)

### [Remove text by variable position](https://exceljet.net/formulas/remove-text-by-variable-position)

The REPLACE function will replace text by position. You can use REPLACE to remove text by providing an empty string ("") for the "new\_text" argument. In this case, we want to remove the labels that appear inside text. The labels vary in length, and include words like "Make", "Model", "Fuel economy...

[![Excel formula: Remove text by matching](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20text%20by%20matching.png "Excel formula: Remove text by matching")](https://exceljet.net/formulas/remove-text-by-matching)

### [Remove text by matching](https://exceljet.net/formulas/remove-text-by-matching)

The SUBSTITUTE function lets you replace text by matching content. In this case, we want to remove hyphens from telephone numbers. The SUBSTITUTE function can handle this easily — we just need to provide a cell reference (B6), the text to remove ("-"), and the an empty string ("") for replacement...

[![Excel formula: Remove last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20last%20word.png "Excel formula: Remove last word")](https://exceljet.net/formulas/remove-last-word)

### [Remove last word](https://exceljet.net/formulas/remove-last-word)

In this example, the goal is to remove the last word from the text strings in column B. This article explains two approaches: A modern formula based on the TEXTBEFORE function. A more traditional formula for older versions in Excel. The first option is much simpler, and you should use it if you...

Related functions
-----------------

[![Excel REPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20replace%20function.png "Excel REPLACE function")](https://exceljet.net/functions/replace-function)

### [REPLACE Function](https://exceljet.net/functions/replace-function)

The Excel REPLACE function replaces characters at a specified position in a given text string with another text string. REPLACE a good solution when the text to replace can't easily be matched, but the location is predictable.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    
*   [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)
    
*   [Remove first character](https://exceljet.net/formulas/remove-first-character)
    
*   [Remove text by variable position](https://exceljet.net/formulas/remove-text-by-variable-position)
    
*   [Remove text by matching](https://exceljet.net/formulas/remove-text-by-matching)
    
*   [Remove last word](https://exceljet.net/formulas/remove-last-word)
    

### Functions

*   [REPLACE Function](https://exceljet.net/functions/replace-function)
    

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