# Get last name from name - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-last-name-from-name

---

[Skip to main content](https://exceljet.net/formulas/get-last-name-from-name#main-content)

[](https://exceljet.net/formulas/get-last-name-from-name#)

*   [Previous](https://exceljet.net/formulas/get-first-name-from-name-with-comma)
    
*   [Next](https://exceljet.net/formulas/get-last-name-from-name-with-comma)
    

[Names](https://exceljet.net/formulas#Names)

Get last name from name
=======================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[FIND](https://exceljet.net/functions/find-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8093/download?token=yCavPQgG)
 (14.27 KB)

![Excel formula: Get last name from name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_last_name_from_name_0.png "Excel formula: Get last name from name")

Summary
-------

To extract the last name from a full name in <first> <middle> <last> format, you can use the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
. In the worksheet shown, the formula in cell D5 is:

    =TEXTAFTER(B5," ",-1)

As the formula is copied down, it returns the lat name from each name listed in column B, ignoring middle names when they exist.

_Note: As of this writing, the TEXTAFTER function is only available in [Excel 365](https://exceljet.net/glossary/excel-365)
. See below for an alternative formula that will work in older versions of Excel._

Generic formula
---------------

    =TEXTAFTER(A1," ",-1)

Explanation 
------------

In this example, the goal is to extract the last name from names that appear in <first> <middle> <last> format, where the middle name is not always present. The easiest way to do this is with the newer TEXTAFTER function. In older versions of Excel, you can use a significantly more complex formula based on the RIGHT, FIND, and SUBSTITUTE functions. Both options are explained below.

_Note: This is a great example of how new functions in Excel like TEXTBEFORE and TEXTAFTER are game-changers that can radically simplify formulas. Note the contrast between the modern solution and the legacy solution._

### Modern solution

In the current version of Excel, the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
 is the best way to solve this problem. TEXTAFTER extracts text that occurs _after_ a given delimiter. In its simplest form, TEXTAFTER only requires two arguments, text and delimiter. However, in this case, we also need to provide an instance number:

    =TEXTAFTER(text,delimiter,instance_num)

In the worksheet shown, the formula we are using to return the last name looks like this:

    =TEXTAFTER(B5," ",-1)

*   _text_ - B5, the full name in column B
*   _delimiter_ - " ", a single space
*   _instance\_num_ - provided as -1, the first space _from the end_

The key here is setting _instance\_num_ to -1. Normally, a positive instance number tells TEXTAFTER to count instances from the left. A _negative_ instance number tells TEXTAFTER to count instances from the _right_. In other words, we are asking TEXTAFTER for the text after the last space. This is important, because some names have middle names, and we need to ignore the first space in that case. TEXTAFTER has many other options that you can read more about [here](https://exceljet.net/functions/textafter-function)
.

### Legacy solution

In older versions of Excel that do not offer the TEXTAFTER function, you can use an alternative formula that looks like this:

    =MID(B5,FIND("*",SUBSTITUTE(B5," ","*",LEN(B5)-LEN(SUBSTITUTE(B5," ",""))))+1,100)

_Note: it is also possible to use the RIGHT function in a similar formula, but using MID is a bit of a shortcut._

This is a complicated formula. One reason it's complicated is that we don't have a direct way to find the last space in a name, which is important when a name contains more than two words (i.e. contains one or more middle names). As a result, we need to employ some trickery with the SUBSTITUTE function to locate and mark the last space in the name with an asterisk (\*).

At the core, this formula uses the [MID function](https://exceljet.net/functions/mid-function)
 to extract characters in the name starting at a particular location. The complex part of the formula does just one thing: it calculates how many characters need to be extracted, represented by **n** below:

    =MID(B5,n,100)

The code that calculates **n** is below:

    FIND("*",SUBSTITUTE(B5," ","*",LEN(B5)-LEN(SUBSTITUTE(B5," ",""))))+1

At a high level, the snippet above replaces the last space (" ") in the full name with an asterisk (\*) and then uses the FIND function to determine the numeric position of the asterisk (\*). Once we have that number, we simply add 1 to determine a _start\_num_ for MID.

How does the code replace only the last space with an asterisk? This is the clever part. Buckle up, because the explanation gets a bit technical. The key to this formula is this bit:

    SUBSTITUTE(B5," ","*",LEN(B5)-LEN(SUBSTITUTE(B5," ","")))
    

Normally, the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 will replace all instances of _old\_text_ with _new\_text_. However, SUBSTITUTE has an optional fourth argument called _instance\_num_ that specifies which "instance" of the old text should be replaced. If the argument is omitted, all instances are replaced. If a number like 2 is provided, SUBSTITUTE will replace only the second instance.

At this point, the problem becomes how to calculate the correct _instance\_num_. Looking back at the names in column B, we can see that we want to provide instance number as 2 when a name contains a middle name, and instance number as 1 when there is a middle name. The way we solve the problem is to count the number of spaces in the name, which we do in the snippet below:

    LEN(B4)-LEN(SUBSTITUTE(B4," ",""))
    

This is a fairly common pattern in Excel formulas that must calculate how many times a character appears in a text string. In brief, we calculate the total length of the text string with the [LEN function](https://exceljet.net/functions/len-function)
, then subtract the length of the text string after the target character has been removed with SUBSTITUTE. You can find a more detailed explanation [here](https://exceljet.net/formulas/count-specific-characters-in-text-string)
.

In cell B5, the name is "Susan Ann Chang", so the code above evaluates like this:

    =LEN(B4)-LEN(SUBSTITUTE(B4," ",""))
    =15-LEN("SusanAnnChang")
    =15-13
    =2
    

This means we have 2 spaces in the name, and 2 becomes the instance number used to replace the second space with an asterisk (\*). Below is the formula simplified to show the calculated 2:

    =MID(B5,FIND("*",SUBSTITUTE(B5," ","*",2))+1,100)

After SUBSTITUTE runs, we have "Susan Ann\*Chang":

    =MID(B5,FIND("*","Susan Ann*Chang")+1,100)

We're getting close!

Next, the [FIND function](https://exceljet.net/functions/find-function)
 runs and returns the numeric position of the asterisk (\*) in "Susan Ann\*Chang", which is 10. We then add 1 to get a starting position of 11. This is the number used for **n** in the formula above. The formula calculates a final result like this:

    =MID(B5,10+1,100)
    =MID(B5,11,100)
    ="Chang"

The MID function begins extracting text at the 11th character, extracts all remaining text, and returns "Chang" as a final result.

Notice that we provide _num\_chars_ as 100. This arbitrary number is part of a shortcut with MID. When _num\_chars_ is larger than the remaining characters, the MID function is programmed to simply extract _all remaining text_, which works perfectly in this case. You can increase this number as needed.

### With the RIGHT function

As mentioned above, the [RIGHT function](https://exceljet.net/functions/right-function)
 can also be used to extract the last names like this:

    =RIGHT(B5,LEN(B5)-FIND("*",SUBSTITUTE(B5," ","*",LEN(B5)-LEN(SUBSTITUTE(B5," ","")))))

This formula is similar to the formula above, but a bit more complex because we need to be more precise when calculating the number of characters to extract from the RIGHT. With the MID function, once we know the location of the asterisk, we simply ask for all remaining text using an arbitrarily large number. With RIGHT, we need to work out the number of characters to ask for by subtracting the position of the asterisk from the total length of the name.

_Note: Extra spaces in the names will cause problems with the formulas on this page. One solution is to use the [TRIM function](https://exceljet.net/functions/trim-function)
 first to normalize spaces, then use the formula on the result from TRIM._

Related formulas
----------------

[![Excel formula: Get first name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_0.png "Excel formula: Get first name from name")](https://exceljet.net/formulas/get-first-name-from-name)

### [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)

In this example, the goal is to extract the first name from names that appear in <first> <middle> <last> format, where the middle name is optional. The easiest way to do this is with the newer TEXTBEFORE function. In older versions of Excel, you can use an alternative formula...

[![Excel formula: Get middle name from full name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_middle_name_from_name_0.png "Excel formula: Get middle name from full name")](https://exceljet.net/formulas/get-middle-name-from-full-name)

### [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)

In this example, the goal is to return the middle name from a full name in "First Middle Last" format. In the current version of Excel this is a fairly simple problem using the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, a similar formula is significantly more complicated, based...

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

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

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

*   [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)
    
*   [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)
    
*   [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)
    
*   [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)
    
*   [Get last name from name with comma](https://exceljet.net/formulas/get-last-name-from-name-with-comma)
    
*   [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)
    

### Functions

*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
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