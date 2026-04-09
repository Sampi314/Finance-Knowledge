# Cell begins with - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cell-begins-with

---

[Skip to main content](https://exceljet.net/formulas/cell-begins-with#main-content)

[](https://exceljet.net/formulas/cell-begins-with#)

*   [Previous](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)
    
*   [Next](https://exceljet.net/formulas/cell-contains-all-of-many-things)
    

[Text](https://exceljet.net/formulas#Text)

Cell begins with
================

by Dave Bruns · Updated 27 Jan 2023

Related functions 
------------------

[LEFT](https://exceljet.net/functions/left-function)

[EXACT](https://exceljet.net/functions/exact-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Cell begins with](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cell_begins_with.png "Excel formula: Cell begins with")

Summary
-------

To test if a cell begins with specific text, you can use a formula based on the [LEFT function](https://exceljet.net/functions/left-function)
. In the example shown, the formula in cell D5, copied down, is:

    =LEFT(B5,3)="xyz"

This formula returns TRUE when the value in column B begins with "xyz" and FALSE if not. Note that this formula is _not_ case-sensitive. See below for a case-sensitive option.

Generic formula
---------------

    =LEFT(A1,3)="xyz"

Explanation 
------------

In this example, the goal is to test values in column B to see if they begin with a specific text string, which is "xyz" in the worksheet shown. This problem can be solved with the LEFT function, as explained below.

### LEFT function

The [LEFT function](https://exceljet.net/functions/left-function)
 extracts a given number of characters from the left side of a text string. For example, the formula below returns the first three letters of "apple", which is "app":

    =LEFT("apple",3) // returns "app"

This means we can use the LEFT function to test if cell B5 begins with "xyz" like this:

    =LEFT(B5,3)="xyz"

The LEFT function extracts the first 3 characters in cell B5 and the result is compared to the string "xyz" forcing a TRUE or FALSE result. The formula is solved like this:

    =LEFT(B5,3)="xyz"
    =LEFT("ABC-1224-HNN",3)="xyz"
    ="ABC"="xyz"
    =FALSE

For cell B5 the result is FALSE, since "ABC-1224-HNN" does not begin with "xyz". In cell B6, however, the result is TRUE, since "XYZ-6543-JWB" _does_ begin with "xyz".

    =LEFT(B6,3)="xyz"
    =LEFT("XYZ-6543-JWB",3)="xyz"
    ="XYZ"="xyz"
    =TRUE

Note that Excel is not case-sensitive by default, so "XYZ"="xyz" will return TRUE in a formula. Also note the _num\_chars_ argument is set to 3 above, but must be modified according to the situation. For example, to test for a value that begins with "apple", _num\_chars_ should be set to 5:

    =LEFT(B5,5)="apple"

###   
Case-sensitive option

Excel is not case-sensitive by default, but you can easily adapt the formula to use the [EXACT function](https://exceljet.net/functions/exact-function)
 to make the formula case-sensitive like this:

    =EXACT(LEFT(B5,3),"xyz")

EXACT takes two arguments, _text1_ and _text2_. EXACT will only return TRUE when _text1_ and _text2_ are exactly the same, taking into account case. For example:

    =EXACT("abc","ABC") // returns FALSE
    =EXACT("abc","Abc") // returns FALSE
    =EXACT("abc","abc") // returns TRUE

Turning back to cell B6 in the worksheet shown, the two formulas below return different results:

    =EXACT(LEFT(B6,3),"xyz") // returns FALSE
    =EXACT(LEFT(B6,3),"XYZ") // returns TRUE

The first formula returns FALSE because the EXACT function is case-sensitive, so "XYZ" _does not_ equal "xyz". The second formula returns TRUE because "XYZ" _does_ equal "XYZ" taking into account case. Note we don't need the equal to operator (=) in this formula since EXACT performs a comparison automatically.

### If cell begins with

To adapt the formulas above to "If cell begins with", simply drop the formulas into the [IF function](https://exceljet.net/functions/if-function)
 as the logical test. For example, to return "Yes" when a cell contains "xyz" and "No" when not, you can use a formula like this

    =IF(LEFT(B5,3)="xyz", "Yes", "No")
    

The case-sensitive version of the formula works the same way:

    =IF(EXACT(LEFT(B5,3),"XYZ"), "Yes", "No")
    

### Other functions

It is worth noting that Excel contains two other functions, the [SEARCH function](https://exceljet.net/functions/search-function)
 and the [FIND function](https://exceljet.net/functions/find-function)
 that are meant to look for a substring in a text value. They could be used to solve this problem, but they are more work to configure in this case, and the resulting formulas are more complicated, so I don't see any advantage to using them.

Alternately, you could use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 with a [wildcard](https://exceljet.net/functions/countif-function)
 to solve this problem like this:

    =COUNTIF(B5,"xyz*")<>0

This works fine, but keep in mind that COUNTIF is in a [group of eight \*IFS functions](https://exceljet.net/articles/excels-racon-functions)
 that won't accept an [array](https://exceljet.net/glossary/array)
 for the _range_ argument. This means you can't use COUNTIF to test values in an array returned by another operation. I don't like this limitation, so I avoid the \*IFS functions when there is a good alternative.

Related formulas
----------------

[![Excel formula: Cell ends with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_ends_with.png "Excel formula: Cell ends with")](https://exceljet.net/formulas/cell-ends-with)

### [Cell ends with](https://exceljet.net/formulas/cell-ends-with)

In this example, the goal is to test values in column B to see if they end with a specific text string, which is "jwb" in the worksheet shown. This problem can be solved with the RIGHT function, as explained below. RIGHT function The RIGHT function extracts a given number of characters from the...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Categorize text with keywords](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/categorize_text_with_keywords.png "Excel formula: Categorize text with keywords")](https://exceljet.net/formulas/categorize-text-with-keywords)

### [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)

In this example, the goal is to categorize various expenses using the categories shown in column F and the keywords shown in column E. This is a case where it seems like we should perform a lookup operation of some kind, but the problem is that the keywords appear embedded in the text and the...

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

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

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

*   [Cell ends with](https://exceljet.net/formulas/cell-ends-with)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)
    
*   [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)
    
*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    
*   [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)
    

### Functions

*   [LEFT Function](https://exceljet.net/functions/left-function)
    
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