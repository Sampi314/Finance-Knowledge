# Get last name from name with comma - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-last-name-from-name-with-comma

---

[Skip to main content](https://exceljet.net/formulas/get-last-name-from-name-with-comma#main-content)

[](https://exceljet.net/formulas/get-last-name-from-name-with-comma#)

*   [Previous](https://exceljet.net/formulas/get-last-name-from-name)
    
*   [Next](https://exceljet.net/formulas/get-middle-name-from-full-name)
    

[Names](https://exceljet.net/formulas#Names)

Get last name from name with comma
==================================

by Dave Bruns · Updated 20 Nov 2023

Related functions 
------------------

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[LEFT](https://exceljet.net/functions/left-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Get last name from name with comma](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_last_name_from_name_with_comma.png "Excel formula: Get last name from name with comma")

Summary
-------

To extract the first name from a full name in "Last, First" format, you can use the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
. In the worksheet shown, the formula in cell D5 is:

    =TEXTBEFORE(B5,",")

As the formula is copied down, it returns the last name from each name listed in column B.

_Note: As of this writing, the TEXTBEFORE function is only available in [Excel 365](https://exceljet.net/glossary/excel-365)
. See below for an alternative formula that will work in older versions of Excel_

Generic formula
---------------

    =TEXTBEFORE(name,",")

Explanation 
------------

In this example, the goal is to extract the last name from a list of names in "Last, First" format as seen in column B. In the current version of Excel, the easiest solution is to use the TEXTBEFORE function. In older versions of Excel, it can be solved with a more complex formula based on the LEFT and FIND functions. Both approaches are explained below.

### Modern solution

In the current version of Excel, the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
 is the best way to solve this problem. TEXTBEFORE extracts text that occurs _before_ a given delimiter. In its simplest form, TEXTBEFORE only requires two arguments, _text_ and _delimiter_:

    =TEXTBEFORE(text,delimiter)

In the worksheet shown, the formula we are using to return the last name looks like this:

    =TEXTBEFORE(B5,",")

*   _text_ - B5, the name in column B
*   _delimiter_ - "," (a comma)

Note that the comma needs to be enclosed in double quotes (",") and there is no need to add a space after the comma. In this configuration, the TEXTBEFORE function simply returns all text that occurs _before_ the comma. TEXTBEFORE has many other options that you can read more about [here](https://exceljet.net/functions/textbefore-function)
.

### Legacy solution

In older versions of Excel that do not provide the TEXTBEFORE function, you can solve this problem with a more complex formula based on the RIGHT, LEN, and FIND functions:

    =LEFT(B5,FIND(",",B5)-1)

At a high level, the [LEFT function](https://exceljet.net/functions/left-function)
 extracts text starting at the _left_ side of a text string. LEFT takes two arguments, _text_ and _num\_chars_, which indicates how many characters to extract:

    =LEFT(text,num_chars)
    

For example, if we use "apple" for _text_ and 3 for _num\_chars_, we get "app":

    =LEFT("apple",3) returns "app"
    

The main challenge in this example is to calculate how many characters to extract, which is equal to the length of the last name. This is done with the [FIND function](https://exceljet.net/functions/find-function)
 like this:

    FIND(",",B5)-1

FIND returns the location of text as a numeric position. Because the comma appears as the 6th character in the text, the FIND function returns 6. This is one more character than we need, so we subtract 1:

    FIND(",",B5)-1 // returns 5
    

The result is 5, which is the length of the last name in "Chang, Amy". The code above returns this result directly to the LEFT function as the _num\_chars_ argument:

    LEFT("Chang, Amy",5) // returns "Chang" 
    

LEFT returns "Chang" as the final result. To extract the _first_ name from names in column B [see the formulas on this page](https://exceljet.net/formulas/get-first-name-from-name-with-comma)
.

Related formulas
----------------

[![Excel formula: Get first name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_with_comma.png "Excel formula: Get first name from name with comma")](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

### [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

In this example, the goal is to extract the first name from a list of names in "Last, First" format as seen in column B. There are several ways to approach this problem. In the current version of Excel, the easiest solution is to use the TEXTAFTER function. In older versions of Excel, it can be...

[![Excel formula: Get first name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_0.png "Excel formula: Get first name from name")](https://exceljet.net/formulas/get-first-name-from-name)

### [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)

In this example, the goal is to extract the first name from names that appear in <first> <middle> <last> format, where the middle name is optional. The easiest way to do this is with the newer TEXTBEFORE function. In older versions of Excel, you can use an alternative formula...

[![Excel formula: Get last name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_0.png "Excel formula: Get last name from name")](https://exceljet.net/formulas/get-last-name-from-name)

### [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)

In this example, the goal is to extract the last name from names that appear in <first> <middle> <last> format, where the middle name is not always present. The easiest way to do this is with the newer TEXTAFTER function. In older versions of Excel, you can use a significantly...

[![Excel formula: Join first and last name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_first_and_last_names.png "Excel formula: Join first and last name")](https://exceljet.net/formulas/join-first-and-last-name)

### [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)

In this example, the goal is to join different parts of a name (first, middle, last) into a full name. This is an example of concatenation . To concatenate means to join one text value to another with a formula, or in a more general programming language. In a current version of Excel, the simplest...

Related functions
-----------------

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

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

*   [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)
    
*   [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)
    
*   [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)
    
*   [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)
    

### Functions

*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

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