# How to use formula criteria (50 examples) | Exceljet

**Source:** https://exceljet.net/articles/how-to-use-formula-criteria

---

[Skip to main content](https://exceljet.net/articles/how-to-use-formula-criteria#main-content)

[](https://exceljet.net/articles/how-to-use-formula-criteria#)

*   [Previous](https://exceljet.net/articles/101-excel-functions)
    
*   [Next](https://exceljet.net/articles/excel-shows-formula-not-result)
    

How to use formula criteria (50 examples)
=========================================

by Dave Bruns · Updated 11 May 2024

![Things to know about formula criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/Things_to_know_about_formula_criteria.jpeg "Things to know about formula criteria")

Summary
-------

Criteria are a key concept in Excel, but building useful criteria for text, numbers, dates, times, etc. is hard because it requires a good understanding of how Excel handles data. This guide will help you build formulas that work the first time with over 50 examples.

One of the most important skills for building formulas is creating _criteria_ – the part of a formula that decides what to include or exclude in a calculation. However, it can be surprisingly tricky to build effective criteria because it requires a good understanding of how Excel handles data. If you've ever spent an afternoon troubleshooting a formula that seems like it should "just work", you know what I mean :)

This guide aims to help you build formulas that work the _first_ time.

_Note: language mavens will point out that "criterion" is singular and "criteria" is plural, but I'm going to use "criteria" in both cases to keep things simple._

> Function names on dark backgrounds below are links to more information.

What do criteria do?
--------------------

Among other things, criteria:

*   Direct logical flow with IF/THEN logic
*   Restrict processing to matching values only
*   Create conditional sums and counts
*   Filter data to exclude irrelevant information
*   Trigger conditional formatting rules

To help set the stage, let's look at three examples of criteria in action.

### Example #1

In the screen below, F3 contains this formula:

    =IF(E3>30,"Yes","No")
    

![Formula criteria example #1](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/formula%20criteria%20example%201.png?itok=janqpmAK "Formula criteria example #1")

_Translation: If the value in E3 is greater than 30, return "Yes", otherwise return "No"._

Here, E3>30 is the criteria, used inside IF to determine if the formula should return "Yes" or "No" for each invoice.

### Example #2

In the next example, D3 contains this formula:

    =IF(OR(B3="red",B3="green"),C3*1.1,C3)
    

![Formula criteria example #2 - increase price if red or green](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/formula%20criteria%20example%202.png?itok=QdhGD6Ee "Formula criteria example #2 - increase price if red or green")

_Translation: if B3 is either "red" or "green", increase the price by 10%. Otherwise, return the original price._

### Example #3

In this example, the SUMIFS function is used to sum the total only when the color is "red":

    =SUMIFS(E3:E7,B3:B7,"red")
    

![Formula criteria example #2 - SUMIF when color is "red"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/formula%20criteria%20example%203.png?itok=qbFid8fV "Formula criteria example #2 - SUMIF when color is "red"")

_Translation: sum values in E3:E7 when the value in B3:B7 is "red"._

Criteria Basics
---------------

This section covers the building blocks of formula criteria and some simple ways to verify that criteria are performing as expected. 

### What are criteria?

Criteria are logical expressions that return TRUE or FALSE, or their numerical equivalents, 1 or 0.

That's it.

The trick is to construct criteria in a way so that they only return TRUE when the test meets your exact criteria. In all other cases, criteria should return FALSE or zero. If you can master this one idea, you have the foundation to build and understand many advanced formulas.

### Logical operators

Criteria often make use of the logical operators listed in the table below.

| Operator | Meaning | Example |
| --- | --- | --- |
| \=  | Equal to | \=A1=10 |
| <>  | Not equal to | \=A1<>10 |
| \>  | Greater than | \=A1>100 |
| <   | Less than | \=A1<100 |
| \>= | Greater than or equal to | \=A1>=75 |
| <=  | Less than or equal to | \=A1<=0 |

Logical operators can be combined in various ways, as seen in the examples below.

### Logical functions

Excel has several so-called "logical functions" that can be used to construct and utilize conditions. The table below lists the key logical functions.

| Function | Purpose |
| --- | --- |
| [IF](https://exceljet.net/functions/if-function) | Test one condition; direct logical flow |
| [IFS](https://exceljet.net/functions/ifs-function) | Test multiple conditions; direct logical flow |
| [NOT](https://exceljet.net/functions/not-function) | Reverse criteria or results |
| [AND](https://exceljet.net/functions/and-function) | Test multiple conditions, return TRUE if all are TRUE |
| [OR](https://exceljet.net/functions/or-function) | Test multiple conditions, return TRUE if at least one is TRUE |
| [XOR](https://exceljet.net/functions/or-function) | Exclusive OR – return TRUE if one or the other, not both |
| [IFERROR](https://exceljet.net/functions/iferror-function) | Trap errors and return alternative results |

### Multiple criteria

Naturally, there are many cases where you will want to use multiple criteria. In simple situations, you can use the AND, OR, and NOT functions. Here are a few examples:

    =AND(A1>0,A1<10) // greater than 0 and less than 10
    =OR(A1="red",A1="blue") // red or blue
    =NOT(OR(A1="red",A1="blue")) // not red or blue
    =AND(ISNUMBER(A1),A1>100) // number greater than 100
    

### Wildcards

Excel provides three "wildcards" for matching text in formulas:

| Character | Name | Purpose |
| --- | --- | --- |
| \*  | Asterisk | Match zero or more characters |
| ?   | Question mark | Match any one character |
| ~   | Tilde | Match literal wildcard |

Wildcards can be used alone or combined to get a variety of matching behaviors:

| Usage | Behavior | Will match |
| --- | --- | --- |
| ?   | Any one character | "A", "B", "c", "z", etc. |
| ??  | Any two characters | "AA", "AZ", "zz", etc. |
| ??? | Any three characters | "Jet", "AAA", "ccc", etc. |
| \*  | Any characters | "apple", "APPLE", "A100", etc. |
| \*th | Ends in "th" | "bath", "fourth", etc. |
| c\* | Starts with "c" | "Cat", "CAB", "cindy", "candy", etc. |
| ?\* | At least one character | "a", "b", "ab", "ABCD", etc. |
| ???-?? | 5 characters with a hyphen | "ABC-99","100-ZT", etc. |
| \*~? | Ends with a question mark | "Hello?", "Anybody home?", etc. |
| \*xyz\* | Contains "xyz" | "code is XYZ", "100-XYZ", "XyZ90", etc. |

Here are a few examples of using wildcards for criteria in the COUNTIFS function.

    =COUNTIFS(A1:A100,"*red*") // count cells that contain "red"
    =COUNTIFS(A1:A100, "www*") // count cells starting with "www"
    =COUNTIFS(A1:A100,"?????") // count cells with 5 characters
    

Not all functions allow wildcards. Here is a list of common functions that do:

*   [AVERAGEIF](https://exceljet.net/functions/averageif-function)
    , [AVERAGEIFS](https://exceljet.net/functions/averageifs-function)
    
*   [COUNTIF](https://exceljet.net/functions/countif-function)
    , [COUNTIFS](https://exceljet.net/functions/countifs-function)
    
*   [SUMIF](https://exceljet.net/functions/sumif-function)
    , [SUMIFS](https://exceljet.net/functions/sumifs-function)
    
*   [VLOOKUP](https://exceljet.net/functions/vlookup-function)
    , [HLOOKUP](https://exceljet.net/functions/hlookup-function)
    
*   [MATCH](https://exceljet.net/functions/match-function)
    
*   [SEARCH](https://exceljet.net/functions/search-function)
    

Notice the IF function is _not_ on this list. To get wildcard behavior with IF, you can combine the SEARCH and ISNUMBER functions, as described below.

### Testing criteria

The classic way to test criteria is to wrap them in the IF function. For example, to check for "red" or "blue", we can wrap the OR function inside IF like this:

    =IF(OR(B3="red",B3="blue"),"OK", "")
    

![Formula criteria - testing with IF function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/formula%20criteria%20testing%201.png?itok=J2eFlBKC "Formula criteria - testing with IF function")

_Translation: if the color is "red" or "blue", return "OK". Otherwise, return nothing._

However, you can also test criteria directly on the worksheet as a formula. Let's say you want to process values that are 80 and higher. In the screen below, C3 contains this formula, copied down. 

    =B3>=80
    

![Formula criteria - testing directly on worksheet](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/formula%20criteria%20testing%202.png?itok=z75VeCkn "Formula criteria - testing directly on worksheet")

_Translation: the value in B3 is greater than or equal to 80._

Without IF or another function, we only get a result of TRUE or FALSE, but it's enough to verify criteria are working as expected.

Don't be thrown off by the equals (=) sign when testing criteria as a formula. All Excel formulas must begin with an equals sign, so it must be included. Remove the equal sign when you move criteria into another formula.

Another way to test criteria is to use F9 to evaluate the criteria in place. Just carefully select a logical expression, and press F9. Excel will immediately evaluate the expression and display the result.

Video: [How to use F9 to debug a formula](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
.

### Adding criteria to formulas

Of course, in most cases, you don't want to return TRUE or FALSE to a cell, you want to return some other value based on criteria returning TRUE or FALSE. To do that, just remove the equal sign and add the criteria where needed in the formula.

In the example below, the formula C3 contains this formula, which uses the criteria above as the logical test inside IF:

    =IF(B3>=80,"Pass","Fail")
    

![Adding criteria to a formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/adding%20criteria%20to%20formula.png?itok=obwDBt_W "Adding criteria to a formula")

_Translation: if the value in B3 is greater than or equal to 80, return "Pass". Otherwise, return "Fail"._

> See also: 23 tips for formulas ([video](https://exceljet.net/videos/23-excel-formula-tips)
>  | [article](https://exceljet.net/articles/29-ways-to-save-time-with-excel-formulas)
> )

Criteria Examples
-----------------

This section shows examples of how to build criteria to accomplish a variety of tasks for different kinds of content.

### Blank or not blank

There are several ways you can check for blank or non-blank cells. To return TRUE if A1 is blank, you can use either:

    =ISBLANK(A1)
    =A1=""
    

To reverse the logic and check for non-blank cells, you can use:

    =NOT(ISBLANK(A1))
    =A1<>""
    

Another way to test for a blank cell is to count characters:

    =LEN(A1)=0
    

If the count is zero, the cell is "blank". This formula is useful when testing cells that may contain formulas that return empty strings (""). ISBLANK(A1) will return FALSE if a formula returns an empty string in A1, but LEN(A1)=0 will return TRUE.

### Criteria for text

To return TRUE if a cell contains "red", you can use:

    =A1="red" 
    

To reverse logic, you can use the NOT function or the "not equals to" operator (<>) like this:

    =NOT(A1="red")
    =A1<>"red"
    

Notice in each case the text IS enclosed in double quotes (e.g. "red"). If you don't use quotes, Excel will think you are trying to reference a named range or a function and will return the #NAME error.

### Criteria for numbers

To test if A1 is equal to 5, you can use criteria like this:

    =A1=5 // TRUE if A1 equals 5
    

Here are some other examples of criteria to test numeric values:

    =A1<100 // less than 100
    =A1>=1 // greater than or equal to 1
    =A1<>0 // not equal to zero
    =AND(A1>0,A1<5) // greater than zero, less than 5
    =MOD(A1,3)=0 // value is a multiple of 3
    

Notice numbers are NOT enclosed in double quotes. If you enclose a number in quotes, you are telling Excel to treat the number as text, which will make the criteria useless. Also, remember that [number formatting](https://exceljet.net/articles/custom-number-formats)
 in Excel affects display only, and does not change numeric data in any way. Do not include dollar signs ($), percent signs (%), or other formatting information when building criteria to test numbers.

### Criteria for dates

Dates in Excel are just numbers, which means you are free to use ordinary math operations on dates if you like. With Order dates in column A and Delivery dates in column B,  this formula in column C will mark delivery times greater than 3 days as "late":

    =IF((B2-A2)>3,"Late","")
    

Excel also provides a large number of specific functions for working with dates. For example, to check if a date is "in the future" you can use the TODAY function like this:

    =A1>TODAY()
    

![Formula criteria date example - greater than today](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/formula%20criteria%20date%20example.png?itok=CO8Fh4P5 "Formula criteria date example - greater than today")

To check if a date occurs in the next 30 days, the formula can be extended to:

    =AND(A1>TODAY(),A1<=(TODAY()+30))
    

_Translation: IF A2 is greater than today AND less than or equal today + 30 days, return TRUE._

Here are a few other examples of criteria for dates, assuming A1 contains a valid date:

    =DAY(A1)>15 // greater than 15th
    =MONTH(A1)=6 // month is June
    =YEAR(A1) = 2019 // year is 2019
    =WEEKDAY(A1)=2 // date is a Monday
    

The safest way to insert a valid date into criteria is to use the DATE function, which accepts _year_, _month_, and _day_ as separate arguments. Here are a couple of examples:

    =A1>DATE(2019,1,1) // after Jan. 1, 2019
    =AND(A1>=DATE(2018,6,1),B4<=DATE(2018,8,31)) // Jun-Aug 2018
    

### Criteria for times

Times are fractional numbers in Excel, so you can use simple math for time in some cases. For example, to check if a time in A1 is after 12:00 PM (more than 12 hours), you can use:

    =A1>.5
    

This works because 1 day = 24 hours, so a half day = 12 hours.

For more granular work, Excel has special functions to extract time by component. For example, with the time 8:45 AM in cell A1:

    =HOUR(A1) // returns 8
    =MINUTE(A1) // returns 45
    =SECOND(A1) // returns 0
    

The safest way to insert a time in criteria is to use the TIME function. Here are some examples:

    =A1>TIME(9,15,0) // after 9:15 AM
    =AND(A1>=TIME(9,0,0),A1<=TIME(17,0,0)) // 9 AM to 5 PM
    

### Criteria for SUMIFS, COUNTIFS, etc.

The criteria for SUMIFS, COUNTIFS, AVERAGEIFS, and similar range-based functions follow slightly different rules. This is because the criteria are split into two parts (criteria range and criteria), and this impacts the syntax when criteria include operators.

Simple criteria based on equality don't need special handling. The equals (=) operator is implied, so there's no need to include it:

    =COUNTIFS(A1:A100,10) // count cells equal to 10
    =COUNTIFS(A1:A100,"red") // count cells that equal "red"
    

 However, things change when we add operators:

    =COUNTIFS(A1:A100,">10") // count cells greater than 10
    =COUNTIFS(A1:A100,"<0") // count cells less than zero
    

Notice the quotes ("") around the criteria? These are required when criteria include an operator in these functions.

### Criteria for data types

Excel allows three main data types: text, numbers, and logicals. Dates, times, percentages, and fractions are all just numbers with [number formatting](https://exceljet.net/articles/custom-number-formats)
 applied to change the way they are displayed. By default, numbers are right-aligned, text is left-aligned, and logical values are centered. However a user can override alignment manually, so this is not a good test of type.

Excel provides three functions you can use to check data types: ISTEXT, ISNUMBER, and ISLOGICAL. These functions return TRUE or FALSE. In the screen below, the cells D3, F3, and H3 contain these formulas, copied down:

    =ISTEXT(B3)
    =ISNUMBER(B3)
    =ISLOGICAL(B3)
    

![Formula criteria - using functions to test data types](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/formula%20criteria%20for%20data%20types.png?itok=2W2k9I4x "Formula criteria - using functions to test data types")

To use these functions as criteria, just place them in the correct location of a formula. For example, to check if A1 contains a number, you can use ISNUMBER as the logical test inside IF like this:

    =IF(ISNUMBER(B3),"OK","Invalid")
    

Note: Formulas are not a data type, but you can check for formulas with the [ISFORMULA function](https://exceljet.net/functions/isformula-function)
:

    =ISFORMULA(A1) // TRUE if A1 contains formula
    

Getting fancy
-------------

The examples above show the fundamentals of using criteria in formulas, there are many ways to make criteria more sophisticated. This section explores a few techniques.

### Making criteria variable

It is often useful to make criteria variable, by referencing a cell on the worksheet. For example, in the worksheet below, the passing score is in cell E3, and the formula to determine pass or fail looks like this:

    =IF(B3>=$E$3,"Pass","Fail")
    

![Making criteria variable - test score example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/making%20criteria%20variable%201.png?itok=oqZqdWxh "Making criteria variable - test score example")

Placing the passing score in cell E3 makes it easy to change at any time without editing formulas. Note that the reference to $E$3 is [absolute](https://exceljet.net/glossary/absolute-reference)
 to prevent changes as the formula is copied down.

### Making criteria variable in COUNTIFS, SUMIFS, etc.

As before, if criteria are testing for equality, no special handling is needed:

    =COUNTIF(range,A1) // count cells equal to A1
    

However, if criteria include operators, you will need to use [concatenation](https://exceljet.net/glossary/concatenation)
. For example, to count cells _greater than_ A1, join ">" to "A1" like this:

    =COUNTIF(range,">"&A1)
    

The concatenation runs first. If A1 contains the number 10, this is the formula after concatenation:

    =COUNTIF(range,">10")
    

Notice the pattern is the same as explained earlier – if criteria includes operators, it must appear in quotes ("").

Here are more examples of using concatenation in criteria:

    =COUNTIF(range,"<"&B1) // count less than value in B1
    =COUNTIF(range,"<>"&"") // count not blank cells
    =COUNTIF(range,"*"&B1&"*") // count contains text in B1
    =COUNTIF(range,">"&TODAY()) // count dates in future
    =COUNTIF(range,"<"&TODAY()+7) // count up to 7 days from today
    

### Contains specific text

One tricky situation is when you want to test if a cell _contains_ specific text. For functions that support wildcards (like COUNTIFS, SUMIFS, etc.), you can use wildcards to do this. For example, to count cells that contain "red" anywhere in a cell with COUNTIFS, you can use an asterisk like this:

    =COUNTIFS(A1:A100,"*red*")
    

However, many other functions (like the IF function) don't support wildcards. In that case, you can combine ISNUMBER and SEARCH to create logic that checks a cell for a partial match. In the screen below, D3 contains this formula:

    =ISNUMBER(SEARCH(C3,B3))
    

![Formula criteria - cell contains specific text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/formula%20criteria%20cell%20contains%20specific%20text.png?itok=DuArFUnf "Formula criteria - cell contains specific text")

You can use this expression as criteria inside IF like this

    =IF(ISNUMBER(SEARCH("red",A1)),"red", "")
    

_Translation: if "red" is found anywhere in A1, return "red"._

This works because SEARCH returns a numeric position if "red" is found, and ISNUMBER returns TRUE. If not, SEARCH returns an error, and ISNUMBER returns FALSE. For more details, see [this page](https://exceljet.net/formulas/cell-contains-specific-text)
.

### Nested IFs

Nested IF formulas are often used to check multiple criteria and return multiple results. In general, the challenge is to build nested IFs so that the criteria appear in the right sequence. For example, here is a nested IF formula that assigns a letter grade based on a numeric score:

    =IF(C5<64,"F",IF(C5<73,"D",IF(C5<85,"C",IF(C5<95,"B","A"))))
    

![Nested IF example for assigning grades](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/nested%20IF%20example%20for%20grades.png?itok=L--mWzrE "Nested IF example for assigning grades")

Notice we are testing for low scores first, then progressively higher scores.

More: [19 tips for nested IFs](https://exceljet.net/articles/nested-ifs)
 (with alternatives)

### Array constants in criteria

Array constants are hard-coded arrays with fixed values like this: {"A","B","C"}. They can sometimes be used as criteria to create simple OR logic criteria. For example, in the screen below, cell F4 contains this formula:

    =SUM(SUMIFS(C3:C7,B3:B7,{"red","gold"}))
    

![Formula criteria with array constants](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/formula%20criteria%20with%20array%20constants.png?itok=cygjlNzG "Formula criteria with array constants")

_Translation: SUM sales where the color is "red" OR "gold"._

Because we give SUMIFS two values for criteria, it returns two results. The SUM function then returns the sum of the two results.

### Simple array formula criteria

Array formulas are a complicated topic, but the criteria for simple array formulas can be quite simple. A classic example is using the IF function to "filter out" values that should be excluded, and then processing the result with another function.

In the screen below, the formula in G4 is:

    {=MAX(IF(regions=F4,totals))}
    

where **regions** is the [named range](https://exceljet.net/glossary/named-range)
 B3:B8 and **totals** is the named range D3:D8.

_Note: this is an array formula and must be entered with control + shift + enter._

The result is the top value for each region.

![Formula criteria for simple array formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/making%20criteria%20simple%20array%20formula.png?itok=j-Gtja0H "Formula criteria for simple array formula")

For criteria, we use the expression:

    regions=F4
    

This compares all region values with "West" from F4, and returns the following array result in the logical test for IF:

    {TRUE;FALSE;TRUE;FALSE;TRUE;FALSE}
    

The final array returned by IF looks like this:

    {10500;FALSE;12500;FALSE;11800;FALSE}
    

Only values associated with the "West" region make it into the array. Values associated with the "East" region are FALSE.

The MAX function then returns the largest value in the array, ignoring all FALSE values.

Advanced formula criteria
-------------------------

Below are links to more advanced formula criteria examples. Each link has a screenshot and a full explanation.

*   [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)
    
*   [Sum if value is equal to one of many](https://exceljet.net/formulas/sum-if-one-of-many-things)
    
*   [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
    
*   [Get nth largest value with criteria](https://exceljet.net/formulas/nth-largest-value-with-criteria)
    
*   [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)
    
*   [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
    

### More formula resources

The following links contain more detailed information on Excel formulas:

*   [How to build logical formulas](https://exceljet.net/plc/how-to-build-logical-formulas)
     (video)
*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    
*   [30+ conditional formatting formulas](https://exceljet.net/conditional-formatting-formulas)
    
*   [Core Formula (paid training)](https://exceljet.net/training/core-formula)
    

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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