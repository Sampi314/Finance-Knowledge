# Random list of names - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/random-list-of-names

---

[Skip to main content](https://exceljet.net/formulas/random-list-of-names#main-content)

[](https://exceljet.net/formulas/random-list-of-names#)

*   [Previous](https://exceljet.net/formulas/minimum-value-if-unique)
    
*   [Next](https://exceljet.net/formulas/random-numbers-without-duplicates)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Random list of names
====================

by Dave Bruns · Updated 20 Dec 2025

Related functions 
------------------

[TAKE](https://exceljet.net/functions/take-function)

[SORTBY](https://exceljet.net/functions/sortby-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

[ROWS](https://exceljet.net/functions/rows-function)

[INDEX](https://exceljet.net/functions/index-function)

[CHOOSEROWS](https://exceljet.net/functions/chooserows-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9430/download?token=47qH0WT1)
 (23.98 KB)

![Excel formula: Random list of names](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/random-list-of-names.png "Excel formula: Random list of names")

Summary
-------

To create a random list of names, you can use a formula based on the [TAKE function](https://exceljet.net/functions/take-function)
, [SORTBY function](https://exceljet.net/functions/sortby-function)
, and the [RANDARRAY function](https://exceljet.net/functions/randarray-function)
. In the example shown, the formula in D5 is:

    =TAKE(SORTBY(B5:B104,RANDARRAY(ROWS(B5:B104))),10)
    

The result is a random list of 10 names from the list of 100 names in column B.

Generic formula
---------------

    =TAKE(SORTBY(names,RANDARRAY(ROWS(names))),n)

Explanation 
------------

In this example, the goal is to create a list of 10 random names from a larger list of 100 names. In other words, we want to select a _random subset_ of names from a larger list. The names to select from are in column B, starting in row 5. The formula should handle any number of names in the input list and handle the number of names to select as a variable.

This is an interesting problem in Excel. Although there are several functions dedicated to generating random numbers, including [RAND](https://exceljet.net/functions/rand-function)
, [RANDARRAY](https://exceljet.net/functions/randarray-function)
, and [RANDBETWEEN](https://exceljet.net/functions/randbetween-function)
, it isn't obvious how you would use the output from these functions to generate a random list of names.

This article looks at two formula options to solve this problem. The first option involves sorting all 100 names in a random order, then selecting the first 10 names from the sorted list. The second option generates a list of 10 random integers between 1 and 100, then uses these numbers as indices to select the names in the original list. To start off, let's look at how we can simply sort the names in a random order.

### Table of contents

*   [Sorting names in a random order](https://exceljet.net/formulas/random-list-of-names#sorting-names-in-a-random-order)
    
*   [Option 1: TAKE with SORTBY and RANDARRAY](https://exceljet.net/formulas/random-list-of-names#option-1-take-with-sortby-and-randarray)
    
*   [Option 2: INDEX with RANDARRAY](https://exceljet.net/formulas/random-list-of-names#option-2-index-with-randarray)
    
*   [Sampling with and without replacement](https://exceljet.net/formulas/random-list-of-names#sampling-with-and-without-replacement)
    
*   [Summary and recommendation](https://exceljet.net/formulas/random-list-of-names#summary-and-recommendation)
    

### Sorting names in a random order

To _sort_ the names in a random order, we can use the [SORTBY function](https://exceljet.net/functions/sortby-function)
 and the [RANDARRAY function](https://exceljet.net/functions/randarray-function)
. You can see how this works in the worksheet below, where the formula in D5 is:

    =SORTBY(B5:B104,RANDARRAY(ROWS(B5:B104)))
    

![A general purpose formula to sort all names in random order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/random-list-of-names-randomly-sorted-names.png "A general purpose formula to sort all names in random order")

_This formula sorts all 100 names in B4:B104 in random order._

Working from the inside out, the [ROWS function](https://exceljet.net/functions/rows-function)
 is used to get the number of rows in the range B5:B104 (100), which is returned to the [RANDARRAY function](https://exceljet.net/functions/randarray-function)
 as the _rows_ argument. This determines the number of random numbers to create:

    =RANDARRAY(ROWS(B5:B104))
    =RANDARRAY(100) // generates 100 random numbers
    

Next, the RANDARRAY function creates an array of 100 random numbers between 0 and 1. These are long decimals that look something like this:

    {0.909292521,0.69722143,0.839223233,0.837319958,0.097171021,...}
    

In the screenshot below, you can see a full set of 100 random numbers in column D. These are the numbers that will be used to sort the names in a random order.

![Example of the random numbers created by RANDARRAY](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/random-list-of-names-random-numbers-only.png "Example of the random numbers created by RANDARRAY")

_This formula generates 100 random decimal numbers, one for each name in B5:B104._

Next, the array of random numbers created by the RANDARRAY function is returned to the SORTBY function as the _sort\_by_ argument:

    =SORTBY(B5:B104,{0.909292521,0.69722143,0.839223233,0.837319958,0.097171021,...})
    

The SORTBY function then sorts the input list by the random array of numbers. The result is a list of names in a random order.

This formula is generally useful to sort _any range of values_ in a random order. Next, let's look at how we can use it to generate 10 random names from the list of 100 names.

> Note: the RANDARRAY function is a [volatile function](https://exceljet.net/glossary/volatile-function)
>  and will recalculate every time the worksheet is changed, causing values to be resorted. To stop values from sorting automatically, you can copy the formulas, then use Paste Special > Values to convert formulas to static values. Another option is to adapt the formula to use a this [seeded random number generator](https://exceljet.net/articles/seeded-random-number-generator-in-excel)
> . This involves replacing RANDARRAY with the custom RAND\_SEQUENCE function explained in the article.

### Option 1: TAKE with SORTBY and RANDARRAY

Option 1 involves selecting the first 10 names from a randomly sorted list. To sort the list in a random order, we use the SORTBY function with the RANDARRAY function as explained in the previous section. Then, we use the TAKE function to select the first 10 names from the sorted list. You can see this approach in the worksheet below, where the formula in D5 is:

    =TAKE(SORTBY(B5:B104,RANDARRAY(ROWS(B5:B104))),10)
    

![Creating a random list of names with TAKE, SORTBY, and RANDARRAY](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/random-list-of-names-with-take-sortby-and-randarray.png "Creating a random list of names with TAKE, SORTBY, and RANDARRAY")

_This formula sorts all 100 names in B4:B104 in random order, then uses the TAKE function to fetch the first 10 names in the sorted list._

Working from the inside out, we use SORTBY with RANDARRAY to sort the names in a random order as [explained above](https://exceljet.net/formulas/random-list-of-names#sorting-names-in-a-random-order)
:

    =SORTBY(B5:B104,RANDARRAY(ROWS(B5:B104))) // randomly sort all names
    

The result from SORTBY is a list of all 100 names in a randomly sorted order.

Finally, we need to retrieve 10 names. Because we already have names in a random order, we can simply ask the [TAKE function](https://exceljet.net/functions/take-function)
 to fetch the first 10 names in the sorted list:

    =TAKE(randomly_sorted_names,10)
    

Because the input list was sorted randomly, the result from TAKE is a random list of 10 names. I like this approach because it is simple and a great example of how [new functions](https://exceljet.net/new-excel-functions)
 like TAKE can be useful. Let's look at another approach to this problem.

### Option 2: INDEX with RANDARRAY

Another way to solve this problem is to generate an array of random integers and then use the [INDEX function](https://exceljet.net/functions/index-function)
 to select the names at these positions, without sorting the names first. You can see this approach in the worksheet below, where the formula in D5 looks like this:

    =INDEX(B5:B104,RANDARRAY(10,1,1,ROWS(B5:B104),1))
    

![Creating a random list of names with INDEX and RANDARRAY](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/random-list-of-names-with-index-and-randarray.png "Creating a random list of names with INDEX and RANDARRAY")

_This formula generates 10 random integers between 1 and 100, then uses INDEX to select names at those positions in the range B5:B104._

As before, the [ROWS function](https://exceljet.net/functions/rows-function)
 is used to count the names in the input. However, in this case, the output from ROWS is delivered to RANDARRAY as the _max_ argument, which determines the maximum value for the random numbers to generate.

    =RANDARRAY(10,1,1,ROWS(B5:B104),1)
    

The complete configuration of [RANDARRAY](https://exceljet.net/functions/randarray-function)
 is as follows:

*   rows: 10
*   columns: 1
*   min: 1
*   max: 100 (from `ROWS(B5:B104)`)
*   integer: TRUE

The result from RANDARRAY is an array of 10 random integers between 1 and 100, like this:

    {95;81;6;90;88;82;85;5;82;46}
    

This array is returned directly to the INDEX function as the row argument:

    =INDEX(B5:B104,{95;81;6;90;88;82;85;5;82;46})
    

Because we give INDEX an _array_ of 10 row numbers, it will return an _array_ of 10 results, each corresponding to a name at the given position:

    {"Darlene";"Larry";"Bernice";"Elizabeth";"Jose";"Donald";"Jennifer";"Damian";"Angie";"Homer"}
    

The final result is a random list of 10 names extracted from the list of 100 names in B5:B104. This approach is more efficient than Option 1 because it does not need to sort the entire list of 100 names. Instead, it creates only as many random integers as we need, then uses those numbers directly to extract names in that position from the master list. However, it comes with a caveat: there is no guarantee that the random integers created by RANDARRAY will be unique, and duplicate integers will result in duplicate names.

> Note we are using INDEX and not TAKE to extract names in option 2. This is because we need to extract _specific rows_ from the list, not the first 10 rows. Another option would be to use the [CHOOSEROWS function](https://exceljet.net/functions/chooserows-function)
>  to extract the names. Both INDEX and CHOOSEROWS will produce the same result.

### Sampling with and without replacement

The two options above represent different approaches to random sampling. In statistics, there's an important distinction between _sampling with replacement_ and _sampling without replacement_:

*   **Sampling with replacement** means each time you pick an item, it goes back into the pool before the next draw. The same item can appear multiple times in your sample. This is like drawing names from a hat and returning each name before drawing again.
*   **Sampling without replacement** means once an item is picked, it's removed from the pool and can't be selected again. Each item in your sample will be unique.

**Option 1** (TAKE with SORTBY) implements sampling _without replacement_. By sorting the entire list randomly and taking the first 10 names, we guarantee that every selected name is unique. This is what most people expect when they ask for "10 random names from a list."

**Option 2** (INDEX with RANDARRAY) implements sampling _with replacement_ by default. Because RANDARRAY generates random integers independently, the same number can appear more than once, resulting in duplicate names. Each draw is independent, so there's no guarantee of uniqueness unless you add additional logic to prevent duplicates.

### Summary and recommendation

This article presents two formula options to create a random list of names. [Option 1](https://exceljet.net/formulas/random-list-of-names#option-1-take-with-sortby-and-randarray)
 uses TAKE with SORTBY to select names from a randomly sorted list, using _sampling without replacement_, which guarantees unique names. [Option 2](https://exceljet.net/formulas/random-list-of-names#option-2-index-with-randarray)
 uses INDEX with RANDARRAY to directly extract names by position, using _sampling with replacement_, which may produce duplicates.

I recommend Option 1 for most cases because it delivers the expected behavior: a random subset with no duplicates. It also performs well—I tested it on 100,000 random text strings without noticeable performance issues. Use Option 2 only if you specifically need sampling with replacement or are working with extremely large datasets where performance becomes critical.

Related formulas
----------------

[![Excel formula: Sort by custom list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20custom%20list.png "Excel formula: Sort by custom list")](https://exceljet.net/formulas/sort-by-custom-list)

### [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)

In this example, we are sorting a table with 10 rows and 3 columns. In the range J5:J7 (the named range custom ), the colors "red", "blue", and "green" are listed in the desired sort order. The goal is to sort the table using values in the Group column in this same custom order. The SORTBY function...

[![Excel formula: Random sort](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random_sort.png "Excel formula: Random sort")](https://exceljet.net/formulas/random-sort)

### [Random sort](https://exceljet.net/formulas/random-sort)

In this example, the goal is to perform a random sort of the data in B5:B16 with a formula. This can be done with the SORTBY function and the RANDARRAY function . SORTBY function The SORTBY function sorts provided values by one or more "sort by" arrays. The sort by arrays make it possible to sort...

[![Excel formula: Random numbers without duplicates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20numbers%20without%20duplicates.png "Excel formula: Random numbers without duplicates")](https://exceljet.net/formulas/random-numbers-without-duplicates)

### [Random numbers without duplicates](https://exceljet.net/formulas/random-numbers-without-duplicates)

In this example, the goal is to generate a list of random numbers without duplicates. This involves jumping through a few hoops because although the RANDARRAY function can easily generate a list of random integers, there is no guarantee that the numbers will be unique. In the explanation below, we'...

[![Excel formula: Random text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20text%20values.png "Excel formula: Random text values")](https://exceljet.net/formulas/random-text-values)

### [Random text values](https://exceljet.net/formulas/random-text-values)

The CHOOSE function provides the framework for this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are using four values:...

Related functions
-----------------

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel RANDARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_randarray_function.png "Excel RANDARRAY function")](https://exceljet.net/functions/randarray-function)

### [RANDARRAY Function](https://exceljet.net/functions/randarray-function)

The Excel RANDARRAY function generates an array of random numbers between two values. The size or the array is specified by _rows_ and _columns_ arguments. The generated values can be either decimals or whole numbers.

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel CHOOSEROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20chooserows%20function.png "Excel CHOOSEROWS function")](https://exceljet.net/functions/chooserows-function)

### [CHOOSEROWS Function](https://exceljet.net/functions/chooserows-function)

The Excel CHOOSEROWS function returns specific rows from an array or range. The rows to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a row in the given array.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/New%20dynamic%20array%20functions%20in%20Excel-Play.png)](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

### [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

In this video, we'll quickly review new Dynamic Array functions in Excel. With the introduction of dynamic array formulas, Excel includes 6 brand new functions that directly leverage dynamic array behavior. Each of these functions is covered in more detail later in the course, so this is just a...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)
    
*   [Random sort](https://exceljet.net/formulas/random-sort)
    
*   [Random numbers without duplicates](https://exceljet.net/formulas/random-numbers-without-duplicates)
    
*   [Random text values](https://exceljet.net/formulas/random-text-values)
    

### Functions

*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [CHOOSEROWS Function](https://exceljet.net/functions/chooserows-function)
    

### Videos

*   [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
    

### Articles

*   [Seeded Random Number Generator in Excel](https://exceljet.net/articles/seeded-random-number-generator-in-excel)
    
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