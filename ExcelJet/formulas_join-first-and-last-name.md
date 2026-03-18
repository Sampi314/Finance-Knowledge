# Join first and last name - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/join-first-and-last-name

---

[Skip to main content](https://exceljet.net/formulas/join-first-and-last-name#main-content)

[](https://exceljet.net/formulas/join-first-and-last-name#)

*   [Previous](https://exceljet.net/formulas/get-middle-name-from-full-name)
    
*   [Next](https://exceljet.net/formulas/put-names-into-proper-case)
    

[Names](https://exceljet.net/formulas#Names)

Join first and last name
========================

by Dave Bruns · Updated 25 Nov 2023

Related functions 
------------------

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[CONCAT](https://exceljet.net/functions/concat-function)

[CONCATENATE](https://exceljet.net/functions/concatenate-function)

![Excel formula: Join first and last name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/join_first_and_last_names.png "Excel formula: Join first and last name")

Summary
-------

To combine a first name to a last name in Excel you can use the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
. In the worksheet shown, the formulas in cell F5 and H5 look like this:

    =TEXTJOIN(" ",1,B5,D5) // first and last
    =TEXTJOIN(" ",1,B5:D5) // first, middle, and last

The first formula returns a full name composed of the first and last names. The second formula returns a full name composed of the first, middle, and last names. As these formulas are copied down, they return the results seen in columns F and H. See below for a detailed explanation.

_Note: TEXTJOIN is only available in Excel 2019 or later. See below for formulas you can use in older versions of Excel._

Generic formula
---------------

    =TEXTJOIN(" ",1,first,last)

Explanation 
------------

In this example, the goal is to join different parts of a name (first, middle, last) into a full name. This is an example of [concatenation](https://exceljet.net/glossary/concatenation)
. To concatenate means to join one text value to another with a formula, or in a more general programming language. In a current version of Excel, the simplest approach is to use the TEXTJOIN function, which is a flexible function for concatenating values in Excel. In an older version of Excel, you can use manual concatenation with the ampersand (&) operator, or you can use the older CONCATENATE function. The article below discusses all three approaches.

_Note: Formulas that use concatenation in Excel are quite common, so it is a skill worth knowing. For a more detailed explanation of concatenation see [How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
._

### TEXTJOIN solution

In the current version of Excel, the easiest way to join different parts of a name together is to use the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
. To join the First name in column B to the Last name in column D together with TEXTJOIN the formula in cell F5 looks like this:

    =TEXTJOIN(" ",1,B5,D5)

The inputs to TEXTJOIN are as follows:

*   _delimiter_ - a single space (" ")
*   _ignore\_empty_ - 1, equivalent to TRUE
*   _text1_ - B5, the first name
*   _text2_ - D5, the last name

With this configuration, TEXTJOIN joins the first name in cell B5 to the last name in cell D5 together with a single space (" ") between them. If either value is empty, the _ignore\_empty_ argument set to 1 will cause TEXTJOIN to ignore the empty value and return the other value without a space.

You can easily adapt this formula to join all three names (first, middle, and last) together with TEXTJOIN. The formula used to perform this task in H5 looks like this:

    =TEXTJOIN(" ",1,B5:D5)

*   _delimiter_ - a single space (" ")
*   _ignore\_empty_ - 1, equivalent to TRUE
*   _text1_ - the range B5:D5

Note that in this case, we give TEXTJOIN the _range_ B5:D5 as _text1_. TEXTJOIN will join all three values together separated by a single space (" "). Because _ignore\_empty_ is set to 1 (equivalent to TRUE in Excel), when a middle name is not present, TEXTJOIN will ignore that value and not add an extra space between the first and last names.

_Note: newer versions of Excel also offer the [CONCAT function](https://exceljet.net/functions/concat-function)
 (which replaces the CONCATENATE function in functionality). However, in this case, the TEXTJOIN function is a better option because it can automatically ignore empty values._

### Manual concatenation solution

![Join first and last names with manual concatenation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/join_first_and_last_names_with_manual_concatenation.png "Join first and last names with manual concatenation")

In an older version of Excel that does not offer the TEXTJOIN function, you can use manual concatenation with the ampersand (&) [operator](https://exceljet.net/glossary/math-operators)
. This is often the technique used by more advanced users because it is simple and flexible. To join the first name in column B to the last name in column D together, you can use a formula like this:

    =B5&" "&D5

The result is the first name in cell B5 joined to the last name in cell D5 separated by a space (" "). To use the manual concatenation to join the first, middle, and last names together, the formula in H5 is a bit more complex:

    =B5&" "&IF(C5<>"",C5&" ","")&D5

At the core, this formula is similar to the first formula above. We begin with the first name in B5 and end with the last name in cell D5. However, to avoid adding an extra space when the middle name is blank we use the [IF function](https://exceljet.net/functions/if-function)
 to apply some conditional logic like this:

    IF(C5<>"",C5&" ","")

The translation for this formula is: _If cell C5 is not empty, return the value in C5 joined to a single space. If C5 is empty, return an empty string (""). In other words, if there is a middle name, add it with a space, otherwise, add nothing._

_Note: When you use concatenation in a formula, be sure to enclose any literal text in double quotes (""). However, do not enclose the ampersand (&) or cell references in quotes_.

### CONCATENATE solution

![Join first and last names with CONCATENATE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/join_first_and_last_names_with_concatenate_function.png "Join first and last names with CONCATENATE function")

Another way to solve this problem is with the older [CONCATENATE function](https://exceljet.net/functions/concatenate-function)
. In the worksheet below the formula in cell F5 is:

    =CONCATENATE(B5," ",D5)
    

And the formula in H5 looks like this:

    =CONCATENATE(B5," ",IF(C5<>"",C5&" ",""),D5)

In the formula above, we aren't able to avoid using the ampersand (&) entirely, because we still need the conditional logic created by the IF function to avoid adding extra space when the middle name is not present. This is something that TEXTJOIN handles automatically, which makes it a better option in more current versions of Excel.

Related formulas
----------------

[![Excel formula: Get first name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_0.png "Excel formula: Get first name from name")](https://exceljet.net/formulas/get-first-name-from-name)

### [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)

In this example, the goal is to extract the first name from names that appear in <first> <middle> <last> format, where the middle name is optional. The easiest way to do this is with the newer TEXTBEFORE function. In older versions of Excel, you can use an alternative formula...

[![Excel formula: Get last name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_0.png "Excel formula: Get last name from name")](https://exceljet.net/formulas/get-last-name-from-name)

### [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)

In this example, the goal is to extract the last name from names that appear in <first> <middle> <last> format, where the middle name is not always present. The easiest way to do this is with the newer TEXTAFTER function. In older versions of Excel, you can use a significantly...

[![Excel formula: Get first name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_with_comma.png "Excel formula: Get first name from name with comma")](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

### [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

In this example, the goal is to extract the first name from a list of names in "Last, First" format as seen in column B. There are several ways to approach this problem. In the current version of Excel, the easiest solution is to use the TEXTAFTER function. In older versions of Excel, it can be...

[![Excel formula: Get last name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_with_comma.png "Excel formula: Get last name from name with comma")](https://exceljet.net/formulas/get-last-name-from-name-with-comma)

### [Get last name from name with comma](https://exceljet.net/formulas/get-last-name-from-name-with-comma)

In this example, the goal is to extract the last name from a list of names in "Last, First" format as seen in column B. In the current version of Excel, the easiest solution is to use the TEXTBEFORE function. In older versions of Excel, it can be solved with a more complex formula based on the LEFT...

[![Excel formula: Get name from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_name_from_email_address_0.png "Excel formula: Get name from email address")](https://exceljet.net/formulas/get-name-from-email-address)

### [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)

In this example, the goal is to extract the name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTBEFORE function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the LEFT and FIND functions. All three...

[![Excel formula: Join cells with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join%20cells%20with%20comma_0.png "Excel formula: Join cells with comma")](https://exceljet.net/formulas/join-cells-with-comma)

### [Join cells with comma](https://exceljet.net/formulas/join-cells-with-comma)

Working from the inside out, the formula first joins the values the 5 cells to the left using the concatenation operator (...

Related functions
-----------------

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel CONCAT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20concat%20function.png "Excel CONCAT function")](https://exceljet.net/functions/concat-function)

### [CONCAT Function](https://exceljet.net/functions/concat-function)

The Excel CONCAT function concatenates (joins) values supplied as references or constants. Unlike the [CONCATENATE function](https://exceljet.net/functions/concatenate-function)
 (which CONCAT replaces), CONCAT will accept a [range](https://exceljet.net/glossary/range)
 of cells to join, in addition to individual...

[![Excel CONCATENATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20concatenate%20function.png "Excel CONCATENATE function")](https://exceljet.net/functions/concatenate-function)

### [CONCATENATE Function](https://exceljet.net/functions/concatenate-function)

The Excel CONCATENATE function concatenates (joins) join up to 30 values together and returns the result as text. In Excel 2019 and later, the [CONCAT](https://exceljet.net/functions/concat-function)
 and [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
 functions are better, more flexible alternatives...

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
    
*   [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)
    
*   [Get last name from name with comma](https://exceljet.net/formulas/get-last-name-from-name-with-comma)
    
*   [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)
    
*   [Join cells with comma](https://exceljet.net/formulas/join-cells-with-comma)
    

### Functions

*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [CONCAT Function](https://exceljet.net/functions/concat-function)
    
*   [CONCATENATE Function](https://exceljet.net/functions/concatenate-function)
    

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