# Remove protocol from URL - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-protocol-from-url

---

[Skip to main content](https://exceljet.net/formulas/remove-protocol-from-url#main-content)

[](https://exceljet.net/formulas/remove-protocol-from-url#)

*   [Previous](https://exceljet.net/formulas/get-top-level-domain-tld)
    
*   [Next](https://exceljet.net/formulas/remove-trailing-slash-from-url)
    

[Internet](https://exceljet.net/formulas#Internet)

Remove protocol from URL
========================

by Dave Bruns · Updated 15 Aug 2023

Related functions 
------------------

[MID](https://exceljet.net/functions/mid-function)

[RIGHT](https://exceljet.net/functions/right-function)

[LEN](https://exceljet.net/functions/len-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Remove protocol from URL](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove_protocol_from_url.png "Excel formula: Remove protocol from URL")

Summary
-------

To remove the protocol (i.e. https://, http://, ftp://, etc.) from a URL, you can use a formula based on the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
. In the example shown, where B5 contains a URL with a protocol, the formula in D5 is:

    =TEXTAFTER(B5,"//")
    

As the formula is copied down, it removes the protocol from each URL as shown.

_Notes: TEXTAFTER is a newer function in Excel. In older versions of Excel, you can use a formula based on the MID and FIND functions, as explained below._

Generic formula
---------------

    =TEXTAFTER(url,"//")

Explanation 
------------

In this example, the goal is to remove the protocol from a list of URLs. To remove the protocol from a URL, we need to remove the first part of the URL. Protocols typically look like this:

*   http://
*   https://
*   sftp://

Notice that all protocols end with a double slash ("//"). In the current version of Excel, the easiest way to do this is with the TEXTAFTER function. In older versions of Excel, you can use a formula based on the MID and FIND functions. Both options are explained below.

### TEXTAFTER function

The TEXTAFTER function returns the text that occurs _after_ a given delimiter. TEXTAFTER supports [many options](https://exceljet.net/functions/textafter-function)
, but for this problem, we only need to provide the first two arguments:

    =TEXTAFTER(text,delimiter)

*   _Text_: the text string to process.
*   _Delimiter_: the place at which to split the text.

To remove all text up to and including the double slash, we can use the TEXTAFTER function like this:

    =TEXTAFTER(B5,"//")

As the formula is copied down the table, it extracts the text that occurs after the double slash ("//"). The result is the original URL without the protocol.

_Want to learn more about TEXTAFTER? Check out our guide: [How to use the TEXTAFTER function](https://exceljet.net/functions/textafter-function)
._

### Legacy Excel

In an older version of Excel without the TEXTAFTER function, you can remove the protocol from a URL with a formula based on the MID function and the FIND function like this:

    =MID(B5,FIND("//",B5)+2,LEN(B5))

The core of this formula is the [MID function](https://exceljet.net/functions/mid-function)
, which extracts the text in a URL starting with the character after "//", and ending with the character before the trailing slash ("/"):

    =MID(text,start_num,num_chars)
    

The text is the URL in cell B5. The _start\_num_ is calculated using the [FIND function](https://exceljet.net/functions/find-function)
 like this:

    FIND("//",B5)+2
    

FIND returns the position of the double slash ("//") in the URL as a number. With the text "https://www.domain.com" in cell B5, FIND returns 9. We don't want to start extracting at character 9 however, we want to skip the double slash ("//") altogether, so we add 2 to the result from FIND which results in 11. This is the value used for _start\_num._ At this point, we have:

    =MID(B5,11,LEN(B5))

To provide a value for _num\_chars_, we use the [LEN function](https://exceljet.net/functions/len-function)
, which returns a count of all the characters in B5, which is 22. Using the LEN function like this is a shortcut, designed to simplify the formula. LEN will return 22, which is greater than the number of characters that remain. However, when _num\_chars_ exceeds the remaining string length, MID will simply extract all remaining characters. Using LEN to provide _num\_chars_ is an easy way to give MID a number that is always large enough, without the trouble of calculating exactly how many characters remain. Dropping in the value returned by the LEN function, we now have a formula that looks like this:

    =MID(B5,11,22) // returns "www.domain.com"

The MID function begins extracting at character 11 and extracts all remaining text. The final result is "www.domain.com". 

Related formulas
----------------

[![Excel formula: Get domain from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_from_email_address_0.png "Excel formula: Get domain from email address")](https://exceljet.net/formulas/get-domain-from-email-address)

### [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)

In this example, the goal is to extract just the domain name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTAFTER function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the RIGHT, LEN, and FIND...

[![Excel formula: Create email address from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create_email_address_from_name.png "Excel formula: Create email address from name")](https://exceljet.net/formulas/create-email-address-from-name)

### [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)

One of the key skills you need to be good with Excel formulas is concatenation . Put simply, concatenation is just a fancy name for joining text together. In Excel formulas, the primary operator for concatenation is the ampersand (&). A good example of a simple concatenation task is the...

[![Excel formula: Get domain name from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_name_from_url_0.png "Excel formula: Get domain name from URL")](https://exceljet.net/formulas/get-domain-name-from-url)

### [Get domain name from URL](https://exceljet.net/formulas/get-domain-name-from-url)

In this example, the goal is to extract the domain name from a list of URLs. In the current version of Excel, the easiest way to do this is to use a formula based on the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, you can use a more complicated formula based on the LEFT and FIND...

[![Excel formula: Get top level domain (TLD)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_top_level_domain_TLD.png "Excel formula: Get top level domain (TLD)")](https://exceljet.net/formulas/get-top-level-domain-tld)

### [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)

In this example, the goal is to extract the top-level domain (TLD) from a list of domains. A top-level domain is the last segment of text in a domain name, for example, ".com", ".net", or ".net". In the current version of Excel, the TEXTAFTER function is a simple way to solve this problem. In an...

[![Excel formula: Get name from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_name_from_email_address_0.png "Excel formula: Get name from email address")](https://exceljet.net/formulas/get-name-from-email-address)

### [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)

In this example, the goal is to extract the name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTBEFORE function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the LEFT and FIND functions. All three...

Related functions
-----------------

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

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

*   [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)
    
*   [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)
    
*   [Get domain name from URL](https://exceljet.net/formulas/get-domain-name-from-url)
    
*   [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)
    
*   [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)
    

### Functions

*   [MID Function](https://exceljet.net/functions/mid-function)
    
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