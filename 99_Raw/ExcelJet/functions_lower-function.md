# Excel LOWER function | Exceljet

**Source:** https://exceljet.net/functions/lower-function

---

[Skip to main content](https://exceljet.net/functions/lower-function#main-content)

[](https://exceljet.net/functions/lower-function#)

*   [Previous](https://exceljet.net/functions/len-function)
    
*   [Next](https://exceljet.net/functions/mid-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

LOWER Function
==============

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[LOWER](https://exceljet.net/functions/lower-function)

[UPPER](https://exceljet.net/functions/upper-function)

[PROPER](https://exceljet.net/functions/proper-function)

[EXACT](https://exceljet.net/functions/exact-function)

![Excel LOWER function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20lower%20function.png "Excel LOWER function")

Summary
-------

The Excel LOWER function converts a text string to all lowercase letters. Numbers, punctuation, and spaces are not affected.

Purpose 
--------

Convert text to lower case

Return value 
-------------

Text in lower case.

Syntax
------

    =LOWER(text)

*   _text_ - The text that should be converted to lower case.

Using the LOWER function 
-------------------------

The LOWER function converts a text string to all lowercase letters. The LOWER function takes just one argument, _text_, which can be a text value or cell reference. LOWER changes any uppercase characters in the text value to lowercase. Numbers, punctuation, and spaces are not affected. LOWER will convert numbers to text with [number formatting](https://exceljet.net/glossary/number-format)
 removed.

### Examples

    =LOWER("Apple") // returns "apple"
    =LOWER("APPLE") // returns "apple"
    

Numbers or punctuation characters inside a text string are unaffected:

    =LOWER("XYY-020-KWP") // returns "xyy-020-kwp"
    

If a numeric value is given to LOWER, [number formatting](https://exceljet.net/glossary/number-format)
 is removed. For example, if cell A1 contains the date June 26, 2021, date formatting will be lost and LOWER will return a [date serial number](https://exceljet.net/glossary/excel-date)
 as text:

    =LOWER(A1) // returns "44373"
    

If necessary, you can use the [TEXT function](https://exceljet.net/functions/text-function)
 to work around this limitation. Use TEXT to convert the number to a text value, then pass that value into lower:

    =LOWER(TEXT(A1,"mmmm d, yyyy")) // returns "June 26, 2021"
    

### Related functions

Use the [LOWER function](https://exceljet.net/functions/lower-function)
 to convert text to lowercase, use the [UPPER function](https://exceljet.net/functions/upper-function)
 to convert text to uppercase, and use the [PROPER function](https://exceljet.net/functions/proper-function)
 to capitalize the words in a text string.

### Notes

*   All letters in _text_ are converted to lowercase.
*   Numbers and punctuation characters are not affected.
*   Number formatting is removed from standalone numeric values.

LOWER function examples
-----------------------

[![Excel formula: Create email address from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create_email_address_from_name.png "Excel formula: Create email address from name")](https://exceljet.net/formulas/create-email-address-from-name)

### [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)

One of the key skills you need to be good with Excel formulas is concatenation . Put simply, concatenation is just a fancy name for joining text together. In Excel formulas, the primary operator for concatenation is the ampersand (&). A good example of a simple concatenation task is the...

[![Excel formula: Count specific characters in text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_specific_characters_in_text.png "Excel formula: Count specific characters in text string")](https://exceljet.net/formulas/count-specific-characters-in-text-string)

### [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)

In this example, the goal is to count the number of occurrences of a character in a cell or text string. Strangely, Excel does not have a function dedicated to counting characters, so we need to use a formula that computes a count manually. The typical way to do this is to use a formula based on...

[![Excel formula: Normalize text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/normalize%20text.png "Excel formula: Normalize text")](https://exceljet.net/formulas/normalize-text)

### [Normalize text](https://exceljet.net/formulas/normalize-text)

The formula shown in this example uses a series of nested SUBSTITUTE functions to strip out parentheses, hyphens, colons, semi-colons, exclamation marks, commas, and periods. The process runs from the inside out, with each SUBSTITUTE replacing one character with a single space, then handing off to...

LOWER function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Dynamic%20arrays%20are%20native-PLay.png)](https://exceljet.net/videos/dynamic-arrays-are-native)

### [Dynamic arrays are native](https://exceljet.net/videos/dynamic-arrays-are-native)

In this video we'll look at how dynamic array behavior is native and deeply integrated in Excel. Although new dynamic array functions will get a lot of attention, it's important to understand that dynamic array behavior is native and deeply integrated. All formulas will now run on a new calculation...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20change%20case%20with%20UPPER%2C%20LOWER%20and%20PROPER-thumb.png)](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

### [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

When you're working with text in Excel, you'll frequently need to change case. In this video we'll look at three functions that allow you to easily change case of text in Excel: UPPER, LOWER, and PROPER. In this worksheet, we have two columns that contain names. Column B contains last names in...

Related functions
-----------------

[![Excel LOWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lower%20function.png "Excel LOWER function")](https://exceljet.net/functions/lower-function)

### [LOWER Function](https://exceljet.net/functions/lower-function)

The Excel LOWER function converts a text string to all lowercase letters. Numbers, punctuation, and spaces are not affected.

[![Excel UPPER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20upper%20function.png "Excel UPPER function")](https://exceljet.net/functions/upper-function)

### [UPPER Function](https://exceljet.net/functions/upper-function)

The Excel UPPER function converts a text string to all uppercase letters. Numbers, punctuation, and spaces are not affected.

[![Excel PROPER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20proper%20function.png "Excel PROPER function")](https://exceljet.net/functions/proper-function)

### [PROPER Function](https://exceljet.net/functions/proper-function)

The Excel PROPER function capitalizes each word in a given text string. Numbers, punctuation, and spaces are not affected.

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)
    
*   [Normalize text](https://exceljet.net/formulas/normalize-text)
    
*   [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)
    

### Videos

*   [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)
    
*   [Dynamic arrays are native](https://exceljet.net/videos/dynamic-arrays-are-native)
    

### Functions

*   [LOWER Function](https://exceljet.net/functions/lower-function)
    
*   [UPPER Function](https://exceljet.net/functions/upper-function)
    
*   [PROPER Function](https://exceljet.net/functions/proper-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    

### Links

*   [Microsoft LOWER function documentation](https://support.office.com/en-us/article/lower-function-3f21df02-a80c-44b2-afaf-81358f9fdeb4)
    

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