# Random numbers without duplicates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/random-numbers-without-duplicates

---

[Skip to main content](https://exceljet.net/formulas/random-numbers-without-duplicates#main-content)

[](https://exceljet.net/formulas/random-numbers-without-duplicates#)

*   [Previous](https://exceljet.net/formulas/random-list-of-names)
    
*   [Next](https://exceljet.net/formulas/random-sort)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Random numbers without duplicates
=================================

by Dave Bruns · Updated 9 Apr 2024

Related functions 
------------------

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[SORTBY](https://exceljet.net/functions/sortby-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

[INDEX](https://exceljet.net/functions/index-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7096/download?token=4xZrzxX8)
 (20.58 KB)

![Excel formula: Random numbers without duplicates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/random%20numbers%20without%20duplicates.png "Excel formula: Random numbers without duplicates")

Summary
-------

To return random numbers without duplicates you can use a formula based on the [RANDARRAY](https://exceljet.net/functions/randarray-function)
, [SEQUENCE](https://exceljet.net/functions/sequence-function)
, [SORTBY](https://exceljet.net/functions/sortby-function)
, and [INDEX](https://exceljet.net/functions/index-function)
 functions. In the example shown, the formula in F5 is:

    =INDEX(SORTBY(SEQUENCE(C5,1,C4,C6),RANDARRAY(C5)),SEQUENCE(C7))
    

The result is a list of 12 random numbers greater than 10000, in multiples of 10. By design, the numbers are unique and contain no duplicates.

_Note: [RANDARRAY](https://exceljet.net/functions/randarray-function)
 and [RAND](https://exceljet.net/functions/rand-function)
 are [volatile functions](https://exceljet.net/glossary/volatile-function)
 and will recalculate with each worksheet change._

Explanation 
------------

In this example, the goal is to generate a list of random numbers without duplicates. This involves jumping through a few hoops because although the RANDARRAY function can easily generate a list of random integers, there is no guarantee that the numbers will be unique. In the explanation below, we'll look first at a simple option with the RANDARRAY function, then at a more complete solution based on the SEQUENCE function.

### Background study

*   [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
     - 3 min video
*   [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)
     - 3 min video

### RANDARRAY option

The [RANDARRAY function](https://exceljet.net/functions/randarray-function)
 makes it easy to generate a list of random integers. For example, to generate 12 random numbers between 1 and 100, you can use RANDARRAY like this:

    =RANDARRAY(12,1,1,100,TRUE)
    

The _rows_ [argument](https://exceljet.net/glossary/function-argument)
 sets how many numbers are returned, _columns_ is 1, _start_ is 1, _end_ is 100, and _integer_ is set to TRUE. This formula works fine. However, if you enter the formula and [press F9](https://exceljet.net/shortcuts/calculate-worksheets)
 a few times, you will likely see some duplicate numbers because there is no guarantee that the numbers are unique.

By increasing the range of numbers generated, we can reduce the possibility of duplicates substantially. For example, this formula returns 12 random numbers between 10000 and 50000:

    =RANDARRAY(12,1,10000,50000,TRUE)
    

Although there is still a possibility of duplicates, the chance is much lower since there are 40,002 possible numbers. To ensure that there are no duplicates, we can wrap RANDARRAY inside the [UNIQUE function](https://exceljet.net/videos/the-unique-function)
 like this:

    =UNIQUE(RANDARRAY(12,1,10000,50000,TRUE))
    

The formula above works well if a specific number of results is _not required_. However, because the UNIQUE function will _remove_ duplicates if they exist, the final count of numbers returned will change. To work around this problem, and ensure a fixed number of unique random numbers, we can take a different approach with the SEQUENCE function as described below.

### Random sort

Another approach is to use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 to generate a unique list of numbers, then use [SORTBY](https://exceljet.net/functions/sortby-function)
 and [RANDARRAY](https://exceljet.net/functions/randarray-function)
 to sort the list randomly. For example, to return 15 numbers sorted randomly, you can use a formula like this:

    =SORTBY(SEQUENCE(15),RANDARRAY(15))
    

SEQUENCE returns an array of numbers between 1-15, RANDARRAY returns an array of 15 decimal values, and the SORTBY function sorts the output from SEQUENCE using the output from RANDARRAY. The result is a list of the 15 numbers between 1-15, sorted randomly.

### Random sort and extract

An alternative to the simple approach described above is to create a list of unique numbers with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
, sort the list randomly, and then _extract_ a portion of the list. This guarantees a specific number of unique values across a large range of possibilities. This is the approach used in the worksheet shown above, where the formula in cell F5 is:

    =INDEX(SORTBY(SEQUENCE(C5,1,C4,C6),RANDARRAY(C5)),SEQUENCE(C7))
    

Replacing the cell references with their values, we have:

    =INDEX(SORTBY(SEQUENCE(1000,1,10000,10),RANDARRAY(1000)),SEQUENCE(12))
    

Working from the inside out, the core of the formula is this:

    SORTBY(SEQUENCE(1000,1,10000,10),RANDARRAY(1000))
    

At a high level, the [SORTBY function](https://exceljet.net/functions/sortby-function)
 is used to sort the output from SEQUENCE randomly. The [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 is configured to generate 1000 numbers starting at 10000. The _step_ argument is given as 10 to return numbers that are multiples of 10. The result from SEQUENCE is an [array](https://exceljet.net/glossary/array)
 that contains 1000 numbers. The first 10 numbers in the array look like this:

    {10000;10010;10020;10030;10040;10050;10060;10070;10080;10090;...}
    

These numbers are returned directly to SORTBY as the _array_ argument.

The [RANDARRAY function](https://exceljet.net/functions/randarray-function)
 is set to output 1000 numbers. By default, RANDARRAY will return an array of long decimals. The first 10 numbers in the array will look something like this:

    {0.568145559543193;0.0442765690172342;0.682220112357301;0.293859840996845;0.0875380500249507;0.0872080540305316;0.384740824003848;0.8250435788655;0.698609517138334;0.844906019655289;...}
    

These numbers are provided to [SORTBY](https://exceljet.net/functions/sortby-function)
 as the _by\_array1_ argument. With the result from SEQUENCE as _array_, and the result from RANDARRAY as _by\_array1_, SORTBY sorts all 1000 numbers randomly and returns the sorted array to the [INDEX function](https://exceljet.net/functions/index-function)
. If we refer to this randomly sorted array  as "random\_array", we can simplify and rewrite the original formula like this:

    =INDEX(random_array,SEQUENCE(C7))
    

Here, _random\_array_ is delivered to INDEX as the _array_ argument. The SEQUENCE function creates an array with the numbers 1-12, and returns this array to INDEX as the _row\_num_ argument:

    =INDEX(random_array,{1;2;3;4;5;6;7;8;9;10;11;12})
    

With these inputs, INDEX returns the first 12 rows from the randomly sorted array as a final result. The numbers are guaranteed to be unique because the original array created by SEQUENCE contains no duplicates.

### Random names

The approach described above can be applied to other related problems. For example, once you have a list of random numbers without duplicates, you can use those numbers with the [INDEX function](https://exceljet.net/functions/index-function)
 to create a [random list of names without duplicates](https://exceljet.net/formulas/random-list-of-names)
.

### Legacy Excel

[Dynamic array formulas are a new feature in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. If you have a version of Excel without SEQUENCE, SORTBY, and RANDARRAY, you can take a more manual approach. One method is to enter the core set of numbers to choose from in one column, and use the [RAND function](https://exceljet.net/functions/rand-function)
 to assign random decimal values to each number in another column. Then you can use an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
 with the LARGE function to extract random numbers according to their numeric rank. The screen below shows the basic idea:

![Random numbers without duplicates by numeric rank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/random%20numbers%20without%20duplicates%20by%20rank.png?itok=4UvSVsfs "Random numbers without duplicates by numeric rank")

The formula in F5, copied down, is:

    =INDEX(number,MATCH(LARGE(rand,E5),rand,0))
    

where **number** (B5:B104) and **rand** (C5:C104) are [named ranges](https://exceljet.net/glossary/named-range)
. The [LARGE function](https://exceljet.net/functions/large-function)
 is used to get the nth largest random decimal number in C5:C104, where **n** comes from column E. LARGE returns this value to the [MATCH function](https://exceljet.net/functions/match-function)
 as _lookup\_value_, which locates the position of the value in the random decimal values. MATCH returns this position to the [INDEX function](https://exceljet.net/functions/index-function)
, and INDEX returns the number at that position in B5:B104. The final result is 10 random numbers between 1-100 in F5:F14 without duplicates.

Related formulas
----------------

[![Excel formula: Random list of names](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random-list-of-names.png "Excel formula: Random list of names")](https://exceljet.net/formulas/random-list-of-names)

### [Random list of names](https://exceljet.net/formulas/random-list-of-names)

In this example, the goal is to create a list of 10 random names from a larger list of 100 names. In other words, we want to select a random subset of names from a larger list. The names to select from are in column B, starting in row 5. The formula should handle any number of names in the input...

[![Excel formula: Sort by custom list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20custom%20list.png "Excel formula: Sort by custom list")](https://exceljet.net/formulas/sort-by-custom-list)

### [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)

In this example, we are sorting a table with 10 rows and 3 columns. In the range J5:J7 (the named range custom ), the colors "red", "blue", and "green" are listed in the desired sort order. The goal is to sort the table using values in the Group column in this same custom order. The SORTBY function...

[![Excel formula: Random sort](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random_sort.png "Excel formula: Random sort")](https://exceljet.net/formulas/random-sort)

### [Random sort](https://exceljet.net/formulas/random-sort)

In this example, the goal is to perform a random sort of the data in B5:B16 with a formula. This can be done with the SORTBY function and the RANDARRAY function . SORTBY function The SORTBY function sorts provided values by one or more "sort by" arrays. The sort by arrays make it possible to sort...

[![Excel formula: Random text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20text%20values.png "Excel formula: Random text values")](https://exceljet.net/formulas/random-text-values)

### [Random text values](https://exceljet.net/formulas/random-text-values)

The CHOOSE function provides the framework for this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are using four values:...

Related functions
-----------------

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel RANDARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_randarray_function.png "Excel RANDARRAY function")](https://exceljet.net/functions/randarray-function)

### [RANDARRAY Function](https://exceljet.net/functions/randarray-function)

The Excel RANDARRAY function generates an array of random numbers between two values. The size or the array is specified by _rows_ and _columns_ arguments. The generated values can be either decimals or whole numbers.

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

*   [Random list of names](https://exceljet.net/formulas/random-list-of-names)
    
*   [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)
    
*   [Random sort](https://exceljet.net/formulas/random-sort)
    
*   [Random text values](https://exceljet.net/formulas/random-text-values)
    

### Functions

*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

### Training

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