# Count cells that contain specific text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-contain-specific-text

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-contain-specific-text#main-content)

[](https://exceljet.net/formulas/count-cells-that-contain-specific-text#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-contain-positive-numbers)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-contain-text)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that contain specific text
======================================

by Dave Bruns · Updated 17 Aug 2022

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[SEARCH](https://exceljet.net/functions/search-function)

[FIND](https://exceljet.net/functions/find-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")

Summary
-------

To count cells that contain certain text, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 with a [wildcard](https://exceljet.net/glossary/wildcard)
. In the example shown, the formula in E5 is:

    =COUNTIF(B5:B15,"*a*")
    

The result is 6, since there are six cells in B5:B15 that contain the letter "a".

Generic formula
---------------

    =COUNTIF(range,"*txt*")

Explanation 
------------

In this example, the goal is to count cells that _contain_ a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count.

### COUNTIF function

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 counts cells in a range that meet supplied criteria. For example, to count the number of cells in a [range](https://exceljet.net/glossary/range)
 that contain "apple" you can use COUNTIF like this:

    =COUNTIF(range,"apple") // equal to "apple"
    

Notice this is an exact match. To be included in the count, a cell must contain "apple" and only "apple". If a cell contains any other characters, it will not be counted.

In the example shown, the goal is to count cells that _contain_ specific text, meaning the text is a _substring_ that can be anywhere in the cell. To do this, we need to use the asterisk (\*) character as a [wildcard](https://exceljet.net/glossary/wildcard)
. To count cells that contain the substring "apple", we can use a formula like this:

    =COUNTIF(range,"*apple*")
    

The asterisk (\*) wildcard matches zero or more characters of any kind, so this formula will count cells that contain "apple" anywhere in the cell. The formulas used in the worksheet shown follow the same pattern:

    =COUNTIF(B5:B15,"*a*") // contains "a"
    =COUNTIF(B5:B15,"*2*") // contains "2"
    =COUNTIF(B5:B15,"*-S*") // contains "-s"
    =COUNTIF(B5:B15,"*x*") // contains "x"
    

You can easily adjust this formula to use a cell reference in _criteria_. For example, if A1 contains the text you want to match, you can use:

    =COUNTIF(range,"*"&A1&"*")
    

Inside COUNTIF, the two asterisks are [concatenated](https://exceljet.net/glossary/concatenation)
 to the value in A1, and the formula works as before. The COUNTIF function supports three different wildcards, [see this page](https://exceljet.net/functions/countif-function)
 for more details.

Note the COUNTIF formula above won't work if you are looking for a particular number and cells contain numeric data. This is because the wildcard automatically causes COUNTIF to look for text only (i.e. to look for "2" instead of just 2). Because a text value won't ever be found in a true number, COUNTIF will return zero. In addition, COUNTIF is _not_ case-sensitive, so you can't perform a case-sensitive count. The SUMPRODUCT alternative below can handle both cases.

### SUMPRODUCT function

Another way to solve this problem is with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and [Boolean algebra](https://exceljet.net/glossary/boolean-logic)
. This approach has the benefit of being case-sensitive if needed. In addition, you can use this technique to find a number inside of a number, something you can't do with COUNTIF.

To count cells that contain specific text with SUMPRODUCT, you can use the [SEARCH function](https://exceljet.net/functions/search-function)
. SEARCH returns the position of text in a text string as a number. For example, the formula below returns 6 since the "a" appears first as the sixth character in the string:

    =SEARCH( "a","The cat sat") // returns 6
    

If the text is not found, SEARCH returns a #VALUE! error:

    =SEARCH( "x","The cat sat") // returns #VALUE!
    

To count cells that contain "a" in the worksheet shown with SUMPRODUCT, you can use the [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [SEARCH](https://exceljet.net/functions/search-function)
 functions like this:

    =SUMPRODUCT(--ISNUMBER(SEARCH("a",B5:B15)))
    

Working from the inside out, the [logical test](https://exceljet.net/glossary/logical-test)
 inside SUMPRODUCT is based on SEARCH:

    SEARCH("a",B5:B15)
    

Because the range B5:B15 contains 11 cells, the result from SEARCH is an [array](https://exceljet.net/glossary/array)
 with 11 results:

    {1;1;1;1;2;2;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!}
    

In this array, numbers indicate the position of "a" in cells where "a" is found. The #VALUE! errors indicate cells where "a" was not found. To convert these results into a simple array of TRUE and FALSE values, the SEARCH function is [nested](https://exceljet.net/glossary/nesting)
 in the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
:

    ISNUMBER(SEARCH("a",B5:B15))
    

ISNUMBER returns TRUE for any number and FALSE for errors. SEARCH delivers the array of results to ISNUMBER, and ISNUMBER converts the results to an array that contains only TRUE and FALSE values:

    {TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

In this array, TRUE corresponds to cells that contain "a" and FALSE corresponds to cells that do not contain "a". We want to count these results, but we first need to convert the TRUE and FALSE values to their numeric equivalents, 1 and 0. To do this, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--):

    --ISNUMBER(SEARCH("a",B5:B15))
    

The result inside of SUMPRODUCT looks like this:

    =SUMPRODUCT({1;1;1;1;1;1;0;0;0;0;0}) // returns 6
    

With a single array to process, SUMPRODUCT sums the array and returns 6 as a final result.

One benefit of this formula is it will find a number inside a numeric value. In addition, there is no need to use wildcards to indicate position, because SEARCH will automatically look through all text in a cell.

### Case-sensitive option

For a case-sensitive count, you can replace the SEARCH function with the [FIND function](https://exceljet.net/functions/find-function)
 like this:

    =SUMPRODUCT(--(ISNUMBER(FIND(text,range))))
    

The FIND function works just like the SEARCH function, but is case-sensitive. You can use a formula like this to count cells that contain "APPLE" and not "apple". [This example provides more detail](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)
.

Related formulas
----------------

[![Excel formula: Count cells that contain case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20case%20sensitive.png "Excel formula: Count cells that contain case sensitive")](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)

### [Count cells that contain case sensitive](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)

In this example, the goal is to count codes that appear as substrings in a case-sensitive way. The functions COUNTIF and COUNTIFS are both good options for counting text values, but these functions are not case-sensitive, so they can't be used to solve this problem. The solution is to use the FIND...

[![Excel formula: Count cells that contain text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20text.png "Excel formula: Count cells that contain text")](https://exceljet.net/formulas/count-cells-that-contain-text)

### [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)

In this example, the goal is to count cells in a range that contain text values. This could be hard-coded text like "apple" or "red", numbers entered as text, or formulas that return text values. Empty cells and cells that contain numeric values or errors should not be included in the count. This...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Running count of occurrence in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20count%20of%20occurrence%20in%20list.png "Excel formula: Running count of occurrence in list")](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

### [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

In this example, the goal is to create a running count for a specific value that appears in column B. The value to count is entered in cell E5, which is the named range value . The core of the solution explained below is the COUNTIF function , with help from the IF function to suppress a count for...

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Count cells that contain either x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20either%20x%20or%20y.png "Excel formula: Count cells that contain either x or y")](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

### [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

In this example, the goal is to count cells in the range B5:B15 that contain either "x" or "y", where x and y are both text strings . When you count cells with "OR logic", you need to be careful not to double count. For example, if you are counting cells that contain "blue" or "green", you can't...

[![Excel formula: If cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20contains%20one%20of%20many%20things.png "Excel formula: If cell contains one of many things")](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

### [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

This formula uses two named ranges : things , and results . If you are porting this formula directly, be sure to use named ranges with the same names (defined based on your data). If you don't want to use named ranges, use absolute references instead. The core of this formula is this snippet:...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain case sensitive](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)
    
*   [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
    
*   [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)
    
*   [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)
    
*   [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

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