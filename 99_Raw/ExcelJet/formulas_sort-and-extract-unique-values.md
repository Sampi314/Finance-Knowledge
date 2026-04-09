# Sort and extract unique values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sort-and-extract-unique-values

---

[Skip to main content](https://exceljet.net/formulas/sort-and-extract-unique-values#main-content)

[](https://exceljet.net/formulas/sort-and-extract-unique-values#)

*   [Previous](https://exceljet.net/formulas/simple-currency-conversion)
    
*   [Next](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Sort and extract unique values
==============================

by Dave Bruns · Updated 22 Sep 2022

Related functions 
------------------

[MMULT](https://exceljet.net/functions/mmult-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Sort and extract unique values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sort%20and%20extract%20unique%20values.png "Excel formula: Sort and extract unique values")

Summary
-------

To dynamically sort and extract unique values from a list of data, you can use an [array formula](https://exceljet.net/glossary/array-formula)
 to establish a rank in a [helper column](https://exceljet.net/glossary/helper-column)
, then use a specially constructed [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula to extract unique values. In the example shown, the formula to establish rank in C5:C13 is:

    =IF(data="",ROWS(data),MMULT(--(data>TRANSPOSE(data)),ROW(data)^0))
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B13.

_Note: this is a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
, entered with control + shift + enter._

Generic formula
---------------

    =MMULT(--(data>TRANSPOSE(data)),ROW(data)^0)

Explanation 
------------

_Note: the core idea of this formula is adapted from an example in [Mike Girvin's](https://www.youtube.com/user/excelisfun)
 excellent book [Control+Shift+Enter](http://www.amazon.com/gp/product/1615470077/?tag=exceljet-20)
._

The example shown uses several formulas, which are described below. At a high level, the [MMULT function](https://exceljet.net/functions/mmult-function)
 is used to compute a numeric rank in a helper column (column C), and this rank is then used by an [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula in column G to extract unique values.

### Ranking data values

The MMULT function performs matrix multiplication and is used to assign a numeric rank to each value. The first array is created with the following expression:

    --(data>TRANSPOSE(data))
    

Here, we use the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 to create a horizontal [array](https://exceljet.net/glossary/array)
 of **data**, and all values are compared to one another. In essence, each value is compared against _every other value_ to answer the question "is this value greater than every other value". This results in a two-dimensional array, 9 columns x 9 rows, filled with TRUE and FALSE values. The [double negative](https://exceljet.net/glossary/double-unary)
 (--) is used to coerce the TRUE FALSE values to 1s and zeros. You can visualize the resulting array like this:

![Array result from MMULT function](https://exceljet.net/sites/default/files/images/formulas/inline/array%20result%20from%20MMULT%20operation.png "Array result from MMULT function")

The matrix of 1s and zeros above becomes **array1** inside the MMULT function. **Array2** is created with this expression:

    ROW(data)^0
    

Here, each row number in "data" is raised to the power of zero to create a one-dimensional array, 1 column x 9 rows, filled with the number 1. MMULT then returns the matrix product of the two arrays, which become the values seen in the rank column.

We get back all 9 rankings at the same time in an [array](https://exceljet.net/glossary/array)
, so we need to put the results into different cells all at once. Otherwise, each cell will only show the first ranking value in the array that is returned.

_Note: this is a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
, entered with control + shift + enter, in the range C5:C13._

### Handling blank cells

Empty cells are handled with this part of the ranking formula:

    =IF(data="",ROWS(data)
    

Here, before we run MMULT, we check if the current cell in "data" is blank. If so, we assign a rank value that equals the row count in data. This is done to force blank cells to the bottom of the list, where they can easily be excluded later as unique values are extracted (explained below).

### Counting unique values

To count unique values in the data, the formula in E5 is:

    =SUM(--(FREQUENCY(rank,rank)>0))-(blank>0)
    

Since the ranking formula above assigns a numeric rank to each value, we can use the [FREQUENCY function](https://exceljet.net/functions/frequency-function)
 with [SUM](https://exceljet.net/functions/sum-function)
 to count unique values. This formula is [explained in detail here](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)
. We then subtract 1 from the result if there are any empty cells in the data:

    -(blank>0)
    

where "blank" is the named range E8, and contains this formula:

    =COUNTBLANK(data)
    

Essentially, we reduce the unique count by one if there are blank cells in the data, since we don't include these in results. The unique count in cell E5 is named "unique" (for unique count), and is used by the INDEX and MATCH formula to filter out blank cells (described below).

### Extracting unique values

To extract unique values, G5 contains the following formula, copied down:

    =IF(ROWS($G$5:G5)>unique,"",INDEX(data,MATCH(MIN(IF(ISNA(MATCH(data,$G$4:G4,0)),rank)),rank,0)))
    

Before we run the INDEX and MATCH formula, we first check if the current row count in the extraction area is greater than the unique count the [named range](https://exceljet.net/glossary/named-range)
 "unique" (E5):

    =IF(ROWS($G$5:G5)>unique,"",
    

If, so, we are done extracting unique values and we return an [empty string](https://exceljet.net/glossary/empty-string)
 (""). If not, we run the extraction formula:

    INDEX(data,MATCH(MIN(IF(ISNA(MATCH(data,$G$4:G4,0)),rank)),rank,0))
    

Note there are two MATCH functions here, one inside the other. The inner MATCH uses an [expanding range](https://exceljet.net/glossary/expanding-reference)
 for an array and the named range "data" for the lookup value:

    MATCH(data,$G$4:G4,0)
    

Notice the expanding range begins on the "row above", row 4 in the example. The result from the inner MATCH is an array which, for each value in data, contains either a numeric position (the value has already been extracted) or the #N/A error (the value has not yet been extracted). We then use IF and ISNA to filter these results, and return the rank value for all values in "data" not yet extracted:

    IF(ISNA(results),rank))
    

This operation results in an array, which is fed into the MIN function in order to get the "minimum rank value" for data values not yet extracted. The MIN function returns this value to the outer MATCH as a lookup value and the [named range](https://exceljet.net/glossary/named-range)
 "rank" as the array:

    MATCH(min_not_extracted,rank)),rank,0)
    

Finally, MATCH returns the position of the lowest rank value to INDEX as a row number, and INDEX returns the data value in the current row of the extraction range.

### UNIQUE and SORT in Excel 365

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the [UNIQUE](https://exceljet.net/functions/unique-function)
 and [SORT](https://exceljet.net/functions/sort-function)
 functions provide a more elegant way to [list unique values](https://exceljet.net/formulas/unique-values)
 and [count unique values](https://exceljet.net/formulas/count-unique-values)
. These formulas can be adapted to [apply logical criteria](https://exceljet.net/formulas/unique-values-with-criteria)
, and SORT can be combined with UNIQUE.

Related formulas
----------------

[![Excel formula: Sort numbers ascending or descending](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20numbers%20ascending%20or%20descending.png "Excel formula: Sort numbers ascending or descending")](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)

### [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)

The SMALL function is meant to extract the "nth" smallest value from a set of data. The value for N is supplied as the second argument. To get the smallest value with SMALL, supply 1, to get the second smallest value, supply 2, and so on. =SMALL(data,1) // 1st smallest =SMALL(data,2) // 2nd...

[![Excel formula: Display sorted values with helper column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/display%20sorted%20values%20with%20helper%20column.png "Excel formula: Display sorted values with helper column")](https://exceljet.net/formulas/display-sorted-values-with-helper-column)

### [Display sorted values with helper column](https://exceljet.net/formulas/display-sorted-values-with-helper-column)

This formula relies on a helper column that already contains a sequential list of numbers to represent an established sort order. The numbers in the helper column are independent of the operation of this formula. As long as the sequence is continuous, it can represent an ascending or descending...

[![Excel formula: Random sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20sort%20formula.png "Excel formula: Random sort formula")](https://exceljet.net/formulas/random-sort-formula)

### [Random sort formula](https://exceljet.net/formulas/random-sort-formula)

This formula depends on two helper columns. The first helper column holds random values created with the RAND() function. The formula in C5, copied down is: =RAND() The RAND function generates a random value at each row. Note: RAND is a volatile function and will generate new values with each...

[![Excel formula: Basic numeric sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sort%20with%20rank%20in%20helper%20column2.png "Excel formula: Basic numeric sort formula")](https://exceljet.net/formulas/basic-numeric-sort-formula)

### [Basic numeric sort formula](https://exceljet.net/formulas/basic-numeric-sort-formula)

Note: this formula is the set-up for a formula that can extract and display data using a predefined sort order in a helper column. One example here . The core of this formula is the RANK function, which is used to generate a rank of sales values, where the highest number is ranked #1: =RANK(C5,...

[![Excel formula: Basic text sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20text%20sort%20formula.png "Excel formula: Basic text sort formula")](https://exceljet.net/formulas/basic-text-sort-formula)

### [Basic text sort formula](https://exceljet.net/formulas/basic-text-sort-formula)

This formula uses the "greater than or equal to" operator with text, something you might not have tried before. When Excel compares text, it decides which value is "greater" than another based on rules that follow the ASCII specification . Inside COUNTIF, the range argument is supplied as the named...

[![Excel formula: Sort text and numbers with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20mixed%20data%20with%20a%20formula.png "Excel formula: Sort text and numbers with formula")](https://exceljet.net/formulas/sort-text-and-numbers-with-formula)

### [Sort text and numbers with formula](https://exceljet.net/formulas/sort-text-and-numbers-with-formula)

This formula first generates a rank value using an expression based on COUNTIF: =COUNTIF(data,"<="...

[![Excel formula: Count unique numeric values in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20numeric%20values.png "Excel formula: Count unique numeric values in a range")](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)

### [Count unique numeric values in a range](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)

Note: Prior to Excel 365, Excel did not have a dedicated function to count unique values. This formula shows one way to count unique values, as long as they are numeric. If you have text values, or a mix of text and numbers, you'll need to use a more complicated formula . The Excel FREQUENCY...

Related functions
-----------------

[![Excel MMULT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mmult%20function.png "Excel MMULT function")](https://exceljet.net/functions/mmult-function)

### [MMULT Function](https://exceljet.net/functions/mmult-function)

The Excel MMULT function returns the matrix product of two arrays. The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. 

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20MATCH%20Function%20for%20exact%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

### [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

The MATCH function finds the relative position of an item in a list. MATCH can find exact matches or approximate matches. In this video, we'll look at how to use MATCH to find an exact match. The MATCH function takes three arguments: the lookup\_value, which is the value you're looking up, the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)
    
*   [Display sorted values with helper column](https://exceljet.net/formulas/display-sorted-values-with-helper-column)
    
*   [Random sort formula](https://exceljet.net/formulas/random-sort-formula)
    
*   [Basic numeric sort formula](https://exceljet.net/formulas/basic-numeric-sort-formula)
    
*   [Basic text sort formula](https://exceljet.net/formulas/basic-text-sort-formula)
    
*   [Sort text and numbers with formula](https://exceljet.net/formulas/sort-text-and-numbers-with-formula)
    
*   [Count unique numeric values in a range](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)
    

### Functions

*   [MMULT Function](https://exceljet.net/functions/mmult-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

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