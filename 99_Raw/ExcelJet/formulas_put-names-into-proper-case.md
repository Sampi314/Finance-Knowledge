# Put names into proper case - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/put-names-into-proper-case

---

[Skip to main content](https://exceljet.net/formulas/put-names-into-proper-case#main-content)

[](https://exceljet.net/formulas/put-names-into-proper-case#)

*   [Previous](https://exceljet.net/formulas/join-first-and-last-name)
    
*   [Next](https://exceljet.net/formulas/split-full-name-into-parts)
    

[Names](https://exceljet.net/formulas#Names)

Put names into proper case
==========================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[PROPER](https://exceljet.net/functions/proper-function)

[TRIM](https://exceljet.net/functions/trim-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

![Excel formula: Put names into proper case](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/put_names_into_proper_case.png "Excel formula: Put names into proper case")

Summary
-------

To format names in "proper case" (i.e. first letter of each name capitalized) you can use a formula based on [PROPER function](https://exceljet.net/functions/proper-function)
. In the worksheet shown, the formula in D5 is:

    =PROPER(B5)
    

As the formula is copied down, it returns each name in column B formatted in proper case.

Generic formula
---------------

    =PROPER(A1)

Explanation 
------------

The goal in this example is to reformat names that appear in mixed upper and lower case letters into "proper case", defined as each word in the name beginning with a capital letter. This can easily be done in Excel with the PROPER function.

### PROPER function

The [PROPER function](https://exceljet.net/functions/proper-function)
 automatically reformats text so that all words are capitalized. At the same time, it lowercases all other text. For example:

    =PROPER("ben franklin") // returns "Ben Franklin"
    =PROPER("ben FRANKLIN") // returns "Ben Franklin"

In the example shown, the formula in cell D5 is:

    =PROPER(B5)

As the formula is copied down, it returns the names in column B with each word capitalized. In cases where a name is all uppercase, it converts the name to lowercase, and then capitalizes each word.

### Removing extra space

If names contain extra space characters, you can normalize spaces and convert to proper case in one step by nesting the TRIM function inside PROPER like this:

    =PROPER(TRIM("ben  franklin ")) // returns "Ben Franklin"
    

The [TRIM function](https://exceljet.net/functions/trim-function)
 removes leading and trailing spaces and converts runs of spaces to a single space. The result is returned to PROPER, which capitalizes each word as before.

### Last name first

It is also possible to restructure the name so that the last name appears first, followed by the first and middle name as seen in the workbook below. The formula in cell D5 is:

    =PROPER(TEXTAFTER(B5," ",-1)&", "&TEXTBEFORE(B5," ",-1))
    

![Formula to put names into proper case with last name first](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/put_names_into_proper_case_with_last_name_first.png "Formula to put names into proper case with last name first")

Working from the inside out, the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
 extracts the last name:

    TEXTAFTER(B5," ",-1) // returns "JOHNSON"
    

The [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
 extracts the first and middle names:

    TEXTBEFORE(B5," ",-1) // returns "EMILY MARIE"
    

Next, the two values are joined together with [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
:

    ="JOHNSON"&", "&"EMILY MARIE"
    ="JOHNSON, EMILY MARIE"

Finally, the PROPER function capitalizes each name:

    =PROPER("JOHNSON, EMILY MARIE")
    ="Johnson, Emily Marie"

Both TEXTBEFORE and TEXTAFTER have many options. For more information, see these links:

*   [Excel TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
    
*   [Excel TEXTAFTER function](https://exceljet.net/functions/textafter-function)
    

Related formulas
----------------

[![Excel formula: Remove leading and trailing spaces from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20leading%20and%20trailing%20spaces.png "Excel formula: Remove leading and trailing spaces from text")](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

### [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

The TRIM function is fully automatic. It removes both leading and trailing spaces from text strings, and also "normalizes" multiple spaces between words to one space character only. All you need to do is supply a reference to a cell. TRIM with CLEAN If you also need to remove line breaks from cells...

[![Excel formula: Join first and last name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_first_and_last_names.png "Excel formula: Join first and last name")](https://exceljet.net/formulas/join-first-and-last-name)

### [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)

In this example, the goal is to join different parts of a name (first, middle, last) into a full name. This is an example of concatenation . To concatenate means to join one text value to another with a formula, or in a more general programming language. In a current version of Excel, the simplest...

[![Excel formula: Get first name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_0.png "Excel formula: Get first name from name")](https://exceljet.net/formulas/get-first-name-from-name)

### [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)

In this example, the goal is to extract the first name from names that appear in <first> <middle> <last> format, where the middle name is optional. The easiest way to do this is with the newer TEXTBEFORE function. In older versions of Excel, you can use an alternative formula...

[![Excel formula: Get last name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_0.png "Excel formula: Get last name from name")](https://exceljet.net/formulas/get-last-name-from-name)

### [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)

In this example, the goal is to extract the last name from names that appear in <first> <middle> <last> format, where the middle name is not always present. The easiest way to do this is with the newer TEXTAFTER function. In older versions of Excel, you can use a significantly...

[![Excel formula: Get middle name from full name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_middle_name_from_name_0.png "Excel formula: Get middle name from full name")](https://exceljet.net/formulas/get-middle-name-from-full-name)

### [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)

In this example, the goal is to return the middle name from a full name in "First Middle Last" format. In the current version of Excel this is a fairly simple problem using the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, a similar formula is significantly more complicated, based...

Related functions
-----------------

[![Excel PROPER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20proper%20function.png "Excel PROPER function")](https://exceljet.net/functions/proper-function)

### [PROPER Function](https://exceljet.net/functions/proper-function)

The Excel PROPER function capitalizes each word in a given text string. Numbers, punctuation, and spaces are not affected.

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

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

*   [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)
    
*   [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)
    
*   [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)
    
*   [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)
    
*   [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)
    

### Functions

*   [PROPER Function](https://exceljet.net/functions/proper-function)
    
*   [TRIM Function](https://exceljet.net/functions/trim-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    

### Videos

*   [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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