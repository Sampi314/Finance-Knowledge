# If complete show checkmark - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-complete-show-checkmark

---

[Skip to main content](https://exceljet.net/formulas/if-complete-show-checkmark#main-content)

[](https://exceljet.net/formulas/if-complete-show-checkmark#)

*   [Previous](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z)
    
*   [Next](https://exceljet.net/formulas/if-date-is-between-two-dates)
    

[If](https://exceljet.net/formulas#If)

If complete show checkmark
==========================

by Dave Bruns · Updated 27 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[UNICHAR](https://exceljet.net/functions/unichar-function)

[CHAR](https://exceljet.net/functions/char-function)

![Excel formula: If complete show checkmark](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_complete_show_checkmark.png "Excel formula: If complete show checkmark")

Summary
-------

To show a checkmark (also called a "tick mark") when a task is complete, you can use a formula based on the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the formula in D5 is:

    =IF(C5="complete","✓","")

As the formula is copied down, IF returns a checkmark (✓) if the value in column C is "complete". Otherwise, IF returns an [empty string](https://exceljet.net/glossary/empty-string)
 (""), which looks like an blank cell in Excel.

Generic formula
---------------

    =IF(C5="complete","✓","")

Explanation 
------------

The goal is to display a checkmark (also called a "tick mark" in British English) when a task is marked complete. The easiest way to do this is with the IF function and the mark you would like to display. The article below explains several options.

### IF with a plain checkmark

The simplest approach, and the one that appears in the example shown, is to use a plain text checkmark like this:

    =IF(C5="complete","✓","")

This formula uses the [IF function](https://exceljet.net/functions/if-function)
 to check for "complete" in column C. When the value is "complete", IF returns a checkmark (✓). When the value in column C is anything else, IF returns an empty string (""), which looks like a blank cell in Excel. Notice the checkmark itself must be enclosed in double quotes ("") since it is text.

### IF with UNICHAR

A more flexible way to display a checkmark is to use the IF function with the [UNICHAR function](https://exceljet.net/functions/unichar-function)
 like this:

    =IF(C5="complete",UNICHAR(10003),"")

![If function with unichar function to display checkmark](https://exceljet.net/sites/default/files/images/formulas/inline/If_function_with_unichar_function_to_display_checkmark.png "If function with unichar function to display checkmark")

The logic of this formula is the same as the original formula above. However, instead of hardcoding a plain text version of a checkmark into the formula, the UNICHAR function is used to return the Unicode character 10003. The benefit of this approach is that you can easily change the number to display a different character. Here are a few examples of Unicode characters related to check and tick marks:

![Unicode characters for checkmark or tick mark](https://exceljet.net/sites/default/files/images/formulas/inline/Unicode_characters_for_checkmark_or_tick_mark.png "Unicode characters for checkmark or tick mark")

To use a different symbol, change the number in the formula. For example, use 10007 for an "X":

    =IF(C5="complete",UNICHAR(10007),"")

![If function with unicode x character](https://exceljet.net/sites/default/files/images/formulas/inline/If_function_with_unicode_x_character.png "If function with unicode x character")

For more useful Unicode symbols, see: [How to use the UNICHAR function](https://exceljet.net/functions/unichar-function)
.

### IF with CHAR

An older way to display a checkmark in a formula is to use IF with the [CHAR function](https://exceljet.net/functions/char-function)
, then format the result with the Wingdings font:

    =IF(C5="complete",CHAR(252),"")

![If function with char function and wingdings to display checkmark](https://exceljet.net/sites/default/files/images/formulas/inline/If_function_with_char_function_to_display_checkmark.png "If function with char function and wingdings to display checkmark")

_Note: with this option, you must format the range D4:D12 with the Wingdings font. If you skip this step, you will not see a checkmark. Instead, you will see a character like "ü" or similar._

### With conditional formatting

You can also use Excel's built-in [conditional formatting icons](https://exceljet.net/videos/how-to-use-icon-sets-with-conditional-formatting)
 to show a checkmark, but you don't have much flexibility. Visit [this page](https://exceljet.net/conditional-formatting-formulas)
 for a comprehensive guide on conditional formatting with formulas, featuring many practical examples.

Related formulas
----------------

[![Excel formula: If cell is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_blank.png "Excel formula: If cell is blank")](https://exceljet.net/formulas/if-cell-is-blank)

### [If cell is blank](https://exceljet.net/formulas/if-cell-is-blank)

In the example worksheet, column D contains a date when a task is completed. If the task is not yet complete, the cell in column D will be empty (blank). In column E, the goal is to display the word "Open" when there is no date in column D. If there is a date in column D, the formula in column E...

[![Excel formula: If cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains.png "Excel formula: If cell contains")](https://exceljet.net/formulas/if-cell-contains)

### [If cell contains](https://exceljet.net/formulas/if-cell-contains)

The goal is to do something if a cell contains a given substring. For example, in the worksheet above, a formula returns "x" when a cell contains "abc". If you are familiar with Excel, you will probably think first of the IF function. However, one limitation of IF is that it does not support...

[![Excel formula: Return blank if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/return_blank_if.png "Excel formula: Return blank if")](https://exceljet.net/formulas/return-blank-if)

### [Return blank if](https://exceljet.net/formulas/return-blank-if)

The goal is to display a blank cell based on a specific condition. In the worksheet shown, we want to return the value from column C, but only when the value in column B is "A". If the value in column B is anything else, we want to display nothing. The easiest way to solve this problem is with the...

[![Excel formula: Validate input with check mark](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/validate_input_with_check_mark.png "Excel formula: Validate input with check mark")](https://exceljet.net/formulas/validate-input-with-check-mark)

### [Validate input with check mark](https://exceljet.net/formulas/validate-input-with-check-mark)

This formula is a good example of nesting one function inside another. At the core, this formula uses the IF function to return a check mark (✓) when a logical test returns TRUE: =IF(logical\_test,"✓","") If the test returns FALSE, the formula returns an empty string (""). For the logical test, we...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel UNICHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unichar_function.png "Excel UNICHAR function")](https://exceljet.net/functions/unichar-function)

### [UNICHAR Function](https://exceljet.net/functions/unichar-function)

The Excel UNICHAR function returns the Unicode character at a given code point

[![Excel CHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")](https://exceljet.net/functions/char-function)

### [CHAR Function](https://exceljet.net/functions/char-function)

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_insert_symbols_and_special_characters-thumb.png)](https://exceljet.net/videos/how-to-insert-symbols-and-special-characters-in-excel)

### [How to insert symbols and special characters in Excel](https://exceljet.net/videos/how-to-insert-symbols-and-special-characters-in-excel)

In this lesson we'll look at how to add symbols and other special characters to text in Excel. This includes things like the copyright symbol, math signs, arrows, and the graphics found in fonts like Wingdings. Let's take a look. There are several different ways to insert symbols and special...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [If cell is blank](https://exceljet.net/formulas/if-cell-is-blank)
    
*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    
*   [Return blank if](https://exceljet.net/formulas/return-blank-if)
    
*   [Validate input with check mark](https://exceljet.net/formulas/validate-input-with-check-mark)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [UNICHAR Function](https://exceljet.net/functions/unichar-function)
    
*   [CHAR Function](https://exceljet.net/functions/char-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [How to insert symbols and special characters in Excel](https://exceljet.net/videos/how-to-insert-symbols-and-special-characters-in-excel)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

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