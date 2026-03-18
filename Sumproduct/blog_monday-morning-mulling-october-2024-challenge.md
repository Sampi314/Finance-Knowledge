# Monday Morning Mulling: October 2024 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-october-2024-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: October 2024 Challenge

*   October 27, 2024

Monday Morning Mulling: October 2024 Challenge
==============================================

Monday Morning Mulling: October 2024 Challenge
==============================================

28 October 2024

_On the final Friday of each month, set a challenge in Excel for you to solve over the weekend. On the Monday, we publish one suggested solution. No-one is stating this is the best approach, it’s just the one we selected. If you don’t like it, lump it – or contact us with your preferred solution._

**_The Challenge_**

On Friday, we gave you a straightforward challenge – simply duplicate some values. We wanted you to write a single formula that would duplicate the values from a column in a new column, as shown in the example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/155d9689d7d00f62b198a148209e11bb-1.jpg)

You can download the original question file [here](https://www.sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/October/sp-repeating-values-challenge.xlsx)
. We have a list of values, and we need a single formula that will duplicate each value. Bonus points were available if you could write a formula that gives a configurable number of duplicates.

**_Suggested Solution_**

Whilst there are undoubtedly many solutions to this challenge, we picked one that we found to be concise and flexible (or else it was the first one we thought of…). The formula we came up with is as follows (our values are in the range **C11:C17**):

**\=TEXTSPLIT(CONCAT(REPT(C11:C17&”,”,E8)),,”,”,1)**

![](https://sumproduct.com/wp-content/uploads/2025/05/1f785e59a8062c35113472d45d8b03b1-1.jpg)

This one is all about manipulating text, so we start by using the **REPT** function to repeat the values with an added comma two \[2\] times. We didn’t want to hard-code the two, so we refer to cell **E8**. We can change **E8** to repeat the values any number of times (within a generous limit imposed by Excel regarding string length).

**REPT(C11:C17&”,”,E8)**

As an interim step, it gives an array of the values repeated with commas, as shown here:

![](<Base64-Image-Removed>)

We then use **CONCAT** to join the values in that array.

**CONCAT(REPT(C11:C17&”,”,E8))**

This yields a string with all the repeated values separated by comma as below:

![](<Base64-Image-Removed>)

Finally, we can use **TEXTSPLIT** to create a single column with all the values, one per row. We leave the **col\_delimiter** argument empty, since we don’t want to split it into columns. We specify a comma as the **row\_delimiter** and use 1 in the **ignore\_empty** argument, which prevents it from adding a blank cell to our output from the trailing comma on the last value in the list.

**\=TEXTSPLIT(CONCAT(REPT(C11:C17&”,”,E8)),,”,”,1)**

![](<Base64-Image-Removed>)

You can download our solution file [here](https://www.sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/October/sp-repeating-values-solution.xlsx)
.

_The Final Friday Fix will return on Friday 29 November 2024 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-october-2024-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-october-2024-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-october-2024-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-october-2024-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-october-2024-challenge/#0 "close")

top