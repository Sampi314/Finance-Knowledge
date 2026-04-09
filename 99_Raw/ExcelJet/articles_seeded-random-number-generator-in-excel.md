# Seeded Random Number Generator in Excel | Exceljet

**Source:** https://exceljet.net/articles/seeded-random-number-generator-in-excel

---

[Skip to main content](https://exceljet.net/articles/seeded-random-number-generator-in-excel#main-content)

[](https://exceljet.net/articles/seeded-random-number-generator-in-excel#)

*   [Previous](https://exceljet.net/articles/how-to-replace-excels-datedif-function)
    
*   [Next](https://exceljet.net/articles/modeling-the-4-percent-retirement-rule-in-excel)
    

Seeded Random Number Generator in Excel
=======================================

by Kurt Bruns · Updated 16 Dec 2025

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/9450/download?token=baxD3f5q)
 (47.1 KB)

![Building a seeded random number generator in Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/seeded_random_number_generator_artwork.jpg "Building a seeded random number generator in Excel")

Summary
-------

How to keep random numbers from changing in Excel? Excel's random functions like RAND and RANDARRAY recalculate every time you edit your worksheet, making it impossible to maintain stable random results. This article shows you how to build a seeded random number generator using Excel's LAMBDA function, allowing you to generate reproducible random numbers that only change when you want them to. Perfect for scenarios like randomly assigning students to groups or any situation where you need consistent, repeatable random results.

If you've generated random numbers in Excel before, you'll know there's a limitation where, every time you make a change to the spreadsheet, functions like [RAND](https://exceljet.net/functions/rand-function)
, [RANDBETWEEN](https://exceljet.net/functions/randbetween-function)
, and [RANDARRAY](https://exceljet.net/functions/randarray-function)
 recalculate and return different values. In Excel lingo, functions with this behavior are called [_volatile functions_](https://exceljet.net/glossary/volatile-function)
.

This volatility can be frustrating when you need random results to stay put. Fortunately, there's a solution: a seeded random number generator. In this article, we'll show you how to build one using Excel's LAMBDA function, giving you full control over when your random numbers change. We'll start by looking at the problem in detail, then walk through building a custom function step by step.

### Table of Contents

*   [The problem with random formulas](https://exceljet.net/articles/seeded-random-number-generator-in-excel#the-problem-with-random-formulas)
    
*   [What is a seeded random number generator?](https://exceljet.net/articles/seeded-random-number-generator-in-excel#what-is-a-seeded-random-number-generator)
    
*   [Benefits of seeded random numbers](https://exceljet.net/articles/seeded-random-number-generator-in-excel#benefits-of-seeded-random-numbers)
    
*   [Our approach](https://exceljet.net/articles/seeded-random-number-generator-in-excel#our-approach)
    
*   [The RNG algorithm](https://exceljet.net/articles/seeded-random-number-generator-in-excel#the-rng-algorithm)
    
*   [Implementing the LAMBDA function](https://exceljet.net/articles/seeded-random-number-generator-in-excel#implementing-the-lambda-function)
    
*   [Improving the formula](https://exceljet.net/articles/seeded-random-number-generator-in-excel#improving-the-formula)
    
*   [Creating a custom HASH function](https://exceljet.net/articles/seeded-random-number-generator-in-excel#creating-a-custom-hash-function)
    
*   [Sorting students with RAND\_SEQUENCE](https://exceljet.net/articles/seeded-random-number-generator-in-excel#sorting-students-with-rand_sequence)
    
*   [Using RAND\_SEQUENCE in your workbooks](https://exceljet.net/articles/seeded-random-number-generator-in-excel#using-rand_sequence-in-your-workbooks)
    

### The problem with random formulas

To illustrate the problem with random formulas in Excel clearly, let's look at an example. Imagine a teacher wants to randomly assign students to groups every month. One simple way to do this is to set up the groups in one column and, in the next column, sort the students randomly. You can see this approach in the workbook below, where the original list of students is in column B, the list of groups is in column D, and the randomly sorted students are in column E. The formula in cell E5 looks like this:

    =SORTBY(B5:B13,RANDARRAY(ROWS(B5:B13)))
    

![A simple formula to randomly sort students into groups](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/random_number_generator_the_problem.png "A simple formula to randomly sort students into groups")

_See_ [_Random list of names_](https://exceljet.net/formulas/random-list-of-names)
 _for details about how this formula works._

At first glance, everything looks great. We have successfully placed 9 students into 3 groups using a random sort. However, the problem is that RANDARRAY is a volatile function, which means it will recalculate each time the worksheet changes. You can see how this works in the screens below, where three unrelated edits cause the formula to return new results:

![The random sort changes when an unrelated edit is made in cell G5](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/random_number_generator_the_problem_edit1.png "The random sort changes when an unrelated edit is made in cell G5")

![The random sort changes when an unrelated edit is made in cell G6](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/random_number_generator_the_problem_edit2.png "The random sort changes when an unrelated edit is made in cell G6")

![The random sort changes when an unrelated edit is made in cell G7](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/random_number_generator_the_problem_edit3.png "The random sort changes when an unrelated edit is made in cell G7")

_Every change to the worksheet creates new random groups!_

The classic solution to this problem is to copy the randomly sorted students to the clipboard and use Paste Special > Values to create static values that won't change. However, this is an annoying workaround, since it requires several manual steps, and it also destroys the formulas used to generate random results in the first place. What we really want is a way to generate new random numbers _on demand_.

This is not a new problem. For most programming languages, there exists a tried and true solution used when generating random numbers called _seed values_. It works like this: when you initialize a random number generator with a seed value, you get reproducible random numbers _based on the seed value_. The key idea here is **reproducible**, meaning two separate calls with the same seed value will produce the _same random numbers_. The solution is a Seeded Random Number Generator, sometimes abbreviated to "RNG".

### What is a seeded random number generator?

A seeded random number generator creates numbers that look random but come from a repeatable process. You give it a starting value called a seed, and it uses that seed to produce a sequence of random-looking numbers. Use the same seed again, and you get the exact same sequence. Change the seed, and you get a completely different sequence. Random number generators are built with specific algorithms and are used in almost every programming environment and platform. Excel's built-in random functions don't let you choose a seed, so results change whenever the worksheet recalculates. A seeded generator fixes that by giving you stable, reproducible random numbers that won't change with every worksheet change.

### Benefits of seeded random numbers

As shown above, Excel's built-in random functions are volatile and recalculate with each workbook change. Having a seeded random number generator available in Excel offers important benefits, including:

*   On-demand generation of new random values based on a seed.
*   Stable random results that don't recalculate when workbooks are opened or edited.
*   Repeatable results with the same seed value.
*   Better performance by avoiding excessive recalculation.
*   Reproducible worksheet demos.

These benefits allow you to build stable and reproducible worksheets that do things like:

*   Randomly assign students to groups at the start of every month.
*   Randomly pick winners in a prize drawing.
*   Simulate random events in financial modeling or risk analysis.
*   Create reproducible dice rolls or card shuffles.
*   Generate random lists of names, products, countries, sizes, etc

In short, a seeded Random Number Generator is valuable in Excel because it gives you "reproducible randomness"—something Excel's built-in random functions cannot provide.

### Our Approach

We are going to implement a random number generator in Excel by writing a LAMBDA function and naming it `RAND_SEQUENCE` in the name manager. Our function will take two arguments:

*   `seed` - a text string representing the seed value.
*   `n` - a number indicating how many random values to return.

When we're finished, we'll be able to call our new function like any other Excel function, and it will return random decimal values. For example, if we call RAND\_SEQUENCE with the seed "apple" and the number 3, we'll get back numbers like this:

    =RAND_SEQUENCE("apple",3) // returns {0.710028;0.444729;0.560484}
    

And, when we call the function again somewhere else in the spreadsheet and pass in the same seed value, we'll get the same random values:

    =RAND_SEQUENCE("apple",3) // returns {0.710028;0.444729;0.560484}
    

In other words, the function returns random numbers, but these numbers are uniquely determined by the seed value passed into the function. To generate a new sequence of random numbers, we pass in a different seed value. This is what makes a function like this so useful and is exactly what the teacher in our scenario could use to reassign students into groups at the start of every month.

This approach is made possible by the new LAMBDA functions introduced in Excel over the past few years, including [LET](https://exceljet.net/functions/let-function)
, [LAMBDA](https://exceljet.net/functions/lambda-function)
, [MAP](https://exceljet.net/functions/map-function)
, [SCAN](https://exceljet.net/functions/scan-function)
, [REDUCE](https://exceljet.net/functions/reduce-function)
, and [more](https://exceljet.net/new-excel-functions)
. These functions really expand what's possible in Excel by unlocking new ways to tackle hard problems. In our case, implementing a seeded random number generator is an excellent example of how these functions can be used to create a useful new feature that can be used just like a built-in Excel function.

### The RNG algorithm

There are many different ways to implement a seeded random number generator. We are going to write a formula that uses the [Park-Miller "minimal standard" LCG algorithm](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
, because it's well-documented and straightforward to implement.

The way this algorithm works is by performing a series of multiplications and mod operations on an initial seed value. For example, starting with an integer seed value, we multiply it by `a=16807` and then take the remainder of dividing the result by `m=2147483647` using the MOD function. This gives us a random integer between zero and the value of `m`. To generate the next random integer, we use the previous result as the seed value and repeat the process.

For example, to generate the first integer using a seed value of `42` we calculate the result of `MOD(a*42, m)` like this:

    =LET(
      seed,42,
      a,16807,
      m,2147483647,
      MOD(a*seed,m)
    ) // returns 705894
    

Then, to generate the next integer, we pass in `705894` as the current seed value and perform the same operation: multiply by `a` and take the remainder of dividing by `m`.

    =LET(
      seed,705894,
      a,16807,
      m,2147483647,
      MOD(a*seed,m)
    ) // returns 1126542223
    

And so on. The screenshot below shows how this formula can be adapted to generate values in Excel. Notice that the seed value is defined as the value in the cell above, starting at B5. As the formula in `B6` is dragged down, it generates the sequence of random integers seen below:

![Simple random number generation by dragging the formula down](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/random_number_generator_simple_rng.png "Simple random number generation by dragging the formula down")

To normalize this sequence of random integers to numbers between zero and one, we can divide by the value of `m=2147483647` like this:

![Dividing by m to normalize output ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/random_number_generator_simple_rng_normalized.png "Dividing by m to normalize output")

This gives us a seeded sequence of random numbers using the Park-Miller algorithm. Now you could use this formula as-is in a helper column, but what we want to do is convert this to a LAMBDA function that takes in a seed and quantity as arguments and spills the random numbers. There are a number of benefits to doing this:

1.  Naming the function in the name manager makes it so we can use it elsewhere in the spreadsheet and abstracts the implementation details from the user.
2.  Having a function that spills the results removes the need for a helper column and makes the random number generator more practical to use.
3.  The arguments can be normalized to prevent errors.

The end result will be a function that takes in a seed value and quantity as arguments and spills the random numbers. This is similar to the behavior of [RANDARRAY](https://exceljet.net/functions/randarray-function)
, except our function allows us to control when the random numbers are generated.

### Implementing the LAMBDA function

First, let's create a formula that has the spill behavior that we want. Once we get that working, we'll wrap it in a [LAMBDA](https://exceljet.net/functions/lambda-function)
 and give it a name in the name manager.

To start, we'll use the [SCAN function](https://exceljet.net/functions/scan-function)
 to generate a sequence of seed values. The syntax of the SCAN function looks like this:

    =SCAN([initial_value],array,lambda)
    

*   initial\_value (optional): The starting value for the accumulation.
*   array: The array (range or constant array) to process.
*   lambda(accumulator, value): A custom function that defines how to combine the running total (accumulator) with each element (value).

The way SCAN works is it processes each element of the array. At each step:

*   The accumulator holds the running result so far
*   The value is the current element from the array
*   The LAMBDA function is called with the current value of the accumulator and the current element from the array to calculate the next value of the accumulator

For example, the following formula generates a running total for the input array `{1; 2; 3}` generated by the [SEQUENCE](https://exceljet.net/functions/sequence-function)
 function:

    =SCAN(0,SEQUENCE(3),LAMBDA(acc,val,acc+val)) // returns {1;3;6}
    

The key feature of SCAN is that it outputs an _array of running results for each step_, which is the spill behavior we want. In other words, the length of the input array controls how many times the lambda function is called, so our basic setup looks something like this:

    =LET(
      seed,42,
      n,5,
      step,LAMBDA(...)
      SCAN(seed,SEQUENCE(n),step)
    )
    

We call SCAN with the initial seed value and an array whose length is equal to the number of random integers to generate. The step function will implement the logic from earlier to calculate the next seed value using the current seed value.

For example, to generate the first three values, set up the formula like this with the `seed=42` and `n=3`:

    =LET(
      seed,42,
      n,3,
      a,16807,
      m,2147483647,
      step,LAMBDA(s,_,MOD(a*s,m)),
      SCAN(seed,SEQUENCE(n),step)
    ) // returns {705894;1126542223;1579310009}
    

This formula returns the same sequence of integers as before: `{705894; 1126542223; 1579310009}`.

To understand how SCAN works in this context, let's trace through the chain of calls to the lambda function. When we call `SCAN(seed, SEQUENCE(3), step)`, the lambda function `step` gets called three times with the following arguments:

1.  `step(42, 1) → returns 705894`
2.  `step(705894, 2) → returns 1126542223`
3.  `step(1126542223, 3) → returns 1579310009`

The lambda function calculates the next seed value by multiplying the current seed value by `a=16807` and taking the remainder of dividing by `m=2147483647` using the MOD function. For each call, the result is passed to the next call to be used as the seed value represented by the argument `s`. This is why the first argument of the lambda function is called an accumulator, because it gets passed between each call.

> Note: We don't actually use the values in the array generated by SEQUENCE. This is why the second argument of the `step` lambda function is named with an underscore symbol (\_) to indicate that the value is never used. What's important about the input array is that it controls how many times the `step` lambda function is called.

As before, to normalize these random numbers to be in the range from zero to one, we divide by the value of `m`.

    =LET(
      seed,42,
      n,5,
      a,16807,
      m,2147483647,
      step,LAMBDA(s,_,MOD(a*s,m)),
      results,SCAN(seed,SEQUENCE(n),step),
      results/m
    )
    

This formula generates a sequence of random numbers based on the seed value, where `n=5` controls how many values are generated.

![Random Number Generator using SCAN to spill](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/random_number_generator_with_scan_function.png "Random Number Generator using SCAN to spill")

To convert this into a lambda function, wrap the formula in a lambda function and change `seed` and `n` to be parameters of the lambda function. For example, the following formula is equivalent to the previous version that uses LET:

    =LAMBDA(seed,n,
      LET(
        a,16807,
        m,2147483647,
        step,LAMBDA(s,_,MOD(a*s,m)),
        results,SCAN(seed,SEQUENCE(n),step),
        results/m
      )
    )(42,5)
    

Here we are invoking our lambda function and passing in `seed=42` and `n=5` as input, which is a good way to test and tweak the lambda function before adding it to the name manager. When we add the formula to the name manager, we'll remove the `(42, 5)` which is a special syntax used to call the function before it has a name. To name the formula, go to Formulas > Name Manager > New and enter `RAND_SEQUENCE` for the name and then enter the following formula for the value:

    =LAMBDA(seed,n,
      LET(
        a,16807,
        m,2147483647,
        step,LAMBDA(s,_,MOD(a*s,m)),
        results,SCAN(seed,SEQUENCE(n),step),
        results/m
      )
    )
    

After adding the formula to the name manager, you should see the function in the name manager like this:

![Custom function RAND_SEQUENCE in name manager](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/NameManager-RAND_SEQUENCE.png "Custom function RAND_SEQUENCE in name manager")

Now we can use the RAND\_SEQUENCE function in the spreadsheet like this to generate a sequence of 10 random numbers using a seed value.

![Calling our custom RAND_SEQUENCE function like other Excel functions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/random_number_generator_custom_function_rand_sequence.png "Calling our custom RAND_SEQUENCE function like other Excel functions")

### Improving the formula

This is a good start, but there are some improvements we should make to make the function more robust and user-friendly. To begin with, we should normalize the seed value so it is an integer greater than zero and less than `m`. This prevents some issues that can arise if the seed value is zero or greater than `m`. To do this, modify the formula by introducing a new variable `start` that gets set to the normalized seed value:

    =LAMBDA(seed,n,
      LET(
        a,16807,
        m,2147483647,
        start,IF(INT(seed)=0,1,MOD(INT(seed),m)),
        step,LAMBDA(s,_,MOD(a*s,m)),
        results,SCAN(start,SEQUENCE(n),step),
        results/m
      )
    )
    

The second improvement addresses some more subtle issues.

*   If the seed value is small, say in the range of `1-100`, the first random number will always be a relatively small number.
*   Because of how the algorithm works, adjacent seed values produce similar sequences of random numbers. This isn't a huge issue, but it is noticeable if using adjacent seed values like `42` and `43` to sort a list.

These issues can be avoided by using seed values that are evenly distributed across the range of `1` to `m`, but this is a bit of a hassle for the user. We can address both of these issues with a hash function.

### Creating a custom HASH function

A simple way to handle the issues mentioned above is to introduce a "hash" function in the name manager and use it to generate seed values. Hash functions are another example of a well-understood and useful concept that can be implemented in Excel using the new lambda functions. Simply put, a hash function takes in a string and returns a number.

What this means for our RAND\_SEQUENCE function is that we can pass a string instead of an integer to be used as the seed value. This will resolve both issues. The hash function will produce a suitably large integer for the seed value, and make it easy for the user to avoid adjacent seed values.

The following formula implements a hash function (DJB2) that takes in a string and returns a number. For example, given the string `"apple"`, the hash function returns the number `253337143`:

    =LAMBDA(str,
      LET(
        s,TEXT(str,"@"),
        bytes,UNICODE(MID(s,SEQUENCE(LEN(s)),1)),
        h0,5381,
        step,LAMBDA(h,c,MOD(h*33+c,2^32)),
        REDUCE(h0,bytes,step)
      )
    )("apple") // returns 253337143
    

As before, to create a new custom function, we open the Name Manager at Formulas > Name Manager > New and enter `HASH` for the name and the lambda function above for the value. Now we can use the new HASH function like this:

    =HASH("apple") // returns 253337143
    =HASH("orange") // returns 319921761
    

To incorporate the HASH function into the RAND\_SEQUENCE function, we use it to normalize the seed value like this:

    =LAMBDA(seed,n,
      LET(
        a,16807,
        m,2147483647,
        h,HASH(seed),
        start,IF(INT(h)=0,1,MOD(INT(h),m)),
        step,LAMBDA(s,_,MOD(a*s,m)),
        results,SCAN(start,SEQUENCE(n),step),
        results/m
      )
    )
    

Now we have a robust and user-friendly random number generator that can be used to generate reproducible random numbers using a seed value like "apple" or "orange".

    =RAND_SEQUENCE("apple",10) // spills ten random numbers
    

![RAND_SEQUENCE using HASH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/random_number_generator_rand_sequence_with_hash.png "RAND_SEQUENCE using HASH")

### Sorting students with RAND\_SEQUENCE

To use the custom RAND\_SEQUENCE function to sort students into groups, we can adapt our original random sort formula above to use random numbers generated by the RAND\_SEQUENCE function instead of RANDARRAY:

    =SORTBY(range,RANDARRAY(ROWS(range)))
    

Becomes:

    =SORTBY(range,RAND_SEQUENCE(ROWS(range)))
    

A final touch is to wrap the formula in the LET function so that we only refer to the range once. You can see how this works in the worksheet below, where the following formula sorts the students in `B3:B11` with the seed value of "apple" in `G3`.

    =LET(
      students,B3:B11,
      SORTBY(students,RAND_SEQUENCE(G3,ROWS(students)))
    )
    

![Random groups with the seed value "apple"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/random_number_generator_sort_students_apple.png "Random groups with the seed value \"apple\"")

Now that we have a seeded random number determining the sort order, the results will not change when routine edits are made to the worksheet. Only the seed value in G3 controls the output — other changes in the workbook will not cause the formula to generate new results. When we change the seed value in G5 to "orange", the formula will sort the students in a different random order:

![Random groups with the seed value "orange"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/random_number_generator_sort_students_orange.png "Random groups with the seed value \"orange\"")

Even better, the random sort is reproducible: if you change the seed value back to "apple", you again see the random sort associated with that seed. In other words, you can easily reproduce the first random sort.

This is exactly what we set out to do. We have a function that takes in a seed value and quantity as arguments and spills random numbers. This is a significant upgrade to the volatile results that Excel's random functions generate, and very handy in any situation where you need stable and reproducible random results.

### Using RAND\_SEQUENCE in your workbooks

You might wonder how you can easily define the two custom functions explained above, RAND\_SEQUENCE and HASH in your own workbooks without recreating them from scratch with the Name Manager. This is not difficult. The Excel workbook attached to this article contains the RAND\_SEQUENCE function and the HASH function already defined and ready to use. To quickly copy these functions into your own workbook, follow these steps:

1.  Go to Sheet8 in the workbook, which uses the final function
2.  Right-click the sheet name and select "Move or Copy…"
3.  For "To book", select an existing (or new) workbook.
4.  Tick the "Create a copy" checkbox to leave the original sheet intact.
5.  Click OK to copy the sheet.
6.  The named formulas are now in the destination workbook.
7.  If desired, delete the copied sheet. The named formulas will remain.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

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