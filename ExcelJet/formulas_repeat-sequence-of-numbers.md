# Repeat sequence of numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/repeat-sequence-of-numbers

---

[Skip to main content](https://exceljet.net/formulas/repeat-sequence-of-numbers#main-content)

[](https://exceljet.net/formulas/repeat-sequence-of-numbers#)

*   [Previous](https://exceljet.net/formulas/repeat-range-of-values)
    
*   [Next](https://exceljet.net/formulas/return-array-with-index-function)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Repeat sequence of numbers
==========================

by Dave Bruns · Updated 26 Jun 2024

Related functions 
------------------

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[MOD](https://exceljet.net/functions/mod-function)

![Excel formula: Repeat sequence of numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/repeat_sequence_of_numbers.png "Excel formula: Repeat sequence of numbers")

Summary
-------

To repeat a sequence of numbers, you can use a formula based on the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 and the [MOD function](https://exceljet.net/functions/mod-function)
. In the example shown, the formula in cell D5 looks like this:

    =MOD(SEQUENCE(B5*B8,,0),3)+1

This formula repeats the numbers {1,2,3} four times into the range D5:D16.

_Note: to repeat an arbitrary list of values like {"a","b","c"} [see this page](https://exceljet.net/formulas/repeat-range-of-values)
, which builds directly on the formula here._

Generic formula
---------------

    =MOD(SEQUENCE(n*x)-1,n)+1

Explanation 
------------

In this example, the goal is to repeat a sequence of numbers. This is a useful way to create repeating sequences of numbers by itself. In addition, this formula is a building block to the [more general formula here](https://exceljet.net/formulas/repeat-range-of-values)
, which can repeat ranges and arbitrary values that are not sequential numbers.

### Ingredients

The formulas on this page are based on two functions: the SEQUENCE function and the MOD function.

*   The [SEQUENCE function](https://exceljet.net/functions/sequence-function)
     is designed to create all kinds of numeric sequences. For a quick primer, watch this short video: [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    .
*   The [MOD function](https://exceljet.net/functions/mod-function)
     is a classic match formula that returns the remainder after division. MOD often shows up in problems that have a "repeating" element: [highlight every other row](https://exceljet.net/formulas/highlight-every-other-row)
    , [sum every nth row](https://exceljet.net/formulas/sum-every-nth-row)
    , and so on.

### Repeat sequence of numbers

To repeat a sequence of numbers, you can use a generalized version of a formula that looks like this, where "n" is the number of items being repeated and "x" is the number of times to repeat the items:

    =MOD(SEQUENCE(n*x)-1,n)+1

For example, to repeat the numbers {1,2,3} four times, n=3 and x=4, so we can use:

    =MOD(SEQUENCE(3*4,,0),3)+1

What's going on here?

In a nutshell, the SEQUENCE function creates an array of sequential numbers, and the MOD function converts these numbers into repeating numbers. Working from the inside out, SEQUENCE is configured like this:

    =SEQUENCE(3*4,,0)

*   rows - numbers (3) \* repeats (4) = 12
*   columns - left blank intentionally (defaults to 1)
*   start - given as 0 to start the sequence at zero instead of 1

Note that we get 12 for rows by multiplying the repeating numbers (3) by the number of repeats (4). Also note that the optional third argument, start, is given as zero to begin the sequence at 0 instead of 1. The evaluation of SEQUENCE works like this:

    =SEQUENCE(3*4,,0)
    =SEQUENCE(12,,0)
    ={0;1;2;3;4;5;6;7;8;9;10;11}

The final result is a zero-based sequence of 12 numbers. Next, the array returned by SEQUENCE is passed into the MOD function as the _number_ argument, with the divisor set to 3:

    =MOD({0;1;2;3;4;5;6;7;8;9;10;11},3)+1

The MOD function divides each number by 3 and returns the remainder after division. The result is an array of repeating numbers like this:

    ={0;1;2;0;1;2;0;1;2;0;1;2}+1

Finally, 1 is added to each number in the array to shift the numbers into their final form. The final result looks like this:

    {1;2;3;1;2;3;1;2;3;1;2;3}

Now, let's adjust the formula to repeat the numbers 1-6 two times. For this problem, n=6 and x=2, so the formula looks like this:

    =MOD(SEQUENCE(6*2,,0),6)+1

 As before, SEQUENCE generates an array of 12 numbers starting with zero, and MOD returns the remainder after dividing by 6.

    =MOD(SEQUENCE(6*2,,0),6)+1
    =MOD(SEQUENCE(12,,0),6)+1
    =MOD({0;1;2;3;4;5;6;7;8;9;10;11},6)+1
    ={0;1;2;3;4;5;0;1;2;3;4;5}+1
    {1;2;3;4;5;6;1;2;3;4;5;6}

In the final step, we add 1 to each number in the array to the repeating numbers from {0,1,2} to {1,2,3}. The workbook below shows how the formulas compare side-by-side:

![Repeating a sequence of numbers with MOD and SEQUENCE](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/repeat_sequence_of_numbers_example.png "Repeating a sequence of numbers with MOD and SEQUENCE")

To recap, the first formula repeats the numbers 1-3 four times, and the second formula repeats the numbers 1-6 twice.

### Repeat a sequence of numbers into columns

With a small adjustment, you can repeat a series of numbers in columns instead of rows. In the worksheet below, the formulas in cell B5 and cell B8 are:

    B5=MOD(SEQUENCE(,3*4,0),3)+1
    B8=MOD(SEQUENCE(,6*2,0),6)+1

![Repeating a sequence of numbers in columns with MOD and SEQUENCE](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/repeat_sequence_of_numbers_in_columns_example.png "Repeating a sequence of numbers in columns with MOD and SEQUENCE")

As above, the first formula repeats the numbers {1,2,3} four times, and the second formula repeats the numbers {1,2,3,4,5,6} two times. The only difference is that the n \* x calculation appears as the _columns_ argument in SEQUENCE instead of the _rows_ argument, which is left empty.

Related formulas
----------------

[![Excel formula: Repeat range of values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/repeat_range_of_values.png "Excel formula: Repeat range of values")](https://exceljet.net/formulas/repeat-range-of-values)

### [Repeat range of values](https://exceljet.net/formulas/repeat-range-of-values)

In this example, the goal is to repeat a range of values. This can be done in various ways in Excel, but I think the CHOOSEROWS/ CHOOSECOLS functions are the easiest way to retrieve values from the range for now. Both functions work natively with two-dimensional ranges and can accept a single array...

Related functions
-----------------

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Repeat range of values](https://exceljet.net/formulas/repeat-range-of-values)
    

### Functions

*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
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