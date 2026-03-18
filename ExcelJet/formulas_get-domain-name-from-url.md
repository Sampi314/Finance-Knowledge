# Get domain name from URL - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-domain-name-from-url

---

[Skip to main content](https://exceljet.net/formulas/get-domain-name-from-url#main-content)

[](https://exceljet.net/formulas/get-domain-name-from-url#)

*   [Previous](https://exceljet.net/formulas/get-domain-from-email-address)
    
*   [Next](https://exceljet.net/formulas/get-name-from-email-address)
    

[Internet](https://exceljet.net/formulas#Internet)

Get domain name from URL
========================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[LEFT](https://exceljet.net/functions/left-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Get domain name from URL](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_domain_name_from_url_0.png "Excel formula: Get domain name from URL")

Summary
-------

To extract the domain from a URL path you can use a formula based on the [TEXTAFTER](https://exceljet.net/functions/textafter-function)
 and [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
 functions. In the worksheet shown, the formula in cell C5 is:

    =TEXTBEFORE(TEXTAFTER(B5,"//"),"/")

As the formula is copied down, it returns the domain name from each of the URLs shown in column B.

_Note: TEXTAFTER and TEXTBEFORE are new functions in Excel. In older versions of Excel, you can use a more complicated formula based on the LEFT and FIND functions, as explained below._

Generic formula
---------------

    =TEXTBEFORE(TEXTAFTER(url,"//"),"/")

Explanation 
------------

In this example, the goal is to extract the domain name from a list of URLs. In the current version of Excel, the easiest way to do this is to use a formula based on the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, you can use a more complicated formula based on the LEFT and FIND functions. Both approaches are explained below.

### TEXTAFTER with TEXTBEFORE

The formula in the worksheet shown uses the [TEXTAFTER](https://exceljet.net/functions/textafter-function)
 and [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
 functions to extract domain names from URLs. As the names imply, the TEXTAFTER function extracts text that occurs _after_ a given delimiter, and the TEXTBEFORE function extracts text that occurs _before_ a given delimiter. To solve this problem, each function needs just two arguments, _text_ and _delimiter_:

    =TEXTAFTER(text,delimiter)
    =TEXTBEFORE(text,delimiter)

*   _text_ - the text string to split
*   _delimiter_ - the place at which to split the text

In the worksheet shown, the formula in cell C5 uses both functions like this:

    =TEXTBEFORE(TEXTAFTER(B5,"//"),"/")

This is an example of [nesting](https://exceljet.net/glossary/nesting)
 one function inside another. Working from the inside out, the TEXTAFTER function is first used to strip the "protocol" from the URL. In this case, the protocol is the text "https://" or "http://". To locate the protocol, we use "//" for the delimiter and provide B5 for text:

    TEXTAFTER(B5,"//")

TEXTAFTER locates the double forward slash "//" and returns all text that follows. With the text "https://exceljet.net/formulas/" in cell B5, TEXTAFTER returns "exceljet.net/formulas/". This text is then handed off directly to the TEXTBEFORE function as the _text_ argument for further processing:

    =TEXTBEFORE("exceljet.net/formulas/","/")

Here, TEXTBEFORE is configured to use a single forward slash "/" for the _delimiter_. TEXTBEFORE locates the single forward slash "/" and returns all previous text. The final result is the domain "exceljet.net".

### Remove the www

If you want to remove the "www" subdomain from the domain when it is extracted, you can nest the original formula inside the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 like this:

    =SUBSTITUTE(TEXTBEFORE(TEXTAFTER(url,"//"),"/"),"www.","")

SUBSTITUTE is configured to replace "www." with an empty string (""). If "www." is not found, SUBSTITUTE returns the original result.

### Legacy Excel

In older versions of Excel without the TEXTBEFORE or TEXTAFTER functions, this is a more challenging problem. For a quick solution, you can use a formula like this:

    =LEFT(B5,FIND("/",B5,9)-1)

![Extracting the domain from a URL in older versions of Excel](https://exceljet.net/sites/default/files/images/formulas/inline/get_domain_name_from_url_legacy.png "Extracting the domain from a URL in older versions of Excel")

At the core, this formula is extracting characters from the left side of the URL with the [LEFT function](https://exceljet.net/functions/left-function)
, and using the [FIND function](https://exceljet.net/functions/find-function)
 to figure out how many characters to extract. First, FIND locates the "/" character in the URL, starting at the 9th character:

    FIND("/",B5,9)

This is the "clever" part of the formula. URLs begin with something called a "protocol" which looks like this:

http://  
https://  
ftp://  
sftp://

By starting at the 9th character, the protocol is skipped, and the FIND function will return the location of the _third_ instance of "/", which is the _first_ instance after the double slash in the protocol. With the text "https://exceljet.net/formulas/" in cell B5, the third instance of "/" is the 21st character in the URL, so FIND returns the number 21. The LEFT function then extracts 21 characters from the URL, starting at the left. The result is the domain name with a trailing slash, "https://exceljet.net/". To get the domain name without a trailing slash, we subtract 1 from the result of FIND like so:

    =LEFT(B5,FIND("/",B5,9)-1)

One limitation of this formula is that it leaves the protocol (i.e. "https://") in place. To remove the protocol in a _second step_, you can use a formula like this:

    =MID(C5,FIND("//",C5)+2,LEN(C5))

Essentially, this formula uses the [MID function](https://exceljet.net/functions/mid-function)
 and the FIND function to extract text starting after the "//". The number of characters to extract is provided by the [LEN function](https://exceljet.net/functions/len-function)
, which returns the number of characters in cell C5. This is actually a hack to keep things simple. LEN will return 30 in this case, but there are only 20 characters left to extract after the "//". This works because when the number of characters (_num\_chars_) exceeds the remaining string length MID will extract all remaining text. Using LEN to provide _num\_chars_ is a simple way to give MID a number that is always large enough.

Related formulas
----------------

[![Excel formula: Create email address from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create_email_address_from_name.png "Excel formula: Create email address from name")](https://exceljet.net/formulas/create-email-address-from-name)

### [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)

One of the key skills you need to be good with Excel formulas is concatenation . Put simply, concatenation is just a fancy name for joining text together. In Excel formulas, the primary operator for concatenation is the ampersand (&). A good example of a simple concatenation task is the...

[![Excel formula: Get domain from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_from_email_address_0.png "Excel formula: Get domain from email address")](https://exceljet.net/formulas/get-domain-from-email-address)

### [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)

In this example, the goal is to extract just the domain name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTAFTER function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the RIGHT, LEN, and FIND...

[![Excel formula: Get name from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_name_from_email_address_0.png "Excel formula: Get name from email address")](https://exceljet.net/formulas/get-name-from-email-address)

### [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)

In this example, the goal is to extract the name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTBEFORE function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the LEFT and FIND functions. All three...

[![Excel formula: Get top level domain (TLD)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_top_level_domain_TLD.png "Excel formula: Get top level domain (TLD)")](https://exceljet.net/formulas/get-top-level-domain-tld)

### [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)

In this example, the goal is to extract the top-level domain (TLD) from a list of domains. A top-level domain is the last segment of text in a domain name, for example, ".com", ".net", or ".net". In the current version of Excel, the TEXTAFTER function is a simple way to solve this problem. In an...

[![Excel formula: Remove protocol from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_protocol_from_url.png "Excel formula: Remove protocol from URL")](https://exceljet.net/formulas/remove-protocol-from-url)

### [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)

In this example, the goal is to remove the protocol from a list of URLs. To remove the protocol from a URL, we need to remove the first part of the URL. Protocols typically look like this: http:// https:// sftp:// Notice that all protocols end with a double slash ("//"). In the current version of...

Related functions
-----------------

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

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

*   [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)
    
*   [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)
    
*   [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)
    
*   [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)
    
*   [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)
    

### Functions

*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
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