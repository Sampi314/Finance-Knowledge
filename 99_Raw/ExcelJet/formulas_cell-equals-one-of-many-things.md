# Cell equals one of many things - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cell-equals-one-of-many-things

---

[Skip to main content](https://exceljet.net/formulas/cell-equals-one-of-many-things#main-content)

[](https://exceljet.net/formulas/cell-equals-one-of-many-things#)

*   [Previous](https://exceljet.net/formulas/cell-ends-with)
    
*   [Next](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
    

[Text](https://exceljet.net/formulas#Text)

Cell equals one of many things
==============================

by Dave Bruns · Updated 18 Jan 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[TRIM](https://exceljet.net/functions/trim-function)

![Excel formula: Cell equals one of many things](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cell_equals_one_of_many_things.png "Excel formula: Cell equals one of many things")

Summary
-------

To test if a cell is equal to one of many things, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in cell C5 is:

    =SUMPRODUCT(--(B5=things))>0

where **things** is the named range E5:E9. The result in cell C5 is TRUE, since "green" is one of the values in E5:E9. As the formula is copied down, it returns a TRUE or FALSE result for each value in column B.

Generic formula
---------------

    =SUMPRODUCT(--(A1=things))>0

Explanation 
------------

In this example, the goal is to return a TRUE or FALSE result for each value in column B, based on whether it appears in the range E5:E9, which has been named "things" for convenience.

### Context

Imagine you have a list of values in the range B5:B16 and you want to check each value to see if it appears in another list of values in the range E5:E9, which has been named "things". You might think you can use a formula like this:

    =B5=things

However, because we are comparing B5 to the range E5:E9, which contains five values, the formula will return five results. With "green" in cell B5, the result will be an [array](https://exceljet.net/glossary/array)
 like this:

    {FALSE;FALSE;TRUE;FALSE;FALSE}

And if we copy the formula down, _each value_ in column B will return five results. This idea isn't going to work as-is. You could build a more complicated formula using [nested IF statements](https://exceljet.net/formulas/nested-if-function-example)
 to check for each value separately, but this is a tricky path that will take much longer and greatly increase the chance of errors. A much simpler, cleaner approach is to use an array formula based on the SUMPRODUCT function.

### Solution with SUMPRODUCT

The [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 multiplies ranges or arrays together and returns the sum of products. This sounds boring, but SUMPRODUCT is a versatile function that can be used to solve many tricky problems in Excel. It works nicely in this case because it can handle arrays natively in any version of Excel.

> Note: In Excel 2021 or Excel 365, you can use the SUM function instead of SUMPRODUCT and it will just work fine. However, if the worksheet is opened in an older version of Excel, it will appear as a traditional [array formula](https://exceljet.net/glossary/array-formula)
>  surrounded by curly braces. If you need backward compatibility, [SUMPRODUCT avoids this complication](https://exceljet.net/articles/why-sumproduct)
>  and works the same in all versions.

Back to the problem. As mentioned above, if we compare the value in cell B5 directly with the values in things (E5:E9), we get back an _array_ that contains five TRUE or FALSE values. This seems inconvenient because it isn't obvious how we can resolve this list of five results into a single TRUE or FALSE value. However, we can use SUMPRODUCT to process the array of TRUE/FALSE values and return a single result with a formula like this:

    =SUMPRODUCT(--(B5=things))>0

At a high level, this formula counts the TRUE values in the array and then checks if the result is greater than zero. Working from the inside out, the expression B5=things returns five values, as explained above. 

    ​=B5=things // returns {FALSE;FALSE;TRUE;FALSE;FALSE}

If we simplify the formula, we now have:

    =SUMPRODUCT(--({FALSE;FALSE;TRUE;FALSE;FALSE}))>0

You might wonder what the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is doing here. SUMPRODUCT is designed to process numeric values, and it will simply ignore TRUE and FALSE values. If we try to use the raw values, SUMPRODUCT will return zero:

    =SUMPRODUCT(FALSE;FALSE;TRUE;FALSE;FALSE}) // returns 0

The double negative (--) is a simple trick to force Excel to convert the TRUE and FALSE values to their numeric equivalents, 1 and 0. After this operation is evaluated, we can simplify the formula to this:

    =SUMPRODUCT({0;0;1;0;0})>0

Notice that each FALSE value in the array is now zero, and the lone TRUE in the array is now 1. Now you can see where we are headed. Since the array contains only numbers, SUMPRODUCT will return a sum. If we get any non-zero result, we have a match, so we use >0 to force a final result of either TRUE or FALSE:

    =SUMPRODUCT({0;0;1;0;0})>0
    =1>0
    =TRUE

### With a hard-coded list

There's no requirement to use a range for your list of things to check for. If you're only looking for a small number of things, you can use a list in array format, which is called an [array constant](https://exceljet.net/glossary/array-constant)
. For example, if you're just looking for the colors red, blue, and green, you can use {"red","blue","green"} like this:

    =SUMPRODUCT(--(B5={"red","blue","green"}))>0
    

Using a range is a more flexible approach since the values appear on the worksheet and can be changed at any time.

### Dealing with extra spaces

If the cells you are testing contain any extra space, they won't match properly. To strip all extra space, you can modify the formula to use the [TRIM function](https://exceljet.net/functions/trim-function)
 like so:

    =SUMPRODUCT(--(TRIM(A1)=things))>0
    

TRIM will strip leading or trailing space characters from the value before it is compared to the list of things.

Related formulas
----------------

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Get first match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_match_cell_contains.png "Excel formula: Get first match cell contains")](https://exceljet.net/formulas/get-first-match-cell-contains)

### [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)

The general goal is to search through a cell for one of several specified values and return the first match found if one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

[![Excel formula: Get all matches cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_all_matches_cell_contains.png "Excel formula: Get all matches cell contains")](https://exceljet.net/formulas/get-all-matches-cell-contains)

### [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)

In this example the goal is to check a cell for several things at once, and return a comma separated list of the things that were found. In other words, we want check for the colors seen in column E and list the colors found in column C. The formula in C5, copied down, is: =TEXTJOIN(", ",1,FILTER(...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

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
    
*   [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    
*   [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [TRIM Function](https://exceljet.net/functions/trim-function)
    

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