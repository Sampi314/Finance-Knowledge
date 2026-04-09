# XLOOKUP wildcard contains substring - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-wildcard-contains-substring

---

[Skip to main content](https://exceljet.net/formulas/xlookup-wildcard-contains-substring#main-content)

[](https://exceljet.net/formulas/xlookup-wildcard-contains-substring#)

*   [Previous](https://exceljet.net/formulas/xlookup-two-way-exact-match)
    
*   [Next](https://exceljet.net/formulas/xlookup-wildcard-match-example)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP wildcard contains substring
===================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7900/download?token=bwOvumB7)
 (15.48 KB)

![Excel formula: XLOOKUP wildcard contains substring](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP_wildcard_contains_substring.png "Excel formula: XLOOKUP wildcard contains substring")

Summary
-------

To create a "contains substring" type lookup formula, you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 with wildcards. In the example shown, the formula in F5 is:

    XLOOKUP("*"&G4&"*",data[Title],data,,2)

Where G4 contains a partial string to look for and **data** is an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range B5:D16. Note that _match\_mode_ must be set to 2 to use wildcards with XLOOKUP.

_Note: In older versions of Excel that do not provide the XLOOKUP function, you can also use the VLOOKUP function. Both formulas are explained below._

Generic formula
---------------

    XLOOKUP("*"&A1&"*",range1,range2,,2)

Explanation 
------------

The goal is to look up the Title, Author, and Year in the list of books as shown using a formula based on a partial match and a wildcard. The text string to search for is entered in cell G4. All data is in an Excel Table named data in the range B5:D16. This problem can be easily solved with the XLOOKUP function or the VLOOKUP function. Both methods are explained below.

### XLOOKUP function

The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 is a modern upgrade to the VLOOKUP function. The full generic syntax for XLOOKUP looks like this:

    =XLOOKUP(lookup_value,lookup_array,return_array,if_not_found,match_mode,search_mode)

Briefly, these arguments have the following meaning:

*   _lookup\_value_ - the value to look for
*   _lookup\_array_ - the range or array to search within
*   _return\_array_ - the range or array to return values from
*   _if\_not\_found_ - the value to return if the _lookup\_value_ is not found 
*   _match\_mode_ - settings for exact, approximate, and wildcard matching
*   _search\_mode_ - control for search direction, and binary search

The XLOOKUP function has built-in support for formula wildcards when the _match\_mode_ argument is set to 2. Only the first three arguments are required in XLOOKUP so for this problem we need to supply four values: _lookup\_value, lookup\_array_, _return\_array,_ and _match\_mode_:

    =XLOOKUP(lookup_value,lookup_array,return_array,,match_mode)

Notice that we simply leave _if\_not\_found_ empty, though you are free to enter any value you like here. To start off, we provide _lookup\_value_. This is the tricky part of the formula:

    =XLOOKUP("*"&G4&"*",

Here, we [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the value in cell G4 to an asterisk (\*) [wildcard](https://exceljet.net/glossary/wildcard)
 on either side. With the string "cop" in cell G4, the result will be a string like "\*cop\*".The asterisk will match "zero or more characters" so by using an asterisk at the start and the end of the search string, we are asking XLOOKUP to match the text _anywhere it occurs in the Title_, which is provided as _lookup\_array_:

    XLOOKUP("*"&G4&"*",data[Title],

Next, we need to provide the _return\_array_. Here, because we want all three columns of data, we use another small trick. Instead of asking for each column separately, we ask for the entire table, which is named **data**:

    XLOOKUP("*"&G4&"*",data[Title],data,

This will cause XLOOKUP to return the entire matching row, with Title, Author, and Year included. Next, we omit a value for _if\_not\_found_ by simply skipping the argument altogether. Feel free to use a value like "Not found" if you like.

    XLOOKUP("*"&G4&"*",data[Title],data,,

Last, we need to provide a value for _match\_mode._ To enable wildcard matching with XLOOKUP, supply the number 2. This is the final XLOOKUP formula in cell G6:

    XLOOKUP("*"&G4&"*",data[Title],data,,2)

There is one more step we need to take. Because we have asked XLOOKUP to return the entire matching row, XLOOKUP will return three values (Title, Author, and Year) in an array that spills onto the worksheet in the original horizontal orientation. We need the results to be organized vertically, so we nest the XLOOKUP function inside the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 like this:

    =TRANSPOSE(XLOOKUP("*"&G4&"*",data[Title],data,,2))

Transpose will "flip" the orientation of the array returned by XLOOKUP. With the text "cop" in cell G4, XLOOKUP will return an array to the TRANSPOSE function like this:

    =TRANSPOSE({"Demon Copperhead","Barbara Kingsolver",2022})

The comma separators tell us this is a _[horizontal array](https://exceljet.net/glossary/array)
_. After TRANSPOSE runs, we have an array like this:

    {"Demon Copperhead";"Barbara Kingsolver";2022}

The semicolons (;) indicate a _vertical array_. The array lands in cell G6, and the values [spill](https://exceljet.net/glossary/spill)
 vertically into the range G6:G8.

### XLOOKUP with individual columns

Although the formula used in the worksheet has XLOOKUP set to return an entire row from **data**, we can easily configure XLOOKUP to return individual columns like this:

    =XLOOKUP("*"&G4&"*",data[Title],data[Title],,2) // title
    =XLOOKUP("*"&G4&"*",data[Title],data[Author],,2) // author
    =XLOOKUP("*"&G4&"*",data[Title],data[Year],,2) // year

Because each formula outputs a single value, the formulas can be placed in any cell and there is no need for the TRANSPOSE function. 

> For more details on XLOOKUP, see [How to use the XLOOKUP function](https://exceljet.net/functions/xlookup-function)
> .

### Get all matches

If you want to get _all matches_, instead of the _first match_, you will need to use the [FILTER function](https://exceljet.net/functions/filter-function)
. You can find an example of FILTER with a "text contains" type match [here](https://exceljet.net/formulas/filter-text-contains)
.

### VLOOKUP function

In older versions of Excel that do not offer the XLOOKUP function, the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 can be used instead like this:

    =VLOOKUP("*"&G4&"*",data,1,0) // title
    =VLOOKUP("*"&G4&"*",data,2,0) // author
    =VLOOKUP("*"&G4&"*",data,3,0) // year

For _lookup\_value_, we use the same wildcard trick explained above: we [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 an asterisk (\*) to either side of the search string in G4:

    =VLOOKUP("*"&G4&"*",

For _table\_array_, we provide the Excel Table named **data**:

    =VLOOKUP("*"&G4&"*",data,

Next, we need to supply a column number, where Title = 1, Author = 2, and Year = 3. To retrieve the Title, we provide 1 for _col\_index\_num_:

    =VLOOKUP("*"&G4&"*",data,1

Finally, we must set VLOOKUP in _exact match mode_ to enable wildcard support. To do that, we provide FALSE or zero for the last argument, called _range\_lookup_, like this:

    =VLOOKUP("*"&G4&"*",data,1,0)

The formulas to retrieve Author and Year are the same, except for the column number:

    =VLOOKUP("*"&G4&"*",data,2,0) // author
    =VLOOKUP("*"&G4&"*",data,3,0) // year

> For more details on VLOOKUP, see [How to use the VLOOKUP function](https://exceljet.net/functions/vlookup-function)
> .

Related formulas
----------------

[![Excel formula: XLOOKUP wildcard match example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20wildcard%20match%20example.png "Excel formula: XLOOKUP wildcard match example")](https://exceljet.net/formulas/xlookup-wildcard-match-example)

### [XLOOKUP wildcard match example](https://exceljet.net/formulas/xlookup-wildcard-match-example)

Working from the inside out, XLOOKUP is configured to find the value in H4 in the Last name column, and return all fields. In order to support wildcards , match\_mode is provided as 2: XLOOKUP(H4,D5:D15,B5:E15,2) // match Last, return all fields The lookup\_value comes from cell H4 The lookup\_array...

[![Excel formula: XLOOKUP match text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20match%20text%20contains.png "Excel formula: XLOOKUP match text contains")](https://exceljet.net/formulas/xlookup-match-text-contains)

### [XLOOKUP match text contains](https://exceljet.net/formulas/xlookup-match-text-contains)

The XLOOKUP function contains built-in support for wildcards, but this feature must be enabled explicitly by setting match mode to the number 2. In the example shown, XLOOKUP is configured to match the value entered in cell E5, which may appear anywhere in the lookup values in B5:B15. The formula...

[![Excel formula: XLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20case%20sensitive.png "Excel formula: XLOOKUP case-sensitive ")](https://exceljet.net/formulas/xlookup-case-sensitive)

### [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the color in the "Color" column. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP...

[![Excel formula: VLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20case%20sensitive.png "Excel formula: VLOOKUP case-sensitive ")](https://exceljet.net/formulas/vlookup-case-sensitive)

### [VLOOKUP case-sensitive](https://exceljet.net/formulas/vlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on Color with VLOOKUP. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". This presents several challenges. First, Excel is not case-sensitive by default, and there is no built-in...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20MATCH%20Function%20for%20exact%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

### [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

The MATCH function finds the relative position of an item in a list. MATCH can find exact matches or approximate matches. In this video, we'll look at how to use MATCH to find an exact match. The MATCH function takes three arguments: the lookup\_value, which is the value you're looking up, the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [XLOOKUP wildcard match example](https://exceljet.net/formulas/xlookup-wildcard-match-example)
    
*   [XLOOKUP match text contains](https://exceljet.net/formulas/xlookup-match-text-contains)
    
*   [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)
    
*   [VLOOKUP case-sensitive](https://exceljet.net/formulas/vlookup-case-sensitive)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    
*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    

### Articles

*   [XLOOKUP vs VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)
    
*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
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