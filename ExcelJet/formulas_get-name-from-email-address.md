# Get name from email address - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-name-from-email-address

---

[Skip to main content](https://exceljet.net/formulas/get-name-from-email-address#main-content)

[](https://exceljet.net/formulas/get-name-from-email-address#)

*   [Previous](https://exceljet.net/formulas/get-domain-name-from-url)
    
*   [Next](https://exceljet.net/formulas/get-page-from-url)
    

[Internet](https://exceljet.net/formulas#Internet)

Get name from email address
===========================

by Dave Bruns · Updated 11 Aug 2023

Related functions 
------------------

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[LEFT](https://exceljet.net/functions/left-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Get name from email address](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_name_from_email_address_0.png "Excel formula: Get name from email address")

Summary
-------

To extract the name from an email address, you can use a formula based on the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
. In the example shown, the formula in D5 is:

    =TEXTBEFORE(C5,"@")
    

As the formula is copied down the table, it extracts the name from each email address as shown.

_Notes: (1) TEXTBEFORE is a newer function in Excel. In older versions of Excel, you can use a formula based on the LEFT function as explained below. (2) All emails shown in the worksheet are fictional._

Generic formula
---------------

    =TEXTBEFORE(A1,"@")

Explanation 
------------

In this example, the goal is to extract the name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTBEFORE function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the LEFT and FIND functions. All three options are explained below.

### TEXTBEFORE function

The [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
 returns the text that occurs _before_ a given delimiter. The generic syntax for TEXTBEFORE supports many options:

    =TEXTBEFORE(text,delimiter,[instance_num],[match_mode],[match_end],[if_not_found])

However, most of these arguments are optional. For this problem, we only need to provide the first two arguments, _text_ and _delimiter_:

    =TEXTBEFORE(text,delimiter)

_Text_ is the text string to split, and _delimiter_ is the location at which to split the string. Since all email addresses contain the "@" character separating the name from the domain, we can extract the name with a formula like this:

    =TEXTBEFORE(C5,"@")

As the formula is copied down the column, it extracts the name from each of the emails as shown in the worksheet. For more details on TEXTBEFORE, see [How to use the TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
.

_Note: You can use the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
 to extract the domain from the email._

### TEXTSPLIT function

Another easy way to solve this problem is with the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
, which is designed to split a text string at a given delimiter and return all parts of the split string in a single step. To solve this problem with TEXTSPLIT, use a formula like this in cell D5:

    =TEXTSPLIT(C5,"@")

As the formula is copied down, TEXTSPLIT will split the email at the @ character and return the name and the domain. These two values will spill into column D and column E as seen below:

![Using TEXTSPLIT to get name and domain from an email address](https://exceljet.net/sites/default/files/images/formulas/inline/get_name_from_email_address_with_textsplit.png "Using TEXTSPLIT to get name and domain from an email address")

The advantage of this approach is that you get both the email and the domain with a single formula. For more details on TEXTSPLIT, see [How to use the TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
.

### Legacy Excel

In older versions of Excel that do not provide the TEXTBEFORE  or TEXTSPLIT functions, you can use a formula based on the [LEFT](https://exceljet.net/functions/left-function)
 and [FIND](https://exceljet.net/functions/find-function)
 functions:

    =LEFT(C5,FIND("@",C5)-1)
    

At the core, this formula extracts characters _from the left_ with the LEFT function, using FIND to figure out how many characters to extract. C5 contains the email "john.doe123@abc.com", so FIND returns 12, since the "@" occurs as the 12th character. We then subtract 1 to prevent the formula from extracting the "@" along with the name:

    FIND("@",C5)-1 // returns 11
    

The result is 11, which is returned directly to the LEFT function as the _num\_chars_ argument:

    =LEFT(C5,11) // returns "john.doe123"
    

The final result returned by LEFT is "john.doe123". As the formula is copied down the column, it performs the same operation on each email address. Although this formula is more complicated than the TEXTBEFORE or TEXTSPLIT options above, it achieves the same result.

Related formulas
----------------

[![Excel formula: Create email address from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create_email_address_from_name.png "Excel formula: Create email address from name")](https://exceljet.net/formulas/create-email-address-from-name)

### [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)

One of the key skills you need to be good with Excel formulas is concatenation . Put simply, concatenation is just a fancy name for joining text together. In Excel formulas, the primary operator for concatenation is the ampersand (&). A good example of a simple concatenation task is the...

[![Excel formula: Get domain from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_from_email_address_0.png "Excel formula: Get domain from email address")](https://exceljet.net/formulas/get-domain-from-email-address)

### [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)

In this example, the goal is to extract just the domain name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTAFTER function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the RIGHT, LEN, and FIND...

[![Excel formula: Get domain name from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_name_from_url_0.png "Excel formula: Get domain name from URL")](https://exceljet.net/formulas/get-domain-name-from-url)

### [Get domain name from URL](https://exceljet.net/formulas/get-domain-name-from-url)

In this example, the goal is to extract the domain name from a list of URLs. In the current version of Excel, the easiest way to do this is to use a formula based on the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, you can use a more complicated formula based on the LEFT and FIND...

[![Excel formula: Get top level domain (TLD)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_top_level_domain_TLD.png "Excel formula: Get top level domain (TLD)")](https://exceljet.net/formulas/get-top-level-domain-tld)

### [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)

In this example, the goal is to extract the top-level domain (TLD) from a list of domains. A top-level domain is the last segment of text in a domain name, for example, ".com", ".net", or ".net". In the current version of Excel, the TEXTAFTER function is a simple way to solve this problem. In an...

[![Excel formula: Remove protocol from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_protocol_from_url.png "Excel formula: Remove protocol from URL")](https://exceljet.net/formulas/remove-protocol-from-url)

### [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)

In this example, the goal is to remove the protocol from a list of URLs. To remove the protocol from a URL, we need to remove the first part of the URL. Protocols typically look like this: http:// https:// sftp:// Notice that all protocols end with a double slash ("//"). In the current version of...

Related functions
-----------------

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20extract%20text%20with%20LEFT%20and%20RIGHT-thumb_0.png)](https://exceljet.net/videos/how-to-extract-text-with-left-and-right)

### [How to extract text with LEFT and RIGHT](https://exceljet.net/videos/how-to-extract-text-with-left-and-right)

In this video, we'll look at how to use the RIGHT and LEFT functions to extract specific text from data. Let's take a look. Here we have some customer data. To illustrate how to extract text using the LEFT and RIGHT functions, I'll use them both to pull out just certain parts of this information...

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
    
*   [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)
    
*   [Get domain name from URL](https://exceljet.net/formulas/get-domain-name-from-url)
    
*   [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)
    
*   [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)
    

### Functions

*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

### Videos

*   [How to extract text with LEFT and RIGHT](https://exceljet.net/videos/how-to-extract-text-with-left-and-right)
    
*   [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)
    

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