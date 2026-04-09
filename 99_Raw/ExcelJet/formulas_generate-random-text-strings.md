# Generate random text strings - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/generate-random-text-strings

---

[Skip to main content](https://exceljet.net/formulas/generate-random-text-strings#main-content)

[](https://exceljet.net/formulas/generate-random-text-strings#)

*   [Previous](https://exceljet.net/formulas/filter-with-partial-match)
    
*   [Next](https://exceljet.net/formulas/get-column-totals)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Generate random text strings
============================

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[SORTBY](https://exceljet.net/functions/sortby-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

[COUNTA](https://exceljet.net/functions/counta-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[CHAR](https://exceljet.net/functions/char-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6382/download?token=LUaawa5_)
 (17.82 KB)

![Excel formula: Generate random text strings](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/generate%20random%20strings.png "Excel formula: Generate random text strings")

Summary
-------

To generate a list of random text strings, you can use a formula based on [INDEX](https://exceljet.net/functions/index-function)
, [RANDARRAY](https://exceljet.net/functions/randarray-function)
, and [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
. In the example shown, the formula in D5 is:

    =TEXTJOIN("",1,INDEX(chars,RANDARRAY(6,1,1,26,TRUE)))
    

where **chars** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B30 containing the letters A-Z. As the formula is copied down the column, it generates a new 6-character text string on each line.

Generic formula
---------------

    =INDEX(characters,RANDARRAY(n,1,1,count,TRUE))

Explanation 
------------

The new [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 in [Excel 365](https://exceljet.net/glossary/excel-365)
 make it much easier to solve certain tricky problems with formulas.

In this example, the goal is to generate a list of random 6-character codes. The randomness is handled by the [RANDARRAY function](https://exceljet.net/functions/randarray-function)
, a new function in Excel 365. RANDARRAY returns 6 random numbers to INDEX, which then retrieves 6 random values from the named range **chars.** The results from INDEX are then concatenated together with the TEXTJOIN function.

In the example shown, the formula in D5 is:

    =TEXTJOIN("",1,INDEX(chars,RANDARRAY(6,1,1,26,TRUE)))
    

Working from the inside out, the RANDARRAY function is used to generate an [array](https://exceljet.net/glossary/array)
 containing six random numbers between 1-26:

    RANDARRAY(6,1,1,26,TRUE) // return array like {14;5;21;7;25;3}
    

Note the array returned will vary with each instance of the RANDARRAY function. Also, because RANDARRAY is a [volatile function](https://exceljet.net/glossary/volatile-function)
, it will recalculate with each worksheet change.

This array of random numbers is returned directly to the [INDEX function](https://exceljet.net/functions/index-function)
 as the _rows_ argument:

    INDEX(chars,{14;5;21;7;25;3})
    

Because we are asking INDEX for 6 rows, we get back 6 results in an array like this:

    {"N","E","U","G","Y","C"}
    

This array is returned to the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 as the _text1_ argument:

    =TEXTJOIN("",1,{"N","E","U","G","Y","C"}) // returns "NEUGYC"
    

TEXTJOIN is set to use an [empty string](https://exceljet.net/glossary/empty-string)
 as the delimiter and to ignore empty values. With this configuration, TEXTJOIN simply [concatenates](https://exceljet.net/glossary/concatenation)
 all values together and returns a 6-character text string like "NEUGYC".

### Count chars programmatically

Instead of hardcoding the size of **chars** directly into the RANDARRAY function, you can use the COUNTA function to count the elements in the array and return that count to RANDARRAY:

    RANDARRAY(6,1,1,COUNTA(chars),TRUE)
    

This assumes **chars** does not contain any empty cells.

### Generate chars programmatically

Since the letters A-Z have underlying numeric code values, it is possible to generate the array of characters used to assemble text strings programmatically, instead of using a [range](https://exceljet.net/glossary/range)
. This can be done with the [CHAR function](https://exceljet.net/functions/char-function)
 and the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
.

To generate an array with all uppercase letters A-Z, which map to ASCII 65-90:

    =CHAR(SEQUENCE(26,1,65,1)) // returns {"A","B","C",...}
    

To generate lowercase letters a-z, which correspond to ASCII 97-122:

    =CHAR(SEQUENCE(26,1,97,1)) // returns {"a","b","c",...}
    

This code can be dropped into the original formula to replace **chars** like this:

    =TEXTJOIN("",1,INDEX(CHAR(SEQUENCE(26,1,65,1)),RANDARRAY(6,1,1,26,TRUE)))
    

### Other characters

The characters in the named range **chars** can be anything you like. If you add more than 26 characters (or fewer) adjust the number 26 as appropriate, or use COUNTA as explained above.

### Without Excel 365

It is possible to generate random text strings without Excel 365, but the formula is more tedious and redundant. Since we don't have a good way to get 6 random numbers all at once, we use the [RANDBETWEEN function](https://exceljet.net/functions/randbetween-function)
 to get one random value at a time:

    =INDEX(chars,RANDBETWEEN(1,26))&
    INDEX(chars,RANDBETWEEN(1,26))&
    INDEX(chars,RANDBETWEEN(1,26))&
    INDEX(chars,RANDBETWEEN(1,26))&
    INDEX(chars,RANDBETWEEN(1,26))&
    INDEX(chars,RANDBETWEEN(1,26))
    

This formula uses the [INDEX function](https://exceljet.net/functions/index-function)
 to retrieve one random value at a time from the [named range](https://exceljet.net/glossary/named-range)
 **chars**, and the 6 results are [concatenated](https://exceljet.net/glossary/concatenation)
 together into a single text string. Line breaks added for [readability](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
.

It is also possible to generate values A-Z directly with CHAR and RANDBETWEEN like this:

    =CHAR(RANDBETWEEN(65,90))&
    CHAR(RANDBETWEEN(65,90))&
    CHAR(RANDBETWEEN(65,90))&
    CHAR(RANDBETWEEN(65,90))&
    CHAR(RANDBETWEEN(65,90))&
    CHAR(RANDBETWEEN(65,90))
    

In this version, RANDBETWEEN is returning a value between 65 and 90 (inclusive) that corresponds to the ASCII value for the letters A-Z (uppercase). The CHAR function translates the numeric value to a letter. As above, all results are concatenated together in a single text string.

Related formulas
----------------

[![Excel formula: Random list of names](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random-list-of-names.png "Excel formula: Random list of names")](https://exceljet.net/formulas/random-list-of-names)

### [Random list of names](https://exceljet.net/formulas/random-list-of-names)

In this example, the goal is to create a list of 10 random names from a larger list of 100 names. In other words, we want to select a random subset of names from a larger list. The names to select from are in column B, starting in row 5. The formula should handle any number of names in the input...

[![Excel formula: Random sort](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random_sort.png "Excel formula: Random sort")](https://exceljet.net/formulas/random-sort)

### [Random sort](https://exceljet.net/formulas/random-sort)

In this example, the goal is to perform a random sort of the data in B5:B16 with a formula. This can be done with the SORTBY function and the RANDARRAY function . SORTBY function The SORTBY function sorts provided values by one or more "sort by" arrays. The sort by arrays make it possible to sort...

Related functions
-----------------

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel RANDARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_randarray_function.png "Excel RANDARRAY function")](https://exceljet.net/functions/randarray-function)

### [RANDARRAY Function](https://exceljet.net/functions/randarray-function)

The Excel RANDARRAY function generates an array of random numbers between two values. The size or the array is specified by _rows_ and _columns_ arguments. The generated values can be either decimals or whole numbers.

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel CHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")](https://exceljet.net/functions/char-function)

### [CHAR Function](https://exceljet.net/functions/char-function)

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Random list of names](https://exceljet.net/formulas/random-list-of-names)
    
*   [Random sort](https://exceljet.net/formulas/random-sort)
    

### Functions

*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [CHAR Function](https://exceljet.net/functions/char-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

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