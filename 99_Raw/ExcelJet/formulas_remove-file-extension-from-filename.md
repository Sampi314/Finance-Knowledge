# Remove file extension from filename - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-file-extension-from-filename

---

[Skip to main content](https://exceljet.net/formulas/remove-file-extension-from-filename#main-content)

[](https://exceljet.net/formulas/remove-file-extension-from-filename#)

*   [Previous](https://exceljet.net/formulas/remove-characters-from-right)
    
*   [Next](https://exceljet.net/formulas/remove-first-character)
    

[Text](https://exceljet.net/formulas#Text)

Remove file extension from filename
===================================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[LEFT](https://exceljet.net/functions/left-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Remove file extension from filename](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove%20file%20extension%20from%20filename.png "Excel formula: Remove file extension from filename")

Summary
-------

To remove a file extension from a file name, you can use a formula based on the [LEFT](https://exceljet.net/functions/left-function)
 and [FIND](https://exceljet.net/functions/find-function)
 functions. In the example shown, the formula in C5 is:

    =LEFT(B5,FIND(".",B5)-1)
    

Generic formula
---------------

    =LEFT(filename,FIND(".",filename)-1)

Explanation 
------------

The core of this formula is the LEFT function which simply extracts text from the file name, starting at the left, and ending at the character before the first period (".").

    =LEFT(filename,characters)
    

The FIND function is used to figure out how many characters to extract:

    FIND(".",B5)-1
    

Find returns the position of the first match (6 in the first example) from which 1 is subtracted. The result, 5, goes into LEFT like this:

    =LEFT(B5,5)
    

and the LEFT function returns the first five characters from the left: "Happy".

_Note: because this formula finds the first occurrence of ".", it will remove all file extensions when there is more than one._

Related formulas
----------------

[![Excel formula: Remove text by position](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20text%20by%20position.png "Excel formula: Remove text by position")](https://exceljet.net/formulas/remove-text-by-position)

### [Remove text by position](https://exceljet.net/formulas/remove-text-by-position)

The replace function lets you replace text based on its location and length. In this case, we want to strip off the drive and path and leave only the document name. The length of this part of the string (text) is 24 and the starting position is 1, and the pattern never changes. The REPLACE function...

[![Excel formula: Remove first character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20first%20character.png "Excel formula: Remove first character")](https://exceljet.net/formulas/remove-first-character)

### [Remove first character](https://exceljet.net/formulas/remove-first-character)

This formula uses the REPLACE function to replace the first character in a cell with an empty string (""). The arguments for REPLACE are configured as follows: old\_text is the original value from column B start\_num is hardcoded as the number 1 num\_chars comes from column C new\_text is entered as an...

[![Excel formula: Remove characters from right](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_characters_from_right.png "Excel formula: Remove characters from right")](https://exceljet.net/formulas/remove-characters-from-right)

### [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)

In this example, the goal is to remove the asterisk (\*) at the end of each text city/country name in column B. As usual, there are many ways to solve a problem like this in Excel. In the article below, we'll look at two good options. The first is a traditional formula based on the LEFT function and...

Related functions
-----------------

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

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
    
*   [Remove first character](https://exceljet.net/formulas/remove-first-character)
    
*   [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)
    

### Functions

*   [LEFT Function](https://exceljet.net/functions/left-function)
    
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