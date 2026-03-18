# Remove last word - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-last-word

---

[Skip to main content](https://exceljet.net/formulas/remove-last-word#main-content)

[](https://exceljet.net/formulas/remove-last-word#)

*   [Previous](https://exceljet.net/formulas/remove-first-character)
    
*   [Next](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)
    

[Text](https://exceljet.net/formulas#Text)

Remove last word
================

by Dave Bruns · Updated 7 Mar 2025

Related functions 
------------------

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[TRIM](https://exceljet.net/functions/trim-function)

[MID](https://exceljet.net/functions/mid-function)

[FIND](https://exceljet.net/functions/find-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[LEN](https://exceljet.net/functions/len-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8994/download?token=wcOE-1F6)
 (21.95 KB)

![Excel formula: Remove last word](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove%20last%20word.png "Excel formula: Remove last word")

Summary
-------

To remove the last word from a text string, you can use a formula based on the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
 together with the [TRIM function](https://exceljet.net/functions/trim-function)
. In the example shown, the formula in cell D5, copied down, is:

    =TEXTBEFORE(TRIM(B5)," ",-1)

As the formula is copied down, it removes the last word from each text string in column B.

> Note: TEXTBEFORE is only available in newer versions of Excel. See below for a formula that will work in older versions.

Generic formula
---------------

    =TEXTBEFORE(TRIM(B5)," ",-n)

Explanation 
------------

In this example, the goal is to remove the last word from the text strings in column B. This article explains two approaches:

1.  A modern formula based on the TEXTBEFORE function.
2.  A more traditional formula for older versions in Excel.

The first option is much simpler, and you should use it if you have the TEXTBEFORE function. The second formula is significantly more complex and only makes sense if you don't have TEXTBEFORE.

> This formula is a great example of how [new functions](https://exceljet.net/new-excel-functions)
>  in Excel completely change how problems are solved. The traditional formula is much more complex than the modern formula. 

### Modern formula based on TEXTBEFORE

In the latest version of Excel, we can easily solve this problem with the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
. TEXTBEFORE is designed to extract text that occurs before a given delimiter with a syntax like this:

    =TEXTBEFORE(text,delimiter)

For example, we can extract "Bob" from "Bob Alan Jones" by using a space as a delimiter like this:

    =TEXTBEFORE("Bob Alan Jones"," ") // returns "Bob"

The third argument for TEXTBEFORE is called "instance\_num" and specifies the instance of the delimiter as a numeric index (i.e., instance 1, instance 2, instance 3, etc.) This argument is optional and defaults to 1. This is why we get "Bob" when we don't provide a value for _instance\_num_. If we set _instance\_num_ to 2, we get "Bob Alan":

    =TEXTBEFORE("Bob Alan Jones"," ",2) // returns "Bob Alan"

The instance number can also be provided as a _negative_ number, which counts from the _end_ of the text string:

    =TEXTBEFORE("Bob Alan Jones"," ",-2) // returns "Bob"
    =TEXTBEFORE("Bob Alan Jones"," ",-1) // returns "Bob Alan"

This feature is the key to using TEXTBEFORE to solve this problem. Since we don't know how many words a text string will contain, we don't know what (positive) instance number to provide to TEXTBEFORE to target text before the last word. However, if we switch to a negative instance number, we can easily target the last word by using -1 for _instance\_num._ The meaning is "first space from the end" which is the same as "last space from the start". The formula looks like this:

    =TEXTBEFORE(B5," ",-1)

This will work fine as long as the text string in B5 always contains words separated by just one space (" "). However, if the number of spaces between words is irregular, or if there are extra spaces after the text, the formula may not work correctly. To avoid this problem, we ensure the spacing is consistent by nesting the [TRIM function](https://exceljet.net/functions/trim-function)
 inside TEXTBEFORE:

    =TEXTBEFORE(TRIM(B5)," ",-1)

Inside TEXTBEFORE, the TRIM function normalizes the space in the text string from cell B5. TRIM makes sure there is just one space between words and removes any leading or trailing spaces. The "trimmed" text is returned directly to TEXTBEFORE as the _text_ argument. The TEXTBEFORE function then returns all text before the last word, effectively removing the last word.

### Customizing the modern formula

Since this formula is so simple, it's easy to customize its behavior. To remove more than the last word (i.e., the last two words, the last three words, etc.), we only need to adjust the instance number:

    =TEXTBEFORE(TRIM(A1)," ",-1) // remove last word
    =TEXTBEFORE(TRIM(A1)," ",-2) // remove last two words
    =TEXTBEFORE(TRIM(A1)," ",-3) // remove last three words

The generic formula to return the last n words looks like this:

    =TEXTBEFORE(TRIM(A1)," ",-n)

_Note: If you provide a value for n that is out of range, TEXTBEFORE will return a #N/A error._

We can also easily change the delimiter used to separate words. For example, to remove the last 2 words separated by hyphens, we can use a formula like this:

    =TEXTBEFORE(TRIM(A1),"-",-2)

You can see how this works in the worksheet below:

![Customized formula to remove the last two words separated by hyphens](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/remove_last_two_words_example.png "Customized formula to remove the last two words separated by hyphens")

### Traditional formula for older versions of Excel

In older versions of Excel, this is a much harder problem to solve because there is no easy way to split text at the last space. A classic traditional formula solution looks like this:

    =MID(B5,1,FIND("~",SUBSTITUTE(B5," ","~",LEN(B5)-LEN(SUBSTITUTE(B5," ",""))))-1)

At the highest level, this formula uses the MID function to remove the last word from a text string. The challenge is to figure out where the last word begins and set a marker before the last word. Then, we can locate the marker with FIND and extract everything up to that point. The formula is convoluted, but the steps are simple. First, we count how many spaces exist in the text using LEN and SUBSTITUTE like this:

    LEN(B5)-LEN(SUBSTITUTE(B5," ","")) // returns 6

[This page](https://exceljet.net/formulas/count-specific-characters-in-text-string)
 explains this part of the formula in more detail. Next, we use the somewhat obscure _instance_ argument in the SUBSTITUTE function to replace the _last_ space with a tilde (~):

    SUBSTITUTE(B5," ","~",6) // insert tilde

> We use a tilde (~) only because it's a rarely occurring character. You can use any character you like, so long as it doesn't appear in the source text.

At this point in the process, the formula looks like this:

    =MID(B5,1,FIND("~","It's been seven hours and fifteen~days")-1)

Notice that the tilde (~) acts as a marker to indicate where the last word begins. Next, we use FIND to figure out where the tilde is:

    FIND("~","It's been seven hours and fifteen~days") // returns 34

FIND returns 34 because the tilde is the 34th character in the text string. Because we don't want to extract the tilde itself, we subtract 1 from the number that FIND returns. The result, 33, is returned to the MID function as the _num\_chars_ argument. We are finally ready to extract text. At this point, we can simply the formula as follows:

    =MID(B5,1,33)

The MID function extracts all text from character 1 through character 33, effectively removing the last word from the original text in cell B5.

> This formula is a great example of how [new functions](https://exceljet.net/new-excel-functions)
>  in Excel completely change how tricky problems are solved. The traditional formula is much more complex and much less transparent than the TEXTBEFORE solution. Plus, we haven't even accounted for irregular spacing, which would require adding the TRIM function around each instance of B5 in the formula, which would make the formula even more complicated.

### Customizing the traditional formula

The same formula structure can be used with a different delimiter. For example, to remove all text after the last forward slash "/", you can use a generic formula like this:

    =MID(A1,1,FIND("~",SUBSTITUTE(A1,"/","~",LEN(A1)-LEN(SUBSTITUTE(A1,"/",""))))-1)

You can also adapt the formula to remove the last 2 words, last 3 words, etc. The general form for this formula looks like this:

    =MID(A1,1,FIND("~",SUBSTITUTE(A1,d,"~",LEN(A1)-LEN(SUBSTITUTE(A1,d,""))-(n-1)))-1)
    

In the above formula, **n** is the number of words to remove, and **d** represents the delimiter to use.

Related formulas
----------------

[![Excel formula: Remove text by position](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20text%20by%20position.png "Excel formula: Remove text by position")](https://exceljet.net/formulas/remove-text-by-position)

### [Remove text by position](https://exceljet.net/formulas/remove-text-by-position)

The replace function lets you replace text based on its location and length. In this case, we want to strip off the drive and path and leave only the document name. The length of this part of the string (text) is 24 and the starting position is 1, and the pattern never changes. The REPLACE function...

[![Excel formula: Remove text by variable position](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20text%20by%20variable%20position.png "Excel formula: Remove text by variable position")](https://exceljet.net/formulas/remove-text-by-variable-position)

### [Remove text by variable position](https://exceljet.net/formulas/remove-text-by-variable-position)

The REPLACE function will replace text by position. You can use REPLACE to remove text by providing an empty string ("") for the "new\_text" argument. In this case, we want to remove the labels that appear inside text. The labels vary in length, and include words like "Make", "Model", "Fuel economy...

[![Excel formula: Remove characters from right](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_characters_from_right.png "Excel formula: Remove characters from right")](https://exceljet.net/formulas/remove-characters-from-right)

### [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)

In this example, the goal is to remove the asterisk (\*) at the end of each text city/country name in column B. As usual, there are many ways to solve a problem like this in Excel. In the article below, we'll look at two good options. The first is a traditional formula based on the LEFT function and...

Related functions
-----------------

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

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

*   [Remove text by position](https://exceljet.net/formulas/remove-text-by-position)
    
*   [Remove text by variable position](https://exceljet.net/formulas/remove-text-by-variable-position)
    
*   [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)
    

### Functions

*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [TRIM Function](https://exceljet.net/functions/trim-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

### Videos

*   [Excel TEXTBEFORE function](https://exceljet.net/videos/excel-textbefore-function)
    

### Training

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