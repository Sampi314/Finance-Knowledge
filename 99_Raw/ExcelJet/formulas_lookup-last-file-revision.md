# Lookup last file revision - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lookup-last-file-revision

---

[Skip to main content](https://exceljet.net/formulas/lookup-last-file-revision#main-content)

[](https://exceljet.net/formulas/lookup-last-file-revision#)

*   [Previous](https://exceljet.net/formulas/longest-winning-streak)
    
*   [Next](https://exceljet.net/formulas/mark-rows-with-logical-tests)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Lookup last file revision
=========================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[SEARCH](https://exceljet.net/functions/search-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[MAX](https://exceljet.net/functions/max-function)

[INDEX](https://exceljet.net/functions/index-function)

[IF](https://exceljet.net/functions/if-function)

[ROW](https://exceljet.net/functions/row-function)

![Excel formula: Lookup last file revision](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lookup%20last%20file%20revision.png "Excel formula: Lookup last file revision")

Summary
-------

To find the position (row) of the last file revision in a table, you can use a formula based on several Excel functions: MAX, IF, ISERROR, ROW, and INDEX. In the example shown, the formula in cell H6 is:

    =MAX(IF(ISERROR(SEARCH(H5&"*",files)),0,ROW(files)-ROW(INDEX(files,1,1))+1))

where "files" is the [named range](https://exceljet.net/glossary/named-range)
 C4:C11.

_Note: this is an array formula and must be entered with control + shift + enter in Excel 2019 and earlier._

Generic formula
---------------

    {=MAX(IF(ISERROR(SEARCH(H5&"*",files)),0,ROW(files)-ROW(INDEX(files,1,1))+1))}
    

Explanation 
------------

### Context

In this example, we have a number of file versions listed in a table with a date and user name. Note that file names are repeated, except for the code appended at the end to represent version ("CA", "CB", "CC", "CD", etc.).

For a given file, we want to locate the position (row number) for the last revision. This is a tricky problem because the version codes at the end of the file names make it harder to match the file name. Also, by default, Excel match formulas will return the first match, not the last match, so we need to work around that challenge with some tricky techniques.

### How the formula works

At the core of this formula, we build a list of row numbers for a given file. Then we use the MAX function to get the largest row number, which corresponds to the last revision (last occurrence) of that file.

To find all occurrences of a given file, we use the SEARCH function, configured with the asterisk (\*) wildcard to match the file name, ignoring the version codes. SEARCH will throw a VALUE error when text isn't found, so we wrap SEARCH with ISERROR:

    ISERROR(SEARCH(H5&"*",files))
    

This results in an array of TRUE and FALSE values like this:

    {FALSE;TRUE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE}

It's confusing, but TRUE represents an error (text not found), and FALSE represents a match. This array result is fed into the IF function as the logical test. For value if TRUE, we use zero, and for value if true, we supply this code, [which generates relative row numbers](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
 for the range we are working with:

    ROW(files)-ROW(INDEX(files,1,1))+1)
    

The IF function then returns an array of values like this:

    {1;0;3;4;0;0;7;0}

All numbers except zero represent matches for "filename1" – i.e. the row number inside the named range "files" where "filename1" appears.

Finally, we use the MAX function to get the maximum value in this array, which is 7 in this example.

Use INDEX with this row number to retrieve information related to the last revision (i.e. full file name, date, user, etc).

### Without named range

Named ranges make it fast and easy to set up a more complex formula, since you don't have to enter cell addresses by hand. However, in this case, we are using an extra function (INDEX) to get the first cell of the named range "files", which complicates things a bit. Without the named range, the formula looks like this:

    {=MAX(IF(ISERROR(SEARCH(H5&"*",C4:C11)),0,ROW(C4:C11)-ROW(C4)+1))}
    

Related formulas
----------------

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

[![Excel formula: Get last match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_match.png "Excel formula: Get last match")](https://exceljet.net/formulas/get-last-match)

### [Get last match](https://exceljet.net/formulas/get-last-match)

In the example shown, we have a set of order data that includes Date, Product, Name, and Amount. The data is sorted by date in ascending order. The goal is to look up the latest order for a given person by Name. In other words, we want the last match by name. The challenge is that Excel lookup...

[![Excel formula: Lookup last file version](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Lookup%20last%20file%20version.png "Excel formula: Lookup last file version")](https://exceljet.net/formulas/lookup-last-file-version)

### [Lookup last file version](https://exceljet.net/formulas/lookup-last-file-version)

This formula uses the LOOKUP function to find and retrieve the last matching file name. The lookup value is 2, and the lookup\_vector is created with this: 1/(ISNUMBER(FIND(G6,files))) Inside this snippet, the FIND function looks for the value in G6 inside the named range "files" (B5:B11). The...

Related functions
-----------------

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

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

*   [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    
*   [Get last match](https://exceljet.net/formulas/get-last-match)
    
*   [Lookup last file version](https://exceljet.net/formulas/lookup-last-file-version)
    

### Functions

*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    

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