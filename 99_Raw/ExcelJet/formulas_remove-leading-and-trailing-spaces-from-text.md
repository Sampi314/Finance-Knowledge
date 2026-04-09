# Remove leading and trailing spaces from text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text

---

[Skip to main content](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text#main-content)

[](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text#)

*   [Previous](https://exceljet.net/formulas/remove-last-word)
    
*   [Next](https://exceljet.net/formulas/remove-line-breaks)
    

[Text](https://exceljet.net/formulas#Text)

Remove leading and trailing spaces from text
============================================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[CLEAN](https://exceljet.net/functions/clean-function)

[TRIM](https://exceljet.net/functions/trim-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

![Excel formula: Remove leading and trailing spaces from text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove%20leading%20and%20trailing%20spaces.png "Excel formula: Remove leading and trailing spaces from text")

Summary
-------

If you need to strip leading and trailing spaces from text in one or more cells, you can use the TRIM function. In the example show, the formula in cell C3 is:

    =TRIM(B3)
    

Once you've removed extra spaces, you can copy the cells with formulas and paste special elsewhere as "values" to get the final text.

Video: [How to clean text with TRIM and CLEAN](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

Generic formula
---------------

    =TRIM(text)

Explanation 
------------

The TRIM function is fully automatic. It removes both leading and trailing spaces from text strings, and also "normalizes" multiple spaces between words to one space character only. All you need to do is supply a reference to a cell.

### TRIM with CLEAN

If you also need to remove line breaks from cells, you can add the CLEAN function like so:

    =TRIM(CLEAN(text))
    

The CLEAN function removes a range of non-printing characters, including line breaks, and returns "cleaned" text. The TRIM function then takes over to remove extra spaces and returns the final text.

### Other problematic characters

Note that CLEAN cannot remove all non-printing characters, notably a non-breaking space, which can appear in Excel as CHAR(160). By adding the SUBSTITUTE function to the formula, you can remove specific characters. For example, to remove a non-breaking space, you can use:

    =TRIM(CLEAN(SUBSTITUTE(B1,CHAR(160)," ")))
    

Related formulas
----------------

[![Excel formula: Clean and reformat telephone numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/clean_and_reformat_telephone_numbers.png "Excel formula: Clean and reformat telephone numbers")](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

### [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

In this example, the goal is to clean up telephone numbers with inconsistent formatting and then reformat the numbers in the same way. In practice, this means we need to start by removing the extra non-numeric characters, including spaces, dashes, periods, and parentheses. Once these characters are...

[![Excel formula: Remove unwanted characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20unwanted%20characters.png "Excel formula: Remove unwanted characters")](https://exceljet.net/formulas/remove-unwanted-characters)

### [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)

The SUBSTITUTE function can find and replace text in a cell, wherever it occurs. In this case, we are using SUBSTITUTE to find a character with code number 202, and replace it with an empty string (""), which effectively removes the character completely. How can you figure out which character(s)...

Related functions
-----------------

[![Excel CLEAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20clean%20function.png "Excel CLEAN function")](https://exceljet.net/functions/clean-function)

### [CLEAN Function](https://exceljet.net/functions/clean-function)

The Excel CLEAN function takes a text string and returns text that has been "cleaned" of line breaks and other non-printable characters.

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

Related videos
--------------

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

*   [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
    
*   [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)
    

### Functions

*   [CLEAN Function](https://exceljet.net/functions/clean-function)
    
*   [TRIM Function](https://exceljet.net/functions/trim-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    

### Videos

*   [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)
    

### Links

*   [Cleaning "Dirty" Data (Ron de Bruin)](http://www.rondebruin.nl/win/s9/win017.htm)
    

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