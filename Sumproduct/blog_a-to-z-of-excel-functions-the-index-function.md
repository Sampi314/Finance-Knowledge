# A to Z of Excel Functions: The INDEX Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The INDEX Function

*   February 14, 2020

A to Z of Excel Functions: The INDEX Function
=============================================

A to Z of Excel Functions: The INDEX Function
=============================================

15 February 2020

**The INDEX function**

**INDEX** with its best friend **MATCH** – as a combination – are two of the most useful functions at a modeller’s disposal. They provide a versatile lookup in a way that **LOOKUP**, **HLOOKUP** and **VLOOKUP** simply cannot. The best way to illustrate this point is by means of an example.

Here is a common problem. Imagine you have built a financial model and your Balance Sheet – ahem! – contains misbalances. You need to fix it. Now I am sure you have never had this mistake yourself, but you have “close friends” that have encountered this feast of fun: solving Balance Sheet errors can take a _long_ while. One of the first things modellers will do is locate the first period (in ascending order) that has such an error, as identifying the issue in this period may often solve the problem for all periods.

Consider the following example:

![](<Base64-Image-Removed>)

This is a common modelling query. The usual suspects, **LOOKUP** and **HLOOKUP** / **VLOOKUP** do not work here:

*   **LOOKUP(lookup\_value, lookup\_vector, \[result\_vector\])** gives the wrong date as the balance checks are not in strict ascending order (_i.e._ ascending alphanumerically with no duplicates); _whilst_
*   **HLOOKUP(lookup\_value, table\_array, row\_index\_number, \[range\_lookup\])** gives _#VALUE!_ since the first row must contain the data to be ‘looked up’, but the Balance Check is in row 13 in our example above, whereas the dates we need to return are in row 4 – hence we get a syntax error.

There is a solution, however: **INDEX MATCH**. They form a highly versatile tag team, but are worth introducing individually.

**_INDEX_**

Essentially, **INDEX(array, row\_number, \[column\_number\])** returns a value or the reference to a value from within a table or range (list). For example, **INDEX({7,8,9,10,11,12},3)** returns the third item in the list {7,8,9,10,11,12}, _i.e._ 9. This could have been a range: **INDEX(A1:A10,5)** gives the value in cell **A5**, _etc_.

**INDEX** can work in two dimensions as well (hence the **column\_number** reference). Consider the following example:

![](<Base64-Image-Removed>)

**INDEX(F11:L21,4,5)** returns the value in the fourth row, fifth column of the table array **F11:L21** (clearly 26 in the above illustration).

**_MATCH_**

**MATCH(lookup\_value, lookup\_vector, \[match\_type\])** returns the relative position of an item in an array that (approximately) matches a specified value. It is not case sensitive.

The third argument, **match\_type**, does not have to be entered, but for many situations, I strongly recommend that it is specified. It allows one of three values:

*   **match\_type 1 \[default if omitted\]:** finds the largest value less than or equal to the **lookup\_value** – but the **lookup\_vector** must be in strict ascending order, limiting flexibility
*   **match\_type 0:** probably the most useful setting, **MATCH** will find the position of the first value that matches **lookup\_value** exactly. The **lookup\_array** can have data in any order and even allows duplicates
*   **match\_type -1:** finds the smallest value greater than or equal to the **lookup\_value** – but the **lookup\_array** must be in strict descending order, again limiting flexibility.

When using **MATCH**, if there is no (approximate) match, _#N/A_ is returned (this may also occur if data is not correctly sorted depending upon **match\_type**).

**MATCH** is fairly straightforward to use:

![](<Base64-Image-Removed>)

In the figure above, **MATCH(“d”,F12:F22,0)** gives a value of 6, being the relative position of the first ‘d’ in the range. Note that having **match\_type** 0 here is important. The data contains duplicates and is not sorted alphanumerically. Consequently, using **match\_type** 1 and -1 would give the wrong answer: 7 and _#N/A_ respectively.

**_INDEX MATCH_**

Whilst useful functions in their own right, combined they form a highly versatile partnership. Consider the original problem:

![](<Base64-Image-Removed>)

**MATCH(1,J13:O13,0)** equals 5, _i.e._ the first period the balance sheet does not balance in is Period 5. But we can do better than that. **INDEX(J4:O4,5)** equals May-20, so combining the two functions:

**INDEX(J4:O4,MATCH(1,J13:O13,0))**

equals May-20 in one step. This process of stepping out two calculations and then inserting one into another is often referred to as “staggered development”. No, this is not how you construct a financial model late in the evening after having the odd drink or two!

Do note how flexible this combination really is. We do not need to specify an order for the lookup range, we can have duplicates and the value to be returned does not have to be in a row / column below / to the right of the lookup range (indeed, it can be in another workbook never mind another worksheet!). With a little practice, the above technique can be extended to match items on a case sensitive basis, use multiple criteria and even ‘grade’.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/#0 "close")

top