# Convert text to numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-text-to-numbers

---

[Skip to main content](https://exceljet.net/formulas/convert-text-to-numbers#main-content)

[](https://exceljet.net/formulas/convert-text-to-numbers#)

*   [Previous](https://exceljet.net/formulas/convert-numbers-to-text)
    
*   [Next](https://exceljet.net/formulas/count-keywords-cell-contains)
    

[Text](https://exceljet.net/formulas#Text)

Convert text to numbers
=======================

by Dave Bruns · Updated 12 Jul 2025

Related functions 
------------------

[VALUE](https://exceljet.net/functions/value-function)

[LEFT](https://exceljet.net/functions/left-function)

[RIGHT](https://exceljet.net/functions/right-function)

[REGEXREPLACE](https://exceljet.net/functions/regexreplace-function)

[ISTEXT](https://exceljet.net/functions/istext-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: Convert text to numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert_text_to_numbers.png "Excel formula: Convert text to numbers")

Summary
-------

To convert text values to numbers, you can use the [VALUE function](https://exceljet.net/functions/value-function)
, or simply add zero as described below. In the example shown, the formula in D5 is:

    =VALUE(B5)
    

As the formula is copied down it converts the text values in column B to the numbers seen in column D. Note that, by default, Excel will _left-align_ text values and _right-align_ numeric values.

Generic formula
---------------

    =VALUE(A1)

Explanation 
------------

In this example, the goal is to convert the text values seen in column B to the numeric values seen in column D.  There are several ways to fix this problem in Excel, but this article focuses on a formula-based approach to convert text values to numbers. It also explains how to convert values in place with Paste Special, which does not require a formula.

### The problem

Sometimes Excel will incorrectly evaluate a number as a text value. There are many reasons this might happen, including:

1.  The data has been imported from another application, and Excel has misinterpreted values.
2.  Data has been copy-pasted into Excel, and Excel does not recognize values as numbers.
3.  A user has added spaces, hyphens, commas, etc., to a number, changing it to text.
4.  The output of another formula is text, but expected to be a number.

Regardless of the cause, the problem is that a value that looks like a number but is actually text can't be used in Excel like a true number. If you try to use it in a formula, you will typically get a #VALUE! error

### Checking for numbers and text

In this example, the values in column B are "stored as text". One way to understand how Excel is interpreting a value is to check the alignment. By default, Excel will align numeric values to the _right_ side of a cell and text values to the _left_ side of a cell, as you can see in the worksheet above. Alignment can be changed, however, so this is not a foolproof method of checking values.

Another way to check for numbers is to sum the values with the SUM function. The SUM function will ignore text values, so if the result is zero, you know that you have text values. You can also test values more explicitly with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 or the [ISTEXT function](https://exceljet.net/functions/istext-function)
. Both formulas below will return either TRUE or FALSE for a value in cell A1:

    =ISNUMBER(A1) // test for numbers
    =ISTEXT(A1) // test for text

### VALUE function

The [VALUE function](https://exceljet.net/functions/value-function)
 converts text that appears in a recognized format (i.e., a number, date, or time format) into a numeric value. When VALUE can successfully convert a text value to a number, it will just work, and VALUE will return the corresponding number. In cases where VALUE is not able to convert a text value to a number, it will return a #VALUE error.

### Add zero (+0) trick

Another way to convert a text value to a number is to add zero with a formula like this:

    =A1+0
    

The math operation forces Excel to try to convert the text value to a number. If the conversion succeeds, a number will be returned. If the conversion fails, the result will be a #VALUE error.

> You will often see this trick in more advanced formulas because it's short and a little more flexible than the VALUE function.

### Add zero with Paste Special

If you want to perform an "in place" conversion of text to numbers without a formula, another solution is to add zero with a Paste Special command. This approach leaves the converted values in the same cells. The basic steps are as follows:

1.  Add a zero to an unused cell
2.  Copy the cell
3.  Select the values to convert
4.  [Open Paste Special](https://exceljet.net/shortcuts/display-the-paste-special-dialog-box)
     (Control + Option + V)
5.  Choose Values + Add

Video: [How to perform in-place changes with Paste Special](https://exceljet.net/videos/how-to-do-in-place-changes-with-paste-special)
.

### Strip all non-numeric characters

If a text value contains non-numeric characters like dashes, commas, punctuation, and so on, you'll need to remove these characters before you can convert the value to a number. This calls for a more aggressive approach. If you are using a current version of Excel that has the [REGEXREPLACE function](https://exceljet.net/functions/regexreplace-function)
, this formula will do it in one step:

    =REGEXREPLACE(A1,"[^0-9]","")+0

In a nutshell, this formula uses [regular expressions](https://exceljet.net/articles/regular-expressions-in-excel)
 to replace every character that is not strictly a number with nothing. Then we add 0 to convert the text result into a numeric value. The nice thing about this approach is that it will handle all kinds of extra characters that are not numbers, both visible and non-visible. There is no need to identify and specify which characters to remove. For details, see [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
.

In older versions of Excel without the REGEXREPLACE function, we need to take a more manual approach. The formulas in rows 12, 13, and 14 show how to use the [LEFT](https://exceljet.net/functions/left-function)
 and [RIGHT](https://exceljet.net/functions/right-function)
 functions to strip non-numeric characters from a text value before it's converted to a number:

    =LEFT(B12,2)+0 // left 2 characters
    =RIGHT(B13,3)+0 // right 3 characters
    =RIGHT(B14,4)+0 // right 4 characters

Each of these formulas extracts a specific number of characters from the left or right side of the text string. Then we add 0 to the result to make Excel convert the result to a numeric value.

> To extract a number at a known location in the _middle_ of a text string, use the [MID function](https://exceljet.net/functions/mid-function)
> . 

Related formulas
----------------

[![Excel formula: Convert numbers to text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20numbers%20to%20text.png "Excel formula: Convert numbers to text")](https://exceljet.net/formulas/convert-numbers-to-text)

### [Convert numbers to text](https://exceljet.net/formulas/convert-numbers-to-text)

Normally, you want to maintain numeric values in Excel, because they can be used in formulas that perform numeric calculations. However, there are situations where converting numbers to text makes sense. One example is when you want to concatenate (join) a formatted number to text. For example, "...

[![Excel formula: Clean and reformat telephone numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/clean_and_reformat_telephone_numbers.png "Excel formula: Clean and reformat telephone numbers")](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

### [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

In this example, the goal is to clean up telephone numbers with inconsistent formatting and then reformat the numbers in the same way. In practice, this means we need to start by removing the extra non-numeric characters, including spaces, dashes, periods, and parentheses. Once these characters are...

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

Related functions
-----------------

[![Excel VALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20value%20function.png "Excel VALUE function")](https://exceljet.net/functions/value-function)

### [VALUE Function](https://exceljet.net/functions/value-function)

The Excel VALUE function converts text that appears in a recognized format (i.e. a number, date, or time format) into a numeric value. Normally, the VALUE function is not needed in Excel, because Excel automatically converts text to numeric values.

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel REGEXREPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regexreplace_function.png "Excel REGEXREPLACE function")](https://exceljet.net/functions/regexreplace-function)

### [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)

The Excel REGEXREPLACE function replaces text matching a specific regex pattern in a given text string. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXREPLACE will...

[![Excel ISTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20istext%20function.png "Excel ISTEXT function")](https://exceljet.net/functions/istext-function)

### [ISTEXT Function](https://exceljet.net/functions/istext-function)

The Excel ISTEXT function returns TRUE when a cell contains a [text value](https://exceljet.net/glossary/text-value)
, and FALSE if the cell contains any other value. You can use the ISTEXT function to check if a cell contains a text value, or a numeric value entered as text.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20clean%20text%20with%20CLEAN%20and%20TRIM-thumb.png)](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

### [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

When you bring data into Excel you sometimes end up with extra spaces and other characters that cause problems. Excel contains two functions that can help you clean things up. Let's take a look. Here we have a list of movie titles that were copied in from some other system. You can see that there's...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20combine%20functions%20in%20a%20formula-thumb.png)](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)

### [How to combine functions in a formula](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)

In this video I'm going to show you how you can use multiple Excel functions to split, manipulate, and rejoin values inside a single formula. Here we have some sample data and, in column B, we have text values with a number at the end. What we want to do is increment these numbers using the value...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Convert numbers to text](https://exceljet.net/formulas/convert-numbers-to-text)
    
*   [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    

### Functions

*   [VALUE Function](https://exceljet.net/functions/value-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)
    
*   [ISTEXT Function](https://exceljet.net/functions/istext-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

### Videos

*   [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)
    
*   [How to combine functions in a formula](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)
    

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