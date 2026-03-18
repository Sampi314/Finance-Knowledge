# Remove first character - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-first-character

---

[Skip to main content](https://exceljet.net/formulas/remove-first-character#main-content)

[](https://exceljet.net/formulas/remove-first-character#)

*   [Previous](https://exceljet.net/formulas/remove-file-extension-from-filename)
    
*   [Next](https://exceljet.net/formulas/remove-last-word)
    

[Text](https://exceljet.net/formulas#Text)

Remove first character
======================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[REPLACE](https://exceljet.net/functions/replace-function)

[RIGHT](https://exceljet.net/functions/right-function)

[LEN](https://exceljet.net/functions/len-function)

[LEFT](https://exceljet.net/functions/left-function)

![Excel formula: Remove first character](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove%20first%20character.png "Excel formula: Remove first character")

Summary
-------

To remove the first character in a cell, you can use the [REPLACE function](https://exceljet.net/functions/replace-function)
. In the example shown, the formula in D5 is:

    =REPLACE(A1,1,1,"")
    

Generic formula
---------------

    =REPLACE(A1,1,N,"")

Explanation 
------------

This formula uses the REPLACE function to replace the first character in a cell with an [empty string](https://exceljet.net/glossary/empty-string)
 (""). The arguments for REPLACE are configured as follows:

*   **old\_text** is the original value from column B
*   **start\_num** is hardcoded as the number 1
*   **num\_chars** comes from column C
*   **new\_text** is entered as an empty string ("")

The behavior or REPLACE is automatic. With these inputs, the REPLACE function replaces the first character in B5 with an empty string and returns the result.

### Removing N characters

To always remove just the first character, simply hardcode both the start number and number of characters like this:

    =REPLACE(A1,1,1,"")
    

To remove the first N characters from a text value, use the generic form of the formula:

    =REPLACE(A1,1,N,"")
    

where N represents the number of characters to remove.

### With RIGHT and LEFT

You can also use the RIGHT, LEFT, and LEN functions to remove the first character from a cell. The general form of the formula is:

    =RIGHT(text,LEN(text)-N)
    

where N is the number of characters to remove. In this formula, the RIGHT function is used to extract characters from the _right,_ up to (but not including), the characters being removed from the left. In the example shown, the formula in D5 would be:

    =RIGHT(B5,LEN(B5)-C5)
    

The LEN function returns the number of characters in cell B5, from which the value in C5 is subtracted. The result is used by RIGHT to extract the correct number of characters from the RIGHT.

### Getting a numeric value

The formulas above will always return text, even when the result contains numbers only. To get a numeric result, you can add zero like this:

    =REPLACE(A1,1,1,"")+0
    

The math operation causes Excel to coerce the text to numbers. This only works when the value returned by RIGHT contains just numbers.

Related formulas
----------------

[![Excel formula: Remove characters from right](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_characters_from_right.png "Excel formula: Remove characters from right")](https://exceljet.net/formulas/remove-characters-from-right)

### [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)

In this example, the goal is to remove the asterisk (\*) at the end of each text city/country name in column B. As usual, there are many ways to solve a problem like this in Excel. In the article below, we'll look at two good options. The first is a traditional formula based on the LEFT function and...

[![Excel formula: Split text and numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20text%20and%20numbers.png "Excel formula: Split text and numbers")](https://exceljet.net/formulas/split-text-and-numbers)

### [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)

Overview The formula looks complex, but the mechanics are in fact quite simple. As with most formulas that split or extract text, the key is to locate the position of the thing you are looking for. Once you have the position, you can use other functions to extract what you need. In this case, we...

[![Excel formula: Split numbers from units of measure](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20numbers%20and%20units.png "Excel formula: Split numbers from units of measure")](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

### [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

Sometimes you encounter data that mixes units directly with numbers (i.e. 8km, 12v, 7.5hrs). Unfortunately, Excel will treat the numbers in this format as text, and you won't be able to perform math operations on such values. To split a number from a unit value, you need to determine the position...

[![Excel formula: Remove leading and trailing spaces from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20leading%20and%20trailing%20spaces.png "Excel formula: Remove leading and trailing spaces from text")](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

### [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

The TRIM function is fully automatic. It removes both leading and trailing spaces from text strings, and also "normalizes" multiple spaces between words to one space character only. All you need to do is supply a reference to a cell. TRIM with CLEAN If you also need to remove line breaks from cells...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

Related functions
-----------------

[![Excel REPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20replace%20function.png "Excel REPLACE function")](https://exceljet.net/functions/replace-function)

### [REPLACE Function](https://exceljet.net/functions/replace-function)

The Excel REPLACE function replaces characters at a specified position in a given text string with another text string. REPLACE a good solution when the text to replace can't easily be matched, but the location is predictable.

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20combine%20functions%20in%20a%20formula-thumb.png)](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)

### [How to combine functions in a formula](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)

In this video I'm going to show you how you can use multiple Excel functions to split, manipulate, and rejoin values inside a single formula. Here we have some sample data and, in column B, we have text values with a number at the end. What we want to do is increment these numbers using the value...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20clean%20text%20with%20CLEAN%20and%20TRIM-thumb.png)](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

### [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

When you bring data into Excel you sometimes end up with extra spaces and other characters that cause problems. Excel contains two functions that can help you clean things up. Let's take a look. Here we have a list of movie titles that were copied in from some other system. You can see that there's...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)
    
*   [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)
    
*   [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)
    
*   [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    

### Functions

*   [REPLACE Function](https://exceljet.net/functions/replace-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    

### Videos

*   [How to combine functions in a formula](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)
    
*   [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)
    

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