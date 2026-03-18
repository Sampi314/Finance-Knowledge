# Get top level domain (TLD) - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-top-level-domain-tld

---

[Skip to main content](https://exceljet.net/formulas/get-top-level-domain-tld#main-content)

[](https://exceljet.net/formulas/get-top-level-domain-tld#)

*   [Previous](https://exceljet.net/formulas/get-page-from-url)
    
*   [Next](https://exceljet.net/formulas/remove-protocol-from-url)
    

[Internet](https://exceljet.net/formulas#Internet)

Get top level domain (TLD)
==========================

by Dave Bruns · Updated 14 Aug 2023

Related functions 
------------------

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[RIGHT](https://exceljet.net/functions/right-function)

[LEN](https://exceljet.net/functions/len-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Get top level domain (TLD)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_top_level_domain_TLD.png "Excel formula: Get top level domain (TLD)")

Summary
-------

To extract the page from a URL (i.e. the part of a path after the domain), you can use a formula based on the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
. In the example shown, the formula in D5 is:

    ="/"&TEXTAFTER(B5,"/",3)
    

As the formula is copied down, it returns the part of the path that occurs after the domain name.

_Note: TEXTAFTER is a newer function in Excel. In an older version of Excel, you can use a more complicated formula as explained below._

Generic formula
---------------

    =TEXTAFTER(domain,".",-1)

Explanation 
------------

In this example, the goal is to extract the top-level domain (TLD) from a list of domains. A top-level domain is the last segment of text in a domain name, for example, ".com", ".net", or ".net". In the current version of Excel, the TEXTAFTER function is a simple way to solve this problem. In an older version of Excel, you can use a more complicated formula based on several text functions including RIGHT, FIND, LEN, and SUBSTITUTE. Both approaches are explained below.

### TEXTAFTER function

The [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
 returns the text that occurs _after_ a given delimiter. The generic syntax for TEXTAFTER supports many options:

    =TEXTAFTER(text,delimiter,[instance_num],[match_mode],[match_end], [if_not_found])

However, for this problem, we only need to provide the first three arguments:

    =TEXTAFTER(text,delimiter,instance_num)

In the worksheet shown, the formula in cell D5 is:

    =TEXTAFTER(B5,".",-1)

The TEXTAFTER function is configured with the following inputs:

*   _text_ - the domain in cell B5
*   _delimiter_ - a dot (".")
*   _instance\_num_ - given as -1 for the last instance

With the text "https://www.domain.com" in cell B5, TEXTAFTER splits the string at the last "." and returns "com", which is the top-level domain. As the formula is copied down, the other top-level domains are returned.

For more on TEXTAFTER, see [How to use the TEXTAFTER function](https://exceljet.net/functions/textafter-function)
.

### Legacy Excel

Older versions of Excel do not provide the TEXTAFTER function. However, you can still extract the top-level domain (TLD)with a more complicated formula based on several text functions including [RIGHT](https://exceljet.net/functions/right-function)
, [FIND](https://exceljet.net/functions/find-function)
, [LEN](https://exceljet.net/functions/len-function)
, and [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
:

    =RIGHT(B5,LEN(B5)-FIND("*",SUBSTITUTE(B5,".","*",LEN(B5)-LEN(SUBSTITUTE(B5,".","")))))

This is an intimidating formula, complicated by the fact that the text functions in older versions of Excel are quite limited. However, it operates in a series of small steps. At the core, the formula uses the [RIGHT function](https://exceljet.net/functions/right-function)
 to extract characters starting from the right. All of the other functions in this formula just do one thing: they figure out how many characters (n) need to be extracted:

    =RIGHT(B5,n) // n = ??
    

At a high level, the formula replaces the _last_ dot "." in the domain with an asterisk (\*) and then uses the [FIND function](https://exceljet.net/functions/find-function)
 to locate the position of the asterisk. Once the position is known, the RIGHT function is used to extract the TLD. How does the formula know to replace only the last dot? This is the clever and complicated part. The key is here:

    SUBSTITUTE(B5,".","*",LEN(B5)-LEN(SUBSTITUTE(B5,".","")))
    

This snippet does the actual replacement of the last dot with an asterisk (\*). The trick is that the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 has an optional fourth argument that specifies which "instance" of the _old\_text_ should be replaced. If no value is supplied for _instance\_num_, SUBSTITUTE will replace _all instances_ of _old\_text_ with _new\_text_. However, if an _instance\_num_ is provided, SUBSTITUTE will only replace that particular instance of old\_text (i.e. if 2 is provided, SUBSTITUTE will replace the second instance). Figuring out which instance to replace is the hardest part of this problem because we have no direct way to count how many dots are in a text string. Instead, we need to take a manual approach based on the  [LEN function](https://exceljet.net/functions/len-function)
:

    LEN(B5)-LEN(SUBSTITUTE(B5,".",""))
    

Here, we calculate the total number of characters in the domain with LEN, then we subtract the total number of characters with all dots removed with the SUBSTITUTE function. For example, the value in cell B5 is "https://www.domain.com". The above expression evaluates like this:

    =LEN(B5)-LEN(SUBSTITUTE(B5,".",""))
    =22-20
    =2
    

The result (2) is the number of dots in the text, which is provided to SUBSTITUTE as _instance\_num_:

    SUBSTITUTE(B5,".","*",2)
    

SUBSTITUTE then replaces only the second dot with "\*" resulting in the text "https://www.domain\*com". Next, the FIND function locates the asterisk in the text:

    FIND("*","https://www.domain*com") // returns 19
    

The result from FIND is 19, which is subtracted from the total length of the domain:

    =LEN(B5)-19
    =22-19
    =3

The number 3 is returned to the FIND function as _num\_chars_:

    =RIGHT(B5,3) // returns "com"

And the final result returned by RIGHT is "com"

Related formulas
----------------

[![Excel formula: Get domain from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_from_email_address_0.png "Excel formula: Get domain from email address")](https://exceljet.net/formulas/get-domain-from-email-address)

### [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)

In this example, the goal is to extract just the domain name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTAFTER function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the RIGHT, LEN, and FIND...

[![Excel formula: Get middle name from full name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_middle_name_from_name_0.png "Excel formula: Get middle name from full name")](https://exceljet.net/formulas/get-middle-name-from-full-name)

### [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)

In this example, the goal is to return the middle name from a full name in "First Middle Last" format. In the current version of Excel this is a fairly simple problem using the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, a similar formula is significantly more complicated, based...

[![Excel formula: Create email address from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create_email_address_from_name.png "Excel formula: Create email address from name")](https://exceljet.net/formulas/create-email-address-from-name)

### [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)

One of the key skills you need to be good with Excel formulas is concatenation . Put simply, concatenation is just a fancy name for joining text together. In Excel formulas, the primary operator for concatenation is the ampersand (&). A good example of a simple concatenation task is the...

[![Excel formula: Get domain name from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_name_from_url_0.png "Excel formula: Get domain name from URL")](https://exceljet.net/formulas/get-domain-name-from-url)

### [Get domain name from URL](https://exceljet.net/formulas/get-domain-name-from-url)

In this example, the goal is to extract the domain name from a list of URLs. In the current version of Excel, the easiest way to do this is to use a formula based on the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, you can use a more complicated formula based on the LEFT and FIND...

[![Excel formula: Get name from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_name_from_email_address_0.png "Excel formula: Get name from email address")](https://exceljet.net/formulas/get-name-from-email-address)

### [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)

In this example, the goal is to extract the name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTBEFORE function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the LEFT and FIND functions. All three...

[![Excel formula: Remove protocol from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_protocol_from_url.png "Excel formula: Remove protocol from URL")](https://exceljet.net/formulas/remove-protocol-from-url)

### [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)

In this example, the goal is to remove the protocol from a list of URLs. To remove the protocol from a URL, we need to remove the first part of the URL. Protocols typically look like this: http:// https:// sftp:// Notice that all protocols end with a double slash ("//"). In the current version of...

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

*   [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)
    
*   [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)
    
*   [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)
    
*   [Get domain name from URL](https://exceljet.net/formulas/get-domain-name-from-url)
    
*   [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)
    
*   [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)
    

### Functions

*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
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