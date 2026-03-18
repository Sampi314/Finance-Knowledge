# Cell ends with - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cell-ends-with

---

[Skip to main content](https://exceljet.net/formulas/cell-ends-with#main-content)

[](https://exceljet.net/formulas/cell-ends-with#)

*   [Previous](https://exceljet.net/formulas/cell-contains-specific-words)
    
*   [Next](https://exceljet.net/formulas/cell-equals-one-of-many-things)
    

[Text](https://exceljet.net/formulas#Text)

Cell ends with
==============

by Dave Bruns · Updated 20 Feb 2024

Related functions 
------------------

[RIGHT](https://exceljet.net/functions/right-function)

[EXACT](https://exceljet.net/functions/exact-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Cell ends with](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cell_ends_with.png "Excel formula: Cell ends with")

Summary
-------

To test if a cell _ends with_ specific text, you can use a formula based on the [RIGHT function](https://exceljet.net/functions/right-function)
. In the example shown, the formula in cell D5, copied down, is:

    =RIGHT(B5,3)="jwb"

This formula returns TRUE when the value in column B ends with "jwb" and FALSE if not. Note that this formula is _not_ case-sensitive. See below for a case-sensitive alternative.

Generic formula
---------------

    =RIGHT(A1,3)="xyz"

Explanation 
------------

In this example, the goal is to test values in column B to see if they end with a specific text string, which is "jwb" in the worksheet shown. This problem can be solved with the RIGHT function, as explained below.

### RIGHT function

The [RIGHT function](https://exceljet.net/functions/right-function)
 extracts a given number of characters from the _right_ side of a text string. For example, the formula below returns the last three letters of "apple", which is "ple":

    =RIGHT("apple",3) // returns "ple"

This means we can use the RIGHT function to test if cell B5 ends with "jwb" like this:

    =RIGHT(B5,3)="jwb"

The RIGHT function extracts the last 3 characters in cell B5 and the result is compared to the string "jwb", forcing a TRUE or FALSE result. The formula is solved like this:

    =RIGHT(B5,3)="jwb"
    =RIGHT("ABC-1224-HNN",3)="jwb"
    ="HNN"="jwb"
    =FALSE

For cell B5 the result is FALSE, since "ABC-1224-HNN" does not end with "jwb". In cell B6, however, the result is TRUE, since "XYZ-6543-JWB" _does_ end with "jwb".

    =RIGHT(B6,3)="jwb"
    =RIGHT("XYZ-6543-JWB",3)="jwb"
    ="XYZ"="jwb"
    =TRUE

Note that Excel is _not_ case-sensitive by default, so "JWB"="jwb" will return TRUE in a formula. Also note the _num\_chars_ argument is set to 3 above because we want to work with the last 3 letters in the cell only. However, this value needs to be modified to suit the situation. For example, to test for a value that ends with "apple", _num\_chars_ should be set to 5:

    =RIGHT(B5,5)="apple"

###   
Case-sensitive option

Excel is not case-sensitive by default, but you can easily adapt the formula to use the [EXACT function](https://exceljet.net/functions/exact-function)
 to make the formula case-sensitive like this:

    =EXACT(RIGHT(B5,3),"JWB")

EXACT takes two arguments, _text1_ and _text2_. EXACT will only return TRUE when _text1_ and _text2_ are exactly the same, taking into account case. For example:

    =EXACT("abc","ABC") // returns FALSE
    =EXACT("abc","Abc") // returns FALSE
    =EXACT("abc","abc") // returns TRUE

Turning back to cell B6 in the worksheet shown, the two formulas below return different results:

    =EXACT(RIGHT(B6,3),"jwb")// returns FALSE
    =EXACT(RIGHT(B6,3),"JWB") // returns TRUE

The first formula returns FALSE because the EXACT function is case-sensitive, so "JWB" _does not_ equal "jwb". The second formula returns TRUE because "JWB" _does_ equal "JWB" taking into account case. Note that we don't need the equal to operator (=) in this formula because EXACT performs a comparison automatically.

### If cell ends with

To adapt the formulas above to "If cell ends with", simply drop the formulas into the [IF function](https://exceljet.net/functions/if-function)
 as the logical test. For example, to return "Yes" when a cell ends with "jwb" and "No" when not, you can use a formula like this

    =IF(RIGHT(B5,3)="jwb", "Yes", "No")
    

The case-sensitive version of the formula works the same way:

    =IF(EXACT(RIGHT(B5,3),"JWB"), "Yes", "No")
    

### Other functions

It is worth noting that Excel contains two other functions, the [SEARCH function](https://exceljet.net/functions/search-function)
 and the [FIND function](https://exceljet.net/functions/find-function)
 that are meant to look for a substring in a text value. They could be used to solve this problem, but they are more work to configure, so I don't see any advantage to using them. You could however use the COUNTIF function with a [wildcard](https://exceljet.net/glossary/wildcard)
 to solve this problem like this:

    =COUNTIF(B5,"*jwb")<>0

This works fine, but keep in mind that COUNTIF is in a [group of eight \*IFS functions](https://exceljet.net/articles/excels-racon-functions)
 that won't accept an [array](https://exceljet.net/glossary/array)
 for the _range_ argument. This means you can't use COUNTIF to test values in an array returned by another operation. I don't like this limitation, so I avoid the \*IFS functions when there is a good alternative.

Related formulas
----------------

[![Excel formula: Cell begins with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_begins_with.png "Excel formula: Cell begins with")](https://exceljet.net/formulas/cell-begins-with)

### [Cell begins with](https://exceljet.net/formulas/cell-begins-with)

In this example, the goal is to test values in column B to see if they begin with a specific text string, which is "xyz" in the worksheet shown. This problem can be solved with the LEFT function, as explained below. LEFT function The LEFT function extracts a given number of characters from the left...

[![Excel formula: If cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains.png "Excel formula: If cell contains")](https://exceljet.net/formulas/if-cell-contains)

### [If cell contains](https://exceljet.net/formulas/if-cell-contains)

The goal is to do something if a cell contains a given substring. For example, in the worksheet above, a formula returns "x" when a cell contains "abc". If you are familiar with Excel, you will probably think first of the IF function. However, one limitation of IF is that it does not support...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Highlight cells that contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20specific%20text.png "Excel formula: Highlight cells that contain")](https://exceljet.net/formulas/highlight-cells-that-contain)

### [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each of the 10 cells in B2:B11, and B2 will change to the address of the cell being evaluated each...

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

[![Excel formula: Count cells that contain either x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20either%20x%20or%20y.png "Excel formula: Count cells that contain either x or y")](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

### [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

In this example, the goal is to count cells in the range B5:B15 that contain either "x" or "y", where x and y are both text strings . When you count cells with "OR logic", you need to be careful not to double count. For example, if you are counting cells that contain "blue" or "green", you can't...

Related functions
-----------------

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20extract%20text%20with%20LEFT%20and%20RIGHT-thumb_0.png)](https://exceljet.net/videos/how-to-extract-text-with-left-and-right)

### [How to extract text with LEFT and RIGHT](https://exceljet.net/videos/how-to-extract-text-with-left-and-right)

In this video, we'll look at how to use the RIGHT and LEFT functions to extract specific text from data. Let's take a look. Here we have some customer data. To illustrate how to extract text using the LEFT and RIGHT functions, I'll use them both to pull out just certain parts of this information...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cell begins with](https://exceljet.net/formulas/cell-begins-with)
    
*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)
    
*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    
*   [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)
    

### Functions

*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Videos

*   [How to extract text with LEFT and RIGHT](https://exceljet.net/videos/how-to-extract-text-with-left-and-right)
    

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