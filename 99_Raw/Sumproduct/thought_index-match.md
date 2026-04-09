# INDEX MATCH

**Source:** https://sumproduct.com/thought/index-match/

---

[Home](https://sumproduct.com/)

\> INDEX MATCH

*   May 14, 2025

INDEX MATCH
===========

Consideration of one of the most powerful combinations of functions for Excel modelling.

Are Things LOOKing UP for INDEX and MATCH?
==========================================

This feature considers one of the most powerful combinations of Excel functions for looking up data: INDEX and MATCH. By Liam Bastick, director with SumProduct Pty Ltd.

Query
-----

Preparing financial statements in Excel, I want to construct a formula that will tell me if my Balance Sheet is balancing, and, if not, which is the first period that the misbalance occurs in.

![](<Base64-Image-Removed>)

Balance Sheet Summary Illustration

Advice
------

This is a common modelling query. The usual suspects, LOOKUP and HLOOKUP / VLOOKUP do not work here:

*   **LOOKUP(lookup\_value, lookup\_vector,\[result\_vector\])** gives the wrong date as the balance checks are not in **strict** ascending order (i.e. ascending alphanumerically with no duplicates); whilst
*   **HLOOKUP(lookup\_value,table\_array,row\_index\_num,\[range\_lookup\])** gives #VALUE! since the first row must contain the data to be ‘looked up’, but the Balance Check is in row 28 in our example above, whereas the dates we need to return are in row 6 – hence we get a syntax error.

There is a solution, however: INDEX MATCH. They form a highly versatile tag team, but are worth introducing individually.

### Index

Essentially, **INDEX(array, row\_num,\[column\_num\])** returns a value or the reference to a value from within a table or range (list).

For example, INDEX({7,8,9,10,11,12},3) returns the third item in the list {7,8,9,10,11,12}, i.e. 9. This could have been a range: INDEX(A1:A10,5) gives the value in cell A5, etc.

INDEX can work in two dimensions as well (hence the column\_num reference). Consider the following example:

![](<Base64-Image-Removed>)

Two Dimensional INDEX Example

INDEX(F11:L21,4,5) returns the value in the fourth row, fifth column of the table array F11:L21 (clearly 26 in the above illustration).

### Match

**MATCH(lookup\_value,lookup\_array,\[match\_type\])** returns the relative position of an item in an array that (approximately) matches a specified value. It is not case sensitive.

The third argument, match\_type, does not have to be entered, but for many situations, I strongly recommend that it is specified. It allows one of three values:

*   **match\_type 1 \[default if omitted\]**: finds the largest value less than or equal to the lookup\_value – but the lookup\_array must be in strict ascending order, limiting flexibility;
*   **match\_type 0**: probably the most useful setting, MATCH will find the position of the first value that matches lookup\_value exactly. The lookup\_array can have data in any order and even allows duplicates; and
*   **match type -1**: finds the smallest value greater than or equal to the lookup\_value – but the lookup\_array must be in strict descending order, again limiting flexibility.

When using MATCH, if there is no (approximate) match, #N/A is returned (this may also occur if data is not correctly sorted depending upon match\_type).

MATCH is fairly straightforward to use:

![](<Base64-Image-Removed>)

MATCH Example

In the figure above, MATCH(“d”,F12:F22,0) gives a value of 6, being the relative position of the first ‘d’ in the range. Note that having match\_type 0 here is important. The data contains duplicates and is not sorted alphanumerically. Consequently, match\_types 1 and -1 would give the wrong answer: 7 and #N/A respectively.

### Index Match

Whilst useful functions in their own right, combined they form a highly versatile partnership. Consider our original problem:

![](<Base64-Image-Removed>)

Balance Sheet Summary Illustration (Revisited)

MATCH(1,J28:O28,0) equals 5, i.e. the first period the balance sheet does not balance in is Period 5. But we can do better than that.

INDEX(J6:O6,5) equals May-09, so combining the two functions:

INDEX(J6:O6,MATCH(1,J28:O28,0))

equals May-09 in one step, and answers our reader’s query.

Note how flexible this combination really is. We do not need to specify an order for the lookup range, we can have duplicates and the value to be returned does not have to be in a row / column below / to the right of the lookup range (indeed, it can be in another workbook never mind another worksheet!).

With a little practice, the above technique can be extended to match items on a case sensitive basis, use multiple criteria and even ‘grade’. The [attached Excel file](https://sumproduct.com/assets/thought-files/e-m/sp-index-match-examples.xls)
 provides several examples as illustrations.

If you have a query for this section, please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)
 or visit the website [www.sumproduct.com](https://www.sumproduct.com/)

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/index-match/#0)
    
*   [Register](https://sumproduct.com/thought/index-match/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/index-match/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/index-match/#0)

[](https://sumproduct.com/thought/index-match/#0 "close")

top