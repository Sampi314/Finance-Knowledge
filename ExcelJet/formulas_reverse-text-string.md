# Reverse text string - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/reverse-text-string

---

[Skip to main content](https://exceljet.net/formulas/reverse-text-string#main-content)

[](https://exceljet.net/formulas/reverse-text-string#)

*   [Previous](https://exceljet.net/formulas/replace-one-delimiter-with-another)
    
*   [Next](https://exceljet.net/formulas/sort-comma-separated-values)
    

[Text](https://exceljet.net/formulas#Text)

Reverse text string
===================

by Dave Bruns · Updated 22 Oct 2023

Related functions 
------------------

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[MID](https://exceljet.net/functions/mid-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

![Excel formula: Reverse text string](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/reverse%20text%20string.png "Excel formula: Reverse text string")

Summary
-------

You can reverse a text string with the [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
 and [MID](https://exceljet.net/functions/mid-function)
 functions, by using an [array constant](https://exceljet.net/glossary/array-constant)
. In the example shown, the formula in C5 is:

    =TEXTJOIN("",1,MID(B5,{10,9,8,7,6,5,4,3,2,1},1))
    

Generic formula
---------------

    =TEXTJOIN("",1,MID(A1,{10,9,8,7,6,5,4,3,2,1},1))

Explanation 
------------

At the core, this formula uses the MID function to extract each character of a text string in reverse order. The starting character is given as a list of numbers in descending order hard-coded as array constant:

    MID(B5,{10,9,8,7,6,5,4,3,2,1},1)
    

The text argument comes B5, and 1 is specified for the number of characters to extract.

With the string "ABCD" in B5, the output from MID is an array that looks like this:

    {"","","","","","","D","C","B","A"}
    

This array is fed into the TEXTJOIN function as the text1 argument, with delimiter set to an [empty string](https://exceljet.net/glossary/empty-string)
 (""), and ignore blank set to TRUE (entered as 1):

    =TEXTJOIN("",1,{"","","","","","","D","C","B","A"})
    

The TEXTJOIN function [concatenates](https://exceljet.net/articles/how-to-concatenate-in-excel)
 each element in the array together, ignoring blanks, and returns the final result, "DCBA"

### Dynamic array

The array constant in the above example will only support string up to 10 characters. To use a dynamic array that scales to the right size, you can use a more complicated formula like this

    =TEXTJOIN("",1,MID(B5,ABS(ROW(INDIRECT("1:"&LEN(B5)))-(LEN(B5)+1)),1))
    

More information about [generating an array of numbers here](https://exceljet.net/formulas/create-array-of-numbers)
.

### Dynamic array with SEQUENCE function

[Excel 365](https://exceljet.net/glossary/excel-365)
 supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. In Excel 365, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 can generate dynamic number arrays in one step. With SEQUENCE, the formula above can be simplified to:

    =TEXTJOIN("",1,MID(B5,SEQUENCE(LEN(B5),,LEN(B5),-1),1))
    

Inside SEQUENCE, the [LEN function](https://exceljet.net/functions/len-function)
 returns the count of characters in B5, 4. This result is used both for the _rows_ argument and the _start_ argument, with -1 provided for the _step_ argument:

    SEQUENCE(4,,4,-1) // returns {4;3;2;1}
    

and this array is delivered to the MID function as the _start\_num_ argument.

Related formulas
----------------

[![Excel formula: Create array of numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20array%20of%20numbers.png "Excel formula: Create array of numbers")](https://exceljet.net/formulas/create-array-of-numbers)

### [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)

Note: In Excel 365 , the new SEQUENCE function is a better and easier way to create an array of numbers. The method explained below will work in previous versions. The core of this formula is a string that represents rows. For example, to create an array with 10 numbers, you can hard-code a string...

[![Excel formula: Reverse a list or range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/reverse_a_list_or_range.png "Excel formula: Reverse a list or range")](https://exceljet.net/formulas/reverse-a-list-or-range)

### [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)

In this example, the goal is to "reverse" the items in the range B5:B14, so that the first item appears last, the second item appears second to last, and so on. When you first encounter a problem like this in Excel, your first instinct might be to sort the values in some way using the SORT function...

Related functions
-----------------

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)
    
*   [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)
    

### Functions

*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    

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