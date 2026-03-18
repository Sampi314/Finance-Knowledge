# Repeat range of values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/repeat-range-of-values

---

[Skip to main content](https://exceljet.net/formulas/repeat-range-of-values#main-content)

[](https://exceljet.net/formulas/repeat-range-of-values#)

*   [Previous](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)
    
*   [Next](https://exceljet.net/formulas/repeat-sequence-of-numbers)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Repeat range of values
======================

by Dave Bruns · Updated 30 Jun 2024

Related functions 
------------------

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[MOD](https://exceljet.net/functions/mod-function)

[CHOOSEROWS](https://exceljet.net/functions/chooserows-function)

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

![Excel formula: Repeat range of values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/repeat_range_of_values.png "Excel formula: Repeat range of values")

Summary
-------

To repeat a range of values, you can use a formula based on the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 and the [CHOOSEROWS function](https://exceljet.net/functions/chooserows-function)
. In the example shown, the formula in cell D5 looks like this:

    =CHOOSEROWS(B8:B10,MOD(SEQUENCE(3*B5,,0),3)+1)

This formula repeats the values in B8:B10 a total of 4 times.

Generic formula
---------------

    =CHOOSEROWS(range,MOD(SEQUENCE(n*x)-1,n)+1)

Explanation 
------------

In this example, the goal is to repeat a range of values. This can be done in various ways in Excel, but I think the CHOOSEROWS/ CHOOSECOLS functions are the easiest way to retrieve values from the range for now. Both functions work natively with two-dimensional ranges and can accept a single array of numeric index numbers. The formulas below work in two steps:

1.  Generate a repeating list of numeric index numbers.
2.  Use the index numbers to retrieve and repeat values from a range.

Step 1 is based on the formula [explained in detail here](https://exceljet.net/formulas/repeat-sequence-of-numbers)
. Step 2 is based on either the CHOOSEROWS function (to repeat values by row) or the CHOOSECOLS function (to repeat values by column).

### Generic formula

The generalized formula for repeating a range into rows looks like this:

    =CHOOSEROWS(range,MOD(SEQUENCE(n*x)-1,n)+1)

*   _range_ - the range to repeat, or an array constant like {"a";"b";"c"}
*   _n_ - the number of rows to repeat
*   _x_ - the number of times to repeat

### Worksheet formula

In the example shown above, we are repeating 3 values {"dog";"cat";"fish"} 4 times into 12 rows with this formula in cell D5:

    =CHOOSEROWS(B8:B10,MOD(SEQUENCE(3*B5,,0),3)+1)

### Step 1: Generate repeating index numbers

The core idea of this approach is to create a repeating sequence of numbers that can be used as indices to retrieve values from a range or array. This is done with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 and the [MOD function](https://exceljet.net/functions/mod-function)
 here:

    MOD(SEQUENCE(3*B5,,0),3)+1

This code creates a single array of repeating numbers. First, SEQUENCE creates an array of 12 sequential numbers starting with zero:

    =SEQUENCE(3*4,,0)
    =SEQUENCE(12,,0)
    ={0;1;2;3;4;5;6;7;8;9;10;11}

Next, the MOD function converts the numbers into a repeating sequence:

    =MOD({0;1;2;3;4;5;6;7;8;9;10;11},3)+1
    ={0;1;2;0;1;2;0;1;2;0;1;2}+1
    ={1;2;3;1;2;3;1;2;3;1;2;3}

The final result is an array like this:

    {1;2;3;1;2;3;1;2;3;1;2;3}

Notice that we have repeated the values {1;2;3} four times.

_Note: For a more detailed explanation of this part of the formula, which can used standalone, see: [Repeat sequence of numbers](https://exceljet.net/formulas/repeat-sequence-of-numbers)
._

### Step 2: Repeat the values

Now that we have an array of repeating numbers, the next step is to use these numbers to extract values in the range B8:B10. To do that, we use the [CHOOSEROWS function](https://exceljet.net/functions/chooserows-function)
, which is designed to return specific rows from an array or range. The array from the SEQUENCE and MOD operation described above is delivered directly to CHOOSEROWS as _row\_num1_:

    =CHOOSEROWS(B8:B10,{1;2;3;1;2;3;1;2;3;1;2;3})

Although the signature for CHOOSEROWS suggests that row numbers must be provided separately, an array constant works just fine. The result from CHOOSEROWS is an array with the first three rows of the range B5:B10 repeated 4 times:

    {"dog";"cat";"fish";"dog";"cat";"fish";"dog";"cat";"fish";"dog";"cat";"fish"}

This array lands in cell D5 and spills into the range D5:D16.

### Example with a 2D range

Because we are using the CHOOSEROWS function, we have native support for two-dimensional ranges. In the worksheet below, we repeat the range B8:C11 3 times with this formula in cell E5:

    =CHOOSEROWS(B8:C11,MOD(SEQUENCE(4*B5,,0),4)+1)

![Example of repeating a two-dimensional range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/repeat_2d_range_of_values_example.png "Example of repeating a two-dimensional range")

### Repeat range into columns

By switching to CHOOSECOLS, we can repeat a range into columns instead of rows. The [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
 is designed to return specific _columns_ from a range. The generic version of the formula looks like this:

    =CHOOSECOLS(range,MOD(SEQUENCE(n*x)-1,n)+1)

  In the worksheet below, we use this formula to repeat the range B8:B11 5 times by column:

![Example of repeating a range into columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/repeat_range_of_values_into_columns_example.png "Example of repeating a range into columns")

This formula's operation is the same as the original above, except that we repeat values by column.

Related formulas
----------------

[![Excel formula: Repeat sequence of numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/repeat_sequence_of_numbers.png "Excel formula: Repeat sequence of numbers")](https://exceljet.net/formulas/repeat-sequence-of-numbers)

### [Repeat sequence of numbers](https://exceljet.net/formulas/repeat-sequence-of-numbers)

In this example, the goal is to repeat a sequence of numbers. This is a useful way to create repeating sequences of numbers by itself. In addition, this formula is a building block to the more general formula here , which can repeat ranges and arbitrary values that are not sequential numbers...

[![Excel formula: Repeat fixed value every 3 months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/repeat%20value%20every%20n%20months.png "Excel formula: Repeat fixed value every 3 months")](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)

### [Repeat fixed value every 3 months](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)

The first thing this formula does is check the date in column B against the start date: =IF(B4>=start If the date is not greater than the start date, the formula returns zero. If the date is greater than or equal to the start date, the IF function runs this snippet: (MOD(DATEDIF(start,B4,"m")+n,...

Related functions
-----------------

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

[![Excel CHOOSEROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20chooserows%20function.png "Excel CHOOSEROWS function")](https://exceljet.net/functions/chooserows-function)

### [CHOOSEROWS Function](https://exceljet.net/functions/chooserows-function)

The Excel CHOOSEROWS function returns specific rows from an array or range. The rows to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a row in the given array.

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

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

*   [Repeat sequence of numbers](https://exceljet.net/formulas/repeat-sequence-of-numbers)
    
*   [Repeat fixed value every 3 months](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)
    

### Functions

*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [CHOOSEROWS Function](https://exceljet.net/functions/chooserows-function)
    
*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    

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