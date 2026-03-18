# Create email address from name - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/create-email-address-from-name

---

[Skip to main content](https://exceljet.net/formulas/create-email-address-from-name#main-content)

[](https://exceljet.net/formulas/create-email-address-from-name#)

*   [Previous](https://exceljet.net/formulas/worksheet-name-exists)
    
*   [Next](https://exceljet.net/formulas/create-email-with-display-name)
    

[Internet](https://exceljet.net/formulas#Internet)

Create email address from name
==============================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[LEFT](https://exceljet.net/functions/left-function)

[LOWER](https://exceljet.net/functions/lower-function)

[CONCAT](https://exceljet.net/functions/concat-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7947/download?token=r7M6U8HW)
 (16.37 KB)

![Excel formula: Create email address from name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/create_email_address_from_name.png "Excel formula: Create email address from name")

Summary
-------

To create an email address from a name and a domain in Excel, you can use a formula that [concatenates](https://exceljet.net/articles/how-to-concatenate-in-excel)
 values, with help from the [LOWER function](https://exceljet.net/functions/lower-function)
 and the [LEFT function](https://exceljet.net/functions/left-function)
. In the example shown, the formula in E5 is:

    =LOWER(LEFT(C5)&B5)&"@"&$E$2
    

where cell E2 contains a domain name. The result in cell E5 is "tbrown@abc.com". As the formula is copied down, it creates an email address for each name in the list as shown.

Generic formula
---------------

    =LOWER(LEFT(first)&last)&"@"&domain

Explanation 
------------

One of the key skills you need to be good with Excel formulas is _concatenation_. Put simply, concatenation is just a fancy name for joining text together. In Excel formulas, the primary operator for concatenation is the ampersand (&). A good example of a simple concatenation task is the creation of an email address using a first and last name. There are many ways to create an email address, but the core problem is to join together a name and a domain, as seen in the worksheet shown. The formula in E5, copied down, is:

    =LOWER(LEFT(C5)&B5)&"@"&$E$2
    

### Background study

*   [How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
     \- article
*   [LEFT function](https://exceljet.net/functions/left-function)
     - overview
*   [LOWER function](https://exceljet.net/functions/lower-function)
     - overview
*   [How to change case with UPPER, LOWER, and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)
     - video

### How the formula works

In the example shown, the formula in E5 is:

    =LOWER(LEFT(C5)&B5)&"@"&$E$2
    

Working from the inside out, the [LEFT function](https://exceljet.net/functions/left-function)
 is used to get the first character of the first name like this:

    LEFT(C5) // returns "T"
    

LEFT extracts text from the _left side_ of a text string. Normally, we would also give LEFT the number of characters to extract as _num\_chars_ argument. However, in this case, we only want the first character and it turns out that _num\_chars_ defaults to 1, so there is no need to provide a number. With "Tom" in cell C5, the LEFT function returns "T". We then use the concatenation [operator](https://exceljet.net/glossary/math-operators)
 (&) to combine the result from LEFT with cell B5:

    =LEFT(C5)&B5
    ="T"&"BROWN"
    ="TBROWN"
    

The result is the text string "TBROWN", which is returned directly to the LOWER function. Simplifying, at this point we have the following:

    =LOWER("TBROWN")&"@"&$E$2

The [LOWER function](https://exceljet.net/functions/lower-function)
 converts any uppercase characters in a text string to lowercase characters. In this case, LEFT converts "TBROWN" to "tbrown":

    =LOWER("TBROWN") // returns "tbrown"

Simplifying again, we now have:

    ="tbrown"&"@"&$E$2

The remaining formula concatenates the text "tbrown" to the "@" character, and the result is then concatenated to cell E2, as shown below:

    ="tbrown@"&$E$2
    ="tbrown@"&"abc.com"
    ="tbrown@abc.com"

With "abc.com" in cell E2, the final result is "tbrown@abc.com". Notice that the reference to cell $E$2 is an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 to prevent this cell from changing as the formula is copied down the column.

### Alternate email address schemes

In a work environment, there are many different schemes for creating an email address. For example, a name like "Tom Brown" may appear as tbrown@abc.com, tom.brown@abc.com, brown\_tom@abc.com, tombrown@abc.com, etc. The attached worksheet contains formulas for these alternatives:

    =LOWER(LEFT(C5)&B5)&"@"&$E$2 // tbrown@abc.com
    =LOWER(C5&"."&B5)&"@"&$E$2 // tom.brown@abc.com
    =LOWER(B5&"_"&C5)&"@"&$E$2 // brown_tom@abc.com
    =LOWER(C5&B5)&"@"&$E$2 // tombrown@abc.com

Notice all variations use concatenation in different ways to create a different email address. They also use the LOWER function to force all parts of the name to lowercase characters only.

### CONCAT function

If you prefer, you can also use the [CONCAT function](https://exceljet.net/functions/concat-function)
 to solve this problem like this:

    =LOWER(CONCAT(LEFT(C5),B5,"@",$E$2))

CONCAT joins all four values with concatenation without the need for the & operator. The result from CONCAT, "TBROWN@abc.com", is returned directly to the LOWER function:

    =LOWER("TBROWN@abc.com") // returns "tbrown@abc.com"

The final result is "tbrown@abc.com" as in the original formula above. Note that in this formula, we run the entire text string through the LOWER function to keep things simple.

_Note: In an old version of Excel without CONCAT, you can use the [CONCATENATE function](https://exceljet.net/functions/concatenate-function)
 with the same result._

Related formulas
----------------

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

[![Excel formula: Remove protocol from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_protocol_from_url.png "Excel formula: Remove protocol from URL")](https://exceljet.net/formulas/remove-protocol-from-url)

### [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)

In this example, the goal is to remove the protocol from a list of URLs. To remove the protocol from a URL, we need to remove the first part of the URL. Protocols typically look like this: http:// https:// sftp:// Notice that all protocols end with a double slash ("//"). In the current version of...

Related functions
-----------------

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel LOWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lower%20function.png "Excel LOWER function")](https://exceljet.net/functions/lower-function)

### [LOWER Function](https://exceljet.net/functions/lower-function)

The Excel LOWER function converts a text string to all lowercase letters. Numbers, punctuation, and spaces are not affected.

[![Excel CONCAT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20concat%20function.png "Excel CONCAT function")](https://exceljet.net/functions/concat-function)

### [CONCAT Function](https://exceljet.net/functions/concat-function)

The Excel CONCAT function concatenates (joins) values supplied as references or constants. Unlike the [CONCATENATE function](https://exceljet.net/functions/concatenate-function)
 (which CONCAT replaces), CONCAT will accept a [range](https://exceljet.net/glossary/range)
 of cells to join, in addition to individual...

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

*   [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)
    
*   [Get domain name from URL](https://exceljet.net/formulas/get-domain-name-from-url)
    
*   [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)
    
*   [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)
    
*   [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)
    

### Functions

*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [LOWER Function](https://exceljet.net/functions/lower-function)
    
*   [CONCAT Function](https://exceljet.net/functions/concat-function)
    

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