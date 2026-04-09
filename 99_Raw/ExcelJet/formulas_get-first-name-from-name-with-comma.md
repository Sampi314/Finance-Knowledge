# Get first name from name with comma - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-first-name-from-name-with-comma

---

[Skip to main content](https://exceljet.net/formulas/get-first-name-from-name-with-comma#main-content)

[](https://exceljet.net/formulas/get-first-name-from-name-with-comma#)

*   [Previous](https://exceljet.net/formulas/get-first-name-from-name)
    
*   [Next](https://exceljet.net/formulas/get-last-name-from-name)
    

[Names](https://exceljet.net/formulas#Names)

Get first name from name with comma
===================================

by Dave Bruns · Updated 20 Nov 2023

Related functions 
------------------

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[RIGHT](https://exceljet.net/functions/right-function)

[LEN](https://exceljet.net/functions/len-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Get first name from name with comma](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_first_name_from_name_with_comma.png "Excel formula: Get first name from name with comma")

Summary
-------

To extract the first name from a full name in "Last, First" format, you can use the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
. In the worksheet shown, the formula in cell D5 is:

    =TEXTAFTER(B5,", ")

As the formula is copied down, it returns the first name from each name listed in column B.

_Note: As of this writing, the TEXTAFTER function is only available in [Excel 365](https://exceljet.net/glossary/excel-365)
. See below for an alternative formula that will work in older versions of Excel_

Generic formula
---------------

    =TEXTAFTER(name,", ")

Explanation 
------------

In this example, the goal is to extract the first name from a list of names in "Last, First" format as seen in column B. There are several ways to approach this problem. In the current version of Excel, the easiest solution is to use the TEXTAFTER function. In older versions of Excel, it can be solved with a more complex formula based on the RIGHT, LEN, and FIND functions. Both approaches are explained below.

### Modern solution

In the current version of Excel, the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
 is the best way to solve this problem. TEXTAFTER extracts text that occurs _after_ a given delimiter. In its simplest form, TEXTAFTER only requires two arguments, _text_ and _delimiter_:

    =TEXTAFTER(text,delimiter)

In the worksheet shown, the formula we are using to return the last name looks like this:

    =TEXTAFTER(B5,", ")

*   _text_ - B5, the name in column B
*   _delimiter_ - ", " (a comma followed by a single space)

In this configuration, the TEXTAFTER function simply returns all text that appears after the comma and space. If the space character is not  consistent (i.e. sometimes the comma is followed by a space, and sometimes not) you can provide more than one delimiter to TEXTAFTER to handle both situations like this:

    =TEXTAFTER(B8,{", ",","})

The curly braces indicate an array constant, which is a way to pass more than one value into a function. TEXTAFTER has many other options that you can read more about [here](https://exceljet.net/functions/textafter-function)
.

### Legacy solution

In older versions of Excel that do not provide the TEXTAFTER function, you can solve this problem with a more complex formula based on the RIGHT, LEN, and FIND functions:

    =RIGHT(B5,LEN(B5)-FIND(",",B5)-1)
    

As the formula is copied down, it returns the first name from each name in column B. This formula achieves the same result but in a more manual way. At the core, the RIGHT function is used to extract the first name from the full name in column B, _starting from the right_. The [RIGHT function](https://exceljet.net/functions/right-function)
 takes two arguments, the text itself and _num\_chars_, which specifies how many characters to extract:

    =RIGHT(text,num_chars)
    

For example, if we use "apple" for _text_ and 3 for _num\_chars_, we get "ple":

    =RIGHT("apple",3) returns "ple"
    

The complexity in the formula comes from working out how many characters to extract, which is done with the snippet below:

    LEN(B5)-FIND(",",B5)-1
    

The challenge problem is to calculate the length of the first name. To work this out, we locate the position of the comma (",") in the text, then we subtract this location from the total length of the text:

    LEN(B5)-FIND(",",B5)-1
    

The [LEN function](https://exceljet.net/functions/len-function)
 calculates the total characters in the text:

    LEN(B5) // returns 10
    

Because there are ten characters in "Chang, Amy", LEN returns 10. Next, the [FIND function](https://exceljet.net/functions/find-function)
 is used to locate the comma (",") in the text:

    =FIND(",",B5) // returns 6
    

Because the comma (",") occurs as the sixth character in the text, FIND returns 6. When we subtract 6 from 10, we get 4:

    =LEN(B5)-FIND(",",B5)
    =10-6
    =4
    

This is close to what we need, but "Amy" contains 3 characters, _not_ 4 characters. If we ask RIGHT for the last 4 characters in "Chang, Amy", we'll also get the space that follows the comma. So, we need to subtract 1 to take the comma into account:

    =LEN(B5)-FIND(",",B5)-1
    =10-6-1
    =3
    

The code above returns this result directly to the RIGHT function as the _num\_chars_ argument:

    RIGHT("Chang, Amy",3) // returns "Amy" 
    

And RIGHT returns "Amy" as the final result.

_Note:  If there is no space after the comma, there is no need to subtract 1._

### Get the last name

To extract the _last_ name from the names in column B, you can use a similar formula based on the [LEFT function](https://exceljet.net/functions/left-function)
:

    =LEFT(B5,FIND(",",B5)-1)
    

See the [example here](https://exceljet.net/formulas/get-last-name-from-name-with-comma)
 for a full explanation.

Related formulas
----------------

[![Excel formula: Get last name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_with_comma.png "Excel formula: Get last name from name with comma")](https://exceljet.net/formulas/get-last-name-from-name-with-comma)

### [Get last name from name with comma](https://exceljet.net/formulas/get-last-name-from-name-with-comma)

In this example, the goal is to extract the last name from a list of names in "Last, First" format as seen in column B. In the current version of Excel, the easiest solution is to use the TEXTBEFORE function. In older versions of Excel, it can be solved with a more complex formula based on the LEFT...

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

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

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

*   [Get last name from name with comma](https://exceljet.net/formulas/get-last-name-from-name-with-comma)
    
*   [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)
    
*   [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)
    
*   [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)
    

### Functions

*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

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