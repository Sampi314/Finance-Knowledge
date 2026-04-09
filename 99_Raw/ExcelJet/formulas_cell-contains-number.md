# Cell contains number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cell-contains-number

---

[Skip to main content](https://exceljet.net/formulas/cell-contains-number#main-content)

[](https://exceljet.net/formulas/cell-contains-number#)

*   [Previous](https://exceljet.net/formulas/cell-contains-all-of-many-things)
    
*   [Next](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    

[Text](https://exceljet.net/formulas#Text)

Cell contains number
====================

by Dave Bruns · Updated 25 Nov 2022

Related functions 
------------------

[FIND](https://exceljet.net/functions/find-function)

[COUNT](https://exceljet.net/functions/count-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7555/download?token=IUVvaVO6)
 (14.99 KB)

![Excel formula: Cell contains number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cell_contains_number.png "Excel formula: Cell contains number")

Summary
-------

To test if a cell or text string contains a number, you can use the [FIND function](https://exceljet.net/functions/find-function)
 together with the [COUNT function](https://exceljet.net/functions/count-function)
. The numbers to look for are supplied as an [array constant](https://exceljet.net/glossary/array-constant)
. In the example the formula in D5 is:

    =COUNT(FIND({0,1,2,3,4,5,6,7,8,9},B5))>0
    

As the formula is copied down, it returns TRUE if a value contains a number and FALSE if not. See below for an alternate formula based on the SEQUENCE function.

Generic formula
---------------

    =COUNT(FIND({0,1,2,3,4,5,6,7,8,9},A1))>0

Explanation 
------------

In this example, the goal is to test the passwords in column B to see if they contain a number. This is a surprisingly tricky problem because Excel doesn't have a function that will let you test for a number inside a text string directly. Note this is different from checking if a cell value _is a number_. You can easily perform that test with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
. In this case, however, we to test if a cell value _contains_ a number, which may occur anywhere. One solution is to use the FIND function with an array constant. In [Excel 365](https://exceljet.net/glossary/excel-365)
, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can use a different formula based on the SEQUENCE function. Both approaches are explained below.

### FIND function

The FIND function is designed to look inside a text string for a specific substring. If FIND finds the substring, it returns a position of the substring in the text as a number. If the substring is not found, FIND returns a #VALUE error. For example:

    =FIND("p","apple") // returns 2
    =FIND("z","apple") // returns #VALUE!

We can use this same idea to check for numbers as well:

    =FIND(3,"app637") // returns 5
    =FIND(9,"app637") // returns #VALUE!

The challenge in this case is that we need to check the values in column B for ten different numbers, 0-9. One way to do that is to supply these numbers as the [array constant](https://exceljet.net/glossary/array-constant)
 {0,1,2,3,4,5,6,7,8,9}. This is the approach taken in the formula in cell D5:

    =COUNT(FIND({0,1,2,3,4,5,6,7,8,9},B5))>0

Inside the COUNT function, the FIND function is configured to look for all ten numbers in cell B5:

    FIND({0,1,2,3,4,5,6,7,8,9},B5)

Because we are giving FIND ten values to look for, it returns an [array](https://exceljet.net/glossary/array)
 with 10 results. In other words, FIND checks the text in B5 for each number and returns all results at once:

    {#VALUE!,4,5,6,#VALUE!,#VALUE!,#VALUE!,#VALUE!,#VALUE!,#VALUE!}

Unless you look at arrays often, this may look pretty cryptic. Here is the translation: The number 1 was found at position 4, the number 2 was found at position 5, and the number 3 was found at position 6. All other numbers were not found and returned #VALUE errors. 

We are very close now to a final formula. We simply need to tally up results. To do this, we [nest](https://exceljet.net/glossary/nesting)
 the FIND formula above inside the [COUNT function](https://exceljet.net/functions/count-function)
 like this:

    =COUNT(FIND({0,1,2,3,4,5,6,7,8,9},B5))

FIND returns the array of results directly to COUNT, which counts the numbers in the array. COUNT only counts numeric values, and ignores errors. This means COUNT will return a number greater than zero if there are any numbers in the value being tested. In the case of cell B5, COUNT returns 3.

The last step is to check the result from COUNT and force a TRUE or FALSE result. We do this by adding ">0" to the end of formula:

    =COUNT(FIND({0,1,2,3,4,5,6,7,8,9},B5))>0

Now the formula will return TRUE or FALSE. To display a custom result, you can use the [IF function](https://exceljet.net/functions/if-function)
:

    =IF(COUNT(FIND({0,1,2,3,4,5,6,7,8,9},B5))>0, "Yes", "No")
    

The original formula is now nested inside IF as the _logical\_test_ [argument](https://exceljet.net/glossary/function-argument)
. This formula will return "Yes" if B5 contains a number and "No" if not.

### SEQUENCE function

In Excel 365, which offers [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, we can take a different approach to this problem.

    =COUNT(--MID(B5,SEQUENCE(LEN(B5)),1))>0

This isn't necessarily a better approach, just a different way to solve the same problem. At the core, this formula uses the [MID function](https://exceljet.net/functions/mid-function)
 together with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 to split the text in cell B5 into an array:

    MID(B5,SEQUENCE(LEN(B5)),1)

Working from the inside out, the [LEN function](https://exceljet.net/functions/len-function)
 returns the length of the text in cell B5:

    LEN(B5) // returns 6

This number is returned to the SEQUENCE function as the rows argument, and SEQUENCE returns an array of numbers, 1-6:

    =SEQUENCE(LEN(B5))
    =SEQUENCE(6)
    ={1;2;3;4;5;6}

This array is returned to the MID function as the _start\_num_ argument, and, with _num\_chars_ set to 1, the MID function returns an array that contains the characters in cell B5:

    =MID(B5,{1;2;3;4;5;6},1)
    ={"a";"b";"c";"1";"2";"3"}

We can now simplify the original formula to:

    =COUNT(--{"a";"b";"c";"1";"2";"3"})>0

We use the [double-negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to get Excel to try and coerce the values in the array into numbers. The result looks like this:

    =COUNT({#VALUE!;#VALUE!;#VALUE!;1;2;3})>0

The math operation created by the double negative (--) returns an actual number when successful and a #VALUE! error when the operation fails. The [COUNT function](https://exceljet.net/functions/count-function)
 counts the numbers, ignoring any errors, and returns 3. As above, we check the final count with ">0", and the result for cell B5 is TRUE.

_Note: as you might guess, you can easily adapt this formula to [count numbers in a text string](https://exceljet.net/formulas/count-numbers-in-text-string)
._

### Cell equals number?

Note that the formulas above are too complex if you only want to test if a cell _equals_ a number. In that case, you can simply use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 like this:

    =ISNUMBER(A1)
    

Related formulas
----------------

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Range contains one of many substrings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20one%20of%20many%20substrings.png "Excel formula: Range contains one of many substrings")](https://exceljet.net/formulas/range-contains-one-of-many-substrings)

### [Range contains one of many substrings](https://exceljet.net/formulas/range-contains-one-of-many-substrings)

All the hard work is done by the COUNTIF function, which is configured to count the values in the named range "substrings" that appear the named range "rng" with like this: COUNTIF(rng,"\*"&substrings&"\*")) By wrapping substrings in the asterisks, Excel evaluates the formula like this: =...

Related functions
-----------------

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

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

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [Range contains one of many substrings](https://exceljet.net/formulas/range-contains-one-of-many-substrings)
    

### Functions

*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

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