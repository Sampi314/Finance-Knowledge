# Reverse a list or range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/reverse-a-list-or-range

---

[Skip to main content](https://exceljet.net/formulas/reverse-a-list-or-range#main-content)

[](https://exceljet.net/formulas/reverse-a-list-or-range#)

*   [Previous](https://exceljet.net/formulas/return-array-with-index-function)
    
*   [Next](https://exceljet.net/formulas/risk-matrix-example)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Reverse a list or range
=======================

by Dave Bruns · Updated 10 Nov 2025

Related functions 
------------------

[ROWS](https://exceljet.net/functions/rows-function)

[ROW](https://exceljet.net/functions/row-function)

[SORTBY](https://exceljet.net/functions/sortby-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[REDUCE](https://exceljet.net/functions/reduce-function)

[INDEX](https://exceljet.net/functions/index-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9410/download?token=B4IvIoVr)
 (31.47 KB)

![Excel formula: Reverse a list or range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/reverse_a_list_or_range.png "Excel formula: Reverse a list or range")

Summary
-------

To reverse a list (i.e. arrange the values in a range in reverse order), you can use a formula based on the [SORTBY](https://exceljet.net/functions/sortby-function)
 function and the [SEQUENCE](https://exceljet.net/functions/sequence-function)
 function. In the example shown, the formula in D5, copied down, is:

    =SORTBY(B5:B14,SEQUENCE(ROWS(B5:B14)),-1)
    

When the formula is entered in cell D5, the result is the items in the range B5:B14 sorted in reverse order: the first item appears last, the second item appears second to last, and so on.

Generic formula
---------------

    =SORTBY(range,SEQUENCE(ROWS(range)),-1)

Explanation 
------------

In this example, the goal is to "reverse" the items in the range B5:B14, so that the first item appears last, the second item appears second to last, and so on. When you first encounter a problem like this in Excel, your first instinct might be to sort the values in some way using the [SORT function](https://exceljet.net/functions/sort-function)
 or Excel's built-in sort feature. If the items happen to be sorted in alphabetical order, A-Z, you can indeed sort in descending order, Z-A. But what if the items are not sorted in alphabetical order? What if they are in some other order? In that case, you need to use a different approach. What we really want to do in this case is to sort the items in reverse order using their row number. The challenge is that the row number is not part of the data.

### Table of contents

*   [Reversing values in a range](https://exceljet.net/formulas/reverse-a-list-or-range#reversing-values-in-a-range)
    
*   [Alternative formulas](https://exceljet.net/formulas/reverse-a-list-or-range#alternative-formulas)
    
*   [Reversing values in a range by columns](https://exceljet.net/formulas/reverse-a-list-or-range#reversing-values-in-a-range-by-columns)
    
*   [Reversing a comma-separated list](https://exceljet.net/formulas/reverse-a-list-or-range#reversing-a-comma-separated-list)
    
*   [Reversing comma-separated lists for an entire range](https://exceljet.net/formulas/reverse-a-list-or-range#reversing-comma-separated-lists-for-an-entire-range)
    
*   [Reversing a range in Excel 2019 and earlier](https://exceljet.net/formulas/reverse-a-list-or-range#reversing-a-range-in-excel-2019-and-earlier)
    
*   [Implicit intersection operator](https://exceljet.net/formulas/reverse-a-list-or-range#implicit-intersection-operator)
    

### Reversing values in a range

In a current version of Excel, the easiest way to solve this problem is to use a formula based on the [SORTBY function](https://exceljet.net/functions/sortby-function)
 and the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. This is the approach used in the worksheet shown, where the formula in D5 is:

    =SORTBY(B5:B14,SEQUENCE(ROWS(B5:B14)),-1)
    

![Using SORTBY with SEQUENCE to reverse the order of values in a range.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/reverse-a-list-or-range-sortby-and-sequence.png "Using SORTBY with SEQUENCE to reverse the order of values in a range.")

The SORTBY function is designed to sort an array of values in a specific order given by another array, which must be sized to match the array being sorted. In this case, the order is given by the array created by the SEQUENCE function, which is configured like this:

    =SEQUENCE(ROWS(B5:B14))
    

Inside the SEQUENCE function, the [ROWS function](https://exceljet.net/functions/rows-function)
 is used to get the number of rows in the range B5:B14. ROWS returns 10, and this is used as the _rows_ argument in SEQUENCE. The result is an array of numbers from 1 to 10:

    =SEQUENCE(ROWS(B5:B14))
    =SEQUENCE(10)
    ={1;2;3;4;5;6;7;8;9;10}
    

This array is returned to SORTBY as the _by\_array1_ argument, and _sort\_order1_ is provided as -1, which means to sort in descending order:

    =SORTBY(B5:B14,{1;2;3;4;5;6;7;8;9;10},-1)
    

The final result is the items in the range B5:B14 sorted in reverse order.

> Another way to think of this formula is that we are first generating a set of row numbers that don't exist in the data and then using the SORTBY function to sort values in reverse order using the generated row numbers.

> **Pro tip:** You can shorten the formula above a bit by _negating_ the output from SEQUENCE directly, like this: `=SORTBY(B5:B14,-SEQUENCE(ROWS(B5:B14)))`. The output from SEQUENCE is then the negative sequence `{-1;-2;-3;-4;-5;-6;-7;-8;-9;-10}` and there is no need to ask SORTBY to sort in descending order. It's clever, but less intuitive for normal users.

### Alternative formulas

Here are some notes on other related formulas suggested by readers. First, since we already have row numbers, why don't we use them directly like this:

    =SORTBY(B5:B14,ROW(B5:B14),-1)

Here, we use the [ROW function](https://exceljet.net/functions/row-function)
 instead of the ROWS function. For the range B5:B14, ROW returns the array  `{5;6;7;8;9;10;11;12;13;14}` and the formula works as expected. However, one key limitation of this approach is that it won't work if the input is an [array](https://exceljet.net/glossary/array)
; the formula _needs_ actual row numbers. This means you can't use it to reverse an array created by another formula directly.

Jeet suggested a clever formula based on [INDEX](https://exceljet.net/functions/index-function)
 and SEQUENCE. In this formula, we get a row count with ROWS, then use SEQUENCE to build a sequence in reversed order `{10;9;8;7;6;5;4;3;2;1}` by starting SEQUENCE at the count `c` and using -1 as the _step_. Then we use INDEX to pick out the values at those locations:

    =LET(r,B5:B14,c,ROWS(r),INDEX(r,SEQUENCE(c,1,c,-1)))

Finally, Matt Hanchett suggested a formula based on the [REDUCE function](https://exceljet.net/functions/reduce-function)
:

    =REDUCE(,B5:B14,LAMBDA(a,v,VSTACK(v,a)))

In this formula, we omit the _initial\_value_ to keep the formula short. This relies on an interesting behavior of REDUCE when the _initial\_value_ argument is omitted: it will use the first value in the array as the starting value of the accumulator (`a`). This behavior is undocumented, but [mentioned here](https://exceljet.net/functions/reduce-function)
. Note that it will only work with 1D arrays. However, it's still a great example of how the REDUCE+VSTACK technique works.

### Reverse values in a range by columns

To reverse the values in a range by columns, you can use a variation of the formula above. The formula in D5 looks like this:

    =SORTBY(B5:K5,SEQUENCE(,COLUMNS(B5:K5)),-1)
    

![Reversing values in a range by column with a variation of the same formula.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/reverse-a-list-or-range-by-columns.png "Reversing values in a range by column with a variation of the same formula.")

This formula is very similar to the original formula above. The difference is that we have replaced the ROWS function with the [COLUMNS function](https://exceljet.net/functions/columns-function)
 , and we have added a comma to the SEQUENCE function to skip the _rows_ argument so that SEQUENCE creates a horizontal array of numbers in columns. The result is the values in the range B5:K5 sorted in reverse order by columns.

### Reversing a comma-separated list

An interesting variant of the formula above is when you want to reverse the order of comma-separated values in text strings, as seen below. The gist of this solution is to use the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 to split the values into an array. Then use the formula above to sort the array in reverse order. Then use the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 to join the values together again. The formula in D5 looks like this:

    =LET(
      names,TRIM(TEXTSPLIT(B5,,",")),
      snames,SORTBY(names,SEQUENCE(ROWS(names)),-1),
      TEXTJOIN(", ",,snames)
    )
    

![Reversing values in a comma separated list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/reverse-a-comma-separated-list.png "Reversing values in a comma separated list")

At the highest level, the [LET function](https://exceljet.net/functions/let-function)
 is used to assign names to intermediate results. The name _names_ is assigned the result of the TEXTSPLIT function, and the name _snames_ is assigned the result of the SORTBY function. The TEXTJOIN function is used to join the values together again, with a comma and a space between each value. Here's how this formula works step-by-step, working from the inside out:

1.  The TEXTSPLIT function is used to split the values in the text string in B5 into an array of values. Notice we have skipped the _col\_delimiter_ argument, and provided a comma as the _row\_delimiter_ so that the resulting array is a single column of rows.
2.  The [TRIM function](https://exceljet.net/functions/trim-function)
     is used to remove any leading or trailing spaces from each value. This is a normalization step to ensure that the values do not contain any leading or trailing spaces.
3.  The SORTBY function is used to sort the array of values in reverse order, as explained in the original formula above.
4.  The TEXTJOIN function is used to join the values together again, with a comma and a space between each value.

When the formula is entered in cell D5, the result is the values in the text string in B5 reversed in order. As the formula is copied down column D, the process repeats for each text string in the range B5:B14.

> Notice the way we use the SORTBY function in this formula is essentially the same as the original formula above: We are sorting rows in reverse order using an array created by the SEQUENCE function.

### Reversing comma-separated lists for an entire range

To process the entire range in one step, you can adapt the formula above to use the [REDUCE function](https://exceljet.net/functions/reduce-function)
 with the [VSTACK function](https://exceljet.net/functions/vstack-function)
. The formula in D5 looks like this:

    =DROP(REDUCE("",B5:B14,LAMBDA(a,v,VSTACK(a,LET(
      names,TRIM(TEXTSPLIT(v,,",")),
      snames,SORTBY(names,SEQUENCE(ROWS(names)),-1),
      TEXTJOIN(", ",,snames)
    )))),1)
    

![Reversing values in a comma separated list for an entire range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/reverse-a-comma-separated-list-entire-range.png "Reversing values in a comma separated list for an entire range")

This formula works by iterating over each value in the range B5:B14 using the REDUCE function. For each value `v` in the range, the LAMBDA function:

1.  Splits the comma-separated values using TEXTSPLIT
2.  Trims any leading or trailing spaces using TRIM
3.  Reverses the order using SORTBY and SEQUENCE (as explained in the previous section)
4.  Joins the reversed values back together using TEXTJOIN

The VSTACK function stacks each processed result vertically into a single array. The initial value of an empty string ("") is provided to REDUCE, which creates an extra row that we remove using the DROP function. The final result is an array of reversed comma-separated lists that spills into the range D5:D14.

> This pattern of using REDUCE with VSTACK is useful when you need to process each element in a range and return an array of results. The REDUCE function iterates over the range, and VSTACK progressively builds up the final array. For more examples of this pattern, see the [REDUCE function](https://exceljet.net/functions/reduce-function)
>  page.

### Reversing a range in Excel 2019 and earlier

If you are using a legacy version of Excel, you can use a more complex formula based on the [INDEX](https://exceljet.net/functions/index-function)
, [ROWS](https://exceljet.net/functions/rows-function)
, and [ROW](https://exceljet.net/functions/row-function)
 functions. The formula in D5 looks like this:

    =INDEX(list,ROWS(list)+ROW(list)-ROW(),1)
    

![Reversing values in a range in Excel 2019 and earlier](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/reverse-a-list-or-range-excel-2019-and-earlier.png "Reversing values in a range in Excel 2019 and earlier")

> This formula only makes sense if you are using an older version of Excel that does not have the SORTBY and SEQUENCE functions.

As this formula is copied down, it returns the items in reverse order. The name "list" is a [named range](https://exceljet.net/glossary/named-range)
 B5:B14. Named ranges are [absolute references](https://exceljet.net/glossary/absolute-reference)
 by default, so they are convenient to use in a situation like this. If you don't use a named range, use an absolute reference like $B$5:$B$14 instead.

The heart of this formula is the [INDEX](https://exceljet.net/functions/index-function)
 function, which is given the list as the **array** argument:

    =INDEX(list,
    

The second part of the formula is an expression that works out the correct row number as the formula is copied down:

    ROWS(list)+ROW(list)-ROW()
    

1.  ROWS(list) returns the number of rows in the list (10 in the example)
2.  ROW(list) returns the first row number of `list` (5 in the example)
3.  ROW() returns the row number the formula resides in

The result of this expression is a single number starting at 10, and ending at 1 as the formula is copied down. The first formula returns the 10th item in the list, the second formula returns the 9th item in the list, and so on:

    =INDEX(list,10+5-5,1) // item 10
    =INDEX(list,10+5-6,1) // item 9
    =INDEX(list,10+5-7,1) // item 8
    etc.
    

### Implicit intersection operator

Note that if you enter or open the legacy formula above in a modern version of Excel, Excel will add the implicit intersection operator to the formula, as seen in the screenshot above

    =@INDEX(list,ROWS(list)+@ROW(list)-ROW(),1)
    

This @ symbol is called the [implicit intersection](https://exceljet.net/glossary/implicit-intersection)
 operator, and it disables the automatic array behavior where multiple values spill onto the worksheet. In other words, it tells Excel you want a single value. This is done to ensure that older formulas continue to return the same (single) result when they might otherwise spill multiple values onto the worksheet and generate #SPILL! errors.

Related formulas
----------------

[![Excel formula: Sort comma separated values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort_comma_separated_values.png "Excel formula: Sort comma separated values")](https://exceljet.net/formulas/sort-comma-separated-values)

### [Sort comma separated values](https://exceljet.net/formulas/sort-comma-separated-values)

In this example the goal is to sort the comma separated values in column B in alphabetical order. In the latest version of Excel, you can solve this problem with a formula based on TEXTSPLIT, SORT, and TEXTJOIN. In earlier versions of Excel the problem is more complicated. See below for a couple of...

[![Excel formula: Random sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20sort%20formula.png "Excel formula: Random sort formula")](https://exceljet.net/formulas/random-sort-formula)

### [Random sort formula](https://exceljet.net/formulas/random-sort-formula)

This formula depends on two helper columns. The first helper column holds random values created with the RAND() function. The formula in C5, copied down is: =RAND() The RAND function generates a random value at each row. Note: RAND is a volatile function and will generate new values with each...

[![Excel formula: Sort and extract unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20and%20extract%20unique%20values.png "Excel formula: Sort and extract unique values")](https://exceljet.net/formulas/sort-and-extract-unique-values)

### [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)

Note: the core idea of this formula is adapted from an example in Mike Girvin's excellent book Control+Shift+Enter . The example shown uses several formulas, which are described below. At a high level, the MMULT function is used to compute a numeric rank in a helper column (column C), and this rank...

[![Excel formula: Reverse text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/reverse%20text%20string.png "Excel formula: Reverse text string")](https://exceljet.net/formulas/reverse-text-string)

### [Reverse text string](https://exceljet.net/formulas/reverse-text-string)

At the core, this formula uses the MID function to extract each character of a text string in reverse order. The starting character is given as a list of numbers in descending order hard-coded as array constant: MID(B5,{10,9,8,7,6,5,4,3,2,1},1) The text argument comes B5, and 1 is specified for the...

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

Related functions
-----------------

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel REDUCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20reduce%20function.png "Excel REDUCE function")](https://exceljet.net/functions/reduce-function)

### [REDUCE Function](https://exceljet.net/functions/reduce-function)

The Excel REDUCE function applies a custom LAMBDA function to each element in a given array and accumulates results to a single value.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sort comma separated values](https://exceljet.net/formulas/sort-comma-separated-values)
    
*   [Random sort formula](https://exceljet.net/formulas/random-sort-formula)
    
*   [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)
    
*   [Reverse text string](https://exceljet.net/formulas/reverse-text-string)
    
*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    

### Functions

*   [ROWS Function](https://exceljet.net/functions/rows-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [REDUCE Function](https://exceljet.net/functions/reduce-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

### Links

*   [Reverse a list (chandoo)](http://chandoo.org/wp/2009/11/19/reverse-a-list-in-excel/)
    

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