# Find nth occurrence of character - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/find-nth-occurrence-of-character

---

[Skip to main content](https://exceljet.net/formulas/find-nth-occurrence-of-character#main-content)

[](https://exceljet.net/formulas/find-nth-occurrence-of-character#)

*   [Previous](https://exceljet.net/formulas/find-and-replace-multiple-values)
    
*   [Next](https://exceljet.net/formulas/get-first-word)
    

[Text](https://exceljet.net/formulas#Text)

Find nth occurrence of character
================================

by Dave Bruns · Updated 23 Feb 2026

Related functions 
------------------

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[FIND](https://exceljet.net/functions/find-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: Find nth occurrence of character](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/find%20nth%20occurrence%20of%20character.png "Excel formula: Find nth occurrence of character")

Summary
-------

To find the nth occurrence of a character in a text string, you can use a formula based on the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
 together with the [LEN function](https://exceljet.net/functions/len-function)
. In the example shown, the formula in cell D5, copied down, is:

    =LEN(TEXTBEFORE(B5,"-",3))+1

As the formula is copied down, it finds the position of the third occurrence of the hyphen (-) in each text string in column B.

> Note: TEXTBEFORE is only available in newer versions of Excel. See below for a formula that will work in older versions.

Generic formula
---------------

    =LEN(TEXTBEFORE(A1, delimiter, n))+1

Explanation 
------------

In this example, the goal is to determine the position of the nth occurrence of a specific character (delimiter) in the text strings in column B. This article explains two approaches:

1.  A modern formula based on the TEXTBEFORE function.
2.  A more traditional formula for older versions of Excel.

The first option is simpler, and you should use it if you have the TEXTBEFORE function in your version of Excel. The second formula is more complex and makes sense if you don't have TEXTBEFORE.

> This formula is a great example of how [new functions](https://exceljet.net/new-excel-functions)
>  simplify previously complex Excel problems. The traditional formula is more complicated than the modern approach.

### Introduction

When working with text strings, it's common to want to determine the location of a specific occurrence of a character. For example:

*   The location of the third space (" ")
*   The location of the second hyphen ("-")
*   The location of the fourth slash ("/")
*   And so on.

Once you know the position, you can feed it into other formulas to split the text string at that position or extract text before or after that position. For a long time, this has been a challenging problem in Excel because there has been no direct way to target, say, the _third_ hypen ("-") in a text string. Functions like [FIND](https://exceljet.net/functions/find-function)
 and [SEARCH](https://exceljet.net/functions/search-function)
 are good at returning positions, but they cannot specify which instance of a character you want. They always find the _first_ instance. The introduction of the [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
 and [TEXTAFTER](https://exceljet.net/functions/textafter-function)
 functions in Excel is a big step forward because both functions provide an argument for instance number. 

### Modern formula based on TEXTBEFORE

In the latest version of Excel, we can solve this problem easily using the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
. TEXTBEFORE extracts text that appears before a specified delimiter with a syntax like this:

    =TEXTBEFORE(text,delimiter,instance_num)

For example, we can extract "ABC" from "ABC-123-XYZ" by using `-` as the delimiter and specifying the first instance:

    =TEXTBEFORE("ABC-123-XYZ", "-", 1) // returns "ABC"

The third argument, _instance\_num_, determines which occurrence of the delimiter to target. By default, it is set to `1`, meaning the first occurrence. If we provide a 2, TEXTBEFORE extracts text before that second occurrence:

    =TEXTBEFORE("ABC-123-XYZ", "-", 2) // returns "ABC-123"

We can use this behavior to figure out the location of the nth occurrence of a character, by adding in the [LEN function](https://exceljet.net/functions/len-function)
. The idea is:

*   Use `TEXTBEFORE` to extract everything before the nth occurrence of the delimiter.
*   Use `LEN` to count the length of this extracted text.
*   Add `1` to get the exact position of the nth occurrence.

The final formula in formula in cell D5 looks like this:

    =LEN(TEXTBEFORE(B5,"-",3))+1

*   `TEXTBEFORE(B5, "-", 3)`: Extracts everything before the third `-`.
*   `LEN(...)`: Returns the length of this extracted text.
*   `+1`: Gives the exact position of the next character (our target)

### Finding the position of the 1st, 2nd, 3rd, and 4th occurrence

Since this formula is simple, it's easy to customize its behavior. To find a different occurrence of a character, simply change the instance number `n` and adjust the `delimiter` as needed. The generic version of the formula looks like this:

    =LEN(TEXTBEFORE(A1,delimiter,n)) + 1

In the example below, we are using a variable number for `n` in column D and the delimiter is `*`. The formula in F5 is:

    =LEN(TEXTBEFORE(B5,"*",D5))+1

![Find the the position of each asterisk by changing n](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/find_nth_occurrence_of_character_with_variable_n.png "Find the the position of each asterisk by changing n")

The result is the position of the first, second, third, and fourth asterisk ("\*") in each text string. 

### Traditional formula for older versions of Excel

In older versions of Excel, finding the nth occurrence of a character is a bit more complicated because TEXTBEFORE is not available. Instead, we use the [FIND](https://exceljet.net/functions/find-function)
 and [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
 functions together in a formula like this:

    =FIND("~",SUBSTITUTE(B5,"-","~",3))

SUBSTITUTE is useful to us here because it has an optional instance\_num argument that allows you to target the specific occurrence of the text you want to replace. We can't use this directly to find the nth occurrence of a character, but we can use it to replace the nth occurrence with a marker that we then locate with the FIND function. The formula works as follows:

1.  `SUBSTITUTE(B5, "-", "~", 3)`: Replaces the third `-` in the text with a unique marker (`~`).
2.  `FIND("~", ...)`: Finds the position of this marker, which corresponds to the position of the third `-` in the original text.

This approach is effective but less intuitive than using TEXTBEFORE.

> It's important that you use a unique marker that doesn't appear in the text string. In this case, we use the tilde character (~) , but you can adjust to suit your needs.

### Customizing the traditional formula

The same formula structure can be used with a different delimiter. For example, to find the 4th `*`:

    =FIND("~", SUBSTITUTE(A1, "*", "~", 4))

This allows you to locate any occurrence of a character in a text string.

Summary
-------

*   The new `TEXTBEFORE` method is a bit simpler but requires a newer version of Excel.
*   The traditional `FIND` + `SUBSTITUTE` method works well in older versions of Excel.
*   Both approaches allow customization by changing the delimiter and the instance number.

Related formulas
----------------

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Replace one character with another](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/replace%20one%20character%20with%20another.png "Excel formula: Replace one character with another")](https://exceljet.net/formulas/replace-one-character-with-another)

### [Replace one character with another](https://exceljet.net/formulas/replace-one-character-with-another)

The SUBSTITUTE function is full automatic. All you need to do is supply "old text" and "new text". SUBSTITUTE will replace every instance of the old text with the new text. If you need to perform more than one replacement at the same time, you'll need to nest multiple SUBSTITUTE functions. See this...

[![Excel formula: Extract last two words from cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Extract%20last%20two%20words%20from%20cell.png "Excel formula: Extract last two words from cell")](https://exceljet.net/formulas/extract-last-two-words-from-cell)

### [Extract last two words from cell](https://exceljet.net/formulas/extract-last-two-words-from-cell)

At the core, this formula uses the MID function to extract characters starting at the second to last space. The MID function takes 3 arguments: the text to work with, the starting position, and the number of characters to extract. The text comes from column B, and the number of characters can be...

[![Excel formula: Remove last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20last%20word.png "Excel formula: Remove last word")](https://exceljet.net/formulas/remove-last-word)

### [Remove last word](https://exceljet.net/formulas/remove-last-word)

In this example, the goal is to remove the last word from the text strings in column B. This article explains two approaches: A modern formula based on the TEXTBEFORE function. A more traditional formula for older versions in Excel. The first option is much simpler, and you should use it if you...

Related functions
-----------------

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The_TEXTBEFORE_function_Play.png)](https://exceljet.net/videos/excel-textbefore-function)

### [Excel TEXTBEFORE function](https://exceljet.net/videos/excel-textbefore-function)

In this video, we'll take a look at the TEXTBEFORE function. Like the name suggests, TEXTBEFORE is designed to extract text that occurs before a specific marker, called a "delimiter". A delimiter can be one or more characters. Let's look at an example. In this worksheet, we have a list of email...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)
    
*   [Replace one character with another](https://exceljet.net/formulas/replace-one-character-with-another)
    
*   [Extract last two words from cell](https://exceljet.net/formulas/extract-last-two-words-from-cell)
    
*   [Remove last word](https://exceljet.net/formulas/remove-last-word)
    

### Functions

*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

### Videos

*   [Excel TEXTBEFORE function](https://exceljet.net/videos/excel-textbefore-function)
    

### Links

*   [Finding the nth occurrence of a character (Allen Wyatt)](https://excel.tips.net/T003324_Finding_the_Nth_Occurrence_of_a_Character.html)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
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