# Get middle name from full name - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-middle-name-from-full-name

---

[Skip to main content](https://exceljet.net/formulas/get-middle-name-from-full-name#main-content)

[](https://exceljet.net/formulas/get-middle-name-from-full-name#)

*   [Previous](https://exceljet.net/formulas/get-last-name-from-name-with-comma)
    
*   [Next](https://exceljet.net/formulas/join-first-and-last-name)
    

[Names](https://exceljet.net/formulas#Names)

Get middle name from full name
==============================

by Dave Bruns · Updated 22 Nov 2023

Related functions 
------------------

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[MID](https://exceljet.net/functions/mid-function)

[FIND](https://exceljet.net/functions/find-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

![Excel formula: Get middle name from full name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_middle_name_from_name_0.png "Excel formula: Get middle name from full name")

Summary
-------

To extract the middle name from a full name, you can use a formula based on the [TEXTAFTER](https://exceljet.net/functions/textafter-function)
 and [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
 functions like this:

    =TEXTAFTER(TEXTBEFORE(B5," ",-1)," ",,,,"")

As the formula is copied down, it returns the middle name when present, and an empty string ("") when there is no middle name.

_Note: As of this writing, TEXTBEFORE and TEXTAFTER are is only available in [Excel 365](https://exceljet.net/glossary/excel-365)
. See below for an alternative formula that will work in older versions of Excel._

Generic formula
---------------

    =TEXTAFTER(TEXTBEFORE(name," ",-1)," ",,,,"")

Explanation 
------------

In this example, the goal is to return the middle name from a full name in "First Middle Last" format. In the current version of Excel this is a fairly simple problem using the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, a similar formula is significantly more complicated, based on the MID function and multiple FIND functions. Both approaches are explained below.

### Modern solution

In the latest version of Excel you can solve this problem with the [TEXTAFTER](https://exceljet.net/functions/textafter-function)
 and [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
 functions like this:

    =TEXTAFTER(TEXTBEFORE(B5," ",-1)," ",,,,"")

As the formula is copied down, it returns the middle name when present, and an empty string ("") when there is no middle name. Working from the inside out, the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
 is first used to extract all text that occurs _after_ the last space in the name:

    TEXTBEFORE(B5," ",-1) // returns "Emily Marie"

*   _text_ - the full name in cell B5
*   _delimiter_ - a single space (" ")
*   _instance\_num_ - provided as -1 (first space from the end)

The trick here is using -1 for _instance\_num_. A positive instance number tells TEXTBEFORE to count from the _start_ of the text string. A negative instance number tells TEXTBEFORE to count from the _end_. The result is "Emily Marie" (the name without the last name) which is delivered to the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
:

    =TEXTAFTER("Emily Marie"," ",,,,"")

*   _text_ - result from TEXTBEFORE
*   _delimiter_ - a single space (" ")
*   _instance\_num_ - omitted, defaults to 1
*   _match\_mode_ - omitted
*   _match\_end_ - omitted
*   _if\_not\_found_ - an empty string ("")

Essentially, we are asking TEXTAFTER for the text after the (first) space. Importantly, we also provide an empty string ("") for the _if\_not\_found_ argument to gracefully handle cases where there is no middle name.

### Legacy solution

In older versions of Excel that do not provide the TEXTAFTER or TEXTBEFORE functions, it is possible to use a more complex formula to extract the middle name:

    =MID(B9,FIND(" ",B9)+1,FIND(" ",B9,FIND(" ",B9)+1)-FIND(" ",B9)-1)

![Extracting a middle name in older versions of Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/get_middle_name_from_name_legacy_solution.png "Extracting a middle name in older versions of Excel")

This Excel formula is designed to extract the text between the first and second space characters in the cell B5. At a high level, we are using the [MID function](https://exceljet.net/functions/mid-function)
 to extract a substring from the text in cell B5, where the start\_num is the position to start the extraction, and num\_chars is the number of characters to extract:

    MID(B5,start_num,num_chars)

The challenge is in working out the correct values for _start\_num_ and _num\_chars_. To calculate a start number, we use the [FIND function](https://exceljet.net/functions/find-function)
 like this:

    FIND(" ",B5)+1 // start_num

This finds the position of the first space in B5 and adds 1. This calculation is used to set the _start\_num_ for the MID function, effectively starting the extraction from the character immediately _after_ the first space. Next, we need to calculate the number of characters to extract. This is a more difficult problem. First, we find the position of the second space in B5 like this:

    FIND(" ",B5,FIND(" ",B5)+1)

Here, we take advantage of the fact that the FIND function has as optional third argument called _start\_num_, which controls where FIND begins its search. When no value is provided, _start\_num_ will default to 1 and FIND will begin searching from the _beginning_ of the text string. To find the _second space_, we are asking FIND to begin searching _one character after the first space_:

    FIND(" ",B5)+1 // one char after first space

Once we know the location of the second space, we need to subtract the location of the first space:

    FIND(" ",B5,FIND(" ",B5)+ )-FIND(" ",B5)-1

This code calculates the number of characters between the first and second space by subtracting the position of the first space from the position of the second space and then subtracting 1. The result is delivered to the MID function as the num\_chars argument, and MID then extracts all text between the two spaces.

    =MID(B5,FIND(" ",B5)+1,FIND(" ",B5,FIND(" ",B5)+1)-FIND(" ",B5)-1)
    =MID(B5,7,FIND(" ",B5,FIND(" ",B5)+1)-FIND(" ",B5)-1)
    =MID(B5,7,FIND(" ",B5,FIND(" ",B5)+1)-FIND(" ",B5)-1)
    =MID(B5,7,FIND(" ",B5,6+1)-6-1)
    =MID(B5,7,FIND(" ",B5,7)-6-1)
    =MID(B5,7,12-6-1)
    =MID(B5,7,5)
    ="Marie"

The formula above will work correctly when there are two spaces in the name. However, when a second space is not found (i.e. there is no middle name, FIND will return a #VALUE! error. An easy way to manage this error is to embed the original formula into the IFERROR function:

    =IFERROR(MID(B5,FIND(" ",B5)+1,FIND(" ",B5,FIND(" ",B5)+1)-FIND(" ",B5)-1),"")

Now when a second space is not found, FIND will return a #VALUE! error, and IFERROR will catch that error and return an empty string (""), which looks like a blank cell in Excel.

Related formulas
----------------

[![Excel formula: Get first name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_0.png "Excel formula: Get first name from name")](https://exceljet.net/formulas/get-first-name-from-name)

### [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)

In this example, the goal is to extract the first name from names that appear in <first> <middle> <last> format, where the middle name is optional. The easiest way to do this is with the newer TEXTBEFORE function. In older versions of Excel, you can use an alternative formula...

[![Excel formula: Get last name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_0.png "Excel formula: Get last name from name")](https://exceljet.net/formulas/get-last-name-from-name)

### [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)

In this example, the goal is to extract the last name from names that appear in <first> <middle> <last> format, where the middle name is not always present. The easiest way to do this is with the newer TEXTAFTER function. In older versions of Excel, you can use a significantly...

[![Excel formula: Split full name into parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_full_name_into_parts.png "Excel formula: Split full name into parts")](https://exceljet.net/formulas/split-full-name-into-parts)

### [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)

In this example, the goal is to split the names in column B into three separate parts (First, Middle, and Last) with a single formula. In cases where there is no middle name, the Middle column should be blank. In cases where there are two middle names, the Middle column should contain both names...

[![Excel formula: Get first name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_with_comma.png "Excel formula: Get first name from name with comma")](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

### [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

In this example, the goal is to extract the first name from a list of names in "Last, First" format as seen in column B. There are several ways to approach this problem. In the current version of Excel, the easiest solution is to use the TEXTAFTER function. In older versions of Excel, it can be...

[![Excel formula: Get last name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_with_comma.png "Excel formula: Get last name from name with comma")](https://exceljet.net/formulas/get-last-name-from-name-with-comma)

### [Get last name from name with comma](https://exceljet.net/formulas/get-last-name-from-name-with-comma)

In this example, the goal is to extract the last name from a list of names in "Last, First" format as seen in column B. In the current version of Excel, the easiest solution is to use the TEXTBEFORE function. In older versions of Excel, it can be solved with a more complex formula based on the LEFT...

[![Excel formula: Join first and last name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_first_and_last_names.png "Excel formula: Join first and last name")](https://exceljet.net/formulas/join-first-and-last-name)

### [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)

In this example, the goal is to join different parts of a name (first, middle, last) into a full name. This is an example of concatenation . To concatenate means to join one text value to another with a formula, or in a more general programming language. In a current version of Excel, the simplest...

Related functions
-----------------

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20complex%20formula%20step%20by%20step-thumb.png)](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

### [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

When you look at a complex formula in Excel you may be completely baffled at first glance, but all complex formulas are just small steps added together. Let me show you an example. Here we have a list of names. We want to pull out the first name from the full name. There's an Excel function called...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)
    
*   [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)
    
*   [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)
    
*   [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)
    
*   [Get last name from name with comma](https://exceljet.net/formulas/get-last-name-from-name-with-comma)
    
*   [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)
    

### Functions

*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    

### Videos

*   [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)
    

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