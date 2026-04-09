# Remove trailing slash from url - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-trailing-slash-from-url

---

[Skip to main content](https://exceljet.net/formulas/remove-trailing-slash-from-url#main-content)

[](https://exceljet.net/formulas/remove-trailing-slash-from-url#)

*   [Previous](https://exceljet.net/formulas/remove-protocol-from-url)
    
*   [Next](https://exceljet.net/formulas/get-first-name-from-name)
    

[Internet](https://exceljet.net/formulas#Internet)

Remove trailing slash from url
==============================

by Dave Bruns · Updated 16 May 2025

Related functions 
------------------

[LEN](https://exceljet.net/functions/len-function)

[RIGHT](https://exceljet.net/functions/right-function)

[LEFT](https://exceljet.net/functions/left-function)

![Excel formula: Remove trailing slash from url](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove_trailing_slash_from_URL.png "Excel formula: Remove trailing slash from url")

Summary
-------

To remove a trailing slash ("/") from a URL or path, you can use a formula based on the [LEFT](https://exceljet.net/functions/left-function)
 and [LEN](https://exceljet.net/functions/len-function)
 functions. In the example shown, the formula in cell D5 is:

    =LEFT(B5,LEN(B5)-(RIGHT(B5)="/"))
    

As the formula is copied down, it removes the trailing slash ("/") from the URLs in column B when present. URLs that do not end in a forward slash ("/") are returned unchanged.

> See below for an easier way to solve this problem with the [REGEXREPLACE function](https://exceljet.net/functions/regexreplace-function)
>  in Excel 365.

Generic formula
---------------

    =LEFT(url,LEN(B5)-(RIGHT(url)="/"))

Explanation 
------------

The goal is to remove the forward-slash ("/") from the URLs in column B when it is present as the last character. When a URL does not end with a forward slash ("/") the original URL should be returned without modification. Despite the fact that Excel offers many functions designed to work with text strings, there is no entirely straightforward way to solve this problem. The simplest method is to use a formula based on the LEFT function with help from LEN and RIGHT.

> Sometime after I wrote this article, Excel introduced [three new regex functions](https://exceljet.net/articles/regular-expressions-in-excel)
> . One of these functions, [REGEXREPLACE](https://exceljet.net/functions/regexreplace-function)
> , can be used to solve this problem in a simple way. See below.

### LEFT formula solution

The solution in the worksheet shown is based on the [LEFT function](https://exceljet.net/functions/left-function)
. The formula in cell D5 is:

    =LEFT(B5,LEN(B5)-(RIGHT(B5)="/"))

The tricky part of this formula is that it is conditional. If a URL ends in a forward slash ("/") it is removed. If a URL does not end with a forward slash, it is returned unchanged. This could be accomplished with the IF function inside the formula, as explained later in the article. However, the formula above uses a different approach, which takes advantage of the fact that Excel will convert TRUE to 1 and FALSE to zero when prompted by a math operation. This technique is sometimes referred to as [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 and is a way to make parts of a formula conditional without using the IF function.

Video: [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

### The basic idea

At the core, this formula uses the LEFT function to return text starting from the left. If we just wanted to always remove the last character from a text string (regardless of the character) we could use a simple formula like this:

    =LEFT(B5,LEN(B5)-1)

Here, the [LEN function](https://exceljet.net/functions/len-function)
 is used to get a total count of characters in cell B5, from which we subtract 1. The result is returned to LEFT as the _num\_chars_ argument, and LEFT then returns all but the last character. This works great, but we need to remove the last character _only when it is a forward slash_. This means that we need to add conditional logic that will return LEN(B5)-1 if there is a trailing slash and LEN(B5) if there is not a trailing slash.

### Conditional logic

To work out the number of characters that should be returned conditionally, the formula uses this expression:

    LEN(B5)-(RIGHT(B5)="/")
    

Here, total characters are calculated with the LEN function as before. From this result, the result of the following expression is subtracted:

    RIGHT(B5)="/"
    

This expression uses the [RIGHT function](https://exceljet.net/functions/right-function)
 to extract the last character on the right, then tests the result to see if it is a forward slash ("/"). If the expression above returns TRUE, the math operation of subtraction will cause Excel to convert the TRUE to 1. If the expression returns FALSE, Excel will convert FALSE to zero. Therefore, when a URL ends in a forward slash "/", we subtract 1 from the count returned by LEN, and RIGHT returns all but the last character. However, when a URL does not end in "/", we subtract zero from the count returned by LEN, and RIGHT returns the entire string unchanged.

_Note: Normally, we would also give RIGHT the number of characters to extract, which is called num\_chars. However, num\_chars will default to 1 if not provided, so we omit it here since we only want the last character._

### With the IF function

The conditional logic trick above is clever, but the resulting formula is a bit cryptic. A more traditional formula below uses the IF function to accomplish the same thing:

    =LEFT(B5,IF(RIGHT(B5)="/",LEN(B5)-1,LEN(B5)))

Although slightly longer, the conditional logic in this formula is easier to read, and the formula returns the same result in the end. Select the best option to use based on your personal preference.

### With the REGEXREPLACE function

In 2024, Excel introduced support for regular expressions (regex) in formulas in the form of three new functions: [REGEXTEST](https://exceljet.net/functions/regextest-function)
, [REGEXEXTRACT](https://exceljet.net/functions/regexextract-function)
, and [REGEXREPLACE](https://exceljet.net/functions/regexreplace-function)
. We can use the REGEXREPLACE function to solve this problem cleanly like this:

    =REGEXREPLACE(B5,"/$","")

Notice that we only have a single function call for this solution. The inputs to REGEXREPLACE are as follows:

*   _text_ - `B5`
*   _pattern_ - `"/$"`
*   _replacement_ - `""`

At a high level, we are replacing the trailing slash `/` with an empty string `""`. The trick is in how we match the last character, which is done with the pattern `"/$"`. In regex, the dollar sign `$` is a special anchor character that matches the _end_ of a text string. The result is a pattern that matches the slash `/` only when it is the last character. No conditional logic is needed. If a slash appears as the last character, it will be removed. If not, the original text will be returned unchanged. Nice!

> REGEXREPLACE is only available in Excel 365 for now.

Related formulas
----------------

[![Excel formula: Remove protocol from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_protocol_from_url.png "Excel formula: Remove protocol from URL")](https://exceljet.net/formulas/remove-protocol-from-url)

### [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)

In this example, the goal is to remove the protocol from a list of URLs. To remove the protocol from a URL, we need to remove the first part of the URL. Protocols typically look like this: http:// https:// sftp:// Notice that all protocols end with a double slash ("//"). In the current version of...

[![Excel formula: Remove characters from right](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_characters_from_right.png "Excel formula: Remove characters from right")](https://exceljet.net/formulas/remove-characters-from-right)

### [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)

In this example, the goal is to remove the asterisk (\*) at the end of each text city/country name in column B. As usual, there are many ways to solve a problem like this in Excel. In the article below, we'll look at two good options. The first is a traditional formula based on the LEFT function and...

Related functions
-----------------

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

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
    
*   [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)
    

### Functions

*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    

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