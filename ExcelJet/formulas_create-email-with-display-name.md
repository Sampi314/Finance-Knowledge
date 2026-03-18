# Create email with display name - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/create-email-with-display-name

---

[Skip to main content](https://exceljet.net/formulas/create-email-with-display-name#main-content)

[](https://exceljet.net/formulas/create-email-with-display-name#)

*   [Previous](https://exceljet.net/formulas/create-email-address-from-name)
    
*   [Next](https://exceljet.net/formulas/get-domain-from-email-address)
    

[Internet](https://exceljet.net/formulas#Internet)

Create email with display name
==============================

by Dave Bruns · Updated 11 Aug 2023

Related functions 
------------------

[CONCAT](https://exceljet.net/functions/concat-function)

[CONCATENATE](https://exceljet.net/functions/concatenate-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

![Excel formula: Create email with display name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/create%20email%20with%20display%20name.png "Excel formula: Create email with display name")

Summary
-------

To create an email address with a display name, you can use [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
. In the example shown, the formula in D5, copied down, is:

    =B5&" <"&C5&">"
    

The result is a [text string](https://exceljet.net/glossary/text-value)
 that contains both the name and email address enclosed in angle brackets (<>).

Generic formula
---------------

    =name&" <"&email&">"

Explanation 
------------

Some applications show email addresses together with a "display name", where the name appears first, followed by the email address enclosed in angle brackets (<>). The goal in this example is to create a format like this based on an existing name and email address.

In the worksheet shown, column B contains a name, and column C contains an email address. The formula in column D uses the [ampersand character](https://exceljet.net/glossary/math-operators)
 (&) to join the name and email address together:

    =B5&" <"&C5&">"
    

This is an example of [concatenation](https://exceljet.net/glossary/concatenation)
. On the right side of the formula, the email address in C5 is wrapped in angle brackets:

    " <"&C5&">"
    

Notice the angle brackets are text and must be enclosed on double quotes (""). Also notice that opening bracket (<) begins with a space character. This allows us to join the name directly to the left side:

    =B5&" <"&C5&">"
    

The result is the name followed by a space character, followed by the email address in angle brackets.

### Concatenation functions

In the example shown, the ampersand operator (&) is used to concatenate the name, email, and angle brackets manually. The ampersand is a flexible way to concatenate text strings, because it can be used in a formula anywhere. However, Excel also has three functions dedicated to concatenation: [CONCATENATE](https://exceljet.net/functions/concatenate-function)
, [CONCAT](https://exceljet.net/functions/concat-function)
, and [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
. Both CONCATENATE and CONCAT can be used to solve the same problem like this:

    =CONCATENATE(B5," <",C5,">")
    =CONCAT(B5," <",C5,">")
    

Note that the CONCATENATE function is now technically replaced by the [CONCAT function](https://exceljet.net/functions/concat-function)
, which was first released in Excel 2019. The [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 is primarily designed to concatenate ranges.

Related formulas
----------------

[![Excel formula: Create email address from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create_email_address_from_name.png "Excel formula: Create email address from name")](https://exceljet.net/formulas/create-email-address-from-name)

### [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)

One of the key skills you need to be good with Excel formulas is concatenation . Put simply, concatenation is just a fancy name for joining text together. In Excel formulas, the primary operator for concatenation is the ampersand (&). A good example of a simple concatenation task is the...

[![Excel formula: Get name from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_name_from_email_address_0.png "Excel formula: Get name from email address")](https://exceljet.net/formulas/get-name-from-email-address)

### [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)

In this example, the goal is to extract the name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTBEFORE function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the LEFT and FIND functions. All three...

[![Excel formula: Get domain name from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_name_from_url_0.png "Excel formula: Get domain name from URL")](https://exceljet.net/formulas/get-domain-name-from-url)

### [Get domain name from URL](https://exceljet.net/formulas/get-domain-name-from-url)

In this example, the goal is to extract the domain name from a list of URLs. In the current version of Excel, the easiest way to do this is to use a formula based on the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, you can use a more complicated formula based on the LEFT and FIND...

[![Excel formula: Get top level domain (TLD)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_top_level_domain_TLD.png "Excel formula: Get top level domain (TLD)")](https://exceljet.net/formulas/get-top-level-domain-tld)

### [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)

In this example, the goal is to extract the top-level domain (TLD) from a list of domains. A top-level domain is the last segment of text in a domain name, for example, ".com", ".net", or ".net". In the current version of Excel, the TEXTAFTER function is a simple way to solve this problem. In an...

[![Excel formula: Get domain from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_from_email_address_0.png "Excel formula: Get domain from email address")](https://exceljet.net/formulas/get-domain-from-email-address)

### [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)

In this example, the goal is to extract just the domain name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTAFTER function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the RIGHT, LEN, and FIND...

Related functions
-----------------

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

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20change%20case%20with%20UPPER%2C%20LOWER%20and%20PROPER-thumb.png)](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

### [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

When you're working with text in Excel, you'll frequently need to change case. In this video we'll look at three functions that allow you to easily change case of text in Excel: UPPER, LOWER, and PROPER. In this worksheet, we have two columns that contain names. Column B contains last names in...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)
    
*   [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)
    
*   [Get domain name from URL](https://exceljet.net/formulas/get-domain-name-from-url)
    
*   [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)
    
*   [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)
    

### Functions

*   [CONCAT Function](https://exceljet.net/functions/concat-function)
    
*   [CONCATENATE Function](https://exceljet.net/functions/concatenate-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    

### Videos

*   [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)
    

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