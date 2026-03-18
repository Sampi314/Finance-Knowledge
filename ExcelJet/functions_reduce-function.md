# Excel REDUCE function | Exceljet

**Source:** https://exceljet.net/functions/reduce-function

---

[Skip to main content](https://exceljet.net/functions/reduce-function#main-content)

[](https://exceljet.net/functions/reduce-function#)

*   [Previous](https://exceljet.net/functions/randarray-function)
    
*   [Next](https://exceljet.net/functions/regexextract-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

REDUCE Function
===============

by Dave Bruns · Updated 7 Nov 2025

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LET](https://exceljet.net/functions/let-function)

[MAP](https://exceljet.net/functions/map-function)

[SCAN](https://exceljet.net/functions/scan-function)

[REDUCE](https://exceljet.net/functions/reduce-function)

[MAKEARRAY](https://exceljet.net/functions/makearray-function)

[BYCOL](https://exceljet.net/functions/bycol-function)

[BYROW](https://exceljet.net/functions/byrow-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9380/download?token=jjgH-Q83)
 (52.94 KB)

![Excel REDUCE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20reduce%20function.png "Excel REDUCE function")

Summary
-------

The Excel REDUCE function applies a custom LAMBDA function to each element in a given array and accumulates results to a single value.

Purpose 
--------

Reduce an array

Return value 
-------------

A single value

Syntax
------

    =REDUCE([initial_value],array,function)

*   _initial\_value_ - \[optional\] The initial value of the accumulator.
*   _array_ - The array to be reduced.
*   _function_ - The function or custom LAMBDA to apply.

Using the REDUCE function 
--------------------------

The REDUCE function applies a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to each element in a given array and accumulates results to a single value. The REDUCE function is useful when you want to process each element in an array and return a single aggregated result. REDUCE is handy for creating custom calculations that Excel doesn't have built-in functions for, such as conditional sums, conditional counts, and other complex aggregations.

> Like the [SCAN function](https://exceljet.net/functions/scan-function)
> , REDUCE iterates over all elements in an array and performs a calculation on each element while updating the value of an accumulator. However, while SCAN returns an _array_ of intermediate values, REDUCE returns a _single_ final value.

### Key features

*   Reduce or aggregate values into a single result.
*   Uses a custom LAMBDA function to apply calculations.
*   Tracks the prior result of a calculation as an "accumulator".
*   Complete control over how values accumulate.
*   Good for conditional sums, counts, and other complex aggregations.
*   Able to use logical functions like AND, OR, NOT, etc. to apply conditions.
*   Can replace complex formulas with more readable and maintainable code.

> REDUCE returns a _single_ aggregated result after processing all elements in an array. To process an array and return all intermediate values, see the [SCAN function](https://exceljet.net/functions/scan-function)
> . To process each element in an array individually and return an array of transformed results, see the [MAP function](https://exceljet.net/functions/map-function)
> .

### Table of contents

*   [LAMBDA structure](https://exceljet.net/functions/reduce-function#lambda-structure)
    
*   [REDUCE for a basic conditional sum](https://exceljet.net/functions/reduce-function#reduce-for-a-basic-conditional-sum)
    
*   [REDUCE for a conditional count](https://exceljet.net/functions/reduce-function#reduce-for-a-conditional-count)
    
*   [REDUCE for conditional concatenation](https://exceljet.net/functions/reduce-function#reduce-for-conditional-concatenation)
    
*   [REDUCE to split comma-separated values](https://exceljet.net/functions/reduce-function#reduce-to-split-comma-separated-values)
    
*   [REDUCE to extract unique words from a range](https://exceljet.net/functions/reduce-function#reduce-to-extract-unique-words-from-a-range)
    
*   [REDUCE to extract and count unique words](https://exceljet.net/functions/reduce-function#reduce-to-extract-and-count-unique-words)
    
*   [REDUCE to extract unique values case-sensitive](https://exceljet.net/functions/reduce-function#reduce-to-extract-unique-values-case-sensitive)
    
*   [REDUCE to remove unwanted text](https://exceljet.net/functions/reduce-function#reduce-to-remove-unwanted-text)
    
*   [REDUCE to find and replace multiple values](https://exceljet.net/functions/reduce-function#reduce-to-find-and-replace-multiple-values)
    

### LAMBDA structure

The REDUCE function takes three arguments: _initial\_value_, _array_, and function. _Initial\_value_ is an optional initial seed value to use for the accumulator. _Array_ is the array to reduce, and _function_ is typically a custom LAMBDA function to apply to each value in the array. The structure of the LAMBDA used in REDUCE looks like this:

    LAMBDA(a,v,calculation)
    

The first argument, _a_, is the accumulator. The accumulator begins as the _initial\_value_ provided to REDUCE and changes as the REDUCE function iterates over the elements in the array and applies a calculation. The _v_ argument represents the value of each item in the array. The _calculation_ is a formula that operates on the accumulator (a) and value (v). The result of the calculation defines the value of the accumulator for the next iteration, and the final result is the value of the accumulator after all elements have been processed. For example, in the formula below, REDUCE is used to sum all values in an array:

    =REDUCE(0,{1,2,3,4,5},LAMBDA(a,v,a+v)) // returns 15
    

The _initial\_value_ is provided as zero, the _array_ is hard-coded as the array constant {1,2,3,4,5}, and the calculation, `LAMBDA(a,v,a+v)`, simply adds the accumulator and value. The table below shows how the accumulator value changes during each iteration as REDUCE processes the array {1,2,3,4,5} starting with an initial value of 0. Notice that the accumulator is updated with the result of the calculation at each iteration.

| Iteration | Value (v) | Accumulator (a) | Calculation | Result |
| --- | --- | --- | --- | --- |
| Initial | \-  | 0   | \-  | \-  |
| 1   | 1   | 0   | 0 + 1 | 1   |
| 2   | 2   | 1   | 1 + 2 | 3   |
| 3   | 3   | 3   | 3 + 3 | 6   |
| 4   | 4   | 6   | 6 + 4 | 10  |
| 5   | 5   | 10  | 10 + 5 | 15  |

The final result returned by REDUCE is 15, which is the final value of the accumulator after all elements have been processed.

> The REDUCE function always assigns the first argument of LAMBDA to the accumulator (a) and the second argument to the current value (v) from the array. This behavior is built into the function's design and cannot be changed. The names _a_ and _v_ are arbitrary, used to represent _accumulator_ and _value_. You can use any names that make sense to you for a given use case.

> As mentioned above, _initial\_value_ is optional. Although it does not appear in Excel's official documentation, it [seems](https://stackoverflow.com/questions/76678903/how-does-reduce-formula-start-caclulation-without-a-given-initial-value-excel)
>  that if the initial value is omitted, it does not default to zero (0) or an empty string ("") as you might expect. Instead, REDUCE takes the first element of the array as the initial value, then iterates over the remaining elements of the array. In other words, if you omit the _initial\_value_, Excel treats the first element of the array as the starting _accumulator_, and processing continues from the _second_ element onward. To avoid confusion, it's a good idea to set the initial value explicitly. One possible exception is when using REDUCE with VSTACK to stack 1D arrays. In that case, using an empty string ("") for the initial value will result in an extra element in the final array, which you will need to remove later with the DROP function. Omitting the initial value avoids this additional step.

### REDUCE for a basic conditional sum

One way to use the REDUCE function is to create a conditional sum that uses custom logic that would be difficult with a built-in function like SUMIFS. In the worksheet shown below, we have a list of numbers in the range B5:B16, and we want to create a sum of the even numbers in the range. The formula in D5 looks like this:

    =REDUCE(0,B5:B16,LAMBDA(a,v,IF(ISEVEN(v),a+v,a)))
    

Notice that we have provided an _initial\_value_ of zero (0) and the _array_ is given as the range B5:B16. The LAMBDA calculation looks like this:

    LAMBDA(a,v,IF(ISEVEN(v),a+v,a))
    

Inside the LAMBDA function, the `a` argument is the accumulator, and the `v` argument is the value. These values are provided by the REDUCE function. The [IF function](https://exceljet.net/functions/if-function)
 is used with the [ISEVEN function](https://exceljet.net/functions/iseven-function)
 to make the sum conditional. Values in the array are only added to the accumulator if they are even numbers. The REDUCE function iterates over all values in B5:B16. For each value `v`, it checks if it is even using ISEVEN. If it is even, it adds the value to the accumulator `a`. If it is not even, it keeps the accumulator unchanged. The final result is 40, the sum of the even numbers 2,4,6,10,6, and 12.

![REDUCE function for a basic conditional sum](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/reduce-function-basic-conditional-sum.png "REDUCE function for a basic conditional sum")

To calculate a conditional sum of _odd_ numbers, we can simply swap ISEVEN for ISODD:

    =REDUCE(0,B5:B16,LAMBDA(a,v,IF(ISODD(v),a+v,a)))
    

The only difference is that the [ISODD function](https://exceljet.net/functions/isodd-function)
 is used instead of ISEVEN. This formula works just like the formula in D5, but it sums the odd numbers instead of the even numbers. The final result is 60, the sum of the odd numbers 1,3,5,13,27, and 11.

Finally, to illustrate what the same formula looks like without any conditional logic, the formula in cell D7 sums all numbers in the range B5:B16 like this:

    =REDUCE(0,B5:B16,LAMBDA(a,v,a+v))
    

Here, REDUCE iterates over the range B5:B16 and adds the accumulator and value unconditionally at each iteration. The final result is 100.

> The reason this formula is difficult with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
>  is that SUMIFS requires a _range_ for the criteria, but ISODD and ISEVEN will return an _array_ of results.

### REDUCE for a conditional count

REDUCE can also be used to create a conditional count using logic that is difficult with a built-in function like COUNTIFS. In the worksheet shown below, we have a list of values like A-67, B-75, A-71, and so on. The goal is to count values that begin with "A" and that are greater than 75. The formula in cell D5 looks like this:

    =REDUCE(0,B5:B16,LAMBDA(a,v,IF(AND(TEXTBEFORE(v,"-")="a",VALUE(TEXTAFTER(v,"-"))>=75),a+1,a)))
    

Notice that we have provided an _initial\_value_ of zero (0), and the _array_ is given as the range B5:B16. The LAMBDA calculation looks like this:

    LAMBDA(a,v,IF(AND(TEXTBEFORE(v,"-")="a",VALUE(TEXTAFTER(v,"-"))>=75),a+1,a))
    

This example shows how the REDUCE function can be used with the AND function to apply two conditions to a value:

1.  The value must begin with A
2.  The number after the hyphen must be greater than or equal to 75

![REDUCE for a conditional count](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/reduce-function-conditional-count.png "REDUCE for a conditional count")

As always, the values for `a` and `v` are provided by the REDUCE function to the LAMBDA. The [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
 is used to get the text before the hyphen, and the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
 is used to get the text after the hyphen. The [VALUE function](https://exceljet.net/functions/value-function)
 is used to convert the text after the hyphen into a number. The [IF function](https://exceljet.net/functions/if-function)
 is used to check if the value meets the conditions defined by the [AND function](https://exceljet.net/functions/and-function)
. If it does, the accumulator is incremented by 1. If it does not, the accumulator is returned unchanged. In this case, the final result is 2, since there are only two values that meet the conditions: A-77 and A-75.

This example illustrates how the REDUCE function can use logical functions like AND, OR, NOT, etc. to apply conditions to values. These functions aggregate an array of results into a single result, which causes trouble in array operations, but they work fine in REDUCE, since REDUCE deals with arrays one element at a time.

> Notes: (1) The logic above could also be constructed with functions like LEFT, RIGHT, MID, etc. TEXTBEFORE and TEXTAFTER are handy because they'll work for any value that has a hyphen. (2) There are many ways to convert text to numbers in Excel. The [VALUE function](https://exceljet.net/functions/value-function)
>  is one way, but you could also use a [double negative](https://exceljet.net/glossary/double-unary)
>  `--`, or add zero (0) `+0`.

### REDUCE for conditional concatenation

REDUCE can also be used to concatenate values with conditional logic. In the worksheet below, the goal is to create a comma-separated list of names in column B that are greater than five characters long. The formula in D5 looks like this:

    =REDUCE("",B5:B16,LAMBDA(a,v,IF(LEN(v)>5,IF(a="",v,a&", "&v),a)))
    

![REDUCE function for conditional concatenation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/reduce-function-conditional-concatenation.png "REDUCE function for conditional concatenation")

Notice that we have provided an _initial\_value_ of an empty string (""), and the _array_ is given as the range B5:B16. The calculation inside the LAMBDA is:

    LAMBDA(a,v,IF(LEN(v)>5,IF(a="",v,a&", "&v),a))
    

Starting with the initial value of an empty string (""), this formula iterates over each name in the range B5:B16 and uses the [LEN function](https://exceljet.net/functions/len-function)
 to check for names greater than five characters. When found, it adds the name to the accumulator with a comma and a space. If it is not, it keeps the accumulator unchanged. To avoid concatenating a comma to the start of the list, we need to do some extra checking with a second IF function:

    IF(a="",v,a&", "&v)
    

This code only runs if we have found a name greater than five characters. If so, we check if the accumulator is an empty string. If it is, it means we have not yet found any names greater than 5 characters. In that case, we return just the value `v` to start the list. If the accumulator is not empty, it means we already have a name in our list, and we return a comma and a space followed by the new value.

> This example nicely illustrates that the reduce function allows you full control over how the accumulator gets populated. However, I should note that there are different ways in Excel to solve this problem. You could, for example, use the FILTER function to isolate names that are greater than five characters and then use TEXTJOIN for concatenation.

### REDUCE to split comma-separated values

The REDUCE function works nicely with the [VSTACK function](https://exceljet.net/functions/vstack-function)
 to progressively build up an array of values. In the worksheet below, we have a list of comma-separated (CSV) values in column B, and the goal is to split each value in column B into the 5 columns to the right, as shown. The formula in D5 looks like this:

    =DROP(REDUCE("",B5:B15,LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,",")))),1)
    

![REDUCE function to split comma-separated values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/reduce-function-split-comma-separated-values.png "REDUCE function to split comma-separated values")

Notice that we have provided an _initial\_value_ of an empty string (""), and the _array_ is given as the range B5:B16. The calculation inside the LAMBDA is:

    LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,",")))
    

This formula works by iterating over each value in the range B5:B16 and splitting the value into an array of words using the TEXTSPLIT function. The VSTACK function is used to stack the results from TEXTSPLIT into a single array. The final result is an array of values in the range D5:H16. Notice we nest the REDUCE function inside the DROP function to remove the extra array created by setting the initial value to an empty string:

    =DROP(REDUCE(...),1)
    

This formula works around an "array of arrays" limitation in Excel that prevents the TEXTSPLIT function from being used on a range of values. For a detailed explanation, see this article: [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
.

### REDUCE to extract unique words from a range

REDUCE can also be used with TEXTSPLIT to extract unique words from a range. In the worksheet below, the goal is to extract a list of unique words from the range B5:B16. The formula in D5 looks like this:

    =UNIQUE(DROP(REDUCE("",B5:B16,LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,," ")))),1))
    

![REDUCE function to extract unique words from a range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/reduce-function-extract-unique-words-from-a-range.png "REDUCE function to extract unique words from a range")

The initial value is an empty string (""), and the array is the range B5:B16. The calculation inside the LAMBDA is similar to the CSV example above, except we split text using a space (" ") as the delimiter instead of a comma:

    LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,," ")))
    

The REDUCE function iterates over each value in B5:B16 and splits the text into separate words. Then it stacks the words vertically using the VSTACK function. When REDUCE is done, we have a single list of all words in the range. Next, the result from REDUCE is handed off to the DROP function, which removes the first row. This step is necessary because the initial value of an empty string ("") ends up in the final array. Finally, the result from DROP is passed to the UNIQUE function, which returns a list of unique words. This formula is a great example of how functions in Excel can be nested together:

    =UNIQUE(DROP(REDUCE(...)),1))

> Note: if you have inconsistent spacing between words, run the range through the [TRIM function](https://exceljet.net/functions/trim-function)
>  to remove extra spaces as a first step.

### REDUCE to extract and count unique words

In the worksheet below, the goal is to extract a list of unique words from the range B5:B16 and generate a count for each word. This formula builds directly on the previous example. The formula in D5 looks like this:

    =LET(
    rng,B5:B16,
    words,DROP(REDUCE("",rng,LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,," ")))),1),
    GROUPBY(words,words,COUNTA,0,0,-2))
    

![REDUCE function to extract and count unique words](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/reduce-function-extract-and-count-unique-words.png "REDUCE function to extract and count unique words")

To keep things tidy, we use the LET function to create some variables. The variable `rng` is assigned the range B5:B16. The variable `words` is assigned the result from the REDUCE function, which is configured like the previous example, except we don't pass the result into UNIQUE. Instead, we pass the result into the [GROUPBY function](https://exceljet.net/functions/groupby-function)
. The GROUPBY function works like a lightweight, formula-based pivot table. It automatically creates a list of unique words and, using the [COUNTA function](https://exceljet.net/functions/counta-function)
, generates a count for each word in one fell swoop.

> Note: the GROUPBY function is a newer function with many configuration options. For a detailed guide, see this our article on the [GROUPBY function](https://exceljet.net/functions/groupby-function)
> .

### REDUCE to extract unique values case-sensitive

The REDUCE function can sometimes be used to work around difficult limitations in Excel. In the worksheet below, the goal is to extract a unique list of values from the range B5:B16, taking into account upper and lower case characters. This is a tricky problem in Excel because most built-in functions (including UNIQUE) are not case-sensitive. The formula in D5 avoids the UNIQUE function altogether and uses the EXACT function like this:

    =SORT(REDUCE(,B5:B16,LAMBDA(a,v,IF(SUM(--EXACT(a,v)),a,VSTACK(a,v)))))
    

![REDUCE function to extract unique values case-sensitive](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/reduce-function-extract-unique-values-case-sensitive.png "REDUCE function to extract unique values case-sensitive")

Notice that we are not providing an _initial\_value_. This is a rare case where we omit the initial value altogether in order to avoid removing it later with the DROP function. This only works on one-dimensional arrays. The calculation inside the LAMBDA is:

    LAMBDA(a,v,IF(SUM(--EXACT(a,v)),a,VSTACK(a,v)))
    

At a high level, this formula works by iterating over each value in the range B5:B16 and checking if the value `v` is equal to any value already in the accumulator `a`. If so, we return the accumulator unchanged. If not, we add the value `v` to the accumulator using the VSTACK function. The final result is an array of unique and case-sensitive values in the range. What makes the formula case-sensitive is the EXACT function, which is used together with the SUM function to check each value `v` against the accumulator `a` in this snippet, which is used as the logical test in the IF function:

    SUM(--EXACT(a,v))
    

The EXACT function compares two text values in a case-sensitive manner. If the values are the same, it returns TRUE. If the values are different, it returns FALSE. If one of the values is an array (as with the accumulator in this example), the EXACT function will return an _array_ of Booleans. In other words, each value `v` is tested against every value in the accumulator `a` and all results are returned. The double negative (--) coerces the Boolean values to 1s and 0s. The SUM function then adds up the 1s and 0s to give us a count. If the count is greater than 0, it means the value `v` is already in the accumulator `a`, so we return the accumulator unchanged. If the count is 0, it means the value `v` was not found in the accumulator `a`, so we add the value `v` to the accumulator using the VSTACK function. Finally, the result from REDUCE is passed to the SORT function, which sorts the unique values in ascending order.

For a more detailed explanation, see this article: [Extract unique values case-sensitive](https://exceljet.net/formulas/unique-values-case-sensitive)
.

### REDUCE to remove unwanted text

In this example, the goal is to remove a list of unwanted characters from a range of text strings. This is a good example of how REDUCE can be used in ways that aren't immediately obvious. The text strings to process are in column B, and the characters to remove appear in the range F5:F10. The formula in D5 looks like this:

    =TRIM(REDUCE(B5:B16,F5:F10,LAMBDA(a,v,SUBSTITUTE(a,v," "))))
    

![REDUCE function to remove unwanted text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/reduce-function-remove-unwanted-text.png "REDUCE function to remove unwanted text")

This is a pretty clever formula, and it is easy to get confused about how it works. The key is to look first at the initial value, which is provided as the range B5:B16. This is quite different from the above examples, where the values to process are typically provided as the array argument. Here, the values to process are provided as the _initial\_value_, and the characters to remove are provided as the _array_. What this means is that we are actually calling the REDUCE function 12 times (through a built-in process called "[lifting](https://exceljet.net/glossary/lifting)
"), once for each value in the range B5:B16. Then, for each value in B5:B16, REDUCE iterates over the _array_ of values in F5:F10 and applies a custom LAMBDA function like this:

    LAMBDA(a,v,SUBSTITUTE(a,v," "))
    

The [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 is used to replace the unwanted character with a space (" "). The accumulator `a` is an incoming value from B5:B16. The value `v` comes from F5:F10. Inside SUBSTITUTE, `a` is provided for text, `v` is provided for _old\_text_, and a space (" ") is provided for _new\_text_. At each iteration, the output from SUBSTITUTE `a` is used as the starting point for the next iteration. If the unwanted character is not found, SUBSTITUTE returns the value unchanged. When all unwanted values have been processed, REDUCE moves on to the next value in B5:B16. Finally, the result from REDUCE is passed to the TRIM function, which removes any extra spaces from the text strings.

### REDUCE to find and replace multiple values

In the previous example, we used the reduce function to replace _multiple_ values with a _single_ value. However, you may want to replace _multiple_ values with _multiple_ values in a "batch replace all" operation. In the worksheet below, the goal is to replace each of the "find" values in column F with the corresponding "replace" value in column G. The formula in D5 looks like this:

    =LET(
        range,B5:B16,
        find,F5:F9,
        replace,G5:G9,
        ix, SEQUENCE(ROWS(find)),
        result, REDUCE(range,ix,LAMBDA(a,i,
            SUBSTITUTE(a,INDEX(find,i), INDEX(replace,i))
        )),
        TRIM(result)
    )
    

![REDUCE function to find and replace multiple values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/reduce-function-find-and-replace-multiple-values.png "REDUCE function to find and replace multiple values")

This formula is a bit more complex, but the setup is the same as the previous example: we provide source text in the range B5:B16 as the _initial\_value_, then we provide an array that corresponds to the number of "find/replace" pairs in columns F and G as the _array_. The [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 is used to create a sequence of numbers from 1 to the number of "find/replace" pairs in columns F and G. Since there are 5 rows in F5:F9, SEQUENCE returns the array `{1;2;3;4;5}`:

    SEQUENCE(ROWS(find)) // returns {1;2;3;4;5}
    

This gives us an array that REDUCE can iterate over, and a list of indices that we can use to look up the corresponding "find" and "replace" values in columns F and G. As in the previous example, we use the lifting process to call the REDUCE function 12 times (once for each value in the range B5:B16). Then, for each value in B5:B16, REDUCE iterates over the _array_ of values in F5:F9 and applies a custom LAMBDA function like this:

    LAMBDA(a,i,SUBSTITUTE(a,INDEX(find,i), INDEX(replace,i)))
    

The [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 is used to replace the "find" value with the "replace" value. The [INDEX function](https://exceljet.net/functions/index-function)
 is used to get the "find" and "replace" values from the corresponding columns. The `i` argument is the index of the current value in the array. The `a` argument is the accumulator, which is the current value in the range B5:B16. The result from SUBSTITUTE is used as the starting point for the next iteration. When all "find/replace" pairs have been processed, REDUCE moves on to the next value in B5:B16. Finally, the result from REDUCE is passed to the [TRIM function](https://exceljet.net/functions/trim-function)
, which removes any extra spaces from the text strings.

You can extend and customize the table of replacements as needed. If you need better control over word boundaries (i.e., you don't want to match "red" inside "bored", replace the SUBSTITUTE function with the [REGEXEXTRACT function](https://exceljet.net/functions/regexextract-function)
 like this:

    =LET(
        range,B5:B16,
        find,F5:F9,
        replace,G5:G9,
        ix,SEQUENCE(ROWS(find)),
        result,REDUCE(range,ix,LAMBDA(a,i,
            REGEXREPLACE(a,"\b"&INDEX(find,i)&"\b",INDEX(replace,i))
        )),
        TRIM(result)
    )

If you are new to Regular Expressions (regex) in Excel, see our [regex guide here](https://exceljet.net/articles/regular-expressions-in-excel)
.

REDUCE function examples
------------------------

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

[![Excel formula: Find and replace multiple values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find-and-replace-multiple-values.png "Excel formula: Find and replace multiple values")](https://exceljet.net/formulas/find-and-replace-multiple-values)

### [Find and replace multiple values](https://exceljet.net/formulas/find-and-replace-multiple-values)

There is no built-in function to perform a series of find and replace operations in Excel, but you can create a formula that does the same thing. The goal in this example is to replace multiple ("find") values with corresponding ("replace") values in a single "replace all" operation. The text...

[![Excel formula: Reverse a list or range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/reverse_a_list_or_range.png "Excel formula: Reverse a list or range")](https://exceljet.net/formulas/reverse-a-list-or-range)

### [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)

In this example, the goal is to "reverse" the items in the range B5:B14, so that the first item appears last, the second item appears second to last, and so on. When you first encounter a problem like this in Excel, your first instinct might be to sort the values in some way using the SORT function...

[![Excel formula: Count cells that do not contain many strings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain%20many%20strings.png "Excel formula: Count cells that do not contain many strings")](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)

### [Count cells that do not contain many strings](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)

The goal in this example is to count cells in a range that do not contain a given number of strings. The cells to evaluate are in the named range data (B5:B14) and the strings to exclude are listed in the named range exclude (D5:D7). If your needs are simple, you can use the COUNTIFS function to...

[![Excel formula: Unique values case-sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique_values_case_sensitive.png "Excel formula: Unique values case-sensitive")](https://exceljet.net/formulas/unique-values-case-sensitive)

### [Unique values case-sensitive](https://exceljet.net/formulas/unique-values-case-sensitive)

In this example, the goal is to create a formula that will extract unique values from a range of data in a case-sensitive way. Normally, we would use the UNIQUE function to extract unique values. However, UNIQUE is not case-sensitive so it won't work in this situation. One way to solve this problem...

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel MAP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20map%20function.png "Excel MAP function")](https://exceljet.net/functions/map-function)

### [MAP Function](https://exceljet.net/functions/map-function)

The Excel MAP function "maps" a custom LAMBDA function to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array.

[![Excel SCAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")](https://exceljet.net/functions/scan-function)

### [SCAN Function](https://exceljet.net/functions/scan-function)

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other...

[![Excel REDUCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20reduce%20function.png "Excel REDUCE function")](https://exceljet.net/functions/reduce-function)

### [REDUCE Function](https://exceljet.net/functions/reduce-function)

The Excel REDUCE function applies a custom LAMBDA function to each element in a given array and accumulates results to a single value.

[![Excel MAKEARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20makearray%20function.png "Excel MAKEARRAY function")](https://exceljet.net/functions/makearray-function)

### [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)

The Excel MAKEARRAY function returns an array with specified rows and columns, based on a custom [LAMBDA calculation](https://exceljet.net/functions/lambda-function)
. MAKEARRAY can be used to create arrays with variable dimensions based on a calculation....

[![Excel BYCOL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20bycol%20function.png "Excel BYCOL function")](https://exceljet.net/functions/bycol-function)

### [BYCOL Function](https://exceljet.net/functions/bycol-function)

The Excel BYCOL function applies a function to each column in a given array and returns one result per column. BYCOL can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)
    
*   [Count cells that do not contain many strings](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)
    
*   [Unique values case-sensitive](https://exceljet.net/formulas/unique-values-case-sensitive)
    
*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    
*   [Find and replace multiple values](https://exceljet.net/formulas/find-and-replace-multiple-values)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [MAP Function](https://exceljet.net/functions/map-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    
*   [REDUCE Function](https://exceljet.net/functions/reduce-function)
    
*   [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)
    
*   [BYCOL Function](https://exceljet.net/functions/bycol-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    

### Links

*   [Microsoft REDUCE function documentation](https://support.microsoft.com/en-us/office/reduce-function-42e39910-b345-45f3-84b8-0642b568b7cb)
    
*   [Stackoverflow discussion about initial value in REDUCE](https://stackoverflow.com/questions/76678903/how-does-reduce-formula-start-caclulation-without-a-given-initial-value-excel)
    

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