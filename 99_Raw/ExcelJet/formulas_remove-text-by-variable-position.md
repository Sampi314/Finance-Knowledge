# Remove text by variable position - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-text-by-variable-position

---

[Skip to main content](https://exceljet.net/formulas/remove-text-by-variable-position#main-content)

[](https://exceljet.net/formulas/remove-text-by-variable-position#)

*   [Previous](https://exceljet.net/formulas/remove-text-by-position)
    
*   [Next](https://exceljet.net/formulas/remove-unwanted-characters)
    

[Text](https://exceljet.net/formulas#Text)

Remove text by variable position
================================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[REPLACE](https://exceljet.net/functions/replace-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Remove text by variable position](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove%20text%20by%20variable%20position.png "Excel formula: Remove text by variable position")

Summary
-------

To remove text from a cell, when the text is at a variable position, you can use a formula based on the [REPLACE function](https://exceljet.net/functions/replace-function)
, with help from the [FIND function](https://exceljet.net/functions/find-function)
. In the example shown, the formula in C6 is:

    =REPLACE(B6,1,FIND(":",B6)+1,"")
    

which removes all text up to and including the colon (:) and following space.

Generic formula
---------------

    =REPLACE(text,start,FIND(marker,text)+1,"")

Explanation 
------------

The REPLACE function will replace text by position. You can use REPLACE to remove text by providing an [empty string](https://exceljet.net/glossary/empty-string)
 ("") for the "new\_text" argument.

In this case, we want to remove the labels that appear inside text. The labels vary in length, and include words like "Make", "Model", "Fuel economy", and so on. Each label is followed by a colon and a space. We can use the colon as a "marker" to figure out where the label ends.

Working from the inside out, we use the FIND function to get the position of the colon in the text, then add 1 to take into account the space that follows the colon. The result (a number) is plugged into the REPLACE function for the "num\_chars" argument, which represents the number of characters to replace.

The REPLACE function then replaces the text from 1 to "colon + 1" with an empty string (""). In the example shown, the solution looks like this:

    =REPLACE(B6,1,FIND(":",B6)+1,"")
    =REPLACE(B6,1,6,"")
    =2016
    

Related formulas
----------------

[![Excel formula: Remove text by position](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20text%20by%20position.png "Excel formula: Remove text by position")](https://exceljet.net/formulas/remove-text-by-position)

### [Remove text by position](https://exceljet.net/formulas/remove-text-by-position)

The replace function lets you replace text based on its location and length. In this case, we want to strip off the drive and path and leave only the document name. The length of this part of the string (text) is 24 and the starting position is 1, and the pattern never changes. The REPLACE function...

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

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

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
    
*   [Remove text by matching](https://exceljet.net/formulas/remove-text-by-matching)
    
*   [Remove last word](https://exceljet.net/formulas/remove-last-word)
    

### Functions

*   [REPLACE Function](https://exceljet.net/functions/replace-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

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