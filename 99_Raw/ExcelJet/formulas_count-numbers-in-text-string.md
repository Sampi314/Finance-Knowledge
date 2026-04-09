# Count numbers in text string - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-numbers-in-text-string

---

[Skip to main content](https://exceljet.net/formulas/count-numbers-in-text-string#main-content)

[](https://exceljet.net/formulas/count-numbers-in-text-string#)

*   [Previous](https://exceljet.net/formulas/count-line-breaks-in-cell)
    
*   [Next](https://exceljet.net/formulas/count-specific-characters-in-a-range)
    

[Text](https://exceljet.net/formulas#Text)

Count numbers in text string
============================

by Dave Bruns · Updated 24 Nov 2022

Related functions 
------------------

[COUNT](https://exceljet.net/functions/count-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

[ROW](https://exceljet.net/functions/row-function)

![Excel formula: Count numbers in text string](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count_numbers_in_text_string.png "Excel formula: Count numbers in text string")

Summary
-------

To count numbers that appear in a text string, you can use a formula based on the [COUNT function](https://exceljet.net/functions/count-function)
, with help from the [MID](https://exceljet.net/functions/mid-function)
, [SEQUENCE](https://exceljet.net/functions/sequence-function)
, and [LEN](https://exceljet.net/functions/len-function)
 functions. In the example shown, the formula in cell D5 is:

    =COUNT(--MID(B5,SEQUENCE(LEN(B5)),1))

The result in D5 is 2, since there are two numbers in B5. 

Generic formula
---------------

    =COUNT(--MID(A1,SEQUENCE(LEN(A1)),1))

Explanation 
------------

In this example, the goal is to count numbers that appear in column B. The [COUNT function](https://exceljet.net/functions/count-function)
 is designed to only count numeric values, but because all values in the range B5:B15 are [text](https://exceljet.net/glossary/text-value)
, COUNT will return zero. One approach is to [split the characters in each text value into an array](https://exceljet.net/formulas/split-text-string-to-character-array)
, then use the COUNT function to count numbers in the result. This approach is described below.

### Create the array

The first step is to split the text string into an array of characters. This is done with MID, LEN, and SEQUENCE like this:

    MID(B5,SEQUENCE(LEN(B5)),1)

In a nutshell, the [LEN function](https://exceljet.net/functions/len-function)
 returns the length of the text in B5, which is 9, to the SEQUENCE function as the _rows_ argument. [SEQUENCE](https://exceljet.net/functions/sequence-function)
 then generates an a numeric array like {1;2;3;4;5;6;7;8;9}, which is returned to the MID function as the _start\_num_ argument:

    =MID(B5,{1;2;3;4;5;6;7;8;9},1)

The [MID function](https://exceljet.net/functions/mid-function)
 then extracts each of the 9 characters and returns an array like {"1";"8";" ";"a";"p";"p";"l";"e";"s"}. [Read a more detailed explanation here](https://exceljet.net/formulas/split-text-string-to-character-array)
.

### Count numbers

Back in the original formula, we use a [double-negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) operation to force Excel to try and convert each character to a number:

    =COUNT(--{"1";"8";" ";"a";"p";"p";"l";"e";"s"})

Where this operation succeeds, we get a numeric value. Where it fails, we get a #VALUE! error:

    =COUNT({1;8;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!})

The COUNT function then counts the numbers in the array and returns a final result of 2. As the formula is copied down column D, it returns a count of the numbers in each text string in column B.

### Legacy Excel

In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, which lacks [dynamic arrays](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 and the SEQUENCE function, it is more challenging to split a text string to an array of characters. One workaround is to use the ROW and INDIRECT function like this:

    =COUNT(--MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1))

The [INDIRECT function](https://exceljet.net/functions/indirect-function)
 is a way of creating a valid Excel reference with text. The [ROW function](https://exceljet.net/functions/row-function)
 then evaluates the text and returns a reference. The reference in this case is 1:9 (rows 1 through 9), and the ROW function then returns an array of corresponding row numbers. The resulting array is the same as with the SEQUENCE function above:

    =COUNT(--MID(B5,{1;2;3;4;5;6;7;8;9},1))

In the end, this formula returns the same result as above, 2. Note this is an [array formula](https://exceljet.net/articles/what-is-an-array-formula)
 and must be entered with control + shift + enter in older versions of Excel.

Related formulas
----------------

[![Excel formula: Split text string to character array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_to_character_array_0.png "Excel formula: Split text string to character array")](https://exceljet.net/formulas/split-text-string-to-character-array)

### [Split text string to character array](https://exceljet.net/formulas/split-text-string-to-character-array)

In this example, the goal is to use a formula to split a text string into an array of characters. For example, if the text string is "Apple", the resulting array should be {"A","p","p","l","e"}. For a long time, this was quite a difficult problem that required a complicated array formula approach...

[![Excel formula: Cell contains number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_number.png "Excel formula: Cell contains number")](https://exceljet.net/formulas/cell-contains-number)

### [Cell contains number](https://exceljet.net/formulas/cell-contains-number)

In this example, the goal is to test the passwords in column B to see if they contain a number. This is a surprisingly tricky problem because Excel doesn't have a function that will let you test for a number inside a text string directly. Note this is different from checking if a cell value is a...

Related functions
-----------------

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split text string to character array](https://exceljet.net/formulas/split-text-string-to-character-array)
    
*   [Cell contains number](https://exceljet.net/formulas/cell-contains-number)
    

### Functions

*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    

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