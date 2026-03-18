# Extract word containing specific text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/extract-word-containing-specific-text

---

[Skip to main content](https://exceljet.net/formulas/extract-word-containing-specific-text#main-content)

[](https://exceljet.net/formulas/extract-word-containing-specific-text#)

*   [Previous](https://exceljet.net/formulas/extract-text-between-parentheses)
    
*   [Next](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)
    

[Text](https://exceljet.net/formulas#Text)

Extract word containing specific text
=====================================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[MID](https://exceljet.net/functions/mid-function)

[MAX](https://exceljet.net/functions/max-function)

[FIND](https://exceljet.net/functions/find-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[REPT](https://exceljet.net/functions/rept-function)

[TRIM](https://exceljet.net/functions/trim-function)

![Excel formula: Extract word containing specific text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/extract%20word%20containing%20specific%20text.png "Excel formula: Extract word containing specific text")

Summary
-------

To extract a word that contains specific text,you can use a formula based on several functions, including TRIM, LEFT, SUBSTITUTE, MID, MAX, and REPT. You can use this formula to extract things like email addresses, or other substrings with a unique id.

In the example shown, the formula in C5 is:

    =TRIM(MID(SUBSTITUTE(B5," ",REPT(" ",99)),MAX(1,FIND("@",SUBSTITUTE(B5," ",REPT(" ",99)))-50),99))
    

Generic formula
---------------

    =TRIM(MID(SUBSTITUTE(A1," ",REPT(" ",99)),MAX(1,FIND("@",SUBSTITUTE(A1," ",REPT(" ",99)))-50),99))

Explanation 
------------

The gist: this formula "floods" the space between words in a text string with a large number of spaces, finds and extracts the substring of interest, and uses the TRIM function to clean up the mess.

Working from the inside out, the original text in B5 is flooded with spaces using SUBSTITUTE:

    SUBSTITUTE(B5," ",REPT(" ",99))
    

This replaces each single space with 99 spaces.

_Note: 99 is just an arbitrary number that represents the longest word you need to extract._

Next, the FIND function locates the specific character (in this case, "@") inside the flooded text:

    FIND("@",SUBSTITUTE(B5," ",REPT(" ",99)))-50
    

FIND returns the position of the "@" in this text, from which 50 is subtracted. Subtracting 50 effectively "walks back" the position to someplace in the middle of the spaces preceding the substring of interest. In the example shown, the calculated position is 366.

The MAX function is used to handle the problem of the substring appearing first in the text. In that case, the position will be negative, and MAX is used to reset to 1.

With a starting positing established , MID is used to extract 99 characters of text, starting at 366 from the text in B5, again flooded with space:

    MID(SUBSTITUTE(B5," ",REPT(" ",99)),366,99)
    

This extracts the substring of interest, with a lot of space characters before and after.

Finally, the TRIM function is used to trim leading and trailing space, and returns substring containing the special character.

Related formulas
----------------

[![Excel formula: Extract text between parentheses](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20text%20in%20parentheses.png "Excel formula: Extract text between parentheses")](https://exceljet.net/formulas/extract-text-between-parentheses)

### [Extract text between parentheses](https://exceljet.net/formulas/extract-text-between-parentheses)

The foundation of this formula is the MID function, which extracts a specific number of characters from text, starting at a specific location. To figure out where to start extracting text, we use this expression: SEARCH("(",B5)+1 This locates the left parentheses and adds 1 to get the position of...

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Get first word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_first_word_1.png "Excel formula: Get first word")](https://exceljet.net/formulas/get-first-word)

### [Get first word](https://exceljet.net/formulas/get-first-word)

FIND returns the position (as a number) of the first occurrence of a space character in the text. This position, minus one, is fed into the LEFT function as num\_chars . The LEFT function then extracts characters starting at the left side of the text, up to (position - 1). Handling one word If a...

[![Excel formula: Extract word that begins with specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20that%20begins%20with.png "Excel formula: Extract word that begins with specific character")](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

### [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

Starting from the inside out, the MID function is used to extract all text after "@": MID(B5,FIND("@",B5),LEN(B5)) The FIND function provides the starting point, and for total characters to extract, we just use LEN on the original text. This is a bit sloppy, but it avoids having to calculate the...

[![Excel formula: If cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20contains%20one%20of%20many%20things.png "Excel formula: If cell contains one of many things")](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

### [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

This formula uses two named ranges : things , and results . If you are porting this formula directly, be sure to use named ranges with the same names (defined based on your data). If you don't want to use named ranges, use absolute references instead. The core of this formula is this snippet:...

Related functions
-----------------

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rept%20function.png "Excel REPT function")](https://exceljet.net/functions/rept-function)

### [REPT Function](https://exceljet.net/functions/rept-function)

The Excel REPT function repeats characters a given number of times. For example, =REPT("x",5) returns "xxxxx".

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20clean%20text%20with%20CLEAN%20and%20TRIM-thumb.png)](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

### [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

When you bring data into Excel you sometimes end up with extra spaces and other characters that cause problems. Excel contains two functions that can help you clean things up. Let's take a look. Here we have a list of movie titles that were copied in from some other system. You can see that there's...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20complex%20formula%20step%20by%20step-thumb.png)](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

### [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

When you look at a complex formula in Excel you may be completely baffled at first glance, but all complex formulas are just small steps added together. Let me show you an example. Here we have a list of names. We want to pull out the first name from the full name. There's an Excel function called...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract text between parentheses](https://exceljet.net/formulas/extract-text-between-parentheses)
    
*   [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)
    
*   [Get first word](https://exceljet.net/formulas/get-first-word)
    
*   [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)
    
*   [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    

### Functions

*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [REPT Function](https://exceljet.net/functions/rept-function)
    
*   [TRIM Function](https://exceljet.net/functions/trim-function)
    

### Videos

*   [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)
    
*   [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)
    

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