# Get first name from name - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-first-name-from-name

---

[Skip to main content](https://exceljet.net/formulas/get-first-name-from-name#main-content)

[](https://exceljet.net/formulas/get-first-name-from-name#)

*   [Previous](https://exceljet.net/formulas/remove-trailing-slash-from-url)
    
*   [Next](https://exceljet.net/formulas/get-first-name-from-name-with-comma)
    

[Names](https://exceljet.net/formulas#Names)

Get first name from name
========================

by Dave Bruns · Updated 27 Nov 2023

Related functions 
------------------

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[LEFT](https://exceljet.net/functions/left-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Get first name from name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_first_name_from_name_0.png "Excel formula: Get first name from name")

Summary
-------

To extract the first name from a full name in <first> <middle> <last> format, you can use the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
. In the worksheet shown, the formula in cell D5 is:

    =TEXTBEFORE(B5," ")

As the formula is copied down, it returns the first name from each name listed in column B.

_Note: As of this writing, the TEXTBEFORE function is only available in [Excel 365](https://exceljet.net/glossary/excel-365)
. See below for an alternative formula that will work in older versions of Excel._

Generic formula
---------------

    =TEXTBEFORE(name," ")

Explanation 
------------

In this example, the goal is to extract the first name from names that appear in <first> <middle> <last> format, where the middle name is optional. The easiest way to do this is with the newer TEXTBEFORE function. In older versions of Excel, you can use an alternative formula based on the LEFT function and the FIND function. Both formulas are explained below.

_Note: this formula does not account for titles (Ms., Mr., Dr., etc.) in the full name. If titles exist, they should be removed first._

### Modern solution

In the current version of Excel, the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
 is the simplest way to solve this problem. The TEXTBEFORE function extracts text that occurs before a given delimiter. In its simplest form, TEXTBEFORE only requires two arguments, text and delimiter:

    =TEXTBEFORE(text,delimiter)

In this problem, the text we want to work with comes from the names in column B, and the delimiter is a single space (" "). To extract the first name from each full name, the formula in cell D5 looks like this

    =TEXTBEFORE(B5," ")

As the formula is copied down the column, TEXTBEFORE returns the text before the first space character that appears in each name. The TEXTBEFORE function has a lot of options which are [explained on this page](https://exceljet.net/functions/textbefore-function)
.

### Legacy Excel

In older versions of Excel that do not offer the TEXTBEFORE function, you can use an alternative formula that looks like this:

    =LEFT(B5,FIND(" ",B5)-1)

Working from the inside out, the [FIND function](https://exceljet.net/functions/find-function)
 finds the first space character (" ") in the name and returns the position of that space in the full name. The number 1 is subtracted from this number to account for the space itself. The [LEFT function](https://exceljet.net/functions/left-function)
 uses this number as the total number of characters that should be extracted in the next step below.

Back in the worksheet, the first space (" ") in  cell B5 occurs as the 6th character, so FIND returns 6:

    =FIND(" ",B5) // returns 6

After 1 is subtracted, we have 5, which is returned to the LEFT function as _num\_chars_:

    =LEFT(B5,5) // returns  "Emily"

The LEFT function then extracts 5 characters starting at the left and returns "Emily" as a final result.

Related formulas
----------------

[![Excel formula: Get last name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_0.png "Excel formula: Get last name from name")](https://exceljet.net/formulas/get-last-name-from-name)

### [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)

In this example, the goal is to extract the last name from names that appear in <first> <middle> <last> format, where the middle name is not always present. The easiest way to do this is with the newer TEXTAFTER function. In older versions of Excel, you can use a significantly...

[![Excel formula: Get middle name from full name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_middle_name_from_name_0.png "Excel formula: Get middle name from full name")](https://exceljet.net/formulas/get-middle-name-from-full-name)

### [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)

In this example, the goal is to return the middle name from a full name in "First Middle Last" format. In the current version of Excel this is a fairly simple problem using the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, a similar formula is significantly more complicated, based...

[![Excel formula: Split full name into parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_full_name_into_parts.png "Excel formula: Split full name into parts")](https://exceljet.net/formulas/split-full-name-into-parts)

### [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)

In this example, the goal is to split the names in column B into three separate parts (First, Middle, and Last) with a single formula. In cases where there is no middle name, the Middle column should be blank. In cases where there are two middle names, the Middle column should contain both names...

[![Excel formula: Get last name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_with_comma.png "Excel formula: Get last name from name with comma")](https://exceljet.net/formulas/get-last-name-from-name-with-comma)

### [Get last name from name with comma](https://exceljet.net/formulas/get-last-name-from-name-with-comma)

In this example, the goal is to extract the last name from a list of names in "Last, First" format as seen in column B. In the current version of Excel, the easiest solution is to use the TEXTBEFORE function. In older versions of Excel, it can be solved with a more complex formula based on the LEFT...

[![Excel formula: Get first name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_with_comma.png "Excel formula: Get first name from name with comma")](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

### [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

In this example, the goal is to extract the first name from a list of names in "Last, First" format as seen in column B. There are several ways to approach this problem. In the current version of Excel, the easiest solution is to use the TEXTAFTER function. In older versions of Excel, it can be...

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

*   [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)
    
*   [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)
    
*   [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)
    
*   [Get last name from name with comma](https://exceljet.net/formulas/get-last-name-from-name-with-comma)
    
*   [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)
    
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