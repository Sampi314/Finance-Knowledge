# Get domain from email address - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-domain-from-email-address

---

[Skip to main content](https://exceljet.net/formulas/get-domain-from-email-address#main-content)

[](https://exceljet.net/formulas/get-domain-from-email-address#)

*   [Previous](https://exceljet.net/formulas/create-email-with-display-name)
    
*   [Next](https://exceljet.net/formulas/get-domain-name-from-url)
    

[Internet](https://exceljet.net/formulas#Internet)

Get domain from email address
=============================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[RIGHT](https://exceljet.net/functions/right-function)

[LEN](https://exceljet.net/functions/len-function)

[FIND](https://exceljet.net/functions/find-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7951/download?token=o6hRhkOH)
 (19.26 KB)

![Excel formula: Get domain from email address](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_domain_from_email_address_0.png "Excel formula: Get domain from email address")

Summary
-------

To extract the domain from an email address, you can use a formula based on the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
. In the example shown, the formula in E5 is:

    =TEXTAFTER(C5,"@")
    

As the formula is copied down the table, it extracts the domain name from each email as shown.

_Notes: (1) TEXTAFTER is a newer function in Excel. In older versions of Excel, you can use a formula based on the RIGHT function as explained below. (2) All emails shown in the worksheet are fictional._

Generic formula
---------------

    =TEXTAFTER(A1,"@")

Explanation 
------------

In this example, the goal is to extract just the domain name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTAFTER function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the RIGHT, LEN, and FIND functions. All three options are explained below.

### TEXTAFTER function

The [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
 returns the text that occurs _after_ a given delimiter. The generic syntax for TEXTAFTER supports quite a number of options:

    =TEXTAFTER(text,delimiter,[instance_num],[match_mode],[match_end], [if_not_found])

However, most of the inputs are optional and for this problem, we only need to provide the first two arguments:

    =TEXTAFTER(text,delimiter)

Here, _text_ represents the text string to parse, and _delimiter_ represents the place at which to begin extracting. Since all email addresses contain the @ character separating the name from the domain, we can extract the domain with a simple formula like this:

    =TEXTAFTER(C5,"@")

As the formula is copied down the table, it extracts the domain name from each of the emails as shown in the worksheet. For more information, see [How to use the TEXTAFTER function](https://exceljet.net/functions/textafter-function)
.

_Note: You can use the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
 to extract the name portion of the email._

### TEXTSPLIT function

Another easy way to solve this problem is with the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
, which is designed to split a text string at a given delimiter and return all pieces of the string in a single step. To solve this problem with TEXTSPLIT, use a formula like this in cell D5:

    =TEXTSPLIT(C5,"@")

As the formula is copied down, TEXTSPLIT will split the email at the @ character and return the name and the domain in one step:

![Get domain from email with the TEXTSPLIT function](https://exceljet.net/sites/default/files/images/formulas/inline/get_domain_from_email_with_textsplit.png "Get domain from email with the TEXTSPLIT function")

The advantage of this approach is that you get both the email and the domain with a single formula. For more details on TEXTSPLIT, see [How to use the TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
.

### Legacy Excel

In older versions of Excel that do not provide the TEXTAFTER  or TEXTSPLIT functions, you can use a formula based on the [RIGHT](https://exceljet.net/functions/right-function)
, [LEN](https://exceljet.net/functions/len-function)
, and [FIND](https://exceljet.net/functions/find-function)
 functions:

    =RIGHT(C5,LEN(C5)-FIND("@",C5))
    

At the core, this formula extracts characters from the right with the RIGHT function, using FIND and LEN to figure out how many characters to extract. C5 contains the text "john.doe123@abc.com", so LEN returns 19 characters:

    LEN(C5) // returns 19
    

FIND locates the "@" character inside the email address "john.doe123@abc.com". The "@" character is the 12th character, so FIND returns 12:

    FIND("@",C5) // returns 12
    

Next, 12 is subtracted from 19, and the result (7) is returned directly to the RIGHT function as the _num\_chars_ argument. The RIGHT function then extracts 7 characters from the email address, _starting from the right_, and returns "abc.com" as a final result. The complete formula is evaluated like this:

    =RIGHT(C5,LEN(C5)-FIND("@",C5))
    =RIGHT(C5,19-12)
    =RIGHT(C5,7) // returns "abc.com"
    

Although this formula is more complicated than the formulas based on TEXTAFTER or TEXTSPLIT, it will work just fine. If you get unexpected results, you might need to run the email addresses through the [TRIM function](https://exceljet.net/functions/trim-function)
 to strip leading or trailing spaces, since trailing spaces will cause incorrect results. Once you have trimmed email addresses, apply the formula above.

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

[![Excel formula: Create email address from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create_email_address_from_name.png "Excel formula: Create email address from name")](https://exceljet.net/formulas/create-email-address-from-name)

### [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)

One of the key skills you need to be good with Excel formulas is concatenation . Put simply, concatenation is just a fancy name for joining text together. In Excel formulas, the primary operator for concatenation is the ampersand (&). A good example of a simple concatenation task is the...

[![Excel formula: Remove protocol from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_protocol_from_url.png "Excel formula: Remove protocol from URL")](https://exceljet.net/formulas/remove-protocol-from-url)

### [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)

In this example, the goal is to remove the protocol from a list of URLs. To remove the protocol from a URL, we need to remove the first part of the URL. Protocols typically look like this: http:// https:// sftp:// Notice that all protocols end with a double slash ("//"). In the current version of...

Related functions
-----------------

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

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

*   [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)
    
*   [Get domain name from URL](https://exceljet.net/formulas/get-domain-name-from-url)
    
*   [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)
    
*   [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)
    
*   [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)
    

### Functions

*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
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