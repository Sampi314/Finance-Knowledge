# Excel CHOOSE function | Exceljet

**Source:** https://exceljet.net/functions/choose-function

---

[Skip to main content](https://exceljet.net/functions/choose-function#main-content)

[](https://exceljet.net/functions/choose-function#)

*   [Previous](https://exceljet.net/functions/areas-function)
    
*   [Next](https://exceljet.net/functions/column-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

CHOOSE Function
===============

by Dave Bruns · Updated 5 Jun 2021

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[IFS](https://exceljet.net/functions/ifs-function)

[SWITCH](https://exceljet.net/functions/switch-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")

Summary
-------

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

Purpose 
--------

Get a value from a list based on position

Return value 
-------------

The value at the given position.

Syntax
------

    =CHOOSE(index_num,value1,[value2],...)

*   _index\_num_ - The value to choose. A number between 1 and 254.
*   _value1_ - The first value from which to choose.
*   _value2_ - \[optional\] The second value from which to choose.

Using the CHOOSE function 
--------------------------

The CHOOSE function returns a value from a list using a given position or index. The values provided to CHOOSE can be hard-coded constants or cell references. The first argument for the CHOOSE function is _index\_num_. This is a number that refers to subsequent values by index or position. The next arguments, _value1_, _value2_, _value3_, etc. are the values from which to choose from. Choose can handle up to 254 values. However, CHOOSE will not retrieve an item from _inside_ range or array constant provided as a value.  For larger sets of data in a table or range,  [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 is a better way to retrieve a value based on position.

### Examples

The formulas below use CHOOSE to return the 2nd and 3rd values from a list:

    CHOOSE(2,"red","blue","green") // returns "blue"
    CHOOSE(3,"red","blue","green") // returns "green"
    

Above, "blue" is the second value, and "green" is the third value. In the example shown in the screenshot, the formula in cell C5 is:

    CHOOSE(B5,"red","blue","green") // returns "red"
    

CHOOSE will not retrieve values from a [range](https://exceljet.net/glossary/range)
 or [array constant](https://exceljet.net/glossary/array-constant)
. For example, the formula below will return a #VALUE error:

    =CHOOSE(2,A1:A3)  // returns #VALUE
    

This happens because the index number is out of range. In this case, the required syntax is:

    =CHOOSE(2,A1,A2,A3)
    

To retrieve the nth item from a range, use [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
. CHOOSE can be used to provide a variable table to a function like VLOOKUP:

    =VLOOKUP(value,CHOOSE(index_num,rng1,rng2),2,0) // variable table
    

### Notes

*   If _index\_num_ is out of range, CHOOSE will return #VALUE
*   Values can also be references. For example, the address A1, or the ranges A1:10 or B2:B15 can be supplied as values.
*   CHOOSE will not retrieve values from a [range](https://exceljet.net/glossary/range)
     or [array constant](https://exceljet.net/glossary/array-constant)
    .

CHOOSE function examples
------------------------

[![Excel formula: Random number from fixed set of options](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20from%20fixed%20set%20of%20options.png "Excel formula: Random number from fixed set of options")](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

### [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

The CHOOSE function does most of the work in this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are providing four...

[![Excel formula: Get previous Sunday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20previous%20Sunday.png "Excel formula: Get previous Sunday")](https://exceljet.net/formulas/get-previous-sunday)

### [Get previous Sunday](https://exceljet.net/formulas/get-previous-sunday)

In this example, the goal is to calculate the previous Sunday based on any given date. At a high level, this means we need to subtract some number of days from the given date. For example, if the given date is a Monday, we need to subtract 1 day. If the given date is a Tuesday, we need to subtract...

[![Excel formula: Number to words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/number_to_words.png "Excel formula: Number to words")](https://exceljet.net/formulas/number-to-words)

### [Number to words](https://exceljet.net/formulas/number-to-words)

In this example, the goal is to build a custom function that will convert a number like 123 into "One hundred twenty three" or "One hundred twenty three dollars" when currency is specified as USD. In addition, the formula should support multiple currencies and handle decimals. Traditionally, "...

[![Excel formula: INDEX with variable array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20with%20variable%20array.png "Excel formula: INDEX with variable array")](https://exceljet.net/formulas/index-with-variable-array)

### [INDEX with variable array](https://exceljet.net/formulas/index-with-variable-array)

At the core, this is a normal INDEX and MATCH function : =INDEX(array,MATCH(value,range,0)) Where the MATCH function is used to find the correct row to return from array, and the INDEX function returns the value at that array. However, in this case we want to make the array variable, so that the...

[![Excel formula: Custom weekday abbreviation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Custom%20weekday%20abbreviation.png "Excel formula: Custom weekday abbreviation")](https://exceljet.net/formulas/custom-weekday-abbreviation)

### [Custom weekday abbreviation](https://exceljet.net/formulas/custom-weekday-abbreviation)

Working from the inside-out, the WEEKDAY function takes a date and returns a number between 1 and 7. With default settings, the number 1 corresponds to Sunday and the number 7 corresponds to Saturday. The CHOOSE function simply maps numbers to values. The first argument is the number to map, and...

[![Excel formula: Map inputs to arbitrary values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20inputs%20to%20arbitrary%20values.png "Excel formula: Map inputs to arbitrary values")](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)

### [Map inputs to arbitrary values](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)

In this example, the goal is to map the numbers 1-6 to the arbitrary values seen in the table below. For example: If the input is 1, the output should be 10 If the input is 2, the output should be 81 If the input is 3, the output should be 17 If the input is 4, the output should be 23 And so on.....

[![Excel formula: Combine ranges with CHOOSE](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join%20ranges%20with%20choose.png "Excel formula: Combine ranges with CHOOSE")](https://exceljet.net/formulas/combine-ranges-with-choose)

### [Combine ranges with CHOOSE](https://exceljet.net/formulas/combine-ranges-with-choose)

In this example, the goal is to join two one-dimensional ranges together horizontally. This can be done with the CHOOSE function and array constant . The CHOOSE function The CHOOSE function is used to select arbitrary values by numeric position. CHOOSE is a flexible function and accepts a list of...

[![Excel formula: Get day name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20day%20name%20from%20date.png "Excel formula: Get day name from date")](https://exceljet.net/formulas/get-day-name-from-date)

### [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)

In this example, the goal is to get the day name (i.e. Monday, Tuesday, Wednesday, etc.) from a given date. There are several ways to go about this in Excel, depending on your needs. This article explains three approaches: Display date with a custom number format Convert date to day name with TEXT...

[![Excel formula: Get month name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20month%20name%20from%20date_0.png "Excel formula: Get month name from date")](https://exceljet.net/formulas/get-month-name-from-date)

### [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)

In this example, the goal is to get and display the month name from any given date. There are several ways to go about this in Excel, depending on whether you want to extract the month name as text, or just display a valid Excel using the month name. To extract the month name from a date as text ,...

[![Excel formula: VLOOKUP with multiple criteria advanced](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20multiple%20criteria%20advanced.png "Excel formula: VLOOKUP with multiple criteria advanced")](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)

### [VLOOKUP with multiple criteria advanced](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)

In this example, the goal is to use VLOOKUP to retrieve the price for a given item based on three criteria: name, size, and color, which are entered in H5:H7. For example, for a Blue Medium T-shirt, VLOOKUP should return $16.00. The VLOOKUP function does not handle multiple criteria natively...

[![Excel formula: Left lookup with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Look%20left%20with%20VLOOKUP.png "Excel formula: Left lookup with VLOOKUP")](https://exceljet.net/formulas/left-lookup-with-vlookup)

### [Left lookup with VLOOKUP](https://exceljet.net/formulas/left-lookup-with-vlookup)

One of the VLOOKUP function's key limitations is that it can only look up values to the right. In other words, the column that contains lookup values must sit to the left of the values you want to retrieve with VLOOKUP. There is no way to override this behavior since it is hardwired into the...

[![Excel formula: Get fiscal quarter from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20fiscal%20quarter%20from%20date.png "Excel formula: Get fiscal quarter from date")](https://exceljet.net/formulas/get-fiscal-quarter-from-date)

### [Get fiscal quarter from date](https://exceljet.net/formulas/get-fiscal-quarter-from-date)

The choose function uses the first argument to "select" remaining elements. For example, in a scheme where 1 = small, 2 = medium, and 3 = large, this formula will "map" the number 2 to "medium". =CHOOSE(2,"small","medium","large") In the case of fiscal quarters, we can use this same idea to map any...

[![Excel formula: VLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20case%20sensitive.png "Excel formula: VLOOKUP case-sensitive ")](https://exceljet.net/formulas/vlookup-case-sensitive)

### [VLOOKUP case-sensitive](https://exceljet.net/formulas/vlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on Color with VLOOKUP. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". This presents several challenges. First, Excel is not case-sensitive by default, and there is no built-in...

[![Excel formula: Rank with ordinal suffix](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20with%20ordinal%20suffix.png "Excel formula: Rank with ordinal suffix")](https://exceljet.net/formulas/rank-with-ordinal-suffix)

### [Rank with ordinal suffix](https://exceljet.net/formulas/rank-with-ordinal-suffix)

Ordinal numbers represent position or rank in a sequential order. They are normally written using a number + letter suffix: 1st, 2nd, 3rd, etc. To get an ordinal suffix for a small set of numbers, you can use the CHOOSE function like this: =CHOOSE(B5,"st","nd","rd","th","th","th","th","th","th","th...

[![Excel formula: Reverse VLOOKUP example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/reverse%20VLOOKUP%20example.png "Excel formula: Reverse VLOOKUP example")](https://exceljet.net/formulas/reverse-vlookup-example)

### [Reverse VLOOKUP example](https://exceljet.net/formulas/reverse-vlookup-example)

Introduction A key limitation of VLOOKUP is it can only look up values to the right . In other words, the column with lookup values must be to the left of the values you want to retrieve with VLOOKUP. As a result, with standard configuration, there is no way to use VLOOKUP to "look left" and...

CHOOSE function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20CHOOSE%20function-Thumb.png)](https://exceljet.net/videos/how-to-use-the-choose-function)

### [How to use the CHOOSE function](https://exceljet.net/videos/how-to-use-the-choose-function)

In this video we'll look at how you can use the CHOOSE function . Let's look at three examples. In this first example we have some items listed with a numeric color code. We want to bring these names into column D. Now, since I already have a table here, I could just use VLOOKUP and reference the...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel IFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ifs.png "Excel IFS function")](https://exceljet.net/functions/ifs-function)

### [IFS Function](https://exceljet.net/functions/ifs-function)

The Excel IFS function can run multiple tests and return a value corresponding to the first TRUE result. Use the IFS function to evaluate multiple conditions without multiple nested IF statements. IFS allows shorter, easier to read formulas....

[![Excel SWITCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20switch.png "Excel SWITCH function")](https://exceljet.net/functions/switch-function)

### [SWITCH Function](https://exceljet.net/functions/switch-function)

The Excel SWITCH function compares one value against a list of values, and returns a result corresponding to the first match found. When no match is found, SWITCH can return an optional default value....

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)
    
*   [VLOOKUP with multiple criteria advanced](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)
    
*   [Rank with ordinal suffix](https://exceljet.net/formulas/rank-with-ordinal-suffix)
    
*   [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)
    
*   [Reverse VLOOKUP example](https://exceljet.net/formulas/reverse-vlookup-example)
    
*   [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)
    
*   [Get previous Sunday](https://exceljet.net/formulas/get-previous-sunday)
    
*   [Number to words](https://exceljet.net/formulas/number-to-words)
    
*   [Get fiscal quarter from date](https://exceljet.net/formulas/get-fiscal-quarter-from-date)
    
*   [Dynamic calendar formula](https://exceljet.net/formulas/dynamic-calendar-formula)
    

### Videos

*   [How to use the CHOOSE function](https://exceljet.net/videos/how-to-use-the-choose-function)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [IFS Function](https://exceljet.net/functions/ifs-function)
    
*   [SWITCH Function](https://exceljet.net/functions/switch-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    

### Links

*   [Microsoft CHOOSE function documentation](https://support.office.com/en-us/article/choose-function-fc5c184f-cb62-4ec7-a46e-38653b98f5bc)
    

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