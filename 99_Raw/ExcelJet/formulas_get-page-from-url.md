# Get page from URL - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-page-from-url

---

[Skip to main content](https://exceljet.net/formulas/get-page-from-url#main-content)

[](https://exceljet.net/formulas/get-page-from-url#)

*   [Previous](https://exceljet.net/formulas/get-name-from-email-address)
    
*   [Next](https://exceljet.net/formulas/get-top-level-domain-tld)
    

[Internet](https://exceljet.net/formulas#Internet)

Get page from URL
=================

by Dave Bruns · Updated 14 Aug 2023

Related functions 
------------------

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Get page from URL](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_page_from_url.png "Excel formula: Get page from URL")

Summary
-------

To extract the page from a URL (i.e. the part of a path after the domain), you can use a formula based on the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
. In the example shown, the formula in D5 is:

    ="/"&TEXTAFTER(B5,"/",3)
    

As the formula is copied down, it returns the part of the path that occurs after the domain name.

_Note: TEXTAFTER is a newer function in Excel. In an older version of Excel, you can use a formula based on the MID and LEN functions, as explained below._

Generic formula
---------------

    =TRIM(RIGHT(SUBSTITUTE(url,"/",REPT(" ",100)),100))

Explanation 
------------

In this example, we have a list of URLs. The goal is to get the portion of each URL that appears after the domain name. In the current version of Excel, the easiest way to do this is to use the TEXTAFTER function. In an older version of Excel, you can use a formula based on the MID, FIND, and LEN functions. Both approaches are explained below.

### TEXTAFTER function

The [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
 returns the text that occurs _after_ a given delimiter. The generic syntax for TEXTAFTER supports quite a number of options:

    =TEXTAFTER(text,delimiter,[instance_num],[match_mode],[match_end], [if_not_found])

However, most of the inputs are optional and for this problem, we only need to provide the first three arguments:

    =TEXTAFTER(text,delimiter,instance_num)

In the worksheet shown, the formula in cell D5 is:

    ="/"&TEXTAFTER(B5,"/",3)

The TEXTAFTER function is configured with the following inputs:

*   _text_ - the URL in cell B5
*   _delimiter_ - a forward slash "/"
*   _instance\_num_ - 3, for the third occurrence of "/"

With the text "https://exceljet.net/formulas" in cell B5, TEXTAFTER splits the string at the third "/" and returns "formulas". Next, a forward slash "/" is prepended to the result from TEXTAFTER with [concatenation](https://exceljet.net/glossary/concatenation)
 to create a final result that begins with "/". This last step is necessary because TEXTAFTER does not include the delimiter used to split the text, so it needs to be added back manually if desired.

### Legacy Excel

TEXTAFTER is a new function in Excel. In an older version of Excel, you can solve this problem with a formula based on the MID, FIND, and LEN functions:

    =MID(B5,FIND("/",B5,9),LEN(B5))

At the core, this formula is extracting characters with the [MID function](https://exceljet.net/functions/mid-function)
, and using the [FIND function](https://exceljet.net/functions/find-function)
 to figure out where to begin extracting. First, FIND locates the "/" character in the URL, starting at the 9th character:

    FIND("/",B5,9)

This is the "clever" part of the formula. URLs begin with something called a "protocol" (i.e. "http://", "https://", "ftp://", "sftp://", etc.) By starting at the 9th character, the protocol is skipped, and the FIND function returns the location of the _third_ instance of "/", which is the _first_ forward slash "/" after the protocol. With the text "https://exceljet.net/formulas" in cell B5, the third instance of "/" is the 21st character in the URL, so FIND returns the number 21 to the MID function as the _start\_num_ argument. At this point, we have:

    =MID(B5,21,LEN(B5))

To provide a value for the _num\_chars_ argument, we use the [LEN function](https://exceljet.net/functions/len-function)
, which returns a count of all the characters in B5. This is a "hack" to keep things simple. LEN will return 29 in this case, the total number of characters in the text "https://exceljet.net/formulas". This means there are only 20 characters remaining after the "//". However, the MID function doesn't care if the number of characters (_num\_chars_) exceeds the remaining string length. MID will just keep extracting characters until the end of the string. In other words, using LEN to provide _num\_chars_ is an easy way to give MID a number that is always enough to get the job done. Dropping in the value returned by the LEN function, we now have a formula that looks like this:

    =MID(B5,21,29) // returns "/formulas"

The MID function begins extracting at character 21 and extracts all of the remaining text. The final result is "/formulas".  Unlike the TEXTAFTER version of the formula above, there is no need to concatenate a "/" to the beginning, since the MID function _includes_ the delimiter in the result.

Related formulas
----------------

[![Excel formula: Remove protocol from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_protocol_from_url.png "Excel formula: Remove protocol from URL")](https://exceljet.net/formulas/remove-protocol-from-url)

### [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)

In this example, the goal is to remove the protocol from a list of URLs. To remove the protocol from a URL, we need to remove the first part of the URL. Protocols typically look like this: http:// https:// sftp:// Notice that all protocols end with a double slash ("//"). In the current version of...

[![Excel formula: Remove trailing slash from url](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_trailing_slash_from_URL.png "Excel formula: Remove trailing slash from url")](https://exceljet.net/formulas/remove-trailing-slash-from-url)

### [Remove trailing slash from url](https://exceljet.net/formulas/remove-trailing-slash-from-url)

The goal is to remove the forward-slash ("/") from the URLs in column B when it is present as the last character. When a URL does not end with a forward slash ("/") the original URL should be returned without modification. Despite the fact that Excel offers many functions designed to work with text...

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

*   [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)
    
*   [Remove trailing slash from url](https://exceljet.net/formulas/remove-trailing-slash-from-url)
    

### Functions

*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
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