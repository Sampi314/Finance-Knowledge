# LAMBDA contains which things - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lambda-contains-which-things

---

[Skip to main content](https://exceljet.net/formulas/lambda-contains-which-things#main-content)

[](https://exceljet.net/formulas/lambda-contains-which-things#)

*   [Previous](https://exceljet.net/formulas/lambda-contains-one-of-many)
    
*   [Next](https://exceljet.net/formulas/lambda-count-words)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

LAMBDA contains which things
============================

by Dave Bruns · Updated 31 Oct 2023

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LET](https://exceljet.net/functions/let-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SEARCH](https://exceljet.net/functions/search-function)

[SORTBY](https://exceljet.net/functions/sortby-function)

![Excel formula: LAMBDA contains which things](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lambda%20contains%20which%20strings.png "Excel formula: LAMBDA contains which things")

Summary
-------

This example explains the conversion of the [standard Excel formula here](https://exceljet.net/formulas/get-all-matches-cell-contains)
 into a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
. In the example shown, cell C5 contains the custom function, copied down:

    =ContainsWhichThings(B5,things,", ","")
    

where B5 contains the text to process, **things** is the [named range](https://exceljet.net/glossary/named-range)
 E5:E9, the delimiter is a comma, and the default value is an [empty string](https://exceljet.net/glossary/empty-string)
 (""). See below for a detailed explanation.

Explanation 
------------

The goal in this example is to use a formula to report which things exist in a cell. The list of things to check for is in the [named range](https://exceljet.net/glossary/named-range)
 **things** (E5:E9). The result is returned as a comma separated text string.

The first step in creating a custom function with the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 is to verify the logic needed to solve the problem. The formula below will do the job and return the result seen in column C:

    =TEXTJOIN(", ",1,FILTER(things,ISNUMBER(SEARCH(things,B5)),""))
    

This formula uses four separate functions: [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
, [FILTER](https://exceljet.net/functions/filter-function)
, [ISNUMBER](https://exceljet.net/functions/isnumber-function)
, and [SEARCH](https://exceljet.net/functions/search-function)
. The core search logic is [explained in detail here](https://exceljet.net/formulas/cell-contains-specific-text)
. FILTER catches the output from SEARCH and returns a list of matching strings, and TEXTJOIN concatenates the values together and returns a final result.

Thinking about the logic in a more general way, we can see that there are at least four potential inputs: the **text** to process, the **things** to look for, the **delimiter** to use when joining final result, and a **default** value to return if the formula finds no matches. The formula below is a direct port to LAMBDA syntax, with the four inputs above as set up as named arguments:

    =LAMBDA(text,things,delim,default,TEXTJOIN(delim,1,FILTER(things,ISNUMBER(SEARCH(things,text)),default)))
    

Notice the four inputs above have been defined as function arguments. Once this generic version of the function is named and defined with the [Name Manager](https://exceljet.net/glossary/name-manager)
, the custom function can be used like this:

    =ContainsWhichThings(B5,things,", ","")
    

with the same result as before.

### Adding a sort option

In the LAMBDA example above, the primary benefit of making a custom function is ease of use: the custom function is easier to call and configure than the original formula.

However, if we extend the formula to sort results in the order things were found in the text, the base formula becomes significantly more complex and redundant:

    =TEXTJOIN(", ",1,SORTBY(FILTER(things,ISNUMBER(SEARCH(things,B5)),""),SEARCH(FILTER(things,ISNUMBER(SEARCH(things,B5)),""),B5)))
    

In this version, we sort the list returned by FILTER by the position at which things occur in the text. We do this with the [SORTBY function](https://exceljet.net/functions/sortby-function)
 and the main complication is in creating a _sort\_by_ argument, which is done here:

    SEARCH(FILTER(things,ISNUMBER(SEARCH(things,B5)),""),B5) // sort_by
    

Notice the code inside the outer SEARCH repeats code already in the formula. To clean things up, we'll want to use the [LET function](https://exceljet.net/functions/let-function)
, but first, we'll update the existing LAMBDA code to use the new sort logic:

    =LAMBDA(text,things,delim,default,
      TEXTJOIN(", ",1,
        SORTBY(
          FILTER(things,ISNUMBER(SEARCH(things,text)),""),
          SEARCH(FILTER(things,ISNUMBER(SEARCH(things,text)),""),text))
      )
    )(B5,things,", ","")
    

The generic function above works fine, but is still redundant. We can reduce the redundant code by assigning intermediate results to variables with the LET function. Below is a refactored version of the formula above:

    =LAMBDA(text,things,delim,default,
    LET(
      searchResults,FILTER(things,ISNUMBER(SEARCH(things,text)),""),
      sortedResults,SORTBY(searchResults,SEARCH(searchResults,text)),
      result,TEXTJOIN(", ",1,sortedResults),
      result
      )
    )(B5,things,", ","")
    

Notice the primary FILTER(ISNUMBER(SEARCH())) code only appears once now, and the result is assigned to the variable "searchResults", which is used twice in the line below. Next, we'll make the sort optional, by adding a new argument called _sort_:

    =LAMBDA(text,things,delim,default,sort,
    LET(
      searchResults,FILTER(things,ISNUMBER(SEARCH(things,text)),""),
      sortedResults,IF(sort,
      SORTBY(searchResults,SEARCH(searchResults,text)),searchResults),
      result,TEXTJOIN(", ",1,sortedResults),
      result
      )
    )(B5,things,", ","",TRUE)
    

The _sort_ argument acts like a toggle. When _sort_ is TRUE, the function will sort search results in the order they appear in text. When _sort_ is FALSE, the function will leave the list unsorted, and found items will appear in their original order (i.e. the order they are listed in "things").  The logic for this is handled by the [IF function](https://exceljet.net/functions/if-function)
. This is a good example of how the LAMBDA and LET functions together make it possible to extend the behavior of a custom function.

The screen below shows the new version of the formula in action. Notice the _sort_ argument has been set to TRUE, so results are now sorted in the order they appear in **text:**

![LAMBDA contains which strings sorted](https://exceljet.net/sites/default/files/images/formulas/inline/lambda%20contains%20which%20strings%20sort.png "LAMBDA contains which strings sorted")

Related formulas
----------------

[![Excel formula: LAMBDA contains one of many](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20contains%20one%20of%20many.png "Excel formula: LAMBDA contains one of many")](https://exceljet.net/formulas/lambda-contains-one-of-many)

### [LAMBDA contains one of many](https://exceljet.net/formulas/lambda-contains-one-of-many)

Excel does not provide a dedicated "contains" function, but you can create a custom function to test if a cell contains one or many strings with the LAMBDA function . LAMBDA functions do not require VBA, but are only available in Excel 365 . The first step in creating a custom LAMBDA function is to...

[![Excel formula: Count total words in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_total_words_in_cell.png "Excel formula: Count total words in a cell")](https://exceljet.net/formulas/count-total-words-in-a-cell)

### [Count total words in a cell](https://exceljet.net/formulas/count-total-words-in-a-cell)

In this example, the goal is to count the total number of words in a cell. Excel doesn't have a dedicated function for counting words. However, with a little ingenuity, you can create a formula to perform this task using a combination of built-in functions. In newer versions of Excel, the best...

[![Excel formula: LAMBDA replace characters recursive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20replace%20characters.png "Excel formula: LAMBDA replace characters recursive")](https://exceljet.net/formulas/lambda-replace-characters-recursive)

### [LAMBDA replace characters recursive](https://exceljet.net/formulas/lambda-replace-characters-recursive)

The LAMBDA function can be used to create custom, reusable functions in Excel. This example illustrates a feature called recursion, in which a function calls itself. Recursion can be used to create elegant, compact, non-redundant code. However, one disadvantage to recursive LAMBDA functions is that...

[![Excel formula: LAMBDA count words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20count%20words.png "Excel formula: LAMBDA count words")](https://exceljet.net/formulas/lambda-count-words)

### [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)

The LAMBDA function can be used to create reusable, custom functions in Excel without VBA or macros. The first step in creating a LAMBDA function is to verify the formula logic needed in a standard Excel formula. In this example, the base formula is: =LEN(TRIM(B5))-LEN(SUBSTITUTE(B5," ",""))+(LEN(...

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [LAMBDA contains one of many](https://exceljet.net/formulas/lambda-contains-one-of-many)
    
*   [Count total words in a cell](https://exceljet.net/formulas/count-total-words-in-a-cell)
    
*   [LAMBDA replace characters recursive](https://exceljet.net/formulas/lambda-replace-characters-recursive)
    
*   [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    

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