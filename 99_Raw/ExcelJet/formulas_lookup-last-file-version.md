# Lookup last file version - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lookup-last-file-version

---

[Skip to main content](https://exceljet.net/formulas/lookup-last-file-version#main-content)

[](https://exceljet.net/formulas/lookup-last-file-version#)

*   [Previous](https://exceljet.net/formulas/lookup-first-negative-value)
    
*   [Next](https://exceljet.net/formulas/lookup-latest-price)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Lookup last file version
========================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[LOOKUP](https://exceljet.net/functions/lookup-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Lookup last file version](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Lookup%20last%20file%20version.png "Excel formula: Lookup last file version")

Summary
-------

To lookup the latest file version in a list, you can use a formula based on the LOOKUP function together with the ISNUMBER and FIND functions. In the example shown, the formula in cell G7 is:

    =LOOKUP(2,1/(ISNUMBER(FIND(G6,files))),files)
    

where "files" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B11.

### Context

In this example, we have a number of file versions listed in a table with a date and user name. Note that file names are repeated with a counter at the end as a revision number - 001, 002, 003, etc.

Given a file name, we want to retrieve the name of the last or latest revision. There are two challenges:

1.  The challenge is the version codes at the end of the file names make it harder to match the file name.
2.  By default, Excel match formulas will return the first match, not the last match.

To overcome these challenges, we need to use some tricky techniques.

Generic formula
---------------

    =LOOKUP(2,1/(ISNUMBER(FIND(filename,range))),range)

Explanation 
------------

This formula uses the LOOKUP function to find and retrieve the last matching file name. The lookup value is 2, and the lookup\_vector is created with this:

    1/(ISNUMBER(FIND(G6,files)))
    

Inside this snippet, the FIND function looks for the value in G6 inside the named range "files" (B5:B11). The result is an array like this:

    {1;#VALUE!;1;1;#VALUE!;#VALUE!;1}
    

Here, the number 1 represents a match, and the #VALUE error represents a non-matching file name. This array goes into the ISNUMBER function and comes out like this:

    {TRUE;FALSE;TRUE;TRUE;FALSE;FALSE;TRUE}
    

Error values are now FALSE, and the number 1 is now TRUE. This overcomes challenge #1, we now have an array that shows clearly which files in the list contain the file name of interest.

Next, the array is used as the denominator with 1 as numerator. The result looks like this:

    {1;#DIV/0!;1;1;#DIV/0!;#DIV/0!;1}
    

which goes into LOOKUP as the lookup\_vector. This is a tricky solution to challenge #2. The LOOKUP function operates in approximate match mode only, and automatically ignores error values. This means with 2 as a lookup value, VLOOKUP will try to find 2, fail, and step back to the previous number (in this case matching the last 1 in position 7). Finally, LOOKUP uses 7 like an index to retrieve the 7th file in the list of files.

### Handling blank lookups

Oddly, the FIND function returns 1 if the lookup value is an [empty string](https://exceljet.net/glossary/empty-string)
 (""). To guard against a false match, you can wrap the formula in IF and test for an empty lookup:

    =IF(G6<>"",LOOKUP(2,1/(ISNUMBER(FIND(G6,files))),files),"")
    

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

[![Excel formula: Lookup last file revision](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20last%20file%20revision.png "Excel formula: Lookup last file revision")](https://exceljet.net/formulas/lookup-last-file-revision)

### [Lookup last file revision](https://exceljet.net/formulas/lookup-last-file-revision)

Context In this example, we have a number of file versions listed in a table with a date and user name. Note that file names are repeated, except for the code appended at the end to represent version ("CA", "CB", "CC", "CD", etc.). For a given file, we want to locate the position (row number) for...

Related functions
-----------------

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

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
    
*   [Lookup last file revision](https://exceljet.net/formulas/lookup-last-file-revision)
    

### Functions

*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

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