# If cell contains - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-cell-contains

---

[Skip to main content](https://exceljet.net/formulas/if-cell-contains#main-content)

[](https://exceljet.net/formulas/if-cell-contains#)

*   [Previous](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)
    
*   [Next](https://exceljet.net/formulas/if-cell-contains-this-or-that)
    

[If](https://exceljet.net/formulas#If)

If cell contains
================

by Dave Bruns · Updated 14 Dec 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[SEARCH](https://exceljet.net/functions/search-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: If cell contains](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_cell_contains.png "Excel formula: If cell contains")

Summary
-------

To test for cells that _contain_ specific text, you can use a formula based on the [IF function](https://exceljet.net/videos/the-if-function)
 combined with the [SEARCH](https://exceljet.net/functions/search-function)
 and [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 functions. In the example shown, the formula in C5 is:

    =IF(ISNUMBER(SEARCH("abc",B5)),B5,"")
    

> To test for "if cell _equals"_ [you can use a simpler formula](https://exceljet.net/formulas/if-cell-equals)
> .

Generic formula
---------------

    =IF(ISNUMBER(SEARCH("abc",A1)),"x","")

Explanation 
------------

The goal is to do something if a cell contains a given substring. For example, in the worksheet above, a formula returns "x" when a cell _contains_ "abc". If you are familiar with Excel, you will probably think first of the IF function. However, one limitation of IF is that it does [not support wildcards](https://exceljet.net/formulas/if-with-wildcards)
 like "?" and "\*". This means we can't use IF by itself to test for a substring like "abc" that might appear _anywhere_ in a cell. One solution is to create a logical test with the SEARCH and ISNUMBER functions, and then use an IF statement to return a final result. This approach is explained below.

### Finding text in a cell

The [SEARCH function](https://exceljet.net/functions/search-function)
 is designed to look for specific text inside a larger text string. If SEARCH finds the text, it returns the _position_ of the text as a number. If the text is not found, SEARCH returns a #VALUE error. For example, the formulas below show the result of looking for the letters "a", "p", "e", and "z" in the text "apple":

    =SEARCH("a","apple") // returns 1
    =SEARCH("p","apple") // returns 2
    =SEARCH("e","apple") // returns 5
    =SEARCH("z","apple") // returns #VALUE!

Notice that SEARCH returns a numeric position for the first three letters, and returns a #VALUE! error for "z", which is not found. The screen below shows how the formulas above can be transferred to a workbook. The text to search appears in column B and the character to look for is hard coded into the SEARCH function:

![Searching for a character in a cell](https://exceljet.net/sites/default/files/images/formulas/inline/if_cell_contains_search_for_character.png "Searching for a character in a cell")

### Finding a word in a cell

You can use the SEARCH function to find words as well. Notice that SEARCH returns the starting position of the word in the text string:

    =SEARCH("quick","The quick brown fox") // returns 5
    =SEARCH("brown","The quick brown fox") // returns 11
    =SEARCH("fox","The quick brown fox") // returns 17
    =SEARCH("dog","The quick brown fox") // returns #VALUE!

As before, if the "find text" isn't found, SEARCH returns a #VALUE! error as in the last example, where the word "dog" is not found. The screen below shows how the formulas can be set up in a spreadsheet. The text to search is in column B. The word to search for is typed directly into the SEARCH function:

![Searching for a word in a cell](https://exceljet.net/sites/default/files/images/formulas/inline/if_cell_contains_search_for_word.png "Searching for a word in a cell")

The formulas above work fine. However, we don't want the position of the text in a cell, what we really want is a TRUE or FALSE result. Enter the ISNUMBER function.

### Converting results to TRUE and FALSE

Since our goal is to use an IF statement, we want a logical test that will return TRUE or FALSE. The SEARCH function doesn't work by itself because it returns either a numeric position or an error. However, we can easily convert the results from SEARCH into TRUE and FALSE values with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
, which returns TRUE for numeric values and FALSE for anything else:

    =ISNUMBER(2) // returns TRUE
    =ISNUMBER("a") // returns FALSE
    =ISNUMBER(#VALUE!) // returns FALSE
    
    

To convert the result from the SEARCH function into a TRUE or FALSE value, we simply place the SEARCH function inside the ISNUMBER function as shown below:

    =ISNUMBER(SEARCH("fox","The brown fox")) // returns TRUE
    =ISNUMBER(SEARCH("dog","The brown fox")) // returns FALSE

To recap: if SEARCH finds the text in the text string, it returns the position as a number, and ISNUMBER returns TRUE. If SEARCH _can't_ find the text, it returns an error, and ISNUMBER returns FALSE. We now have what we need to create an IF statement to check if a cell contains text.

### If a cell contains a word then

Now that we have a formula that returns TRUE or FALSE, we can use the combination of SEARCH + ISNUMBER as the logical test inside the [IF function](https://exceljet.net/functions/if-function)
, and return whatever result we want. In the worksheet shown, we have a list of email addresses, and we want to identify the emails that _contain_ "abc". The formula in cell C5 looks like this:

    =IF(ISNUMBER(SEARCH("abc",B5)),"x","")
    

The SEARCH function is configured to look for "abc" inside cell B5. If "abc" is found anywhere in cell B5, SEARCH returns a number and ISNUMBER returns TRUE. The IF function then returns "x" as a final result. If "abc" is _not found_, SEARCH returns an error and ISNUMBER returns FALSE. The IF function then returns an empty string ("") as a final result. 

### Return matching values

With a small adjustment, we can return the value that contains "abc" instead of returning "x":

![If cell contains "abc" return value](https://exceljet.net/sites/default/files/images/formulas/inline/if_cell_contains_return_value.png "If cell contains "abc" return value")

To return a cell of the value when it contains "abc", we provide a reference for the _value if true_ argument. If FALSE, we supply an empty string ("") which will display as a blank cell. The formula in cell C5 is:

    =IF(ISNUMBER(SEARCH("abc",B5)),B5,"")

### If column contains value then

If you need to check a column for a specific text value, the simplest approach is to switch to the [COUNTIF function](https://exceljet.net/functions/countif-function)
 with wildcards. For example, to return "Yes" if column A contains the word "dog" in any cell and "No" if not, you can use a formula like this:

    =IF(COUNTIF(A:A,"*dog*"),"Yes","No")

The asterisks (\*) are wildcards that match the text "dog" with any number of characters before or after. With this configuration, the COUNTIF function will return a count of cells that contain "dog" anywhere in the cell. If the count is a positive number, the IF function will evaluate the number as TRUE. If no cells contain "dog", COUNTIF will return zero and the IF function will evaluate this result as FALSE.

### Notes

1.  The SEARCH function is _not_ case-sensitive. If you need a case-sensitive option you can switch to the [FIND function](https://exceljet.net/functions/find-function)
     as [explained here](https://exceljet.net/formulas/cell-contains-specific-text)
    .
2.  If the goal is to return all matching cells or records together, see the [FILTER function](https://exceljet.net/formulas/filter-text-contains)
    .

Related formulas
----------------

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: If cell equals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains_0.png "Excel formula: If cell equals")](https://exceljet.net/formulas/if-cell-equals)

### [If cell equals](https://exceljet.net/formulas/if-cell-equals)

The goal is to do something if a cell equals a given value. The most common way to solve this problem is with the IF function. IF function The IF function runs a logical test and returns one value for a TRUE result, and another value for a FALSE result. The generic syntax for IF looks like this: =...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: If cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20contains%20one%20of%20many%20things.png "Excel formula: If cell contains one of many things")](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

### [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

This formula uses two named ranges : things , and results . If you are porting this formula directly, be sure to use named ranges with the same names (defined based on your data). If you don't want to use named ranges, use absolute references instead. The core of this formula is this snippet:...

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: Cell contains specific words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_words.png "Excel formula: Cell contains specific words")](https://exceljet.net/formulas/cell-contains-specific-words)

### [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)

In this example, the goal is to test the text in a cell and return TRUE if it contains one or more specific words, and FALSE if not. Notice the emphasis here is on words, not substrings. For example, if we are testing for the word "green" and the text contains the word "evergreen" but not the word...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [If cell equals](https://exceljet.net/formulas/if-cell-equals)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    
*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    

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