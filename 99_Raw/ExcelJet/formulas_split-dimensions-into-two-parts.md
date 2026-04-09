# Split dimensions into two parts - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/split-dimensions-into-two-parts

---

[Skip to main content](https://exceljet.net/formulas/split-dimensions-into-two-parts#main-content)

[](https://exceljet.net/formulas/split-dimensions-into-two-parts#)

*   [Previous](https://exceljet.net/formulas/split-dimensions-into-three-parts)
    
*   [Next](https://exceljet.net/formulas/split-numbers-from-units-of-measure)
    

[Text](https://exceljet.net/formulas#Text)

Split dimensions into two parts
===============================

by Dave Bruns · Updated 1 Oct 2020

Related functions 
------------------

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[LEFT](https://exceljet.net/functions/left-function)

[RIGHT](https://exceljet.net/functions/right-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Split dimensions into two parts](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/split%20dimensions%20into%20two%20parts%20-%20left.png "Excel formula: Split dimensions into two parts")

Summary
-------

To split dimensions like "100x50" into two separate parts, you can use formulas based on several functions: [LEFT](https://exceljet.net/functions/left-function)
, [MID](https://exceljet.net/functions/mid-function)
, [RIGHT](https://exceljet.net/functions/right-function)
, [FIND](https://exceljet.net/functions/find-function)
, [LEN](https://exceljet.net/functions/len-function)
, and [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
.

_Note: you can also use Flash Fill in Excel 2013 and above, and the "[Text to columns](https://exceljet.net/glossary/text-to-columns)
" feature in earlier versions of Excel. Both approaches are  simpler than the formulas described below. However, for a formula-based solution, read on._

Explanation 
------------

### Background

A common annoyance with data is that it may be represented as text instead of numbers. This is especially common with dimensions, which may appear in one text string that includes units, for example:

50 ft x 200 ft  
153 ft x 324 ft  
Etc.

In a spreadsheet, it's a lot more convenient to have actual numbers so that you can use them in calculations as you wish.

Extracting individual dimensions from a text representation can be done with formulas that combine several text functions.

### Solution

In this case, it because we have both the "ft" unit and space characters (" ") included in the dimensions, it makes sense to remove these first. That will "normalize" the dimensions and simplify the formulas that do the actual extraction.

To remove both "ft" and " ", we are using this formula in cell C6, which contains two nested SUBSTITUTE functions:

    =SUBSTITUTE(SUBSTITUTE(B5,"ft","")," ","")
    

![Using the SUBSTITUTE function to strip units and spaces](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split%20dimensions%20into%20two%20parts%20-%20clean.png?itok=vtjNFrWl "Using the SUBSTITUTE function to strip units and spaces")

This formula takes the original text, and first strips "ft" (in the inner ), then strips spaces with the outer SUBSTITUTE function.

The result is a dimension with just the "x" separating the two parts.

Now we can two relatively straightforward formulas to extract each part. To get the dimension on the left, D6 contains:

    =LEFT(C5,FIND("x",C5)-1)
    

![Using the LEFT function to grab the dimension on the left](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split%20dimensions%20into%20two%20parts%20-%20left.png?itok=WzraEpjB "Using the LEFT function to grab the dimension on the left")

To get the dimension on the right, E6 contains:

    =RIGHT(C5,LEN(C5)-FIND("x",C5))
    

![Using the RIGHT function to grab the dimension on the right](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split%20dimensions%20into%20two%20parts%20-%20right.png?itok=6PxG7DJH "Using the RIGHT function to grab the dimension on the right")

Both of the formulas above extract the correct dimension by using FIND to locate the "x". For more detail, see the related function links on this page.

Related formulas
----------------

[![Excel formula: Get first name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_0.png "Excel formula: Get first name from name")](https://exceljet.net/formulas/get-first-name-from-name)

### [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)

In this example, the goal is to extract the first name from names that appear in <first> <middle> <last> format, where the middle name is optional. The easiest way to do this is with the newer TEXTBEFORE function. In older versions of Excel, you can use an alternative formula...

[![Excel formula: Get first name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_with_comma.png "Excel formula: Get first name from name with comma")](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

### [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

In this example, the goal is to extract the first name from a list of names in "Last, First" format as seen in column B. There are several ways to approach this problem. In the current version of Excel, the easiest solution is to use the TEXTAFTER function. In older versions of Excel, it can be...

[![Excel formula: Split dimensions into three parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_dimensions_into_three_parts.png "Excel formula: Split dimensions into three parts")](https://exceljet.net/formulas/split-dimensions-into-three-parts)

### [Split dimensions into three parts](https://exceljet.net/formulas/split-dimensions-into-three-parts)

In this example, the goal is to split the text strings in column B, which contain three dimensions in the form "L x W x H", into 3 separate dimensions. One problem with dimensions entered as text is that they can't be used for any kind of calculation. So, in addition, we want our final dimensions...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

Related functions
-----------------

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

Related videos
--------------

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

*   [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)
    
*   [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)
    
*   [Split dimensions into three parts](https://exceljet.net/formulas/split-dimensions-into-three-parts)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    

### Functions

*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

### Videos

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