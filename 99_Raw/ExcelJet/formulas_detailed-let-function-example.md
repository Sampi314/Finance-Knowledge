# Detailed LET function example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/detailed-let-function-example

---

[Skip to main content](https://exceljet.net/formulas/detailed-let-function-example#main-content)

[](https://exceljet.net/formulas/detailed-let-function-example#)

*   [Previous](https://exceljet.net/formulas/count-unique-values-with-criteria)
    
*   [Next](https://exceljet.net/formulas/distinct-values)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Detailed LET function example
=============================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[LET](https://exceljet.net/functions/let-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[IF](https://exceljet.net/functions/if-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6929/download?token=Q7NRdhcS)
 (14.56 KB)

![Excel formula: Detailed LET function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/let%20function%20example.png "Excel formula: Detailed LET function example")

Summary
-------

The LET function can simplify certain formulas by making it possible to define and reuse variables. In the example shown, the [LET function](https://exceljet.net/functions/let-function)
 is used to define two variables: _name_ and _points_. The formula in G6 is:

    =LET(
    name,VLOOKUP(G5,B5:D16,2,0),
    points,VLOOKUP(G5,B5:D16,3,0),
    "Hi, "&name&", you have "&points&" points."&IF(points>300," Great job, "&name&"!",""))
    

When a different ID is typed into cell G5, the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 retrieves a new name and points from the data in B5:D16.

_Note: the LET function is new in [Excel 365](https://exceljet.net/glossary/excel-365)
. It's part of the new [dynamic array functions](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 in Excel._

Explanation 
------------

In this example, we have a simple set of data in B5:D16 that includes ID, Name, and Points. The goal is to generate a custom message for any name in the list by entering a valid ID in cell G5. The message uses the name from column C and the points in column D like this:

    "Hi [name], you have [points] points."
    

If points are over 300, the message is extended:

    "Hi [name], you have [points] points. Great job, [name]!"
    

In the article below, we'll build up the formula step-by-step, and then streamline the final formula with the [LET function](https://exceljet.net/functions/let-function)
.

### Concatenation

This formula uses [concatenation](https://exceljet.net/glossary/concatenation)
, which means joining values to form [text strings](https://exceljet.net/glossary/text-value)
. For example, with the number 100 in cell A1, we can use concatenation to write a formula like this:

    ="You have "&A1&" points."
    

which returns this text string:

    "You have 100 points"
    

_Note: Excel has several functions for concatenation including [CONCAT](https://exceljet.net/functions/concat-function)
 and [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
, but I generally prefer to use the ampersand (&) [operator](https://exceljet.net/glossary/math-operators)
 for this kind of problem._

### The lookups

The initial task is to use a numeric ID to look up the name and points. To keep things simple, we're going to use VLOOKUP like this:

    =VLOOKUP(G5,B5:D16,2,0) // look up name
    =VLOOKUP(G5,B5:D16,3,0) // look up points
    

With a valid ID in G5, VLOOKUP will retrieve a name and corresponding points. For more on VLOOKUP, see [the detailed overview here](https://exceljet.net/functions/vlookup-function)
. At the end of the article, we look at how to replace VLOOKUP with [XLOOKUP](https://exceljet.net/functions/xlookup-function)
.

### Formula without LET

Next, we need to concatenate the name and points we looked up in the final message. The first part of the message looks like this:

    ="Hi, "&VLOOKUP(G5,B5:D16,2,0)&", you have "&VLOOKUP(G5,B5:D16,3,0)&" points."
    

So far, so good. If we type the number 131 into G5, we get:

    ="Hi, "&"Finn"&", you have "&"342"&" points!"
    

which evaluates to a final result of:

    "Hi, Finn, you have 342 points!"
    

We now have the first part of the message completed. The second part is conditional. If points are greater than 300, then we add:

    "Great job, [name]!"
    

If points are _not_ greater than 300, we add nothing. We can do this with the [IF function](https://exceljet.net/videos/the-if-function)
 together with VLOOKUP like this:

    =IF(VLOOKUP(G5,B5:D16,3,0)>300," Great job, "&VLOOKUP(G5,B5:D16,2,0)&"!","")
    

Here again, we use VLOOKUP to fetch both points and name. Starting on the left, we first check if points are greater than 300:

    =IF(VLOOKUP(G5,B5:D16,3,0)>300 // check points
    

If not, we just return an [empty string](https://exceljet.net/glossary/empty-string)
 (""). If points _are_ greater than 300, we build part 2:

    "Great job, "&VLOOKUP(G5,B5:D16,2,0)&"!"
    

When the id is 131, VLOOKUP returns "Finn" and we get the following text string:

    "Great job, Finn!"
    

Finally, we need to join the first part of the message to the second part. The final formula is:

    ="Hi, "&VLOOKUP(G5,B5:D16,2,0)&", you have "&VLOOKUP(G5,B5:D16,3,0)&" points."&IF(VLOOKUP(G5,B5:D16,3,0)>300," Great job, "&VLOOKUP(G5,B5:D16,2,0)&"!","")
    

This formula works fine, but it's getting a bit unwieldy. Notice we have four separate calls to VLOOKUP, and two of the four are exact duplicates:

![Original formula without LET function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/original%20formula%20without%20LET%20function.png?itok=drDBU342 "Original formula without LET function")

Let's use the LET function to slim down and simplify this formula.

### Thinking about variables

To use the LET function, we need to think about _variables_. The main purpose of variables is to define a useful name that can be reused elsewhere in the formula code. In addition, when the value assigned to a variable is _calculated_, there is an opportunity to improve performance by reducing the number of times the calculation is performed. Using a variable also has the advantage of keeping a calculation in one place only, which reduces errors and the editing needed to keep multiple copies in sync.

Looking at the formula above, there are two obvious places where a named variable makes sense: the lookup for _name_, and the lookup for _points_. Both of these lookups appear twice in the formula, so this is a good opportunity to simplify.

### Implementing LET

The basic pattern for implementing LET with two variables looks like this:

    =LET(name1,value1,name2,value2,result)
    

Notice names and values appear in pairs – we declare _name1_ and assign _value1_, then we declare _name2_ and assign _value2_. Lastly, we add a _result_. The result is the final result returned by LET. This is typically a calculation, adjusted to use the declared variables.

In this case, we'll use "name" for _name1_, and "points" for _name2_. To assign values to each variable, we'll use the VLOOKUP function configured as shown below:

    =VLOOKUP(G5,B5:D16,2,0) // look up name
    =VLOOKUP(G5,B5:D16,3,0) // look up points
    

Putting this into the LET function, we begin like this:

    =LET(name,VLOOKUP(G5,B5:D16,2,0),points,VLOOKUP(G5,B5:D16,3,0),
    

This defines the variables "name" and "points" and assigns values to both, based on the id in cell G5. Next, we need to add the calculation that determines a final result. We'll start with the original formula above:

    ="Hi, "&VLOOKUP(G5,B5:D16,2,0)&", you have "&VLOOKUP(G5,B5:D16,3,0)&" points."&IF(VLOOKUP(G5,B5:D16,3,0)>300," Great job, "&VLOOKUP(G5,B5:D16,2,0)&"!","")
    

We could use this formula as-is, and it would run correctly, but it would defeat the purpose of using the LET function. To take advantage of LET, we need to replace the VLOOKUPs with the variables we've already declared, like this:

    ="Hi, "&name&", you have "&points&" points."&IF(points>300," Great job, "&name&"!","")
    

Now we need to add this code to the LET function as the last argument:

    =LET(name,VLOOKUP(G5,B5:D16,2,0),points,VLOOKUP(G5,B5:D16,3,0),"Hi, "&name&", you have "&points&" points."&IF(points>300," Great job, "&name&"!",""))
    

This formula will return the same result as the original formula, but notice we only use VLOOKUP twice, instead of four times, and the calculation part of the formula is somewhat easier to read since we are using _name_ and _points_ as variables.

To improve readability, we can add [line breaks](https://exceljet.net/shortcuts/insert-line-break-in-cell)
 (Alt + enter) like this:

    =LET(
    name,VLOOKUP(G5,B5:D16,2,0),
    points,VLOOKUP(G5,B5:D16,3,0),
    "Hi, "&name&", you have "&points&" points."&IF(points>300," Great job, "&name&"!",""))
    

You will see formatting like this frequently in formulas that use the LET function because it makes the formula easier to read, write, and edit. Here is the result in Excel. I've added one additional line break between part 1 and part 2 to keep everything on screen:

![Converted formula with LET and line breaks](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/converted%20formula%20with%20LET%20and%20line%20breaks.png?itok=GgQ3eqsc "Converted formula with LET and line breaks")

_Note: you'll need to [expand the formula bar](https://exceljet.net/videos/shortcuts-for-formulas)
 (control + shift + u) to see extra lines._

### More readability

You are free to add more variables to LET if it helps you work with the formula more efficiently. For example, we could break the message into two parts, _part1_ and _part2_, then join them together at the end like this:

    =LET(
    name,VLOOKUP(G5,B5:D16,2,0),
    points,VLOOKUP(G5,B5:D16,3,0),
    part1,"Hi, "&name&", you have "&points&" points.",
    part2,IF(points>300," Great job, "&name&"!",""),
    part1&part2)
    

This alternative won't run any faster, but it can make the formula easier to read and create.

### With XLOOKUP

One nice thing about LET is that it isolates calculation steps in a way that makes them easier to change. For example, although we've been using VLOOKUP to retrieve the _name_ and _points_ values we need, we can easily swap out VLOOKUP for XLOOKUP like this:

    =LET(
    name,XLOOKUP(G5,B5:B16,C5:C16),
    points,XLOOKUP(G5,B5:B16,D5:D16),
    part1,"Hi, "&name&", you have "&points&" points.",
    part2,IF(points>300," Great job, "&name&"!",""),
    part1&part2)
    

Notice we only changed the way _name_ and _points_ are defined. The rest of the formula did not change. Here is what this formula looks like in Excel with the formula bar expanded:

![Example of LET function with XLOOKUP](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/example%20of%20let%20function%20with%20xlookup.png?itok=8yYTWQ8M "Example of LET function with XLOOKUP")

Related formulas
----------------

[![Excel formula: List upcoming birthdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20upcoming%20birthdays.png "Excel formula: List upcoming birthdays")](https://exceljet.net/formulas/list-upcoming-birthdays)

### [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)

In this example, the goal is to list the next n upcoming birthdays from a larger set of 25 birthdays based on the current date. The set of birthdays are in an Excel Table named data in the range B5:C29. In the example shown, we are using 7 for n , so the result will be the next 7 upcoming birthdays...

[![Excel formula: LAMBDA strip characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20strip%20characters.png "Excel formula: LAMBDA strip characters")](https://exceljet.net/formulas/lambda-strip-characters)

### [LAMBDA strip characters](https://exceljet.net/formulas/lambda-strip-characters)

This is an experimental formula to strip characters from text. The experimental part is using character codes instead of regular characters as a way to make the formula case-sensitive, and providing a way to reverse the logic of the formula with the "keep" input parameter. Unlike the formula...

[![Excel formula: Get days, months, and years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20months%20and%20years%20between%20dates.png "Excel formula: Get days, months, and years between dates")](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

### [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

In this example, the goal is to output the time between a start date and an end date as a text string that lists years, months, and days separately. For example, given a start date of 1-Jan-2018 and an end date of 1-Jul-2018, the result should be a string like this: "1 years, 6 months, 0 days"...

Related functions
-----------------

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)
    
*   [LAMBDA strip characters](https://exceljet.net/formulas/lambda-strip-characters)
    
*   [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
    

### Functions

*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

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