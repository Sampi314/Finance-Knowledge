# Split text string to character array - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/split-text-string-to-character-array

---

[Skip to main content](https://exceljet.net/formulas/split-text-string-to-character-array#main-content)

[](https://exceljet.net/formulas/split-text-string-to-character-array#)

*   [Previous](https://exceljet.net/formulas/split-text-string-at-specific-character)
    
*   [Next](https://exceljet.net/formulas/split-text-with-delimiter)
    

[Text](https://exceljet.net/formulas#Text)

Split text string to character array
====================================

by Dave Bruns · Updated 21 Mar 2025

Related functions 
------------------

[REGEXEXTRACT](https://exceljet.net/functions/regexextract-function)

[MID](https://exceljet.net/functions/mid-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[LEN](https://exceljet.net/functions/len-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9005/download?token=5N6adXAU)
 (28.27 KB)

![Excel formula: Split text string to character array](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/split_text_string_to_character_array_0.png "Excel formula: Split text string to character array")

Summary
-------

To convert a text string into an array of characters, you can use a simple formula based on the [REGEXEXTRACT function](https://exceljet.net/functions/regexextract-function)
. In the example shown, the formula in cell D5 is:

    =REGEXEXTRACT(B5,".",1)

The result is a [horizontal array](https://exceljet.net/glossary/array)
 containing the 9 characters in "12 apples" that [spills](https://exceljet.net/glossary/spill)
 into the range D5:L5. As the formula is copied down, each text string in column B is converted to an array of characters.

> REGEXEXTRACT is a [new function](https://exceljet.net/articles/regular-expressions-in-excel)
>  in Excel 365. The article below describes some alternatives that will work in older versions of Excel.

Generic formula
---------------

    =REGEXEXTRACT(text,".",1)

Explanation 
------------

In this example, the goal is to use a formula to split a text string into an [array](https://exceljet.net/glossary/array)
 of characters. For example, if the text string is "Apple", the resulting array should be {"A","p","p","l","e"}. For a long time, this was quite a difficult problem that required a complicated array formula approach. When the SEQUENCE function was introduced, the problem became simpler since SEQUENCE could generate numbers that could be used with the MID function to extract characters one by one. The big breakthrough, however, came when the [REGEXEXTRACT function was introduced](https://exceljet.net/articles/regular-expressions-in-excel)
. For the first time in Excel, you can convert a text string to an array of characters with a single function call. The article below explains several options for solving this problem, including options that will work in older versions of Excel.

### Why create an array of characters?

Why would you want to convert a text string to an array? Basically, an array is a convenient container that you can feed into many other functions. Remember that arrays in Excel correspond directly to ranges, and there are many Excel functions designed to work with arrays and ranges. Once you have content in an array, you apply functions to sort, filter, count, analyze, extract unique values, etc. For example, you could use the FILTER function to preserve or remove specific characters and then use the TEXTJOIN function to recombine the remaining characters into a text string. Here are some scenarios where splitting a text string into an array of characters can be useful:

*   To remove specific characters in a text string with the FILTER function.
*   To sort characters in a text string with the SORT function.
*   To count unique characters in a text string with the UNIQUE function.
*   To process characters with the CODE or UNICODE function.

### Why not TEXTSPLIT?

The newer [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 is designed to split text strings into arrays using a custom delimiter. TEXTSPLIT works great for splitting text into words or splitting comma-separated text. However, there is currently no way to split text into characters with TEXTSPLIT because there is no "delimiter" between characters. You might think you can do something clever like this:

    =TEXTSPLIT(A1,"")

But that won't work. TEXTSPLIT will return a #VALUE! error.

### Option #1 - REGEXEXTRACT

In 2024, Excel introduced the [REGEXEXTRACT function](https://exceljet.net/functions/regexextract-function)
 and this provides the simplest and cleanest way to convert a text string to an array of characters. This is the method used in the workbook shown above, where the formula in D5 looks like this:

    =REGEXEXTRACT(B5,".",1)

![How to convert a text string to an array of characters with REGEXEXTRACT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split_text_string_to_character_array_with_REGEXEXTRACT.png "How to convert a text string to an array of characters with REGEXEXTRACT")

The configuration for REGEXEXTRACT is simple:

*   _text_ - provided as B5
*   _pattern_ - provided as "." (in regex, this means "any single character")
*   _return\_mode_ - provided as 1 (all matches)

In cell D5, the REGEXEXTRACT function returns an array of 9 characters like this:

    {"1","2"," ","a","p","p","l","e","s"}

As the formula is copied down, it returns a character array for each of the text strings seen in column B. As you can see, this is a simple and elegant solution. I recommend this approach if you have access to REGEXEXTRACT.

### Option #2 - MID and SEQUENCE

Before the REGEXEXTRACT function became available in Excel, the best way to solve this problem was to use a formula based on the MID, SEQUENCE, and LEN functions. You can see this approach below, where the formula in D5 is:

    =MID(B5,SEQUENCE(1,LEN(B5)),1)

![How to split text to an array of characters with SEQUENCE and MID](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split_text_string_to_character_array_with_SEQUENCE_and_MID.png "How to split text to an array of characters with SEQUENCE and MID")

Essentially, this is a workaround formula. To understand this formula, we need to consider how the MID function is designed to work. Typically, the [MID function](https://exceljet.net/functions/mid-function)
 is used to extract one or more characters from a text string with a syntax like this:

    =MID(text,start_num,num_chars)

For example, you can use MID like this:

    =MID("12 apples",1,1) // returns "1"
    =MID("12 apples",1,2) // returns "12"
    =MID("12 apples",3,6) // returns "apple"

Depending on the value given for _start\_num_ and _num\_chars_, we get a different part of the string. However, in this case, we don't want to return parts of the text string; we want to return all the characters in the text string together in an array. The trick is to ask the MID function for more than one _start\_num_ simultaneously. For example, to return the three letters in "red" in an array, we can use the [array constant](https://exceljet.net/glossary/array-constant)
 {1,2,3} like this:

    =MID("red",{1,2,3},1) // returns {"r","e","d"}

Because we are asking MID for 1 character starting at three positions {1,2,3}, we get back all three letters in "red" in a single array. This approach works, but we need a way to generate the numeric sequence _dynamically_. Enter the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
, which is perfectly suited for this task. Turning back to the example above, we have this formula in cell D5:

    =MID(B5,SEQUENCE(1,LEN(B5)),1)

Working from the& inside out, the [LEN function](https://exceljet.net/functions/len-function)
 is used to calculate the number of characters in cell B5, which is 9. Dropping that value into the formula, we have:

    =MID(B5,SEQUENCE(1,9),1)

With 1 for the _rows_ argument and 9 for _columns_, SEQUENCE returns a numeric array beginning with 1 and ending with 9. This array is delivered to the MID function as the _start\_num,_ with _num\_chars_ set to 1:

    =MID(B5,{1,2,3,4,5,6,7,8,9},1)

In other words, we are asking MID for 1 character starting at nine different positions, one for each character in the source text. With this configuration, MID dutifully extracts all 9 characters in delivers the result in an array like this:

    {"1","2"," ","a","p","p","l","e","s"}

When this array lands in cell D5, it [spills](https://exceljet.net/glossary/spill)
 into the range D5:L5. Notice the final array is comma-separated, which corresponds to a horizontal [array](https://exceljet.net/glossary/array)
 or range in Excel. The reason we get a horizontal array in columns instead of a vertical array in rows is that we configured SEQUENCE to ask for columns instead of rows.

> This formula is more transparent than the REGEXEXTRACT option. It is possible to understand what the formula is doing step-by-step. However, it is also significantly more complex.

Legacy Excel
------------

In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, it is more challenging to split a text string into an array of characters. There are two basic approaches. The first and easiest is to use carefully constructed mixed references in a worksheet that has the numbers you need already available. The second approach is to use a more complex array formula.

### Option #1 - MID + Mixed references

If the goal is to extract characters into separate cells, you can use a simple formula that relies on mixed references. The trick is to set up a worksheet that contains a sequence of numbers that can be used to extract characters one by one with the [MID function](https://exceljet.net/functions/mid-function)
. You can see this approach below, where the formula in D5 looks like this:

    =MID($B5,D$4,1)

![How to split text into characters in Legacy Excel with MID and relative references](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split_text_string_to_character_array_with_MID_and_mixed_references.png "How to split text into characters in Legacy Excel with MID and relative references")

This works because we can use the numbers in the range D4:P4 directly as _start\_num_ inside the MID function. Notice that $B5 and D$4 are both [mixed references](https://exceljet.net/glossary/mixed-reference)
 so that the formula can be copied throughout the range. Compared to the [dynamic array](https://exceljet.net/glossary/dynamic-array)
 solution above, one big difference in this approach is that results will not automatically spill onto the worksheet into a [spill range](https://exceljet.net/glossary/spill-range)
. Instead, the formulas must be manually copied into a range of cells big enough to hold all characters.

### Option #2 - Array formula with INDIRECT + ROW

There is a way to generate an array of characters from a text string in older versions of Excel, but it requires a more complicated array formula. The core of this solution is to use the [ROW](https://exceljet.net/functions/row-function)
 and [INDIRECT](https://exceljet.net/functions/indirect-function)
 functions in place of SEQUENCE like this:

    =MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1)

You will find code like this in many older array formulas that predate [dynamic arrays in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. The INDIRECT function is a way of changing cell references as text into actual cell references. In the formula above, INDIRECT converts the text "1:9" into an actual reference, and ROW returns an array of row numbers. The code evaluates like this:

    =MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1)
    =MID(B5,ROW(INDIRECT("1:"&9)),1)
    =MID(B5,ROW(INDIRECT("1:9")),1)
    =MID(B5,{1;2;3;4;5;6;7;8;9},1)
    ={"1";"2";" ";"a";"p";"p";"l";"e";"s"}
    

One problem with the formula above is that the array is vertical because we are using the ROW function. To get a horizontal array, the last step is to wrap the formula in the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 like this:

    =TRANSPOSE(MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1))

The final result is a horizontal array, as you can see in the worksheet below:

![How to split text into characters in Legacy Excel with an array formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split_text_string_to_character_array_with_array_formula.png "How to split text into characters in Legacy Excel with an array formula")

Unfortunately, this array formula won't spill in older versions of Excel, and it requires special handling. To make it work, you must first select the correct number of cells (D5:L5 in row 5), then enter the formula as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
. This makes the formula unworkable if you need automation. However, this approach still has value in older versions of Excel in formulas that don't need to [spill](https://exceljet.net/glossary/spill)
 multiple values. For an example, see [Count numbers in a text string](https://exceljet.net/formulas/count-numbers-in-text-string)
.

Related formulas
----------------

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

[![Excel formula: Count numbers in text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_numbers_in_text_string.png "Excel formula: Count numbers in text string")](https://exceljet.net/formulas/count-numbers-in-text-string)

### [Count numbers in text string](https://exceljet.net/formulas/count-numbers-in-text-string)

In this example, the goal is to count numbers that appear in column B. The COUNT function is designed to only count numeric values, but because all values in the range B5:B15 are text , COUNT will return zero. One approach is to split the characters in each text value into an array , then use the...

[![Excel formula: Cell contains number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_number.png "Excel formula: Cell contains number")](https://exceljet.net/formulas/cell-contains-number)

### [Cell contains number](https://exceljet.net/formulas/cell-contains-number)

In this example, the goal is to test the passwords in column B to see if they contain a number. This is a surprisingly tricky problem because Excel doesn't have a function that will let you test for a number inside a text string directly. Note this is different from checking if a cell value is a...

Related functions
-----------------

[![Excel REGEXEXTRACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regexextract_function.png "Excel REGEXEXTRACT function")](https://exceljet.net/functions/regexextract-function)

### [REGEXEXTRACT Function](https://exceljet.net/functions/regexextract-function)

The Excel REGEXEXTRACT function extracts matching text defined by a given pattern. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXEXTRACT will return the first match, but...

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    
*   [Count numbers in text string](https://exceljet.net/formulas/count-numbers-in-text-string)
    
*   [Cell contains number](https://exceljet.net/formulas/cell-contains-number)
    

### Functions

*   [REGEXEXTRACT Function](https://exceljet.net/functions/regexextract-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

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