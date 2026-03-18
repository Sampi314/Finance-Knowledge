# INDEX MATCH INDEX

**Source:** https://sumproduct.com/thought/index-match-index/

---

[Home](https://sumproduct.com/)

\> INDEX MATCH INDEX

*   May 14, 2025

INDEX MATCH INDEX
=================

Has INDEX MATCH met its MATCH?.

Has INDEX MATCH Met Its MATCH?
==============================

We revisit one of the most powerful combinations of Excel functions for looking up data: INDEX and MATCH. By Liam Bastick, director (and Excel MVP) with SumProduct Pty Ltd.

### Query

I have read your previous article on using **INDEX(MATCH)** as a flexible way to lookup data in financial models, but what do you do when you have more than one criteria to look up? Can the idea be extended?

### Advice

I have discussed looking up data with combination **INDEX(MATCH)** before (please see the INDEX MATCH [\>article](https://www.sumproduct.com/thought/index-match)
). Probably the Lennon and McCartney of Excel combinations, I summarise them below again as a refresher.

### INDEX

Essentially, **INDEX(array, row\_num,\[column\_num\])** returns a value or the reference to a value from within a table or range (list).

For example, **INDEX({7,8,9,10,11,12},3)** returns the third item in the list {7,8,9,10,11,12}, i.e. 9. This could have been a range: **INDEX(A1:A10,5)** gives the value in cell **A5**, etc.

**INDEX** can work in two dimensions as well (hence the **column\_num** reference). Consider the following example:

### Two Dimensional INDEX Example

![](https://sumproduct.com/wp-content/uploads/2025/05/23322e9074ed46262908afccb5acec04.jpg)

**INDEX(F11:L21,4,5)** returns the value in the fourth row, fifth column of the table array **F11:L21** (clearly 26 in the above illustration).

### MATCH

**MATCH(lookup\_value,lookup\_array,\[match\_type\])** returns the relative position of an item in an array that (approximately) matches a specified value. It is not case sensitive.

The third argument, **match\_type**, does not have to be entered, but for many situations, I strongly recommend that it is specified. It allows one of three values:

*   **match\_type 1** \[default if omitted\]: finds the largest value less than or equal to the lookup\_value – but the **lookup\_array** must be in strict ascending order, limiting flexibility;
*   **match\_type 0:** probably the most useful setting, MATCH will find the position of the first value that matches lookup\_value exactly. The **lookup\_array** can have data in any order and even allows duplicates; and
*   **match type -1:** finds the smallest value greater than or equal to the lookup\_value – but the **lookup\_array** must be in strict descending order, again limiting flexibility.

When using **MATCH**, if there is no (approximate) match, #N/A is returned (this may also occur if data is not correctly sorted depending upon **match\_type**).

**MATCH** is fairly straightforward to use:

### MATCH Example

![](<Base64-Image-Removed>)

In the figure above, **MATCH(“d”,F12:F22,0)** gives a value of 6, being the relative position of the first ‘d’ in the range. Note that having **match\_type** 0 here is important. The data contains duplicates and is not sorted alphanumerically. Consequently, **match\_types** 1 and -1 would give the wrong answer: 7 and #N/A respectively.

### INDEX MATCH

As mentioned earlier, whilst useful functions in their own right, combined they form a highly versatile partnership. Consider the following common situation:

### Balance Sheet Summary Illustration

![](<Base64-Image-Removed>)

**MATCH(1,$J$18:$S$18,0)** equals 5, i.e. the first period the balance sheet does not balance in is Period 5. But we can do better than that.

**INDEX($J$12:$S$12,5)** equals 2020, so combining the two functions:

INDEX($J$12:$S$12,MATCH(1,$J$18:$S$18,0))

equals 2020 in one step. Note how flexible this combination really is. We do not need to specify an order for the lookup range, we can have duplicates and the value to be returned does not have to be in a row / column below / to the right of the lookup range (indeed, it can be in another workbook never mind another worksheet!).

However, this approach considers one criterion only (in the above example, ascertaining when the first misbalance occurs). What happens if there is more than one criteria? This can depend upon how the data is presented.

### Pivoted Data and INDEX MATCH MATCH

Pivoted data is when data is understood by cross-referencing criteria in two or more dimensions; in essence, the output is similar to results produced by a PivotTable. For example, consider the following illustration:

### Pivoted Multiple Criteria

![](<Base64-Image-Removed>)

In this example, I have constructed a formula to determine the costs for iGrapple, a new company probably in the throes of lots of copyright infringement battles if it really existed. The formula here uses **INDEX(MATCH,MATCH)** syntax, as it identifies the relevant row and column of the table to return.

The formula

\=INDEX($G$13:$I$19,MATCH($G$24,$F$13:$F$19,0),MATCH($G$25,$G$12:$I$12,0))

considers the range **$G$13:$I$19** and selects the row based on the result of **MATCH($G$24,$F$13:$F$19,0)**, which identifies which row iGrapple is in the range **$F$13:$F$19**, Further, the final argument selects the column based on **MATCH($G$25,$G$12:$I$12,0)**, i.e. which column ‘Costs’ is in, in the range **$G$12:$I$12**.

The intersection of the row and column selected returns the pivoted value.

### Unpivoted Data and INDEX MATCH INDEX

“Unpivoted” data is simply data in a tabular format, i.e. as required to be the source for an Excel PivotTable. Here, a value may be looked up in one of two ways. Consider the following example:

### Unpivoted Multiple Criteria

![](<Base64-Image-Removed>)

For those that know the following functions, **SUMIFS** or **SUMPRODUCT** would not work here as the field to be returned is non-numeric (i.e. of the form “ABCxxx”). The **INDEX(MATCH)** idea can be adopted though: it may be extended using arrays (see the Array of Light [Article](https://www.sumproduct.com/thought/array-of-light)
) such as

{=INDEX($I$13:$I$30,MATCH($G$35&$G$36&$G$37,$F$13:$F$30&$G$13:$G$30&$H$13:$H$30,0))}

which is entered using **CTRL+SHIFT+ENTER**, in order to generate the braces that surround the formula (these may not be typed manually).

The first argument, **$I$13:$I$30**, states where the lookup data should be retrieved from, whereas **MATCH** uses the **&** (ampersand) concatenation operator to combine the three criteria **($G$35&$G$36&$G$37)** to be matched against the three columns **$F$13:$F$30&$G$13:$G$30&$H$13:$H$30**. Note that these columns must also be concatenated: **$F$13:$H$30** will not work. This is because the **&** acts as a delimiter so that Excel understands which criterion is matched against which column.

There are problems with arrays. End users may not understand your array formulae. How many basic Excel users would understand the array formula explained above? Advanced users will all too often use an array function when there are simpler, easier to understand alternatives.

Large array formulae can slow down calculations significantly. Worse still, they can simply stop calculating with no error message provided. In conclusion, array formulae can be very powerful but they should be used sparingly.

With this borne in mind, there is an alternative solution:

### Unpivoted Multiple Criteria Revisited

![](<Base64-Image-Removed>)

This alternative formula,

\=INDEX($I$13:$I$30,MATCH($G$35&$G$36&$G$37,INDEX($F$13:$F$30&$G$13:$G$30&$H$13:$H$30,0),0))

is not an array formula, but implements almost the same logic. This is known as the **INDEX(MATCH(INDEX))** approach. In this instance, the final argument of the previous array formula has been replaced by

INDEX($F$13:$F$30&$G$13:$G$30&$H$13:$H$30,0).

This is a very crafty use of the **INDEX** function. **INDEX(Range,0)** is a way of referencing the whole **Range** in a formula without needing to enter the formula as an array formula. It is a neat trick to remember as it may be used time and time again in financial modelling to avoid creating array formulae unnecessarily.

### Word to the Wise

As usual, the examples are available to peruse in the [attached Excel file](https://sumproduct.com/assets/thought-files/has-index-match-met-its-match/sp---index-match-index-examples.xlsm)
. Where possible, do try to avoid these nested function monsters. **INDEX(MATCH,MATCH)** and **INDEX(MATCH(INDEX))** can often be simplified by simpler layouts and / or model structure. PivotTables may even be a viable alternative as well. Try to Keep It Simple Stupid (KISS).

If you wish to read more on INDEX and MATCH you can find another article [\>here](https://www.sumproduct.com/thought/index-match)
, otherwise please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/index-match-index/#0)
    
*   [Register](https://sumproduct.com/thought/index-match-index/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/index-match-index/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/index-match-index/#0)

[](https://sumproduct.com/thought/index-match-index/#0 "close")

top